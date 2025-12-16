# Merge Sort Scaffold

## When to Use
- Sorting with guaranteed O(n log n) worst case
- When stable sort is required
- External sorting (sorting data larger than memory)
- Counting inversions
- Problems requiring divide-and-conquer on arrays

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Merge Sort.

1) Problem Restatement
- Given: unsorted array A of n elements
- Goal: sort in non-decreasing order
- Properties needed: stable sort, O(n log n) guaranteed

2) State Definition
State = (array_segment, lo, hi)

Where:
- lo = start index of segment
- hi = end index of segment
- Each recursive call works on A[lo..hi]

3) Divide Step
mid = lo + (hi - lo) / 2

Split array into two halves:
- Left: A[lo..mid]
- Right: A[mid+1..hi]

4) Conquer Step (Recursive)
- Recursively sort left half
- Recursively sort right half
- Base case: single element (lo == hi) is already sorted

5) Combine Step (Merge)
Merge two sorted halves into one sorted array:
a) Create temporary arrays L and R
b) i = 0, j = 0, k = lo
c) While both arrays have elements:
   - If L[i] <= R[j]: A[k++] = L[i++]  (stable: prefer left)
   - Else: A[k++] = R[j++]
d) Copy remaining elements from L or R

6) Verification Protocol
- Array is sorted (A[i] <= A[i+1] for all i)
- All original elements present
- Stable: equal elements maintain relative order
```

---

## Worked Example

### Problem
Sort A = [38, 27, 43, 3, 9, 82, 10]

### Expected Scaffold Application

**1) Problem Restatement**
- 7 elements, unsorted
- Sort in ascending order

**2-5) Divide and Conquer Tree**

```
                [38, 27, 43, 3, 9, 82, 10]
                          |
           ┌──────────────┴──────────────┐
     [38, 27, 43, 3]              [9, 82, 10]
           |                            |
      ┌────┴────┐                 ┌─────┴─────┐
  [38, 27]   [43, 3]          [9, 82]      [10]
     |          |                 |           |
  ┌──┴──┐    ┌──┴──┐          ┌──┴──┐       (base)
[38]  [27]  [43]  [3]       [9]   [82]
```

**Merge operations (bottom-up):**

**Level 3 (base cases):** All single elements are sorted.

**Level 2 merges:**
- Merge [38] and [27]: compare 38 vs 27 → [27, 38]
- Merge [43] and [3]: compare 43 vs 3 → [3, 43]
- Merge [9] and [82]: compare 9 vs 82 → [9, 82]
- [10] stays as [10]

**Level 1 merges:**
Merge [27, 38] and [3, 43]:
| Step | L pointer | R pointer | Compare | Result array        |
|------|-----------|-----------|---------|---------------------|
| 1    | 27        | 3         | 3 < 27  | [3]                 |
| 2    | 27        | 43        | 27 < 43 | [3, 27]             |
| 3    | 38        | 43        | 38 < 43 | [3, 27, 38]         |
| 4    | -         | 43        | copy R  | [3, 27, 38, 43]     |

Merge [9, 82] and [10]:
| Step | L pointer | R pointer | Compare | Result array   |
|------|-----------|-----------|---------|----------------|
| 1    | 9         | 10        | 9 < 10  | [9]            |
| 2    | 82        | 10        | 10 < 82 | [9, 10]        |
| 3    | 82        | -         | copy L  | [9, 10, 82]    |

**Level 0 (final merge):**
Merge [3, 27, 38, 43] and [9, 10, 82]:
| Step | L ptr | R ptr | Compare  | Result                        |
|------|-------|-------|----------|-------------------------------|
| 1    | 3     | 9     | 3 < 9    | [3]                           |
| 2    | 27    | 9     | 9 < 27   | [3, 9]                        |
| 3    | 27    | 10    | 10 < 27  | [3, 9, 10]                    |
| 4    | 27    | 82    | 27 < 82  | [3, 9, 10, 27]                |
| 5    | 38    | 82    | 38 < 82  | [3, 9, 10, 27, 38]            |
| 6    | 43    | 82    | 43 < 82  | [3, 9, 10, 27, 38, 43]        |
| 7    | -     | 82    | copy R   | [3, 9, 10, 27, 38, 43, 82]    |

**6) Final Result**
[3, 9, 10, 27, 38, 43, 82]

**Verification:**
- Sorted: 3 < 9 < 10 < 27 < 38 < 43 < 82 ✓
- All 7 original elements present ✓

### Final Answer
Sorted array: **[3, 9, 10, 27, 38, 43, 82]**

---

## Counting Inversions Variant

Inversion: pair (i, j) where i < j but A[i] > A[j]

During merge, when taking from right array:
- All remaining elements in left array form inversions
- Add (elements remaining in left) to inversion count

---

## Common Failure Modes

1. **Wrong mid calculation** → mid = lo + (hi - lo) / 2
2. **Incorrect split** → left is [lo..mid], right is [mid+1..hi]
3. **Not copying remaining elements** → must empty both temp arrays
4. **Unstable merge** → use <= not < when comparing for stability
5. **Stack overflow** → very deep recursion for large arrays
6. **Not handling empty subarrays** → base case when lo >= hi
