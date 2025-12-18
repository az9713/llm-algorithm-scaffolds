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

**Start with these verified scaffolds for best results:**

| If you need to... | Use this scaffold | Reliability |
|-------------------|-------------------|-------------|
| Find shortest path with heuristic | `scaffolds/01_graph/astar.md` | **CERTIFIED (100%)** |
| Order tasks with dependencies | `scaffolds/01_graph/topological_sort.md` | **CERTIFIED (100%)** |
| Sort data efficiently | `scaffolds/02_divide_conquer/merge_sort.md` | **CERTIFIED (100%)** |
| Solve placement puzzles | `scaffolds/04_backtracking/nqueens.md` | **CERTIFIED (100%)** |
| Find combinations summing to target | `scaffolds/04_backtracking/subset_sum.md` | **CERTIFIED (100%)** |

**Other commonly used scaffolds:**

| If you need to... | Use this scaffold | Reliability |
|-------------------|-------------------|-------------|
| Find shortest path (unweighted) | `scaffolds/01_graph/bfs.md` | PARTIAL (72.7%) |
| Search sorted data | `scaffolds/02_divide_conquer/binary_search.md` | PARTIAL (72.7%) |
| Find minimum spanning tree | `scaffolds/03_greedy/kruskal.md` | PARTIAL (81.8%) |
| Compare string similarity | `scaffolds/05_dynamic_programming/edit_distance.md` | PARTIAL (54.5%) |

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
| [Verification Guide](docs/VERIFICATION.md) | Automated testing framework | Validating scaffolds |
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
├── verify.py                 # Automated verification tool
├── .gitignore               # Git ignore rules
│
├── docs/                    # All documentation
│   ├── QUICK_START.md      # Start here - 10 examples
│   ├── USER_GUIDE.md       # Complete user manual
│   ├── DEVELOPER_GUIDE.md  # Contributor guide
│   ├── VERIFICATION.md     # Verification framework guide
│   ├── GLOSSARY.md         # Definitions
│   └── FAQ.md              # Common questions
│
├── scaffolds/               # All scaffold templates
│   ├── README.md           # Scaffold index
│   ├── templates/          # Generic templates (8 files)
│   ├── 01_graph/           # Graph algorithms (7 files)
│   ├── 02_divide_conquer/  # Divide & conquer (3 files)
│   ├── 03_greedy/          # Greedy algorithms (4 files)
│   ├── 04_backtracking/    # Backtracking (4 files)
│   ├── 05_dynamic_programming/  # DP (5 files)
│   ├── 06_optimization/    # Optimization (4 files)
│   ├── 07_string/          # String algorithms (3 files)
│   └── 08_numerical/       # Numerical methods (3 files)
│
└── verification/            # Automated verification framework
    ├── cli.py              # Command-line interface
    ├── runner.py           # Test orchestrator
    ├── reference/          # Ground truth implementations
    ├── generators/         # Test case generators
    ├── validators/         # Output validators
    └── reports/            # Report generators
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

## Automated Verification

Want to verify that scaffolds produce correct results? We have a fully automated verification framework.

### Quick Start

```bash
# 1. Install dependencies
pip install -r requirements-verification.txt

# 2. Set your API key
export ANTHROPIC_API_KEY=your_key_here

# 3. Run verification
python verify.py dijkstra          # Verify one scaffold
python verify.py --category graph  # Verify a category
python verify.py                   # Verify all 33 scaffolds
```

### What It Does

The verification framework:
1. **Generates test cases** using trusted libraries (networkx, numpy, scipy)
2. **Sends scaffold + test** to Claude API
3. **Parses responses** and extracts answers
4. **Validates** against ground truth
5. **Generates reports** with pass/fail status

### Certification Status

| Status | Pass Rate | Meaning |
|--------|-----------|---------|
| CERTIFIED | ≥90% | Scaffold works reliably |
| PARTIAL | 50-89% | Scaffold needs improvement |
| FAILED | <50% | Scaffold has issues |

### Current Results (December 2025)

| Status | Count | Scaffolds |
|--------|-------|-----------|
| **CERTIFIED** | 5 | astar, merge_sort, nqueens, subset_sum, topological_sort |
| **PARTIAL** | 6 | kruskal (81.8%), bfs (72.7%), binary_search (72.7%), bellman_ford (54.5%), dfs (54.5%), edit_distance (54.5%) |
| **FAILED** | 22 | See [VERIFICATION.md](docs/VERIFICATION.md) for details |

**Recommendation:** Start with certified scaffolds for the best experience.

See [Verification Guide](docs/VERIFICATION.md) for complete documentation.

---

## Requirements

**For using scaffolds (no technical skills needed):**
- A text editor to read/copy the scaffolds
- Access to an LLM (ChatGPT, Claude, Gemini, etc.)

No installation, no dependencies, no programming required.

**For running automated verification (optional):**
- Python 3.9+
- Anthropic API key
- Dependencies: `pip install -r requirements-verification.txt`

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
- **Improving failing scaffolds** (22 scaffolds need work!)

### High-Impact Contribution Areas

With only 5 of 33 scaffolds achieving 100% pass rate, there's significant opportunity to improve:

| Priority | Scaffold | Current Rate | Improvement Opportunity |
|----------|----------|--------------|------------------------|
| High | quickselect | 36.4% | Better partition state tracking |
| High | sudoku | 27.3% | More explicit constraint checking |
| High | dijkstra | 27.3% | Priority queue state tables |
| Medium | lis | 9.1% | Clearer DP state transitions |
| Medium | huffman | 9.1% | Step-by-step tree construction |

See [VERIFICATION.md](docs/VERIFICATION.md) for detailed failure analysis and improvement strategies.

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
