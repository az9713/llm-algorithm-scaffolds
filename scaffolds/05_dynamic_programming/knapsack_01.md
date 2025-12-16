# 0/1 Knapsack Problem Scaffold

## When to Use
- Selecting items to maximize value with weight limit
- Items are **indivisible** (take it or leave it)
- Subset selection with capacity constraint
- Budget allocation, cargo loading, project selection
- When greedy doesn't work (items can't be fractioned)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following 0/1 Knapsack problem using Dynamic Programming.

1) Problem Restatement
- Given: n items, each with value v[i] and weight w[i]
- Knapsack capacity: W
- Each item either fully taken (1) or not taken (0)
- Goal: maximize total value while total weight ≤ W

2) State Definition
dp[i][j] = maximum value achievable using items 1..i with capacity j

Dimensions:
- i = 0 to n (items considered)
- j = 0 to W (capacity used)

3) Recurrence Relation
For each item i and capacity j:

If w[i] > j (item doesn't fit):
    dp[i][j] = dp[i-1][j]  (can't take item i)

If w[i] ≤ j (item fits):
    dp[i][j] = max(
        dp[i-1][j],           // don't take item i
        dp[i-1][j-w[i]] + v[i] // take item i
    )

4) Base Cases
dp[0][j] = 0 for all j  (no items → no value)
dp[i][0] = 0 for all i  (no capacity → no value)

5) Computation Order
Fill table row by row (items) or column by column (capacity).
For space optimization: single row, process capacity in reverse.

6) Solution Extraction
- Maximum value: dp[n][W]
- Items selected: backtrack from dp[n][W]
  - If dp[i][j] ≠ dp[i-1][j]: item i was taken
  - Move to dp[i-1][j-w[i]]

7) Verification Protocol
- Trace selected items
- Sum weights ≤ W
- Sum values = dp[n][W]
```

---

## Worked Example

### Problem
Capacity W = 7
| Item | Value | Weight |
|------|-------|--------|
| 1    | 1     | 1      |
| 2    | 4     | 3      |
| 3    | 5     | 4      |
| 4    | 7     | 5      |

### Expected Scaffold Application

**1) Problem Restatement**
- 4 items, capacity = 7
- Select items to maximize value

**2-4) Build DP Table**

|     | j=0 | j=1 | j=2 | j=3 | j=4 | j=5 | j=6 | j=7 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| i=0 | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| i=1 | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| i=2 | 0   | 1   | 1   | 4   | 5   | 5   | 5   | 5   |
| i=3 | 0   | 1   | 1   | 4   | 5   | 6   | 6   | 9   |
| i=4 | 0   | 1   | 1   | 4   | 5   | 7   | 8   | 9   |

**Filling the table:**

Row 1 (item 1: v=1, w=1):
- j≥1: can take item 1, dp[1][j] = max(0, 0+1) = 1

Row 2 (item 2: v=4, w=3):
- j<3: can't fit, dp[2][j] = dp[1][j]
- j=3: max(dp[1][3]=1, dp[1][0]+4=4) = 4
- j=4: max(dp[1][4]=1, dp[1][1]+4=5) = 5

Row 3 (item 3: v=5, w=4):
- j=4: max(dp[2][4]=5, dp[2][0]+5=5) = 5
- j=5: max(dp[2][5]=5, dp[2][1]+5=6) = 6
- j=7: max(dp[2][7]=5, dp[2][3]+5=9) = 9

Row 4 (item 4: v=7, w=5):
- j=5: max(dp[3][5]=6, dp[3][0]+7=7) = 7
- j=6: max(dp[3][6]=6, dp[3][1]+7=8) = 8
- j=7: max(dp[3][7]=9, dp[3][2]+7=8) = 9

**5) Maximum Value**
dp[4][7] = **9**

**6) Backtrack to Find Items**
- At dp[4][7]=9: dp[3][7]=9 (same), item 4 NOT taken
- At dp[3][7]=9: dp[2][7]=5 (different), item 3 TAKEN
  - Move to dp[2][7-4] = dp[2][3] = 4
- At dp[2][3]=4: dp[1][3]=1 (different), item 2 TAKEN
  - Move to dp[1][3-3] = dp[1][0] = 0
- At dp[1][0]=0: done

**Items selected: 2 and 3**

**7) Verification**
- Weight: 3 + 4 = 7 ≤ 7 ✓
- Value: 4 + 5 = 9 = dp[4][7] ✓

### Final Answer
Maximum value: **9**
Items selected: 2 (v=4, w=3) and 3 (v=5, w=4)

---

## Space-Optimized Version

Use 1D array, process capacity in **reverse**:
```
dp[j] = max(dp[j], dp[j-w[i]] + v[i])
```

Processing in reverse prevents using updated values from same row.

---

## Common Failure Modes

1. **Using greedy** → doesn't work for 0/1 (only fractional)
2. **Allowing item reuse** → that's unbounded knapsack, different problem
3. **Wrong recurrence direction** → must consider "don't take" option
4. **Off-by-one in table dimensions** → need (n+1) × (W+1)
5. **Forward iteration in 1D** → must go backward in capacity
6. **Forgetting base cases** → dp[0][j] and dp[i][0] must be 0
