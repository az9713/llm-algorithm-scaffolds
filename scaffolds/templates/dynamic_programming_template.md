# Generic Dynamic Programming Scaffold Template

## Category Definition

**What makes Dynamic Programming unique:**
- Break problem into overlapping subproblems
- Store solutions to avoid recomputation (memoization/tabulation)
- Build optimal solution from optimal sub-solutions

**When to use Dynamic Programming:**
- Optimal substructure: optimal solution uses optimal sub-solutions
- Overlapping subproblems: same subproblems solved repeatedly
- Problem asks for optimum (max/min) or count of ways

**Key distinguishing features:**
- Trade space for time (store intermediate results)
- Bottom-up (tabulation) or top-down (memoization)
- Recurrence relation defines the solution
- Often O(n²) or O(n×m) complexity

---

## Essential State Components

### [REQUIRED] - Must be in every DP scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `dp[state]` | Optimal value for subproblem | `dp[i] = max profit using items 0..i` |
| `state_definition` | What each state represents | `dp[i][w] = value with i items, capacity w` |
| `base_case` | Initial values | `dp[0][*] = 0` |
| `recurrence` | How to compute dp[state] | `dp[i][w] = max(take, skip)` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `choice[]` | Reconstructing solution | `choice[i][w] = TAKE or SKIP` |
| `parent[]` | Path reconstruction | `parent[i] = j` |
| `2D/3D state` | Multiple constraints | `dp[i][j][k]` |
| `rolling array` | Space optimization | `dp[w]` instead of `dp[i][w]` |

### State Invariants
- dp[state] contains optimal value for that exact subproblem
- Once computed, dp[state] never changes
- Subproblems computed before they are needed

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Input: [YOUR_INPUT]
   - Output: [MAXIMIZE/MINIMIZE/COUNT] [YOUR_OBJECTIVE]
   - Constraints: [YOUR_CONSTRAINTS]

2) State Definition
   dp[[STATE_VARIABLES]] = [WHAT_IT_REPRESENTS]

   Dimensions:
   - [DIM_1]: [MEANING] (range: [BOUNDS])
   - [DIM_2]: [MEANING] (range: [BOUNDS])

3) Base Case(s)
   dp[[BASE_STATE]] = [BASE_VALUE]

   (Initialize all starting conditions)

4) Recurrence Relation
   dp[[STATE]] = [COMBINE_FUNCTION](
       [OPTION_1]: [SUBPROBLEM_1] + [COST_1],
       [OPTION_2]: [SUBPROBLEM_2] + [COST_2],
       ...
   )

   WHERE:
   - [OPTION_1] means: [DESCRIPTION]
   - [OPTION_2] means: [DESCRIPTION]

5) Computation Order
   Fill table [ROW_BY_ROW / COLUMN_BY_COLUMN / DIAGONAL]
   Dependency: dp[i][j] depends on [EARLIER_STATES]

6) Answer Location
   Final answer = dp[[FINAL_STATE]]

7) Solution Reconstruction (if needed)
   Trace back from [FINAL_STATE] using [CHOICE_ARRAY/COMPARISON]

8) Verification
   - Recurrence correctly captures all choices
   - Base cases cover all boundary conditions
   - No circular dependencies
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] State definition is complete (captures all relevant information)
- [ ] Base cases handle all boundary conditions
- [ ] Recurrence considers ALL possible choices/transitions
- [ ] Computation order respects dependencies
- [ ] No subproblem depends on itself (no cycles)
- [ ] Final answer location is correct
- [ ] Space/time complexity is acceptable

---

## Derivation Examples

### Example 1: 0/1 Knapsack (from this template)

**Filled-in values:**
- State: **dp[i][w] = max value using items 0..i-1 with capacity w**
- Base case: **dp[0][w] = 0 for all w (no items)**
- Recurrence: **max(skip item i, take item i if it fits)**
- Answer: **dp[n][W]**

