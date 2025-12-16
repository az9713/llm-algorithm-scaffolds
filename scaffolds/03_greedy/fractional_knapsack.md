# Fractional Knapsack Scaffold

## When to Use
- Knapsack problem where items can be divided
- Maximizing value with weight constraint
- Resource allocation with continuous quantities
- When items are divisible (gold dust, liquids, time)
- NOT for indivisible items (use DP 0/1 Knapsack instead)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following Fractional Knapsack problem using Greedy.

1) Problem Restatement
- Given: n items with values v[i] and weights w[i]
- Knapsack capacity: W
- Items are DIVISIBLE (can take fraction 0 ≤ x[i] ≤ 1)
- Goal: maximize total value while total weight ≤ W
- Maximize: Σ(x[i] × v[i]) subject to Σ(x[i] × w[i]) ≤ W

2) State Definition
State = (remaining_capacity, items_with_ratios)

Where:
- remaining_capacity = W - weight_taken_so_far
- For each item: compute value_density = v[i] / w[i]
- Sort items by value_density (descending)

3) Greedy Choice Property
Always take as much as possible of the highest value-density item first.

Why this works:
- Value per unit weight is maximized by high-density items
- Taking fractions allows optimal packing
- Proven optimal for fractional version

4) Algorithm Procedure
a) Compute value_density[i] = v[i] / w[i] for each item
b) Sort items by value_density in descending order
c) remaining = W
d) total_value = 0
e) For each item i in sorted order:
   - If w[i] ≤ remaining:
     - Take entire item: x[i] = 1
     - remaining -= w[i]
     - total_value += v[i]
   - Else if remaining > 0:
     - Take fraction: x[i] = remaining / w[i]
     - total_value += x[i] × v[i]
     - remaining = 0
     - break
f) Return total_value and fractions taken

5) Termination Condition
- Knapsack full (remaining = 0)
- All items considered

6) Verification Protocol
- Total weight ≤ W
- No item fraction exceeds 1 or is negative
- Total value computed correctly
- Greedy optimal (no better value-density item was skipped)
```

---

## Worked Example

### Problem
Knapsack capacity W = 50
| Item | Value | Weight | Value/Weight |
|------|-------|--------|--------------|
| A    | 60    | 10     | 6.0          |
| B    | 100   | 20     | 5.0          |
| C    | 120   | 30     | 4.0          |

### Expected Scaffold Application

**1) Problem Restatement**
- 3 items, knapsack capacity = 50
- Items are divisible
- Maximize value

**2) Compute Value Density**
| Item | Value | Weight | Density |
|------|-------|--------|---------|
| A    | 60    | 10     | 6.0     |
| B    | 100   | 20     | 5.0     |
| C    | 120   | 30     | 4.0     |

Sorted by density: A (6.0), B (5.0), C (4.0)

**3-4) Greedy Selection**

| Step | Item | Density | Weight | Remaining | Take        | Value Added |
|------|------|---------|--------|-----------|-------------|-------------|
| Init | -    | -       | -      | 50        | -           | 0           |
| 1    | A    | 6.0     | 10     | 50        | All (x=1)   | 60          |
|      |      |         |        | 40        |             | Total: 60   |
| 2    | B    | 5.0     | 20     | 40        | All (x=1)   | 100         |
|      |      |         |        | 20        |             | Total: 160  |
| 3    | C    | 4.0     | 30     | 20        | Fraction    | ?           |
|      |      |         |        |           | x = 20/30   | 80          |
|      |      |         |        |           | = 2/3       | Total: 240  |
|      |      |         |        | 0         | FULL        |             |

**Item C fraction calculation:**
- Need 20 more weight capacity
- Item C weighs 30
- Take fraction: 20/30 = 2/3
- Value gained: (2/3) × 120 = 80

**5) Result**
| Item | Fraction Taken | Weight Used | Value Gained |
|------|----------------|-------------|--------------|
| A    | 1.0            | 10          | 60           |
| B    | 1.0            | 20          | 100          |
| C    | 2/3 ≈ 0.667    | 20          | 80           |
| **Total** |           | **50**      | **240**      |

**6) Verification**
- Total weight: 10 + 20 + 20 = 50 = W ✓
- All fractions ∈ [0, 1] ✓
- Took highest density items first ✓
- Total value: 60 + 100 + 80 = 240 ✓

### Final Answer
Maximum value: **240**
Take: 100% of A, 100% of B, 66.7% of C

---

## Comparison: Fractional vs 0/1 Knapsack

Same items, same W = 50:

**Fractional (Greedy):** A + B + 2/3C = 240

**0/1 (must take whole items):**
- A + B = 60 + 100 = 160 (weight 30)
- A + C = 60 + 120 = 180 (weight 40)
- B + C = 100 + 120 = 220 (weight 50) ← Best for 0/1

Fractional allows 240 > 220 because we can take partial C.

---

## Common Failure Modes

1. **Sorting by value instead of density** → WRONG! High value but heavy items may be bad
2. **Sorting by weight** → WRONG! Light items may have low value
3. **Using for 0/1 knapsack** → Greedy doesn't work for indivisible items
4. **Taking fractions > 1** → can only take up to 100% of item
5. **Not stopping when full** → continue processing wastes effort
6. **Integer division errors** → use float/decimal for fractions
