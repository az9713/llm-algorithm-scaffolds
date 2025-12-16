# Dijkstra's Algorithm Scaffold

## When to Use
- Shortest path with **non-negative edge weights**
- When edges have different costs/distances
- Single-source shortest paths
- GPS navigation, network routing
- When BFS won't work (weighted edges)
- **NOT usable with negative edge weights** (use Bellman-Ford instead)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Dijkstra's Algorithm.

1) Problem Restatement
- Define the graph: vertices, edges with non-negative weights
- Identify source vertex
- Goal: find shortest distance from source to all vertices (or specific target)
- CRITICAL: Verify all edge weights are ≥ 0

2) State Definition
For each vertex v:
- dist[v] = shortest known distance from source to v
- visited[v] = whether v has been finalized
- parent[v] = predecessor in shortest path

Data structure:
- Priority queue (min-heap) ordered by distance

Initialization:
- dist[source] = 0
- dist[v] = ∞ for all v ≠ source
- All vertices unvisited

3) Relaxation Semantics
For edge (u, v) with weight w:
- If dist[u] + w < dist[v]:
  - Update dist[v] = dist[u] + w
  - Update parent[v] = u
  - Update v's position in priority queue

4) Algorithm Procedure
a) Initialize dist[], visited[], priority queue with source
b) While priority queue not empty:
   - u = extract vertex with minimum dist[]
   - If u already visited: skip
   - Mark u as visited
   - For each neighbor v of u:
     - If not visited and dist[u] + weight(u,v) < dist[v]:
       - Update dist[v]
       - Update parent[v]
       - Add/update v in priority queue
c) dist[] contains shortest distances to all reachable vertices

5) Termination Condition
- Target vertex extracted from queue → shortest path to target found
- Queue empty → all reachable vertices processed

6) Verification Protocol
- Trace path using parent[] from target to source
- Sum edge weights along path
- Verify sum equals dist[target]
- Confirm no negative edges existed
```

---

## Worked Example

### Problem
Find shortest path from A to all vertices:
```
        5
    A -----> B
    |        |
   2|        |1
    v        v
    C -----> D
        3
```
Edges: A→B(5), A→C(2), B→D(1), C→D(3)

### Expected Scaffold Application

**1) Problem Restatement**
- 4 vertices: A, B, C, D
- 4 directed edges with positive weights
- Source: A
- Find shortest paths to all vertices

**2) Initial State**
| Vertex | dist | visited | parent |
|--------|------|---------|--------|
| A      | 0    | false   | null   |
| B      | ∞    | false   | null   |
| C      | ∞    | false   | null   |
| D      | ∞    | false   | null   |

Priority queue: [(A, 0)]

**3-4) Algorithm Execution**

| Step | Extract | dist | Relax edges               | Queue after             |
|------|---------|------|---------------------------|-------------------------|
| 1    | A (d=0) | --   | B:0+5=5, C:0+2=2          | [(C,2), (B,5)]          |
| 2    | C (d=2) | --   | D:2+3=5                   | [(B,5), (D,5)]          |
| 3    | B (d=5) | --   | D:5+1=6, but 6>5, no update | [(D,5)]               |
| 4    | D (d=5) | --   | (no outgoing edges)       | []                      |

**5) Final Distances**
| Vertex | Shortest Distance | Path     |
|--------|-------------------|----------|
| A      | 0                 | A        |
| B      | 5                 | A → B    |
| C      | 2                 | A → C    |
| D      | 5                 | A → C → D |

**6) Verification**
Path to D: A → C → D
Weights: 2 + 3 = 5 ✓

Note: A → B → D = 5 + 1 = 6, which is longer than A → C → D = 5 ✓

### Final Answer
Shortest distances from A: {A:0, B:5, C:2, D:5}
Shortest path to D: A → C → D (distance 5)

---

## Common Failure Modes

1. **Using with negative edges** → produces wrong results, use Bellman-Ford
2. **Not using priority queue** → O(V²) instead of O(E log V)
3. **Revisiting already-finalized vertices** → inefficient
4. **Not updating priority queue on relaxation** → may find suboptimal paths
5. **Confusing with BFS** → Dijkstra is for weighted, BFS for unweighted
6. **Initializing all distances to 0** → must be ∞ except source
