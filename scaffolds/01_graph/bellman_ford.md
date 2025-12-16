# Bellman-Ford Algorithm Scaffold

## When to Use
- Shortest paths with **negative edge weights**
- Detecting negative cycles
- When Dijkstra cannot be used (negative edges)
- Single-source shortest paths in general weighted graphs
- Distributed routing protocols (distance vector)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using the Bellman-Ford Algorithm.

1) Problem Restatement
- Define the graph: V vertices, E edges with weights (can be negative)
- Identify source vertex s
- Goal: find shortest distance from s to all other vertices
- Secondary goal: detect if negative cycle exists

2) State Definition
For each vertex v:
- dist[v] = current shortest known distance from s to v
- pred[v] = predecessor vertex in shortest path

Initialization:
- dist[s] = 0
- dist[v] = ∞ for all v ≠ s
- pred[v] = null for all v

3) Relaxation Semantics
For edge (u, v) with weight w:
- If dist[u] + w < dist[v]:
  - Update dist[v] = dist[u] + w
  - Update pred[v] = u

4) Algorithm Procedure
a) Initialize dist[] and pred[] as above
b) Repeat (V - 1) times:
   - For each edge (u, v, w) in graph:
     - Relax edge: if dist[u] + w < dist[v], update dist[v] and pred[v]
c) Negative cycle detection (V-th iteration):
   - For each edge (u, v, w):
     - If dist[u] + w < dist[v]: NEGATIVE CYCLE EXISTS
d) If no negative cycle: dist[] contains shortest distances

5) Termination Condition
- After V-1 iterations: shortest paths found (if no negative cycle)
- V-th iteration finds improvement: negative cycle detected

6) Verification Protocol
- For each vertex v, trace path using pred[] back to s
- Sum edge weights along path
- Verify sum equals dist[v]
- Confirm no negative cycle (or report it)
```

---

## Worked Example

### Problem
Find shortest paths from vertex A in this graph:
```
A --2--> B --3--> C
|        ^        |
|        |        |
4       -5        1
|        |        |
v        |        v
D -------+------> E
    (D->B = -5, D->E = 2)
```
Edges: A→B(2), A→D(4), B→C(3), C→E(1), D→B(-5), D→E(2)

### Expected Scaffold Application

**1) Problem Restatement**
- 5 vertices: A, B, C, D, E
- 6 directed edges with weights (including negative D→B = -5)
- Source: A
- Find shortest paths to all vertices

**2) Initial State**
| Vertex | dist | pred |
|--------|------|------|
| A      | 0    | null |
| B      | ∞    | null |
| C      | ∞    | null |
| D      | ∞    | null |
| E      | ∞    | null |

**3-4) Algorithm Execution**

**Iteration 1:**
| Edge     | Check                | Update?                  |
|----------|----------------------|--------------------------|
| A→B(2)   | 0 + 2 < ∞?          | Yes: dist[B]=2, pred[B]=A |
| A→D(4)   | 0 + 4 < ∞?          | Yes: dist[D]=4, pred[D]=A |
| B→C(3)   | 2 + 3 < ∞?          | Yes: dist[C]=5, pred[C]=B |
| C→E(1)   | 5 + 1 < ∞?          | Yes: dist[E]=6, pred[E]=C |
| D→B(-5)  | 4 + (-5) < 2?       | Yes: dist[B]=-1, pred[B]=D |
| D→E(2)   | 4 + 2 < 6?          | No                       |

After iteration 1: dist = [A:0, B:-1, C:5, D:4, E:6]

**Iteration 2:**
| Edge     | Check                | Update?                  |
|----------|----------------------|--------------------------|
| A→B(2)   | 0 + 2 < -1?         | No                       |
| A→D(4)   | 0 + 4 < 4?          | No                       |
| B→C(3)   | -1 + 3 < 5?         | Yes: dist[C]=2, pred[C]=B |
| C→E(1)   | 2 + 1 < 6?          | Yes: dist[E]=3, pred[E]=C |
| D→B(-5)  | 4 + (-5) < -1?      | No                       |
| D→E(2)   | 4 + 2 < 3?          | No                       |

After iteration 2: dist = [A:0, B:-1, C:2, D:4, E:3]

**Iterations 3, 4:** No further changes.

**Negative Cycle Check (iteration 5):**
No edge can be relaxed → No negative cycle.

**5) Final Distances**
| Vertex | Shortest Distance | Path        |
|--------|-------------------|-------------|
| A      | 0                 | A           |
| B      | -1                | A → D → B   |
| C      | 2                 | A → D → B → C |
| D      | 4                 | A → D       |
| E      | 3                 | A → D → B → C → E |

**6) Verification**
Path to E: A → D → B → C → E
Weights: 4 + (-5) + 3 + 1 = 3 ✓

### Final Answer
Shortest distances from A: {A:0, B:-1, C:2, D:4, E:3}
No negative cycle detected.

---

## Common Failure Modes

1. **Only running V-2 iterations** → missing some shortest paths
2. **Forgetting negative cycle check** → returning invalid results
3. **Processing edges in wrong order matters less** → but be systematic
4. **Confusing with Dijkstra** → Dijkstra CANNOT handle negative edges
5. **Not initializing dist[source] = 0** → all distances remain ∞
6. **Stopping early if no changes** → valid optimization but must still check cycles
