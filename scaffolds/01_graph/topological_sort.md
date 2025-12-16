# Topological Sort Scaffold

## When to Use
- Ordering tasks with dependencies (prerequisites)
- Build systems / compilation order
- Course scheduling with prerequisites
- Any DAG (Directed Acyclic Graph) linearization
- Detecting if a directed graph has cycles

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Topological Sort.

1) Problem Restatement
- Define the DAG: vertices (tasks/items), directed edges (dependencies)
- Edge A→B means "A must come before B"
- Goal: linear ordering where all dependencies are satisfied
- Precondition: Graph must be acyclic (DAG)

2) State Definition
For Kahn's Algorithm (BFS-based):
- in_degree[v] = number of incoming edges to v
- queue = vertices with in_degree = 0 (no dependencies)
- result = ordered list of vertices

For DFS-based:
- visited[v] = whether v has been processed
- stack = vertices in reverse finish order

3) Algorithm Semantics

Kahn's Algorithm:
- Remove a vertex with in_degree = 0
- Add it to result
- Decrease in_degree of all its neighbors
- Repeat until queue empty

DFS-based:
- Run DFS from each unvisited vertex
- Add vertex to front of result when DFS finishes
- Result is reverse of finish times

4) Algorithm Procedure (Kahn's)
a) Calculate in_degree for all vertices
b) Add all vertices with in_degree = 0 to queue
c) While queue not empty:
   - v = dequeue
   - Add v to result
   - For each neighbor u of v:
     - in_degree[u] -= 1
     - If in_degree[u] == 0: enqueue u
d) If result.length < V: cycle detected (not a DAG)
e) Otherwise: result is valid topological order

5) Termination Condition
- All vertices processed → valid ordering found
- Vertices remain but queue empty → cycle exists

6) Verification Protocol
- For each edge (u, v): verify u appears before v in result
- Confirm all vertices are included exactly once
- If cycle claimed: identify the cycle
```

---

## Worked Example

### Problem
Order these courses given prerequisites:
- CS101 (no prerequisites)
- CS102 requires CS101
- CS201 requires CS101
- CS202 requires CS102 and CS201
- MATH101 (no prerequisites)
- CS301 requires CS202 and MATH101

Graph edges (A→B means A before B):
CS101→CS102, CS101→CS201, CS102→CS202, CS201→CS202, MATH101→CS301, CS202→CS301

### Expected Scaffold Application

**1) Problem Restatement**
- 6 vertices: CS101, CS102, CS201, CS202, MATH101, CS301
- 6 directed edges representing prerequisites
- Goal: valid course ordering

**2) Initial State (Kahn's Algorithm)**
| Vertex  | in_degree | Outgoing edges           |
|---------|-----------|--------------------------|
| CS101   | 0         | CS102, CS201             |
| CS102   | 1         | CS202                    |
| CS201   | 1         | CS202                    |
| CS202   | 2         | CS301                    |
| MATH101 | 0         | CS301                    |
| CS301   | 2         | (none)                   |

Initial queue: [CS101, MATH101] (in_degree = 0)

**3-4) Algorithm Execution**

| Step | Dequeue  | Result so far              | Update in_degrees          | Queue after        |
|------|----------|----------------------------|----------------------------|--------------------|
| 1    | CS101    | [CS101]                    | CS102:0, CS201:0           | [MATH101,CS102,CS201] |
| 2    | MATH101  | [CS101, MATH101]           | CS301:1                    | [CS102, CS201]     |
| 3    | CS102    | [CS101, MATH101, CS102]    | CS202:1                    | [CS201]            |
| 4    | CS201    | [CS101, MATH101, CS102, CS201] | CS202:0               | [CS202]            |
| 5    | CS202    | [..., CS202]               | CS301:0                    | [CS301]            |
| 6    | CS301    | [..., CS301]               | (none)                     | []                 |

**5) Result**
Order: CS101 → MATH101 → CS102 → CS201 → CS202 → CS301

(Note: MATH101 can be taken any time before CS301. CS102 and CS201 can be swapped.)

**6) Verification**
Check all edges:
- CS101→CS102: CS101 before CS102 ✓
- CS101→CS201: CS101 before CS201 ✓
- CS102→CS202: CS102 before CS202 ✓
- CS201→CS202: CS201 before CS202 ✓
- MATH101→CS301: MATH101 before CS301 ✓
- CS202→CS301: CS202 before CS301 ✓

All 6 vertices included exactly once ✓

### Final Answer
Valid course order: CS101, MATH101, CS102, CS201, CS202, CS301

---

## Common Failure Modes

1. **Not detecting cycles** → algorithm hangs or gives partial result
2. **Reversing edge direction** → A→B means A before B, not after
3. **Forgetting multiple valid orderings exist** → any valid order is correct
4. **Not handling disconnected components** → must process all components
5. **Confusing in-degree with out-degree** → Kahn's uses in-degree
6. **DFS approach: wrong stack order** → add on finish, not on visit
