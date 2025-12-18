"""
Exact match validator for deterministic algorithm outputs.
"""

from typing import Any

from .base import ValidationResult, Validator


class ExactMatchValidator(Validator):
    """Validator for exact equality of values."""

    @property
    def name(self) -> str:
        return "exact_match"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check for exact equality.

        Args:
            expected: Ground truth value.
            actual: Value from LLM.
            **kwargs: Optional parameters:
                - normalize: If True, normalize strings/lists before comparison.
                - ignore_order: If True, compare lists as sets.

        Returns:
            ValidationResult with validation outcome.
        """
        normalize = kwargs.get("normalize", True)
        ignore_order = kwargs.get("ignore_order", False)

        if normalize:
            expected = self._normalize_value(expected)
            actual = self._normalize_value(actual)

        if ignore_order and isinstance(expected, list) and isinstance(actual, list):
            # Compare as sorted lists (for hashable items) or sets
            try:
                is_valid = sorted(expected) == sorted(actual)
            except TypeError:
                # Non-comparable items, try set comparison
                is_valid = set(map(str, expected)) == set(map(str, actual))
        else:
            is_valid = expected == actual

        return ValidationResult(
            is_valid=is_valid,
            score=1.0 if is_valid else 0.0,
            message="" if is_valid else f"Expected {expected}, got {actual}",
            expected=expected,
            actual=actual,
        )


class DictMatchValidator(Validator):
    """Validator for dictionary equality with optional key normalization."""

    @property
    def name(self) -> str:
        return "dict_match"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check dictionary equality.

        Args:
            expected: Expected dictionary.
            actual: Actual dictionary.
            **kwargs: Optional parameters:
                - key_transform: Function to normalize keys.
                - value_tolerance: Tolerance for numeric values.

        Returns:
            ValidationResult with validation outcome.
        """
        if not isinstance(expected, dict) or not isinstance(actual, dict):
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Expected dict types, got {type(expected)} and {type(actual)}",
                expected=expected,
                actual=actual,
            )

        key_transform = kwargs.get("key_transform", lambda x: str(x).strip())
        value_tolerance = kwargs.get("value_tolerance", 0)

        # Normalize keys
        expected_norm = {key_transform(k): v for k, v in expected.items()}
        actual_norm = {key_transform(k): v for k, v in actual.items()}

        if set(expected_norm.keys()) != set(actual_norm.keys()):
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Key mismatch: expected {set(expected_norm.keys())}, got {set(actual_norm.keys())}",
                expected=expected,
                actual=actual,
            )

        mismatches = []
        for key in expected_norm:
            exp_val = expected_norm[key]
            act_val = actual_norm[key]

            if isinstance(exp_val, (int, float)) and isinstance(act_val, (int, float)):
                if value_tolerance > 0:
                    if abs(exp_val - act_val) > value_tolerance:
                        mismatches.append((key, exp_val, act_val))
                elif exp_val != act_val:
                    mismatches.append((key, exp_val, act_val))
            elif exp_val != act_val:
                mismatches.append((key, exp_val, act_val))

        if mismatches:
            return ValidationResult(
                is_valid=False,
                score=1.0 - len(mismatches) / len(expected_norm),
                message=f"Value mismatches: {mismatches}",
                expected=expected,
                actual=actual,
                details={"mismatches": mismatches},
            )

        return ValidationResult(
            is_valid=True,
            score=1.0,
            message="",
            expected=expected,
            actual=actual,
        )


class PathMatchValidator(Validator):
    """Validator for path equality (allows equivalent paths)."""

    @property
    def name(self) -> str:
        return "path_match"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check path equality, allowing for equivalent paths.

        Args:
            expected: Expected path as list or dict with "path" key.
            actual: Actual path from LLM as list or dict with "path" key.
            **kwargs: Optional parameters:
                - check_cost: If True and cost provided, verify path cost.
                - expected_cost: Expected path cost.
                - edges: Edge weights for cost verification.

        Returns:
            ValidationResult with validation outcome.
        """
        # Extract path from dict if wrapped
        if isinstance(expected, dict) and "path" in expected:
            expected = expected["path"]
        if isinstance(actual, dict) and "path" in actual:
            actual = actual["path"]

        if not isinstance(expected, list) or not isinstance(actual, list):
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Expected list paths, got {type(expected)} and {type(actual)}",
                expected=expected,
                actual=actual,
            )

        # Normalize path elements
        expected = [str(x).strip() for x in expected]
        actual = [str(x).strip() for x in actual]

        # Check start and end
        if not expected or not actual:
            is_valid = expected == actual
        elif expected[0] != actual[0] or expected[-1] != actual[-1]:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Path endpoints mismatch: {expected[0]}->{expected[-1]} vs {actual[0]}->{actual[-1]}",
                expected=expected,
                actual=actual,
            )
        else:
            # Paths have same endpoints
            # If cost checking is enabled, verify path cost
            check_cost = kwargs.get("check_cost", False)
            if check_cost and "edges" in kwargs:
                edges = kwargs["edges"]
                expected_cost = kwargs.get("expected_cost")

                # Calculate actual path cost
                actual_cost = self._calculate_path_cost(actual, edges)
                if expected_cost is not None and abs(actual_cost - expected_cost) > 1e-9:
                    return ValidationResult(
                        is_valid=False,
                        score=0.5,
                        message=f"Path cost mismatch: expected {expected_cost}, got {actual_cost}",
                        expected=expected,
                        actual=actual,
                        details={"expected_cost": expected_cost, "actual_cost": actual_cost},
                    )

        is_valid = expected == actual
        return ValidationResult(
            is_valid=is_valid,
            score=1.0 if is_valid else 0.5,  # Partial credit for valid different path
            message="" if is_valid else f"Different path: expected {expected}, got {actual}",
            expected=expected,
            actual=actual,
        )

    def _calculate_path_cost(self, path: list, edges: list) -> float:
        """Calculate total cost of a path given edges."""
        edge_map = {}
        for edge in edges:
            if len(edge) >= 3:
                u, v, w = edge[0], edge[1], edge[2]
                edge_map[(str(u), str(v))] = w

        cost = 0.0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if (u, v) in edge_map:
                cost += edge_map[(u, v)]
            elif (v, u) in edge_map:  # Undirected
                cost += edge_map[(v, u)]

        return cost


def get_exact_match_validator() -> ExactMatchValidator:
    """Factory function."""
    return ExactMatchValidator()


def get_dict_match_validator() -> DictMatchValidator:
    """Factory function."""
    return DictMatchValidator()


def get_path_match_validator() -> PathMatchValidator:
    """Factory function."""
    return PathMatchValidator()
