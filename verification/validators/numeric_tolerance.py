"""
Numeric tolerance validator for floating-point comparisons.
"""

import math
from typing import Any

from .base import ValidationResult, Validator


class NumericToleranceValidator(Validator):
    """Validator for numeric values with tolerance."""

    def __init__(
        self,
        absolute_tolerance: float = 1e-9,
        relative_tolerance: float = 1e-6,
    ):
        """
        Initialize with tolerance values.

        Args:
            absolute_tolerance: Absolute tolerance for comparison.
            relative_tolerance: Relative tolerance for comparison.
        """
        self.absolute_tolerance = absolute_tolerance
        self.relative_tolerance = relative_tolerance

    @property
    def name(self) -> str:
        return "numeric_tolerance"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check numeric equality within tolerance.

        Uses: |expected - actual| <= atol + rtol * |expected|

        Args:
            expected: Expected numeric value.
            actual: Actual numeric value from LLM.
            **kwargs: Optional overrides for atol, rtol.

        Returns:
            ValidationResult with validation outcome.
        """
        atol = kwargs.get("absolute_tolerance", self.absolute_tolerance)
        rtol = kwargs.get("relative_tolerance", self.relative_tolerance)

        # Handle None
        if actual is None:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message="Actual value is None",
                expected=expected,
                actual=actual,
            )

        # Try to convert to float
        try:
            expected_f = float(expected)
            actual_f = float(actual)
        except (TypeError, ValueError) as e:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Cannot convert to float: {e}",
                expected=expected,
                actual=actual,
            )

        # Handle special cases
        if math.isnan(expected_f) and math.isnan(actual_f):
            return ValidationResult(
                is_valid=True,
                score=1.0,
                message="Both NaN",
                expected=expected,
                actual=actual,
            )

        if math.isinf(expected_f) and math.isinf(actual_f):
            # Same sign infinity
            is_valid = (expected_f > 0) == (actual_f > 0)
            return ValidationResult(
                is_valid=is_valid,
                score=1.0 if is_valid else 0.0,
                message="" if is_valid else "Infinity sign mismatch",
                expected=expected,
                actual=actual,
            )

        # Standard tolerance check
        diff = abs(expected_f - actual_f)
        threshold = atol + rtol * abs(expected_f)
        is_valid = diff <= threshold

        if is_valid:
            return ValidationResult(
                is_valid=True,
                score=1.0,
                message="",
                expected=expected,
                actual=actual,
            )
        else:
            # Calculate partial score based on how close
            if abs(expected_f) > 1e-10:
                relative_error = diff / abs(expected_f)
                score = max(0.0, 1.0 - relative_error)
            else:
                score = 0.0

            return ValidationResult(
                is_valid=False,
                score=score,
                message=f"Difference {diff} exceeds tolerance {threshold}",
                expected=expected,
                actual=actual,
                details={
                    "difference": diff,
                    "threshold": threshold,
                    "relative_error": diff / abs(expected_f) if abs(expected_f) > 1e-10 else float("inf"),
                },
            )


class RootValidator(Validator):
    """Validator for root-finding results."""

    def __init__(self, tolerance: float = 1e-6):
        self.tolerance = tolerance

    @property
    def name(self) -> str:
        return "root_validator"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Validate root by checking f(root) ≈ 0.

        Args:
            expected: Expected root value or dict with "root" key.
            actual: Actual root from LLM or dict with "root" key.
            **kwargs: Must include 'function' to evaluate.

        Returns:
            ValidationResult with validation outcome.
        """
        # Extract root from dict if wrapped
        if isinstance(expected, dict) and "root" in expected:
            expected = expected["root"]
        if isinstance(actual, dict) and "root" in actual:
            actual = actual["root"]

        f = kwargs.get("function")
        if f is None:
            # Fall back to numeric comparison
            validator = NumericToleranceValidator(self.tolerance, self.tolerance)
            return validator.validate(expected, actual)

        try:
            actual_f = float(actual)
            residual = abs(f(actual_f))
        except (TypeError, ValueError) as e:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Cannot evaluate function: {e}",
                expected=expected,
                actual=actual,
            )

        is_valid = residual <= self.tolerance

        return ValidationResult(
            is_valid=is_valid,
            score=1.0 if is_valid else max(0.0, 1.0 - residual),
            message="" if is_valid else f"f(root) = {residual} exceeds tolerance",
            expected=expected,
            actual=actual,
            details={"residual": residual},
        )


class OptimizationValidator(Validator):
    """Validator for optimization results (value within bounds of optimum)."""

    def __init__(self, tolerance_percent: float = 5.0):
        """
        Initialize with tolerance percentage.

        Args:
            tolerance_percent: How far from optimum is acceptable (percentage).
        """
        self.tolerance_percent = tolerance_percent

    @property
    def name(self) -> str:
        return "optimization_validator"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Validate optimization result is within bounds of optimum.

        Args:
            expected: Expected optimal value.
            actual: Actual value from LLM.
            **kwargs: Optional parameters:
                - minimize: If True, actual should be <= expected * (1 + tol).
                - tolerance_percent: Override default tolerance.

        Returns:
            ValidationResult with validation outcome.
        """
        minimize = kwargs.get("minimize", True)
        tol_pct = kwargs.get("tolerance_percent", self.tolerance_percent)

        try:
            expected_f = float(expected)
            actual_f = float(actual)
        except (TypeError, ValueError) as e:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Cannot convert to float: {e}",
                expected=expected,
                actual=actual,
            )

        if abs(expected_f) < 1e-10:
            # Near-zero expected, use absolute tolerance
            threshold = tol_pct / 100.0
            is_valid = abs(actual_f) <= threshold
        else:
            # Relative tolerance
            threshold = abs(expected_f) * (tol_pct / 100.0)

            if minimize:
                # For minimization, actual should not be much worse than expected
                is_valid = actual_f <= expected_f + threshold
            else:
                # For maximization, actual should not be much worse than expected
                is_valid = actual_f >= expected_f - threshold

        if is_valid:
            return ValidationResult(
                is_valid=True,
                score=1.0,
                message="",
                expected=expected,
                actual=actual,
            )
        else:
            # Calculate how far off
            diff = abs(actual_f - expected_f)
            relative_diff = diff / abs(expected_f) if abs(expected_f) > 1e-10 else float("inf")

            return ValidationResult(
                is_valid=False,
                score=max(0.0, 1.0 - relative_diff),
                message=f"Value {actual_f} exceeds {tol_pct}% tolerance from optimal {expected_f}",
                expected=expected,
                actual=actual,
                details={
                    "difference": diff,
                    "relative_difference": relative_diff,
                    "tolerance_percent": tol_pct,
                },
            )


def get_numeric_tolerance_validator(
    absolute_tolerance: float = 1e-9,
    relative_tolerance: float = 1e-6,
) -> NumericToleranceValidator:
    """Factory function."""
    return NumericToleranceValidator(absolute_tolerance, relative_tolerance)


def get_root_validator(tolerance: float = 1e-6) -> RootValidator:
    """Factory function."""
    return RootValidator(tolerance)


def get_optimization_validator(tolerance_percent: float = 5.0) -> OptimizationValidator:
    """Factory function."""
    return OptimizationValidator(tolerance_percent)
