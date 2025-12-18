# Developer Guide - Algorithmic Scaffolding for LLMs

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started as a Developer](#getting-started-as-a-developer)
3. [Project Architecture](#project-architecture)
4. [Understanding Scaffold Structure](#understanding-scaffold-structure)
5. [Creating New Scaffolds](#creating-new-scaffolds)
6. [Using Generic Templates](#using-generic-templates)
7. [Testing Scaffolds](#testing-scaffolds)
8. [Automated Verification Framework](#automated-verification-framework)
9. [Style Guidelines](#style-guidelines)
10. [Common Patterns and Anti-Patterns](#common-patterns-and-anti-patterns)
11. [Contributing to the Project](#contributing-to-the-project)
12. [Maintenance Tasks](#maintenance-tasks)
13. [Troubleshooting Development Issues](#troubleshooting-development-issues)

---

## Introduction

### Purpose of This Guide

This guide is for anyone who wants to:
- Create new algorithm scaffolds
- Improve existing scaffolds
- Understand how the project works internally
- Contribute to the project

### What You'll Learn

By following this guide, you will be able to:
1. Understand the complete project structure
2. Create professional-quality scaffolds from scratch
3. Use generic templates to speed up scaffold creation
4. Test scaffolds effectively across different LLMs
5. Follow project conventions consistently
6. Contribute improvements to the project

### Prerequisites

**Required knowledge:**
- Basic understanding of algorithms (what they do, not implementation)
- Ability to read and write Markdown
- Familiarity with at least one AI assistant (ChatGPT, Claude, etc.)

**Not required:**
- Programming expertise
- Deep algorithm knowledge (you'll learn as you go)
- Git expertise (though helpful for contributing)

---

## Getting Started as a Developer

### Step 1: Get the Project Files

**Option A: Download as ZIP**
1. Go to the project location
2. Download all files as a ZIP
3. Extract to a folder on your computer
4. Open the folder in your text editor

**Option B: Clone with Git (if you know Git)**
```bash
git clone [repository-url]
cd algorithmic_scaffolding_discover_ai
```

### Step 2: Set Up Your Environment

**Recommended text editors (any will work):**
- **VS Code** (free, recommended) - Best markdown preview
- **Sublime Text** - Fast and lightweight
- **Notepad++** (Windows) - Simple and effective
- **TextEdit** (Mac) - Built-in, works fine
- **Any editor** that can handle plain text files

**Optional but helpful:**
1. Install a Markdown preview extension for your editor
2. Set up a folder bookmark for quick access

### Step 3: Explore the Project Structure

Open these files to understand the project:
1. `README.md` - Project overview
2. `CLAUDE.md` - Technical context
3. `scaffolds/README.md` - Scaffold index
4. One scaffold file (e.g., `scaffolds/01_graph/bfs.md`) - See the structure
5. One template file (e.g., `scaffolds/templates/graph_algorithm_template.md`) - See the pattern

### Step 4: Try Using a Scaffold

Before creating scaffolds, use one:
1. Copy `scaffolds/01_graph/bfs.md` Scaffold Instructions
2. Paste into an AI assistant
3. Add a simple problem
4. Observe how the AI uses the scaffold

This experience is essential for creating good scaffolds.

---

## Project Architecture

### Directory Structure Explained

```
algorithmic_scaffolding_discover_ai/
│
├── README.md                    # Main entry point for users
│   └── Purpose: First thing people see, overview and quick links
│
├── CLAUDE.md                    # Context for Claude Code AI
│   └── Purpose: Helps AI assistants understand the project
│
├── .gitignore                   # Git ignore rules
│   └── Purpose: Keeps unnecessary files out of version control
│
├── docs/                        # All documentation
│   ├── USER_GUIDE.md           # Complete user manual
│   ├── DEVELOPER_GUIDE.md      # This file - for contributors
│   ├── QUICK_START.md          # Hands-on tutorial with examples
│   ├── GLOSSARY.md             # Definitions of terms
│   ├── FAQ.md                  # Frequently asked questions
│   └── algorithmic_scaffolding_for_llms.txt  # Original concept
│
├── scaffolds/                   # All scaffold templates
│   │
│   ├── README.md               # Index of all scaffolds
│   │   └── Purpose: Quick reference to find scaffolds
│   │
│   ├── templates/              # Generic category templates (8 files)
│   │   └── Purpose: Meta-templates for creating new scaffolds
│   │
│   ├── 01_graph/               # Graph algorithm scaffolds
│   ├── 02_divide_conquer/      # Divide & conquer scaffolds
│   ├── 03_greedy/              # Greedy algorithm scaffolds
│   ├── 04_backtracking/        # Backtracking scaffolds
│   ├── 05_dynamic_programming/ # Dynamic programming scaffolds
│   ├── 06_optimization/        # Optimization scaffolds
│   ├── 07_string/              # String algorithm scaffolds
│   └── 08_numerical/           # Numerical method scaffolds
│
└── .ignore/                    # Source materials (not in git)
    └── Purpose: Original research notes and transcripts
```

### File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Scaffold files | `algorithm_name.md` | `dijkstra.md` |
| Template files | `category_template.md` | `graph_algorithm_template.md` |
| Documentation | `UPPERCASE_NAME.md` | `USER_GUIDE.md` |
| Folders | `NN_category_name` | `01_graph` |

### Relationship Between Files

```
┌─────────────────────────────────────────────────────────────────┐
│                        Generic Templates                         │
│  (scaffolds/templates/*.md)                                     │
│  - Define patterns for each algorithm category                  │
│  - Used as starting point for new scaffolds                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    Fill in the blanks
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      Specific Scaffolds                          │
│  (scaffolds/NN_category/*.md)                                   │
│  - Concrete scaffolds for specific algorithms                   │
│  - Ready to use with AI assistants                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    User copies to AI
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       AI Assistant                               │
│  - Follows scaffold instructions                                │
│  - Produces step-by-step solutions                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Understanding Scaffold Structure

### Required Sections

Every scaffold MUST have these sections:

```markdown
# [Algorithm Name] Scaffold

## When to Use
[Problem characteristics that indicate this algorithm]

## Scaffold Instructions
[THE MAIN CONTENT - what users copy to AI]

## Worked Example
[Complete example showing the scaffold in action]

## Common Failure Modes
[What goes wrong without scaffolding]
```

### Detailed Section Breakdown

#### Section 1: When to Use

**Purpose:** Help users identify if this scaffold fits their problem

**Must include:**
- Problem characteristics
- Input/output description
- When NOT to use (if applicable)

**Example:**
```markdown
## When to Use

Use BFS (Breadth-First Search) when you need to:
- Find the shortest path in an **unweighted** graph
- Explore all nodes at distance k before distance k+1
- Find the minimum number of steps/hops/moves

**Input:** Graph with nodes and edges (no weights or all weights = 1)
**Output:** Shortest path from start to goal, measured by number of edges

**Do NOT use when:**
- Edges have different weights → Use Dijkstra instead
- You only need to check if a path exists → DFS may be faster
```

#### Section 2: Scaffold Instructions

**Purpose:** The actual template users copy to AI

**Must include these subsections:**

```markdown
## Scaffold Instructions

### 1) Problem Restatement
[Ask AI to restate problem in algorithm terms]

### 2) State Definition
[Define what variables to track]

### 3) Initialization
[Set starting values]

### 4) Algorithm Procedure
[Step-by-step instructions]

### 5) Termination Condition
[When to stop]

### 6) Verification Protocol
[How to check the answer]
```

**Critical rules:**
- Be explicit about EVERY state variable
- Number every step
- Use consistent terminology
- Include format for showing state

#### Section 3: Worked Example

**Purpose:** Show exactly how the scaffold works

**Must include:**
- Concrete problem instance
- Complete solution trace
- Final answer with verification

**Example structure:**
```markdown
## Worked Example

### Problem
Find shortest path from A to D in this graph:
- A connects to B (1 edge)
- A connects to C (1 edge)
- B connects to D (1 edge)
- C connects to D (1 edge)

### Solution Trace

**Initialization:**
- queue = [A]
- visited = {A}
- distance = {A: 0}
- parent = {A: None}

**Iteration 1:**
- Dequeue: A
- Neighbors of A: B, C
- For B: not visited, add to queue, distance[B] = 1
- For C: not visited, add to queue, distance[C] = 1
- queue = [B, C]
- visited = {A, B, C}

[Continue for each iteration...]

### Final Answer
Shortest path: A → B → D
Distance: 2 edges

### Verification
- Path uses valid edges: A-B ✓, B-D ✓
- Each hop counted: 2 hops total ✓
- No shorter path exists: Confirmed by BFS property ✓
```

#### Section 4: Common Failure Modes

**Purpose:** Help users understand what goes wrong without scaffolds

**Must include:**
- At least 3 failure modes
- Why each happens
- How scaffold prevents it

**Example:**
```markdown
## Common Failure Modes

### 1. Not tracking visited nodes
**Without scaffold:** AI revisits nodes, potentially infinite loop
**With scaffold:** Explicit visited set prevents revisits

### 2. Using wrong data structure
**Without scaffold:** AI might use stack (DFS) instead of queue (BFS)
**With scaffold:** Queue explicitly specified

### 3. Forgetting to track parents
**Without scaffold:** AI finds distance but can't reconstruct path
**With scaffold:** Parent tracking built into state definition
```

---

## Creating New Scaffolds

### Step-by-Step Process

#### Step 1: Choose Your Algorithm

1. Identify an algorithm not yet covered
2. Determine which category it belongs to
3. Check if a similar scaffold exists (don't duplicate)

#### Step 2: Research the Algorithm

Understand these aspects:
1. What problem does it solve?
2. What are the inputs and outputs?
3. What state needs to be tracked?
4. What are the key steps?
5. How do you know it's done?
6. How do you verify correctness?

**Good resources:**
- Wikipedia (for overview)
- Algorithm textbooks
- Visualization websites (visualgo.net, etc.)

#### Step 3: Open the Generic Template

1. Go to `scaffolds/templates/`
2. Open the template for your category
3. Read through the entire template
4. Note the fill-in-the-blank sections

#### Step 4: Create Your Scaffold File

1. Create new file in appropriate category folder
2. Name it `algorithm_name.md`
3. Copy the scaffold structure (not the template)

#### Step 5: Fill In Each Section

Work through each section:

**When to Use:**
```markdown
## When to Use

Use [Algorithm Name] when:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

**Input:** [Description]
**Output:** [Description]
```

**Scaffold Instructions:**
Use the generic template as your guide:
1. Copy the core pattern
2. Replace bracketed items with specific values
3. Add algorithm-specific details

**Worked Example:**
1. Create a simple but realistic problem
2. Solve it step by step
3. Show every state change
4. Verify the answer

**Common Failure Modes:**
1. Think about what could go wrong
2. Test without scaffold to see actual failures
3. Document 3+ failure modes

#### Step 6: Test Your Scaffold

See the [Testing Scaffolds](#testing-scaffolds) section below.

#### Step 7: Refine Based on Testing

1. Fix any issues found in testing
2. Clarify confusing instructions
3. Add more detail where AI struggled
4. Simplify overly complex sections

#### Step 8: Update the Index

Add your scaffold to `scaffolds/README.md`:
```markdown
| [Algorithm Name] | `NN_category/algorithm_name.md` | [Brief description] |
```

---

## Using Generic Templates

### Available Templates

| Template | Use For | Location |
|----------|---------|----------|
| Graph Algorithm | BFS, DFS, Dijkstra, etc. | `templates/graph_algorithm_template.md` |
| Divide & Conquer | Binary search, sorting, etc. | `templates/divide_conquer_template.md` |
| Greedy | Activity selection, Huffman, etc. | `templates/greedy_template.md` |
| Backtracking | N-Queens, Sudoku, etc. | `templates/backtracking_template.md` |
| Dynamic Programming | Knapsack, LCS, etc. | `templates/dynamic_programming_template.md` |
| Optimization | Gradient descent, SA, etc. | `templates/optimization_template.md` |
| String Algorithm | KMP, tries, etc. | `templates/string_algorithm_template.md` |
| Numerical Method | Root finding, integration, etc. | `templates/numerical_method_template.md` |

### Template Structure

Each template contains:

1. **Category Definition** - What makes this family unique
2. **Essential State Components** - Required and optional state
3. **Core Pattern** - Fill-in-the-blank scaffold
4. **Derivation Checklist** - Verification before use
5. **Derivation Examples** - How existing scaffolds were made

### How to Use a Template

#### Example: Creating a new graph scaffold

**Step 1:** Open `scaffolds/templates/graph_algorithm_template.md`

**Step 2:** Find the Core Pattern section:
```
# [YOUR_ALGORITHM_NAME] Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Graph type: [DIRECTED/UNDIRECTED]
   - Edge weights: [WEIGHTED/UNWEIGHTED/NEGATIVE_ALLOWED]
   ...
```

**Step 3:** Replace bracketed items:
```
# Prim's MST Scaffold

## Scaffold Instructions

1) Problem Restatement
   - Graph type: UNDIRECTED
   - Edge weights: WEIGHTED (positive)
   ...
```

**Step 4:** Continue filling all sections

**Step 5:** Compare with derivation examples in the template

---

## Testing Scaffolds

### Testing Philosophy

Every scaffold should be tested to ensure:
1. AI follows the instructions
2. Solutions are correct
3. Instructions are clear
4. Edge cases are handled

### Testing Process

#### Step 1: Create Test Cases

Create at least 3 test cases:

| Test Type | Purpose | Example |
|-----------|---------|---------|
| Simple | Basic functionality | 4-node graph |
| Medium | Normal complexity | 8-node graph |
| Edge case | Boundary conditions | Single node, disconnected graph |

#### Step 2: Test with Multiple AIs

Test with at least 2 different AI assistants:
- ChatGPT (GPT-4 or GPT-3.5)
- Claude
- Gemini (optional but helpful)

**Why multiple AIs?** Different models have different strengths. A good scaffold works with all of them.

#### Step 3: Document Results

For each test:
```markdown
### Test: [Name]
**AI:** [ChatGPT/Claude/Gemini]
**Problem:** [Brief description]
**Expected:** [Expected answer]
**Actual:** [AI's answer]
**Followed scaffold:** [Yes/Partially/No]
**Issues:** [Any problems observed]
```

#### Step 4: Iterate

If tests reveal issues:
1. Identify the root cause
2. Modify the scaffold
3. Re-test
4. Repeat until all tests pass

### Testing Checklist

Before finalizing a scaffold:

- [ ] Tested with at least 2 AI assistants
- [ ] Simple case works correctly
- [ ] Medium complexity case works correctly
- [ ] At least one edge case tested
- [ ] AI follows all steps in order
- [ ] AI shows state at each step
- [ ] Final answer is verified
- [ ] No ambiguous instructions

---

## Automated Verification Framework

The project includes a fully automated verification framework that validates scaffolds produce correct results when used with LLMs.

### Current Status (December 2025)

**Verified:** 33 scaffolds
**Certified (100%):** 5 scaffolds (astar, merge_sort, nqueens, subset_sum, topological_sort)
**Partial (≥50%):** 6 scaffolds
**Failed (<50%):** 22 scaffolds

See [VERIFICATION.md](VERIFICATION.md) for detailed status of each scaffold.

### Recent Technical Improvements

The verification framework received significant updates in December 2025:

#### 1. Unicode Encoding Fix (`verification/cli.py`)

**Problem:** Windows cp1252 encoding couldn't handle Unicode symbols.

**Solution:**
```python
# Before (caused UnicodeEncodeError on Windows)
status_symbols = {"pass": "✓", "partial": "◐", "fail": "✗"}

# After (works on all platforms)
status_symbols = {"pass": "[OK]", "partial": "[..]", "fail": "[XX]"}
```

#### 2. MST Validator Fix (`verification/validators/set_equivalence.py`)

**Problem:** MSTValidator was iterating over dict keys instead of edge list.

**Solution:**
```python
# Fixed to handle {"total_weight": N, "edges": [...]} format
if isinstance(actual, dict):
    actual_weight = actual.get("total_weight", 0)
    if actual_weight == 0 and "edges" in actual:
        edges = actual.get("edges", [])
        for edge in edges:
            if isinstance(edge, (list, tuple)) and len(edge) >= 3:
                actual_weight += float(edge[2])
```

**Impact:** Kruskal scaffold improved from 0% to 81.8% pass rate.

#### 3. Activity Selection Parser Fix (`verification/llm/response_parser.py`)

**Problem:** Parser returned extra `activities` field not expected by validator.

**Solution:** Parser now returns only `{"count": N}` to match expected format.

#### 4. Algorithm-Specific Output Formats (`verification/llm/prompt_builder.py`)

Added 12 new output formats to improve LLM response structure:
- `huffman`, `sudoku`, `graph_coloring`, `matrix_chain`
- `trie`, `monte_carlo`, `optimization`, `activity`
- `kruskal`, `fractional_knapsack`, `subset_sum`, `edit_distance`

### Framework Architecture

```
verification/
├── cli.py                 # Command-line interface
├── config.py              # Pydantic settings
├── runner.py              # Test orchestrator
├── registry.py            # Scaffold-to-generator/validator mapping
├── llm/                   # LLM integration
│   ├── base.py           # Abstract LLM interface
│   ├── claude.py         # Claude API implementation
│   ├── prompt_builder.py # Scaffold parser and prompt construction
│   └── response_parser.py # Response parsing
├── reference/             # Ground truth implementations
│   ├── graph.py          # networkx-based
│   ├── divide_conquer.py
│   ├── greedy.py
│   ├── backtracking.py
│   ├── dynamic_programming.py
│   ├── optimization.py
│   ├── string_algo.py
│   └── numerical.py
├── generators/            # Test case generators
│   ├── base.py           # TestCase, TestSuite classes
│   └── graph_gen.py      # Category-specific generators
├── validators/            # Output validators
│   ├── base.py           # Validator ABC
│   ├── exact_match.py
│   ├── numeric_tolerance.py
│   └── set_equivalence.py
└── reports/               # Report generation
    └── generator.py
```

### Running Verification

```bash
# Setup
pip install -r requirements-verification.txt
export ANTHROPIC_API_KEY=your_key_here

# Basic commands
python verify.py list              # List all scaffolds
python verify.py dijkstra          # Verify single scaffold
python verify.py --category graph  # Verify a category
python verify.py                   # Verify ALL scaffolds
python verify.py --mode cert       # Use Opus for certification
```

### How Verification Works

1. **Test Generation**: Creates test cases using reference implementations
2. **Prompt Building**: Combines scaffold + test case into prompt
3. **LLM Execution**: Sends prompt to Claude API
4. **Response Parsing**: Extracts structured answers from LLM response
5. **Validation**: Compares answer against ground truth
6. **Reporting**: Generates markdown certification reports

### Adding a New Scaffold to Verification

When you create a new scaffold, follow these steps to add verification support:

#### Step 1: Add Reference Implementation

Add the algorithm to the appropriate file in `verification/reference/`:

```python
# verification/reference/graph.py
def new_algorithm(vertices: list, edges: list, **params) -> dict:
    """Implement using trusted library (networkx, numpy, scipy)."""
    import networkx as nx

    G = nx.DiGraph()
    G.add_nodes_from(vertices)
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Use library function
    result = nx.some_algorithm(G, **params)

    return {"result_key": result}
```

#### Step 2: Register the Scaffold

Add to `verification/registry.py`:

```python
SCAFFOLD_REGISTRY = {
    "graph": [
        "bfs", "dfs", "dijkstra", "astar",
        "bellman_ford", "floyd_warshall", "topological_sort",
        "new_algorithm"  # Add your scaffold here
    ],
    # ...
}

VALIDATOR_REGISTRY = {
    # ...
    "new_algorithm": "exact_match",  # or "numeric", "set", etc.
}
```

#### Step 3: Add Output Format

Update `verification/llm/prompt_builder.py`:

```python
OUTPUT_FORMATS = {
    # ...
    "new_algorithm": """
OUTPUT FORMAT:
Provide your final answer as:
RESULT: <value>
""",
}
```

#### Step 4: Add Response Parser

Update `verification/llm/response_parser.py`:

```python
class ResponseParser:
    def parse_new_algorithm(self, response: str) -> dict:
        """Parse new_algorithm response."""
        # Extract result from response
        match = re.search(r'RESULT:\s*(.+)', response)
        if match:
            return {"result_key": match.group(1).strip()}
        return {}
```

#### Step 5: Test Your Addition

```bash
# Run verification for your new scaffold
python verify.py new_algorithm

# Check the report
cat verification_results/reports/new_algorithm_report.md
```

### Validator Types

| Validator | Use Case | Example |
|-----------|----------|---------|
| `exact_match` | Exact value match | BFS distances |
| `dict_match` | Dictionary comparison | Dijkstra distances |
| `path_match` | Path comparison | Shortest paths |
| `numeric` | Float with tolerance | Newton-Raphson roots |
| `set` | Unordered set match | MST edges |
| `optimization` | Within % of optimum | Simulated annealing |

### Creating Custom Validators

```python
from verification.validators.base import Validator, ValidationResult

class MyValidator(Validator):
    def validate(self, actual: any, expected: any) -> ValidationResult:
        # Custom validation logic
        is_correct = self._check(actual, expected)

        return ValidationResult(
            is_valid=is_correct,
            message="Validation passed" if is_correct else "Mismatch",
            details={"actual": actual, "expected": expected}
        )
```

### Testing Reference Implementations

```bash
# Run all reference implementation tests
pytest verification/tests/

# Run specific test file
pytest verification/tests/test_reference.py

# Run with verbose output
pytest -v verification/tests/
```

### Cost Management

| Mode | Model | Cost Per Scaffold | All 33 Scaffolds |
|------|-------|------------------|------------------|
| `dev` (default) | Claude Haiku | ~$0.01 | ~$0.30 |
| `cert` | Claude Opus | ~$0.50 | ~$15.00 |

**Best practice:**
- Use `dev` mode for iteration
- Use `cert` mode only for final certification

### Certification Status

| Status | Pass Rate | Meaning |
|--------|-----------|---------|
| CERTIFIED | ≥90% | Scaffold works reliably |
| PARTIAL | 50-89% | Scaffold needs improvement |
| FAILED | <50% | Scaffold has issues |

---

## Style Guidelines

### Markdown Formatting

**Headers:**
```markdown
# Main Title (only one per file)
## Major Section
### Subsection
#### Minor subsection (use sparingly)
```

**Code blocks:**
```markdown
Use triple backticks with language hint:

```python
def example():
    pass
```

For pseudocode, use no language or 'text':

```text
For each item in list:
    Process item
```
```

**Tables:**
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
```

**Lists:**
```markdown
Numbered (for sequential steps):
1. First step
2. Second step
3. Third step

Bulleted (for non-sequential items):
- Item one
- Item two
- Item three
```

### Scaffold Writing Style

**Be explicit:**
```markdown
# Bad - too vague
Update the state

# Good - explicit
Update state:
- distance[neighbor] = distance[current] + edge_weight
- parent[neighbor] = current
- Add neighbor to priority queue with priority = distance[neighbor]
```

**Use consistent terminology:**
```markdown
# Bad - inconsistent
First examine the node, then look at the vertex, then check the point

# Good - consistent
First examine the node, then look at its neighbors, then check each neighbor node
```

**Number all steps:**
```markdown
# Bad - unnumbered
Initialize the queue
While queue is not empty
Process current node

# Good - numbered
1. Initialize: queue = [start_node]
2. While queue is not empty:
   2a. current = dequeue()
   2b. For each neighbor of current:
       2b-i. If not visited: enqueue(neighbor)
```

### Documentation Style

**Use simple language:**
```markdown
# Bad - too technical
The algorithm exhibits O(V + E) time complexity due to adjacency list traversal

# Good - accessible
The algorithm visits each node once and checks each edge once,
so it runs faster on sparse graphs
```

**Include visual aids when helpful:**
```markdown
State after iteration 3:
┌─────────┬──────────┬────────┐
│ Node    │ Distance │ Parent │
├─────────┼──────────┼────────┤
│ A       │ 0        │ None   │
│ B       │ 2        │ A      │
│ C       │ 4        │ A      │
│ D       │ ∞        │ -      │
└─────────┴──────────┴────────┘
```

---

## Common Patterns and Anti-Patterns

### Patterns (Do These)

**Pattern 1: Explicit State Tables**
```markdown
State = (
    current_node,
    visited: set of nodes,
    distances: map from node → number,
    parents: map from node → node
)

Show state as table after each iteration.
```

**Pattern 2: Clear Termination**
```markdown
STOP when:
- Goal node is dequeued (for single-target search), OR
- Queue is empty (all reachable nodes visited)
```

**Pattern 3: Verification Steps**
```markdown
VERIFY by:
1. Trace path using parent pointers: goal → ... → start
2. Sum edge weights along path
3. Confirm sum equals reported distance
```

### Anti-Patterns (Avoid These)

**Anti-Pattern 1: Ambiguous Instructions**
```markdown
# Bad
Process the neighbors appropriately

# Good
For each neighbor N of current node C:
    If N not in visited:
        Calculate new_distance = distances[C] + weight(C, N)
        If new_distance < distances[N]:
            distances[N] = new_distance
            parents[N] = C
```

**Anti-Pattern 2: Missing State Components**
```markdown
# Bad - what if we need the path later?
Track: visited nodes, current node

# Good
Track:
- visited: set of processed nodes
- current: node being processed
- distances: shortest known distance to each node
- parents: previous node on shortest path (for path reconstruction)
```

**Anti-Pattern 3: No Verification**
```markdown
# Bad
Return the answer

# Good
Return the answer and verify:
1. Check all constraints are satisfied
2. Trace through solution step by step
3. Confirm no better solution exists (for optimization)
```

---

## Contributing to the Project

### Types of Contributions

1. **New scaffolds** - Add algorithms not yet covered
2. **Improvements** - Better explanations, more examples
3. **Bug fixes** - Correct errors in existing scaffolds
4. **Documentation** - Improve guides and explanations
5. **Testing** - Test scaffolds with different AIs

### Contribution Process

#### Step 1: Identify What to Contribute

- Check existing scaffolds for gaps
- Look at the algorithm list in `scaffolds/README.md`
- Consider algorithms you use frequently

#### Step 2: Create Your Contribution

Follow the guidelines in this document:
- Use templates for new scaffolds
- Follow style guidelines
- Test thoroughly

#### Step 3: Self-Review Checklist

Before submitting:

- [ ] Follows project structure
- [ ] Uses consistent formatting
- [ ] Tested with multiple AIs
- [ ] Worked example is complete
- [ ] Failure modes documented
- [ ] Index updated (if new scaffold)

#### Step 4: Submit

**If using Git:**
1. Fork the repository
2. Create a branch for your changes
3. Commit with clear message
4. Create pull request

**If not using Git:**
1. Prepare your files
2. Contact project maintainers
3. Share your contribution

---

## Maintenance Tasks

### Regular Maintenance

**Monthly:**
- Test 5 random scaffolds with latest AI models
- Update any that fail
- Check for new algorithms to add

**Quarterly:**
- Review and update documentation
- Check for outdated information
- Add new FAQs based on user feedback

### When AI Models Update

When major AI updates occur (e.g., GPT-5, Claude 4):
1. Test all scaffolds with new model
2. Note any that need adjustment
3. Update scaffolds as needed
4. Document any model-specific notes

### Keeping Documentation Current

- Update screenshots if UI changes
- Add new FAQs as questions arise
- Refine explanations based on user feedback
- Keep links working

---

## Troubleshooting Development Issues

### Problem: Can't Figure Out the Algorithm

**Solution:**
1. Search for visualizations online (visualgo.net)
2. Watch YouTube explanations
3. Work through examples by hand
4. Ask for help in discussions

### Problem: Scaffold Is Too Complex

**Solution:**
1. Break into smaller sub-scaffolds
2. Simplify state representation
3. Focus on core algorithm, not optimizations
4. Compare with simpler existing scaffolds

### Problem: AI Doesn't Follow Instructions

**Solution:**
1. Make instructions more explicit
2. Add numbered sub-steps
3. Include "IMPORTANT:" callouts
4. Test exact wording variations

### Problem: Different AIs Give Different Results

**Solution:**
1. Find common denominator instructions
2. Add model-specific notes if needed
3. Simplify ambiguous parts
4. Focus on working with majority of models

### Problem: Worked Example Is Wrong

**Solution:**
1. Verify by hand calculation
2. Use online algorithm visualizers
3. Test with simple cases first
4. Have someone else review

---

## Improving Failing Scaffolds

With only 5 of 33 scaffolds achieving 100% pass rate, there's significant opportunity for improvement.

### Why Scaffolds Fail

Based on verification analysis, LLMs struggle with:

| Challenge | Affected Scaffolds | Symptoms |
|-----------|-------------------|----------|
| **Priority queue management** | dijkstra | Wrong node selected next |
| **Matrix operations** | floyd_warshall, matrix_chain | Index errors, dimension confusion |
| **Greedy choice logic** | activity_selection, fractional_knapsack | Wrong "best" option selected |
| **Tree construction** | huffman, trie | Parent-child relationships lost |
| **Hash calculations** | rabin_karp | Modular arithmetic errors |
| **Convergence criteria** | newton_raphson, bisection | Premature stopping or infinite loops |

### Strategies to Improve Pass Rates

#### 1. Add Explicit State Tables

Before:
```
Track distances and visited nodes.
```

After:
```
After EACH iteration, show this table:
| Node | Distance | Visited | Parent |
|------|----------|---------|--------|
| A    | 0        | Yes     | None   |
| B    | ...      | ...     | ...    |
```

#### 2. Number Every Decision Point

Before:
```
Select the best item using the greedy criterion.
```

After:
```
For item selection:
1. Calculate value-to-weight ratio for EACH remaining item
2. List all ratios in a table: | Item | Value | Weight | Ratio |
3. Select the item with HIGHEST ratio
4. VERIFY: Is this ratio truly the maximum? Double-check.
```

#### 3. Add Verification Checkpoints

Before:
```
Continue until the heap is empty.
```

After:
```
CHECKPOINT after each extraction:
- What node was extracted?
- What is its final distance?
- Is this distance minimal? (Check: no shorter path through unvisited nodes)
- List remaining heap contents
```

#### 4. Break Complex Steps into Sub-Steps

Before:
```
Build the Huffman tree from frequency table.
```

After:
```
Building Huffman tree:
1. Create leaf node for each character with its frequency
2. Insert all leaves into a min-heap ordered by frequency
3. While heap has more than one node:
   a. Extract two nodes with LOWEST frequencies
   b. Create new internal node with frequency = sum
   c. Set extracted nodes as left and right children
   d. Insert new node into heap
   e. SHOW current heap state
4. Remaining node is the root
```

### Testing Your Improvements

```bash
# Test single scaffold before and after changes
python verify.py <scaffold_name>

# Compare results
cat verification_results/reports/<scaffold_name>_report.md

# Run full regression to ensure no breakage
python verify.py --category <category>
```

### Key Files for Scaffold Improvements

| File | Purpose | When to Modify |
|------|---------|----------------|
| `scaffolds/NN_category/<name>.md` | Scaffold content | Always - primary improvement target |
| `verification/llm/prompt_builder.py` | Output format instructions | When LLM output structure needs changing |
| `verification/llm/response_parser.py` | Response parsing | When LLM output format changes |
| `verification/registry.py` | Validator mappings | When validator type needs changing |

---

## Summary

You now have comprehensive knowledge to:
- Understand the project architecture
- Create new scaffolds using templates
- Test scaffolds effectively
- Follow project conventions
- Contribute to the project
- **Improve failing scaffolds using targeted strategies**

### Priority Improvement Targets

Based on current verification results, these scaffolds have the most potential for improvement:

| Scaffold | Current Rate | Likely Fix |
|----------|-------------|------------|
| quickselect | 36.4% | Better partition tracking |
| sudoku | 27.3% | More explicit constraint checking |
| dijkstra | 27.3% | Priority queue state tables |
| lis | 9.1% | Clearer DP state transitions |
| huffman | 9.1% | Step-by-step tree construction |

**Your first task:** Pick one scaffold from the improvement targets, analyze its failure report, and propose specific improvements.

**Questions?** Check the [FAQ](FAQ.md) or ask in project discussions.
