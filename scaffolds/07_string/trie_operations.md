# Trie (Prefix Tree) Operations Scaffold

## When to Use
- Prefix-based search and autocomplete
- Dictionary/vocabulary storage
- IP routing (longest prefix match)
- Spell checking
- Word games (Scrabble, Boggle)
- When queries share common prefixes

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using a Trie data structure.

1) Problem Restatement
- Given: set of strings (words/keys)
- Operations: insert, search, prefix search, delete
- Goal: efficient string operations based on prefixes

2) Trie Node Definition
Each node contains:
- children: map/array of child nodes (one per character)
- is_end_of_word: boolean flag marking word termination
- (optional) count, value, or other data

For alphabet of size k:
- Array-based: children[k] (fast but memory-heavy)
- Map-based: children = {} (memory-efficient)

3) Insert Operation
insert(word):
a) Start at root node
b) For each character c in word:
   - If children[c] doesn't exist: create new node
   - Move to children[c]
c) Mark current node as end_of_word = true

4) Search Operation
search(word):
a) Start at root node
b) For each character c in word:
   - If children[c] doesn't exist: return false
   - Move to children[c]
c) Return current node's is_end_of_word

5) Prefix Search
starts_with(prefix):
a) Start at root node
b) For each character c in prefix:
   - If children[c] doesn't exist: return false
   - Move to children[c]
c) Return true (prefix exists, regardless of is_end_of_word)

6) Verification Protocol
- Inserted words are searchable
- Non-inserted words return false
- Prefixes of inserted words are found
- Structure maintains prefix sharing
```

---

## Worked Example

### Problem
Build a trie with words: ["cat", "car", "card", "care", "dog"]
Then search for "car", "care", "ca", "dare"

### Expected Scaffold Application

**1) Problem Restatement**
- Insert 5 words into trie
- Perform exact search and prefix search

**2) Trie Structure After Insertions**

```
        (root)
       /      \
      c        d
      |        |
      a        o
     /|\       |
    t r *      g*
      |
      d* e*

Legend:
* = is_end_of_word
```

Detailed node structure:
```
root
├── 'c' → node_c
│   └── 'a' → node_ca
│       ├── 't' → node_cat [end]
│       └── 'r' → node_car [end]
│           ├── 'd' → node_card [end]
│           └── 'e' → node_care [end]
└── 'd' → node_d
    └── 'o' → node_do
        └── 'g' → node_dog [end]
```

**3) Insert Trace for "card"**

| Step | Character | Current Node | Action | Result |
|------|-----------|--------------|--------|--------|
| 1    | c         | root         | Find child 'c' | Move to node_c |
| 2    | a         | node_c       | Find child 'a' | Move to node_ca |
| 3    | r         | node_ca      | Find child 'r' | Move to node_car |
| 4    | d         | node_car     | Create child 'd' | Move to node_card |
| 5    | -         | node_card    | Mark end | is_end = true |

**4-5) Search Operations**

**Search "car" (exact match):**
| Step | Character | Node | Exists? |
|------|-----------|------|---------|
| 1    | c         | root → node_c | Yes |
| 2    | a         | node_c → node_ca | Yes |
| 3    | r         | node_ca → node_car | Yes |
| End  | -         | is_end_of_word? | **true** ✓ |

Result: **true** (found)

**Search "care" (exact match):**
c → a → r → e → is_end = true
Result: **true** (found)

**Search "ca" (exact match):**
c → a → is_end = **false**
Result: **false** (prefix exists, but "ca" not a word)

**Prefix search "ca" (starts_with):**
c → a → reached end of prefix
Result: **true** (words with prefix "ca" exist)

**Search "dare" (exact match):**
d → node_d has child 'o', not 'a'
Result: **false** (not found)

**6) Summary of Results**
| Query | Type | Result |
|-------|------|--------|
| "car" | search | true |
| "care" | search | true |
| "ca" | search | false |
| "ca" | starts_with | true |
| "dare" | search | false |

### Final Answer
- "car": found ✓
- "care": found ✓
- "ca": not a complete word, but is a valid prefix
- "dare": not found

---

## Autocomplete Implementation

```
autocomplete(prefix):
1. Navigate to node at end of prefix
2. If not found, return []
3. DFS/BFS from that node, collecting all words
4. Return collected words
```

For prefix "ca": would return ["cat", "car", "card", "care"]

---

## Delete Operation

```
delete(word):
1. Navigate to end of word, track path
2. Mark is_end_of_word = false
3. If node has no children and is not end of another word:
   - Remove node and propagate up
```

---

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) new nodes max |
| Search | O(m) | O(1) |
| Prefix | O(m) | O(1) |
| Delete | O(m) | O(1) |

m = length of word/prefix

---

## Common Failure Modes

1. **Forgetting is_end_of_word flag** → can't distinguish prefixes from words
2. **Not handling empty string** → root itself might be end of word
3. **Memory leaks on delete** → must clean up unused nodes
4. **Case sensitivity** → normalize to lowercase or handle both
5. **Non-alphabetic characters** → use map instead of fixed array
6. **Confusing search vs starts_with** → search checks is_end, prefix doesn't
