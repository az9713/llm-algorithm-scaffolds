# Floyd-Warshall Algorithm Scaffold

## When to Use
- Finding shortest paths between **ALL pairs** of vertices
- Dense graphs where you need many shortest paths
- Detecting negative cycles
- Transitive closure of a graph
- When the graph is small enough (O(V³) complexity)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using the Floyd-Warshall Algorithm.

1) Problem Restatement
- Define the graph: V vertices, edges with weights
- Goal: compute shortest path distance between every pair (i, j)
- Secondary: detect negative cycles

2) State Definition
dist[i][j] = shortest known distance from vertex i to vertex j

Initialization:
- dist[i][i] = 0 for all i
- dist[i][j] = weight(i,j) if edge exists
- dist[i][j] = ∞ if no direct edge

3) Relaxation Semantics (through intermediate vertex k)
For all pairs (i, j):
- If dist[i][k] + dist[k][j] < dist[i][j]:
  - Update dist[i][j] = dist[i][k] + dist[k][j]

This asks: "Is going through k a shorter path from i to j?"

4) Algorithm Procedure
a) Initialize dist[][] matrix as above
b) For k = 1 to V (each vertex as intermediate):
   - For i = 1 to V:
     - For j = 1 to V:
       - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
c) Negative cycle detection:
   - If any dist[i][i] < 0: negative cycle exists

5) Termination Condition
- All k, i, j combinations processed
- dist[][] contains all-pairs shortest distances

6) Verification Protocol
- For sample pairs, trace path through intermediate vertices
- Verify dist[i][j] + dist[j][k] ≥ dist[i][k] (triangle inequality)
- Check diagonal: dist[i][i] = 0 (or negative if cycle)
```

---

## Worked Example

### Problem
Find all-pairs shortest paths:
```
    1       2
A -----> B -----> C
^        |        |
|        |3       |
|        v        |
+------- D <------+
    4         -1
```
Edges: A→B(1), B→C(2), B→D(3), C→D(-1), D→A(4)

### Expected Scaffold Application

**1) Problem Restatement**
- 4 vertices: A, B, C, D (indexed 0,1,2,3)
- 5 directed edges including one negative (C→D = -1)
- Find shortest distance between all pairs

**2) Initial Distance Matrix**
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | ∞ | ∞ |
| B | ∞ | 0 | 2 | 3 |
| C | ∞ | ∞ | 0 |-1 |
| D | 4 | ∞ | ∞ | 0 |

**3-4) Algorithm Execution**

**k = A (consider paths through A):**
- Check all (i,j): Can going through A improve any path?
- D→B via A: dist[D][A] + dist[A][B] = 4 + 1 = 5 < ∞ → update dist[D][B] = 5
- D→C via A: dist[D][A] + dist[A][C] = 4 + ∞ = ∞ → no update

Matrix after k=A:
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | ∞ | ∞ |
| B | ∞ | 0 | 2 | 3 |
| C | ∞ | ∞ | 0 |-1 |
| D | 4 | 5 | ∞ | 0 |

**k = B (consider paths through B):**
- A→C via B: 1 + 2 = 3 < ∞ → dist[A][C] = 3
- A→D via B: 1 + 3 = 4 < ∞ → dist[A][D] = 4
- D→C via B: 5 + 2 = 7 < ∞ → dist[D][C] = 7
- D→D via B: 5 + 3 = 8, not < 0 → no update

Matrix after k=B:
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 3 | 4 |
| B | ∞ | 0 | 2 | 3 |
| C | ∞ | ∞ | 0 |-1 |
| D | 4 | 5 | 7 | 0 |

**k = C (consider paths through C):**
- A→D via C: 3 + (-1) = 2 < 4 → dist[A][D] = 2
- B→D via C: 2 + (-1) = 1 < 3 → dist[B][D] = 1
- D→D via C: 7 + (-1) = 6, not < 0 → no update

Matrix after k=C:
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 3 | 2 |
| B | ∞ | 0 | 2 | 1 |
| C | ∞ | ∞ | 0 |-1 |
| D | 4 | 5 | 7 | 0 |

**k = D (consider paths through D):**
- B→A via D: 1 + 4 = 5 < ∞ → dist[B][A] = 5
- C→A via D: (-1) + 4 = 3 < ∞ → dist[C][A] = 3
- C→B via D: (-1) + 5 = 4 < ∞ → dist[C][B] = 4
- A→A via D: 2 + 4 = 6, not < 0 → no negative cycle through A

Matrix after k=D (Final):
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 3 | 2 |
| B | 5 | 0 | 2 | 1 |
| C | 3 | 4 | 0 |-1 |
| D | 4 | 5 | 7 | 0 |

**5) Negative Cycle Check**
All diagonal entries are 0 → No negative cycle.

**6) Verification**
- dist[A][D] = 2. Path: A→B→C→D. Weights: 1+2+(-1) = 2 ✓
- Triangle inequality: dist[A][B] + dist[B][D] = 1+1 = 2 = dist[A][D] ✓

### Final Answer
All-pairs shortest distance matrix computed. No negative cycles.

---

## Common Failure Modes

1. **Wrong loop order** → k must be outermost loop (intermediate vertex)
2. **Not initializing diagonal to 0** → self-distances wrong
3. **Forgetting ∞ + ∞ overflow** → handle infinity carefully
4. **Missing negative cycle check** → invalid results if cycle exists
5. **Using for sparse graphs** → inefficient, use Dijkstra/Bellman-Ford instead
6. **Not considering edge direction** → directed vs undirected matters
