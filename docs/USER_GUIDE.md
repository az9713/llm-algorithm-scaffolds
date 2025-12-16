# User Guide - Algorithmic Scaffolding for LLMs

## Table of Contents

1. [Introduction](#introduction)
2. [What You'll Learn](#what-youll-learn)
3. [Prerequisites](#prerequisites)
4. [Understanding the Basics](#understanding-the-basics)
5. [How to Use Scaffolds](#how-to-use-scaffolds)
6. [Finding the Right Scaffold](#finding-the-right-scaffold)
7. [Step-by-Step Usage Instructions](#step-by-step-usage-instructions)
8. [Understanding Scaffold Components](#understanding-scaffold-components)
9. [Tips for Best Results](#tips-for-best-results)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Usage](#advanced-usage)
12. [Next Steps](#next-steps)

---

## Introduction

### What is This Guide?

This guide teaches you how to use **algorithmic scaffolds** to help AI assistants (like ChatGPT, Claude, or Gemini) solve complex problems correctly. You don't need any programming experience to use this guide.

### Who is This For?

- Anyone who uses AI assistants for problem-solving
- Students learning algorithms
- Professionals needing reliable AI-generated solutions
- Curious learners who want to understand how AI thinks

### What Problem Does This Solve?

AI assistants are helpful, but they sometimes make mistakes on complex problems like:
- Finding the best route between cities
- Scheduling meetings without conflicts
- Solving puzzles
- Making optimal decisions with constraints

**Scaffolds help AI follow proven problem-solving methods correctly.**

---

## What You'll Learn

By the end of this guide, you will be able to:

1. Understand what algorithmic scaffolds are and why they work
2. Find the right scaffold for your problem
3. Use scaffolds correctly with any AI assistant
4. Interpret the AI's step-by-step solution
5. Verify that solutions are correct
6. Troubleshoot when things don't work
7. Combine scaffolds for complex problems

---

## Prerequisites

### What You Need

1. **Access to an AI assistant** - Any of these will work:
   - ChatGPT (chat.openai.com)
   - Claude (claude.ai)
   - Gemini (gemini.google.com)
   - Any other modern LLM

2. **A way to read text files** - Any of these:
   - A web browser (if viewing on GitHub)
   - Notepad, TextEdit, or any text editor
   - VS Code, Sublime Text, or similar

3. **Basic computer skills**:
   - Opening files
   - Copying and pasting text
   - Typing in a chat interface

### What You DON'T Need

- Programming knowledge
- Math expertise
- Technical background
- Any software installation

---

## Understanding the Basics

### What is an Algorithm?

An **algorithm** is a step-by-step procedure for solving a problem. Like a recipe:

```
Recipe (Algorithm) for Making Tea:
1. Boil water
2. Put tea bag in cup
3. Pour hot water into cup
4. Wait 3-5 minutes
5. Remove tea bag
6. Add milk/sugar if desired
```

Algorithms exist for many problems:
- Finding shortest routes (Dijkstra's algorithm)
- Searching sorted lists (Binary search)
- Scheduling tasks (Greedy algorithms)
- Solving puzzles (Backtracking)

### What is a Scaffold?

A **scaffold** is a template that tells the AI:
1. **What to remember** (state) - like keeping track of which cities you've visited
2. **What to do at each step** (transitions) - like "move to the nearest unvisited city"
3. **When to stop** (termination) - like "stop when you've visited all cities"
4. **How to check the answer** (verification) - like "add up all distances"

### Why Do AI Assistants Need Scaffolds?

AI assistants are trained on text, not algorithms. They can:
- **Explain** algorithms well
- **Follow** clear instructions
- **Write** code that implements algorithms

But they often struggle to:
- **Execute** algorithms step-by-step correctly
- **Remember** all the state across many steps
- **Backtrack** when they hit dead ends

**Scaffolds provide the structure that AI assistants need.**

### A Simple Analogy

Imagine building furniture:

**Without instructions (no scaffold):**
- You might assemble pieces in the wrong order
- You might forget a step
- You might end up with extra screws

**With instructions (scaffold):**
- Clear step-by-step guidance
- Pictures showing what things should look like
- Checklist to verify you're done

Scaffolds do the same thing for AI problem-solving.

---

## How to Use Scaffolds

### The Basic Process

```
┌─────────────────────────────────────────────────────────────┐
│  1. IDENTIFY your problem type                              │
│     "I need to find the shortest route"                     │
│                         ↓                                   │
│  2. SELECT the appropriate scaffold                         │
│     "I'll use the Dijkstra scaffold"                        │
│                         ↓                                   │
│  3. COPY the scaffold instructions                          │
│     Open the file, copy the text                            │
│                         ↓                                   │
│  4. PASTE into your AI assistant                            │
│     Put it in ChatGPT/Claude/etc.                           │
│                         ↓                                   │
│  5. ADD your specific problem                               │
│     "Find shortest path from A to D in this graph..."       │
│                         ↓                                   │
│  6. REVIEW the AI's step-by-step solution                   │
│     Check that each step makes sense                        │
│                         ↓                                   │
│  7. VERIFY the final answer                                 │
│     Make sure the solution is correct                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Finding the Right Scaffold

### Problem Type Quick Reference

Use this table to find the right scaffold:

| Your Problem | Example | Scaffold to Use |
|--------------|---------|-----------------|
| Find shortest path (all edges equal) | "Fewest hops between computers" | BFS |
| Find shortest path (edges have costs) | "Cheapest flight route" | Dijkstra |
| Find shortest path (some costs negative) | "Profit/loss calculations" | Bellman-Ford |
| Find path with distance estimate | "GPS navigation" | A* |
| Find any path/check connectivity | "Is there a way from A to B?" | DFS |
| Order tasks with dependencies | "Build order for software" | Topological Sort |
| Search in sorted data | "Find a name in phonebook" | Binary Search |
| Sort data efficiently | "Arrange by date" | Merge Sort |
| Find k-th smallest item | "Find median salary" | Quickselect |
| Schedule non-overlapping events | "Meeting room booking" | Activity Selection |
| Build network with minimum cost | "Cheapest way to connect cities" | Kruskal's MST |
| Compress data | "Make files smaller" | Huffman Coding |
| Fill bag with most value | "Best items for limited budget" | Knapsack |
| Solve Sudoku | "Complete the puzzle" | Sudoku Backtracking |
| Place queens without conflict | "N-Queens puzzle" | N-Queens |
| Color map with limited colors | "Schedule without conflicts" | Graph Coloring |
| Find subset that sums to target | "Exact change problem" | Subset Sum |
| Compare two texts | "How similar are these?" | Edit Distance / LCS |
| Find pattern in text | "Search in document" | KMP / Rabin-Karp |
| Find root of equation | "Solve x² = 2" | Newton-Raphson / Bisection |
| Optimize complex function | "Best parameters" | Gradient Descent / Simulated Annealing |

### Detailed Category Guide

#### Category 1: Graph Algorithms
**Use when:** Your problem involves connections, networks, or relationships

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| BFS | Shortest path in unweighted graphs | `scaffolds/01_graph/bfs.md` |
| DFS | Exploring all paths, cycle detection | `scaffolds/01_graph/dfs.md` |
| Dijkstra | Shortest path with positive weights | `scaffolds/01_graph/dijkstra.md` |
| A* | Shortest path with heuristic guidance | `scaffolds/01_graph/astar.md` |
| Bellman-Ford | Shortest path allowing negative weights | `scaffolds/01_graph/bellman_ford.md` |
| Floyd-Warshall | All pairs shortest paths | `scaffolds/01_graph/floyd_warshall.md` |
| Topological Sort | Ordering with dependencies | `scaffolds/01_graph/topological_sort.md` |

#### Category 2: Divide & Conquer
**Use when:** You can split a big problem into smaller identical problems

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| Binary Search | Finding items in sorted data | `scaffolds/02_divide_conquer/binary_search.md` |
| Merge Sort | Sorting data stably | `scaffolds/02_divide_conquer/merge_sort.md` |
| Quickselect | Finding k-th element | `scaffolds/02_divide_conquer/quickselect.md` |

#### Category 3: Greedy Algorithms
**Use when:** Making the locally best choice leads to the globally best solution

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| Activity Selection | Scheduling non-overlapping events | `scaffolds/03_greedy/activity_selection.md` |
| Huffman Coding | Optimal data compression | `scaffolds/03_greedy/huffman.md` |
| Kruskal's MST | Minimum cost network | `scaffolds/03_greedy/kruskal.md` |
| Fractional Knapsack | Divisible item selection | `scaffolds/03_greedy/fractional_knapsack.md` |

#### Category 4: Backtracking
**Use when:** You need to try possibilities and undo bad choices

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| N-Queens | Placement puzzles | `scaffolds/04_backtracking/nqueens.md` |
| Sudoku | Grid constraint puzzles | `scaffolds/04_backtracking/sudoku.md` |
| Graph Coloring | Assignment with constraints | `scaffolds/04_backtracking/graph_coloring.md` |
| Subset Sum | Finding exact combinations | `scaffolds/04_backtracking/subset_sum.md` |

#### Category 5: Dynamic Programming
**Use when:** The problem has overlapping subproblems

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| 0/1 Knapsack | Selecting items with weight limit | `scaffolds/05_dynamic_programming/knapsack_01.md` |
| LCS | Longest common subsequence | `scaffolds/05_dynamic_programming/lcs.md` |
| Edit Distance | String similarity | `scaffolds/05_dynamic_programming/edit_distance.md` |
| LIS | Longest increasing subsequence | `scaffolds/05_dynamic_programming/lis.md` |
| Matrix Chain | Optimal parenthesization | `scaffolds/05_dynamic_programming/matrix_chain.md` |

#### Category 6: Optimization
**Use when:** Searching for best solution in large space

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| Gradient Descent | Continuous optimization | `scaffolds/06_optimization/gradient_descent.md` |
| Simulated Annealing | Escaping local optima | `scaffolds/06_optimization/simulated_annealing.md` |
| Genetic Algorithm | Complex search spaces | `scaffolds/06_optimization/genetic_algorithm.md` |
| Hill Climbing | Simple local search | `scaffolds/06_optimization/hill_climbing.md` |

#### Category 7: String Algorithms
**Use when:** Working with text patterns and sequences

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| KMP | Efficient pattern matching | `scaffolds/07_string/kmp.md` |
| Rabin-Karp | Multiple pattern matching | `scaffolds/07_string/rabin_karp.md` |
| Trie Operations | Prefix-based operations | `scaffolds/07_string/trie_operations.md` |

#### Category 8: Numerical Methods
**Use when:** Solving mathematical equations or estimating values

| Scaffold | Best For | File Location |
|----------|----------|---------------|
| Newton-Raphson | Fast root finding | `scaffolds/08_numerical/newton_raphson.md` |
| Bisection | Guaranteed root finding | `scaffolds/08_numerical/bisection.md` |
| Monte Carlo | Probabilistic estimation | `scaffolds/08_numerical/monte_carlo.md` |

---

## Step-by-Step Usage Instructions

### Step 1: Open the Scaffold File

**Method A: If you have the files on your computer**
1. Navigate to the project folder
2. Open the `scaffolds` folder
3. Open the appropriate category folder (e.g., `01_graph`)
4. Double-click the scaffold file (e.g., `dijkstra.md`)
5. The file will open in your default text editor

**Method B: If viewing on GitHub or online**
1. Navigate to the scaffold folder in your browser
2. Click on the scaffold file
3. The content will display in your browser

### Step 2: Locate the "Scaffold Instructions" Section

Every scaffold file has this structure:

```markdown
# [Algorithm Name] Scaffold

## When to Use           ← Background information
[Describes when to use this algorithm]

## Scaffold Instructions  ← THIS IS WHAT YOU COPY
[The actual template to use]

## Worked Example        ← Reference example
[Shows the scaffold in action]

## Common Failure Modes  ← Troubleshooting help
[What can go wrong]
```

**Find the section labeled "Scaffold Instructions"** - this is what you'll copy.

### Step 3: Copy the Scaffold Instructions

**On Windows:**
1. Click at the start of the Scaffold Instructions section
2. Hold Shift and click at the end of the section
3. Press Ctrl+C to copy

**On Mac:**
1. Click at the start of the Scaffold Instructions section
2. Hold Shift and click at the end of the section
3. Press Cmd+C to copy

**Alternative method:**
1. Select all text in the section by clicking and dragging
2. Right-click and select "Copy"

### Step 4: Open Your AI Assistant

**For ChatGPT:**
1. Go to chat.openai.com
2. Log in if needed
3. Click "New chat" to start fresh

**For Claude:**
1. Go to claude.ai
2. Log in if needed
3. Start a new conversation

**For Gemini:**
1. Go to gemini.google.com
2. Log in if needed
3. Start a new chat

### Step 5: Paste the Scaffold

1. Click in the message input box
2. Press Ctrl+V (Windows) or Cmd+V (Mac) to paste
3. Don't send yet!

### Step 6: Add Your Specific Problem

After the scaffold text, add:
- A blank line
- "Now solve this specific problem:"
- Your problem details

**Example:**
```
[Scaffold text you pasted]

Now solve this specific problem:
- Graph nodes: A, B, C, D, E
- Edges: A-B (cost 2), A-C (cost 4), B-C (cost 1), B-D (cost 7), C-E (cost 3), D-E (cost 1)
- Find: Shortest path from A to E
```

### Step 7: Send and Review

1. Press Enter or click Send
2. Watch the AI work through the scaffold
3. It should show step-by-step work
4. Review each step for correctness

### Step 8: Verify the Result

The AI's answer should include:
- The final solution
- The cost/value if applicable
- Verification that it's correct

**Check by:**
- Following the solution path yourself
- Adding up costs
- Checking constraints are met

---

## Understanding Scaffold Components

### Anatomy of a Scaffold

Every scaffold has these key parts:

```
1) Problem Restatement      ← AI restates your problem
2) State Definition         ← What the AI will track
3) Initialization          ← Starting values
4) Main Algorithm          ← Step-by-step procedure
5) Termination Condition   ← When to stop
6) Verification            ← Checking the answer
```

### What Each Part Does

**1) Problem Restatement**
- AI confirms it understands your problem
- Helps catch misunderstandings early
- You can correct if needed

**2) State Definition**
- Lists all variables the AI will track
- Like a checklist of what to remember
- Example: "distances to each node", "visited nodes"

**3) Initialization**
- Sets starting values
- Example: "distance to start = 0, all others = infinity"

**4) Main Algorithm**
- The core procedure
- Usually a loop that repeats until done
- Each iteration makes progress

**5) Termination Condition**
- How the AI knows it's done
- Example: "goal node reached" or "all nodes visited"

**6) Verification**
- Final check that the answer is correct
- Traces through the solution
- Confirms all constraints are met

---

## Tips for Best Results

### Do's

1. **Copy the entire scaffold** - Don't skip sections
2. **Be specific about your problem** - Include all details
3. **Ask for step-by-step work** - Say "show your work"
4. **Start with simple examples** - Build up to complex ones
5. **Verify the answer** - Check the AI's work
6. **Use the worked example** - Compare your problem to it

### Don'ts

1. **Don't modify the scaffold** (until you're experienced)
2. **Don't skip the verification step**
3. **Don't assume the first answer is correct**
4. **Don't use scaffolds for problems they don't fit**

### Magic Phrases That Help

When the AI doesn't follow the scaffold correctly, try:

- "Please follow the scaffold exactly, step by step."
- "Show your state after each step in a table."
- "Verify your answer by tracing through the solution."
- "Start over and be more careful with the state updates."
- "What is the current state? List all variables."

### When to Use Which AI

| AI | Strengths | Best For |
|----|-----------|----------|
| GPT-4 | Complex reasoning | Hard optimization problems |
| Claude | Following instructions | Precise algorithm execution |
| Gemini | Mathematical tasks | Numerical methods |
| GPT-3.5 | Speed | Simple scaffolds |

---

## Troubleshooting

### Problem: AI Ignores the Scaffold

**Symptoms:** AI gives answer without showing steps

**Solutions:**
1. Add "Follow the scaffold step by step, showing all work."
2. Start fresh conversation
3. Try a different AI assistant

### Problem: AI Makes Errors Mid-Solution

**Symptoms:** Steps are correct then suddenly wrong

**Solutions:**
1. Ask "Please verify step N - is that correct?"
2. Point out the error and ask to continue from before it
3. Break problem into smaller parts

### Problem: AI Says "I Can't Do This"

**Symptoms:** AI refuses or says it's not capable

**Solutions:**
1. Rephrase as a hypothetical: "If you were to solve this..."
2. Start with the worked example first
3. Use a more capable AI model

### Problem: Answer Seems Wrong

**Symptoms:** Solution doesn't match expected result

**Solutions:**
1. Ask AI to verify: "Check this by tracing through the solution"
2. Try the problem with a smaller example first
3. Compare with the worked example in the scaffold

### Problem: Scaffold Doesn't Fit My Problem

**Symptoms:** Can't figure out how to apply the scaffold

**Solutions:**
1. Check if a different scaffold fits better
2. Read the "When to Use" section carefully
3. See FAQ or ask in discussions

---

## Advanced Usage

### Combining Scaffolds

Some problems need multiple algorithms:

**Example: Traveling Salesman approximation**
1. Use Kruskal's MST to get minimum spanning tree
2. Use DFS to traverse the tree
3. This gives a reasonable (though not optimal) tour

**How to combine:**
```
First, I'll use the Kruskal scaffold to find the MST:
[Kruskal scaffold]

[Solve MST problem]

Now, using the MST result, I'll apply DFS:
[DFS scaffold]

[Complete the solution]
```

### Creating Custom Scaffolds

Use the generic templates in `scaffolds/templates/` to create your own:

1. Choose the category template that matches your algorithm type
2. Fill in the blanks for your specific algorithm
3. Add a worked example
4. Test it with the AI

See [Developer Guide](DEVELOPER_GUIDE.md) for detailed instructions.

### Optimizing for Token Usage

If your AI has token limits:

1. **Shorten the scaffold** - Remove worked examples after learning
2. **Use abbreviations** - "dist" instead of "distance"
3. **Summarize state** - "Show state as: (node, dist, prev)"

### Multi-Step Problem Solving

For very complex problems:

1. Break into sub-problems
2. Solve each with appropriate scaffold
3. Combine results
4. Verify combined solution

---

## Next Steps

### Beginner Path
1. Complete [Quick Start Guide](QUICK_START.md) - all 10 examples
2. Try 3 scaffolds on your own problems
3. Read FAQ for common issues
4. Explore one category deeply

### Intermediate Path
1. Try all scaffolds in one category
2. Compare AI performance across assistants
3. Start modifying scaffolds
4. Read the generic templates

### Advanced Path
1. Create your own scaffolds
2. Contribute to the project
3. Read Developer Guide
4. Help others in discussions

---

## Summary

You now know how to:
- Find the right scaffold for your problem
- Copy and use scaffolds with AI assistants
- Interpret step-by-step solutions
- Troubleshoot common issues
- Advance to more complex usage

**Start practicing with the [Quick Start Guide](QUICK_START.md)!**
