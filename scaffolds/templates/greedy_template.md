# Generic Greedy Algorithm Scaffold Template

## Category Definition

**What makes Greedy Algorithms unique:**
- Make locally optimal choice at each step
- Never reconsider past decisions
- Hope local optimum leads to global optimum

**When to use a Greedy Algorithm:**
- Optimal substructure: optimal solution contains optimal sub-solutions
- Greedy choice property: local best leads to global best
- Problem has matroid structure (independence system)

**Key distinguishing features:**
- Simple, fast (often O(n log n) due to sorting)
- No backtracking
- Must PROVE greedy works (or use DP instead)
- Often involves sorting by some criterion

---

## Essential State Components

### [REQUIRED] - Must be in every greedy scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `sorted_items` | Items ordered by greedy criterion | `by finish time` |
| `selected` | Items/choices made so far | `{task1, task3}` |
| `current_state` | State after selections | `time=5, weight=10` |
| `greedy_criterion` | How to rank choices | `value/weight ratio` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `remaining_capacity` | Resource-constrained problems | `capacity = 15` |
| `last_selection` | When new choice depends on previous | `last_end_time = 4` |
| `running_total` | Accumulating value/cost | `total_value = 42` |

### State Invariants
- Once selected, an item stays selected
- Greedy criterion ordering is fixed (determined upfront)
- Each selection is compatible with previous selections

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Items/choices: [YOUR_ITEM_SET]
   - Constraint: [YOUR_CONSTRAINT]
   - Objective: [MAXIMIZE/MINIMIZE] [YOUR_OBJECTIVE]

2) Greedy Criterion
   Sort items by: [YOUR_SORTING_KEY]
   Ordering: [ASCENDING/DESCENDING]

   WHY this works: [PROOF_SKETCH]

3) State Definition
   State = (
       selected: [SET_OF_CHOSEN_ITEMS],
       [RESOURCE_STATE]: ___,
       [CONSTRAINT_STATE]: ___
   )

4) Selection Rule
   For each item in sorted order:
       If [FEASIBILITY_CHECK]:
           Add item to selected
           Update [STATE_VARIABLES]

5) Termination
   - All items considered, OR
   - [RESOURCE_EXHAUSTED], OR
   - [GOAL_REACHED]

6) Verification
   - All constraints satisfied
   - No feasible item was wrongly skipped
   - [OPTIMALITY_ARGUMENT]: local choices led to global optimum
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Greedy criterion is well-defined
- [ ] Proof (or strong argument) that greedy works
- [ ] Sorting order is correct (ascending vs descending)
- [ ] Feasibility check is precise
- [ ] State updates are correct after each selection
- [ ] Edge cases: empty input, all items selected, none selected

---

## Derivation Examples

### Example 1: Activity Selection (from this template)

**Filled-in values:**
- Greedy criterion: **Earliest finish time**
- Sorting: **Ascending by finish time**
- Feasibility: **Start time ≥ last finish time**
- Why it works: **Earliest finish leaves most room for future activities**

```
Sort activities by finish time (ascending)
selected = []
last_finish = -∞

For each activity in sorted order:
    If activity.start >= last_finish:
        selected.append(activity)
        last_finish = activity.finish
```

---

### Example 2: Fractional Knapsack (from this template)

**Filled-in values:**
- Greedy criterion: **Value-to-weight ratio (value density)**
- Sorting: **Descending by density**
- Feasibility: **Remaining capacity > 0**
- Why it works: **Highest value per unit weight maximizes total value**

```
Sort items by value/weight (descending)
remaining = capacity
total_value = 0

For each item in sorted order:
    If remaining >= item.weight:
        Take all: remaining -= item.weight, total += item.value
    Else:
        Take fraction: total += (remaining/item.weight) * item.value
        remaining = 0
        break
```

---

### Example 3: Huffman Coding (from this template)

**Filled-in values:**
- Greedy criterion: **Minimum frequency**
- Data structure: **Min-heap (priority queue)**
- Selection: **Always combine two smallest frequencies**
- Why it works: **Low-frequency symbols get longer codes (deeper in tree)**

```
Build min-heap of (frequency, node) pairs

While heap has more than one node:
    left = extract_min()
    right = extract_min()
    merged = new_node(frequency = left.freq + right.freq)
    merged.left = left
    merged.right = right
    insert(merged)

Return remaining node as Huffman tree root
```

---

## When Greedy DOESN'T Work

**0/1 Knapsack:** Greedy by value/weight ratio fails.
- Example: Items (60, 10), (100, 20), (120, 30), capacity 50
- Greedy: takes (60,10) first → suboptimal
- Must use DP instead

**Red flags that greedy may fail:**
- Items can't be divided (fractional)
- Choice affects future choices in complex ways
- No clear dominance relationship
- Counterexamples exist

---

## Creating Your Own Greedy Scaffold

1. **Identify the greedy criterion**
   - What makes one choice "better" than another?
   - This becomes your sorting key

2. **Prove (or argue) correctness**
   - Exchange argument: show greedy choice is at least as good
   - Stays ahead: greedy solution dominates alternatives
   - If you can't prove it, consider DP

3. **Define feasibility**
   - When is a choice valid given current state?
   - What constraints must be maintained?

4. **Determine state updates**
   - How does selecting an item change the problem?
   - What resources are consumed?

5. **Handle edge cases**
   - Empty input?
   - All items feasible?
   - No items feasible?
