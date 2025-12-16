# Graph Coloring Scaffold

## When to Use
- Assigning resources without conflicts (scheduling, register allocation)
- Partitioning with adjacency constraints
- Map coloring problems
- Frequency assignment in wireless networks
- Compiler register allocation
- Any problem where adjacent items cannot share same label

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Backtracking for Graph Coloring.

1) Problem Restatement
- Given graph G = (V, E)
- Assign one of k colors to each vertex
- No two adjacent vertices (connected by edge) may have same color
- Find: valid k-coloring, or minimum k needed (chromatic number)

2) State Definition
State = (vertex_index, color_assignment)

Where:
- vertex_index = current vertex being colored (0 to |V|-1)
- color[v] = color assigned to vertex v (or unassigned)
- available[v] = colors not used by v's neighbors

3) Constraint Check Semantics
For assigning color c to vertex v:
- For each neighbor u of v:
  - If color[u] == c: INVALID
- If no neighbor has color c: VALID

4) Algorithm Procedure
a) Order vertices (heuristic: most constrained first)
b) Base case: if all vertices colored, solution found
c) For current vertex v:
   - Compute available colors (not used by colored neighbors)
   - For each available color c:
     - Assign color[v] = c
     - Recurse to next vertex
     - If success: return solution
     - Else: unassign color[v] (backtrack)
d) If no color works: backtrack (or increase k)

5) Termination Condition
- All vertices colored → valid coloring found
- No valid color for current vertex → backtrack
- All colorings tried → need more colors (or problem is infeasible)

6) Verification Protocol
- Every vertex has a color assigned
- For every edge (u,v): color[u] ≠ color[v]
- Number of colors used ≤ k
```

---

## Worked Example

### Problem
Color this graph with minimum colors:
```
    A --- B
    |  X  |
    C --- D
```
Edges: A-B, A-C, A-D, B-C, B-D, C-D (complete graph K4)

### Expected Scaffold Application

**1) Problem Restatement**
- 4 vertices: A, B, C, D
- 6 edges forming complete graph
- Every pair is connected → need 4 colors (chromatic number = 4)

**2) Initial State**
- color = {A: ?, B: ?, C: ?, D: ?}
- Available colors: {1, 2, 3, 4}

**3-4) Algorithm Execution**

**Try with 3 colors first (will fail):**
```
Vertex A: assign color 1
  color = {A: 1}

  Vertex B: neighbors={A:1} → available={2,3}
    Try color 2
    color = {A: 1, B: 2}

    Vertex C: neighbors={A:1, B:2} → available={3}
      Assign color 3
      color = {A: 1, B: 2, C: 3}

      Vertex D: neighbors={A:1, B:2, C:3} → available={}
      NO AVAILABLE COLOR → BACKTRACK

    Backtrack from C

    Vertex C: no more colors to try → BACKTRACK

  Vertex B: Try color 3
  color = {A: 1, B: 3}

    Vertex C: neighbors={A:1, B:3} → available={2}
      Assign color 2

      Vertex D: neighbors={A:1, B:3, C:2} → available={}
      NO AVAILABLE COLOR → BACKTRACK

... (all 3-color attempts fail)
```

**Try with 4 colors:**
```
Vertex A: assign color 1
  Vertex B: assign color 2
    Vertex C: assign color 3
      Vertex D: neighbors={A:1, B:2, C:3} → available={4}
        Assign color 4
        ALL VERTICES COLORED → SUCCESS
```

**5) Solution**
- A: color 1
- B: color 2
- C: color 3
- D: color 4

**6) Verification**
Check all edges:
- A-B: 1 ≠ 2 ✓
- A-C: 1 ≠ 3 ✓
- A-D: 1 ≠ 4 ✓
- B-C: 2 ≠ 3 ✓
- B-D: 2 ≠ 4 ✓
- C-D: 3 ≠ 4 ✓

All constraints satisfied with 4 colors.

### Final Answer
Minimum colors needed: 4
Coloring: A=1, B=2, C=3, D=4

---

## Simpler Example: Triangle

Graph: A-B-C-A (triangle)

With 2 colors: Impossible (try and fail)
With 3 colors: A=1, B=2, C=3

Chromatic number of triangle = 3

---

## Common Failure Modes

1. **Not checking all neighbors** → missing constraint violations
2. **Trying insufficient colors** → need to increment k and retry
3. **Poor vertex ordering** → much slower search; use degree heuristic
4. **Not using forward checking** → can prune earlier with constraint propagation
5. **Confusing edge direction** → undirected edges constrain both endpoints
6. **Stopping at first valid k** → may not be minimum if question asks for chromatic number
