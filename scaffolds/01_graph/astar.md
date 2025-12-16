# A* Search Scaffold

## When to Use
- Finding shortest/optimal path with heuristic guidance
- When you have domain knowledge to estimate remaining cost
- Pathfinding in games, maps, navigation
- When Dijkstra is too slow and you can estimate distance to goal
- Problems where admissible heuristics exist

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using A* Search.

1) Problem Restatement
- Define the graph: nodes, edges, edge costs
- Identify: start node, goal node
- Define the heuristic function h(n) = estimated cost from n to goal
- CRITICAL: Verify h(n) is admissible (never overestimates true cost)

2) State Definition
For each node n, track:
- g(n) = actual cost from start to n
- h(n) = heuristic estimate from n to goal
- f(n) = g(n) + h(n) = estimated total cost through n
- parent(n) = previous node in best path

Data structures:
- Open set (priority queue): nodes to explore, ordered by f(n)
- Closed set: nodes already fully explored

3) Transition Semantics
For each neighbor m of current node n:
- tentative_g = g(n) + cost(n, m)
- If m not seen OR tentative_g < g(m):
  - Update g(m) = tentative_g
  - Update f(m) = g(m) + h(m)
  - Set parent(m) = n
  - Add m to open set (or update priority)

4) Algorithm Procedure
a) Initialize:
   - g(start) = 0, f(start) = h(start)
   - open_set = {start}, closed_set = {}
b) While open_set is not empty:
   - current = node in open_set with lowest f(n)
   - If current == goal: reconstruct and return path
   - Move current from open_set to closed_set
   - For each neighbor of current:
     - If neighbor in closed_set: skip
     - Calculate tentative_g
     - If better path found: update and add to open_set
c) If open_set empty: no path exists

5) Termination Condition
- Goal node popped from open_set → optimal path found
- Open set empty → no path exists

6) Verification Protocol
- Confirm h(n) ≤ actual_cost(n, goal) for all n (admissibility)
- Trace path and sum edge costs
- Verify g(goal) equals path cost
- Check no better path was missed
```

---

## Worked Example

### Problem
Find shortest path from S to G on a grid:
```
S . . .
. # # .
. . . G
```
S=(0,0), G=(2,3). '#' = obstacle.
Movement: 4-directional, cost = 1 per step.
Heuristic: Manhattan distance h(n) = |nx - gx| + |ny - gy|

### Expected Scaffold Application

**1) Problem Restatement**
- Grid 3x4, obstacles at (1,1), (1,2)
- Start: (0,0), Goal: (2,3)
- h(n) = Manhattan distance to (2,3)
- Admissibility: Manhattan distance never overestimates on 4-directional grid ✓

**2) State Definition**
For each cell (r,c): track g, h, f, parent

Initial values:
- g(0,0) = 0
- h(0,0) = |0-2| + |0-3| = 5
- f(0,0) = 0 + 5 = 5

**3-4) Algorithm Execution**

| Step | Current | f   | Open Set (by f)           | Action                |
|------|---------|-----|---------------------------|-----------------------|
| 1    | (0,0)   | 5   | {(0,1):6, (1,0):6}        | Expand start          |
| 2    | (0,1)   | 6   | {(1,0):6, (0,2):6}        | Both have f=6         |
| 3    | (1,0)   | 6   | {(0,2):6, (2,0):6}        | Expand (1,0)          |
| 4    | (0,2)   | 6   | {(2,0):6, (0,3):6}        | Continue              |
| 5    | (2,0)   | 6   | {(0,3):6, (2,1):6}        | Moving down           |
| ...  | ...     | ... | ...                       | Continue expanding    |
| N    | (2,3)   | 5   | --                        | Goal reached!         |

**5) Optimal Path Found**
Path: (0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3)
Total cost: 5 steps

**6) Verification**
- Each step is valid (adjacent, no obstacle) ✓
- Total cost = 5 ✓
- h(n) ≤ true distance for all expanded nodes ✓
- This is optimal (matches h(start) lower bound) ✓

### Final Answer
Optimal path: S → (0,1) → (0,2) → (0,3) → (1,3) → G
Cost: 5

---

## Common Failure Modes

1. **Non-admissible heuristic** → may find suboptimal path
2. **Forgetting to check closed set** → infinite loops or inefficiency
3. **Not updating when better path found** → suboptimal results
4. **Incorrect priority queue ordering** → expanding wrong nodes first
5. **Heuristic inconsistency** → may need to re-expand closed nodes
6. **Confusing g and f values** → g is actual cost, f is estimate
