# Newton-Raphson Method Scaffold

## When to Use
- Finding roots of equations (f(x) = 0)
- Fast convergence when near root (quadratic)
- When derivative is available/computable
- Optimization (finding where f'(x) = 0)
- Computing square roots, cube roots, etc.

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following root-finding problem using Newton-Raphson Method.

1) Problem Restatement
- Given: function f(x) where we want f(x) = 0
- Also need: derivative f'(x)
- Goal: find x* such that f(x*) = 0

2) State Definition
State = (current_x, f(x), f'(x), iteration)

Required:
- f(x) = function value at current point
- f'(x) = derivative at current point
- Both must be computable

3) Update Rule
x_new = x_old - f(x_old) / f'(x_old)

Geometric interpretation:
- Draw tangent line at (x_old, f(x_old))
- Find where tangent crosses x-axis
- That's x_new

4) Algorithm Procedure
a) Choose initial guess x₀
b) For each iteration until convergence:
   - Compute f(x) and f'(x)
   - If |f'(x)| < ε: derivative too small, may fail
   - x_new = x - f(x) / f'(x)
   - If |x_new - x| < tolerance: converged
   - x = x_new
c) Return x

5) Convergence Criteria
- |f(x)| < ε (function close to zero)
- |x_new - x_old| < δ (x stopped changing)
- Maximum iterations reached

6) Verification Protocol
- f(x*) ≈ 0
- Compare with analytical solution if known
- Check convergence rate (should be quadratic near root)
```

---

## Worked Example

### Problem
Find √2 by solving x² - 2 = 0
Starting at x₀ = 1

### Expected Scaffold Application

**1) Problem Restatement**
- f(x) = x² - 2
- f'(x) = 2x
- Root is x = √2 ≈ 1.41421356...

**2) State Definition**
- f(x) = x² - 2
- f'(x) = 2x
- Initial: x₀ = 1

**3-4) Algorithm Execution**

| Iter | x        | f(x)      | f'(x) | x_new = x - f(x)/f'(x) |
|------|----------|-----------|-------|------------------------|
| 0    | 1        | -1        | 2     | 1 - (-1)/2 = 1.5       |
| 1    | 1.5      | 0.25      | 3     | 1.5 - 0.25/3 = 1.41667 |
| 2    | 1.41667  | 0.00694   | 2.833 | 1.41667 - 0.00245 = 1.41422 |
| 3    | 1.41422  | 0.00002   | 2.828 | 1.41421356...          |

**Convergence:**
- After iteration 3: x ≈ 1.41421356
- |f(x)| = |x² - 2| ≈ 0.0000001 < ε ✓

**5) Verification**
- True √2 = 1.41421356237...
- Our result: 1.41421356...
- Correct to 8 decimal places after just 3 iterations!

**Quadratic Convergence:**
| Iter | Error (x - √2) |
|------|----------------|
| 0    | 0.414          |
| 1    | 0.085          |
| 2    | 0.0025         |
| 3    | 0.000002       |

Error roughly squares each iteration (quadratic convergence).

### Final Answer
√2 ≈ **1.41421356**

---

## Example: Cube Root

Find ∛5 by solving x³ - 5 = 0

f(x) = x³ - 5, f'(x) = 3x²
x₀ = 2

| Iter | x     | x_new               |
|------|-------|---------------------|
| 0    | 2     | 2 - (8-5)/(12) = 1.75 |
| 1    | 1.75  | 1.75 - (5.36-5)/9.19 = 1.711 |
| 2    | 1.711 | ≈ 1.71 (converged)  |

∛5 ≈ 1.70997...

---

## When Newton-Raphson Fails

1. **f'(x) = 0:** Division by zero
2. **Bad initial guess:** May diverge or find wrong root
3. **Oscillation:** x bounces between two values
4. **Flat regions:** Slow or no convergence

**Solutions:**
- Use bisection first to get close
- Add damping: x_new = x - α × f(x)/f'(x) where 0 < α < 1
- Try different starting points

---

## Multidimensional Newton (for systems)

For F(x) = 0 where x and F are vectors:

x_new = x_old - J⁻¹ × F(x_old)

Where J is the Jacobian matrix of partial derivatives.

---

## Common Failure Modes

1. **Zero derivative** → division by zero, method fails
2. **Wrong derivative** → verify f'(x) is correct
3. **Poor initial guess** → may diverge or find wrong root
4. **Multiple roots** → may find any one, not specifically desired root
5. **Cycling** → oscillates without converging
6. **Overshoot** → step too large, flies past root
