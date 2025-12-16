# Sudoku Solver Scaffold

## When to Use
- Constraint satisfaction problems with fixed domains
- Grid-based puzzles with row/column/block constraints
- Problems requiring propagation + search
- Any problem with mutual exclusion in multiple dimensions
- Exact cover problems

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following Sudoku puzzle using Backtracking with Constraint Propagation.

1) Problem Restatement
- 9×9 grid divided into 9 3×3 boxes
- Fill each cell with digits 1-9
- Each row must contain 1-9 exactly once
- Each column must contain 1-9 exactly once
- Each 3×3 box must contain 1-9 exactly once
- Some cells are pre-filled (given)

2) State Definition
State = (grid, possible_values)

Where:
- grid[r][c] = digit placed (1-9) or 0 (empty)
- possible[r][c] = set of valid digits for empty cell (r,c)

Constraint sets:
- row_used[r] = digits already in row r
- col_used[c] = digits already in column c
- box_used[b] = digits already in box b (b = (r//3)*3 + c//3)

3) Constraint Propagation
For each empty cell (r,c):
- possible[r][c] = {1..9} - row_used[r] - col_used[c] - box_used[box(r,c)]
- If |possible[r][c]| == 1: place that digit (naked single)
- If |possible[r][c]| == 0: contradiction → backtrack

4) Algorithm Procedure
a) Initialize grid with givens, compute possible values
b) Apply constraint propagation until no more naked singles
c) If grid complete: solution found
d) If any cell has 0 possibilities: backtrack
e) Choose cell with minimum remaining values (MRV heuristic)
f) For each value v in possible[chosen_cell]:
   - Place v, update constraints
   - Recurse (repeat from step b)
   - If failed: remove v, restore constraints (backtrack)

5) Termination Condition
- All 81 cells filled with valid digits → solution
- Contradiction reached → backtrack or no solution

6) Verification Protocol
- Each row contains {1,2,3,4,5,6,7,8,9}
- Each column contains {1,2,3,4,5,6,7,8,9}
- Each 3×3 box contains {1,2,3,4,5,6,7,8,9}
- Original givens unchanged
```

---

## Worked Example

### Problem
Solve this 4×4 mini-Sudoku (digits 1-4, 2×2 boxes):
```
1 . | . .
. . | 1 .
----+----
. 1 | . .
. . | . 4
```

### Expected Scaffold Application

**1) Problem Restatement**
- 4×4 grid, 4 2×2 boxes
- Digits 1-4, each appears once per row/column/box
- Givens: (0,0)=1, (1,2)=1, (2,1)=1, (3,3)=4

**2) Initial State**
```
Grid:        Possible values:
1 . . .      1 {2,3,4} {2,3,4} {2,3,4}
. . 1 .      {2,3,4} {2,3,4} 1 {2,3,4}
. 1 . .      {2,3,4} 1 {2,3,4} {2,3,4}
. . . 4      {2,3,4} {2,3,4} {2,3,4} 4
```

**3) Constraint Propagation - Round 1**

Cell (0,1): row has 1, col has 1 → possible = {2,3,4} - {1} - {1} = {2,3,4}
Cell (0,2): row has 1, col has 1 → possible = {2,3,4}
Cell (0,3): row has 1, box has 1 → possible = {2,3,4}
...

Apply row/col/box constraints:
```
(0,1): row={1}, col={1}, box={1} → {2,3,4}
(0,2): row={1}, col={1}, box={1} → {2,3,4}
(0,3): row={1}, col={4}, box={1} → {2,3}
(1,0): row={1}, col={1}, box={1} → {2,3,4}
(1,1): row={1}, col={1}, box={1} → {2,3,4}
(1,3): row={1}, col={4}, box={1} → {2,3}
(2,0): row={1}, col={1}, box={1} → {2,3,4}
(2,2): row={1}, col={1}, box={4} → {2,3}
(2,3): row={1}, col={4}, box={4} → {2,3}
(3,0): row={4}, col={1}, box={1} → {2,3}
(3,1): row={4}, col={1}, box={1} → {2,3}
(3,2): row={4}, col={1}, box={4} → {2,3}
```

**4) Backtracking Search**

Choose cell with MRV: (0,3) has {2,3}

Try (0,3) = 2:
- Update: row0={1,2}, col3={2,4}
- (1,3) now has {3} → place 3
- (2,3) now has {2,3} - {2} - {3} = {} → CONTRADICTION

Backtrack, try (0,3) = 3:
- Update: row0={1,3}, col3={3,4}
- (1,3) now has {2}
- Continue...

After full propagation and search:
```
1 2 3 4
3 4 1 2
4 1 2 3
2 3 4 1
```

**5-6) Verification**
- Row 0: {1,2,3,4} ✓
- Row 1: {1,2,3,4} ✓
- Row 2: {1,2,3,4} ✓
- Row 3: {1,2,3,4} ✓
- Columns: all contain {1,2,3,4} ✓
- Boxes: all contain {1,2,3,4} ✓
- Givens preserved ✓

### Final Answer
```
1 2 3 4
3 4 1 2
4 1 2 3
2 3 4 1
```

---

## Common Failure Modes

1. **Forgetting box constraints** → only checking rows and columns
2. **Wrong box index formula** → use (r//3)*3 + c//3 for 9×9
3. **Not propagating after placement** → missing obvious deductions
4. **Modifying givens** → must preserve original clues
5. **Not restoring state on backtrack** → corrupted constraint sets
6. **Inefficient cell selection** → MRV heuristic dramatically improves speed
