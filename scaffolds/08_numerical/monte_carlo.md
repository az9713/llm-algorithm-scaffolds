# Monte Carlo Methods Scaffold

## When to Use
- Estimating integrals/areas
- Simulating random processes
- Problems with high dimensionality
- When analytical solution is intractable
- Probabilistic reasoning and inference
- Risk analysis and uncertainty quantification

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Monte Carlo Simulation.

1) Problem Restatement
- Given: quantity to estimate (integral, probability, expectation)
- Method: use random sampling to approximate
- Accuracy: improves with more samples (∝ 1/√n)

2) Sampling Strategy
Define how to generate random samples:
- Uniform sampling: equal probability across domain
- Importance sampling: bias toward important regions
- Stratified sampling: divide domain into strata

3) Estimator Definition
For estimating E[f(X)]:
- Generate n random samples: X₁, X₂, ..., Xₙ
- Estimate: Ê[f(X)] = (1/n) Σ f(Xᵢ)

For estimating integral ∫f(x)dx over [a,b]:
- Estimate: (b-a)/n × Σ f(Xᵢ) where Xᵢ ~ Uniform[a,b]

4) Algorithm Procedure
a) Define the quantity to estimate
b) Define sampling distribution
c) Generate n random samples
d) Compute f(sample) for each sample
e) Aggregate: mean, proportion, or sum
f) Compute confidence interval if needed

5) Error Analysis
Standard error: SE = σ / √n
95% CI: estimate ± 1.96 × SE

Error decreases as 1/√n (need 100x samples for 10x accuracy)

6) Verification Protocol
- Run multiple times, check consistency
- Compare with analytical result if known
- Increase n and verify convergence
- Check sampling is truly random
```

---

## Worked Example

### Problem
Estimate π using Monte Carlo simulation.

**Method:** Random points in unit square, count those inside quarter circle.

### Expected Scaffold Application

**1) Problem Restatement**
- Quarter circle of radius 1 in unit square
- Area of quarter circle = π/4
- Area of square = 1
- Ratio (points in circle / total points) ≈ π/4

**2) Sampling Strategy**
- Generate points (x, y) uniformly in [0,1] × [0,1]
- Point is inside quarter circle if x² + y² ≤ 1

**3) Estimator**
π̂ = 4 × (points inside circle) / (total points)

**4) Algorithm Execution (n = 1000)**

| Sample | x      | y      | x² + y² | Inside? |
|--------|--------|--------|---------|---------|
| 1      | 0.234  | 0.567  | 0.376   | Yes     |
| 2      | 0.891  | 0.445  | 0.991   | Yes     |
| 3      | 0.923  | 0.612  | 1.227   | No      |
| 4      | 0.156  | 0.789  | 0.647   | Yes     |
| ...    | ...    | ...    | ...     | ...     |
| 1000   | 0.432  | 0.321  | 0.289   | Yes     |

**Results (typical run):**
- Total points: 1000
- Points inside circle: 783
- π̂ = 4 × 783/1000 = **3.132**

**5) Error Analysis**
- True π = 3.14159...
- p = π/4 ≈ 0.785
- SE = √(p(1-p)/n) = √(0.785×0.215/1000) ≈ 0.013
- 95% CI for p: 0.783 ± 0.026
- 95% CI for π: 3.132 ± 0.104

**6) Verification**
| n     | π̂    | Error  |
|-------|------|--------|
| 100   | 3.08 | 0.062  |
| 1000  | 3.132| 0.010  |
| 10000 | 3.141| 0.001  |
| 100000| 3.1417| 0.0001|

Error decreases as 1/√n ✓

### Final Answer
π ≈ **3.14** (with n = 10000, error ≈ 0.01)

---

## Integration Example

Estimate ∫₀¹ x² dx (true value = 1/3)

**Method:**
1. Sample n points Xᵢ uniformly from [0, 1]
2. Compute f(Xᵢ) = Xᵢ² for each
3. Estimate = (1/n) Σ Xᵢ²

| n     | Estimate | True  | Error  |
|-------|----------|-------|--------|
| 100   | 0.312    | 0.333 | 0.021  |
| 1000  | 0.329    | 0.333 | 0.004  |
| 10000 | 0.3328   | 0.333 | 0.0005 |

---

## Importance Sampling

When sampling uniformly is inefficient (e.g., rare events):

Instead of sampling uniformly:
1. Sample from proposal distribution q(x) that emphasizes important regions
2. Reweight: estimate = (1/n) Σ [f(Xᵢ) × p(Xᵢ) / q(Xᵢ)]

This reduces variance when q(x) ∝ |f(x)| × p(x).

---

## Applications

| Application | What's Sampled | What's Estimated |
|-------------|---------------|------------------|
| π estimation | Random points | Area ratio |
| Integration | Domain points | Integral value |
| Risk analysis | Scenarios | VaR, expected loss |
| Physics | Particle paths | Physical quantities |
| Finance | Price paths | Option values |
| ML | Model parameters | Posterior distribution |

---

## Common Failure Modes

1. **Too few samples** → high variance, unreliable estimate
2. **Bad random number generator** → biased results
3. **Not using variance reduction** → inefficient for rare events
4. **Ignoring correlation** → incorrect confidence intervals
5. **Wrong estimator** → must match the quantity being estimated
6. **Seed not set** → results not reproducible
