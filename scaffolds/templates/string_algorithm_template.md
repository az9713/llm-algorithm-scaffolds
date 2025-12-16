# Generic String Algorithm Scaffold Template

## Category Definition

**What makes String Algorithms unique:**
- Operate on sequences of characters
- Exploit structure of text (patterns, prefixes, suffixes)
- Often use preprocessing to enable fast queries

**When to use String Algorithms:**
- Pattern matching (find occurrences of substring)
- String comparison and similarity
- Text indexing and search
- Prefix/suffix-based operations

**Key distinguishing features:**
- Preprocessing phase + query phase
- Failure/prefix functions for efficient backtracking
- Hash functions for probabilistic matching
- Trie/suffix structures for multi-pattern search

---

## Essential State Components

### [REQUIRED] - Must be in every string scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `text` | String being searched/processed | `"ABABDABACDABABCABAB"` |
| `pattern` | Pattern to find (if applicable) | `"ABABCABAB"` |
| `position` | Current position in text/pattern | `text_idx=5, pat_idx=3` |
| `result` | Match positions or computed value | `[10]` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `failure[]` | KMP-style algorithms | `failure = [0,0,1,2,0,...]` |
| `hash` | Rolling hash algorithms | `hash("ABC") = 294` |
| `trie_node` | Multi-pattern matching | `root → 'A' → 'B' → ...` |
| `suffix_array` | Suffix-based algorithms | `SA = [5, 3, 1, 0, 4, 2]` |
| `lcp[]` | Longest common prefix | `LCP = [0, 1, 3, 0, 2]` |

### State Invariants
- Position indices are always within bounds
- Preprocessed structures are consistent with input
- Partial matches are tracked correctly

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Input: [TEXT / PATTERN / MULTIPLE_PATTERNS]
   - Output: [MATCH_POSITIONS / BOOLEAN / TRANSFORMED_STRING]
   - Constraints: [ALPHABET_SIZE / CASE_SENSITIVITY / etc.]

2) State Definition
   State = (
       text_position: [INDEX_IN_TEXT],
       pattern_position: [INDEX_IN_PATTERN],
       [PREPROCESSED_DATA]: ___,
       matches: [RESULT_ACCUMULATOR]
   )

3) Preprocessing Phase
   For [PATTERN/TEXT]:
       Compute [AUXILIARY_STRUCTURE]:
       [PREPROCESSING_ALGORITHM]

   Result: [WHAT_PREPROCESSING_PRODUCES]

4) Main Processing Phase
   Initialize: text_pos = 0, pattern_pos = 0

   While text_pos < len(text):
       If [MATCH_CONDITION]:
           [ADVANCE_BOTH]
           If [COMPLETE_MATCH]:
               Record match at [POSITION]
               [CONTINUE_SEARCH_LOGIC]
       Else:
           [MISMATCH_HANDLING]
           (Use preprocessed data to skip efficiently)

5) Termination
   - Text fully scanned
   - All patterns checked (for multi-pattern)

6) Output
   Return [MATCH_POSITIONS / COUNT / BOOLEAN]

7) Verification
   - Each reported match is valid
   - No matches were missed
   - Preprocessing is correct
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Input format is clear (text, pattern, alphabet)
- [ ] Preprocessing correctly captures required information
- [ ] Match condition is precise
- [ ] Mismatch handling uses preprocessing efficiently
- [ ] All edge cases handled (empty strings, no matches, overlapping matches)
- [ ] Verification confirms correctness

---

## Derivation Examples

### Example 1: KMP Pattern Matching (from this template)

**Filled-in values:**
- Preprocessing: **Build failure function for pattern**
- Match condition: **text[i] == pattern[j]**
- Mismatch handling: **j = failure[j-1] (skip using failure function)**
- Complete match: **j == pattern_length**

```
Preprocessing: Build failure[] for pattern
    failure[0] = 0
    For i = 1 to m-1:
        j = failure[i-1]
        While j > 0 and pattern[i] != pattern[j]:
            j = failure[j-1]
        If pattern[i] == pattern[j]:
            j++
        failure[i] = j

Main Phase:
    i = 0, j = 0  (text index, pattern index)

    While i < n:
        If text[i] == pattern[j]:
            i++, j++
            If j == m:
                Match found at i - m
                j = failure[j-1]  (continue searching)
        Else:
            If j > 0:
                j = failure[j-1]  (efficient skip)
            Else:
                i++
```

