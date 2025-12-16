# Hill Climbing Scaffold

## When to Use
- Simple local optimization
- Quick baseline solutions
- Problems with smooth landscapes
- When computational resources are limited
- Starting point for more sophisticated methods
- Local search component in hybrid algorithms

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following optimization problem using Hill Climbing.

1) Problem Restatement
- Given: objective function f(x) to maximize/minimize
- Goal: find local optimum
- Limitation: may get stuck in local optima (not global)

2) State Definition
State = (current_solution, current_value)

Where:
- current_solution = current position in search space
- current_value = f(current_solution)

3) Neighbor Generation
Define how to generate neighboring solutions:
- Continuous: add small random perturbation
- Discrete: flip bit, swap elements, change one value
- Must be "local" moves (small changes)

4) Hill Climbing Variants

Simple (Steepest Ascent):
- Evaluate ALL neighbors
- Move to the BEST neighbor if it improves
- Stop when no neighbor is better

First-Choice:
- Generate neighbors randomly
- Move to FIRST neighbor that improves
- More efficient for large neighborhood

Stochastic:
- Randomly select among uphill neighbors
- More exploration than steepest ascent

5) Algorithm Procedure (Steepest Ascent)
a) Initialize: x = starting solution
b) Loop:
   - Generate all neighbors N(x)
   - best_neighbor = argmax f(n) for n in N(x)
   - If f(best_neighbor) > f(x):
     - x = best_neighbor
   - Else:
     - Return x (local optimum reached)

6) Verification Protocol
- No neighbor is better than final solution
- Objective value at each step (should be monotonic)
- Try multiple random restarts to find global optimum
```

---

## Worked Example

### Problem
Maximize f(x) = -(x-3)² + 9 for integer x ∈ [0, 6]
Starting at x = 0.

### Expected Scaffold Application

**1) Problem Restatement**
- Parabola with maximum at x = 3, f(3) = 9
- Integer search space: {0, 1, 2, 3, 4, 5, 6}

**2) State Definition**
- x = current integer position
- f(x) = -(x-3)² + 9

**3) Neighbors**
For integer x, neighbors are x-1 and x+1 (if in range).

**4-5) Algorithm Execution**

| Step | x | f(x) | Neighbors | f(neighbors) | Best neighbor | Move? |
|------|---|------|-----------|--------------|---------------|-------|
| 0    | 0 | 0    | {1}       | {5}          | 1             | Yes   |
| 1    | 1 | 5    | {0,2}     | {0,8}        | 2             | Yes   |
| 2    | 2 | 8    | {1,3}     | {5,9}        | 3             | Yes   |
| 3    | 3 | 9    | {2,4}     | {8,8}        | 2 or 4        | No    |

**Step 3 analysis:**
- Current: f(3) = 9
- f(2) = 8 < 9
- f(4) = 8 < 9
- No improvement possible → STOP

**6) Result**
Local (and global) optimum: x = **3**, f(x) = **9**

### Final Answer
Maximum at x = **3**, f(x) = **9**

---

## Example: Stuck in Local Optimum

**Problem:** Maximize f(x) = sin(x) + sin(2x) for x ∈ [0, 10]
(Multiple peaks!)

Starting at x = 8:
```
Step 0: x = 8.0, f = 0.91
Step 1: x = 7.9, f = 0.98
Step 2: x = 7.8, f = 1.04
...
Step N: x = 7.5, f = 1.14 (local max)
```

Stuck at local maximum x ≈ 7.5 instead of global maximum x ≈ 1.8.

**Solution:** Random restarts or use simulated annealing.

---

## Random Restart Hill Climbing

```
best_overall = None
for i in 1 to num_restarts:
    x = random_starting_point()
    local_best = hill_climb(x)
    if local_best better than best_overall:
        best_overall = local_best
return best_overall
```

This helps find global optimum probabilistically.

---

## Comparison of Variants

| Variant | Pros | Cons |
|---------|------|------|
| Steepest Ascent | Best local move | Expensive if many neighbors |
| First-Choice | Fast per iteration | May miss best neighbor |
| Stochastic | More exploration | Slower convergence |
| Random Restart | Better global search | Need many restarts |

---

## Common Failure Modes

1. **Stuck in local optimum** → use random restarts or simulated annealing
2. **Plateaus (flat regions)** → sideways moves or random jumps
3. **Ridges** → diagonal moves may be needed
4. **Wrong neighbor definition** → too small = slow, too large = misses details
5. **Not tracking best-ever** → may lose good solution
6. **Infinite loop on plateau** → limit sideways moves
