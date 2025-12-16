# Edit Distance (Levenshtein Distance) Scaffold

## When to Use
- Spell checking and autocorrect
- DNA sequence alignment
- Fuzzy string matching
- Measuring similarity between strings
- Natural language processing
- Diff algorithms

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following Edit Distance problem using Dynamic Programming.

1) Problem Restatement
- Given: two strings A = a₁...aₘ and B = b₁...bₙ
- Operations allowed (each costs 1):
  - Insert a character
  - Delete a character
  - Replace a character
- Goal: minimum operations to transform A into B

2) State Definition
dp[i][j] = minimum edits to transform A[1..i] into B[1..j]

Dimensions:
- i = 0 to m (prefix length of A)
- j = 0 to n (prefix length of B)

3) Recurrence Relation
If A[i] == B[j]:
    dp[i][j] = dp[i-1][j-1]  (no edit needed, characters match)
Else:
    dp[i][j] = 1 + min(
        dp[i-1][j],     // delete A[i]
        dp[i][j-1],     // insert B[j]
        dp[i-1][j-1]    // replace A[i] with B[j]
    )

4) Base Cases
dp[i][0] = i for all i  (delete all of A)
dp[0][j] = j for all j  (insert all of B)

5) Computation Order
Fill table row by row, left to right.

6) Solution Extraction
- Edit distance: dp[m][n]
- Edit sequence: backtrack from dp[m][n]
  - If A[i] == B[j]: no edit, move diagonally
  - Else: find which operation (min of 3) was used

7) Verification Protocol
- Apply edit sequence to A
- Result should equal B
- Count of edits = dp[m][n]
```

---

## Worked Example

### Problem
Find edit distance between A = "SUNDAY" and B = "SATURDAY"

### Expected Scaffold Application

**1) Problem Restatement**
- A = "SUNDAY" (length 6)
- B = "SATURDAY" (length 8)
- Find minimum edits to transform A → B

**2-4) Build DP Table**

|     |""| S | A | T | U | R | D | A | Y |
|-----|--|---|---|---|---|---|---|---|---|
| ""  | 0| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| S   | 1| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| U   | 2| 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 |
| N   | 3| 2 | 2 | 2 | 3 | 3 | 4 | 5 | 6 |
| D   | 4| 3 | 3 | 3 | 3 | 4 | 3 | 4 | 5 |
| A   | 5| 4 | 3 | 4 | 4 | 4 | 4 | 3 | 4 |
| Y   | 6| 5 | 4 | 4 | 5 | 5 | 5 | 4 | 3 |

**Filling key cells:**
- dp[1][1]: S==S → dp[0][0] = 0
- dp[2][4]: U==U → dp[1][3] = 2
- dp[4][6]: D==D → dp[3][5] = 3
- dp[5][7]: A==A → dp[4][6] = 3
- dp[6][8]: Y==Y → dp[5][7] = 3

**5) Edit Distance**
dp[6][8] = **3**

**6) Backtrack for Edit Sequence**

| Position | A char | B char | dp value | From          | Operation    |
|----------|--------|--------|----------|---------------|--------------|
| (6,8)    | Y      | Y      | 3        | (5,7) diag    | match        |
| (5,7)    | A      | A      | 3        | (4,6) diag    | match        |
| (4,6)    | D      | D      | 3        | (3,5) diag    | match        |
| (3,5)    | N      | R      | 3        | (2,4) diag    | replace N→R  |
| (2,4)    | U      | U      | 2        | (1,3) diag    | match        |
| (1,3)    | S      | T      | 2        | (0,2) diag    | replace S→T... wait |

Let me re-trace more carefully:
| (1,3)    | S      | T      | 2        | (1,2)=1 left  | insert T     |
| (1,2)    | S      | A      | 1        | (1,1)=0 left  | insert A     |
| (1,1)    | S      | S      | 0        | (0,0) diag    | match        |

**Edit operations (reading forward):**
1. Match S
2. Insert A after S → "SAUNDAY"
3. Insert T after A → "SATUNDAY"
4. Match U
5. Replace N with R → "SATURDAY"
6. Match D, A, Y

Wait, let me verify: That's only 3 edits (insert A, insert T, replace N→R) = 3 ✓

**7) Verification**
SUNDAY
→ SAUNDAY (insert A at position 2)
→ SATUNDAY (insert T at position 3)
→ SATURDAY (replace N with R)

3 edits ✓

### Final Answer
Edit distance: **3**
Operations: Insert 'A', Insert 'T', Replace 'N'→'R'

---

## Variants

**Weighted Edit Distance:**
- Different costs for insert/delete/replace
- Modify the +1 to appropriate cost

**Damerau-Levenshtein:**
- Also allows transposition (swap adjacent characters)
- Requires 2D+diagonal tracking

---

## Common Failure Modes

1. **Forgetting +1 for operations** → just taking min without adding cost
2. **Wrong base cases** → dp[i][0]=i, dp[0][j]=j are crucial
3. **Confusing insert/delete direction** → insert into A vs delete from A
4. **Not handling match case** → when equal, cost is 0 (diagonal only)
5. **Off-by-one indexing** → strings are 1-indexed in DP
6. **Backtracking errors** → must identify which of 3 operations was used
