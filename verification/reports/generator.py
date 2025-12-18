"""
Certification report generator.

Generates markdown reports from verification results.
"""

from datetime import datetime
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..runner import ScaffoldResults


class ReportGenerator:
    """Generates certification reports from verification results."""

    def __init__(self, templates_dir: Path | None = None):
        """
        Initialize report generator.

        Args:
            templates_dir: Directory containing Jinja2 templates.
        """
        if templates_dir is None:
            templates_dir = Path(__file__).parent / "templates"

        self.templates_dir = templates_dir
        self.env = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(["html", "xml"]),
        )

    def generate_scaffold_report(
        self,
        results: ScaffoldResults,
        output_path: Path,
    ) -> Path:
        """
        Generate report for a single scaffold.

        Args:
            results: Scaffold verification results.
            output_path: Path to write report.

        Returns:
            Path to generated report.
        """
        template = self.env.get_template("scaffold_report.md.j2")

        # Organize results by tier
        by_tier = {"simple": [], "standard": [], "edge": []}
        for result in results.test_results:
            tier = result.test_case.tier
            if tier in by_tier:
                by_tier[tier].append(result)

        report = template.render(
            scaffold=results.scaffold,
            model=results.model,
            total_tests=results.total_tests,
            passed_tests=results.passed_tests,
            pass_rate=results.pass_rate * 100,
            total_tokens=results.total_tokens,
            started_at=results.started_at,
            completed_at=results.completed_at,
            results_by_tier=by_tier,
            generated_at=datetime.now().isoformat(),
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")

        return output_path

    def generate_summary_report(
        self,
        all_results: list[ScaffoldResults],
        output_path: Path,
    ) -> Path:
        """
        Generate summary report for all scaffolds.

        Args:
            all_results: List of scaffold results.
            output_path: Path to write report.

        Returns:
            Path to generated report.
        """
        template = self.env.get_template("summary.md.j2")

        # Calculate aggregate stats
        total_scaffolds = len(all_results)
        certified = sum(1 for r in all_results if r.pass_rate >= 0.9)
        partial = sum(1 for r in all_results if 0.5 <= r.pass_rate < 0.9)
        failed = sum(1 for r in all_results if r.pass_rate < 0.5)

        total_tests = sum(r.total_tests for r in all_results)
        total_passed = sum(r.passed_tests for r in all_results)
        overall_pass_rate = total_passed / total_tests if total_tests > 0 else 0

        report = template.render(
            total_scaffolds=total_scaffolds,
            certified=certified,
            partial=partial,
            failed=failed,
            total_tests=total_tests,
            total_passed=total_passed,
            overall_pass_rate=overall_pass_rate * 100,
            scaffolds=sorted(all_results, key=lambda r: -r.pass_rate),
            generated_at=datetime.now().isoformat(),
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")

        return output_path


# Create default templates
def create_default_templates(templates_dir: Path) -> None:
    """Create default Jinja2 templates if they don't exist."""
    templates_dir.mkdir(parents=True, exist_ok=True)

    scaffold_template = """# Scaffold Verification Report: {{ scaffold }}

## Summary

- **Status:** {% if pass_rate >= 90 %}CERTIFIED{% elif pass_rate >= 50 %}PARTIAL{% else %}FAILED{% endif %}
- **Model:** {{ model }}
- **Test Date:** {{ started_at.strftime('%Y-%m-%d %H:%M') }}
- **Pass Rate:** {{ "%.1f"|format(pass_rate) }}% ({{ passed_tests }}/{{ total_tests }})
- **Total Tokens:** {{ total_tokens }}

## Test Results by Tier

### Simple Cases
{% for result in results_by_tier.simple %}
- [{{ "PASS" if result.passed else "FAIL" }}] {{ result.test_case.id }}: {{ result.test_case.description }}
{% endfor %}

### Standard Cases
{% for result in results_by_tier.standard %}
- [{{ "PASS" if result.passed else "FAIL" }}] {{ result.test_case.id }}: {{ result.test_case.description }}
{% endfor %}

### Edge Cases
{% for result in results_by_tier.edge %}
- [{{ "PASS" if result.passed else "FAIL" }}] {{ result.test_case.id }}: {{ result.test_case.description }}
{% endfor %}

## Failure Analysis

{% for result in results_by_tier.simple + results_by_tier.standard + results_by_tier.edge %}
{% if not result.passed %}
### {{ result.test_case.id }}
- **Error:** {{ result.error or result.validation_result.message if result.validation_result else "Unknown" }}
- **Expected:** {{ result.test_case.expected }}
- **Actual:** {{ result.parsed_answer.answer if result.parsed_answer else "N/A" }}
{% endif %}
{% endfor %}

---

Generated with [Claude Code](https://claude.com/claude-code) on {{ generated_at }}
"""

    summary_template = """# Algorithmic Scaffolding Certification Report

## Executive Summary

- **Date:** {{ generated_at[:10] }}
- **Total Scaffolds:** {{ total_scaffolds }}
- **Fully Certified:** {{ certified }}
- **Partially Certified:** {{ partial }}
- **Failed:** {{ failed }}
- **Overall Pass Rate:** {{ "%.1f"|format(overall_pass_rate) }}%

## Certification Matrix

| Scaffold | Pass Rate | Status |
|----------|-----------|--------|
{% for scaffold in scaffolds %}
| {{ scaffold.scaffold }} | {{ "%.1f"|format(scaffold.pass_rate * 100) }}% | {% if scaffold.pass_rate >= 0.9 %}CERTIFIED{% elif scaffold.pass_rate >= 0.5 %}PARTIAL{% else %}FAILED{% endif %} |
{% endfor %}

## Methodology

Tests were conducted using:
- Model: {{ scaffolds[0].model if scaffolds else "N/A" }}
- Test cases per scaffold: {{ (total_tests / total_scaffolds)|int if total_scaffolds > 0 else 0 }}
- Validation: Reference implementations using trusted libraries (networkx, numpy, scipy)

## Recommendations

{% if failed > 0 %}
### Scaffolds Requiring Attention
{% for scaffold in scaffolds if scaffold.pass_rate < 0.5 %}
- **{{ scaffold.scaffold }}**: {{ "%.1f"|format(scaffold.pass_rate * 100) }}% pass rate
{% endfor %}
{% endif %}

---

Generated with [Claude Code](https://claude.com/claude-code) on {{ generated_at }}
"""

    (templates_dir / "scaffold_report.md.j2").write_text(scaffold_template, encoding="utf-8")
    (templates_dir / "summary.md.j2").write_text(summary_template, encoding="utf-8")


def get_report_generator() -> ReportGenerator:
    """Factory function that ensures templates exist."""
    templates_dir = Path(__file__).parent / "templates"
    create_default_templates(templates_dir)
    return ReportGenerator(templates_dir)
