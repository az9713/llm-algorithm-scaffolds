"""
Test case generators for graph algorithms.
"""

import random
from typing import Any

from ..reference.graph import dijkstra, bfs, topological_sort
from .base import TestCase, TestCaseGenerator


class DijkstraGenerator(TestCaseGenerator):
    """Generate test cases for Dijkstra's algorithm."""

    @property
    def scaffold_name(self) -> str:
        return "dijkstra"

    def generate_simple(self, count: int = 3) -> list[TestCase]:
        """Generate simple Dijkstra test cases."""
        cases = []

        # Case 1: Simple 4-node graph (from scaffold worked example)
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 5], ["A", "C", 2], ["B", "D", 1], ["C", "D", 3]]
        result = dijkstra(vertices, edges, "A")
        cases.append(TestCase(
            id=self._make_id("simple", 1),
            scaffold=self.scaffold_name,
            tier="simple",
            input={"vertices": vertices, "edges": edges, "source": "A"},
            expected={"distances": result.distances},
            description="Simple 4-node graph from scaffold example",
        ))

        # Case 2: Linear path
        vertices = ["1", "2", "3", "4"]
        edges = [["1", "2", 1], ["2", "3", 2], ["3", "4", 3]]
        result = dijkstra(vertices, edges, "1")
        cases.append(TestCase(
            id=self._make_id("simple", 2),
            scaffold=self.scaffold_name,
            tier="simple",
            input={"vertices": vertices, "edges": edges, "source": "1"},
            expected={"distances": result.distances},
            description="Linear path 1->2->3->4",
        ))

        # Case 3: Star topology
        vertices = ["center", "a", "b", "c"]
        edges = [["center", "a", 1], ["center", "b", 2], ["center", "c", 3]]
        result = dijkstra(vertices, edges, "center")
        cases.append(TestCase(
            id=self._make_id("simple", 3),
            scaffold=self.scaffold_name,
            tier="simple",
            input={"vertices": vertices, "edges": edges, "source": "center"},
            expected={"distances": result.distances},
            description="Star topology from center",
        ))

        return cases[:count]

    def generate_standard(self, count: int = 5) -> list[TestCase]:
        """Generate standard complexity Dijkstra test cases."""
        cases = []

        # Case 1: 6-node graph with multiple paths
        vertices = ["A", "B", "C", "D", "E", "F"]
        edges = [
            ["A", "B", 2], ["A", "C", 4],
            ["B", "C", 1], ["B", "D", 7],
            ["C", "D", 3], ["C", "E", 5],
            ["D", "F", 1], ["E", "F", 2],
        ]
        result = dijkstra(vertices, edges, "A")
        cases.append(TestCase(
            id=self._make_id("standard", 1),
            scaffold=self.scaffold_name,
            tier="standard",
            input={"vertices": vertices, "edges": edges, "source": "A"},
            expected={"distances": result.distances},
            description="6-node graph with multiple paths",
        ))

        # Generate more random cases
        for i in range(2, count + 1):
            n = random.randint(5, 8)
            vertices = [f"V{j}" for j in range(n)]
            edges = []

            # Create connected graph
            for j in range(n - 1):
                edges.append([vertices[j], vertices[j + 1], random.randint(1, 10)])

            # Add random edges
            for _ in range(n):
                u, v = random.sample(vertices, 2)
                w = random.randint(1, 10)
                edges.append([u, v, w])

            result = dijkstra(vertices, edges, vertices[0])
            cases.append(TestCase(
                id=self._make_id("standard", i),
                scaffold=self.scaffold_name,
                tier="standard",
                input={"vertices": vertices, "edges": edges, "source": vertices[0]},
                expected={"distances": result.distances},
                description=f"Random {n}-node graph",
            ))

        return cases[:count]

    def generate_edge_cases(self, count: int = 3) -> list[TestCase]:
        """Generate edge case test cases."""
        cases = []

        # Case 1: Single node
        vertices = ["A"]
        edges = []
        result = dijkstra(vertices, edges, "A")
        cases.append(TestCase(
            id=self._make_id("edge", 1),
            scaffold=self.scaffold_name,
            tier="edge",
            input={"vertices": vertices, "edges": edges, "source": "A"},
            expected={"distances": result.distances},
            description="Single node graph",
        ))

        # Case 2: Disconnected graph
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["C", "D", 1]]
        result = dijkstra(vertices, edges, "A")
        cases.append(TestCase(
            id=self._make_id("edge", 2),
            scaffold=self.scaffold_name,
            tier="edge",
            input={"vertices": vertices, "edges": edges, "source": "A"},
            expected={"distances": result.distances},
            description="Disconnected graph",
        ))

        # Case 3: All same weights
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["C", "D", 1]]
        result = dijkstra(vertices, edges, "A")
        cases.append(TestCase(
            id=self._make_id("edge", 3),
            scaffold=self.scaffold_name,
            tier="edge",
            input={"vertices": vertices, "edges": edges, "source": "A"},
            expected={"distances": result.distances},
            description="All edges have same weight",
        ))

        return cases[:count]


class BFSGenerator(TestCaseGenerator):
    """Generate test cases for BFS."""

    @property
    def scaffold_name(self) -> str:
        return "bfs"

    def generate_simple(self, count: int = 3) -> list[TestCase]:
        """Generate simple BFS test cases."""
        cases = []

        # Case 1: Simple tree
        vertices = ["A", "B", "C", "D", "E"]
        edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["B", "E", 1]]
        result = bfs(vertices, edges, "A", "E")
        cases.append(TestCase(
            id=self._make_id("simple", 1),
            scaffold=self.scaffold_name,
            tier="simple",
            input={"vertices": vertices, "edges": edges, "source": "A", "target": "E"},
            expected={"path": result.path, "distances": result.distances},
            description="Simple tree BFS",
        ))

        # Add more cases...
        return cases[:count]

    def generate_standard(self, count: int = 5) -> list[TestCase]:
        """Generate standard BFS test cases."""
        cases = []
        # Simplified for brevity
        return cases[:count]

    def generate_edge_cases(self, count: int = 3) -> list[TestCase]:
        """Generate edge BFS test cases."""
        cases = []
        # Simplified for brevity
        return cases[:count]


class TopologicalSortGenerator(TestCaseGenerator):
    """Generate test cases for topological sort."""

    @property
    def scaffold_name(self) -> str:
        return "topological_sort"

    def generate_simple(self, count: int = 3) -> list[TestCase]:
        """Generate simple topological sort test cases."""
        cases = []

        # Case 1: Simple DAG
        vertices = ["A", "B", "C", "D"]
        edges = [["A", "B", 1], ["A", "C", 1], ["B", "D", 1], ["C", "D", 1]]
        result = topological_sort(vertices, edges)
        cases.append(TestCase(
            id=self._make_id("simple", 1),
            scaffold=self.scaffold_name,
            tier="simple",
            input={"vertices": vertices, "edges": edges},
            expected={"order": result.order},
            description="Simple 4-node DAG",
            metadata={"valid_orders_count": 2},  # A,B,C,D or A,C,B,D
        ))

        return cases[:count]

    def generate_standard(self, count: int = 5) -> list[TestCase]:
        """Generate standard topological sort test cases."""
        return []

    def generate_edge_cases(self, count: int = 3) -> list[TestCase]:
        """Generate edge topological sort test cases."""
        return []


# Factory function
def get_graph_generators() -> dict[str, TestCaseGenerator]:
    """Get all graph algorithm test case generators."""
    return {
        "dijkstra": DijkstraGenerator(),
        "bfs": BFSGenerator(),
        "topological_sort": TopologicalSortGenerator(),
    }
