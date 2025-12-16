# Generic Optimization Algorithm Scaffold Template

## Category Definition

**What makes Optimization Algorithms unique:**
- Search for best solution in a large/continuous space
- Iteratively improve current solution
- Balance exploration (finding new regions) vs exploitation (refining current best)

**When to use Optimization Algorithms:**
- Solution space too large for exhaustive search
- No closed-form solution exists
- Approximate solutions are acceptable
- Objective function may have multiple local optima

**Key distinguishing features:**
- Iterative refinement
- May not find global optimum (local search)
- Randomness often helps escape local optima
- Trade-off between solution quality and computation time

---

## Essential State Components

### [REQUIRED] - Must be in every optimization scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `current_solution` | Current candidate solution | `x = [1.5, -0.3, 2.1]` |
| `objective(x)` | Function to optimize | `f(x) = x² + 2x + 1` |
| `best_solution` | Best found so far | `best_x, best_value` |
| `termination_criteria` | When to stop | `iterations > 1000` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `gradient` | Gradient-based methods | `∇f(x) = [2x+2, ...]` |
| `temperature` | Simulated annealing | `T = 100 → 0.01` |
| `population` | Evolutionary methods | `[solution1, ..., solutionN]` |
| `step_size` | Learning rate/move size | `α = 0.01` |
| `neighborhood` | Local search | `N(x) = {x': ||x-x'|| < ε}` |
| `constraints` | Constrained optimization | `g(x) ≤ 0, h(x) = 0` |

### State Invariants
- best_solution always tracks the best seen so far
- Objective function evaluations are consistent
- Termination is guaranteed (bounded iterations or convergence)

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Objective: [MINIMIZE/MAXIMIZE] f(x) = [YOUR_OBJECTIVE_FUNCTION]
   - Variables: x = [YOUR_DECISION_VARIABLES]
   - Domain: x ∈ [YOUR_FEASIBLE_REGION]
   - Constraints: [YOUR_CONSTRAINTS]

2) State Definition
   State = (
       current: [CURRENT_SOLUTION],
       best: [BEST_SOLUTION_FOUND],
       [ALGORITHM_SPECIFIC_STATE]: ___
   )

3) Initialization
   current = [INITIAL_SOLUTION_METHOD]
   best = current
   [INITIALIZE_ALGORITHM_PARAMETERS]

4) Iteration Loop
   While not [TERMINATION_CONDITION]:

       a) Generate candidate(s):
          candidate = [CANDIDATE_GENERATION_METHOD]

       b) Evaluate:
          candidate_value = objective(candidate)

       c) Acceptance decision:
          If [ACCEPTANCE_CRITERION]:
              current = candidate

       d) Update best:
          If objective(current) [BETTER_THAN] objective(best):
              best = current

       e) Update parameters:
          [PARAMETER_UPDATE_RULE]

5) Termination Conditions
   - [MAX_ITERATIONS]: iterations > [LIMIT]
   - [CONVERGENCE]: |f(x_new) - f(x_old)| < [TOLERANCE]
   - [TIME_LIMIT]: elapsed_time > [BUDGET]

6) Output
   Return best solution and its objective value

7) Verification
   - Solution is feasible (satisfies constraints)
   - Objective value is correctly computed
   - Compare against known bounds if available
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Objective function is clearly defined
- [ ] Solution representation is appropriate
- [ ] Initialization produces feasible solutions
- [ ] Candidate generation explores relevant regions
- [ ] Acceptance criterion balances exploration/exploitation
- [ ] Termination is guaranteed
- [ ] Best solution tracking is correct

---

## Derivation Examples

### Example 1: Gradient Descent (from this template)

**Filled-in values:**
- Objective: **Minimize differentiable function f(x)**
- Candidate generation: **x - α∇f(x) (move opposite to gradient)**
- Acceptance: **Always accept (for basic version)**
- Termination: **||∇f(x)|| < ε or max iterations**

