# Gradient Descent Scaffold

## When to Use
- Minimizing differentiable functions
- Training machine learning models
- Finding optimal parameters
- Convex optimization
- Continuous optimization problems

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following optimization problem using Gradient Descent.

1) Problem Restatement
- Given: differentiable function f(x)
- Goal: find x* that minimizes f(x)
- Method: iteratively move in direction of steepest descent

2) State Definition
State = (current_x, learning_rate, iteration)

Where:
- current_x = current parameter values (can be vector)
- learning_rate (α) = step size
- gradient = ∇f(x) at current point

3) Update Rule
x_new = x_old - α × ∇f(x_old)

Key components:
- ∇f(x) = gradient (direction of steepest ascent)
- Negative gradient = direction of steepest descent
- α controls step size

4) Algorithm Procedure
a) Initialize: x = x₀ (starting point), α = learning_rate
b) For each iteration until convergence:
   - Compute gradient: g = ∇f(x)
   - Update: x = x - α × g
   - Check convergence: ||g|| < ε or |f(x_new) - f(x_old)| < ε
c) Return x

5) Convergence Criteria
- Gradient magnitude < threshold
- Change in function value < threshold
- Maximum iterations reached
- Parameters stopped changing

6) Verification Protocol
- Gradient at solution ≈ 0
- f(x*) < f(x₀)
- Second derivative test (if applicable)
- Compare with analytical solution (if known)
```

---

## Worked Example

### Problem
Minimize f(x) = x² - 4x + 5
Starting at x₀ = 0, learning rate α = 0.1

### Expected Scaffold Application

**1) Problem Restatement**
- f(x) = x² - 4x + 5
- Parabola opening upward, has unique minimum
- Analytical minimum: f'(x) = 2x - 4 = 0 → x* = 2

**2) State Definition**
- x = current position
- α = 0.1
- ∇f(x) = f'(x) = 2x - 4

**3-4) Algorithm Execution**

| Iter | x    | f(x)  | f'(x) = 2x-4 | x_new = x - 0.1×f'(x) |
|------|------|-------|--------------|------------------------|
| 0    | 0    | 5     | -4           | 0 - 0.1×(-4) = 0.4     |
| 1    | 0.4  | 3.76  | -3.2         | 0.4 + 0.32 = 0.72      |
| 2    | 0.72 | 2.92  | -2.56        | 0.72 + 0.256 = 0.976   |
| 3    | 0.976| 2.36  | -2.048       | 0.976 + 0.205 = 1.181  |
| 4    | 1.181| 2.03  | -1.638       | 1.181 + 0.164 = 1.345  |
| 5    | 1.345| 1.78  | -1.310       | 1.345 + 0.131 = 1.476  |
| ...  | ...  | ...   | ...          | ...                    |
| 10   | 1.82 | 1.03  | -0.36        | 1.86                   |
| 15   | 1.95 | 1.003 | -0.10        | 1.96                   |
| 20   | 1.99 | 1.0002| -0.02        | 1.99                   |

**Convergence:** As iterations increase, x → 2, f(x) → 1

**5) Convergence Check**
At iteration 20:
- |f'(x)| = 0.02 < 0.05 (threshold) ✓
- x ≈ 1.99 ≈ 2 ✓

**6) Verification**
- Analytical solution: x* = 2
- f(2) = 4 - 8 + 5 = 1 (minimum value)
- f''(2) = 2 > 0 (confirms minimum) ✓
- Our result: x ≈ 1.99, f(x) ≈ 1.0002 ✓

### Final Answer
Minimum at x ≈ **2**, f(x) = **1**

---

## Multivariate Example

**Problem:** Minimize f(x,y) = x² + y² (2D bowl)

Gradient: ∇f = [2x, 2y]

| Iter | (x, y)     | ∇f          | (x,y) - 0.1×∇f |
|------|------------|-------------|----------------|
| 0    | (3, 4)     | (6, 8)      | (2.4, 3.2)     |
| 1    | (2.4, 3.2) | (4.8, 6.4)  | (1.92, 2.56)   |
| ...  | ...        | ...         | → (0, 0)       |

Converges to minimum at origin.

---

## Learning Rate Selection

| α too small | α too large | α just right |
|-------------|-------------|--------------|
| Slow convergence | Oscillation/divergence | Fast convergence |
| Many iterations | May never converge | Stable |

**Adaptive methods:** Adam, RMSprop, AdaGrad adjust α automatically.

---

## Common Failure Modes

1. **Learning rate too large** → overshoots, diverges
2. **Learning rate too small** → extremely slow convergence
3. **Stuck in local minimum** → for non-convex functions
4. **Wrong gradient computation** → verify analytically or numerically
5. **Not normalizing features** → different scales cause issues
6. **Stopping too early** → check multiple convergence criteria
