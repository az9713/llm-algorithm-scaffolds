# N-Queens Problem Scaffold

## When to Use
- Placing N items on an N×N grid with constraints
- Configuration problems with mutual exclusion
- Any problem where choices must satisfy global constraints
- Classic constraint satisfaction problems
- Learning backtracking fundamentals

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Backtracking.

1) Problem Restatement
- Place N queens on an N×N chessboard
- No two queens may attack each other
- Queens attack along rows, columns, and diagonals
- Find one valid configuration (or all configurations)

2) State Definition
State = (row, columns_placed)

Where:
- row = current row being filled (0 to N-1)
- columns_placed = list of column positions for rows 0..row-1

Constraint tracking:
- used_columns = set of columns already occupied
- used_diag1 = set of (row - col) values (↘ diagonals)
- used_diag2 = set of (row + col) values (↙ diagonals)

3) Constraint Check Semantics
For placing queen at (row, col):
- col not in used_columns
- (row - col) not in used_diag1
- (row + col) not in used_diag2

If all pass: placement is valid.

4) Algorithm Procedure (Backtracking)
a) Base case: if row == N, solution found → record and return
b) For each column c in 0..N-1:
   - If placing queen at (row, c) is valid:
     - Add c to used_columns, update diagonals
     - Recurse to row + 1
     - Remove c from used_columns, restore diagonals (backtrack)
c) If no valid column found: backtrack to previous row

5) Termination Condition
- Row N reached → valid solution found
- All possibilities exhausted → no solution (or all solutions found)

6) Verification Protocol
- Count: exactly N queens placed
- No two queens share same row (automatic by construction)
- No two queens share same column
- No two queens share same diagonal
```

---

## Worked Example

### Problem
Solve 4-Queens: Place 4 queens on a 4×4 board.

### Expected Scaffold Application

**1) Problem Restatement**
- 4×4 board, place 4 queens
- Each queen on different row, column, and diagonals

**2) Initial State**
- row = 0
- columns_placed = []
- used_columns = {}
- used_diag1 = {} (row - col)
- used_diag2 = {} (row + col)

**3-4) Algorithm Execution (showing backtracking)**

```
Row 0: Try col 0
  Place Q at (0,0): used_cols={0}, diag1={0}, diag2={0}

  Row 1: Try col 0 - blocked (column)
         Try col 1 - blocked (diag1: 1-1=0)
         Try col 2 - VALID
    Place Q at (1,2): used_cols={0,2}, diag1={0,-1}, diag2={0,3}

    Row 2: Try col 0 - blocked (column)
           Try col 1 - blocked (diag2: 2+1=3)
           Try col 2 - blocked (column)
           Try col 3 - blocked (diag1: 2-3=-1)
           NO VALID COLUMN → BACKTRACK

  Remove Q from (1,2)

  Row 1: Try col 3 - VALID
    Place Q at (1,3): used_cols={0,3}, diag1={0,-2}, diag2={0,4}

    Row 2: Try col 0 - blocked (column)
           Try col 1 - VALID
      Place Q at (2,1): used_cols={0,1,3}, diag1={0,-2,1}, diag2={0,4,3}

      Row 3: Try col 0 - blocked (column)
             Try col 1 - blocked (column)
             Try col 2 - blocked (diag1: 3-2=1)
             Try col 3 - blocked (column)
             NO VALID COLUMN → BACKTRACK

    Remove Q from (2,1)

    Row 2: Try col 2 - blocked (diag2: 2+2=4)
           Try col 3 - blocked (column)
           NO VALID COLUMN → BACKTRACK

  Remove Q from (1,3)
  Row 1: No more columns → BACKTRACK

Remove Q from (0,0)

Row 0: Try col 1
  Place Q at (0,1): used_cols={1}, diag1={-1}, diag2={1}

  Row 1: Try col 0 - blocked (diag2: 1+0=1)
         Try col 1 - blocked (column)
         Try col 2 - blocked (diag1: 1-2=-1)
         Try col 3 - VALID
    Place Q at (1,3): used_cols={1,3}, diag1={-1,-2}, diag2={1,4}

    Row 2: Try col 0 - VALID
      Place Q at (2,0): used_cols={0,1,3}, diag1={-1,-2,2}, diag2={1,4,2}

      Row 3: Try col 0 - blocked (column)
             Try col 1 - blocked (column)
             Try col 2 - VALID!
        Place Q at (3,2): SOLUTION FOUND!
```

**5) Solution Found**
```
. Q . .    (row 0, col 1)
. . . Q    (row 1, col 3)
Q . . .    (row 2, col 0)
. . Q .    (row 3, col 2)
```

**6) Verification**
- 4 queens placed ✓
- Columns used: {0, 1, 2, 3} - all different ✓
- Diag1 (row-col): {-1, -2, 2, 1} - all different ✓
- Diag2 (row+col): {1, 4, 2, 5} - all different ✓
- No attacks possible ✓

### Final Answer
Solution: Queens at (0,1), (1,3), (2,0), (3,2)

---

## Common Failure Modes

1. **Wrong diagonal formula** → row-col and row+col are the standard formulas
2. **Not backtracking properly** → must undo constraint additions
3. **Checking row conflicts** → unnecessary if placing one queen per row
4. **Off-by-one errors** → use 0-indexed or 1-indexed consistently
5. **Stopping at first solution when all needed** → control return behavior
6. **Not pruning early** → check constraints before recursing
