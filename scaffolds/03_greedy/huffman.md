# Huffman Coding Scaffold

## When to Use
- Optimal prefix-free encoding
- Data compression
- Building optimal binary trees
- Variable-length encoding based on frequency
- Minimum weighted path length trees

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Huffman's Algorithm.

1) Problem Restatement
- Given: set of symbols with frequencies/weights
- Goal: create prefix-free binary codes minimizing expected code length
- Output: binary code for each symbol (shorter codes for frequent symbols)

2) State Definition
State = (forest of trees, priority queue)

Where:
- Each symbol starts as a single-node tree
- Trees ordered by total frequency (min-heap)
- Internal nodes represent merged subtrees

Node structure:
- leaf: (symbol, frequency)
- internal: (left_child, right_child, total_frequency)

3) Merge Operation Semantics
Combine two minimum-frequency trees:
- Create new internal node
- Left child: smaller frequency tree
- Right child: larger frequency tree
- New frequency: sum of children's frequencies
- Insert new tree back into priority queue

4) Algorithm Procedure
a) Create leaf node for each symbol with its frequency
b) Insert all leaves into min-priority queue (by frequency)
c) While queue has more than one tree:
   - Extract two minimum-frequency trees
   - Create new internal node with these as children
   - Set new node's frequency = sum of children
   - Insert new node into queue
d) Remaining tree is the Huffman tree
e) Assign codes: left edge = 0, right edge = 1

5) Termination Condition
- Single tree remains in queue
- All symbols are leaves in this tree

6) Verification Protocol
- Every symbol has unique code
- Codes are prefix-free (no code is prefix of another)
- Compute weighted path length: Σ(frequency × code_length)
- Verify this is minimum possible
```

---

## Worked Example

### Problem
Create Huffman codes for:
| Symbol | Frequency |
|--------|-----------|
| A      | 45        |
| B      | 13        |
| C      | 12        |
| D      | 16        |
| E      | 9         |
| F      | 5         |

### Expected Scaffold Application

**1) Problem Restatement**
- 6 symbols with given frequencies
- Create optimal prefix-free binary codes
- Minimize expected code length

**2) Initial State**
Priority queue (min-heap by frequency):
```
F:5, E:9, C:12, B:13, D:16, A:45
```

**3-4) Algorithm Execution**

**Step 1:** Extract F(5) and E(9), merge
```
    [14]
   /    \
  F:5   E:9

Queue: C:12, B:13, [14], D:16, A:45
```

**Step 2:** Extract C(12) and B(13), merge
```
    [25]
   /    \
 C:12  B:13

Queue: [14], D:16, [25], A:45
```

**Step 3:** Extract [14] and D(16), merge
```
      [30]
     /    \
   [14]   D:16
   /  \
  F:5 E:9

Queue: [25], [30], A:45
```

**Step 4:** Extract [25] and [30], merge
```
         [55]
        /    \
     [25]    [30]
     /  \    /   \
   C:12 B:13 [14] D:16
             /  \
           F:5  E:9

Queue: A:45, [55]
```

**Step 5:** Extract A(45) and [55], merge
```
              [100]
             /     \
          A:45     [55]
                  /    \
               [25]    [30]
               /  \    /   \
             C:12 B:13 [14] D:16
                       /  \
                     F:5  E:9
```

**5) Assign Codes (left=0, right=1)**

Traverse from root to each leaf:
| Symbol | Path         | Code |
|--------|--------------|------|
| A      | left         | 0    |
| C      | right→left→left | 100  |
| B      | right→left→right | 101  |
| F      | right→right→left→left | 1100 |
| E      | right→right→left→right | 1101 |
| D      | right→right→right | 111  |

**6) Verification**

Prefix-free check:
- No code is a prefix of any other ✓
- 0 is not prefix of 100, 101, 1100, 1101, 111 ✓
- 100 is not prefix of 101, 1100, etc. ✓

Weighted path length:
```
WPL = 45×1 + 12×3 + 13×3 + 5×4 + 9×4 + 16×3
    = 45 + 36 + 39 + 20 + 36 + 48
    = 224
```

Average code length:
```
Total frequency = 100
Average = 224/100 = 2.24 bits per symbol
```

### Final Answer
| Symbol | Frequency | Code |
|--------|-----------|------|
| A      | 45        | 0    |
| C      | 12        | 100  |
| B      | 13        | 101  |
| F      | 5         | 1100 |
| E      | 9         | 1101 |
| D      | 16        | 111  |

Weighted Path Length: 224
Average Code Length: 2.24 bits

---

## Common Failure Modes

1. **Not using min-heap** → extracting wrong nodes
2. **Merging more than 2 at once** → binary tree requires pairs
3. **Confusing frequency with code length** → shorter codes for HIGHER frequency
4. **Building tree incorrectly** → merged nodes go back into queue
5. **Non-prefix-free codes** → each leaf must have unique path
6. **Wrong bit assignment convention** → left=0, right=1 is standard but consistent is key
