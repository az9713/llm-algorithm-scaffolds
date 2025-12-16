# Depth-First Search (DFS) Scaffold

## When to Use
- Exploring all paths in a graph
- Cycle detection
- Topological sorting (on DAGs)
- Finding connected components
- Maze solving / pathfinding where any solution is acceptable
- Backtracking problems

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following problem using Depth-First Search.

1) Problem Restatement
- Define the graph: nodes and edges (directed or undirected)
- Identify: start node, goal condition (if any)
- Specify what you're searching for: path, cycle, connectivity, etc.

2) State Definition
State = (current_node, visited_set, path_so_far, any_additional_flags)

Required tracking:
- Current position in the graph
- Set of already-visited nodes (to avoid infinite loops)
- Current path/stack (for backtracking)
- Any problem-specific state (e.g., collected items, remaining resources)

3) Transition Semantics
For each unvisited neighbor of current_node:
- Precondition: neighbor not in visited_set (unless revisiting is allowed)
- Effect: move to neighbor, add to visited_set, push to path
- Backtrack: when no unvisited neighbors remain, pop from path

4) Algorithm Procedure
a) Initialize: visited = {start}, stack = [start]
b) While stack is not empty:
   - current = stack[-1] (peek top)
   - If current satisfies goal condition: return path/result
   - Find first unvisited neighbor
   - If found: push neighbor to stack, add to visited
   - If not found: pop from stack (backtrack)
c) If stack empty and goal not found: no solution exists

5) Termination Condition
- Goal found: return solution
- Stack empty: exhausted all possibilities

6) Verification Protocol
- Trace the path from start to end
- Verify each step uses valid edges
- Confirm no node visited twice (unless allowed)
- Check goal condition is satisfied
```

---

## Worked Example

### Problem
Find a path from node A to node F in this graph:
```
A -- B -- C
|    |    |
D -- E -- F
```
Edges: A-B, A-D, B-C, B-E, C-F, D-E, E-F

### Expected Scaffold Application

**1) Problem Restatement**
- Graph: 6 nodes (A,B,C,D,E,F), undirected edges as listed
- Start: A
- Goal: reach node F
- Task: find any valid path

**2) State Definition**
State = (current_node, visited_set, path)

**3) Transition Semantics**
From any node, can move to adjacent unvisited node.

**4) Algorithm Execution**

| Step | Stack      | Visited         | Action                    |
|------|------------|-----------------|---------------------------|
| 0    | [A]        | {A}             | Start at A                |
| 1    | [A,B]      | {A,B}           | A→B (first neighbor)      |
| 2    | [A,B,C]    | {A,B,C}         | B→C (first unvisited)     |
| 3    | [A,B,C,F]  | {A,B,C,F}       | C→F (goal found!)         |

**5) Result**
Path found: A → B → C → F (length 3)

**6) Verification**
- A-B: valid edge ✓
- B-C: valid edge ✓
- C-F: valid edge ✓
- F is goal ✓
- No repeated nodes ✓

### Final Answer
Path: A → B → C → F

---

## Common Failure Modes

1. **Forgetting to track visited nodes** → infinite loops in cyclic graphs
2. **Not backtracking properly** → missing solutions that require going back
3. **Confusing DFS with BFS** → DFS goes deep first, may not find shortest path
4. **Incorrect neighbor ordering** → different valid paths, but inconsistent results
5. **Not handling disconnected components** → missing nodes in some problems
