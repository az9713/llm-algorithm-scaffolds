"""
Tests for reference implementations.

These tests verify the reference implementations are correct
before using them to validate LLM outputs.
"""

import pytest

from verification.reference.graph import dijkstra, bfs, bellman_ford, floyd_warshall, topological_sort
from verification.reference.dynamic_programming import knapsack_01, lcs, edit_distance, lis
from verification.reference.divide_conquer import binary_search, merge_sort, quickselect
from verification.reference.greedy import activity_selection, fractional_knapsack, kruskal_mst
from verification.reference.backtracking import nqueens, subset_sum
from verification.reference.string_algo import kmp_search, rabin_karp_search
from verification.reference.numerical import newton_raphson, bisection


class TestGraphAlgorithms:
    """Test graph algorithm reference implementations."""

    def test_dijkstra_simple(self):
        """Test Dijkstra on simple graph."""
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 5], ["A", "C", 2], ["B", "D", 1], ["C", "D", 3]]

        result = dijkstra(vertices, edges, "A")

        assert result.distances["A"] == 0
        assert result.distances["B"] == 5
        assert result.distances["C"] == 2
        assert result.distances["D"] == 5  # A->C->D = 2+3

    def test_dijkstra_with_target(self):
        """Test Dijkstra with target vertex."""
        vertices = ["A", "B", "C"]
        edges = [["A", "B", 1], ["B", "C", 2]]

        result = dijkstra(vertices, edges, "A", "C")

        assert result.path == ["A", "B", "C"]
        assert result.distances["C"] == 3

    def test_bfs_shortest_path(self):
        """Test BFS finds shortest path in unweighted graph."""
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["C", "D", 1]]

        result = bfs(vertices, edges, "A", "D")

        assert result.path in [["A", "B", "D"], ["A", "C", "D"]]
        assert result.distances["D"] == 2

    def test_topological_sort_dag(self):
        """Test topological sort on DAG."""
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["C", "D", 1]]

        result = topological_sort(vertices, edges)

        # A must come before B, C; B, C must come before D
        order = result.order
        assert order.index("A") < order.index("B")
        assert order.index("A") < order.index("C")
        assert order.index("B") < order.index("D")
        assert order.index("C") < order.index("D")


class TestDynamicProgramming:
    """Test DP algorithm reference implementations."""

    def test_knapsack_simple(self):
        """Test 0/1 knapsack on simple case."""
        values = [1, 4, 5, 7]
        weights = [1, 3, 4, 5]
        capacity = 7

        result = knapsack_01(values, weights, capacity)

        assert result.value == 9  # Items 2 and 3 (values 4+5)
        assert set(result.solution) == {1, 2}  # 0-indexed

    def test_lcs_strings(self):
        """Test LCS on strings."""
        result = lcs("ABCBDAB", "BDCAB")

        assert result.value == 4
        assert result.solution in ["BCAB", "BDAB"]

    def test_edit_distance(self):
        """Test edit distance."""
        result = edit_distance("kitten", "sitting")

        assert result.value == 3  # k->s, e->i, +g

    def test_lis_increasing(self):
        """Test longest increasing subsequence."""
        result = lis([10, 22, 9, 33, 21, 50, 41, 60, 80])

        assert result.value == 6
        assert result.solution == [10, 22, 33, 50, 60, 80]


class TestDivideAndConquer:
    """Test divide and conquer algorithm reference implementations."""

    def test_binary_search_found(self):
        """Test binary search finds target."""
        result = binary_search([1, 3, 5, 7, 9, 11], 7)

        assert result.found
        assert result.value == 3

    def test_binary_search_not_found(self):
        """Test binary search when target not present."""
        result = binary_search([1, 3, 5, 7, 9, 11], 6)

        assert not result.found
        assert result.value == -1

    def test_merge_sort(self):
        """Test merge sort."""
        result = merge_sort([5, 2, 8, 1, 9, 3])

        assert result.value == [1, 2, 3, 5, 8, 9]

    def test_quickselect(self):
        """Test quickselect finds k-th smallest."""
        result = quickselect([3, 1, 4, 1, 5, 9, 2, 6], 3)

        assert result.value == 2  # 3rd smallest


class TestGreedy:
    """Test greedy algorithm reference implementations."""

    def test_activity_selection(self):
        """Test activity selection."""
        activities = [(0, 6), (1, 4), (3, 5), (5, 7), (5, 9), (8, 9)]

        result = activity_selection(activities)

        assert result.value == 3

    def test_fractional_knapsack(self):
        """Test fractional knapsack."""
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50

        result = fractional_knapsack(values, weights, capacity)

        assert abs(result.value - 240.0) < 0.01  # 120 + 100 + 20


class TestBacktracking:
    """Test backtracking algorithm reference implementations."""

    def test_nqueens_4(self):
        """Test 4-queens has solution."""
        result = nqueens(4)

        assert result.found
        assert len(result.solution) == 4
        # Verify no conflicts
        cols = [c for _, c in result.solution]
        assert len(set(cols)) == 4

    def test_nqueens_3_no_solution(self):
        """Test 3-queens has no solution."""
        result = nqueens(3)

        assert not result.found

    def test_subset_sum_found(self):
        """Test subset sum finds solution."""
        result = subset_sum([3, 34, 4, 12, 5, 2], 9)

        assert result.found
        assert sum(result.solution) == 9


class TestStringAlgorithms:
    """Test string algorithm reference implementations."""

    def test_kmp_pattern_found(self):
        """Test KMP finds pattern."""
        result = kmp_search("ABABDABACDABABCABAB", "ABABCABAB")

        assert result.found
        assert 10 in result.matches

    def test_kmp_pattern_not_found(self):
        """Test KMP when pattern not present."""
        result = kmp_search("AAAA", "BB")

        assert not result.found
        assert result.matches == []

    def test_rabin_karp_multiple_matches(self):
        """Test Rabin-Karp finds multiple matches."""
        result = rabin_karp_search("AABAACAADAABAAABAA", "AABA")

        assert result.found
        assert 0 in result.matches
        assert 9 in result.matches


class TestNumerical:
    """Test numerical algorithm reference implementations."""

    def test_newton_raphson_sqrt2(self):
        """Test Newton-Raphson finds sqrt(2)."""
        f = lambda x: x**2 - 2
        df = lambda x: 2 * x

        result = newton_raphson(f, df, x0=1.5)

        assert result.converged
        assert abs(result.value - 1.41421356) < 1e-6

    def test_bisection_root(self):
        """Test bisection finds root."""
        f = lambda x: x**3 - x - 2

        result = bisection(f, 1, 2)

        assert result.converged
        assert abs(f(result.value)) < 1e-6
