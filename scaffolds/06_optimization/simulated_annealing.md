# Simulated Annealing Scaffold

## When to Use
- Global optimization in discrete or continuous spaces
- Escaping local optima
- Combinatorial optimization (TSP, scheduling)
- When landscape has many local minima
- Problems where gradient is unavailable or expensive

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following optimization problem using Simulated Annealing.

1) Problem Restatement
- Given: objective function f(x) to minimize (or maximize)
- Goal: find global optimum (or near-optimal)
- Challenge: many local optima, need to escape them

2) State Definition
State = (current_solution, current_cost, temperature)

Where:
- current_solution = current candidate
- current_cost = f(current_solution)
- temperature T = controls acceptance probability

3) Temperature Schedule
- Initial temperature T₀: high enough to accept most moves
- Cooling rate: T_new = α × T (α typically 0.9-0.99)
- Final temperature: low enough that only improvements accepted

4) Neighbor Generation & Acceptance
For each iteration:
a) Generate neighbor by small random perturbation
b) Compute Δ = f(neighbor) - f(current)
c) Accept neighbor if:
   - Δ < 0 (improvement): always accept
   - Δ ≥ 0 (worse): accept with probability P = exp(-Δ/T)

5) Algorithm Procedure
a) Initialize: x = random solution, T = T₀
b) While T > T_min and not converged:
   - For i = 1 to iterations_per_temp:
     - x' = generate_neighbor(x)
     - Δ = f(x') - f(x)
     - If Δ < 0 or random() < exp(-Δ/T):
       - x = x'
   - T = α × T (cool down)
c) Return best solution found

6) Verification Protocol
- Track best solution throughout
- Run multiple times (algorithm is stochastic)
- Compare with known optimum if available
- Verify temperature schedule allows sufficient exploration
```

---

## Worked Example

### Problem
Minimize f(x) = x⁴ - 4x² + x over [-3, 3]
This has multiple local minima.

### Expected Scaffold Application

**1) Problem Restatement**
- f(x) = x⁴ - 4x² + x
- Has two local minima (at approximately x ≈ -1.4 and x ≈ 1.4)
- Global minimum at x ≈ 1.38 (f ≈ -3.2)

**2) Initial State**
- x = 0 (starting point)
- f(0) = 0
- T = 10 (initial temperature)
- α = 0.9 (cooling rate)

**3-5) Algorithm Execution**

| Iter | T    | x     | f(x)   | x'    | f(x')  | Δ     | P=exp(-Δ/T) | Accept? |
|------|------|-------|--------|-------|--------|-------|-------------|---------|
| 1    | 10   | 0     | 0      | 0.5   | -0.69  | -0.69 | -           | Yes (improve) |
| 2    | 10   | 0.5   | -0.69  | -0.3  | 0.03   | +0.72 | 0.93        | Yes (P=0.93) |
| 3    | 10   | -0.3  | 0.03   | -0.8  | -1.56  | -1.59 | -           | Yes     |
| 4    | 10   | -0.8  | -1.56  | -1.2  | -2.72  | -1.16 | -           | Yes     |
| 5    | 10   | -1.2  | -2.72  | -0.7  | -1.31  | +1.41 | 0.87        | Yes (random) |
| ...  | ...  | ...   | ...    | ...   | ...    | ...   | ...         | ...     |
| (cool) | 9  | ...   | ...    | ...   | ...    | ...   | ...         | ...     |

**After many iterations with cooling:**

| Phase      | T    | Best x | Best f(x) | Notes                    |
|------------|------|--------|-----------|--------------------------|
| Hot (T≈10) | 10   | varies | varies    | Exploring widely         |
| Warm (T≈1) | 1    | ~1.3   | ~-3.1     | Starting to settle       |
| Cool (T≈0.1)| 0.1 | ~1.38  | ~-3.2     | Refining near optimum    |
| Cold (T≈0.01)| 0.01| 1.38  | -3.21     | Accepting only improvements |

**6) Final Result**
Best found: x ≈ **1.38**, f(x) ≈ **-3.21**

**Verification:**
- Local minimum near x = -1.4: f(-1.4) ≈ -2.8 (not global)
- Global minimum near x = 1.38: f(1.38) ≈ -3.21 ✓
- SA found global despite local optima ✓

### Final Answer
Global minimum: x ≈ **1.38**, f(x) ≈ **-3.21**

---

## TSP Example (Discrete)

**Problem:** Find shortest tour visiting all cities once.

**Neighbor generation:** Swap two cities in tour (or 2-opt: reverse a segment)

**State:** Current tour and its total distance

**Same SA framework** applies with discrete moves.

---

## Parameter Tuning Guidelines

| Parameter | Too Low | Too High | Typical |
|-----------|---------|----------|---------|
| T₀ | Stuck in local opt | Slow start | Accept 80-90% initially |
| α | Cool too fast | Very slow | 0.9 - 0.99 |
| T_min | Stop too early | Unnecessary iterations | 10⁻⁶ to 10⁻³ |
| Iterations/temp | Under-sampled | Slow | 100-1000 |

---

## Common Failure Modes

1. **Temperature too low initially** → never escapes local optima
2. **Cooling too fast** → same problem, insufficient exploration
3. **Poor neighbor generation** → can't reach good solutions
4. **Not tracking best solution** → final state might be worse
5. **Wrong acceptance probability** → must use exp(-Δ/T), not exp(Δ/T)
6. **Not running multiple times** → stochastic algorithm needs repetition
