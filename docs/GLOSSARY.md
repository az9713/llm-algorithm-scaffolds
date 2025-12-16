# Glossary of Terms

This glossary explains all technical terms used in this project. Terms are organized alphabetically and written for beginners.

---

## A

### Algorithm
A step-by-step procedure for solving a problem. Like a recipe, but for computers or mathematical problems.

**Example:** A sorting algorithm arranges items in order (smallest to largest).

### A* (A-Star)
A graph search algorithm that finds the shortest path using a heuristic (educated guess) to guide the search. Faster than Dijkstra when you have a good heuristic.

**When to use:** GPS navigation, game pathfinding.

---

## B

### Backtracking
A problem-solving technique where you try choices one by one, and "undo" (backtrack) when you reach a dead end.

**Analogy:** Solving a maze by trying each path, and turning back when you hit a wall.

**When to use:** Puzzles like Sudoku, N-Queens, or any "try all possibilities" problem.

### Base Case
The simplest version of a problem that can be solved directly without further recursion.

**Example:** In factorial, base case is: factorial(0) = 1.

### BFS (Breadth-First Search)
A graph traversal that explores all neighbors at the current depth before moving deeper. Uses a queue.

**Analogy:** Ripples spreading out from a stone dropped in water.

**When to use:** Finding shortest path when all edges have equal weight.

### Binary Search
A search algorithm that repeatedly divides a sorted list in half to find a target value.

**Analogy:** Finding a word in a dictionary by opening to the middle, then half of the remaining section, etc.

**When to use:** Searching in sorted data.

---

## C

### Complexity (Time/Space)
A measure of how an algorithm's resource usage grows with input size.

- **Time complexity:** How long it takes (number of operations)
- **Space complexity:** How much memory it uses

**Common complexities:**
- O(1): Constant - same time regardless of input size
- O(log n): Logarithmic - very fast, like binary search
- O(n): Linear - time grows proportionally with input
- O(n²): Quadratic - time grows with square of input

### Constraint
A rule or limitation that a solution must satisfy.

**Example:** In scheduling, a constraint might be "no two meetings can overlap."

### Convergence
When an iterative algorithm's results approach a stable final value.

**Example:** Newton-Raphson converges to the square root.

---

## D

### DFS (Depth-First Search)
A graph traversal that explores as far as possible along each branch before backtracking. Uses a stack.

**Analogy:** Exploring a maze by always taking the first available turn until you hit a dead end.

**When to use:** Finding any path, detecting cycles, topological sorting.

### Dijkstra's Algorithm
A graph algorithm that finds the shortest path from a source to all other nodes, using edge weights.

**Requirement:** All edge weights must be non-negative (≥ 0).

**When to use:** GPS navigation, network routing.

### Divide and Conquer
A strategy that breaks a problem into smaller subproblems, solves them independently, and combines the results.

**Examples:** Merge sort, binary search.

### Dynamic Programming (DP)
A technique that solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation.

**Key insight:** If you solve the same subproblem multiple times, store the answer.

**When to use:** Optimization problems with overlapping subproblems.

---

## E

### Edge
A connection between two nodes in a graph.

**Types:**
- **Directed edge:** One-way connection (A → B)
- **Undirected edge:** Two-way connection (A — B)
- **Weighted edge:** Has a cost/distance value

### Edit Distance
The minimum number of single-character operations (insert, delete, replace) needed to transform one string into another.

**Example:** "cat" → "car" has edit distance 1 (replace 't' with 'r').

---

## F

### Failure Function (KMP)
An array used in KMP string matching that tells how far to "fall back" when a mismatch occurs, avoiding redundant comparisons.

### FIFO (First-In-First-Out)
Items are processed in the order they were added. Used by queues.

**Analogy:** A line at a store - first person in line is served first.

---

## G

### Graph
A data structure consisting of nodes (vertices) connected by edges.

**Types:**
- **Directed graph:** Edges have direction (one-way streets)
- **Undirected graph:** Edges go both ways (two-way streets)
- **Weighted graph:** Edges have costs/distances

### Greedy Algorithm
An algorithm that makes the locally optimal choice at each step, hoping to find a global optimum.

**When it works:** Activity selection, Huffman coding.
**When it fails:** 0/1 Knapsack (use DP instead).

---

## H

### Heuristic
An educated guess that helps guide an algorithm toward a solution faster.

**Example:** In A*, the heuristic estimates distance to the goal.

### Huffman Coding
A compression algorithm that assigns shorter codes to more frequent characters.

**Result:** Smaller file sizes for text with uneven character frequencies.

---

## I

### Initialization
Setting up the starting state before an algorithm runs.

**Example:** In Dijkstra, initialize all distances to infinity except the source (distance 0).

### Iteration
One cycle through a loop or repeated process.

**Example:** "After 5 iterations, the value converged."

---

## K

### Knapsack Problem
A classic optimization problem: given items with weights and values, find the most valuable combination that fits in a container of limited capacity.

**Variants:**
- **0/1 Knapsack:** Take each item entirely or not at all (use DP)
- **Fractional Knapsack:** Can take partial items (use Greedy)

### KMP (Knuth-Morris-Pratt)
An efficient string matching algorithm that avoids redundant comparisons using a failure function.

