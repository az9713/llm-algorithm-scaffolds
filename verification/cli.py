#!/usr/bin/env python3
"""
Verification CLI - Fully automated scaffold verification.

Usage:
    python -m verification.cli verify              # Verify all scaffolds
    python -m verification.cli verify dijkstra     # Verify single scaffold
    python -m verification.cli verify --category graph  # Verify category
    python -m verification.cli report              # Generate reports from results
    python -m verification.cli list                # List available scaffolds
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from .config import get_settings, Settings
from .registry import get_all_generators, get_validator_for_scaffold, SCAFFOLD_REGISTRY
from .runner import VerificationRunner, ScaffoldResults
from .reports.generator import get_report_generator


def print_header(text: str) -> None:
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_progress(current: int, total: int, name: str, status: str) -> None:
    """Print progress indicator."""
    bar_width = 30
    filled = int(bar_width * current / total)
    bar = "#" * filled + "-" * (bar_width - filled)
    print(f"\r[{bar}] {current}/{total} {name}: {status}", end="", flush=True)


def print_results_table(results: list[ScaffoldResults]) -> None:
    """Print results as a formatted table."""
    print("\n" + "-" * 70)
    print(f"{'Scaffold':<25} {'Passed':<12} {'Rate':<10} {'Status':<15}")
    print("-" * 70)

    for r in sorted(results, key=lambda x: x.scaffold):
        rate = r.pass_rate * 100
        if rate >= 90:
            status = "[OK] CERTIFIED"
        elif rate >= 50:
            status = "[..] PARTIAL"
        else:
            status = "[XX] FAILED"

        print(f"{r.scaffold:<25} {r.passed_tests}/{r.total_tests:<9} {rate:>5.1f}%    {status}")

    print("-" * 70)


class VerificationCLI:
    """Command-line interface for scaffold verification."""

    def __init__(self):
        self.settings = get_settings()
        self.results_dir = self.settings.get_results_path()
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def list_scaffolds(self) -> None:
        """List all available scaffolds."""
        print_header("Available Scaffolds")

        for category, scaffolds in SCAFFOLD_REGISTRY.items():
            print(f"\n{category.upper()}:")
            for scaffold in scaffolds:
                print(f"  - {scaffold}")

        print(f"\nTotal: {sum(len(s) for s in SCAFFOLD_REGISTRY.values())} scaffolds")

    async def verify_scaffold(
        self,
        scaffold_name: str,
        runner: VerificationRunner,
    ) -> ScaffoldResults | None:
        """Verify a single scaffold."""
        generators = get_all_generators()

        if scaffold_name not in generators:
            print(f"  Warning: No test generator for '{scaffold_name}', skipping")
            return None

        generator = generators[scaffold_name]
        validator = get_validator_for_scaffold(scaffold_name)

        # Generate test suite
        test_suite = generator.generate_suite()

        # Run verification
        results = await runner.run_test_suite(
            scaffold_name=scaffold_name,
            test_suite=test_suite,
            validator=validator,
        )

        # Save results
        results_file = self.results_dir / "data" / f"{scaffold_name}.json"
        results_file.parent.mkdir(parents=True, exist_ok=True)
        with open(results_file, "w") as f:
            json.dump(results.to_dict(), f, indent=2, default=str)

        return results

    async def verify_all(
        self,
        scaffolds: list[str] | None = None,
        category: str | None = None,
    ) -> list[ScaffoldResults]:
        """Verify multiple scaffolds."""
        # Determine which scaffolds to verify
        if scaffolds:
            to_verify = scaffolds
        elif category:
            to_verify = SCAFFOLD_REGISTRY.get(category, [])
            if not to_verify:
                print(f"Error: Unknown category '{category}'")
                print(f"Available: {', '.join(SCAFFOLD_REGISTRY.keys())}")
                return []
        else:
            to_verify = [s for scaffolds in SCAFFOLD_REGISTRY.values() for s in scaffolds]

        print_header(f"Verifying {len(to_verify)} Scaffolds")
        print(f"Model: {self.settings.active_model}")
        print(f"Mode: {self.settings.current_mode}")

        # Check API key
        if not self.settings.anthropic_api_key:
            print("\nError: ANTHROPIC_API_KEY not set")
            print("Set it via environment variable or .env file:")
            print("  export VERIFY_ANTHROPIC_API_KEY=your_key")
            return []

        runner = VerificationRunner()
        all_results = []

        for i, scaffold_name in enumerate(to_verify, 1):
            print(f"\n[{i}/{len(to_verify)}] Verifying: {scaffold_name}")

            try:
                results = await self.verify_scaffold(scaffold_name, runner)
                if results:
                    all_results.append(results)
                    status = "PASS" if results.pass_rate >= 0.9 else "PARTIAL" if results.pass_rate >= 0.5 else "FAIL"
                    print(f"  Result: {results.passed_tests}/{results.total_tests} passed ({results.pass_rate*100:.1f}%) - {status}")
            except Exception as e:
                print(f"  Error: {e}")

        # Print summary
        if all_results:
            print_header("Verification Summary")
            print_results_table(all_results)

            total = len(all_results)
            certified = sum(1 for r in all_results if r.pass_rate >= 0.9)
            partial = sum(1 for r in all_results if 0.5 <= r.pass_rate < 0.9)
            failed = sum(1 for r in all_results if r.pass_rate < 0.5)

            print(f"\nCertified: {certified}/{total}")
            print(f"Partial:   {partial}/{total}")
            print(f"Failed:    {failed}/{total}")

            # Generate reports
            self.generate_reports(all_results)

        return all_results

    def generate_reports(self, results: list[ScaffoldResults]) -> None:
        """Generate certification reports."""
        print_header("Generating Reports")

        report_gen = get_report_generator()
        reports_dir = self.results_dir / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)

        # Individual scaffold reports
        for r in results:
            report_path = reports_dir / f"{r.scaffold}_report.md"
            report_gen.generate_scaffold_report(r, report_path)
            print(f"  Created: {report_path.name}")

        # Summary report
        summary_path = reports_dir / "CERTIFICATION_SUMMARY.md"
        report_gen.generate_summary_report(results, summary_path)
        print(f"  Created: {summary_path.name}")

        print(f"\nReports saved to: {reports_dir}")

    def load_existing_results(self) -> list[ScaffoldResults]:
        """Load results from previous runs."""
        results = []
        data_dir = self.results_dir / "data"

        if not data_dir.exists():
            return results

        for json_file in data_dir.glob("*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)

                from .runner import ScaffoldResults, TestResult
                from .generators.base import TestCase
                from .validators.base import ValidationResult

                # Parse timestamps
                started_at = datetime.fromisoformat(data.get("started_at", datetime.now().isoformat()))
                completed_at = datetime.fromisoformat(data.get("completed_at", datetime.now().isoformat())) if data.get("completed_at") else None

                sr = ScaffoldResults(
                    scaffold=data["scaffold"],
                    model=data["model"],
                    started_at=started_at,
                    completed_at=completed_at,
                )

                # Reconstruct TestResult objects from JSON
                test_results = []
                for r in data.get("results", []):
                    # Determine tier from test case ID (e.g., "bfs_simple_01" -> "simple")
                    test_id = r.get("test_case_id", "unknown")
                    tier = "standard"
                    for t in ["simple", "standard", "edge"]:
                        if f"_{t}_" in test_id:
                            tier = t
                            break

                    # Create TestCase
                    test_case = TestCase(
                        id=test_id,
                        scaffold=data["scaffold"],
                        tier=tier,
                        input={},
                        expected=r.get("validation", {}).get("expected", {}),
                        description=f"Test case {test_id}",
                    )

                    # Create ValidationResult
                    validation_data = r.get("validation", {})
                    validation_result = None
                    if validation_data:
                        validation_result = ValidationResult(
                            is_valid=validation_data.get("is_valid", False),
                            score=validation_data.get("score", 0.0),
                            message=validation_data.get("message", ""),
                            expected=validation_data.get("expected"),
                            actual=validation_data.get("actual"),
                            details=validation_data.get("details", {}),
                        )

                    # Create TestResult
                    test_result = TestResult(
                        test_case=test_case,
                        validation_result=validation_result,
                        error=r.get("error"),
                        duration_ms=r.get("duration_ms", 0.0),
                    )
                    test_results.append(test_result)

                sr.test_results = test_results
                results.append(sr)

            except Exception as e:
                print(f"Warning: Could not load {json_file}: {e}")

        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Algorithmic Scaffolding Verification Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m verification.cli list                    # List all scaffolds
  python -m verification.cli verify                  # Verify all scaffolds
  python -m verification.cli verify dijkstra bfs     # Verify specific scaffolds
  python -m verification.cli verify --category graph # Verify a category
  python -m verification.cli verify --mode cert      # Use certification model (Opus)
  python -m verification.cli report                  # Regenerate reports
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # List command
    list_parser = subparsers.add_parser("list", help="List available scaffolds")

    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify scaffolds")
    verify_parser.add_argument(
        "scaffolds",
        nargs="*",
        help="Specific scaffolds to verify (default: all)"
    )
    verify_parser.add_argument(
        "--category", "-c",
        choices=["graph", "divide_conquer", "greedy", "backtracking",
                 "dynamic_programming", "optimization", "string", "numerical"],
        help="Verify all scaffolds in a category"
    )
    verify_parser.add_argument(
        "--mode", "-m",
        choices=["dev", "cert"],
        default="dev",
        help="Mode: 'dev' uses Haiku (faster/cheaper), 'cert' uses Opus (final certification)"
    )

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate reports from existing results")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    cli = VerificationCLI()

    if args.command == "list":
        cli.list_scaffolds()

    elif args.command == "verify":
        # Update mode if specified
        if hasattr(args, "mode"):
            cli.settings.current_mode = args.mode

        asyncio.run(cli.verify_all(
            scaffolds=args.scaffolds if args.scaffolds else None,
            category=args.category,
        ))

    elif args.command == "report":
        results = cli.load_existing_results()
        if results:
            cli.generate_reports(results)
        else:
            print("No existing results found. Run 'verify' first.")


if __name__ == "__main__":
    main()
