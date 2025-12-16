# Algorithmic Scaffolding for LLMs

> **Help AI assistants solve complex problems correctly by providing structured reasoning templates**

## What is This Project?

This project provides **algorithmic scaffolds** - structured prompt templates that guide Large Language Models (LLMs) like ChatGPT, Claude, or Gemini through complex problem-solving. Think of scaffolds as "thinking guides" that help AI follow proven algorithms step-by-step.

### The Problem We Solve

AI assistants are great at many tasks, but they often struggle with:
- Finding the shortest path in a graph
- Solving puzzles like Sudoku
- Optimizing complex decisions
- Following multi-step algorithms correctly

**Why?** Because LLMs process text, not algorithms. They can write about Dijkstra's algorithm but may make mistakes when actually executing it.

### Our Solution

We provide copy-paste templates that:
1. Tell the AI exactly what information to track
2. Guide it through each step of the algorithm
3. Ensure it verifies its answer
4. Prevent common reasoning errors

---

## Quick Start (5 Minutes)

### Step 1: Choose Your Problem Type

| If you need to... | Use this scaffold |
|-------------------|-------------------|
| Find shortest path (unweighted) | `scaffolds/01_graph/bfs.md` |
| Find shortest path (weighted) | `scaffolds/01_graph/dijkstra.md` |
| Search sorted data | `scaffolds/02_divide_conquer/binary_search.md` |
| Schedule non-overlapping activities | `scaffolds/03_greedy/activity_selection.md` |
| Solve Sudoku | `scaffolds/04_backtracking/sudoku.md` |
| Choose items with weight limit | `scaffolds/05_dynamic_programming/knapsack_01.md` |

### Step 2: Copy the Scaffold

Open the scaffold file and copy the **"Scaffold Instructions"** section.

### Step 3: Add Your Problem

Paste into your AI chat and add your specific problem:

```
[Paste scaffold instructions here]

Now solve this specific problem:
- Graph: A connects to B (cost 2), B connects to C (cost 3)...
- Find: Shortest path from A to D
```

### Step 4: Watch the AI Work

The AI will now follow the structured approach, showing its work at each step.

---

## What's Included

### 33 Ready-to-Use Scaffolds

Organized into 8 categories:

| Category | Scaffolds | Example Use Cases |
|----------|-----------|-------------------|
| **Graph Algorithms** | BFS, DFS, Dijkstra, A*, Bellman-Ford, Floyd-Warshall, Topological Sort | Navigation, network routing, dependency ordering |
| **Divide & Conquer** | Binary Search, Merge Sort, Quickselect | Searching, sorting, finding medians |
| **Greedy** | Activity Selection, Huffman Coding, Kruskal's MST, Fractional Knapsack | Scheduling, compression, network design |
| **Backtracking** | N-Queens, Sudoku, Graph Coloring, Subset Sum | Puzzles, constraint satisfaction |
| **Dynamic Programming** | 0/1 Knapsack, LCS, Edit Distance, LIS, Matrix Chain | Optimization, text comparison |
| **Optimization** | Gradient Descent, Simulated Annealing, Genetic Algorithm, Hill Climbing | Machine learning, complex optimization |
| **String Algorithms** | KMP, Rabin-Karp, Trie Operations | Text search, autocomplete |
| **Numerical Methods** | Newton-Raphson, Bisection, Monte Carlo | Root finding, integration |

### 8 Generic Templates

Want to create your own scaffold? Use our category templates:

```
scaffolds/templates/
├── graph_algorithm_template.md      # For any graph algorithm
├── divide_conquer_template.md       # For any divide & conquer
├── greedy_template.md               # For any greedy algorithm
├── backtracking_template.md         # For any backtracking
├── dynamic_programming_template.md  # For any DP problem
├── optimization_template.md         # For any optimization
├── string_algorithm_template.md     # For any string algorithm
└── numerical_method_template.md     # For any numerical method
```

---

## Documentation

| Document | Description | Best For |
|----------|-------------|----------|
| [Quick Start Guide](docs/QUICK_START.md) | 10 hands-on examples | **Start here!** |
| [User Guide](docs/USER_GUIDE.md) | Complete usage instructions | Learning the system |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | How to contribute | Adding new scaffolds |
| [Glossary](docs/GLOSSARY.md) | Terms explained | Understanding concepts |
| [FAQ](docs/FAQ.md) | Common questions | Troubleshooting |
| [Scaffold Index](scaffolds/README.md) | All scaffolds listed | Finding scaffolds |