**When to use:** Finding patterns in text.

---

## L

### LCS (Longest Common Subsequence)
The longest sequence of characters that appears in both strings in the same order (not necessarily consecutive).

**Example:** LCS of "ABCD" and "AEBD" is "ABD" (length 3).

### LIFO (Last-In-First-Out)
The most recently added item is processed first. Used by stacks.

**Analogy:** A stack of plates - you take the top one first.

### LIS (Longest Increasing Subsequence)
The longest subsequence where each element is greater than the previous.

**Example:** In [10, 9, 2, 5, 3, 7, 101], the LIS is [2, 3, 7, 101] (length 4).

### LLM (Large Language Model)
An AI system trained on text that can generate human-like responses. Examples: ChatGPT, Claude, Gemini.

---

## M

### Memoization
Storing the results of function calls to avoid recomputing them. A top-down DP technique.

**Example:** Store fibonacci(10) so you don't recalculate it every time.

### Minimum Spanning Tree (MST)
A subset of edges that connects all nodes in a graph with minimum total weight, without forming cycles.

**Algorithms:** Kruskal's, Prim's.

### Monte Carlo Method
Using random sampling to estimate numerical results.

**Example:** Estimate π by randomly throwing darts at a square with an inscribed circle.

---

## N

### Newton-Raphson Method
An iterative method for finding roots of equations. Very fast when it works.

**Formula:** x_new = x - f(x)/f'(x)

### Node (Vertex)
A point in a graph. Nodes can represent cities, computers, people, etc.

### N-Queens Problem
A puzzle: place N chess queens on an N×N board so no two queens attack each other.

---

## O

### O-notation (Big O)
A way to describe how an algorithm's time or space requirements grow with input size.

**Common values:**
| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Simple loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Brute force |

### Optimal Substructure
A property where the optimal solution contains optimal solutions to subproblems.

**Required for:** Dynamic programming, greedy algorithms.

---

## P

### Path
A sequence of nodes connected by edges in a graph.

**Example:** A → B → C → D is a path of length 3.

### Priority Queue
A data structure where elements are processed by priority, not insertion order. Often implemented with a heap.

**Used in:** Dijkstra's algorithm, A*.

### Pruning
Eliminating branches of a search tree that cannot lead to a valid solution.

**Example:** In backtracking, skip choices that violate constraints.

---

## Q

### Queue
A data structure following FIFO (First-In-First-Out) order.

**Operations:**
- **Enqueue:** Add to back
- **Dequeue:** Remove from front

**Used in:** BFS.

---

## R

### Recurrence Relation
A mathematical formula that defines a value in terms of smaller instances.

**Example:** fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

### Recursion
A technique where a function calls itself with smaller inputs until reaching a base case.

**Components:**
1. Base case (stopping condition)
2. Recursive case (self-call with smaller input)

---

## S

### Scaffold
In this project: A structured template that guides an LLM through an algorithm step by step.

**Components:** State definition, transitions, procedure, verification.

### Simulated Annealing
An optimization algorithm inspired by metallurgy that can escape local optima by sometimes accepting worse solutions.

**When to use:** Complex optimization with many local optima.

### Stack
A data structure following LIFO (Last-In-First-Out) order.

**Operations:**
- **Push:** Add to top
- **Pop:** Remove from top

**Used in:** DFS, backtracking.

### State
All the information needed to describe the current situation in an algorithm.

**Example:** In Dijkstra, state includes: distances, visited nodes, parent pointers.

---

## T

### Tabulation
Building a DP solution bottom-up by filling a table. Opposite of memoization (top-down).

### Termination Condition
The rule that determines when an algorithm should stop.

**Examples:**
- "Queue is empty"
- "Goal node reached"
- "Difference < tolerance"

### Topological Sort
An ordering of nodes in a directed graph where every edge goes from earlier to later in the ordering.

**When to use:** Task scheduling with dependencies, build systems.

### Trie
A tree structure for storing strings where each node represents a character. Enables fast prefix searches.

**When to use:** Autocomplete, spell checkers.

---

## V

### Verification
Checking that a solution is correct after finding it.

**Methods:**
- Trace through the solution
- Check all constraints
- Compare with known values

### Visited Set
A set that tracks which nodes have been processed, preventing infinite loops in graph traversal.

---

## W

### Weight (Edge Weight)
A value associated with an edge, representing cost, distance, or some other measure.

**Example:** Flight from NYC to LA costs $300 → edge weight is 300.

---

## Quick Reference: Algorithm Categories

| Category | Key Characteristic | Examples |
|----------|-------------------|----------|
| Graph | Nodes and edges | BFS, DFS, Dijkstra |
| Divide & Conquer | Split, solve, combine | Binary search, merge sort |
| Greedy | Local best → global best | Activity selection |
| Backtracking | Try, fail, undo | Sudoku, N-Queens |
| Dynamic Programming | Store subproblem results | Knapsack, LCS |
| Optimization | Search for best solution | Gradient descent |
| String | Text patterns | KMP, tries |
| Numerical | Mathematical computation | Newton-Raphson |

---

## Need More Help?

- See [FAQ](FAQ.md) for common questions
- See [User Guide](USER_GUIDE.md) for detailed instructions
- See [Quick Start](QUICK_START.md) for hands-on examples
