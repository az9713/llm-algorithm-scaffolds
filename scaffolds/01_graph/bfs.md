# Breadth-First Search (BFS) Scaffold

## When to Use
- Finding **shortest path** in unweighted graphs
- Level-order traversal
- Finding all nodes within k steps
- Testing bipartiteness
- Minimum number of moves/operations problems
- When you need the FIRST solution found to be optimal

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Breadth-First Search.

1) Problem Restatement
- Define the graph: nodes and edges (directed or undirected)
- Identify: start node, goal condition
- Confirm all edges have equal cost (or cost = 1)
- Goal: find shortest path or minimum steps

2) State Definition
State = (current_node, distance_from_start)

Data structures:
- queue = FIFO queue of nodes to explore
- visited = set of already-seen nodes
- distance[v] = shortest distance from start to v
- parent[v] = predecessor for path reconstruction

3) Transition Semantics
For each neighbor of current node:
- If not visited:
  - Mark as visited
  - Set distance = current_distance + 1
  - Set parent = current_node
  - Add to queue

4) Algorithm Procedure
a) Initialize:
   - visited = {start}
   - distance[start] = 0
   - queue = [start]
b) While queue not empty:
   - current = dequeue (front of queue)
   - If current satisfies goal: reconstruct and return path
   - For each neighbor of current:
     - If neighbor not in visited:
       - visited.add(neighbor)
       - distance[neighbor] = distance[current] + 1
       - parent[neighbor] = current
       - enqueue(neighbor)
c) If queue empty and goal not found: no path exists

5) Termination Condition
- Goal node dequeued → shortest path found
- Queue empty → no path exists

6) Verification Protocol
- Path length equals distance[goal]
- Each step uses a valid edge
- No shorter path exists (BFS guarantee)
```

---

## Worked Example

### Problem
Find shortest path from S to T in this graph:
```
S --- A --- B
|     |     |
C --- D --- T
```
Edges: S-A, S-C, A-B, A-D, C-D, B-T, D-T

### Expected Scaffold Application

**1) Problem Restatement**
- 6 nodes: S, A, B, C, D, T
- 7 undirected edges (equal weight = 1)
- Start: S, Goal: T
- Find minimum number of edges to traverse

**2) Initial State**
- visited = {S}
- distance = {S: 0}
- queue = [S]

**3-4) Algorithm Execution**

| Step | Dequeue | Distance | Explore neighbors        | Queue after          |
|------|---------|----------|--------------------------|----------------------|
| 1    | S       | 0        | A(new, d=1), C(new, d=1) | [A, C]               |
| 2    | A       | 1        | B(new, d=2), D(new, d=2) | [C, B, D]            |
| 3    | C       | 1        | D(seen)                  | [B, D]               |
| 4    | B       | 2        | T(new, d=3)              | [D, T]               |
| 5    | D       | 2        | T(seen)                  | [T]                  |
| 6    | T       | 3        | GOAL REACHED             | --                   |

**5) Path Reconstruction**
- T: parent = B
- B: parent = A
- A: parent = S
Path: S → A → B → T (distance = 3)

**6) Verification**
- S-A: valid edge ✓
- A-B: valid edge ✓
- B-T: valid edge ✓
- Total: 3 edges = distance[T] ✓
- BFS guarantees this is shortest ✓

### Final Answer
Shortest path: S → A → B → T
Distance: 3 edges

---

## Alternative Path Note
There's also: S → A → D → T (also 3 edges)
Both are valid shortest paths. BFS finds one of them (depending on neighbor ordering).

---

## Common Failure Modes

1. **Using stack instead of queue** → becomes DFS, loses shortest-path guarantee
2. **Marking visited on dequeue instead of enqueue** → explores same node multiple times
3. **Applying to weighted graphs** → use Dijkstra instead
4. **Not tracking distance/parent** → can't reconstruct path
5. **Forgetting the goal could be the start** → check before starting loop
6. **Processing edges in different orders** → different valid paths, same length
