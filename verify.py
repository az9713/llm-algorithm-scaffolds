#!/usr/bin/env python3
"""
Scaffold Verification Tool - Main Entry Point

This script provides fully automated verification of algorithm scaffolds.
No coding required - just run the commands.

QUICK START:
    1. Install dependencies:
       pip install -r requirements-verification.txt

    2. Set your API key:
       export ANTHROPIC_API_KEY=your_key_here
       (or create a .env file with VERIFY_ANTHROPIC_API_KEY=your_key)

    3. Run verification:
       python verify.py                    # Verify all scaffolds
       python verify.py dijkstra           # Verify specific scaffold
       python verify.py --category graph   # Verify a category

COMMANDS:
    python verify.py                       # Verify all 33 scaffolds
    python verify.py list                  # Show available scaffolds
    python verify.py dijkstra bfs          # Verify specific scaffolds
    python verify.py --category graph      # Verify all graph algorithms
    python verify.py --mode cert           # Use Opus for final certification
    python verify.py report                # Regenerate reports from results

OPTIONS:
    --mode dev   Use Claude Haiku (faster, cheaper) - DEFAULT
    --mode cert  Use Claude Opus (final certification)
    --category   Verify all scaffolds in a category

CATEGORIES:
    graph, divide_conquer, greedy, backtracking,
    dynamic_programming, optimization, string, numerical

OUTPUT:
    Results are saved to verification_results/
    - data/          JSON results for each scaffold
    - reports/       Markdown certification reports

EXAMPLES:
    # Quick test with one scaffold
    python verify.py dijkstra

    # Verify all graph algorithms
    python verify.py --category graph

    # Full certification with Opus
    python verify.py --mode cert

    # Regenerate reports from existing results
    python verify.py report
"""

import sys
import os

# Add parent directory to path if running directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verification.cli import main, VerificationCLI, print_header
from verification.registry import SCAFFOLD_REGISTRY


def show_quick_help():
    """Show quick usage help."""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║         ALGORITHMIC SCAFFOLDING VERIFICATION TOOL                ║
╚══════════════════════════════════════════════════════════════════╝

QUICK START:
  1. Set API key:  export ANTHROPIC_API_KEY=your_key
  2. Run:          python verify.py dijkstra

USAGE:
  python verify.py                    Verify ALL scaffolds
  python verify.py list               Show available scaffolds
  python verify.py <scaffold>         Verify specific scaffold
  python verify.py --category graph   Verify a category
  python verify.py --mode cert        Use Opus (final certification)
  python verify.py report             Generate reports

For full help: python verify.py --help
""")


if __name__ == "__main__":
    # Handle special case: no args shows quick help
    if len(sys.argv) == 1:
        show_quick_help()
        print("\nNo command specified. Run 'python verify.py list' to see scaffolds")
        print("or 'python verify.py --help' for full usage.\n")
        sys.exit(0)

    # Handle 'list' as a positional arg (convenience)
    if len(sys.argv) == 2 and sys.argv[1] == "list":
        cli = VerificationCLI()
        cli.list_scaffolds()
        sys.exit(0)

    # Handle single scaffold name without 'verify' command
    if len(sys.argv) >= 2 and sys.argv[1] in sum(SCAFFOLD_REGISTRY.values(), []):
        # User typed: python verify.py dijkstra
        # Convert to: python verify.py verify dijkstra
        sys.argv.insert(1, "verify")

    # Handle 'report' without verify command
    if len(sys.argv) == 2 and sys.argv[1] == "report":
        pass  # Let main() handle it

    # Handle no command but has flags
    if len(sys.argv) >= 2 and sys.argv[1].startswith("--"):
        # User typed: python verify.py --category graph
        # Convert to: python verify.py verify --category graph
        sys.argv.insert(1, "verify")

    main()
