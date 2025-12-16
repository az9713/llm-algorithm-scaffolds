# Algorithmic Scaffolding Templates for LLMs

## Overview

This collection provides **algorithmic reasoning scaffolds** that help LLMs solve complex planning and optimization problems correctly. Based on the research from [Discovery AI](https://www.youtube.com/watch?v=r5tAzwQuNAo), these scaffolds work by:

1. **Explicitly defining state representations** before reasoning
2. **Specifying precise action/transition semantics**
3. **Enforcing algorithmic procedures** step-by-step
4. **Requiring verification** of solutions

## Why This Works

> Local LLMs fail at **planning**, not **execution**. They can follow a correct plan but lack the search discipline to discover it reliably.

By injecting the missing algorithmic structure into prompts, even smaller models can solve problems that would otherwise require much larger models.

---

## Quick Start

1. **Identify the problem type** (graph search, optimization, etc.)
2. **Select the appropriate scaffold** from the index below
3. **Copy the "Scaffold Instructions" section** into your prompt
4. **Adapt the state definition** to your specific problem
5. **Let the LLM execute** the algorithm step-by-step

---

## Scaffold Index

### 01. Graph Algorithms
| Algorithm | File | Use Case |
|-----------|------|----------|
| BFS | `01_graph/bfs.md` | Shortest path in unweighted graphs |
| DFS | `01_graph/dfs.md` | Path finding, cycle detection |
| Dijkstra | `01_graph/dijkstra.md` | Shortest path with non-negative weights |
| A* | `01_graph/astar.md` | Heuristic-guided shortest path |
| Bellman-Ford | `01_graph/bellman_ford.md` | Shortest path with negative weights |
| Floyd-Warshall | `01_graph/floyd_warshall.md` | All-pairs shortest paths |
| Topological Sort | `01_graph/topological_sort.md` | Task ordering with dependencies |

### 02. Divide & Conquer
| Algorithm | File | Use Case |
|-----------|------|----------|
| Binary Search | `02_divide_conquer/binary_search.md` | Searching in sorted arrays |
| Merge Sort | `02_divide_conquer/merge_sort.md` | Stable O(n log n) sorting |
| Quickselect | `02_divide_conquer/quickselect.md` | Finding k-th smallest element |

### 03. Greedy Algorithms
| Algorithm | File | Use Case |
|-----------|------|----------|
| Activity Selection | `03_greedy/activity_selection.md` | Interval scheduling |
| Huffman Coding | `03_greedy/huffman.md` | Optimal prefix-free encoding |
| Kruskal's MST | `03_greedy/kruskal.md` | Minimum spanning tree |
| Fractional Knapsack | `03_greedy/fractional_knapsack.md` | Divisible item selection |

### 04. Backtracking
| Algorithm | File | Use Case |
|-----------|------|----------|
| N-Queens | `04_backtracking/nqueens.md` | Constraint placement |
| Sudoku Solver | `04_backtracking/sudoku.md` | Grid constraint satisfaction |
| Graph Coloring | `04_backtracking/graph_coloring.md` | Resource assignment |
| Subset Sum | `04_backtracking/subset_sum.md` | Subset selection |

### 05. Dynamic Programming
| Algorithm | File | Use Case |
|-----------|------|----------|
| 0/1 Knapsack | `05_dynamic_programming/knapsack_01.md` | Indivisible item selection |
| LCS | `05_dynamic_programming/lcs.md` | Longest common subsequence |
| Edit Distance | `05_dynamic_programming/edit_distance.md` | String similarity |
| LIS | `05_dynamic_programming/lis.md` | Longest increasing subsequence |
| Matrix Chain | `05_dynamic_programming/matrix_chain.md` | Optimal parenthesization |

### 06. Optimization
| Algorithm | File | Use Case |
|-----------|------|----------|
| Gradient Descent | `06_optimization/gradient_descent.md` | Continuous optimization |
| Simulated Annealing | `06_optimization/simulated_annealing.md` | Global optimization |
| Genetic Algorithm | `06_optimization/genetic_algorithm.md` | Evolutionary optimization |
| Hill Climbing | `06_optimization/hill_climbing.md` | Local optimization |

### 07. String Algorithms
| Algorithm | File | Use Case |
|-----------|------|----------|
| KMP | `07_string/kmp.md` | Pattern matching |
| Rabin-Karp | `07_string/rabin_karp.md` | Hash-based pattern matching |
| Trie | `07_string/trie_operations.md` | Prefix-based search |

### 08. Numerical Methods
| Algorithm | File | Use Case |
|-----------|------|----------|
| Newton-Raphson | `08_numerical/newton_raphson.md` | Root finding (fast) |
| Bisection | `08_numerical/bisection.md` | Root finding (robust) |
| Monte Carlo | `08_numerical/monte_carlo.md` | Probabilistic estimation |

---

## Template Structure

Each scaffold file contains:

```
# [Algorithm Name] Scaffold

## When to Use
[Problem characteristics that indicate this algorithm]

## Scaffold Instructions (paste this to LLM)
[The actual instructions to copy-paste]

## Worked Example
[Complete example showing input → execution → output]

## Common Failure Modes
[What LLMs typically get wrong without scaffolding]
```

---

## Best Practices

### 1. Match Algorithm to Problem
- **Shortest path?** → BFS (unweighted), Dijkstra (weighted), Bellman-Ford (negative)
- **Optimal selection?** → Greedy (if optimal substructure) or DP
- **Constraint satisfaction?** → Backtracking
- **Global optimization?** → Simulated Annealing, Genetic Algorithm

### 2. Provide Complete Problem Context
Include in your prompt:
- All constraints and rules
- Initial and goal states
- Action costs/effects
- Edge cases

### 3. Verify Output
Always ask the LLM to:
- Trace through the solution step-by-step
- Verify constraints are satisfied
- Check against known solutions if possible

### 4. Use Two-Phase Approach
1. **Plan Phase:** Use scaffold to find solution
2. **Verify Phase:** Re-execute solution from scratch

---

## Example Usage

**Problem:** Find shortest path from A to E in weighted graph.

**Prompt:**
```
[Paste Dijkstra scaffold from 01_graph/dijkstra.md]

Now solve this specific problem:
- Graph: A-B(2), A-C(4), B-C(1), B-D(7), C-D(3), D-E(1)
- Source: A
- Goal: Find shortest path to E
```

**LLM follows scaffold:**
1. Defines state properly
2. Runs Dijkstra step-by-step
3. Returns: A→B→C→D→E (cost 7)
4. Verifies by tracing path

---

## Contributing

To add a new scaffold:
1. Create file in appropriate category folder
2. Follow the template structure
3. Include a complete worked example
4. Document common failure modes

---

## References

- [Discovery AI Video](https://www.youtube.com/watch?v=r5tAzwQuNAo)
- Original research on algorithmic scaffolding for LLMs
- Based on DSPy-style prompt optimization principles

---

## Built With

All 33 scaffolds, 8 generic templates, and documentation were created using:

- **[Claude Code](https://claude.ai/claude-code)** - Anthropic's AI-powered CLI coding assistant
- **Claude Opus 4.5** (`claude-opus-4-5-20251101`) - Anthropic's frontier model

---

## License

These scaffolds are provided for educational and research purposes.