```
State = (x, learning_rate α, iteration)

Initialization:
    x = random or given starting point
    α = 0.01 (or adaptive)

Iteration:
    gradient = ∇f(x)
    x_new = x - α * gradient
    x = x_new

    (Optional) Adjust α based on progress

Termination:
    ||gradient|| < tolerance OR iterations > max

Output: x (local minimum)
```

---

### Example 2: Simulated Annealing (from this template)

**Filled-in values:**
- Objective: **Minimize (possibly non-convex) function**
- Candidate generation: **Random neighbor of current solution**
- Acceptance: **Always if better; probabilistically if worse (based on T)**
- Termination: **Temperature below threshold**

```
State = (current, best, temperature T)

Initialization:
    current = random solution
    best = current
    T = T_initial (high)

Iteration:
    neighbor = random_neighbor(current)
    Δ = f(neighbor) - f(current)

    If Δ < 0:  (neighbor is better)
        current = neighbor
    Else:
        Accept with probability exp(-Δ/T)
        If random() < exp(-Δ/T):
            current = neighbor

    If f(current) < f(best):
        best = current

    T = T * cooling_rate  (e.g., 0.995)

Termination:
    T < T_min OR iterations > max

Output: best
```

---

### Example 3: Genetic Algorithm (from this template)

**Filled-in values:**
- Objective: **Optimize fitness function**
- Candidate generation: **Selection + Crossover + Mutation**
- Acceptance: **Population replacement (generational or steady-state)**
- Termination: **Generations limit or convergence**

```
State = (population, generation, best_individual)

Initialization:
    population = [random_individual() for _ in range(pop_size)]
    Evaluate fitness of all individuals
    best = fittest individual

Iteration (one generation):
    new_population = []

    While len(new_population) < pop_size:
        parent1 = selection(population)  (e.g., tournament)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        new_population.append(child)

    Evaluate fitness of new_population
    population = new_population

    If fittest(population) better than best:
        best = fittest(population)

Termination:
    generation > max_generations OR
    no improvement for N generations

Output: best individual
```

---

## Algorithm Selection Guide

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Differentiable objective | Gradient Descent, Adam, L-BFGS |
| Many local optima | Simulated Annealing, Genetic Algorithm |
| Discrete/combinatorial | Genetic Algorithm, Tabu Search |
| Convex problem | Gradient Descent (converges to global) |
| Black-box function | Bayesian Optimization, Evolution Strategies |
| Constrained problem | Projected Gradient, Penalty Methods |

---

## Exploration vs Exploitation

| Aspect | Exploration | Exploitation |
|--------|-------------|--------------|
| Goal | Find new promising regions | Refine current best |
| Risk | May miss good local optima | May get stuck |
| Examples | High temperature (SA), mutation (GA) | Gradient descent, local search |

**Balance strategies:**
- **Temperature schedule** (SA): Start hot (explore), cool down (exploit)
- **Adaptive mutation** (GA): Decrease mutation rate over time
- **Restarts**: Periodically restart from random points
- **Multi-start**: Run multiple times from different initializations

---

## Creating Your Own Optimization Scaffold

1. **Define the objective function**
   - What exactly are you optimizing?
   - Is it differentiable? Continuous? Bounded?

2. **Choose solution representation**
   - Real-valued vector? Permutation? Binary string?
   - This affects which operators you can use

3. **Design candidate generation**
   - How do you propose new solutions?
   - Gradient-based? Random perturbation? Recombination?

4. **Specify acceptance criterion**
   - Always accept improvements?
   - Sometimes accept worse (for escaping local optima)?

5. **Set termination conditions**
   - Max iterations? Convergence threshold? Time limit?
   - Multiple criteria often combined

6. **Tune parameters**
   - Learning rate, temperature schedule, population size
   - These significantly affect performance

7. **Add constraint handling (if needed)**
   - Penalty functions? Repair operators? Feasibility checks?
