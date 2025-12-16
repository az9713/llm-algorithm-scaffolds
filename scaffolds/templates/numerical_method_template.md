# Generic Numerical Method Scaffold Template

## Category Definition

**What makes Numerical Methods unique:**
- Solve mathematical problems through computation
- Approximate solutions where analytical solutions don't exist
- Iterative refinement toward desired accuracy

**When to use Numerical Methods:**
- Root finding (f(x) = 0)
- Numerical integration
- Solving differential equations
- Approximating values (π, √2, integrals)
- Statistical estimation

**Key distinguishing features:**
- Convergence analysis (does it approach the answer?)
- Error bounds and tolerance
- Stability considerations
- Trade-off between accuracy and computation

---

## Essential State Components

### [REQUIRED] - Must be in every numerical scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `current_estimate` | Current approximation | `x_n = 1.414` |
| `function` | Mathematical function being analyzed | `f(x) = x² - 2` |
| `tolerance` | Acceptable error | `ε = 1e-6` |
| `iteration` | Current iteration count | `n = 5` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `derivative` | Newton-type methods | `f'(x) = 2x` |
| `interval` | Bracketing methods | `[a, b] = [1, 2]` |
| `samples` | Monte Carlo methods | `N = 10000` |
| `step_size` | Numerical integration | `h = 0.01` |
| `previous_estimate` | Secant method | `x_{n-1} = 1.5` |

### State Invariants
- Error decreases (or is bounded) with iterations
- Function evaluations are consistent
- Numerical stability is maintained

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Find: [ROOT / INTEGRAL / SOLUTION / ESTIMATE]
   - Function: f(x) = [YOUR_FUNCTION]
   - Domain: x ∈ [YOUR_DOMAIN]
   - Accuracy: tolerance = [YOUR_TOLERANCE]

2) State Definition
   State = (
       estimate: [CURRENT_APPROXIMATION],
       iteration: [COUNT],
       [METHOD_SPECIFIC_STATE]: ___
   )

3) Initialization
   - Initial guess: x₀ = [STARTING_VALUE]
   - [INTERVAL / DERIVATIVE / SAMPLES]: ___
   - Verify: [PRECONDITIONS]

4) Iteration Formula
   x_{n+1} = [UPDATE_FORMULA]

   WHERE:
   - [TERM_1]: [MEANING]
   - [TERM_2]: [MEANING]

5) Convergence Check
   If [CONVERGENCE_CRITERION]:
       Return x_n as solution

   Criteria options:
   - |x_{n+1} - x_n| < tolerance
   - |f(x_n)| < tolerance
   - iteration > max_iterations

6) Error Analysis
   - Expected convergence rate: [LINEAR / QUADRATIC / ...]
   - Error bound: [ERROR_FORMULA]

7) Output
   Return (estimate, iterations, error_bound)

8) Verification
   - Plug solution back: f(solution) ≈ 0?
   - Compare with known solution if available
   - Check convergence behavior
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Function is properly defined and continuous (where needed)
- [ ] Initial guess is reasonable
- [ ] Convergence conditions are appropriate
- [ ] Iteration formula is correct
- [ ] Error analysis is understood
- [ ] Edge cases handled (division by zero, non-convergence)
- [ ] Maximum iterations prevent infinite loops

---

## Derivation Examples

### Example 1: Newton-Raphson (from this template)

**Filled-in values:**
- Update formula: **x_{n+1} = x_n - f(x_n)/f'(x_n)**
- Convergence: **|x_{n+1} - x_n| < tolerance**
- Rate: **Quadratic (errors square each iteration)**
- Precondition: **f'(x) ≠ 0 near root**

```
Problem: Find root of f(x) = x² - 2 (i.e., √2)
Derivative: f'(x) = 2x

Initialization:
    x = 1.0  (initial guess)
    tolerance = 1e-10

Iteration:
    While |f(x)| > tolerance:
        x_new = x - f(x)/f'(x)
              = x - (x² - 2)/(2x)
              = (x + 2/x) / 2
        x = x_new

Convergence: Quadratic
    Error at step n+1 ≈ (error at step n)²

Output: x ≈ 1.41421356237
```

