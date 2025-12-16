# Subset Sum Problem Scaffold

## When to Use
- Finding subset that sums to target value
- Partition problems (divide into equal halves)
- Knapsack-like decisions (include/exclude items)
- Checking if a sum is achievable
- Coin change with exact amounts
- Any problem with binary include/exclude decisions

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following Subset Sum problem using Backtracking.

1) Problem Restatement
- Given: set of integers S = {a₁, a₂, ..., aₙ}
- Target sum: T
- Find: subset of S that sums exactly to T
- Variants: find one subset, count all subsets, or determine if possible

2) State Definition
State = (index, current_sum, included_items)

Where:
- index = current item being considered (0 to n-1)
- current_sum = sum of items included so far
- included_items = list of items chosen

Pruning conditions:
- current_sum > T (if all items positive) → prune
- current_sum + remaining_sum < T → prune (insufficient items)

3) Decision Semantics
For each item at index i:
- Option 1: INCLUDE item → new_sum = current_sum + S[i]
- Option 2: EXCLUDE item → new_sum = current_sum

Binary choice tree at each step.

4) Algorithm Procedure
a) Sort items if helpful (descending for earlier pruning)
b) Base case:
   - If current_sum == T: solution found
   - If index == n: no more items, backtrack
c) Pruning checks:
   - If current_sum > T (and all positive): backtrack
   - If current_sum + sum(remaining) < T: backtrack
d) Recursive choices:
   - Include S[index]: recurse with sum + S[index]
   - Exclude S[index]: recurse with same sum
e) Backtrack if neither choice leads to solution

5) Termination Condition
- current_sum == T → found valid subset
- All combinations exhausted → no solution exists

6) Verification Protocol
- Sum the included items
- Verify sum equals T exactly
- Verify all items are from original set
- Verify no item used more than once (unless allowed)
```

---

## Worked Example

### Problem
S = {3, 7, 1, 8, 2}
Target T = 11
Find a subset that sums to 11.

### Expected Scaffold Application

**1) Problem Restatement**
- Set: {3, 7, 1, 8, 2}
- Target: 11
- Find any subset summing to exactly 11

**2) Initial State**
- index = 0
- current_sum = 0
- included = []
- total_sum = 3+7+1+8+2 = 21

**3-4) Algorithm Execution (Decision Tree)**

```
                        sum=0, idx=0
                       /            \
              include 3              exclude 3
              sum=3, idx=1           sum=0, idx=1
             /         \                  |
     include 7      exclude 7         include 7
     sum=10, idx=2  sum=3, idx=2      sum=7, idx=2
        |              |                  |
    include 1      include 1          include 1
    sum=11 ✓       sum=4, idx=3       sum=8, idx=3
    FOUND!            |                   |
                  include 8           include 8
                  sum=12 > 11         sum=16 > 11
                  PRUNE               PRUNE
```

**Path to Solution:**
- index 0 (value 3): INCLUDE → sum = 3
- index 1 (value 7): INCLUDE → sum = 10
- index 2 (value 1): INCLUDE → sum = 11 = T ✓

**5) Solution Found**
Subset: {3, 7, 1}
Sum: 3 + 7 + 1 = 11 ✓

**6) Verification**
- Items {3, 7, 1} all from original set ✓
- No duplicates ✓
- Sum = 11 = Target ✓

### Final Answer
Subset {3, 7, 1} sums to 11.

---

## Alternative Solutions
Other valid subsets for T=11:
- {3, 8} = 11 ✓
- {7, 2, 1, 1} - NOT VALID (1 appears only once)
- {8, 2, 1} = 11 ✓

The algorithm finds one; modify to find all if needed.

---

## Partition Variant

**Problem:** Can S = {1, 5, 11, 5} be partitioned into two equal-sum subsets?

Total = 22, so each half must sum to 11.
This reduces to: find subset summing to 11.
Solution: {1, 5, 5} = 11, remaining {11} = 11 ✓

---

## Common Failure Modes

1. **Not handling negative numbers** → pruning logic changes
2. **Pruning too aggressively** → sum > T only works for positive numbers
3. **Counting duplicates incorrectly** → {1,1,1} vs {1} depends on input
4. **Integer overflow** → large sums may overflow
5. **Stopping after first solution** → may need all solutions or count
6. **Not sorting for optimization** → sorting can enable better pruning
