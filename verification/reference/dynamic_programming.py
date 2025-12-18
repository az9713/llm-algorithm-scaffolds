"""
Reference implementations for dynamic programming algorithms.

Implements: 0/1 Knapsack, LCS, Edit Distance, LIS, Matrix Chain Multiplication.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class DPResult:
    """Result from a dynamic programming algorithm."""

    value: int | float
    """Optimal value (max value, min cost, length, etc.)."""

    solution: list | str | None = None
    """The actual solution (selected items, subsequence, etc.)."""

    dp_table: list[list] | None = None
    """The DP table (for debugging/verification)."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        result = {"value": self.value}
        if self.solution is not None:
            result["solution"] = self.solution
        return result


def knapsack_01(
    values: list[int],
    weights: list[int],
    capacity: int,
) -> DPResult:
    """
    0/1 Knapsack problem - select items to maximize value within capacity.

    Args:
        values: List of item values.
        weights: List of item weights.
        capacity: Maximum weight capacity.

    Returns:
        DPResult with maximum value and selected item indices.
    """
    n = len(values)

    # Create DP table
    # dp[i][w] = maximum value using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i - 1][w]

            # Take item i-1 if it fits
            if weights[i - 1] <= w:
                take = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take)

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # 0-indexed item
            w -= weights[i - 1]

    selected.reverse()

    return DPResult(
        value=dp[n][capacity],
        solution=selected,
        dp_table=dp,
    )


def lcs(
    seq1: str | list,
    seq2: str | list,
) -> DPResult:
    """
    Longest Common Subsequence.

    Args:
        seq1: First sequence (string or list).
        seq2: Second sequence (string or list).

    Returns:
        DPResult with LCS length and the subsequence.
    """
    m, n = len(seq1), len(seq2)

    # dp[i][j] = LCS length of seq1[0:i] and seq2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS
    lcs_result = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_result.reverse()

    # Convert back to string if input was string
    if isinstance(seq1, str):
        lcs_result = "".join(lcs_result)

    return DPResult(
        value=dp[m][n],
        solution=lcs_result,
        dp_table=dp,
    )


def edit_distance(
    s1: str,
    s2: str,
    insert_cost: int = 1,
    delete_cost: int = 1,
    replace_cost: int = 1,
) -> DPResult:
    """
    Edit Distance (Levenshtein Distance) between two strings.

    Args:
        s1: Source string.
        s2: Target string.
        insert_cost: Cost of insertion.
        delete_cost: Cost of deletion.
        replace_cost: Cost of replacement.

    Returns:
        DPResult with minimum edit distance.
    """
    m, n = len(s1), len(s2)

    # dp[i][j] = edit distance from s1[0:i] to s2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + delete_cost,  # Delete from s1
                    dp[i][j - 1] + insert_cost,  # Insert into s1
                    dp[i - 1][j - 1] + replace_cost,  # Replace
                )

    # Backtrack to find the operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            operations.append(("match", s1[i - 1]))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + replace_cost:
            operations.append(("replace", s1[i - 1], s2[j - 1]))
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + insert_cost:
            operations.append(("insert", s2[j - 1]))
            j -= 1
        else:
            operations.append(("delete", s1[i - 1]))
            i -= 1

    operations.reverse()

    return DPResult(
        value=dp[m][n],
        solution=operations,
        dp_table=dp,
    )


def lis(
    sequence: list[int | float],
) -> DPResult:
    """
    Longest Increasing Subsequence.

    Uses O(n log n) algorithm with binary search.

    Args:
        sequence: Input sequence of numbers.

    Returns:
        DPResult with LIS length and the subsequence.
    """
    if not sequence:
        return DPResult(value=0, solution=[])

    n = len(sequence)

    # dp[i] = smallest ending element of all increasing subsequences of length i+1
    dp = []
    # parent[i] = index of previous element in the LIS ending at i
    parent = [-1] * n
    # indices[i] = index of the element that gives dp[i]
    indices = []

    def binary_search(arr: list, target: int | float) -> int:
        """Find leftmost position where target should be inserted."""
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if dp[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    for i, num in enumerate(sequence):
        pos = binary_search(dp, num)

        if pos == len(dp):
            dp.append(num)
            indices.append(i)
        else:
            dp[pos] = num
            indices[pos] = i

        if pos > 0:
            parent[i] = indices[pos - 1]

    # Reconstruct the LIS
    lis_result = []
    idx = indices[-1] if indices else -1
    while idx >= 0:
        lis_result.append(sequence[idx])
        idx = parent[idx]

    lis_result.reverse()

    return DPResult(
        value=len(lis_result),
        solution=lis_result,
    )


def matrix_chain_multiplication(
    dimensions: list[int],
) -> DPResult:
    """
    Matrix Chain Multiplication - find optimal parenthesization.

    Args:
        dimensions: List of matrix dimensions [p0, p1, p2, ..., pn]
                   representing n matrices of sizes p0xp1, p1xp2, ..., p(n-1)xpn.

    Returns:
        DPResult with minimum scalar multiplications and parenthesization.
    """
    n = len(dimensions) - 1  # Number of matrices

    if n <= 0:
        return DPResult(value=0, solution="")

    if n == 1:
        return DPResult(value=0, solution="A1")

    # dp[i][j] = minimum cost to multiply matrices i through j
    dp = [[0] * n for _ in range(n)]
    # split[i][j] = optimal split point for matrices i through j
    split = [[0] * n for _ in range(n)]

    # Fill for chains of increasing length
    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    # Build parenthesization string
    def build_parens(i: int, j: int) -> str:
        if i == j:
            return f"A{i + 1}"
        else:
            k = split[i][j]
            left = build_parens(i, k)
            right = build_parens(k + 1, j)
            return f"({left} × {right})"

    parenthesization = build_parens(0, n - 1)

    return DPResult(
        value=dp[0][n - 1],
        solution=parenthesization,
        dp_table=dp,
    )


# Convenience function to run any DP algorithm
def run_dp_algorithm(
    algorithm: str,
    **kwargs,
) -> DPResult:
    """
    Run a DP algorithm by name.

    Args:
        algorithm: Algorithm name (knapsack_01, lcs, edit_distance, lis, matrix_chain).
        **kwargs: Algorithm-specific arguments.

    Returns:
        DPResult from the algorithm.
    """
    algorithms = {
        "knapsack_01": knapsack_01,
        "knapsack": knapsack_01,
        "lcs": lcs,
        "edit_distance": edit_distance,
        "levenshtein": edit_distance,
        "lis": lis,
        "matrix_chain": matrix_chain_multiplication,
        "matrix_chain_multiplication": matrix_chain_multiplication,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm in ("knapsack_01", "knapsack"):
        return func(kwargs["values"], kwargs["weights"], kwargs["capacity"])
    elif algorithm == "lcs":
        return func(kwargs["seq1"], kwargs["seq2"])
    elif algorithm in ("edit_distance", "levenshtein"):
        return func(
            kwargs["s1"],
            kwargs["s2"],
            kwargs.get("insert_cost", 1),
            kwargs.get("delete_cost", 1),
            kwargs.get("replace_cost", 1),
        )
    elif algorithm == "lis":
        return func(kwargs["sequence"])
    elif algorithm in ("matrix_chain", "matrix_chain_multiplication"):
        return func(kwargs["dimensions"])
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
