# Matrix Chain Multiplication Scaffold

## When to Use
- Optimal parenthesization of matrix products
- Minimizing computation cost for chained operations
- Optimal binary tree construction
- Polygon triangulation
- Optimal BST construction (similar structure)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following Matrix Chain Multiplication problem using Dynamic Programming.

1) Problem Restatement
- Given: sequence of matrices A₁, A₂, ..., Aₙ
- Matrix Aᵢ has dimensions p[i-1] × p[i]
- Multiplication is associative: can parenthesize any way
- Goal: find parenthesization minimizing total scalar multiplications
- Cost to multiply (a×b) × (b×c) matrix = a × b × c

2) State Definition
dp[i][j] = minimum cost to multiply matrices Aᵢ through Aⱼ

Dimensions:
- i, j = 1 to n (matrix indices)
- Only upper triangle needed (i ≤ j)

3) Recurrence Relation
dp[i][j] = min over k from i to j-1 of:
    dp[i][k] + dp[k+1][j] + p[i-1] × p[k] × p[j]

Where k is the split point: (Aᵢ...Aₖ)(Aₖ₊₁...Aⱼ)

Intuition: Try all split points, pick minimum total cost.

4) Base Cases
dp[i][i] = 0 for all i (single matrix, no multiplication)

5) Computation Order
By chain length: first all length-1, then length-2, etc.
Or equivalently: diagonals from main diagonal outward.

6) Solution Extraction
- Minimum cost: dp[1][n]
- Optimal parenthesization: track split point k for each (i,j)
  - Recursively build: ((Aᵢ...Aₖ)(Aₖ₊₁...Aⱼ))

7) Verification Protocol
- Check a few alternative parenthesizations have higher cost
- Verify cost calculation at each split
```

---

## Worked Example

### Problem
Multiply matrices A₁(10×30), A₂(30×5), A₃(5×60)

Dimension array: p = [10, 30, 5, 60]

### Expected Scaffold Application

**1) Problem Restatement**
- 3 matrices: A₁(10×30), A₂(30×5), A₃(5×60)
- Find optimal parenthesization
- p = [10, 30, 5, 60]

**2) State Definition**
dp[i][j] for i,j ∈ {1, 2, 3}

**3-4) Build DP Table**

**Base cases (length 1):**
dp[1][1] = dp[2][2] = dp[3][3] = 0

**Length 2 chains:**

dp[1][2]: multiply A₁ × A₂
- Only one way: k=1
- Cost = dp[1][1] + dp[2][2] + p[0]×p[1]×p[2]
- Cost = 0 + 0 + 10×30×5 = **1500**
- Result: (10×30)×(30×5) = (10×5)

dp[2][3]: multiply A₂ × A₃
- Only one way: k=2
- Cost = dp[2][2] + dp[3][3] + p[1]×p[2]×p[3]
- Cost = 0 + 0 + 30×5×60 = **9000**
- Result: (30×5)×(5×60) = (30×60)

**Length 3 chain:**

dp[1][3]: multiply A₁ × A₂ × A₃
- k=1: (A₁)(A₂A₃) = dp[1][1] + dp[2][3] + p[0]×p[1]×p[3]
       = 0 + 9000 + 10×30×60 = 9000 + 18000 = **27000**
- k=2: (A₁A₂)(A₃) = dp[1][2] + dp[3][3] + p[0]×p[2]×p[3]
       = 1500 + 0 + 10×5×60 = 1500 + 3000 = **4500** ← minimum

**5) DP Table**

|       | j=1 | j=2  | j=3   |
|-------|-----|------|-------|
| i=1   | 0   | 1500 | 4500  |
| i=2   | -   | 0    | 9000  |
| i=3   | -   | -    | 0     |

**Minimum cost: dp[1][3] = 4500**

**6) Optimal Parenthesization**
- dp[1][3] achieved at k=2
- Split: (A₁A₂)(A₃)
- dp[1][2] at k=1: just A₁A₂
- Final: **((A₁A₂)A₃)**

**7) Verification**
Compare the two options:

Option 1: (A₁(A₂A₃))
- A₂A₃: 30×5×60 = 9000 ops, result: 30×60
- A₁×(result): 10×30×60 = 18000 ops
- Total: 27000

Option 2: ((A₁A₂)A₃)
- A₁A₂: 10×30×5 = 1500 ops, result: 10×5
- (result)×A₃: 10×5×60 = 3000 ops
- Total: 4500 ✓

### Final Answer
Minimum cost: **4500 scalar multiplications**
Optimal parenthesization: **((A₁A₂)A₃)**

---

## Larger Example Pattern

For n matrices, the DP table is n×n upper triangular.
- Fill by diagonal (chain length)
- O(n³) time complexity
- O(n²) space complexity

---

## Common Failure Modes

1. **Wrong dimension indexing** → matrix Aᵢ is p[i-1]×p[i]
2. **Including cost of single matrix** → dp[i][i] = 0, not a multiplication
3. **Wrong split range** → k goes from i to j-1 (not j)
4. **Forgetting the "glue" cost** → p[i-1]×p[k]×p[j] joins the two halves
5. **Wrong computation order** → must compute smaller chains first
6. **Confusing with actual matrix values** → we only need dimensions
