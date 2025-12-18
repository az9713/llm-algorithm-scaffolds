"""
Reference implementations for divide and conquer algorithms.

Implements: Binary Search, Merge Sort, Quickselect.
"""

from bisect import bisect_left
from dataclasses import dataclass
from typing import Any


@dataclass
class DivideConquerResult:
    """Result from a divide and conquer algorithm."""

    value: Any
    """The result (index, sorted list, k-th element, etc.)."""

    found: bool = True
    """Whether the target was found (for search algorithms)."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        return {"value": self.value, "found": self.found}


def binary_search(
    arr: list,
    target: Any,
) -> DivideConquerResult:
    """
    Binary Search for a target in a sorted array.

    Args:
        arr: Sorted array to search.
        target: Value to find.

    Returns:
        DivideConquerResult with index if found, -1 if not found.
    """
    if not arr:
        return DivideConquerResult(value=-1, found=False)

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return DivideConquerResult(value=mid, found=True)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return DivideConquerResult(value=-1, found=False)


def binary_search_leftmost(
    arr: list,
    target: Any,
) -> DivideConquerResult:
    """
    Binary Search for leftmost occurrence of target.

    Args:
        arr: Sorted array to search.
        target: Value to find.

    Returns:
        DivideConquerResult with leftmost index if found.
    """
    idx = bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return DivideConquerResult(value=idx, found=True)
    return DivideConquerResult(value=-1, found=False)


def merge_sort(
    arr: list,
) -> DivideConquerResult:
    """
    Merge Sort - stable O(n log n) sorting.

    Args:
        arr: Array to sort.

    Returns:
        DivideConquerResult with sorted array.
    """
    if len(arr) <= 1:
        return DivideConquerResult(value=list(arr))

    def merge(left: list, right: list) -> list:
        """Merge two sorted arrays."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr: list) -> list:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(list(arr))
    return DivideConquerResult(value=sorted_arr)


def quickselect(
    arr: list,
    k: int,
) -> DivideConquerResult:
    """
    Quickselect - find k-th smallest element in O(n) average time.

    Args:
        arr: Array to search.
        k: 1-indexed position (k=1 means smallest, k=n means largest).

    Returns:
        DivideConquerResult with k-th smallest element.
    """
    if not arr or k < 1 or k > len(arr):
        raise ValueError(f"Invalid k={k} for array of length {len(arr)}")

    # Convert to 0-indexed
    k_idx = k - 1

    def partition(arr: list, left: int, right: int, pivot_idx: int) -> int:
        """Partition array around pivot, return final pivot position."""
        pivot = arr[pivot_idx]
        # Move pivot to end
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1

        # Move pivot to final position
        arr[store_idx], arr[right] = arr[right], arr[store_idx]
        return store_idx

    def select(arr: list, left: int, right: int, k: int) -> Any:
        if left == right:
            return arr[left]

        # Choose pivot (median of three for better performance)
        pivot_idx = left + (right - left) // 2
        pivot_idx = partition(arr, left, right, pivot_idx)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return select(arr, left, pivot_idx - 1, k)
        else:
            return select(arr, pivot_idx + 1, right, k)

    # Work on a copy to avoid modifying original
    arr_copy = list(arr)
    result = select(arr_copy, 0, len(arr_copy) - 1, k_idx)

    return DivideConquerResult(value=result)


def quickselect_median(
    arr: list,
) -> DivideConquerResult:
    """
    Find median using quickselect.

    Args:
        arr: Array to find median of.

    Returns:
        DivideConquerResult with median value.
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Cannot find median of empty array")

    if n % 2 == 1:
        return quickselect(arr, n // 2 + 1)
    else:
        lower = quickselect(arr, n // 2).value
        upper = quickselect(arr, n // 2 + 1).value
        return DivideConquerResult(value=(lower + upper) / 2)


# Convenience function to run any divide and conquer algorithm
def run_divide_conquer_algorithm(
    algorithm: str,
    **kwargs,
) -> DivideConquerResult:
    """
    Run a divide and conquer algorithm by name.

    Args:
        algorithm: Algorithm name (binary_search, merge_sort, quickselect).
        **kwargs: Algorithm-specific arguments.

    Returns:
        DivideConquerResult from the algorithm.
    """
    algorithms = {
        "binary_search": binary_search,
        "binary_search_leftmost": binary_search_leftmost,
        "merge_sort": merge_sort,
        "quickselect": quickselect,
        "quickselect_median": quickselect_median,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm in ("binary_search", "binary_search_leftmost"):
        return func(kwargs["arr"], kwargs["target"])
    elif algorithm == "merge_sort":
        return func(kwargs["arr"])
    elif algorithm == "quickselect":
        return func(kwargs["arr"], kwargs["k"])
    elif algorithm == "quickselect_median":
        return func(kwargs["arr"])
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
