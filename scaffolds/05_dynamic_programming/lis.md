# Longest Increasing Subsequence (LIS) Scaffold

## When to Use
- Finding longest monotonically increasing subsequence
- Box stacking / Russian doll problems
- Scheduling with increasing constraints
- Patience sorting
- Longest chain problems

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following LIS problem using Dynamic Programming.

1) Problem Restatement
- Given: sequence A = a₁, a₂, ..., aₙ
- Find: longest subsequence where elements are strictly increasing
- Subsequence: elements in order, not necessarily contiguous

2) State Definition (O(n²) approach)
dp[i] = length of LIS ending at index i

For O(n log n) approach:
tails[k] = smallest ending element of all LIS of length k

3) Recurrence Relation (O(n²))
dp[i] = 1 + max(dp[j]) for all j < i where A[j] < A[i]
If no such j exists: dp[i] = 1

Intuition: LIS ending at i extends some LIS ending at j where A[j] < A[i]

4) Base Cases
dp[i] = 1 for all i (each element is LIS of length 1)

5) Computation Order
Left to right: dp[1], dp[2], ..., dp[n]

6) Solution Extraction
- LIS length: max(dp[i]) over all i
- Actual LIS: backtrack from index with max dp value
  - Record predecessor during forward pass
  - Follow predecessor chain backward

7) Verification Protocol
- Extracted sequence is strictly increasing
- It's a valid subsequence of original array
- No longer increasing subsequence exists
```

---

## Worked Example

### Problem
Find LIS of A = [10, 22, 9, 33, 21, 50, 41, 60, 80]

### Expected Scaffold Application

**1) Problem Restatement**
- Array of 9 integers
- Find longest strictly increasing subsequence

**2-4) Build DP Table (O(n²) method)**

| Index | Value | Check previous | dp[i] | Predecessor |
|-------|-------|----------------|-------|-------------|
| 0     | 10    | (none)         | 1     | -1          |
| 1     | 22    | 10<22 ✓        | 2     | 0           |
| 2     | 9     | 10≮9, 22≮9     | 1     | -1          |
| 3     | 33    | 10<33, 22<33 → max(1,2)+1 | 3 | 1      |
| 4     | 21    | 10<21, 9<21 → max(1,1)+1  | 2 | 0 or 2  |
| 5     | 50    | 10,22,33<50 → max(1,2,3)+1 | 4 | 3      |
| 6     | 41    | 10,22,33<41 → max(1,2,3)+1 | 4 | 3      |
| 7     | 60    | 10,22,33,50,41<60 → max+1 | 5 | 5 or 6  |
| 8     | 80    | all except 9<80 → max+1   | 6 | 7       |

**Detailed calculation for index 5 (value 50):**
- j=0: A[0]=10 < 50, dp[0]=1
- j=1: A[1]=22 < 50, dp[1]=2
- j=2: A[2]=9 < 50, dp[2]=1
- j=3: A[3]=33 < 50, dp[3]=3 ← max
- j=4: A[4]=21 < 50, dp[4]=2
- dp[5] = 3 + 1 = 4, predecessor = 3

**5) LIS Length**
max(dp) = dp[8] = **6**

**6) Backtrack for LIS**
Starting at index 8 (value 80, dp=6):
- Index 8: 80, predecessor = 7
- Index 7: 60, predecessor = 5
- Index 5: 50, predecessor = 3
- Index 3: 33, predecessor = 1
- Index 1: 22, predecessor = 0
- Index 0: 10, predecessor = -1 (done)

**LIS: [10, 22, 33, 50, 60, 80]**

**7) Verification**
- 10 < 22 < 33 < 50 < 60 < 80 ✓ (strictly increasing)
- All elements from original array ✓
- Order preserved ✓
- Length 6 ✓

### Final Answer
LIS: **[10, 22, 33, 50, 60, 80]**
Length: **6**

---

## O(n log n) Algorithm (Patience Sorting)

More efficient approach using binary search:

```
tails = []
for each element x in array:
    if x > last element of tails (or tails empty):
        append x to tails
    else:
        binary search for first element >= x
        replace it with x

LIS length = len(tails)
```

**For our example:**
| x  | Action                     | tails         |
|----|----------------------------|---------------|
| 10 | append                     | [10]          |
| 22 | append                     | [10, 22]      |
| 9  | replace 10                 | [9, 22]       |
| 33 | append                     | [9, 22, 33]   |
| 21 | replace 22                 | [9, 21, 33]   |
| 50 | append                     | [9, 21, 33, 50] |
| 41 | replace 50                 | [9, 21, 33, 41] |
| 60 | append                     | [9, 21, 33, 41, 60] |
| 80 | append                     | [9, 21, 33, 41, 60, 80] |

Length = 6 ✓

Note: `tails` is NOT the actual LIS, just used to track length.

---

## Common Failure Modes

1. **Strict vs non-strict** → "increasing" usually means strict (<, not ≤)
2. **Wrong predecessor tracking** → must track index, not value
3. **Not initializing dp[i]=1** → each element alone is valid LIS
4. **Taking first j instead of max** → must find max dp[j] among valid j
5. **Confusing tails array with LIS** → tails gives length, not sequence
6. **Binary search off-by-one** → use lower_bound for first ≥ x
