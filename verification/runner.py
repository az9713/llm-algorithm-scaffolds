"""
Test runner for scaffold verification.

Orchestrates LLM calls, validation, and result collection.
"""

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .config import get_settings
from .generators.base import TestCase, TestSuite
from .llm.base import LLMRequest, LLMResponse
from .llm.claude import ClaudeProvider
from .llm.prompt_builder import PromptBuilder, ScaffoldParser
from .llm.response_parser import ParsedAnswer, ResponseParser
from .validators.base import ValidationResult

logger = logging.getLogger(__name__)


@dataclass
class TestResult:
    """Result of running a single test case."""

    test_case: TestCase
    """The test case that was run."""

    llm_response: LLMResponse | None = None
    """Raw LLM response."""

    parsed_answer: ParsedAnswer | None = None
    """Parsed answer from LLM."""

    validation_result: ValidationResult | None = None
    """Validation result."""

    error: str | None = None
    """Error message if test failed to run."""

    duration_ms: float = 0.0
    """Time taken for this test."""

    @property
    def passed(self) -> bool:
        """Check if test passed."""
        return (
            self.validation_result is not None
            and self.validation_result.is_valid
            and self.error is None
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "test_case_id": self.test_case.id,
            "passed": self.passed,
            "error": self.error,
            "duration_ms": self.duration_ms,
            "validation": self.validation_result.to_dict() if self.validation_result else None,
            "llm_tokens": {
                "input": self.llm_response.input_tokens if self.llm_response else 0,
                "output": self.llm_response.output_tokens if self.llm_response else 0,
            },
        }


@dataclass
class ScaffoldResults:
    """Results for all tests of a single scaffold."""

    scaffold: str
    """Scaffold name."""

    model: str
    """Model used for testing."""

    test_results: list[TestResult] = field(default_factory=list)
    """Individual test results."""

    started_at: datetime = field(default_factory=datetime.now)
    """When testing started."""

    completed_at: datetime | None = None
    """When testing completed."""

    @property
    def total_tests(self) -> int:
        return len(self.test_results)

    @property
    def passed_tests(self) -> int:
        return sum(1 for r in self.test_results if r.passed)

    @property
    def pass_rate(self) -> float:
        if self.total_tests == 0:
            return 0.0
        return self.passed_tests / self.total_tests

    @property
    def total_tokens(self) -> int:
        return sum(
            (r.llm_response.total_tokens if r.llm_response else 0)
            for r in self.test_results
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "scaffold": self.scaffold,
            "model": self.model,
            "summary": {
                "total_tests": self.total_tests,
                "passed_tests": self.passed_tests,
                "pass_rate": self.pass_rate,
                "total_tokens": self.total_tokens,
            },
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "results": [r.to_dict() for r in self.test_results],
        }


class VerificationRunner:
    """Runs verification tests for scaffolds."""

    def __init__(
        self,
        llm_provider: ClaudeProvider | None = None,
        scaffolds_dir: Path | None = None,
    ):
        """
        Initialize the verification runner.

        Args:
            llm_provider: LLM provider to use. Creates default if not provided.
            scaffolds_dir: Directory containing scaffolds.
        """
        self.settings = get_settings()
        self.llm = llm_provider or ClaudeProvider()
        self.scaffolds_dir = scaffolds_dir or self.settings.get_scaffolds_path()
        self.prompt_builder = PromptBuilder()
        self.response_parser = ResponseParser()

    async def run_test_case(
        self,
        scaffold_path: Path,
        test_case: TestCase,
        validator: Any,
    ) -> TestResult:
        """
        Run a single test case.

        Args:
            scaffold_path: Path to scaffold markdown file.
            test_case: Test case to run.
            validator: Validator to use for checking results.

        Returns:
            TestResult with outcome.
        """
        import time

        start_time = time.perf_counter()

        try:
            # Parse scaffold and build prompt
            scaffold = self.prompt_builder.parser.parse_file(scaffold_path)
            prompt = self.prompt_builder.build_prompt(scaffold, test_case.input)
            system_prompt = self.prompt_builder.build_system_prompt()

            # Call LLM
            request = LLMRequest(
                prompt=prompt,
                system_prompt=system_prompt,
                temperature=self.settings.temperature,
                max_tokens=self.settings.max_tokens,
            )

            response = await self.llm.generate_with_retry(
                request,
                max_retries=self.settings.max_retries,
            )

            # Parse response
            parsed = self.response_parser.parse(response.content, test_case.scaffold)

            # Validate
            if parsed.is_valid:
                validation = validator.validate(
                    test_case.expected,
                    parsed.answer,
                )
            else:
                validation = ValidationResult(
                    is_valid=False,
                    score=0.0,
                    message=f"Failed to parse LLM response: {parsed.parse_error}",
                    expected=test_case.expected,
                    actual=None,
                )

            elapsed_ms = (time.perf_counter() - start_time) * 1000

            return TestResult(
                test_case=test_case,
                llm_response=response,
                parsed_answer=parsed,
                validation_result=validation,
                duration_ms=elapsed_ms,
            )

        except Exception as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            logger.error(f"Error running test case {test_case.id}: {e}")

            return TestResult(
                test_case=test_case,
                error=str(e),
                duration_ms=elapsed_ms,
            )

    async def run_test_suite(
        self,
        scaffold_name: str,
        test_suite: TestSuite,
        validator: Any,
    ) -> ScaffoldResults:
        """
        Run all tests in a test suite.

        Args:
            scaffold_name: Name of the scaffold.
            test_suite: Test suite to run.
            validator: Validator to use.

        Returns:
            ScaffoldResults with all test outcomes.
        """
        # Find scaffold file
        scaffold_path = self._find_scaffold_file(scaffold_name)
        if scaffold_path is None:
            results = ScaffoldResults(
                scaffold=scaffold_name,
                model=self.settings.active_model,
            )
            for tc in test_suite.test_cases:
                results.test_results.append(TestResult(
                    test_case=tc,
                    error=f"Scaffold file not found: {scaffold_name}",
                ))
            results.completed_at = datetime.now()
            return results

        results = ScaffoldResults(
            scaffold=scaffold_name,
            model=self.settings.active_model,
        )

        # Run tests (sequentially to avoid rate limits)
        for test_case in test_suite.test_cases:
            result = await self.run_test_case(scaffold_path, test_case, validator)
            results.test_results.append(result)
            logger.info(
                f"Test {test_case.id}: {'PASS' if result.passed else 'FAIL'}"
            )

        results.completed_at = datetime.now()
        return results

    def _find_scaffold_file(self, scaffold_name: str) -> Path | None:
        """Find scaffold file by name."""
        # Search in category directories
        for category_dir in self.scaffolds_dir.iterdir():
            if category_dir.is_dir():
                scaffold_file = category_dir / f"{scaffold_name}.md"
                if scaffold_file.exists():
                    return scaffold_file

        return None

    def save_results(self, results: ScaffoldResults, output_dir: Path) -> Path:
        """Save results to JSON file."""
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{results.scaffold}_{results.model.replace('/', '_')}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results.to_dict(), f, indent=2)

        return output_file


def run_verification(
    scaffold_name: str,
    test_suite: TestSuite,
    validator: Any,
) -> ScaffoldResults:
    """
    Synchronous wrapper for running verification.

    Args:
        scaffold_name: Name of the scaffold.
        test_suite: Test suite to run.
        validator: Validator to use.

    Returns:
        ScaffoldResults with all test outcomes.
    """
    runner = VerificationRunner()
    return asyncio.run(runner.run_test_suite(scaffold_name, test_suite, validator))
