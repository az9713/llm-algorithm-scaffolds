# Binary Search Scaffold

## When to Use
- Searching in sorted array
- Finding boundary conditions (first/last occurrence)
- Searching in monotonic functions
- Optimization problems with binary search on answer
- Any problem where search space can be halved

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Binary Search.

1) Problem Restatement
- Given: sorted array A[0..n-1] and target value T
- Goal: find index of T, or appropriate boundary
- Precondition: array must be sorted (or problem has monotonic property)

2) State Definition
State = (lo, hi) defining search interval

Invariant (CRITICAL - choose one):
- T is in [lo, hi] (inclusive)
- T is in [lo, hi) (exclusive hi)
- Answer is in [lo, hi]

The invariant must be maintained throughout.

3) Midpoint and Comparison
mid = lo + (hi - lo) / 2  (avoids overflow)

Compare A[mid] with T:
- A[mid] == T: found (or continue for boundaries)
- A[mid] < T: search right half
- A[mid] > T: search left half

4) Algorithm Procedure (Standard: find any occurrence)
a) lo = 0, hi = n - 1
b) While lo <= hi:
   - mid = lo + (hi - lo) / 2
   - If A[mid] == T: return mid
   - If A[mid] < T: lo = mid + 1
   - If A[mid] > T: hi = mid - 1
c) Return -1 (not found)

5) Termination Condition
- lo > hi: element not found
- A[mid] == T: element found

6) Verification Protocol
- Check returned index: A[index] == T
- If not found, verify T not in array
- Check boundary cases: empty array, single element
```

---

## Worked Example

### Problem
Find index of 23 in A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

### Expected Scaffold Application

**1) Problem Restatement**
- Array: 10 elements, sorted ascending
- Target: 23
- Find index of 23

**2) Initial State**
- lo = 0, hi = 9
- Invariant: if 23 exists, it's in A[lo..hi]

**3-4) Algorithm Execution**

| Iteration | lo | hi | mid | A[mid] | Comparison | Action      |
|-----------|----|----|-----|--------|------------|-------------|
| 1         | 0  | 9  | 4   | 16     | 16 < 23    | lo = 5      |
| 2         | 5  | 9  | 7   | 56     | 56 > 23    | hi = 6      |
| 3         | 5  | 6  | 5   | 23     | 23 == 23   | FOUND!      |

**5) Result**
Found at index **5**

**6) Verification**
- A[5] = 23 = target ✓
- Binary search took 3 comparisons for 10 elements
- log₂(10) ≈ 3.3, so 3 comparisons is optimal ✓

### Final Answer
Index: **5**

---

## Variant: Find First Occurrence

**Problem:** Find first (leftmost) occurrence of 23 in [1, 5, 23, 23, 23, 50, 60]

```
lo = 0, hi = n - 1, result = -1

while lo <= hi:
    mid = lo + (hi - lo) / 2
    if A[mid] == T:
        result = mid
        hi = mid - 1   # keep searching left
    elif A[mid] < T:
        lo = mid + 1
    else:
        hi = mid - 1

return result
```

| Iteration | lo | hi | mid | A[mid] | Action           |
|-----------|----|----|-----|--------|------------------|
| 1         | 0  | 6  | 3   | 23     | result=3, hi=2   |
| 2         | 0  | 2  | 1   | 5      | lo=2             |
| 3         | 2  | 2  | 2   | 23     | result=2, hi=1   |
| 4         | 2  | 1  | -   | -      | lo>hi, done      |

First occurrence: index **2**

---

## Variant: Find Last Occurrence

Same but: when A[mid] == T, set lo = mid + 1 to search right.

---

## Variant: Binary Search on Answer

**Problem:** Find minimum speed to finish in time T.

If problem has monotonic property (speed ≥ X works iff speed ≥ X+1 works):
- Binary search on speed values
- Check if speed works
- Find minimum working speed

---

## Common Failure Modes

1. **Integer overflow in mid** → use mid = lo + (hi - lo) / 2
2. **Infinite loop** → ensure lo or hi changes each iteration
3. **Off-by-one errors** → be precise about inclusive/exclusive bounds
4. **Wrong invariant** → clearly define what [lo, hi] means
5. **Not handling duplicates** → specify first/last/any occurrence
6. **Unsorted input** → binary search requires sorted data
