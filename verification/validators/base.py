"""
Base validator interface and common validation utilities.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ValidationResult:
    """Result of validating LLM output against ground truth."""

    is_valid: bool
    """Whether the output is considered correct."""

    score: float = 1.0
    """Correctness score from 0.0 to 1.0."""

    message: str = ""
    """Explanation of validation result."""

    expected: Any = None
    """Expected value."""

    actual: Any = None
    """Actual value from LLM."""

    details: dict[str, Any] = field(default_factory=dict)
    """Additional validation details."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for reporting."""
        return {
            "is_valid": self.is_valid,
            "score": self.score,
            "message": self.message,
            "expected": self.expected,
            "actual": self.actual,
            "details": self.details,
        }


class Validator(ABC):
    """Abstract base class for validators."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of this validator."""
        pass

    @abstractmethod
    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Validate actual output against expected value.

        Args:
            expected: Ground truth value.
            actual: Value from LLM.
            **kwargs: Additional validation parameters.

        Returns:
            ValidationResult with validation outcome.
        """
        pass

    def _normalize_value(self, value: Any) -> Any:
        """Normalize a value for comparison."""
        if isinstance(value, str):
            return value.strip()
        if isinstance(value, (list, tuple)):
            return [self._normalize_value(v) for v in value]
        if isinstance(value, dict):
            return {k: self._normalize_value(v) for k, v in value.items()}
        return value


class CompositeValidator(Validator):
    """Validator that combines multiple validators."""

    def __init__(self, validators: list[Validator], mode: str = "all"):
        """
        Initialize composite validator.

        Args:
            validators: List of validators to apply.
            mode: "all" requires all to pass, "any" requires at least one.
        """
        self._validators = validators
        self._mode = mode

    @property
    def name(self) -> str:
        return f"composite({self._mode})"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """Apply all validators and combine results."""
        results = []
        for validator in self._validators:
            result = validator.validate(expected, actual, **kwargs)
            results.append(result)

        if self._mode == "all":
            is_valid = all(r.is_valid for r in results)
            score = sum(r.score for r in results) / len(results) if results else 0.0
        else:  # "any"
            is_valid = any(r.is_valid for r in results)
            score = max(r.score for r in results) if results else 0.0

        messages = [r.message for r in results if r.message]

        return ValidationResult(
            is_valid=is_valid,
            score=score,
            message="; ".join(messages),
            expected=expected,
            actual=actual,
            details={"sub_results": [r.to_dict() for r in results]},
        )
