# Longest Common Subsequence (LCS) Scaffold

## When to Use
- Finding similarity between two sequences
- Diff algorithms (file comparison)
- DNA/protein sequence alignment
- Version control systems
- Spell checking (similarity measurement)
- NOT finding contiguous substrings (that's different)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following LCS problem using Dynamic Programming.

1) Problem Restatement
- Given: two sequences X = x₁...xₘ and Y = y₁...yₙ
- Subsequence: elements in order but not necessarily contiguous
- Goal: find longest subsequence common to both X and Y

2) State Definition
dp[i][j] = length of LCS of X[1..i] and Y[1..j]

Dimensions:
- i = 0 to m (prefix length of X)
- j = 0 to n (prefix length of Y)

3) Recurrence Relation
If X[i] == Y[j]:
    dp[i][j] = dp[i-1][j-1] + 1  (extend LCS by this match)
Else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char)

Intuition:
- Match: both sequences contribute a character
- No match: try skipping from X or skipping from Y

4) Base Cases
dp[0][j] = 0 for all j  (empty X → LCS length 0)
dp[i][0] = 0 for all i  (empty Y → LCS length 0)

5) Computation Order
Fill table row by row, left to right (or column by column).

6) Solution Extraction
- LCS length: dp[m][n]
- Actual LCS: backtrack from dp[m][n]
  - If X[i] == Y[j]: include character, move to dp[i-1][j-1]
  - Else: move to larger of dp[i-1][j] or dp[i][j-1]

7) Verification Protocol
- LCS is subsequence of X (characters in order)
- LCS is subsequence of Y (characters in order)
- No longer common subsequence exists
```

---

## Worked Example

### Problem
Find LCS of X = "ABCDGH" and Y = "AEDFHR"

### Expected Scaffold Application

**1) Problem Restatement**
- X = "ABCDGH" (length 6)
- Y = "AEDFHR" (length 6)
- Find longest common subsequence

**2-4) Build DP Table**

|     |""| A | E | D | F | H | R |
|-----|--|---|---|---|---|---|---|
| ""  | 0| 0 | 0 | 0 | 0 | 0 | 0 |
| A   | 0| 1 | 1 | 1 | 1 | 1 | 1 |
| B   | 0| 1 | 1 | 1 | 1 | 1 | 1 |
| C   | 0| 1 | 1 | 1 | 1 | 1 | 1 |
| D   | 0| 1 | 1 | 2 | 2 | 2 | 2 |
| G   | 0| 1 | 1 | 2 | 2 | 2 | 2 |
| H   | 0| 1 | 1 | 2 | 2 | 3 | 3 |

**Filling key cells:**
- dp[1][1]: X[1]='A' == Y[1]='A' → dp[0][0]+1 = 1
- dp[2][1]: X[2]='B' ≠ Y[1]='A' → max(dp[1][1], dp[2][0]) = 1
- dp[4][3]: X[4]='D' == Y[3]='D' → dp[3][2]+1 = 2
- dp[6][5]: X[6]='H' == Y[5]='H' → dp[5][4]+1 = 3

**5) LCS Length**
dp[6][6] = **3**

**6) Backtrack to Find LCS**
Starting at dp[6][6] = 3:

| Position | X[i] | Y[j] | Match? | Action              |
|----------|------|------|--------|---------------------|
| (6,6)    | H    | R    | No     | max(dp[5][6], dp[6][5]) → go to (6,5) |
| (6,5)    | H    | H    | Yes    | Include 'H', go to (5,4) |
| (5,4)    | G    | F    | No     | go to (4,4)         |
| (4,4)    | D    | F    | No     | max(dp[3][4], dp[4][3]) → go to (4,3) |
| (4,3)    | D    | D    | Yes    | Include 'D', go to (3,2) |
| (3,2)    | C    | E    | No     | go to (2,2)         |
| (2,2)    | B    | E    | No     | go to (1,2)         |
| (1,2)    | A    | E    | No     | go to (1,1)         |
| (1,1)    | A    | A    | Yes    | Include 'A', go to (0,0) |
| (0,0)    | -    | -    | -      | Done                |

**LCS (reversed): H, D, A → ADH**

**7) Verification**
- "ADH" is subsequence of "ABCDGH": A(1), D(4), H(6) ✓
- "ADH" is subsequence of "AEDFHR": A(1), D(3), H(5) ✓
- Length 3 matches dp[6][6] ✓

### Final Answer
LCS: **"ADH"**
Length: **3**

---

## Variants

**Longest Common Substring** (contiguous):
- Different recurrence: dp[i][j] = dp[i-1][j-1]+1 only if match, else 0
- Answer is max value in table, not dp[m][n]

**Multiple Sequences:**
- 3D DP for 3 sequences, etc.
- Complexity increases exponentially

---

## Common Failure Modes

1. **Confusing with substring** → subsequence allows gaps
2. **Wrong backtracking** → must follow the path that gave max
3. **Off-by-one indexing** → table is (m+1)×(n+1)
4. **Not handling empty strings** → base cases critical
5. **Forgetting both skip options** → must take max of both
6. **Building LCS in wrong order** → backtrack gives reverse order
