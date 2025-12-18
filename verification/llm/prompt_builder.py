"""
Prompt builder for constructing LLM prompts from scaffolds and test cases.

Parses scaffold markdown files and combines them with test case data
to create complete prompts for verification.
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..config import get_settings


@dataclass
class ParsedScaffold:
    """Parsed scaffold from a markdown file."""

    name: str
    """Algorithm name (e.g., 'Dijkstra')."""

    file_path: Path
    """Path to the scaffold file."""

    when_to_use: str
    """Conditions when this algorithm applies."""

    instructions: str
    """The scaffold instructions section (the actual scaffold)."""

    worked_example: str
    """The worked example section."""

    failure_modes: str
    """Common failure modes section."""

    raw_content: str
    """Full raw markdown content."""


class ScaffoldParser:
    """Parser for scaffold markdown files."""

    # Regex patterns for extracting sections
    SECTION_PATTERNS = {
        "when_to_use": r"##\s*When to Use\s*\n(.*?)(?=\n##|\n---|\Z)",
        "instructions": r"##\s*Scaffold Instructions.*?\n```\s*\n(.*?)\n```",
        "worked_example": r"##\s*Worked Example\s*\n(.*?)(?=\n##\s*Common|\n---\s*\n##|\Z)",
        "failure_modes": r"##\s*Common Failure Modes\s*\n(.*?)(?=\n##|\n---|\Z)",
    }

    def parse_file(self, file_path: Path) -> ParsedScaffold:
        """
        Parse a scaffold markdown file.

        Args:
            file_path: Path to the scaffold markdown file.

        Returns:
            ParsedScaffold with extracted sections.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If required sections are missing.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Scaffold file not found: {file_path}")

        content = file_path.read_text(encoding="utf-8")

        # Extract algorithm name from title
        title_match = re.search(r"#\s*(.+?)\s*Scaffold", content)
        name = title_match.group(1).strip() if title_match else file_path.stem

        # Extract sections
        sections: dict[str, str] = {}
        for section_name, pattern in self.SECTION_PATTERNS.items():
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            sections[section_name] = match.group(1).strip() if match else ""

        if not sections["instructions"]:
            raise ValueError(f"No scaffold instructions found in {file_path}")

        return ParsedScaffold(
            name=name,
            file_path=file_path,
            when_to_use=sections["when_to_use"],
            instructions=sections["instructions"],
            worked_example=sections["worked_example"],
            failure_modes=sections["failure_modes"],
            raw_content=content,
        )

    def list_scaffolds(self, scaffolds_dir: Path | None = None) -> list[Path]:
        """
        List all scaffold files in the scaffolds directory.

        Args:
            scaffolds_dir: Directory containing scaffolds. Uses settings if not provided.

        Returns:
            List of paths to scaffold markdown files.
        """
        if scaffolds_dir is None:
            scaffolds_dir = get_settings().get_scaffolds_path()

        scaffolds = []
        for category_dir in sorted(scaffolds_dir.iterdir()):
            if category_dir.is_dir() and category_dir.name.startswith(("0", "1")):
                for md_file in sorted(category_dir.glob("*.md")):
                    if md_file.name != "README.md":
                        scaffolds.append(md_file)

        return scaffolds


