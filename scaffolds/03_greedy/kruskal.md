# Kruskal's Algorithm (MST) Scaffold

## When to Use
- Finding Minimum Spanning Tree (MST)
- Connecting all nodes with minimum total edge weight
- Network design (minimum cable to connect all buildings)
- Clustering (MST then remove expensive edges)
- When you have edge list representation

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Kruskal's Algorithm.

1) Problem Restatement
- Given: connected, weighted, undirected graph G = (V, E)
- Goal: find spanning tree with minimum total edge weight
- Spanning tree: connects all V vertices with exactly V-1 edges, no cycles

2) State Definition
State = (sorted_edges, selected_edges, disjoint_set_forest)

Where:
- edges sorted by weight (ascending)
- selected_edges = edges included in MST
- disjoint_set (Union-Find): tracks connected components

Union-Find operations:
- FIND(x): return root/representative of x's component
- UNION(x, y): merge components containing x and y

3) Greedy Choice Property
Always select the minimum-weight edge that doesn't create a cycle.

Cycle detection:
- Edge (u, v) creates cycle iff FIND(u) == FIND(v)
- If u and v already in same component, adding edge makes cycle

4) Algorithm Procedure
a) Sort all edges by weight: w[1] ≤ w[2] ≤ ... ≤ w[m]
b) Initialize Union-Find with each vertex in its own set
c) selected = []
d) For each edge (u, v, w) in sorted order:
   - If FIND(u) ≠ FIND(v):  (different components)
     - Add edge to selected
     - UNION(u, v)
   - If |selected| == V - 1: done (MST complete)
e) Return selected edges

5) Termination Condition
- V - 1 edges selected → MST complete
- All edges processed but fewer than V-1 selected → graph not connected

6) Verification Protocol
- Exactly V - 1 edges selected
- All vertices connected (one component)
- No cycles exist
- Total weight is minimum (compare with alternatives)
```

---

## Worked Example

### Problem
Find MST for this graph:
```
    A ---4--- B
    |        /|\
    1      2  |  5
    |    /    |    \
    C --3-- D --6-- E
```
Edges: A-B(4), A-C(1), B-C(2), B-D(5), C-D(3), D-E(6)

### Expected Scaffold Application

**1) Problem Restatement**
- 5 vertices: A, B, C, D, E
- 6 edges with weights
- Find spanning tree with minimum total weight

**2) Initial State**
Sorted edges by weight:
| Edge | Weight |
|------|--------|
| A-C  | 1      |
| B-C  | 2      |
| C-D  | 3      |
| A-B  | 4      |
| B-D  | 5      |
| D-E  | 6      |

Union-Find: {A}, {B}, {C}, {D}, {E} (5 separate components)

**3-4) Algorithm Execution**

| Step | Edge | Weight | FIND check      | Action                  | Components          |
|------|------|--------|-----------------|-------------------------|---------------------|
| 1    | A-C  | 1      | A≠C             | SELECT, UNION(A,C)      | {A,C}, {B}, {D}, {E} |
| 2    | B-C  | 2      | B≠C (in {A,C})  | SELECT, UNION(B,{A,C})  | {A,B,C}, {D}, {E}   |
| 3    | C-D  | 3      | C≠D             | SELECT, UNION           | {A,B,C,D}, {E}      |
| 4    | A-B  | 4      | A=B (same set)  | SKIP (would create cycle) | {A,B,C,D}, {E}    |
| 5    | B-D  | 5      | B=D (same set)  | SKIP (would create cycle) | {A,B,C,D}, {E}    |
| 6    | D-E  | 6      | D≠E             | SELECT, UNION           | {A,B,C,D,E}         |

**5) MST Edges Selected**
1. A-C (weight 1)
2. B-C (weight 2)
3. C-D (weight 3)
4. D-E (weight 6)

Total weight: 1 + 2 + 3 + 6 = **12**

**MST Structure:**
```
    A       B
     \     /
    1 \   / 2
       \ /
        C
        |
        | 3
        |
        D
        |
        | 6
        |
        E
```

**6) Verification**
- 4 edges selected = V - 1 = 5 - 1 ✓
- All 5 vertices connected ✓
- No cycles (tree structure) ✓
- Total weight = 12

Alternative check: Could we do better?
- Must include D-E(6) to connect E (only edge to E)
- Must connect {A,B,C} to D: best is C-D(3)
- Within {A,B,C}: need 2 edges from {A-B(4), A-C(1), B-C(2)}
- Best pair: A-C(1) + B-C(2) = 3
- Total minimum = 6 + 3 + 3 = 12 ✓

### Final Answer
MST edges: A-C, B-C, C-D, D-E
Total weight: 12

---

## Prim's Algorithm Alternative

Prim's also finds MST but grows from a single vertex:
- Start at any vertex
- Always add minimum edge connecting tree to non-tree vertex
- Better for dense graphs (adjacency matrix)
- Kruskal's better for sparse graphs (edge list)

---

## Common Failure Modes

1. **Not sorting edges first** → may select non-minimum edge
2. **Wrong cycle detection** → must use proper Union-Find
3. **Stopping too early** → need exactly V-1 edges
4. **Including both (u,v) and (v,u)** → undirected means one edge object
5. **Inefficient Union-Find** → use union by rank + path compression
6. **Forgetting graph might not be connected** → MST only exists for connected graphs
