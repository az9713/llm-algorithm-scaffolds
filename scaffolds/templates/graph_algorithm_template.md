# Generic Graph Algorithm Scaffold Template

## Category Definition

**What makes Graph Algorithms unique:**
- Operate on nodes (vertices) connected by edges
- Explore relationships and paths between entities
- Often involve traversal, shortest paths, or connectivity

**When to use a Graph Algorithm:**
- Finding paths between points
- Exploring reachability or connectivity
- Optimizing routes or networks
- Detecting cycles or ordering dependencies

**Key distinguishing features:**
- Graph representation (adjacency list/matrix)
- Directed vs undirected edges
- Weighted vs unweighted edges
- Single-source vs all-pairs problems

---

## Essential State Components

### [REQUIRED] - Must be in every graph scaffold

| Component | Description | Example |
|-----------|-------------|---------|
| `current_node` | Node being processed | `current = A` |
| `visited` | Nodes already processed | `{A, B, C}` |
| `data_structure` | Queue/Stack/Heap for traversal order | `queue = [D, E]` |
| `graph` | The graph structure itself | `edges: A→B, A→C` |

### [OPTIONAL] - Depending on specific algorithm

| Component | When Needed | Example |
|-----------|-------------|---------|
| `distance[]` | Shortest path algorithms | `dist[B] = 5` |
| `parent[]` | Path reconstruction | `parent[B] = A` |
| `weight(u,v)` | Weighted graphs | `weight(A,B) = 3` |
| `priority` | Priority-based exploration | `f(n) = g(n) + h(n)` |
| `component_id` | Connectivity problems | `comp[A] = 1` |

### State Invariants
- Once a node is marked visited, it stays visited
- Data structure ordering determines exploration order
- Distance/cost values only decrease (for minimization)

---

## Core Pattern (Fill-in-the-Blank)

```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Graph type: [DIRECTED/UNDIRECTED]
   - Edge weights: [WEIGHTED/UNWEIGHTED/NEGATIVE_ALLOWED]
   - Start node: [YOUR_SOURCE]
   - Goal: [FIND_PATH / SHORTEST_PATH / ALL_REACHABLE / DETECT_CYCLE / ...]

2) State Definition
   State = (
       current_node,
       [YOUR_DATA_STRUCTURE]: [QUEUE/STACK/PRIORITY_QUEUE],
       visited: set,
       [ADDITIONAL_STATE]: ___
   )

3) Initialization
   - visited = {[SOURCE]}
   - [DATA_STRUCTURE] = [[SOURCE]]
   - [DISTANCE/COST] = [INITIAL_VALUES]

4) Main Loop
   While [DATA_STRUCTURE] not empty:
       - current = [EXTRACT_OPERATION] from [DATA_STRUCTURE]
       - If [TERMINATION_CHECK]: return result
       - For each neighbor of current:
           - If [NEIGHBOR_CONDITION]:
               - [UPDATE_OPERATION]
               - Add to [DATA_STRUCTURE]

5) Termination Condition
   - [GOAL_REACHED]: ___
   - [EXHAUSTED]: ___

6) Verification
   - [PATH_VALID]: each step uses valid edge
   - [COST_CORRECT]: sum of edges equals reported cost
   - [OPTIMALITY]: no better solution exists (if claiming optimal)
```

---

## Derivation Checklist

Before using your scaffold, verify:

- [ ] Graph representation is clear (nodes, edges, weights)
- [ ] Traversal order is specified (BFS=queue, DFS=stack, Dijkstra=min-heap)
- [ ] Visited tracking prevents infinite loops
- [ ] Termination condition is unambiguous
- [ ] Edge cases handled (disconnected graph, self-loops)
- [ ] Path reconstruction method defined (if needed)
- [ ] Verification step validates the result

---

## Derivation Examples

### Example 1: BFS (from this template)

**Filled-in values:**
- Data structure: **Queue (FIFO)**
- Extract operation: **Dequeue front**
- Neighbor condition: **Not in visited**
- Update operation: **Mark visited, record distance**
- Termination: **Goal node dequeued**

**Key insight:** Queue ensures shortest path (by edge count) in unweighted graphs.

---

### Example 2: Dijkstra (from this template)

**Filled-in values:**
- Data structure: **Priority Queue (min-heap by distance)**
- Extract operation: **Extract minimum distance node**
- Neighbor condition: **New path is shorter**
- Update operation: **Update distance, add to heap**
- Termination: **Target extracted from heap**

**Key insight:** Priority queue ensures nodes are finalized in order of distance.

---

### Example 3: DFS (from this template)

**Filled-in values:**
- Data structure: **Stack (LIFO)**
- Extract operation: **Pop top**
- Neighbor condition: **Not in visited**
- Update operation: **Mark visited, push neighbors**
- Termination: **Stack empty or goal found**

**Key insight:** Stack causes deep exploration before backtracking.

---

## Creating Your Own Graph Scaffold

1. **Identify the traversal order needed**
   - Level-by-level → Queue (BFS)
   - Depth-first → Stack (DFS)
   - By cost/priority → Heap (Dijkstra, A*)

2. **Determine what state to track**
   - Just reachability? → visited set
   - Shortest path? → distance array + parent pointers
   - All paths? → path list

3. **Define the neighbor processing rule**
   - When is a neighbor added to the data structure?
   - What values are updated?

4. **Specify termination and verification**
   - How do you know you're done?
   - How do you confirm the result is correct?