class PromptBuilder:
    """Builder for constructing prompts from scaffolds and test cases."""

    # Output format instructions for different algorithm types
    OUTPUT_FORMATS = {
        "graph_path": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_DISTANCE: <number>
FINAL_PATH: [node1, node2, node3, ...]
""",
        "graph_distances": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_DISTANCES: {"node1": distance1, "node2": distance2, ...}
""",
        "single_value": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_ANSWER: <your answer>
""",
        "list": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_ANSWER: [item1, item2, item3, ...]
""",
        "knapsack": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_VALUE: <maximum value>
FINAL_ITEMS: [item_index1, item_index2, ...]
""",
        "sequence": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_LENGTH: <length>
FINAL_SEQUENCE: [element1, element2, ...]
""",
        "root": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_ROOT: <numerical value>
""",
        "positions": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_POSITIONS: [(row1, col1), (row2, col2), ...]
""",
        "pattern_match": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_MATCHES: [index1, index2, ...] (or [] if no matches)
""",
        "huffman": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_TOTAL_BITS: <number>
FINAL_CODES: {"symbol1": "code1", "symbol2": "code2", ...}
""",
        "sudoku": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_GRID: [[row1], [row2], ..., [row9]]
(where each row is 9 numbers)
If no solution exists, write: FINAL_ANSWER: NO_SOLUTION
""",
        "graph_coloring": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_COLORING: {"node1": color1, "node2": color2, ...}
If no solution exists with the given number of colors, write: FINAL_ANSWER: NO_SOLUTION
""",
        "matrix_chain": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_OPERATIONS: <minimum number of scalar multiplications>
""",
        "trie": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_RESULTS: [result1, result2, ...] (True/False for searches, or list of words for prefix)
""",
        "monte_carlo": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_ESTIMATE: <numerical value>
""",
        "optimization": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_MINIMUM: <minimum value found>
FINAL_SOLUTION: <x value at minimum>
""",
        "activity": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_COUNT: <number of activities selected>
FINAL_ACTIVITIES: [activity_index1, activity_index2, ...]
""",
        "kruskal": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_WEIGHT: <total MST weight>
FINAL_EDGES: [["node1", "node2"], ["node3", "node4"], ...]
""",
        "fractional_knapsack": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_VALUE: <maximum value as decimal>
""",
        "subset_sum": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_SUBSET: [element1, element2, ...] (the subset that sums to target)
If no solution exists, write: FINAL_ANSWER: NO_SOLUTION
""",
        "edit_distance": """
IMPORTANT: After your solution, provide your final answer in EXACTLY this format:
FINAL_DISTANCE: <minimum edit distance>
""",
    }

    # Algorithm to output format mapping
    ALGORITHM_FORMATS = {
        # Graph
        "bfs": "graph_path",
        "dfs": "graph_path",
        "dijkstra": "graph_distances",
        "astar": "graph_path",
        "bellman_ford": "graph_distances",
        "floyd_warshall": "graph_distances",
        "topological_sort": "list",
        "kruskal": "kruskal",
        # Divide & Conquer
        "binary_search": "single_value",
        "merge_sort": "list",
        "quickselect": "single_value",
        # Greedy
        "activity_selection": "activity",
        "huffman": "huffman",
        "fractional_knapsack": "fractional_knapsack",
        # Backtracking
        "nqueens": "positions",
        "sudoku": "sudoku",
        "graph_coloring": "graph_coloring",
        "subset_sum": "subset_sum",
        # DP
        "knapsack_01": "knapsack",
        "lcs": "sequence",
        "edit_distance": "edit_distance",
        "lis": "sequence",
        "matrix_chain": "matrix_chain",
        # String
        "kmp": "pattern_match",
        "rabin_karp": "pattern_match",
        "trie_operations": "trie",
        # Numerical
        "newton_raphson": "root",
        "bisection": "root",
        "monte_carlo": "monte_carlo",
        # Optimization
        "gradient_descent": "optimization",
        "simulated_annealing": "optimization",
        "genetic_algorithm": "optimization",
        "hill_climbing": "optimization",
    }

    def __init__(self):
        self.parser = ScaffoldParser()

    def build_prompt(
        self,
        scaffold: ParsedScaffold,
        test_case: dict[str, Any],
        include_output_format: bool = True,
    ) -> str:
        """
        Build a complete prompt from a scaffold and test case.

        Args:
            scaffold: Parsed scaffold object.
            test_case: Test case dictionary with 'input' key.
            include_output_format: Whether to add output format instructions.

        Returns:
            Complete prompt string.
        """
        parts = [scaffold.instructions]

        # Add problem statement
        problem = self._format_problem(test_case)
        parts.append(f"\nNow solve this specific problem:\n{problem}")

        # Add output format if requested
        if include_output_format:
            algorithm_key = scaffold.file_path.stem.lower()
            format_key = self.ALGORITHM_FORMATS.get(algorithm_key, "single_value")
            parts.append(self.OUTPUT_FORMATS[format_key])

        return "\n".join(parts)

    def _format_problem(self, test_case: dict[str, Any]) -> str:
        """Format a test case input as a problem statement."""
        input_data = test_case.get("input", test_case)

        lines = []
        for key, value in input_data.items():
            if isinstance(value, list):
                if value and isinstance(value[0], list):
                    # List of lists (e.g., edges)
                    formatted = ", ".join(str(item) for item in value)
                    lines.append(f"- {key}: {formatted}")
                else:
                    lines.append(f"- {key}: {value}")
            elif isinstance(value, dict):
                lines.append(f"- {key}: {value}")
            else:
                lines.append(f"- {key}: {value}")

        return "\n".join(lines)

    def build_system_prompt(self) -> str:
        """Build the system prompt for verification runs."""
        return """You are an algorithm execution assistant. Your task is to:
1. Follow the algorithm scaffold instructions EXACTLY as written
2. Show your work step-by-step, including state tables where applicable
3. Provide your final answer in the EXACT format specified at the end of the prompt

Be precise and systematic. Do not skip steps or make assumptions not stated in the problem."""


def get_prompt_builder() -> PromptBuilder:
    """Factory function to create a prompt builder."""
    return PromptBuilder()
