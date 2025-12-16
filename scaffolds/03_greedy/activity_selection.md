# Activity Selection (Interval Scheduling) Scaffold

## When to Use
- Scheduling non-overlapping activities/meetings
- Maximizing number of tasks completed
- Resource allocation with time windows
- Job scheduling on single machine
- Any interval selection problem

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Greedy Activity Selection.

1) Problem Restatement
- Given: n activities with start times s[i] and finish times f[i]
- Constraint: selected activities cannot overlap
- Goal: maximize number of activities selected

2) State Definition
State = (sorted_activities, selected_set, last_finish_time)

Where:
- activities sorted by finish time (ascending) ← KEY INSIGHT
- selected_set = activities chosen so far
- last_finish_time = finish time of most recently selected activity

3) Greedy Choice Property
Always select the activity that finishes earliest among compatible activities.

Why this works:
- Earliest finish leaves maximum room for future activities
- Proven optimal: greedy stays ahead of any alternative solution

4) Algorithm Procedure
a) Sort activities by finish time: f[1] ≤ f[2] ≤ ... ≤ f[n]
b) Select first activity (earliest finish)
c) last_finish = f[1]
d) For each remaining activity i:
   - If s[i] ≥ last_finish (no overlap):
     - Select activity i
     - Update last_finish = f[i]
e) Return selected activities

5) Termination Condition
- All activities considered
- Result: maximum set of non-overlapping activities

6) Verification Protocol
- Check no two selected activities overlap
- Count selected activities
- Verify no unselected activity could be added without conflict
```

---

## Worked Example

### Problem
Schedule maximum activities from:
| Activity | Start | Finish |
|----------|-------|--------|
| A        | 1     | 4      |
| B        | 3     | 5      |
| C        | 0     | 6      |
| D        | 5     | 7      |
| E        | 3     | 9      |
| F        | 5     | 9      |
| G        | 6     | 10     |
| H        | 8     | 11     |
| I        | 8     | 12     |
| J        | 2     | 14     |
| K        | 12    | 16     |

### Expected Scaffold Application

**1) Problem Restatement**
- 11 activities with time intervals
- Select maximum non-overlapping activities
- Greedy approach: earliest finish time first

**2) Sort by Finish Time**
| Activity | Start | Finish | Order |
|----------|-------|--------|-------|
| A        | 1     | 4      | 1     |
| B        | 3     | 5      | 2     |
| C        | 0     | 6      | 3     |
| D        | 5     | 7      | 4     |
| E        | 3     | 9      | 5     |
| F        | 5     | 9      | 6     |
| G        | 6     | 10     | 7     |
| H        | 8     | 11     | 8     |
| I        | 8     | 12     | 9     |
| J        | 2     | 14     | 10    |
| K        | 12    | 16     | 11    |

**3-4) Greedy Selection**

| Consider | Start | Finish | Last_finish | Decision          |
|----------|-------|--------|-------------|-------------------|
| A        | 1     | 4      | -∞          | SELECT (first)    |
| B        | 3     | 5      | 4           | SKIP (3 < 4)      |
| C        | 0     | 6      | 4           | SKIP (0 < 4)      |
| D        | 5     | 7      | 4           | SELECT (5 ≥ 4)    |
| E        | 3     | 9      | 7           | SKIP (3 < 7)      |
| F        | 5     | 9      | 7           | SKIP (5 < 7)      |
| G        | 6     | 10     | 7           | SKIP (6 < 7)      |
| H        | 8     | 11     | 7           | SELECT (8 ≥ 7)    |
| I        | 8     | 12     | 11          | SKIP (8 < 11)     |
| J        | 2     | 14     | 11          | SKIP (2 < 11)     |
| K        | 12    | 16     | 11          | SELECT (12 ≥ 11)  |

**5) Result**
Selected activities: A, D, H, K
Count: 4 activities

Timeline:
```
A:    [1----4]
D:          [5--7]
H:               [8---11]
K:                    [12----16]
      ─────────────────────────────>
      0  2  4  6  8  10  12  14  16
```

**6) Verification**
- A[1,4] and D[5,7]: no overlap (4 ≤ 5) ✓
- D[5,7] and H[8,11]: no overlap (7 ≤ 8) ✓
- H[8,11] and K[12,16]: no overlap (11 ≤ 12) ✓
- Can we add any skipped activity? No, all overlap with selected ✓

### Final Answer
Maximum activities: 4 (A, D, H, K)

---

## Variant: Weighted Activity Selection

If activities have weights/values, greedy doesn't work.
Use **Dynamic Programming** instead:
- Sort by finish time
- DP[i] = max value ending at or before activity i
- Binary search for last compatible activity

---

## Common Failure Modes

1. **Sorting by start time** → WRONG! Must sort by finish time
2. **Sorting by duration** → WRONG! Short activities may overlap many
3. **Greedy on weights** → doesn't work for weighted version
4. **Off-by-one in overlap check** → s[i] ≥ f[j] means no overlap
5. **Not considering all activities** → must check each one
6. **Forgetting this is unweighted** → for weighted, use DP
