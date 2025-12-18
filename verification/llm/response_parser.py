"""
Response parser for extracting structured answers from LLM responses.

Handles various output formats and provides parsed results for validation.
"""

import ast
import json
import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParsedAnswer:
    """Parsed answer from an LLM response."""

    raw_response: str
    """The full raw response from the LLM."""

    answer: Any
    """The extracted answer (type depends on algorithm)."""

    answer_type: str
    """Type of answer extracted (e.g., 'distance', 'path', 'value')."""

    confidence: float = 1.0
    """Confidence in the parsing (1.0 = found exact format, 0.5 = fuzzy match)."""

    parse_error: str | None = None
    """Error message if parsing failed."""

    metadata: dict[str, Any] = field(default_factory=dict)
    """Additional extracted data (e.g., intermediate steps, paths, etc.)."""

    @property
    def is_valid(self) -> bool:
        """Check if parsing was successful."""
        return self.parse_error is None and self.answer is not None


class ResponseParser:
    """Parser for extracting answers from LLM responses."""

    # Patterns for different answer types
    PATTERNS = {
        "distance": r"FINAL_DISTANCE:\s*(\d+(?:\.\d+)?)",
        "distances": r"FINAL_DISTANCES:\s*(\{[^}]+\})",
        "path": r"FINAL_PATH:\s*\[([^\]]+)\]",
        "answer": r"FINAL_ANSWER:\s*(.+?)(?:\n|$)",
        "value": r"FINAL_VALUE:\s*(\d+(?:\.\d+)?)",
        "items": r"FINAL_ITEMS:\s*\[([^\]]*)\]",
        "length": r"FINAL_LENGTH:\s*(\d+)",
        "sequence": r"FINAL_SEQUENCE:\s*\[([^\]]+)\]",
        "root": r"FINAL_ROOT:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)",
        "positions": r"FINAL_POSITIONS:\s*\[([^\]]+)\]",
        "matches": r"FINAL_MATCHES:\s*\[([^\]]*)\]",
        # New patterns for specific algorithms
        "total_bits": r"FINAL_TOTAL_BITS:\s*(\d+)",
        "codes": r"FINAL_CODES:\s*(\{[^}]+\})",
        "grid": r"FINAL_GRID:\s*(\[\[.+?\]\])",
        "coloring": r"FINAL_COLORING:\s*(\{[^}]+\})",
        "operations": r"FINAL_OPERATIONS:\s*(\d+)",
        "results": r"FINAL_RESULTS:\s*\[([^\]]*)\]",
        "estimate": r"FINAL_ESTIMATE:\s*(-?\d+\.?\d*)",
        "minimum": r"FINAL_MINIMUM:\s*(-?\d+\.?\d*(?:[eE][+-]?\d+)?)",
        "solution": r"FINAL_SOLUTION:\s*(-?\d+\.?\d*(?:[eE][+-]?\d+)?)",
        "count": r"FINAL_COUNT:\s*(\d+)",
        "activities": r"FINAL_ACTIVITIES:\s*\[([^\]]*)\]",
        "weight": r"FINAL_WEIGHT:\s*(\d+(?:\.\d+)?)",
        "edges": r"FINAL_EDGES:\s*(\[\[.+?\]\])",
        "subset": r"FINAL_SUBSET:\s*\[([^\]]*)\]",
    }

    def parse(self, response: str, algorithm: str) -> ParsedAnswer:
        """
        Parse an LLM response to extract the answer.

        Args:
            response: The raw LLM response text.
            algorithm: The algorithm name (e.g., 'dijkstra', 'knapsack_01').

        Returns:
            ParsedAnswer with extracted data.
        """
        algorithm = algorithm.lower().replace("-", "_")

        # Route to specialized parsers
        parser_map = {
            # Graph algorithms
            "dijkstra": self._parse_distances,
            "bellman_ford": self._parse_distances,
            "floyd_warshall": self._parse_all_pairs_distances,
            "bfs": self._parse_bfs,
            "dfs": self._parse_dfs,
            "astar": self._parse_astar,
            "topological_sort": self._parse_topological,

            # Divide & Conquer
            "binary_search": self._parse_binary_search,
            "merge_sort": self._parse_merge_sort,
            "quickselect": self._parse_quickselect,

            # Greedy
            "activity_selection": self._parse_activity,
            "huffman": self._parse_huffman,
            "kruskal": self._parse_kruskal,
            "fractional_knapsack": self._parse_fractional_knapsack,

            # DP
            "knapsack_01": self._parse_knapsack,
            "lcs": self._parse_sequence,
            "edit_distance": self._parse_edit_distance,
            "lis": self._parse_sequence,
            "matrix_chain": self._parse_matrix_chain,

            # Backtracking
            "nqueens": self._parse_nqueens,
            "sudoku": self._parse_sudoku,
            "graph_coloring": self._parse_graph_coloring,
            "subset_sum": self._parse_subset_sum,

            # String
            "kmp": self._parse_matches,
            "rabin_karp": self._parse_matches,
            "trie_operations": self._parse_trie,

            # Numerical
            "newton_raphson": self._parse_root,
            "bisection": self._parse_root,
            "monte_carlo": self._parse_monte_carlo,

            # Optimization
            "gradient_descent": self._parse_optimization,
            "simulated_annealing": self._parse_optimization,
            "genetic_algorithm": self._parse_optimization,
            "hill_climbing": self._parse_optimization,
        }

        parser = parser_map.get(algorithm, self._parse_generic)
        return parser(response)

    def _parse_distances(self, response: str) -> ParsedAnswer:
        """Parse single-source shortest path distances."""
        # Try FINAL_DISTANCES format first
        match = re.search(self.PATTERNS["distances"], response, re.IGNORECASE)
        if match:
            try:
                distances = self._safe_eval_dict(match.group(1))
                return ParsedAnswer(
                    raw_response=response,
                    answer={"distances": distances},
                    answer_type="distances",
                )
            except Exception as e:
                pass

        # Try to extract from table or other format
        distances = self._extract_distances_from_text(response)
        if distances:
            return ParsedAnswer(
                raw_response=response,
                answer={"distances": distances},
                answer_type="distances",
                confidence=0.7,
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="distances",
            parse_error="Could not extract distances from response",
        )

    def _parse_all_pairs_distances(self, response: str) -> ParsedAnswer:
        """Parse all-pairs shortest path distances (Floyd-Warshall)."""
        # Try to find distance matrix
        distances = self._extract_matrix_from_text(response)
        if distances:
            return ParsedAnswer(
                raw_response=response,
                answer={"distance_matrix": distances},
                answer_type="distance_matrix",
            )

        # Fall back to single-source distances format
        result = self._parse_distances(response)
        if result.answer:
            # Convert to distance_matrix format
            return ParsedAnswer(
                raw_response=response,
                answer={"distance_matrix": result.answer.get("distances", {})},
                answer_type="distance_matrix",
            )
        return result

    def _parse_path(self, response: str) -> ParsedAnswer:
        """Parse a path result (raw list for generic use)."""
        metadata = {}

        # Try to get distance
        dist_match = re.search(self.PATTERNS["distance"], response, re.IGNORECASE)
        if dist_match:
            metadata["distance"] = float(dist_match.group(1))

        # Get path
        path_match = re.search(self.PATTERNS["path"], response, re.IGNORECASE)
        if path_match:
            path = self._parse_list_content(path_match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer=path,
                answer_type="path",
                metadata=metadata,
            )

        # Try to extract path from text
        path = self._extract_path_from_text(response)
        if path:
            return ParsedAnswer(
                raw_response=response,
                answer=path,
                answer_type="path",
                confidence=0.7,
                metadata=metadata,
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="path",
            parse_error="Could not extract path from response",
        )

    def _parse_bfs(self, response: str) -> ParsedAnswer:
        """Parse BFS result with path and distances."""
        # Get distances
        distances = self._extract_distances_from_text(response)

        # Get path
        path_match = re.search(self.PATTERNS["path"], response, re.IGNORECASE)
        path = []
        if path_match:
            path = self._parse_list_content(path_match.group(1))
        else:
            path = self._extract_path_from_text(response) or []

        if path or distances:
            return ParsedAnswer(
                raw_response=response,
                answer={"path": path, "distances": distances or {}},
                answer_type="bfs",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="bfs",
            parse_error="Could not extract BFS result from response",
        )

    def _parse_dfs(self, response: str) -> ParsedAnswer:
        """Parse DFS result with path and distances."""
        # Same structure as BFS
        return self._parse_bfs(response)

    def _parse_astar(self, response: str) -> ParsedAnswer:
        """Parse A* result with path."""
        path_match = re.search(self.PATTERNS["path"], response, re.IGNORECASE)
        if path_match:
            path = self._parse_list_content(path_match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"path": path},
                answer_type="astar",
            )

        path = self._extract_path_from_text(response)
        if path:
            return ParsedAnswer(
                raw_response=response,
                answer={"path": path},
                answer_type="astar",
                confidence=0.7,
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="astar",
            parse_error="Could not extract A* path from response",
        )

    def _parse_topological(self, response: str) -> ParsedAnswer:
        """Parse topological sort result."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content.startswith("["):
                items = self._safe_eval_list(content)
                if items is not None:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"order": items},
                        answer_type="topological",
                    )

        # Try path pattern as fallback
        path_match = re.search(self.PATTERNS["path"], response, re.IGNORECASE)
        if path_match:
            order = self._parse_list_content(path_match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"order": order},
                answer_type="topological",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="topological",
            parse_error="Could not extract topological order from response",
        )

    def _parse_single_value(self, response: str) -> ParsedAnswer:
        """Parse a single value answer."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            # Try to convert to number
            try:
                if "." in value:
                    return ParsedAnswer(
                        raw_response=response,
                        answer=float(value),
                        answer_type="value",
                    )
                else:
                    return ParsedAnswer(
                        raw_response=response,
                        answer=int(value),
                        answer_type="value",
                    )
            except ValueError:
                return ParsedAnswer(
                    raw_response=response,
                    answer=value,
                    answer_type="value",
                )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="value",
            parse_error="Could not extract answer from response",
        )

    def _parse_list(self, response: str) -> ParsedAnswer:
        """Parse a list answer."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content.startswith("["):
                items = self._safe_eval_list(content)
                if items is not None:
                    return ParsedAnswer(
                        raw_response=response,
                        answer=items,
                        answer_type="list",
                    )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="list",
            parse_error="Could not extract list from response",
        )

    def _parse_knapsack(self, response: str) -> ParsedAnswer:
        """Parse knapsack result (value and items)."""
        metadata = {}

        value_match = re.search(self.PATTERNS["value"], response, re.IGNORECASE)
        if value_match:
            metadata["value"] = int(float(value_match.group(1)))

        items_match = re.search(self.PATTERNS["items"], response, re.IGNORECASE)
        items = []
        if items_match:
            items = self._parse_list_content(items_match.group(1))

        if "value" in metadata:
            return ParsedAnswer(
                raw_response=response,
                answer={"value": metadata["value"], "items": items},
                answer_type="knapsack",
                metadata=metadata,
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="knapsack",
            parse_error="Could not extract knapsack result",
        )

    def _parse_sequence(self, response: str) -> ParsedAnswer:
        """Parse sequence result (length and elements)."""
        metadata = {}

        length_match = re.search(self.PATTERNS["length"], response, re.IGNORECASE)
        if length_match:
            metadata["length"] = int(length_match.group(1))

        seq_match = re.search(self.PATTERNS["sequence"], response, re.IGNORECASE)
        sequence = []
        if seq_match:
            sequence = self._parse_list_content(seq_match.group(1))

        if "length" in metadata or sequence:
            return ParsedAnswer(
                raw_response=response,
                answer={"length": metadata.get("length", len(sequence)), "sequence": sequence},
                answer_type="sequence",
                metadata=metadata,
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="sequence",
            parse_error="Could not extract sequence result",
        )

    def _parse_root(self, response: str) -> ParsedAnswer:
        """Parse root-finding result."""
        match = re.search(self.PATTERNS["root"], response, re.IGNORECASE)
        if match:
            return ParsedAnswer(
                raw_response=response,
                answer={"root": float(match.group(1))},
                answer_type="root",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="root",
            parse_error="Could not extract root from response",
        )

    def _parse_positions(self, response: str) -> ParsedAnswer:
        """Parse positions (e.g., N-Queens)."""
        match = re.search(self.PATTERNS["positions"], response, re.IGNORECASE)
        if match:
            content = match.group(1)
            positions = self._parse_tuple_list(content)
            if positions:
                return ParsedAnswer(
                    raw_response=response,
                    answer=positions,
                    answer_type="positions",
                )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="positions",
            parse_error="Could not extract positions from response",
        )

    def _parse_matches(self, response: str) -> ParsedAnswer:
        """Parse pattern matching result."""
        match = re.search(self.PATTERNS["matches"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if not content:
                return ParsedAnswer(
                    raw_response=response,
                    answer={"matches": []},
                    answer_type="matches",
                )
            matches = self._parse_list_content(content)
            return ParsedAnswer(
                raw_response=response,
                answer={"matches": [int(m) for m in matches if str(m).isdigit()]},
                answer_type="matches",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="matches",
            parse_error="Could not extract matches from response",
        )

    def _parse_edges(self, response: str) -> ParsedAnswer:
        """Parse edge list (e.g., MST)."""
        return self._parse_list(response)

    def _parse_huffman(self, response: str) -> ParsedAnswer:
        """Parse Huffman coding result."""
        total_bits = 0
        codes = {}

        # Try new pattern first: FINAL_TOTAL_BITS and FINAL_CODES
        bits_match = re.search(self.PATTERNS["total_bits"], response, re.IGNORECASE)
        if bits_match:
            total_bits = int(bits_match.group(1))

        codes_match = re.search(self.PATTERNS["codes"], response, re.IGNORECASE)
        if codes_match:
            try:
                codes = self._safe_eval_dict(codes_match.group(1))
            except ValueError:
                pass

        # Fallback: Look for other patterns
        if not total_bits:
            bits_match = re.search(r"(?:total[_\s]*bits|bits|weighted[_\s]*path[_\s]*length|WPL)\s*[=:]\s*(\d+)", response, re.IGNORECASE)
            if bits_match:
                total_bits = int(bits_match.group(1))

        if not codes:
            codes_match = re.search(r"codes?\s*[=:]\s*(\{[^}]+\})", response, re.IGNORECASE)
            if codes_match:
                try:
                    codes = self._safe_eval_dict(codes_match.group(1))
                except ValueError:
                    pass

        # Try to extract codes from a table format
        if not codes:
            # Look for patterns like "A: 0" or "Symbol | Code" tables
            table_pattern = r"([A-Za-z])\s*[:|]\s*([01]+)"
            table_matches = re.findall(table_pattern, response)
            if table_matches:
                codes = {m[0]: m[1] for m in table_matches}

        if total_bits or codes:
            return ParsedAnswer(
                raw_response=response,
                answer={"total_bits": total_bits, "codes": codes},
                answer_type="huffman",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="huffman",
            parse_error="Could not extract Huffman result from response",
        )

    def _parse_sudoku(self, response: str) -> ParsedAnswer:
        """Parse Sudoku result."""
        # Try FINAL_GRID pattern first
        grid_match = re.search(self.PATTERNS["grid"], response, re.IGNORECASE | re.DOTALL)
        if grid_match:
            try:
                grid = self._safe_eval_list(grid_match.group(1))
                if grid and len(grid) == 9:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"solution": grid, "found": True},
                        answer_type="sudoku",
                    )
            except Exception:
                pass

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content == "NO_SOLUTION":
                return ParsedAnswer(
                    raw_response=response,
                    answer={"solution": None, "found": False},
                    answer_type="sudoku",
                )
            if content.startswith("["):
                grid = self._safe_eval_list(content)
                if grid and len(grid) == 9:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"solution": grid, "found": True},
                        answer_type="sudoku",
                    )

        # Try to find a 9x9 grid anywhere in the response
        grid_pattern = r"\[\s*\[[\d,\s]+\](?:\s*,\s*\[[\d,\s]+\]){8}\s*\]"
        grid_match = re.search(grid_pattern, response, re.DOTALL)
        if grid_match:
            try:
                grid = self._safe_eval_list(grid_match.group(0))
                if grid and len(grid) == 9 and all(len(row) == 9 for row in grid):
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"solution": grid, "found": True},
                        answer_type="sudoku",
                    )
            except Exception:
                pass

        # Check for "no solution"
        if re.search(r"no\s+solution", response, re.IGNORECASE):
            return ParsedAnswer(
                raw_response=response,
                answer={"solution": None, "found": False},
                answer_type="sudoku",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="sudoku",
            parse_error="Could not extract Sudoku solution from response",
        )

    def _parse_graph_coloring(self, response: str) -> ParsedAnswer:
        """Parse graph coloring result."""
        # Try FINAL_COLORING pattern first
        coloring_match = re.search(self.PATTERNS["coloring"], response, re.IGNORECASE)
        if coloring_match:
            try:
                coloring = self._safe_eval_dict(coloring_match.group(1))
                return ParsedAnswer(
                    raw_response=response,
                    answer={"coloring": coloring, "found": True},
                    answer_type="graph_coloring",
                )
            except ValueError:
                pass

        # Fallback: Look for coloring dictionary
        coloring_match = re.search(r"coloring\s*[=:]\s*(\{[^}]+\})", response, re.IGNORECASE)
        if coloring_match:
            try:
                coloring = self._safe_eval_dict(coloring_match.group(1))
                return ParsedAnswer(
                    raw_response=response,
                    answer={"coloring": coloring, "found": True},
                    answer_type="graph_coloring",
                )
            except ValueError:
                pass

        # Check for NO_SOLUTION in FINAL_ANSWER
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match and match.group(1).strip() == "NO_SOLUTION":
            return ParsedAnswer(
                raw_response=response,
                answer={"coloring": {}, "found": False},
                answer_type="graph_coloring",
            )

        # Check for "no solution" or "not possible"
        if re.search(r"(?:no\s+solution|not\s+possible|cannot)", response, re.IGNORECASE):
            return ParsedAnswer(
                raw_response=response,
                answer={"coloring": {}, "found": False},
                answer_type="graph_coloring",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="graph_coloring",
            parse_error="Could not extract graph coloring from response",
        )

    def _parse_matrix_chain(self, response: str) -> ParsedAnswer:
        """Parse matrix chain multiplication result."""
        min_ops = 0
        parenthesization = ""

        # Try FINAL_OPERATIONS pattern first
        ops_match = re.search(self.PATTERNS["operations"], response, re.IGNORECASE)
        if ops_match:
            min_ops = int(ops_match.group(1))

        # Fallback: Look for minimum operations in various formats
        if not min_ops:
            ops_match = re.search(r"(?:minimum|min)[_\s]*(?:operations|multiplications|cost|scalar)\s*[=:]\s*(\d+)", response, re.IGNORECASE)
            if ops_match:
                min_ops = int(ops_match.group(1))

        # Look for parenthesization
        paren_match = re.search(r"parenthesization\s*[=:]\s*(.+?)(?:\n|$)", response, re.IGNORECASE)
        if paren_match:
            parenthesization = paren_match.group(1).strip()

        if min_ops:
            return ParsedAnswer(
                raw_response=response,
                answer={"min_operations": min_ops, "parenthesization": parenthesization},
                answer_type="matrix_chain",
            )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = int(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"min_operations": value, "parenthesization": ""},
                    answer_type="matrix_chain",
                )
            except ValueError:
                pass

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="matrix_chain",
            parse_error="Could not extract matrix chain result from response",
        )

    def _parse_trie(self, response: str) -> ParsedAnswer:
        """Parse trie operations result."""
        # Try FINAL_RESULTS pattern first
        results_match = re.search(self.PATTERNS["results"], response, re.IGNORECASE)
        if results_match:
            content = results_match.group(1).strip()
            if content:
                # Try to parse as list of booleans/strings
                results = self._parse_list_content(content)
                # Convert string "True"/"False" to actual booleans
                results = [
                    True if str(r).lower() == "true" else
                    False if str(r).lower() == "false" else r
                    for r in results
                ]
                return ParsedAnswer(
                    raw_response=response,
                    answer={"results": results},
                    answer_type="trie",
                )
            else:
                return ParsedAnswer(
                    raw_response=response,
                    answer={"results": []},
                    answer_type="trie",
                )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content.startswith("["):
                results = self._safe_eval_list(content)
                if results is not None:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"results": results},
                        answer_type="trie",
                    )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="trie",
            parse_error="Could not extract trie results from response",
        )

    def _parse_monte_carlo(self, response: str) -> ParsedAnswer:
        """Parse Monte Carlo result."""
        # Try FINAL_ESTIMATE pattern first
        estimate_match = re.search(self.PATTERNS["estimate"], response, re.IGNORECASE)
        if estimate_match:
            estimate = float(estimate_match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"estimate": estimate},
                answer_type="monte_carlo",
            )

        # Fallback: Look for estimate/pi/value patterns
        estimate_match = re.search(r"(?:estimate|pi|value|result)\s*[=:]\s*(-?\d+\.?\d*)", response, re.IGNORECASE)
        if estimate_match:
            estimate = float(estimate_match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"estimate": estimate},
                answer_type="monte_carlo",
            )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = float(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"estimate": value},
                    answer_type="monte_carlo",
                )
            except ValueError:
                pass

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="monte_carlo",
            parse_error="Could not extract Monte Carlo estimate from response",
        )

    def _parse_optimization(self, response: str) -> ParsedAnswer:
        """Parse optimization result (gradient descent, simulated annealing, etc.)."""
        min_value = None
        solution = None

        # Try FINAL_MINIMUM pattern first
        min_match = re.search(self.PATTERNS["minimum"], response, re.IGNORECASE)
        if min_match:
            min_value = float(min_match.group(1))

        # Try FINAL_SOLUTION pattern
        sol_match = re.search(self.PATTERNS["solution"], response, re.IGNORECASE)
        if sol_match:
            solution = float(sol_match.group(1))

        # Fallback: Look for minimum value in various formats
        if min_value is None:
            min_match = re.search(r"(?:minimum[_\s]*value|min[_\s]*value|minimum|f\(x\))\s*[=:]\s*(-?\d+\.?\d*(?:[eE][+-]?\d+)?)", response, re.IGNORECASE)
            if min_match:
                min_value = float(min_match.group(1))

        # Fallback: Look for solution in various formats
        if solution is None:
            solution_match = re.search(r"(?:solution|x\*?|optimal[_\s]*x|at\s+x)\s*[=:]\s*(-?\d+\.?\d*(?:[eE][+-]?\d+)?)", response, re.IGNORECASE)
            if solution_match:
                solution = float(solution_match.group(1))

        if min_value is not None or solution is not None:
            return ParsedAnswer(
                raw_response=response,
                answer={"minimum_value": min_value, "solution": solution},
                answer_type="optimization",
            )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = float(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"minimum_value": value, "solution": None},
                    answer_type="optimization",
                )
            except ValueError:
                pass

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="optimization",
            parse_error="Could not extract optimization result from response",
        )

    # ========== Algorithm-specific parsers ==========

    def _parse_binary_search(self, response: str) -> ParsedAnswer:
        """Parse binary search result with value and found flag."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        value = None
        if match:
            try:
                value = int(match.group(1).strip())
            except ValueError:
                try:
                    value = float(match.group(1).strip())
                except ValueError:
                    pass

        # Determine if found (assume found if we have a value)
        found = value is not None

        if value is not None:
            return ParsedAnswer(
                raw_response=response,
                answer={"value": value, "found": found},
                answer_type="binary_search",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="binary_search",
            parse_error="Could not extract binary search result from response",
        )

    def _parse_merge_sort(self, response: str) -> ParsedAnswer:
        """Parse merge sort result."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content.startswith("["):
                items = self._safe_eval_list(content)
                if items is not None:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"value": items},
                        answer_type="merge_sort",
                    )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="merge_sort",
            parse_error="Could not extract sorted list from response",
        )

    def _parse_quickselect(self, response: str) -> ParsedAnswer:
        """Parse quickselect result."""
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = int(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"value": value},
                    answer_type="quickselect",
                )
            except ValueError:
                pass

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="quickselect",
            parse_error="Could not extract quickselect result from response",
        )

    def _parse_activity(self, response: str) -> ParsedAnswer:
        """Parse activity selection result."""
        count = 0
        activities = []

        # Try FINAL_COUNT pattern first
        count_match = re.search(self.PATTERNS["count"], response, re.IGNORECASE)
        if count_match:
            count = int(count_match.group(1))

        # Try FINAL_ACTIVITIES pattern
        act_match = re.search(self.PATTERNS["activities"], response, re.IGNORECASE)
        if act_match:
            content = act_match.group(1).strip()
            if content:
                activities = self._parse_list_content(content)

        if count or activities:
            # Only return count to match expected format {'count': N}
            return ParsedAnswer(
                raw_response=response,
                answer={"count": count if count else len(activities)},
                answer_type="activity",
            )

        # Fallback: Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                count = int(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"count": count},
                    answer_type="activity",
                )
            except ValueError:
                # Maybe it's a list of activities
                content = match.group(1).strip()
                if content.startswith("["):
                    items = self._safe_eval_list(content)
                    if items is not None:
                        return ParsedAnswer(
                            raw_response=response,
                            answer={"count": len(items)},
                            answer_type="activity",
                        )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="activity",
            parse_error="Could not extract activity selection result from response",
        )

    def _parse_kruskal(self, response: str) -> ParsedAnswer:
        """Parse Kruskal's MST result."""
        total_weight = 0
        edges = []

        # Try FINAL_WEIGHT pattern first
        weight_match = re.search(self.PATTERNS["weight"], response, re.IGNORECASE)
        if weight_match:
            total_weight = float(weight_match.group(1))
            if total_weight == int(total_weight):
                total_weight = int(total_weight)

        # Try FINAL_EDGES pattern
        edges_match = re.search(self.PATTERNS["edges"], response, re.IGNORECASE | re.DOTALL)
        if edges_match:
            try:
                edges = self._safe_eval_list(edges_match.group(1))
            except Exception:
                pass

        # Fallback: Look for total weight in various formats
        if not total_weight:
            weight_match = re.search(r"(?:total[_\s]*weight|weight|cost|mst[_\s]*weight)\s*[=:]\s*(\d+(?:\.\d+)?)", response, re.IGNORECASE)
            if weight_match:
                total_weight = float(weight_match.group(1))
                if total_weight == int(total_weight):
                    total_weight = int(total_weight)

        # Fallback: Look for edges using FINAL_ITEMS
        if not edges:
            items_match = re.search(self.PATTERNS["items"], response, re.IGNORECASE)
            if items_match:
                edges = self._parse_list_content(items_match.group(1))

        if total_weight or edges:
            return ParsedAnswer(
                raw_response=response,
                answer={"total_weight": total_weight, "edges": edges},
                answer_type="kruskal",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="kruskal",
            parse_error="Could not extract MST result from response",
        )

    def _parse_fractional_knapsack(self, response: str) -> ParsedAnswer:
        """Parse fractional knapsack result."""
        match = re.search(self.PATTERNS["value"], response, re.IGNORECASE)
        if match:
            value = float(match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"value": value},
                answer_type="fractional_knapsack",
            )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = float(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"value": value},
                    answer_type="fractional_knapsack",
                )
            except ValueError:
                pass

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="fractional_knapsack",
            parse_error="Could not extract fractional knapsack result from response",
        )

    def _parse_nqueens(self, response: str) -> ParsedAnswer:
        """Parse N-Queens result with positions and found flag."""
        match = re.search(self.PATTERNS["positions"], response, re.IGNORECASE)
        if match:
            content = match.group(1)
            positions = self._parse_tuple_list(content)
            if positions:
                return ParsedAnswer(
                    raw_response=response,
                    answer={"positions": positions, "found": True},
                    answer_type="nqueens",
                )

        return ParsedAnswer(
            raw_response=response,
            answer={"positions": [], "found": False},
            answer_type="nqueens",
        )

    def _parse_subset_sum(self, response: str) -> ParsedAnswer:
        """Parse subset sum result."""
        # Try FINAL_SUBSET pattern first
        subset_match = re.search(self.PATTERNS["subset"], response, re.IGNORECASE)
        if subset_match:
            content = subset_match.group(1).strip()
            if content:
                items = self._parse_list_content(content)
                return ParsedAnswer(
                    raw_response=response,
                    answer={"subset": items, "found": True},
                    answer_type="subset_sum",
                )
            else:
                return ParsedAnswer(
                    raw_response=response,
                    answer={"subset": [], "found": True},
                    answer_type="subset_sum",
                )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content == "NO_SOLUTION":
                return ParsedAnswer(
                    raw_response=response,
                    answer={"subset": [], "found": False},
                    answer_type="subset_sum",
                )
            if content.startswith("["):
                items = self._safe_eval_list(content)
                if items is not None:
                    return ParsedAnswer(
                        raw_response=response,
                        answer={"subset": items, "found": True},
                        answer_type="subset_sum",
                    )

        # Check for "no solution" or similar
        if re.search(r"no\s+(?:solution|subset)", response, re.IGNORECASE):
            return ParsedAnswer(
                raw_response=response,
                answer={"subset": [], "found": False},
                answer_type="subset_sum",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="subset_sum",
            parse_error="Could not extract subset sum result from response",
        )

    def _parse_edit_distance(self, response: str) -> ParsedAnswer:
        """Parse edit distance result."""
        # Try FINAL_DISTANCE pattern first (edit distance uses this)
        match = re.search(self.PATTERNS["distance"], response, re.IGNORECASE)
        if match:
            value = int(float(match.group(1)))
            return ParsedAnswer(
                raw_response=response,
                answer={"value": value},
                answer_type="edit_distance",
            )

        # Try FINAL_ANSWER pattern
        match = re.search(self.PATTERNS["answer"], response, re.IGNORECASE)
        if match:
            try:
                value = int(match.group(1).strip())
                return ParsedAnswer(
                    raw_response=response,
                    answer={"value": value},
                    answer_type="edit_distance",
                )
            except ValueError:
                pass

        # Try value pattern
        match = re.search(self.PATTERNS["value"], response, re.IGNORECASE)
        if match:
            value = int(float(match.group(1)))
            return ParsedAnswer(
                raw_response=response,
                answer={"value": value},
                answer_type="edit_distance",
            )

        # Fallback: Look for edit distance in text
        match = re.search(r"(?:edit[_\s]*distance|minimum[_\s]*edits?)\s*[=:]\s*(\d+)", response, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            return ParsedAnswer(
                raw_response=response,
                answer={"value": value},
                answer_type="edit_distance",
            )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="edit_distance",
            parse_error="Could not extract edit distance from response",
        )

    def _parse_generic(self, response: str) -> ParsedAnswer:
        """Generic parser as fallback."""
        # Try different patterns
        for name, pattern in self.PATTERNS.items():
            match = re.search(pattern, response, re.IGNORECASE)
            if match:
                return ParsedAnswer(
                    raw_response=response,
                    answer=match.group(1),
                    answer_type=name,
                    confidence=0.5,
                )

        return ParsedAnswer(
            raw_response=response,
            answer=None,
            answer_type="unknown",
            parse_error="Could not parse response with any pattern",
        )

    # Helper methods

    def _parse_list_content(self, content: str) -> list:
        """Parse comma-separated list content."""
        items = []
        for item in content.split(","):
            item = item.strip().strip("'\"")
            if item:
                # Try to convert to number
                try:
                    items.append(int(item))
                except ValueError:
                    try:
                        items.append(float(item))
                    except ValueError:
                        items.append(item)
        return items

    def _parse_tuple_list(self, content: str) -> list[tuple]:
        """Parse list of tuples from string."""
        tuples = []
        pattern = r"\((\d+),\s*(\d+)\)"
        for match in re.finditer(pattern, content):
            tuples.append((int(match.group(1)), int(match.group(2))))
        return tuples

    def _safe_eval_dict(self, s: str) -> dict:
        """Safely evaluate a dictionary string."""
        # Clean up the string
        s = s.strip()
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            # Try JSON parsing
            try:
                return json.loads(s)
            except json.JSONDecodeError:
                raise ValueError(f"Cannot parse as dict: {s}")

    def _safe_eval_list(self, s: str) -> list | None:
        """Safely evaluate a list string."""
        s = s.strip()
        try:
            result = ast.literal_eval(s)
            if isinstance(result, list):
                return result
        except (ValueError, SyntaxError):
            try:
                result = json.loads(s)
                if isinstance(result, list):
                    return result
            except json.JSONDecodeError:
                pass
        return None

    def _extract_distances_from_text(self, response: str) -> dict | None:
        """Try to extract distances from unstructured text."""
        # Look for patterns like "A: 0, B: 5" or "distance to A = 0"
        distances = {}

        patterns = [
            r"(\w+):\s*(\d+(?:\.\d+)?)",
            r"distance to (\w+)\s*[=:]\s*(\d+(?:\.\d+)?)",
            r"(\w+)\s*→\s*(\d+(?:\.\d+)?)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, response, re.IGNORECASE):
                node = match.group(1)
                dist = float(match.group(2))
                if node not in distances:
                    distances[node] = dist

        return distances if distances else None

    def _extract_path_from_text(self, response: str) -> list | None:
        """Try to extract a path from unstructured text."""
        # Look for patterns like "A → B → C" or "A -> B -> C"
        patterns = [
            r"[Pp]ath:\s*([\w\s→\->]+)",
            r"[Ss]hortest path:\s*([\w\s→\->]+)",
        ]

        for pattern in patterns:
            match = re.search(pattern, response)
            if match:
                path_str = match.group(1)
                path = re.split(r"\s*[→\->]+\s*", path_str)
                path = [p.strip() for p in path if p.strip()]
                if len(path) > 1:
                    return path

        return None

    def _extract_matrix_from_text(self, response: str) -> dict | None:
        """Try to extract distance matrix from text."""
        # For Floyd-Warshall, we expect a 2D result
        # This is a simplified implementation
        return None


def get_response_parser() -> ResponseParser:
    """Factory function to create a response parser."""
    return ResponseParser()