```
dp[i][w] = max value achievable with first i items, capacity w

Base: dp[0][*] = 0

Recurrence:
    If weight[i-1] > w:
        dp[i][w] = dp[i-1][w]  (can't take item)
    Else:
        dp[i][w] = max(
            dp[i-1][w],                        (skip item i)
            dp[i-1][w-weight[i-1]] + value[i-1] (take item i)
        )

Order: Fill row by row (i = 1 to n)
Answer: dp[n][W]
```

---

### Example 2: Longest Common Subsequence (from this template)

**Filled-in values:**
- State: **dp[i][j] = LCS length of X[0..i-1] and Y[0..j-1]**
- Base case: **dp[0][j] = dp[i][0] = 0 (empty string)**
- Recurrence: **If match, extend; else take best of excluding one char**
- Answer: **dp[m][n]**

```
dp[i][j] = length of LCS of X[0..i-1] and Y[0..j-1]

Base: dp[0][*] = dp[*][0] = 0

Recurrence:
    If X[i-1] == Y[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1  (extend LCS)
    Else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char)

Order: Fill row by row, left to right
Answer: dp[m][n]
```

---

### Example 3: Edit Distance (from this template)

**Filled-in values:**
- State: **dp[i][j] = min edits to transform X[0..i-1] to Y[0..j-1]**
- Base case: **dp[i][0] = i, dp[0][j] = j (all insertions/deletions)**
- Recurrence: **min of insert, delete, replace (or match)**
- Answer: **dp[m][n]**

```
dp[i][j] = minimum edits to convert X[0..i-1] to Y[0..j-1]

Base:
    dp[i][0] = i  (delete all chars)
    dp[0][j] = j  (insert all chars)

Recurrence:
    If X[i-1] == Y[j-1]:
        dp[i][j] = dp[i-1][j-1]  (no edit needed)
    Else:
        dp[i][j] = 1 + min(
            dp[i-1][j],    (delete from X)
            dp[i][j-1],    (insert into X)
            dp[i-1][j-1]   (replace)
        )

Order: Fill row by row
Answer: dp[m][n]
```

---

## Top-Down vs Bottom-Up

| Approach | Pros | Cons |
|----------|------|------|
| **Top-Down (Memoization)** | Only computes needed states, easier to write | Recursion overhead, stack limits |
| **Bottom-Up (Tabulation)** | No recursion, often faster | May compute unnecessary states |

**Converting between approaches:**
1. Identify recursive structure → natural top-down
2. Determine computation order → convert to bottom-up
3. Identify which states are actually used → prune if needed

---

## Common DP Patterns

| Pattern | State Shape | Example |
|---------|-------------|---------|
| **Linear** | `dp[i]` | Fibonacci, LIS |
| **Two-sequence** | `dp[i][j]` | LCS, Edit Distance |
| **Knapsack** | `dp[i][capacity]` | 0/1 Knapsack, Coin Change |
| **Interval** | `dp[i][j]` (subarray i..j) | Matrix Chain, Palindrome |
| **Grid** | `dp[row][col]` | Path counting, Min path sum |
| **Bitmask** | `dp[mask]` | TSP, Set cover |

---

## Creating Your Own DP Scaffold

1. **Define what a subproblem solves**
   - What is the optimal value/count for a smaller version?
   - What parameters define a subproblem uniquely?

2. **Identify the state dimensions**
   - What information do you need to make decisions?
   - Usually: index/position + resource constraints

3. **Write the recurrence relation**
   - What choices can you make at each step?
   - How does each choice connect to subproblems?

4. **Determine base cases**
   - What are the smallest subproblems?
   - What values do they have?

5. **Establish computation order**
   - What subproblems must be solved first?
   - Usually: smaller indices before larger

6. **Locate the final answer**
   - Which dp cell contains the answer to the original problem?

7. **Add reconstruction (if needed)**
   - Track which choice was made at each step
   - Trace back from final answer to build solution
