"""
Scaffold registry - Maps scaffolds to their generators and validators.

This module provides automatic discovery of test generators and validators
for each scaffold, enabling fully automated verification.
"""

from typing import Any

from .generators.base import TestCaseGenerator, TestCase, TestSuite
from .validators.base import Validator
from .validators.exact_match import ExactMatchValidator, DictMatchValidator, PathMatchValidator
from .validators.numeric_tolerance import NumericToleranceValidator, RootValidator, OptimizationValidator
from .validators.set_equivalence import SetEquivalenceValidator, EdgeSetValidator, MSTValidator


# Registry of all scaffolds organized by category
SCAFFOLD_REGISTRY = {
    "graph": [
        "bfs", "dfs", "dijkstra", "astar",
        "bellman_ford", "floyd_warshall", "topological_sort"
    ],
    "divide_conquer": [
        "binary_search", "merge_sort", "quickselect"
    ],
    "greedy": [
        "activity_selection", "huffman", "kruskal", "fractional_knapsack"
    ],
    "backtracking": [
        "nqueens", "sudoku", "graph_coloring", "subset_sum"
    ],
    "dynamic_programming": [
        "knapsack_01", "lcs", "edit_distance", "lis", "matrix_chain"
    ],
    "optimization": [
        "gradient_descent", "simulated_annealing", "genetic_algorithm", "hill_climbing"
    ],
    "string": [
        "kmp", "rabin_karp", "trie_operations"
    ],
    "numerical": [
        "newton_raphson", "bisection", "monte_carlo"
    ],
}


# Mapping of scaffolds to validator types
VALIDATOR_REGISTRY = {
    # Graph - most use dict match for distances
    "bfs": "path",
    "dfs": "path",
    "dijkstra": "dict",
    "astar": "path",
    "bellman_ford": "dict",
    "floyd_warshall": "dict",
    "topological_sort": "order",

    # Divide & Conquer
    "binary_search": "exact",
    "merge_sort": "exact",
    "quickselect": "exact",

    # Greedy
    "activity_selection": "dict",
    "huffman": "dict",
    "kruskal": "mst",
    "fractional_knapsack": "numeric",

    # Backtracking
    "nqueens": "positions",
    "sudoku": "exact",
    "graph_coloring": "exact",
    "subset_sum": "set",

    # DP
    "knapsack_01": "knapsack",
    "lcs": "sequence",
    "edit_distance": "exact",
    "lis": "sequence",
    "matrix_chain": "exact",

    # Optimization
    "gradient_descent": "optimization",
    "simulated_annealing": "optimization",
    "genetic_algorithm": "optimization",
    "hill_climbing": "optimization",

    # String
    "kmp": "exact",
    "rabin_karp": "exact",
    "trie_operations": "exact",

    # Numerical
    "newton_raphson": "root",
    "bisection": "root",
    "monte_carlo": "numeric",
}


def get_validator_for_scaffold(scaffold_name: str) -> Validator:
    """
    Get the appropriate validator for a scaffold.

    Args:
        scaffold_name: Name of the scaffold.

    Returns:
        Validator instance configured for this scaffold.
    """
    validator_type = VALIDATOR_REGISTRY.get(scaffold_name, "exact")

    validators = {
        "exact": ExactMatchValidator(),
        "dict": DictMatchValidator(),
        "path": PathMatchValidator(),
        "set": SetEquivalenceValidator(),
        "mst": MSTValidator(),
        "edge": EdgeSetValidator(),
        "numeric": NumericToleranceValidator(absolute_tolerance=0.01, relative_tolerance=0.01),
        "root": RootValidator(tolerance=1e-6),
        "optimization": OptimizationValidator(tolerance_percent=10.0),
        "order": ExactMatchValidator(),  # Topological sort may have multiple valid orders
        "positions": SetEquivalenceValidator(),  # N-Queens positions
        "knapsack": DictMatchValidator(),
        "sequence": DictMatchValidator(),
    }

    return validators.get(validator_type, ExactMatchValidator())


# =============================================================================
# Universal Test Case Generator
# =============================================================================

