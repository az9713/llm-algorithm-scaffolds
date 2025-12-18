"""
Reference implementations for greedy algorithms.

Implements: Activity Selection, Huffman Coding, Kruskal's MST, Fractional Knapsack.
"""

import heapq
from dataclasses import dataclass
from typing import Any

import networkx as nx


@dataclass
class GreedyResult:
    """Result from a greedy algorithm."""

    value: Any
    """The result (count, total value, etc.)."""

    solution: Any = None
    """The actual solution (selected items, tree edges, etc.)."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        result = {"value": self.value}
        if self.solution is not None:
            result["solution"] = self.solution
        return result


def activity_selection(
    activities: list[tuple[int, int]] | list[tuple[str, int, int]],
) -> GreedyResult:
    """
    Activity Selection Problem - select maximum non-overlapping activities.

    Args:
        activities: List of (start, end) or (name, start, end) tuples.

    Returns:
        GreedyResult with count and selected activities.
    """
    if not activities:
        return GreedyResult(value=0, solution=[])

    # Normalize to (name, start, end) format
    if len(activities[0]) == 2:
        activities = [(i, a[0], a[1]) for i, a in enumerate(activities)]

    # Sort by end time
    sorted_activities = sorted(activities, key=lambda x: x[2])

    selected = []
    last_end = float("-inf")

    for activity in sorted_activities:
        name, start, end = activity
        if start >= last_end:
            selected.append(activity)
            last_end = end

    return GreedyResult(
        value=len(selected),
        solution=selected,
    )


@dataclass
class HuffmanNode:
    """Node in a Huffman tree."""

    freq: int
    char: str | None = None
    left: "HuffmanNode | None" = None
    right: "HuffmanNode | None" = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        return self.freq < other.freq


def huffman_coding(
    frequencies: dict[str, int],
) -> GreedyResult:
    """
    Huffman Coding - build optimal prefix-free binary codes.

    Args:
        frequencies: Dictionary mapping characters to frequencies.

    Returns:
        GreedyResult with total weighted path length and character codes.
    """
    if not frequencies:
        return GreedyResult(value=0, solution={})

    if len(frequencies) == 1:
        char = list(frequencies.keys())[0]
        return GreedyResult(value=frequencies[char], solution={char: "0"})

    # Build priority queue of leaf nodes
    heap = [HuffmanNode(freq=freq, char=char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heap[0]

    # Generate codes by traversing tree
    codes: dict[str, str] = {}

    def generate_codes(node: HuffmanNode, code: str) -> None:
        if node.char is not None:
            codes[node.char] = code
            return
        if node.left:
            generate_codes(node.left, code + "0")
        if node.right:
            generate_codes(node.right, code + "1")

    generate_codes(root, "")

    # Calculate weighted path length (total bits)
    total_bits = sum(frequencies[char] * len(code) for char, code in codes.items())

    return GreedyResult(
        value=total_bits,
        solution=codes,
    )


def kruskal_mst(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
) -> GreedyResult:
    """
    Kruskal's algorithm for Minimum Spanning Tree.

    Args:
        vertices: List of vertex names.
        edges: List of (u, v, weight) edges.

    Returns:
        GreedyResult with total weight and MST edges.
    """
    # Use networkx for correctness
    G = nx.Graph()
    G.add_nodes_from(vertices)

    for edge in edges:
        if len(edge) == 3:
            u, v, w = edge
            G.add_edge(u, v, weight=w)
        else:
            u, v = edge
            G.add_edge(u, v, weight=1)

    # Check if graph is connected
    if not nx.is_connected(G):
        # Return MST of largest connected component
        largest_cc = max(nx.connected_components(G), key=len)
        G = G.subgraph(largest_cc).copy()

    # Get MST using networkx
    mst = nx.minimum_spanning_tree(G, weight="weight")

    mst_edges = [(u, v, mst[u][v]["weight"]) for u, v in mst.edges()]
    total_weight = sum(w for _, _, w in mst_edges)

    return GreedyResult(
        value=total_weight,
        solution=mst_edges,
    )


def fractional_knapsack(
    values: list[float],
    weights: list[float],
    capacity: float,
) -> GreedyResult:
    """
    Fractional Knapsack - select items (with fractions) to maximize value.

    Args:
        values: List of item values.
        weights: List of item weights.
        capacity: Maximum weight capacity.

    Returns:
        GreedyResult with maximum value and fractions taken.
    """
    if not values or capacity <= 0:
        return GreedyResult(value=0.0, solution=[])

    n = len(values)

    # Calculate value-to-weight ratio for each item
    items = [(i, values[i], weights[i], values[i] / weights[i] if weights[i] > 0 else float("inf"))
             for i in range(n)]

    # Sort by ratio in descending order
    items.sort(key=lambda x: x[3], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    fractions = [0.0] * n

    for idx, val, wt, ratio in items:
        if remaining_capacity <= 0:
            break

        if wt <= remaining_capacity:
            # Take entire item
            fractions[idx] = 1.0
            total_value += val
            remaining_capacity -= wt
        else:
            # Take fraction of item
            fraction = remaining_capacity / wt
            fractions[idx] = fraction
            total_value += val * fraction
            remaining_capacity = 0

    return GreedyResult(
        value=total_value,
        solution=fractions,
    )


# Convenience function to run any greedy algorithm
def run_greedy_algorithm(
    algorithm: str,
    **kwargs,
) -> GreedyResult:
    """
    Run a greedy algorithm by name.

    Args:
        algorithm: Algorithm name (activity_selection, huffman, kruskal, fractional_knapsack).
        **kwargs: Algorithm-specific arguments.

    Returns:
        GreedyResult from the algorithm.
    """
    algorithms = {
        "activity_selection": activity_selection,
        "huffman": huffman_coding,
        "huffman_coding": huffman_coding,
        "kruskal": kruskal_mst,
        "kruskal_mst": kruskal_mst,
        "fractional_knapsack": fractional_knapsack,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm == "activity_selection":
        return func(kwargs["activities"])
    elif algorithm in ("huffman", "huffman_coding"):
        return func(kwargs["frequencies"])
    elif algorithm in ("kruskal", "kruskal_mst"):
        return func(kwargs["vertices"], kwargs["edges"])
    elif algorithm == "fractional_knapsack":
        return func(kwargs["values"], kwargs["weights"], kwargs["capacity"])
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
