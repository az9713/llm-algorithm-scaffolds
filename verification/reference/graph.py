"""
Reference implementations for graph algorithms.

Uses networkx as the trusted library for ground truth.
"""

from collections import deque
from dataclasses import dataclass
from typing import Any, Callable

import networkx as nx


@dataclass
class GraphResult:
    """Result from a graph algorithm."""

    distances: dict[str, float] | None = None
    """Shortest distances from source."""

    path: list[str] | None = None
    """Path from source to target."""

    predecessors: dict[str, str | None] | None = None
    """Predecessor map for path reconstruction."""

    order: list[str] | None = None
    """Ordering (for topological sort)."""

    distance_matrix: dict[str, dict[str, float]] | None = None
    """All-pairs distances (for Floyd-Warshall)."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        result = {}
        if self.distances is not None:
            result["distances"] = self.distances
        if self.path is not None:
            result["path"] = self.path
        if self.order is not None:
            result["order"] = self.order
        if self.distance_matrix is not None:
            result["distance_matrix"] = self.distance_matrix
        return result


def build_graph(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    directed: bool = True,
) -> nx.DiGraph | nx.Graph:
    """
    Build a networkx graph from vertices and edges.

    Args:
        vertices: List of vertex names.
        edges: List of (source, target, weight) tuples or lists.
        directed: Whether the graph is directed.

    Returns:
        networkx graph object.
    """
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_nodes_from(vertices)

    for edge in edges:
        if len(edge) == 3:
            u, v, w = edge
            G.add_edge(u, v, weight=w)
        else:
            u, v = edge
            G.add_edge(u, v, weight=1)

    return G


def bfs(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    source: str,
    target: str | None = None,
    directed: bool = True,
) -> GraphResult:
    """
    Breadth-First Search for shortest path in unweighted graph.

    Args:
        vertices: List of vertex names.
        edges: List of edges (weight is ignored, treated as 1).
        source: Source vertex.
        target: Target vertex (optional).
        directed: Whether the graph is directed.

    Returns:
        GraphResult with distances and optional path.
    """
    G = build_graph(vertices, edges, directed)

    # BFS for shortest paths
    distances = {source: 0}
    predecessors = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if v not in distances:
                distances[v] = distances[u] + 1
                predecessors[v] = u
                queue.append(v)

    # Build path to target if specified
    path = None
    if target is not None and target in distances:
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()

    # Set unreachable vertices to infinity
    for v in vertices:
        if v not in distances:
            distances[v] = float("inf")

    return GraphResult(
        distances=distances,
        path=path,
        predecessors=predecessors,
    )


def dfs(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    source: str,
    target: str | None = None,
    directed: bool = True,
) -> GraphResult:
    """
    Depth-First Search for path finding.

    Note: DFS does NOT guarantee shortest path.

    Args:
        vertices: List of vertex names.
        edges: List of edges.
        source: Source vertex.
        target: Target vertex (optional).
        directed: Whether the graph is directed.

    Returns:
        GraphResult with path if found.
    """
    G = build_graph(vertices, edges, directed)

    visited = set()
    predecessors = {source: None}

    def dfs_recursive(u: str) -> bool:
        visited.add(u)
        if target is not None and u == target:
            return True
        for v in G.neighbors(u):
            if v not in visited:
                predecessors[v] = u
                if dfs_recursive(v):
                    return True
        return False

    found = dfs_recursive(source)

    path = None
    if target is not None and found:
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = predecessors.get(current)
        path.reverse()

    return GraphResult(
        path=path,
        predecessors=predecessors,
    )


def dijkstra(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    source: str,
    target: str | None = None,
    directed: bool = True,
) -> GraphResult:
    """
    Dijkstra's algorithm for shortest paths with non-negative weights.

    Args:
        vertices: List of vertex names.
        edges: List of (source, target, weight) edges.
        source: Source vertex.
        target: Target vertex (optional).
        directed: Whether the graph is directed.

    Returns:
        GraphResult with distances and optional path.
    """
    G = build_graph(vertices, edges, directed)

    # Use networkx implementation
    if target is not None:
        try:
            path = nx.dijkstra_path(G, source, target, weight="weight")
            length = nx.dijkstra_path_length(G, source, target, weight="weight")
            distances = dict(nx.single_source_dijkstra_path_length(G, source, weight="weight"))

            # Set unreachable to infinity
            for v in vertices:
                if v not in distances:
                    distances[v] = float("inf")

            return GraphResult(
                distances=distances,
                path=path,
            )
        except nx.NetworkXNoPath:
            distances = dict(nx.single_source_dijkstra_path_length(G, source, weight="weight"))
            for v in vertices:
                if v not in distances:
                    distances[v] = float("inf")
            return GraphResult(distances=distances, path=None)
    else:
        distances = dict(nx.single_source_dijkstra_path_length(G, source, weight="weight"))
        for v in vertices:
            if v not in distances:
                distances[v] = float("inf")
        return GraphResult(distances=distances)


def astar(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    source: str,
    target: str,
    heuristic: Callable[[str, str], float] | dict[str, float] | None = None,
    directed: bool = True,
) -> GraphResult:
    """
    A* algorithm for shortest path with heuristic.

    Args:
        vertices: List of vertex names.
        edges: List of (source, target, weight) edges.
        source: Source vertex.
        target: Target vertex.
        heuristic: Heuristic function h(n, target) or dict of h values.
        directed: Whether the graph is directed.

    Returns:
        GraphResult with path.
    """
    G = build_graph(vertices, edges, directed)

    # Convert heuristic dict to function if needed
    if isinstance(heuristic, dict):
        h_dict = heuristic

        def h_func(n: str, t: str) -> float:
            return h_dict.get(n, 0)

        heuristic = h_func
    elif heuristic is None:
        # Default: zero heuristic (equivalent to Dijkstra)
        def h_func(n: str, t: str) -> float:
            return 0

        heuristic = h_func

    try:
        path = nx.astar_path(G, source, target, heuristic=heuristic, weight="weight")
        return GraphResult(path=path)
    except nx.NetworkXNoPath:
        return GraphResult(path=None)


def bellman_ford(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    source: str,
    directed: bool = True,
) -> GraphResult:
    """
    Bellman-Ford algorithm for shortest paths (handles negative weights).

    Args:
        vertices: List of vertex names.
        edges: List of (source, target, weight) edges.
        source: Source vertex.
        directed: Whether the graph is directed.

    Returns:
        GraphResult with distances, or None if negative cycle exists.

    Raises:
        ValueError: If a negative cycle is detected.
    """
    G = build_graph(vertices, edges, directed)

    try:
        distances, predecessors = nx.single_source_bellman_ford(G, source, weight="weight")

        # Convert predecessors to simple dict
        pred_dict = {v: predecessors.get(v, [None])[-1] if predecessors.get(v) else None
                     for v in vertices}

        # Set unreachable to infinity
        for v in vertices:
            if v not in distances:
                distances[v] = float("inf")

        return GraphResult(
            distances=dict(distances),
            predecessors=pred_dict,
        )
    except nx.NetworkXUnbounded:
        raise ValueError("Negative cycle detected")


def floyd_warshall(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
    directed: bool = True,
) -> GraphResult:
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.

    Args:
        vertices: List of vertex names.
        edges: List of (source, target, weight) edges.
        directed: Whether the graph is directed.

    Returns:
        GraphResult with distance matrix.
    """
    G = build_graph(vertices, edges, directed)

    # Use networkx implementation
    distances = dict(nx.floyd_warshall(G, weight="weight"))

    # Convert to nested dict with string keys
    distance_matrix = {}
    for u in vertices:
        distance_matrix[u] = {}
        for v in vertices:
            if u in distances and v in distances[u]:
                distance_matrix[u][v] = distances[u][v]
            else:
                distance_matrix[u][v] = float("inf") if u != v else 0

    return GraphResult(distance_matrix=distance_matrix)