---

## Why Does This Work?

### The Science Behind It

Research shows that LLMs fail at **planning**, not **execution**. They can:
- Explain algorithms correctly
- Follow clear instructions
- Verify solutions

But they struggle to:
- Maintain state across many steps
- Backtrack when stuck
- Explore systematically

**Scaffolds solve this** by providing the structure that LLMs lack:
- Explicit state definitions
- Clear transition rules
- Step-by-step procedures
- Verification protocols

### Real Improvement

Without scaffolding:
```
Q: Find shortest path from A to E in this graph...
A: The shortest path is A -> C -> E with cost 7.
   [WRONG - missed A -> B -> D -> E with cost 5]
```

With scaffolding:
```
Q: [Dijkstra scaffold] Find shortest path from A to E...
A: Step 1: Initialize distances...
   Step 2: Process A, update neighbors...
   ...
   Final: A -> B -> D -> E with cost 5 [CORRECT]
```

---

## Project Structure

```
algorithmic_scaffolding_discover_ai/
│
├── README.md                 # You are here
├── CLAUDE.md                 # Context for Claude Code
├── .gitignore               # Git ignore rules
│
├── docs/                    # All documentation
│   ├── QUICK_START.md      # Start here - 10 examples
│   ├── USER_GUIDE.md       # Complete user manual
│   ├── DEVELOPER_GUIDE.md  # Contributor guide
│   ├── GLOSSARY.md         # Definitions
│   └── FAQ.md              # Common questions
│
└── scaffolds/               # All scaffold templates
    ├── README.md           # Scaffold index
    ├── templates/          # Generic templates (8 files)
    ├── 01_graph/           # Graph algorithms (7 files)
    ├── 02_divide_conquer/  # Divide & conquer (3 files)
    ├── 03_greedy/          # Greedy algorithms (4 files)
    ├── 04_backtracking/    # Backtracking (4 files)
    ├── 05_dynamic_programming/  # DP (5 files)
    ├── 06_optimization/    # Optimization (4 files)
    ├── 07_string/          # String algorithms (3 files)
    └── 08_numerical/       # Numerical methods (3 files)
```

---

## Getting Started

### For Users (No Technical Skills Needed)

1. **Read** [Quick Start Guide](docs/QUICK_START.md) - 10 worked examples
2. **Try** copying a scaffold into ChatGPT, Claude, or Gemini
3. **Experiment** with your own problems
4. **Explore** more scaffolds as needed

### For Developers

1. **Read** [Developer Guide](docs/DEVELOPER_GUIDE.md)
2. **Understand** the scaffold structure
3. **Create** new scaffolds using templates
4. **Test** with multiple LLMs
5. **Contribute** your improvements

---

## Requirements

**None!** This is a collection of text templates. You just need:
- A text editor to read/copy the scaffolds
- Access to an LLM (ChatGPT, Claude, Gemini, etc.)

No installation, no dependencies, no programming required.

---

## Frequently Asked Questions

**Q: Which AI should I use?**
A: Any modern LLM works. Claude, GPT-4, and Gemini Pro give best results.

**Q: Do I need to understand the algorithm?**
A: No! The scaffold guides the AI. But understanding helps you verify results.

**Q: What if the AI doesn't follow the scaffold?**
A: Try: "Please follow the scaffold step by step, showing your work."

**Q: Can I modify the scaffolds?**
A: Yes! Adapt them to your needs. See the Developer Guide.

See [FAQ](docs/FAQ.md) for more questions.

---

## Contributing

We welcome contributions! See [Developer Guide](docs/DEVELOPER_GUIDE.md) for:
- How to add new scaffolds
- Style guidelines
- Testing procedures

---

## Credits

- Based on research from Discovery AI
- Reference: [Discovery AI Video](https://www.youtube.com/watch?v=r5tAzwQuNAo)

### Built With

This entire project - all 33 algorithm scaffolds, 8 generic templates, and comprehensive documentation - was created using:

- **[Claude Code](https://claude.ai/claude-code)** - Anthropic's AI-powered coding assistant
- **Claude Opus 4.5** (`claude-opus-4-5-20251101`) - Anthropic's most capable model

The scaffolds, templates, documentation, quick start guide, glossary, FAQ, and all other content were generated through collaborative human-AI development.

---

## License

This project is provided for educational and research purposes.