---

### Example 2: Bisection Method (from this template)

**Filled-in values:**
- Update formula: **midpoint c = (a+b)/2, then narrow interval**
- Convergence: **(b - a) < tolerance**
- Rate: **Linear (error halves each iteration)**
- Precondition: **f(a) and f(b) have opposite signs**

```
Problem: Find root of f(x) in [a, b] where f(a)·f(b) < 0

Initialization:
    a, b = interval with sign change
    Verify: f(a) * f(b) < 0

Iteration:
    While (b - a) > tolerance:
        c = (a + b) / 2
        If f(c) == 0:
            Return c (exact root)
        If f(a) * f(c) < 0:
            b = c  (root in left half)
        Else:
            a = c  (root in right half)

Convergence: Linear
    After n iterations: error ≤ (b-a)/2^n

Output: (a + b) / 2
```

---

### Example 3: Monte Carlo Integration (from this template)

**Filled-in values:**
- Estimate: **Average of f(random samples) × domain size**
- Convergence: **Error ~ 1/√N (by CLT)**
- Rate: **O(1/√N) regardless of dimension**
- Precondition: **Ability to sample uniformly from domain**

```
Problem: Estimate ∫∫...∫ f(x) dx over domain D

Initialization:
    N = number of samples
    volume = measure of domain D

Iteration:
    sum = 0
    For i = 1 to N:
        x = random_point_in(D)
        sum += f(x)

    estimate = (volume / N) * sum

Error Analysis:
    Standard error ≈ σ / √N
    Where σ = std deviation of f over D

Output: (estimate, standard_error)

Verification:
    - Compare with analytical result if known
    - Check that increasing N reduces error ~ 1/√N
```

---

## Convergence Rate Comparison

| Rate | Meaning | Example |
|------|---------|---------|
| **Linear** | Error multiplied by constant c < 1 | Bisection, Fixed-point |
| **Superlinear** | c → 0 as n → ∞ | Secant method |
| **Quadratic** | Error squared each step | Newton-Raphson |
| **O(1/√N)** | Statistical convergence | Monte Carlo |

---

## Common Numerical Pitfalls

| Pitfall | Description | Mitigation |
|---------|-------------|------------|
| **Division by zero** | f'(x) = 0 in Newton | Check denominator, use hybrid |
| **Non-convergence** | Oscillation or divergence | Limit iterations, check conditions |
| **Loss of precision** | Subtracting similar numbers | Reformulate, use higher precision |
| **Slow convergence** | Poor initial guess | Better initialization, restart |

---

## Algorithm Selection Guide

| Problem Type | Recommended Method |
|--------------|-------------------|
| Root finding (smooth, good guess) | Newton-Raphson |
| Root finding (guaranteed convergence) | Bisection + Newton hybrid |
| Root finding (no derivative) | Secant, Brent's method |
| Integration (1D, smooth) | Simpson's, Gaussian quadrature |
| Integration (high dimension) | Monte Carlo |
| ODE solving | Runge-Kutta, Euler |

---

## Creating Your Own Numerical Scaffold

1. **Define the mathematical problem precisely**
   - What are you computing?
   - What inputs are needed?
   - What is the desired output format?

2. **Choose or derive the iteration formula**
   - How does each iteration improve the estimate?
   - What is the mathematical basis?

3. **Establish convergence criteria**
   - When is the answer "good enough"?
   - How do you measure error?

4. **Analyze convergence rate**
   - How fast does error decrease?
   - How many iterations are needed?

5. **Identify failure modes**
   - When might the method fail?
   - What safeguards are needed?

6. **Implement verification**
   - How can you check the answer?
   - What invariants should hold?

7. **Handle numerical stability**
   - Are there catastrophic cancellation risks?
   - Is the algorithm stable for all inputs?