def topological_sort(
    vertices: list[str],
    edges: list[tuple[str, str, float] | list],
) -> GraphResult:
    """
    Topological sort for directed acyclic graphs.

    Args:
        vertices: List of vertex names.
        edges: List of edges (weights ignored).

    Returns:
        GraphResult with ordering.

    Raises:
        ValueError: If graph has a cycle.
    """
    G = build_graph(vertices, edges, directed=True)

    try:
        order = list(nx.topological_sort(G))
        return GraphResult(order=order)
    except nx.NetworkXUnfeasible:
        raise ValueError("Graph contains a cycle, topological sort not possible")


# Convenience function to run any graph algorithm
def run_graph_algorithm(
    algorithm: str,
    vertices: list[str],
    edges: list,
    source: str | None = None,
    target: str | None = None,
    directed: bool = True,
    **kwargs,
) -> GraphResult:
    """
    Run a graph algorithm by name.

    Args:
        algorithm: Algorithm name (bfs, dfs, dijkstra, astar, bellman_ford,
                   floyd_warshall, topological_sort).
        vertices: List of vertex names.
        edges: List of edges.
        source: Source vertex (required for most algorithms).
        target: Target vertex (optional).
        directed: Whether the graph is directed.
        **kwargs: Additional algorithm-specific arguments.

    Returns:
        GraphResult from the algorithm.
    """
    algorithms = {
        "bfs": bfs,
        "dfs": dfs,
        "dijkstra": dijkstra,
        "astar": astar,
        "bellman_ford": bellman_ford,
        "floyd_warshall": floyd_warshall,
        "topological_sort": topological_sort,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm == "floyd_warshall":
        return func(vertices, edges, directed)
    elif algorithm == "topological_sort":
        return func(vertices, edges)
    elif algorithm == "astar":
        return func(vertices, edges, source, target, kwargs.get("heuristic"), directed)
    elif algorithm in ("bfs", "dfs", "dijkstra"):
        return func(vertices, edges, source, target, directed)
    elif algorithm == "bellman_ford":
        return func(vertices, edges, source, directed)
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