---

### Example 2: Rabin-Karp (from this template)

**Filled-in values:**
- Preprocessing: **Compute hash of pattern**
- Match condition: **hash(window) == hash(pattern)**
- Mismatch handling: **Roll hash to next window**
- Verification: **Character-by-character comparison on hash match**

```
Preprocessing:
    pattern_hash = hash(pattern)
    window_hash = hash(text[0:m])
    h = d^(m-1) mod q  (for rolling)

Main Phase:
    For i = 0 to n-m:
        If window_hash == pattern_hash:
            If text[i:i+m] == pattern:  (verify)
                Match found at i

        If i < n-m:
            # Rolling hash: remove first char, add next char
            window_hash = (d*(window_hash - text[i]*h) + text[i+m]) mod q

Parameters:
    d = alphabet size (e.g., 256)
    q = large prime (e.g., 101)
```

---

### Example 3: Trie-Based Multi-Pattern Search (from this template)

**Filled-in values:**
- Preprocessing: **Build trie from all patterns**
- Match condition: **Current char exists in trie children**
- Mismatch handling: **Reset to root (or use failure links for Aho-Corasick)**
- Complete match: **Reached a terminal node**

```
Preprocessing: Build Trie
    root = new TrieNode()
    For each pattern:
        node = root
        For each char in pattern:
            If char not in node.children:
                node.children[char] = new TrieNode()
            node = node.children[char]
        node.is_terminal = True
        node.pattern = pattern

Main Phase:
    node = root
    For i = 0 to n-1:
        While node != root and text[i] not in node.children:
            node = root  (or node = node.failure for Aho-Corasick)

        If text[i] in node.children:
            node = node.children[text[i]]

        # Check for matches at current node (and suffix links)
        temp = node
        While temp != root:
            If temp.is_terminal:
                Match found: temp.pattern at position i - len(pattern) + 1
            temp = temp.suffix_link  (for Aho-Corasick)
```

---

## Common String Algorithm Patterns

| Pattern | Use Case | Example Algorithms |
|---------|----------|-------------------|
| **Preprocessing + Scan** | Single pattern matching | KMP, Boyer-Moore |
| **Rolling Hash** | Probabilistic matching | Rabin-Karp |
| **Trie-based** | Multi-pattern, prefix search | Aho-Corasick, Autocomplete |
| **Suffix-based** | Substring queries | Suffix Array, Suffix Tree |
| **DP on strings** | Similarity, alignment | Edit Distance, LCS |

---

## Complexity Trade-offs

| Algorithm | Preprocessing | Query | Space |
|-----------|--------------|-------|-------|
| Naive | O(1) | O(nm) | O(1) |
| KMP | O(m) | O(n) | O(m) |
| Rabin-Karp | O(m) | O(n) avg | O(1) |
| Boyer-Moore | O(m + σ) | O(n/m) best | O(σ) |
| Suffix Array | O(n log n) | O(m log n) | O(n) |
| Trie | O(Σ|patterns|) | O(n) | O(Σ|patterns| × σ) |

Where: n = text length, m = pattern length, σ = alphabet size

---

## Creating Your Own String Scaffold

1. **Identify the problem type**
   - Single pattern? Multiple patterns?
   - Exact match? Approximate match?
   - One query? Many queries on same text?

2. **Choose preprocessing strategy**
   - Pattern-based (KMP failure function)
   - Text-based (suffix array)
   - Hash-based (Rabin-Karp)

3. **Define the matching condition**
   - When do characters match?
   - When is a complete match found?

4. **Design efficient mismatch handling**
   - How to skip unnecessary comparisons?
   - Use preprocessed information

5. **Handle overlapping matches**
   - Report all? Only longest? Only non-overlapping?

6. **Consider edge cases**
   - Empty pattern or text
   - Pattern longer than text
   - No matches exist
   - All characters match (worst case for some algorithms)
