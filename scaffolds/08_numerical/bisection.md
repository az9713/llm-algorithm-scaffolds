# Bisection Method Scaffold

## When to Use
- Finding roots when f(a) and f(b) have opposite signs
- Guaranteed convergence (unlike Newton-Raphson)
- When derivative is unavailable or expensive
- Robust root bracketing
- Simple and reliable baseline method

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following root-finding problem using Bisection Method.

1) Problem Restatement
- Given: continuous function f(x)
- Given: interval [a, b] where f(a) × f(b) < 0 (opposite signs)
- Goal: find x* where f(x*) = 0

2) Prerequisite Check
Verify: f(a) × f(b) < 0
- If both positive or both negative: no guaranteed root in interval
- Intermediate Value Theorem: root must exist in [a, b]

3) State Definition
State = (a, b, midpoint, f_a, f_b, f_mid)

Invariant: root is always in [a, b]
Each iteration halves the interval.

4) Algorithm Procedure
a) Verify f(a) × f(b) < 0
b) While (b - a) > tolerance:
   - mid = (a + b) / 2
   - f_mid = f(mid)
   - If f_mid == 0: exact root found
   - If f(a) × f_mid < 0:
     - Root in [a, mid], so b = mid
   - Else:
     - Root in [mid, b], so a = mid
c) Return (a + b) / 2

5) Convergence Analysis
- Error halves each iteration
- After n iterations: error ≤ (b-a) / 2^n
- Linear convergence (slower than Newton-Raphson)
- But GUARANTEED to converge

6) Verification Protocol
- Final interval [a, b] has f(a) × f(b) < 0
- (b - a) < tolerance
- f(midpoint) ≈ 0
```

---

## Worked Example

### Problem
Find root of f(x) = x³ - x - 2 in [1, 2]
(Root is approximately 1.521)

### Expected Scaffold Application

**1) Problem Restatement**
- f(x) = x³ - x - 2
- Interval: [1, 2]
- Tolerance: 0.01

**2) Prerequisite Check**
- f(1) = 1 - 1 - 2 = -2 (negative)
- f(2) = 8 - 2 - 2 = 4 (positive)
- f(1) × f(2) = -8 < 0 ✓ Root exists in [1, 2]

**3-4) Algorithm Execution**

| Iter | a    | b    | mid  | f(a)   | f(b)  | f(mid) | New interval |
|------|------|------|------|--------|-------|--------|--------------|
| 0    | 1    | 2    | 1.5  | -2     | 4     | -0.125 | [1.5, 2]     |
| 1    | 1.5  | 2    | 1.75 | -0.125 | 4     | 3.11   | [1.5, 1.75]  |
| 2    | 1.5  | 1.75 | 1.625| -0.125 | 3.11  | 1.29   | [1.5, 1.625] |
| 3    | 1.5  | 1.625| 1.5625| -0.125| 1.29  | 0.53   | [1.5, 1.5625]|
| 4    | 1.5  | 1.5625| 1.5312| -0.125| 0.53 | 0.19   | [1.5, 1.5312]|
| 5    | 1.5  | 1.5312| 1.5156| -0.125| 0.19 | 0.03   | [1.5, 1.5156]|
| 6    | 1.5  | 1.5156| 1.5078| -0.125| 0.03 | -0.05  | [1.5078, 1.5156]|
| 7    | 1.5078| 1.5156| 1.5117| -0.05| 0.03 | -0.01  | [1.5117, 1.5156]|

**Interval width:** 1.5156 - 1.5117 = 0.0039 < 0.01 ✓

**5) Result**
Root ≈ (1.5117 + 1.5156) / 2 = **1.5137**

Actual root: x ≈ 1.5214

**6) Verification**
- f(1.5137) = (1.5137)³ - 1.5137 - 2 ≈ -0.015 ≈ 0 ✓
- Interval width < tolerance ✓

### Final Answer
Root of x³ - x - 2: x ≈ **1.52** (within tolerance 0.01)

---

## Iterations Needed

To achieve tolerance ε starting from interval [a, b]:

n = ⌈log₂((b-a)/ε)⌉

Example: [1, 2] with ε = 0.001
n = ⌈log₂(1/0.001)⌉ = ⌈log₂(1000)⌉ = ⌈9.97⌉ = 10 iterations

---

## Comparison: Bisection vs Newton-Raphson

| Aspect | Bisection | Newton-Raphson |
|--------|-----------|----------------|
| Convergence | Linear (slow) | Quadratic (fast) |
| Guarantee | Always converges | May diverge |
| Requirements | f(a)×f(b)<0 | Need f'(x) |
| Per iteration | 1 function eval | f and f' evals |
| Robustness | Very robust | Sensitive |

**Best practice:** Use bisection to get close, then Newton-Raphson to refine.

---

## Multiple Roots

If interval contains multiple roots:
- Bisection finds ONE of them
- No guarantee which one
- To find all: subdivide interval and check each

---

## Common Failure Modes

1. **Same sign at endpoints** → no guaranteed root, must bracket
2. **Discontinuous function** → may find discontinuity, not root
3. **Multiple roots in interval** → finds only one
4. **Tolerance too tight** → floating point limits may prevent convergence
5. **f(mid) ≈ 0 but not exact** → need tolerance check, not exact zero
6. **Integer overflow in midpoint** → use mid = a + (b-a)/2 not (a+b)/2