class UniversalGenerator(TestCaseGenerator):
    """
    Universal test case generator that works for any scaffold.

    Uses reference implementations to generate ground truth for any test case.
    """

    def __init__(self, scaffold_name: str, seed: int = 42):
        super().__init__(seed)
        self._scaffold_name = scaffold_name
        self._category = self._get_category()

    @property
    def scaffold_name(self) -> str:
        return self._scaffold_name

    def _get_category(self) -> str:
        """Find which category this scaffold belongs to."""
        for category, scaffolds in SCAFFOLD_REGISTRY.items():
            if self._scaffold_name in scaffolds:
                return category
        return "unknown"

    def generate_simple(self, count: int = 3) -> list[TestCase]:
        """Generate simple test cases using reference implementations."""
        return self._generate_tier("simple", count)

    def generate_standard(self, count: int = 5) -> list[TestCase]:
        """Generate standard test cases."""
        return self._generate_tier("standard", count)

    def generate_edge_cases(self, count: int = 3) -> list[TestCase]:
        """Generate edge case tests."""
        return self._generate_tier("edge", count)

    def _generate_tier(self, tier: str, count: int) -> list[TestCase]:
        """Generate test cases for a tier using the appropriate reference."""
        cases = []

        # Get generator function based on category
        generator_func = self._get_generator_func()
        if generator_func is None:
            return cases

        for i in range(count):
            try:
                test_input, expected = generator_func(tier, i)
                cases.append(TestCase(
                    id=self._make_id(tier, i + 1),
                    scaffold=self.scaffold_name,
                    tier=tier,
                    input=test_input,
                    expected=expected,
                    description=f"{tier.capitalize()} case {i + 1} for {self.scaffold_name}",
                ))
            except Exception as e:
                # Skip cases that fail to generate
                pass

        return cases

    def _get_generator_func(self):
        """Get the appropriate test case generator function."""
        generators = {
            # Graph algorithms
            "dijkstra": self._gen_dijkstra,
            "bfs": self._gen_bfs,
            "dfs": self._gen_bfs,  # Same structure
            "bellman_ford": self._gen_dijkstra,
            "floyd_warshall": self._gen_floyd_warshall,
            "topological_sort": self._gen_topological,
            "astar": self._gen_astar,
            # Divide & Conquer
            "binary_search": self._gen_binary_search,
            "merge_sort": self._gen_merge_sort,
            "quickselect": self._gen_quickselect,
            # Dynamic Programming
            "knapsack_01": self._gen_knapsack,
            "lcs": self._gen_lcs,
            "edit_distance": self._gen_edit_distance,
            "lis": self._gen_lis,
            "matrix_chain": self._gen_matrix_chain,
            # Greedy
            "activity_selection": self._gen_activity,
            "kruskal": self._gen_kruskal,
            "fractional_knapsack": self._gen_fractional_knapsack,
            "huffman": self._gen_huffman,
            # Backtracking
            "nqueens": self._gen_nqueens,
            "subset_sum": self._gen_subset_sum,
            "sudoku": self._gen_sudoku,
            "graph_coloring": self._gen_graph_coloring,
            # String
            "kmp": self._gen_pattern_match,
            "rabin_karp": self._gen_pattern_match,
            "trie_operations": self._gen_trie,
            # Numerical
            "newton_raphson": self._gen_newton,
            "bisection": self._gen_bisection,
            "monte_carlo": self._gen_monte_carlo,
            # Optimization
            "gradient_descent": self._gen_gradient_descent,
            "simulated_annealing": self._gen_simulated_annealing,
            "genetic_algorithm": self._gen_genetic_algorithm,
            "hill_climbing": self._gen_hill_climbing,
        }
        return generators.get(self.scaffold_name)

    # -------------------------------------------------------------------------
    # Graph Generators
    # -------------------------------------------------------------------------

    def _gen_dijkstra(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Dijkstra test case."""
        import random
        from .reference.graph import dijkstra

        if tier == "simple":
            n = 4
        elif tier == "standard":
            n = random.randint(5, 8)
        else:
            n = random.choice([1, 2, 10])  # Edge cases

        vertices = [chr(65 + i) for i in range(n)]  # A, B, C, ...
        edges = []

        # Create connected graph
        for i in range(n - 1):
            edges.append([vertices[i], vertices[i + 1], random.randint(1, 10)])

        # Add random edges
        for _ in range(n // 2):
            u, v = random.sample(vertices, 2)
            edges.append([u, v, random.randint(1, 10)])

        result = dijkstra(vertices, edges, vertices[0])

        return (
            {"vertices": vertices, "edges": edges, "source": vertices[0]},
            {"distances": result.distances}
        )

    def _gen_bfs(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate BFS test case."""
        import random
        from .reference.graph import bfs

        if tier == "simple":
            n = 4
        elif tier == "standard":
            n = random.randint(5, 8)
        else:
            n = random.choice([1, 2])

        vertices = [chr(65 + i) for i in range(n)]
        edges = []

        for i in range(n - 1):
            edges.append([vertices[i], vertices[i + 1], 1])

        for _ in range(n // 2):
            u, v = random.sample(vertices, 2)
            edges.append([u, v, 1])

        target = vertices[-1] if n > 1 else vertices[0]
        result = bfs(vertices, edges, vertices[0], target)

        return (
            {"vertices": vertices, "edges": edges, "source": vertices[0], "target": target},
            {"path": result.path, "distances": result.distances}
        )

    def _gen_floyd_warshall(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Floyd-Warshall test case."""
        import random
        from .reference.graph import floyd_warshall

        n = 3 if tier == "simple" else 4 if tier == "standard" else 2
        vertices = [chr(65 + i) for i in range(n)]
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                if random.random() > 0.3:
                    edges.append([vertices[i], vertices[j], random.randint(1, 10)])

        result = floyd_warshall(vertices, edges, directed=False)

        return (
            {"vertices": vertices, "edges": edges},
            {"distance_matrix": result.distance_matrix}
        )

    def _gen_topological(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate topological sort test case."""
        from .reference.graph import topological_sort

        if tier == "simple":
            vertices = ["A", "B", "C", "D"]
            edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["C", "D", 1]]
        else:
            vertices = ["A", "B", "C", "D", "E", "F"]
            edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1],
                     ["C", "D", 1], ["D", "E", 1], ["E", "F", 1]]

        result = topological_sort(vertices, edges)

        return (
            {"vertices": vertices, "edges": edges},
            {"order": result.order}
        )

    def _gen_astar(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate A* test case."""
        from .reference.graph import astar

        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 3], ["B", "D", 2], ["C", "D", 1]]
        heuristic = {"A": 3, "B": 2, "C": 1, "D": 0}

        result = astar(vertices, edges, "A", "D", heuristic)

        return (
            {"vertices": vertices, "edges": edges, "source": "A", "target": "D", "heuristic": heuristic},
            {"path": result.path}
        )

    # -------------------------------------------------------------------------
    # Divide & Conquer Generators
    # -------------------------------------------------------------------------

    def _gen_binary_search(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate binary search test case."""
        import random
        from .reference.divide_conquer import binary_search

        if tier == "simple":
            arr = [1, 3, 5, 7, 9]
            target = 5
        elif tier == "standard":
            arr = sorted(random.sample(range(100), 15))
            target = random.choice(arr)
        else:
            arr = list(range(0, 20, 2))
            target = 7  # Not in array

        result = binary_search(arr, target)

        return (
            {"arr": arr, "target": target},
            {"value": result.value, "found": result.found}
        )

    def _gen_merge_sort(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate merge sort test case."""
        import random
        from .reference.divide_conquer import merge_sort

        if tier == "simple":
            arr = [5, 2, 8, 1, 9]
        elif tier == "standard":
            arr = [random.randint(1, 100) for _ in range(10)]
        else:
            arr = [1] * 5  # All same

        result = merge_sort(arr)

        return (
            {"arr": arr},
            {"value": result.value}
        )

    def _gen_quickselect(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate quickselect test case."""
        import random
        from .reference.divide_conquer import quickselect

        if tier == "simple":
            arr = [3, 1, 4, 1, 5, 9, 2, 6]
            k = 3
        else:
            arr = [random.randint(1, 100) for _ in range(10)]
            k = random.randint(1, len(arr))

        result = quickselect(arr, k)

        return (
            {"arr": arr, "k": k},
            {"value": result.value}
        )

    # -------------------------------------------------------------------------
    # DP Generators
    # -------------------------------------------------------------------------

    def _gen_knapsack(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate knapsack test case."""
        import random
        from .reference.dynamic_programming import knapsack_01

        if tier == "simple":
            values = [1, 4, 5, 7]
            weights = [1, 3, 4, 5]
            capacity = 7
        else:
            n = random.randint(4, 8)
            values = [random.randint(1, 20) for _ in range(n)]
            weights = [random.randint(1, 10) for _ in range(n)]
            capacity = sum(weights) // 2

        result = knapsack_01(values, weights, capacity)

        return (
            {"values": values, "weights": weights, "capacity": capacity},
            {"value": result.value, "items": result.solution}
        )

    def _gen_lcs(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate LCS test case."""
        from .reference.dynamic_programming import lcs

        if tier == "simple":
            seq1, seq2 = "ABCBDAB", "BDCAB"
        else:
            seq1, seq2 = "AGGTAB", "GXTXAYB"

        result = lcs(seq1, seq2)

        return (
            {"seq1": seq1, "seq2": seq2},
            {"length": result.value, "sequence": result.solution}
        )

    def _gen_edit_distance(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate edit distance test case."""
        from .reference.dynamic_programming import edit_distance

        pairs = [("kitten", "sitting"), ("sunday", "saturday"), ("", "abc")]
        s1, s2 = pairs[idx % len(pairs)]

        result = edit_distance(s1, s2)

        return (
            {"s1": s1, "s2": s2},
            {"value": result.value}
        )

    def _gen_lis(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate LIS test case."""
        import random
        from .reference.dynamic_programming import lis

        if tier == "simple":
            sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        else:
            sequence = [random.randint(1, 100) for _ in range(12)]

        result = lis(sequence)

        return (
            {"sequence": sequence},
            {"length": result.value, "sequence": result.solution}
        )

    # -------------------------------------------------------------------------
    # Greedy Generators
    # -------------------------------------------------------------------------

    def _gen_activity(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate activity selection test case."""
        from .reference.greedy import activity_selection

        activities = [(0, 6), (1, 4), (3, 5), (5, 7), (5, 9), (8, 9)]
        result = activity_selection(activities)

        return (
            {"activities": activities},
            {"count": result.value}
        )

    def _gen_kruskal(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Kruskal MST test case."""
        from .reference.greedy import kruskal_mst

        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 3], ["B", "C", 2], ["B", "D", 4], ["C", "D", 5]]

        result = kruskal_mst(vertices, edges)

        return (
            {"vertices": vertices, "edges": edges},
            {"total_weight": result.value, "edges": result.solution}
        )

    def _gen_fractional_knapsack(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate fractional knapsack test case."""
        from .reference.greedy import fractional_knapsack

        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50

        result = fractional_knapsack(values, weights, capacity)

        return (
            {"values": values, "weights": weights, "capacity": capacity},
            {"value": result.value}
        )

    # -------------------------------------------------------------------------
    # Backtracking Generators
    # -------------------------------------------------------------------------

    def _gen_nqueens(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate N-Queens test case."""
        from .reference.backtracking import nqueens

        n = 4 if tier == "simple" else 8 if tier == "standard" else 1
        result = nqueens(n)

        return (
            {"n": n},
            {"positions": result.solution, "found": result.found}
        )

    def _gen_subset_sum(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate subset sum test case."""
        from .reference.backtracking import subset_sum

        if tier == "simple":
            numbers = [3, 34, 4, 12, 5, 2]
            target = 9
        else:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            target = 15

        result = subset_sum(numbers, target)

        return (
            {"numbers": numbers, "target": target},
            {"subset": result.solution, "found": result.found}
        )

    # -------------------------------------------------------------------------
    # String Generators
    # -------------------------------------------------------------------------

    def _gen_pattern_match(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate pattern matching test case."""
        from .reference.string_algo import kmp_search

        if tier == "simple":
            text = "ABABDABACDABABCABAB"
            pattern = "ABABCABAB"
        else:
            text = "AABAACAADAABAAABAA"
            pattern = "AABA"

        result = kmp_search(text, pattern)

        return (
            {"text": text, "pattern": pattern},
            {"matches": result.matches}
        )

    # -------------------------------------------------------------------------
    # Numerical Generators
    # -------------------------------------------------------------------------

    def _gen_newton(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Newton-Raphson test case."""
        from .reference.numerical import newton_raphson
        import math

        f = lambda x: x**2 - 2
        df = lambda x: 2 * x
        result = newton_raphson(f, df, x0=1.5)

        return (
            {"function": "x^2 - 2", "x0": 1.5},
            {"root": result.value}
        )

    def _gen_bisection(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate bisection test case."""
        from .reference.numerical import bisection

        f = lambda x: x**3 - x - 2
        result = bisection(f, 1, 2)

        return (
            {"function": "x^3 - x - 2", "a": 1, "b": 2},
            {"root": result.value}
        )

    # -------------------------------------------------------------------------
    # New Generators: Greedy - Huffman
    # -------------------------------------------------------------------------

    def _gen_huffman(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Huffman coding test case."""
        from .reference.greedy import huffman_coding

        if tier == "simple":
            frequencies = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}
        elif tier == "standard":
            frequencies = {
                "a": 10, "b": 15, "c": 12, "d": 3, "e": 4,
                "f": 13, "g": 1, "h": 2
            }
        else:
            # Edge case - single character or equal frequencies
            if idx == 0:
                frequencies = {"a": 100}
            elif idx == 1:
                frequencies = {"a": 10, "b": 10}
            else:
                frequencies = {"a": 5, "b": 5, "c": 5, "d": 5}

        result = huffman_coding(frequencies)

        return (
            {"frequencies": frequencies},
            {"total_bits": result.value, "codes": result.solution}
        )

    # -------------------------------------------------------------------------
    # New Generators: Backtracking - Sudoku, Graph Coloring
    # -------------------------------------------------------------------------

    def _gen_sudoku(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Sudoku test case."""
        from .reference.backtracking import sudoku

        # Pre-defined puzzles of varying difficulty
        if tier == "simple":
            # Easy puzzle with many filled cells
            grid = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        elif tier == "standard":
            grid = [
                [0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0]
            ]
        else:
            # Edge case - nearly complete puzzle
            grid = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 0]  # Only one cell to fill
            ]

        result = sudoku(grid)

        return (
            {"grid": grid},
            {"solution": result.solution, "found": result.found}
        )

    def _gen_graph_coloring(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate graph coloring test case."""
        from .reference.backtracking import graph_coloring

        if tier == "simple":
            vertices = ["A", "B", "C", "D"]
            edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
            num_colors = 2
        elif tier == "standard":
            vertices = ["A", "B", "C", "D", "E"]
            edges = [
                ("A", "B"), ("A", "C"), ("B", "C"),
                ("B", "D"), ("C", "D"), ("D", "E"), ("C", "E")
            ]
            num_colors = 3
        else:
            # Edge case - complete graph K3 needs 3 colors
            vertices = ["A", "B", "C"]
            edges = [("A", "B"), ("B", "C"), ("A", "C")]
            num_colors = 3

        result = graph_coloring(vertices, edges, num_colors)

        return (
            {"vertices": vertices, "edges": edges, "num_colors": num_colors},
            {"coloring": result.solution, "found": result.found}
        )

    # -------------------------------------------------------------------------
    # New Generators: Dynamic Programming - Matrix Chain
    # -------------------------------------------------------------------------

    def _gen_matrix_chain(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate matrix chain multiplication test case."""
        from .reference.dynamic_programming import matrix_chain_multiplication

        if tier == "simple":
            # 3 matrices: A1(10x30), A2(30x5), A3(5x60)
            dimensions = [10, 30, 5, 60]
        elif tier == "standard":
            # 4-5 matrices with varying dimensions
            if idx % 2 == 0:
                dimensions = [40, 20, 30, 10, 30]
            else:
                dimensions = [10, 20, 30, 40, 30]
        else:
            # Edge cases
            if idx == 0:
                dimensions = [10, 20]  # Single matrix - no multiplication needed
            elif idx == 1:
                dimensions = [10, 20, 30]  # Two matrices
            else:
                dimensions = [5, 10, 3, 12, 5, 50, 6]  # Many matrices

        result = matrix_chain_multiplication(dimensions)

        return (
            {"dimensions": dimensions},
            {"min_operations": result.value, "parenthesization": result.solution}
        )

    # -------------------------------------------------------------------------
    # New Generators: String - Trie Operations
    # -------------------------------------------------------------------------

    def _gen_trie(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate trie operations test case."""
        from .reference.string_algo import trie_operations

        if tier == "simple":
            words = ["apple", "app", "application", "banana"]
            queries = [
                ("search", "apple"),
                ("search", "app"),
                ("prefix", "app"),
                ("search", "orange"),
            ]
        elif tier == "standard":
            words = ["hello", "help", "heap", "deal", "dear", "dealer"]
            queries = [
                ("search", "hello"),
                ("search", "hel"),
                ("prefix", "hel"),
                ("autocomplete", "hel"),
                ("autocomplete", "dea"),
            ]
        else:
            # Edge cases
            if idx == 0:
                words = [""]
                queries = [("search", ""), ("prefix", "")]
            elif idx == 1:
                words = ["a"]
                queries = [("search", "a"), ("search", "b"), ("prefix", "a")]
            else:
                words = ["test", "testing", "tested", "tester"]
                queries = [("autocomplete", "test")]

        result = trie_operations(words, queries)

        return (
            {"words": words, "queries": queries},
            {"results": result.value}
        )

    # -------------------------------------------------------------------------
    # New Generators: Numerical - Monte Carlo
    # -------------------------------------------------------------------------

    def _gen_monte_carlo(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate Monte Carlo test case."""
        from .reference.numerical import monte_carlo_pi
        import math

        if tier == "simple":
            n_samples = 1000
            seed = 42 + idx
        elif tier == "standard":
            n_samples = 10000
            seed = 100 + idx
        else:
            # Edge cases - very few or many samples
            if idx == 0:
                n_samples = 100
                seed = 1
            elif idx == 1:
                n_samples = 50000
                seed = 12345
            else:
                n_samples = 5000
                seed = 99999

        result = monte_carlo_pi(n_samples, seed)

        return (
            {"task": "estimate_pi", "n_samples": n_samples, "seed": seed},
            {"estimate": result.value, "true_value": math.pi}
        )

    # -------------------------------------------------------------------------
    # New Generators: Optimization Algorithms
    # -------------------------------------------------------------------------

    def _gen_gradient_descent(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate gradient descent test case."""
        from .reference.optimization import gradient_descent
        import numpy as np

        if tier == "simple":
            # Simple quadratic: f(x) = x^2, minimum at x=0
            f = lambda x: x[0]**2 if isinstance(x, np.ndarray) else x**2
            x0 = 5.0
            func_str = "x^2"
            expected_min = 0.0
        elif tier == "standard":
            # f(x) = (x-3)^2 + 1, minimum at x=3
            f = lambda x: (x[0] - 3)**2 + 1 if isinstance(x, np.ndarray) else (x - 3)**2 + 1
            x0 = 0.0
            func_str = "(x-3)^2 + 1"
            expected_min = 1.0
        else:
            # Edge case: x^4 - 2x^2, multiple local minima
            f = lambda x: x[0]**4 - 2*x[0]**2 if isinstance(x, np.ndarray) else x**4 - 2*x**2
            x0 = 0.5
            func_str = "x^4 - 2x^2"
            expected_min = -1.0  # At x = ±1

        result = gradient_descent(f, x0=x0, learning_rate=0.1, max_iter=1000)

        return (
            {"function": func_str, "x0": x0, "learning_rate": 0.1},
            {"minimum_value": expected_min, "solution": result.solution}
        )

    def _gen_simulated_annealing(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate simulated annealing test case."""
        from .reference.optimization import simulated_annealing
        import numpy as np

        seed = 42 + idx

        if tier == "simple":
            # Simple quadratic
            f = lambda x: x[0]**2 if isinstance(x, np.ndarray) else x**2
            x0 = 10.0
            func_str = "x^2"
            expected_min = 0.0
        elif tier == "standard":
            # f(x) = (x-5)^2
            f = lambda x: (x[0] - 5)**2 if isinstance(x, np.ndarray) else (x - 5)**2
            x0 = 0.0
            func_str = "(x-5)^2"
            expected_min = 0.0
        else:
            # Rastrigin function (challenging)
            import math
            f = lambda x: x[0]**2 - 10*math.cos(2*math.pi*x[0]) + 10 if isinstance(x, np.ndarray) else x**2 - 10*math.cos(2*math.pi*x) + 10
            x0 = 2.0
            func_str = "x^2 - 10*cos(2*pi*x) + 10"
            expected_min = 0.0  # At x = 0

        result = simulated_annealing(f, x0=x0, seed=seed)

        return (
            {"function": func_str, "x0": x0, "seed": seed},
            {"minimum_value": expected_min, "solution": result.solution}
        )

    def _gen_genetic_algorithm(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate genetic algorithm test case."""
        from .reference.optimization import genetic_algorithm
        import numpy as np

        seed = 42 + idx

        if tier == "simple":
            # Simple quadratic in [-10, 10]
            f = lambda x: x[0]**2 if isinstance(x, np.ndarray) else x**2
            bounds = [(-10.0, 10.0)]
            func_str = "x^2"
            expected_min = 0.0
        elif tier == "standard":
            # Shifted parabola
            f = lambda x: (x[0] - 3)**2 if isinstance(x, np.ndarray) else (x - 3)**2
            bounds = [(-5.0, 10.0)]
            func_str = "(x-3)^2"
            expected_min = 0.0
        else:
            # 2D function: f(x,y) = x^2 + y^2
            f = lambda x: x[0]**2 + x[1]**2
            bounds = [(-5.0, 5.0), (-5.0, 5.0)]
            func_str = "x^2 + y^2"
            expected_min = 0.0

        result = genetic_algorithm(f, bounds, population_size=30, generations=50, seed=seed)

        return (
            {"function": func_str, "bounds": bounds, "seed": seed},
            {"minimum_value": expected_min, "solution": result.solution}
        )

    def _gen_hill_climbing(self, tier: str, idx: int) -> tuple[dict, dict]:
        """Generate hill climbing test case."""
        from .reference.optimization import hill_climbing
        import numpy as np

        if tier == "simple":
            # Simple quadratic
            f = lambda x: x[0]**2 if isinstance(x, np.ndarray) else x**2
            x0 = 5.0
            func_str = "x^2"
            expected_min = 0.0
        elif tier == "standard":
            # Shifted quadratic
            f = lambda x: (x[0] + 2)**2 + 3 if isinstance(x, np.ndarray) else (x + 2)**2 + 3
            x0 = 5.0
            func_str = "(x+2)^2 + 3"
            expected_min = 3.0
        else:
            # Edge case - start near optimum
            f = lambda x: x[0]**2 if isinstance(x, np.ndarray) else x**2
            x0 = 0.1
            func_str = "x^2"
            expected_min = 0.0

        result = hill_climbing(f, x0=x0, step_size=0.1, max_iter=500)

        return (
            {"function": func_str, "x0": x0},
            {"minimum_value": expected_min, "solution": result.solution}
        )


def get_all_generators() -> dict[str, TestCaseGenerator]:
    """Get generators for all scaffolds."""
    generators = {}

    for category, scaffolds in SCAFFOLD_REGISTRY.items():
        for scaffold in scaffolds:
            generators[scaffold] = UniversalGenerator(scaffold)

    return generators
