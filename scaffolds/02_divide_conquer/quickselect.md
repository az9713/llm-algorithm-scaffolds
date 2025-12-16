# Quickselect (Selection Algorithm) Scaffold

## When to Use
- Finding k-th smallest/largest element
- Finding median without full sort
- Order statistics
- When O(n) average case is needed (vs O(n log n) for sorting)
- Partial sorting problems

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Quickselect.

1) Problem Restatement
- Given: unsorted array A of n elements
- Goal: find the k-th smallest element (1-indexed or 0-indexed)
- No need to fully sort the array

2) State Definition
State = (lo, hi, k)

Where:
- lo, hi define current search range
- k = target rank (adjust for sub-problems)
- After partition: pivot is at its final sorted position

3) Partition Operation
Choose pivot and rearrange so:
- Elements < pivot are to its left
- Elements > pivot are to its right
- Pivot is at index p

Lomuto partition (simpler):
- Choose pivot (often last element)
- i = lo - 1
- For j = lo to hi-1:
  - If A[j] <= pivot: swap A[++i] with A[j]
- Swap A[i+1] with pivot
- Return i+1

4) Algorithm Procedure
a) If lo == hi: return A[lo] (single element)
b) p = partition(A, lo, hi)
c) If k == p: return A[p] (found!)
d) If k < p: recurse on left: quickselect(A, lo, p-1, k)
e) If k > p: recurse on right: quickselect(A, p+1, hi, k)

5) Termination Condition
- k == p after partition: pivot is the answer
- lo == hi: single element is the answer

6) Verification Protocol
- Verify returned element is at position k in sorted array
- Count elements smaller than result (should be k-1 for 0-indexed)
```

---

## Worked Example

### Problem
Find 3rd smallest element in A = [7, 10, 4, 3, 20, 15]
(k = 2 for 0-indexed, k = 3 for 1-indexed; we'll use 0-indexed)

### Expected Scaffold Application

**1) Problem Restatement**
- Array: [7, 10, 4, 3, 20, 15]
- Find element at index 2 in sorted array (3rd smallest)
- k = 2 (0-indexed)

**2) Initial State**
- lo = 0, hi = 5, k = 2
- Array: [7, 10, 4, 3, 20, 15]

**3-4) Algorithm Execution**

**Iteration 1: partition(A, 0, 5)**
Pivot = A[5] = 15

| j | A[j] | A[j] <= 15? | i | Action                | Array state           |
|---|------|-------------|---|------------------------|----------------------|
| - | -    | -           | -1| Initialize             | [7,10,4,3,20,15]     |
| 0 | 7    | Yes         | 0 | swap A[0] with A[0]   | [7,10,4,3,20,15]     |
| 1 | 10   | Yes         | 1 | swap A[1] with A[1]   | [7,10,4,3,20,15]     |
| 2 | 4    | Yes         | 2 | swap A[2] with A[2]   | [7,10,4,3,20,15]     |
| 3 | 3    | Yes         | 3 | swap A[3] with A[3]   | [7,10,4,3,20,15]     |
| 4 | 20   | No          | 3 | no swap               | [7,10,4,3,20,15]     |

Final: swap A[4] with A[5] (pivot)
Array: [7, 10, 4, 3, 15, 20]
Pivot index p = 4

Check: k=2 vs p=4 → k < p → search left half

**Iteration 2: quickselect(A, 0, 3, k=2)**
Pivot = A[3] = 3

| j | A[j] | A[j] <= 3? | i | Action                | Array state           |
|---|------|-------------|---|------------------------|----------------------|
| - | -    | -           | -1| Initialize             | [7,10,4,3,15,20]     |
| 0 | 7    | No          | -1| no swap               | [7,10,4,3,15,20]     |
| 1 | 10   | No          | -1| no swap               | [7,10,4,3,15,20]     |
| 2 | 4    | No          | -1| no swap               | [7,10,4,3,15,20]     |

Final: swap A[0] with A[3] (pivot)
Array: [3, 10, 4, 7, 15, 20]
Pivot index p = 0

Check: k=2 vs p=0 → k > p → search right half

**Iteration 3: quickselect(A, 1, 3, k=2)**
Pivot = A[3] = 7

| j | A[j] | A[j] <= 7? | i | Action                | Array state           |
|---|------|-------------|---|------------------------|----------------------|
| - | -    | -           | 0 | Initialize             | [3,10,4,7,15,20]     |
| 1 | 10   | No          | 0 | no swap               | [3,10,4,7,15,20]     |
| 2 | 4    | Yes         | 1 | swap A[1] with A[2]   | [3,4,10,7,15,20]     |

Final: swap A[2] with A[3] (pivot)
Array: [3, 4, 7, 10, 15, 20]
Pivot index p = 2

Check: k=2 == p=2 → **FOUND!**

**5) Result**
A[2] = **7**

**6) Verification**
Sorted array: [3, 4, 7, 10, 15, 20]
Element at index 2 (0-indexed) = 7 ✓
Elements smaller than 7: {3, 4} = 2 elements ✓

### Final Answer
3rd smallest element: **7**

---

## Median of Medians (Guaranteed O(n))

For worst-case O(n), use median-of-medians pivot selection:
1. Divide into groups of 5
2. Find median of each group
3. Recursively find median of medians
4. Use as pivot

This guarantees good partition but has higher constants.

---

## Common Failure Modes

1. **Wrong k adjustment** → when recursing right, k stays same (not k - p - 1 in some implementations)
2. **Bad pivot choice** → worst case O(n²) with sorted input
3. **Off-by-one in partition** → be careful with boundary conditions
4. **Confusing 0-indexed vs 1-indexed** → clarify k meaning
5. **Not handling equal elements** → partition handles them, but verify
6. **Modifying original array** → quickselect is in-place, mutates array
