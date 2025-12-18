"""
Reference implementations for backtracking algorithms.

Implements: N-Queens, Sudoku, Graph Coloring, Subset Sum.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class BacktrackingResult:
    """Result from a backtracking algorithm."""

    found: bool
    """Whether a solution was found."""

    solution: Any = None
    """The solution (positions, grid, colors, subset, etc.)."""

    all_solutions: list | None = None
    """All solutions if requested."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        result = {"found": self.found}
        if self.solution is not None:
            result["solution"] = self.solution
        if self.all_solutions is not None:
            result["all_solutions"] = self.all_solutions
        return result


def nqueens(
    n: int,
    find_all: bool = False,
) -> BacktrackingResult:
    """
    N-Queens Problem - place N queens on NxN board with no conflicts.

    Args:
        n: Board size.
        find_all: If True, find all solutions.

    Returns:
        BacktrackingResult with queen positions as list of (row, col) tuples.
    """
    if n <= 0:
        return BacktrackingResult(found=False)

    solutions = []

    def is_safe(board: list[int], row: int, col: int) -> bool:
        """Check if placing queen at (row, col) is safe."""
        for r in range(row):
            c = board[r]
            # Same column
            if c == col:
                return False
            # Diagonal
            if abs(r - row) == abs(c - col):
                return False
        return True

    def solve(board: list[int], row: int) -> bool:
        """Recursively place queens."""
        if row == n:
            solutions.append([(r, board[r]) for r in range(n)])
            return not find_all  # Return True to stop if not finding all

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if solve(board, row + 1):
                    return True
                board[row] = -1

        return False

    board = [-1] * n
    solve(board, 0)

    if solutions:
        return BacktrackingResult(
            found=True,
            solution=solutions[0],
            all_solutions=solutions if find_all else None,
        )
    else:
        return BacktrackingResult(found=False)


def sudoku(
    grid: list[list[int]],
) -> BacktrackingResult:
    """
    Sudoku Solver - fill 9x9 grid with digits 1-9.

    Args:
        grid: 9x9 grid with 0 representing empty cells.

    Returns:
        BacktrackingResult with solved grid.
    """
    # Make a copy
    board = [row[:] for row in grid]

    def is_valid(row: int, col: int, num: int) -> bool:
        """Check if placing num at (row, col) is valid."""
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[r][col] for r in range(9)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def find_empty() -> tuple[int, int] | None:
        """Find next empty cell."""
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return None

    def solve() -> bool:
        """Recursively solve the sudoku."""
        empty = find_empty()
        if empty is None:
            return True  # Solved

        row, col = empty
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                if solve():
                    return True
                board[row][col] = 0

        return False

    if solve():
        return BacktrackingResult(found=True, solution=board)
    else:
        return BacktrackingResult(found=False)


def graph_coloring(
    vertices: list[str],
    edges: list[tuple[str, str]],
    num_colors: int,
) -> BacktrackingResult:
    """
    Graph Coloring - assign colors to vertices so no adjacent vertices share a color.

    Args:
        vertices: List of vertex names.
        edges: List of (u, v) edges.
        num_colors: Number of available colors.

    Returns:
        BacktrackingResult with color assignment dict.
    """
    if not vertices:
        return BacktrackingResult(found=True, solution={})

    # Build adjacency list
    adj = {v: [] for v in vertices}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    colors = {v: 0 for v in vertices}

    def is_safe(vertex: str, color: int) -> bool:
        """Check if vertex can be assigned color."""
        for neighbor in adj[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    def solve(idx: int) -> bool:
        """Recursively assign colors."""
        if idx == len(vertices):
            return True

        vertex = vertices[idx]
        for color in range(1, num_colors + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                if solve(idx + 1):
                    return True
                colors[vertex] = 0

        return False

    if solve(0):
        return BacktrackingResult(found=True, solution=dict(colors))
    else:
        return BacktrackingResult(found=False)


def subset_sum(
    numbers: list[int],
    target: int,
    find_all: bool = False,
) -> BacktrackingResult:
    """
    Subset Sum - find subset that sums to target.

    Args:
        numbers: List of numbers.
        target: Target sum.
        find_all: If True, find all subsets.

    Returns:
        BacktrackingResult with subset (list of numbers or indices).
    """
    solutions = []

    def solve(idx: int, current_sum: int, subset: list[int]) -> bool:
        """Recursively find subsets."""
        if current_sum == target:
            solutions.append(subset[:])
            return not find_all

        if idx >= len(numbers) or current_sum > target:
            return False

        # Include current number
        subset.append(numbers[idx])
        if solve(idx + 1, current_sum + numbers[idx], subset):
            return True
        subset.pop()

        # Exclude current number
        if solve(idx + 1, current_sum, subset):
            return True

        return False

    solve(0, 0, [])

    if solutions:
        return BacktrackingResult(
            found=True,
            solution=solutions[0],
            all_solutions=solutions if find_all else None,
        )
    else:
        return BacktrackingResult(found=False)


# Convenience function to run any backtracking algorithm
def run_backtracking_algorithm(
    algorithm: str,
    **kwargs,
) -> BacktrackingResult:
    """
    Run a backtracking algorithm by name.

    Args:
        algorithm: Algorithm name (nqueens, sudoku, graph_coloring, subset_sum).
        **kwargs: Algorithm-specific arguments.

    Returns:
        BacktrackingResult from the algorithm.
    """
    algorithms = {
        "nqueens": nqueens,
        "n_queens": nqueens,
        "sudoku": sudoku,
        "graph_coloring": graph_coloring,
        "subset_sum": subset_sum,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm in ("nqueens", "n_queens"):
        return func(kwargs["n"], kwargs.get("find_all", False))
    elif algorithm == "sudoku":
        return func(kwargs["grid"])
    elif algorithm == "graph_coloring":
        return func(kwargs["vertices"], kwargs["edges"], kwargs["num_colors"])
    elif algorithm == "subset_sum":
        return func(kwargs["numbers"], kwargs["target"], kwargs.get("find_all", False))
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
