"""
Set equivalence validator for unordered collections.
"""

from typing import Any

from .base import ValidationResult, Validator


class SetEquivalenceValidator(Validator):
    """Validator for unordered set equality."""

    @property
    def name(self) -> str:
        return "set_equivalence"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check set equivalence (order-independent).

        Args:
            expected: Expected collection.
            actual: Actual collection from LLM.
            **kwargs: Optional parameters:
                - key: Function to extract comparison key from elements.

        Returns:
            ValidationResult with validation outcome.
        """
        key_func = kwargs.get("key", None)

        if not hasattr(expected, "__iter__") or not hasattr(actual, "__iter__"):
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Expected iterable types, got {type(expected)} and {type(actual)}",
                expected=expected,
                actual=actual,
            )

        # Convert to sets for comparison
        try:
            if key_func:
                expected_set = set(key_func(x) for x in expected)
                actual_set = set(key_func(x) for x in actual)
            else:
                expected_set = set(self._to_hashable(x) for x in expected)
                actual_set = set(self._to_hashable(x) for x in actual)
        except TypeError as e:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Cannot convert to set: {e}",
                expected=expected,
                actual=actual,
            )

        is_valid = expected_set == actual_set

        if is_valid:
            return ValidationResult(
                is_valid=True,
                score=1.0,
                message="",
                expected=expected,
                actual=actual,
            )
        else:
            missing = expected_set - actual_set
            extra = actual_set - expected_set

            # Calculate Jaccard similarity for partial score
            intersection = len(expected_set & actual_set)
            union = len(expected_set | actual_set)
            score = intersection / union if union > 0 else 0.0

            return ValidationResult(
                is_valid=False,
                score=score,
                message=f"Set mismatch: missing {missing}, extra {extra}",
                expected=expected,
                actual=actual,
                details={"missing": list(missing), "extra": list(extra)},
            )

    def _to_hashable(self, item: Any) -> Any:
        """Convert item to hashable form."""
        if isinstance(item, list):
            return tuple(self._to_hashable(x) for x in item)
        if isinstance(item, dict):
            return tuple(sorted((k, self._to_hashable(v)) for k, v in item.items()))
        return item


class EdgeSetValidator(Validator):
    """Validator for edge sets (e.g., MST edges)."""

    @property
    def name(self) -> str:
        return "edge_set"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Check edge set equivalence.

        Edges can be in either direction for undirected graphs.

        Args:
            expected: Expected edge list.
            actual: Actual edge list from LLM.
            **kwargs: Optional parameters:
                - directed: If False (default), edges are bidirectional.
                - check_weights: If True, also verify edge weights.

        Returns:
            ValidationResult with validation outcome.
        """
        directed = kwargs.get("directed", False)
        check_weights = kwargs.get("check_weights", True)

        def normalize_edge(edge):
            """Normalize edge for comparison."""
            if len(edge) >= 3:
                u, v, w = edge[0], edge[1], edge[2]
                if not directed and str(u) > str(v):
                    u, v = v, u
                if check_weights:
                    return (str(u), str(v), w)
                return (str(u), str(v))
            else:
                u, v = edge[0], edge[1]
                if not directed and str(u) > str(v):
                    u, v = v, u
                return (str(u), str(v))

        try:
            expected_edges = set(normalize_edge(e) for e in expected)
            actual_edges = set(normalize_edge(e) for e in actual)
        except (TypeError, IndexError) as e:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message=f"Cannot normalize edges: {e}",
                expected=expected,
                actual=actual,
            )

        is_valid = expected_edges == actual_edges

        if is_valid:
            return ValidationResult(
                is_valid=True,
                score=1.0,
                message="",
                expected=expected,
                actual=actual,
            )
        else:
            missing = expected_edges - actual_edges
            extra = actual_edges - expected_edges

            # Calculate score
            intersection = len(expected_edges & actual_edges)
            total = len(expected_edges)
            score = intersection / total if total > 0 else 0.0

            return ValidationResult(
                is_valid=False,
                score=score,
                message=f"Edge set mismatch: missing {len(missing)}, extra {len(extra)}",
                expected=expected,
                actual=actual,
                details={"missing": list(missing), "extra": list(extra)},
            )


class MSTValidator(Validator):
    """Validator for Minimum Spanning Tree results."""

    @property
    def name(self) -> str:
        return "mst_validator"

    def validate(
        self,
        expected: Any,
        actual: Any,
        **kwargs,
    ) -> ValidationResult:
        """
        Validate MST by checking total weight matches.

        Multiple valid MSTs may exist with same total weight.

        Args:
            expected: Expected MST dict with total_weight and edges.
            actual: Actual MST from LLM (dict with total_weight and edges).
            **kwargs: Optional parameters.

        Returns:
            ValidationResult with validation outcome.
        """
        # Handle None or invalid actual
        if actual is None:
            return ValidationResult(
                is_valid=False,
                score=0.0,
                message="No MST result provided",
                expected=expected,
                actual=None,
            )

        # Extract expected weight
        expected_weight = None
        if isinstance(expected, dict):
            expected_weight = expected.get("total_weight")
        elif isinstance(expected, (int, float)):
            expected_weight = expected

        # Extract actual weight
        actual_weight = 0.0
        if isinstance(actual, dict):
            # Dict format: {"total_weight": N, "edges": [...]}
            actual_weight = actual.get("total_weight", 0)
            if actual_weight == 0 and "edges" in actual:
                # Calculate from edges if weight not provided
                edges = actual.get("edges", [])
                for edge in edges:
                    if isinstance(edge, (list, tuple)) and len(edge) >= 3:
                        try:
                            actual_weight += float(edge[2])
                        except (ValueError, TypeError):
                            pass
        elif hasattr(actual, "__iter__"):
            # List of edges format
            for edge in actual:
                if isinstance(edge, (list, tuple)) and len(edge) >= 3:
                    try:
                        actual_weight += float(edge[2])
                    except (ValueError, TypeError):
                        pass

        if expected_weight is not None:
            is_valid = abs(actual_weight - expected_weight) < 1e-9

            return ValidationResult(
                is_valid=is_valid,
                score=1.0 if is_valid else 0.0,
                message="" if is_valid else f"MST weight mismatch: expected {expected_weight}, got {actual_weight}",
                expected=expected_weight,
                actual=actual_weight,
                details={"expected_weight": expected_weight, "actual_weight": actual_weight},
            )
        else:
            # Fall back to edge set comparison
            edge_validator = EdgeSetValidator()
            expected_edges = expected.get("edges", expected) if isinstance(expected, dict) else expected
            actual_edges = actual.get("edges", actual) if isinstance(actual, dict) else actual
            return edge_validator.validate(expected_edges, actual_edges, **kwargs)


def get_set_equivalence_validator() -> SetEquivalenceValidator:
    """Factory function."""
    return SetEquivalenceValidator()


def get_edge_set_validator() -> EdgeSetValidator:
    """Factory function."""
    return EdgeSetValidator()


def get_mst_validator() -> MSTValidator:
    """Factory function."""
    return MSTValidator()
