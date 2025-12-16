# Genetic Algorithm Scaffold

## When to Use
- Global optimization without gradients
- Large, complex search spaces
- Multi-modal functions (many local optima)
- Combinatorial optimization
- When domain knowledge can inform encoding
- Parallelizable optimization

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following optimization problem using a Genetic Algorithm.

1) Problem Restatement
- Given: optimization problem with solution space
- Goal: find solution maximizing/minimizing objective
- Approach: evolve population of candidate solutions

2) Representation (Encoding)
Define how solutions are represented as "chromosomes":
- Binary string: [1,0,1,1,0,0,1,0]
- Real-valued vector: [0.5, 1.2, -0.3]
- Permutation: [3,1,4,2,5] for ordering problems
- Custom encoding for domain

3) Fitness Function
fitness(chromosome) = how good the solution is
- Higher fitness = better solution (for maximization)
- Directly related to objective function

4) Genetic Operators

Selection: Choose parents for reproduction
- Tournament: pick best of k random individuals
- Roulette wheel: probability ∝ fitness
- Rank-based: probability ∝ rank

Crossover: Combine two parents to create offspring
- One-point: split and swap tails
- Two-point: swap middle segment
- Uniform: randomly pick from each parent

Mutation: Random small changes
- Bit flip: flip random bit
- Gaussian: add noise to real values
- Swap: exchange two elements

5) Algorithm Procedure
a) Initialize population of N random chromosomes
b) Evaluate fitness of each individual
c) Repeat for G generations:
   - Selection: choose parents based on fitness
   - Crossover: create offspring (probability Pc)
   - Mutation: modify offspring (probability Pm)
   - Evaluate fitness of offspring
   - Replace population (generational or steady-state)
d) Return best individual found

6) Verification Protocol
- Track best fitness over generations
- Verify fitness improves (on average)
- Check diversity doesn't collapse too early
- Compare with known optimum if available
```

---

## Worked Example

### Problem
Maximize f(x) = x² for x ∈ [0, 31] using 5-bit binary encoding.

### Expected Scaffold Application

**1) Problem Restatement**
- Maximize x² where x is integer 0-31
- Maximum is at x = 31, f(31) = 961

**2) Representation**
5-bit binary encoding: x = 13 → [0,1,1,0,1]

**3) Fitness Function**
fitness([b₄,b₃,b₂,b₁,b₀]) = (16b₄ + 8b₃ + 4b₂ + 2b₁ + b₀)²

**4) Operators**
- Selection: Tournament (k=2)
- Crossover: One-point (Pc = 0.7)
- Mutation: Bit flip (Pm = 0.01 per bit)

**5) Algorithm Execution**

**Generation 0 (Initial Population, N=4):**
| Individual | Chromosome | x  | Fitness (x²) |
|------------|------------|-----|--------------|
| A          | 01100      | 12  | 144          |
| B          | 10011      | 19  | 361          |
| C          | 00101      | 5   | 25           |
| D          | 11000      | 24  | 576          |

Total fitness: 1106
Best: D (576)

**Selection (Tournament, k=2):**
- Tournament 1: A vs C → A (144 > 25)
- Tournament 2: B vs D → D (576 > 361)
- Parents: A and D

**Crossover (one-point at position 2):**
```
A: 01|100  D: 11|000
Offspring 1: 01|000 = 8, fitness = 64
Offspring 2: 11|100 = 28, fitness = 784 ← better than parents!
```

**Mutation (flip random bit, rare):**
Offspring 2: 11100 → 11101 = 29, fitness = 841

**Generation 1:**
| Individual | Chromosome | x  | Fitness |
|------------|------------|-----|---------|
| A'         | 01000      | 8   | 64      |
| B          | 10011      | 19  | 361     |
| C'         | 11101      | 29  | 841     |
| D          | 11000      | 24  | 576     |

Best: C' (841) - improved from 576!

**Continue for more generations...**

**Final Generation:**
| Individual | Chromosome | x  | Fitness |
|------------|------------|-----|---------|
| Best       | 11111      | 31  | 961     |

**6) Verification**
- Best fitness: 961 = 31²  ✓
- Global optimum found ✓
- Fitness improved each generation ✓

### Final Answer
Optimal: x = **31**, f(x) = **961**

---

## TSP Example (Permutation Encoding)

**Representation:** Tour [3,1,4,2,5] = visit cities in that order

**Crossover (Order Crossover - OX):**
```
Parent 1: [1,2,3,4,5]
Parent 2: [5,4,3,2,1]
Cut points: 1 and 3
Child: [_,2,3,_,_] → fill from P2: [5,2,3,4,1]
```

**Mutation (Swap):**
[3,1,4,2,5] → [3,2,4,1,5] (swap positions 2 and 4)

---

## Parameter Guidelines

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Population (N) | 50-200 | Larger for harder problems |
| Generations (G) | 100-1000 | Until convergence |
| Crossover (Pc) | 0.6-0.9 | Main exploration |
| Mutation (Pm) | 0.001-0.05 | Prevent stagnation |
| Tournament (k) | 2-5 | Higher = more pressure |

---

## Common Failure Modes

1. **Premature convergence** → population becomes identical, increase mutation
2. **No improvement** → selection pressure too low or encoding wrong
3. **Invalid offspring** → crossover must preserve validity (esp. permutations)
4. **Fitness scaling issues** → normalize or use rank-based selection
5. **Wrong encoding** → binary isn't always best, match to problem structure
6. **Too small population** → insufficient diversity
