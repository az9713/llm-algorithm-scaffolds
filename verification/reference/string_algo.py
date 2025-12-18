"""
Reference implementations for string algorithms.

Implements: KMP (Knuth-Morris-Pratt), Rabin-Karp, Trie operations.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class StringAlgoResult:
    """Result from a string algorithm."""

    matches: list[int] | None = None
    """List of match positions (for pattern matching)."""

    found: bool = False
    """Whether pattern/prefix was found."""

    value: Any = None
    """Generic value result."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        result = {"found": self.found}
        if self.matches is not None:
            result["matches"] = self.matches
        if self.value is not None:
            result["value"] = self.value
        return result


def kmp_search(
    text: str,
    pattern: str,
) -> StringAlgoResult:
    """
    Knuth-Morris-Pratt pattern matching algorithm.

    Args:
        text: Text to search in.
        pattern: Pattern to find.

    Returns:
        StringAlgoResult with list of match positions.
    """
    if not pattern:
        return StringAlgoResult(matches=list(range(len(text) + 1)), found=True)

    if not text:
        return StringAlgoResult(matches=[], found=False)

    # Build failure function (partial match table)
    def build_lps(pattern: str) -> list[int]:
        """Build longest proper prefix which is also suffix array."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    lps = build_lps(pattern)
    matches = []

    n, m = len(text), len(pattern)
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return StringAlgoResult(matches=matches, found=len(matches) > 0)


def rabin_karp_search(
    text: str,
    pattern: str,
    base: int = 256,
    prime: int = 101,
) -> StringAlgoResult:
    """
    Rabin-Karp hash-based pattern matching algorithm.

    Args:
        text: Text to search in.
        pattern: Pattern to find.
        base: Base for hash calculation.
        prime: Prime modulus for hash.

    Returns:
        StringAlgoResult with list of match positions.
    """
    if not pattern:
        return StringAlgoResult(matches=list(range(len(text) + 1)), found=True)

    if not text or len(pattern) > len(text):
        return StringAlgoResult(matches=[], found=False)

    n, m = len(text), len(pattern)
    matches = []

    # Calculate hash of pattern and first window
    pattern_hash = 0
    text_hash = 0
    h = pow(base, m - 1, prime)

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # Slide pattern over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Hash match, verify character by character
            if text[i : i + m] == pattern:
                matches.append(i)

        # Calculate hash for next window
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return StringAlgoResult(matches=matches, found=len(matches) > 0)


@dataclass
class TrieNode:
    """Node in a Trie."""

    children: dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False
    value: Any = None


class Trie:
    """Trie (prefix tree) data structure."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, value: Any = None) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def search(self, word: str) -> bool:
        """Check if word exists in trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix."""
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str) -> list[str]:
        """Get all words that start with prefix."""
        node = self._find_node(prefix)
        if node is None:
            return []

        words = []
        self._collect_words(node, prefix, words)
        return words

    def _find_node(self, prefix: str) -> TrieNode | None:
        """Find node corresponding to prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_words(self, node: TrieNode, prefix: str, words: list[str]) -> None:
        """Collect all words from this node."""
        if node.is_end:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)


def trie_operations(
    words: list[str],
    queries: list[tuple[str, str]],
) -> StringAlgoResult:
    """
    Perform trie operations.

    Args:
        words: List of words to insert.
        queries: List of (operation, arg) tuples where operation is
                'search', 'prefix', or 'autocomplete'.

    Returns:
        StringAlgoResult with list of results for each query.
    """
    trie = Trie()
    for word in words:
        trie.insert(word)

    results = []
    for op, arg in queries:
        if op == "search":
            results.append(trie.search(arg))
        elif op == "prefix":
            results.append(trie.starts_with(arg))
        elif op == "autocomplete":
            results.append(trie.get_words_with_prefix(arg))
        else:
            results.append(None)

    return StringAlgoResult(value=results, found=True)


# Convenience function to run any string algorithm
def run_string_algorithm(
    algorithm: str,
    **kwargs,
) -> StringAlgoResult:
    """
    Run a string algorithm by name.

    Args:
        algorithm: Algorithm name (kmp, rabin_karp, trie_operations).
        **kwargs: Algorithm-specific arguments.

    Returns:
        StringAlgoResult from the algorithm.
    """
    algorithms = {
        "kmp": kmp_search,
        "kmp_search": kmp_search,
        "rabin_karp": rabin_karp_search,
        "rabin_karp_search": rabin_karp_search,
        "trie": trie_operations,
        "trie_operations": trie_operations,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm in ("kmp", "kmp_search"):
        return func(kwargs["text"], kwargs["pattern"])
    elif algorithm in ("rabin_karp", "rabin_karp_search"):
        return func(
            kwargs["text"],
            kwargs["pattern"],
            kwargs.get("base", 256),
            kwargs.get("prime", 101),
        )
    elif algorithm in ("trie", "trie_operations"):
        return func(kwargs["words"], kwargs["queries"])
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
