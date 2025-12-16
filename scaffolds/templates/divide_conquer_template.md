# Generic Divide & Conquer Scaffold Template

## Category Definition

**What makes Divide & Conquer unique:**
- Breaks problem into smaller subproblems of the same type
- Solves subproblems recursively
- Combines subproblem solutions into final answer

**When to use Divide & Conquer:**
- Problem can be split into independent subproblems
- Subproblems are smaller instances of the original
- Combining solutions is efficient
- T(n) = a·T(n/b) + f(n) recurrence applies

**Key distinguishing features:**
- Recursive structure
- Subproblems don't overlap (unlike DP)
- Often achieves O(n log n) complexity
- Clear divide, conquer, combine phases

---

## Essential State Components

### [REQUIRED] - Must be in every D&C scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `lo, hi` | Bounds of current subproblem | `lo=0, hi=n-1` |
| `base_case` | When to stop recursing | `lo >= hi` |
| `divide_point` | How to split the problem | `mid = (lo+hi)/2` |
| `combine` | How to merge solutions | `merge(left, right)` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `pivot` | Partition-based algorithms | `pivot = A[hi]` |
| `target` | Search problems | `target = 42` |
| `invariant` | Maintained property | `answer in [lo,hi]` |

### State Invariants
- Subproblems are strictly smaller than parent
- Base case is always reachable
- Combined solution is valid for original problem

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Input: [YOUR_INPUT_STRUCTURE]
   - Output: [YOUR_DESIRED_OUTPUT]
   - Size: n = [PROBLEM_SIZE]

2) State Definition
   State = (
       lo: [LOWER_BOUND],
       hi: [UPPER_BOUND],
       [ADDITIONAL_STATE]: ___
   )

3) Base Case
   If [BASE_CONDITION]:
       Return [BASE_RESULT]

4) Divide Step
   [DIVIDE_POINT] = [DIVISION_FORMULA]

   Left subproblem: [lo, DIVIDE_POINT]
   Right subproblem: [DIVIDE_POINT+1, hi]

   (or describe how problem is partitioned)

5) Conquer Step (Recursive)
   left_result = solve([LEFT_SUBPROBLEM])
   right_result = solve([RIGHT_SUBPROBLEM])

6) Combine Step
   result = [COMBINE_OPERATION](left_result, right_result)
   Return result

7) Termination
   - Base case reached in all branches
   - Recursion depth: O(log n) for balanced division

8) Verification
   - Result satisfies original problem requirements
   - Subproblem solutions correctly combined
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Base case is clearly defined and reachable
- [ ] Division creates strictly smaller subproblems
- [ ] Subproblems are independent (no shared mutations)
- [ ] Combine step correctly merges partial solutions
- [ ] Recursion depth is bounded (no infinite recursion)
- [ ] Complexity analysis: T(n) = a·T(n/b) + f(n)

---

## Derivation Examples

### Example 1: Binary Search (from this template)

**Filled-in values:**
- Base case: **lo > hi → not found**
- Divide point: **mid = lo + (hi - lo) / 2**
- Subproblem choice: **If target < A[mid], search left; else search right**
- Combine: **N/A (only one branch taken)**

**Key insight:** Only one subproblem solved (not both) → O(log n).

```
divide_point = mid = (lo + hi) / 2

If A[mid] == target: return mid
If A[mid] < target: search [mid+1, hi]
If A[mid] > target: search [lo, mid-1]
```

---

### Example 2: Merge Sort (from this template)

**Filled-in values:**
- Base case: **lo >= hi → single element, already sorted**
- Divide point: **mid = (lo + hi) / 2**
- Subproblems: **Both halves are sorted recursively**
- Combine: **Merge two sorted halves**

**Key insight:** Combine step (merge) is O(n), called O(log n) times → O(n log n).

```
divide_point = mid
left_sorted = mergesort(lo, mid)
right_sorted = mergesort(mid+1, hi)
result = merge(left_sorted, right_sorted)
```

---

### Example 3: Quickselect (from this template)

**Filled-in values:**
- Base case: **lo == hi → return A[lo]**
- Divide: **Partition around pivot**
- Subproblem choice: **Only search half containing k-th element**
- Combine: **N/A (answer in one partition)**

**Key insight:** Like binary search, only one branch → O(n) average.

```
pivot_index = partition(lo, hi)

If k == pivot_index: return A[k]
If k < pivot_index: search [lo, pivot_index-1]
If k > pivot_index: search [pivot_index+1, hi]
```

---

## Creating Your Own D&C Scaffold

1. **Identify the base case**
   - What's the smallest problem you can solve directly?
   - Usually: empty, single element, or trivially solvable

2. **Define how to divide**
   - Split in half? (binary search, merge sort)
   - Partition around pivot? (quicksort, quickselect)
   - Split by some other criterion?

3. **Determine which subproblems to solve**
   - Both halves? (merge sort)
   - Only one half? (binary search, quickselect)
   - Multiple subproblems? (Strassen's algorithm)

4. **Define the combine step**
   - How do subproblem solutions become the full solution?
   - Merge operation? Selection? Aggregation?

5. **Analyze complexity**
   - Use Master Theorem: T(n) = a·T(n/b) + f(n)
