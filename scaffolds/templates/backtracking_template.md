# Generic Backtracking Scaffold Template

## Category Definition

**What makes Backtracking unique:**
- Systematic search through solution space
- Build solution incrementally
- Abandon partial solutions that can't lead to valid complete solution

**When to use Backtracking:**
- Constraint satisfaction problems
- Finding all solutions (or one solution)
- Decision problems with many constraints
- Combinatorial problems (permutations, combinations)

**Key distinguishing features:**
- Recursive exploration of choices
- Pruning invalid branches early
- Undo choices when backtracking
- Often exponential but pruning helps

---

## Essential State Components

### [REQUIRED] - Must be in every backtracking scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `partial_solution` | Current choices made | `[Q at (0,1), Q at (1,3)]` |
| `decision_point` | Current position in search | `row = 2` |
| `constraints` | Rules that must be satisfied | `no two queens attack` |
| `is_valid(choice)` | Check if choice is allowed | `can_place(row, col)` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `used` | Tracking used resources | `used_columns = {1, 3}` |
| `remaining` | Items/choices left | `remaining_sum = 15` |
| `pruning_state` | For early termination | `sum_so_far > target` |
| `all_solutions` | When collecting all | `solutions = [...]` |

### State Invariants
- Partial solution satisfies all constraints so far
- Backtracking restores state exactly to before the choice
- All valid choices are explored (completeness)

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Solution structure: [WHAT_COMPLETE_SOLUTION_LOOKS_LIKE]
   - Constraints: [RULES_TO_SATISFY]
   - Goal: [FIND_ONE / FIND_ALL / COUNT]

2) State Definition
   State = (
       partial_solution: [CURRENT_CHOICES],
       decision_index: [WHERE_WE_ARE],
       [CONSTRAINT_TRACKING]: ___
   )

3) Base Case
   If [SOLUTION_COMPLETE]:
       [RECORD/RETURN] solution
       Return [TRUE / continue searching]

4) Recursive Case
   For each [CHOICE] at current decision point:
       If [IS_VALID](choice):
           [MAKE_CHOICE]: update state
           result = backtrack(next_decision_point)
           [UNDO_CHOICE]: restore state

           If result == found and only need one:
               Return found

5) Pruning (Optional but important)
   Before exploring choice:
       If [CANNOT_POSSIBLY_SUCCEED]:
           Skip this branch

6) Termination
   - Solution found (for find-one)
   - All branches explored (for find-all)

7) Verification
   - Solution satisfies all constraints
   - All choices are valid given previous choices
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Solution structure is clearly defined
- [ ] All constraints are identified
- [ ] IS_VALID check is complete and correct
- [ ] MAKE_CHOICE and UNDO_CHOICE are symmetric
- [ ] Base case correctly identifies complete solutions
- [ ] Pruning conditions are sound (don't prune valid solutions)

---

## Derivation Examples

### Example 1: N-Queens (from this template)

**Filled-in values:**
- Partial solution: **List of column positions, one per row**
- Decision point: **Current row**
- Constraints: **No two queens share row/column/diagonal**
- IS_VALID: **Column not used, diagonals not used**

```
State = (row, columns_placed, used_cols, used_diag1, used_diag2)

Base case: row == N → solution found

For col in 0..N-1:
    If col not in used_cols AND
       (row-col) not in used_diag1 AND
       (row+col) not in used_diag2:

        MAKE: add col, update sets
        backtrack(row + 1)
        UNDO: remove col, restore sets
```

---

### Example 2: Sudoku Solver (from this template)

**Filled-in values:**
- Partial solution: **Filled grid cells**
- Decision point: **Next empty cell**
- Constraints: **Row/column/box uniqueness**
- IS_VALID: **Digit not in row, column, or 3x3 box**

```
State = (grid, next_empty_cell)

Base case: no empty cells → solved

For digit in 1..9:
    If valid_placement(cell, digit):
        MAKE: grid[cell] = digit
        result = backtrack(next_empty)
        If result: return True
        UNDO: grid[cell] = empty

Return False (no valid digit)
```

---

### Example 3: Subset Sum (from this template)

**Filled-in values:**
- Partial solution: **Subset of items selected**
- Decision point: **Current item index**
- Constraints: **Sum equals target**
- IS_VALID: **Current sum + item ≤ target**
- Pruning: **Current sum > target**

```
State = (index, current_sum, selected_items)

Base case:
    If current_sum == target: solution found
    If index == n: no solution on this path

Pruning: If current_sum > target: return (prune)

# Try including current item
MAKE: current_sum += items[index]
backtrack(index + 1)
UNDO: current_sum -= items[index]

# Try excluding current item
backtrack(index + 1)
```

---

## Pruning Strategies

Effective pruning dramatically improves performance:

| Strategy | Description | Example |
|----------|-------------|---------|
| **Constraint propagation** | Eliminate invalid choices upfront | Sudoku: naked singles |
| **Bound checking** | Prune if optimal is impossible | Sum already exceeds target |
| **Symmetry breaking** | Avoid equivalent solutions | First queen only in left half |
| **Forward checking** | Check if remaining choices exist | No valid digit for empty cell |

---

## Creating Your Own Backtracking Scaffold

1. **Define what a complete solution looks like**
   - How many decisions? What structure?
   - When is the solution "done"?

2. **Identify all constraints**
   - What rules must the solution satisfy?
   - How do choices affect future choices?

3. **Design the IS_VALID check**
   - Given current state, is this choice allowed?
   - What needs to be tracked to check quickly?

4. **Ensure UNDO perfectly reverses MAKE**
   - State after undo must equal state before make
   - This is where bugs commonly hide

5. **Add pruning for performance**
   - What conditions guarantee failure?
   - Can you propagate constraints?
