# CLAUDE.md - Project Context for Claude Code

## Project Overview

**Algorithmic Scaffolding for LLMs** is a collection of structured prompt templates that help Large Language Models (LLMs) solve complex algorithmic problems correctly. The scaffolds provide explicit reasoning structures that guide LLMs through systematic problem-solving.

## Project Purpose

LLMs often fail at planning and systematic search, even when they can execute correct plans. This project addresses that gap by:
1. Providing pre-built scaffolds for 33+ common algorithms
2. Offering 8 generic templates for creating new scaffolds
3. Enabling users to inject algorithmic discipline into their prompts

## Directory Structure

```
algorithmic_scaffolding_discover_ai/
├── CLAUDE.md                    # This file - project context
├── README.md                    # Main project documentation
├── .gitignore                   # Git ignore rules
├── docs/                        # Documentation
│   ├── algorithmic_scaffolding_for_llms.txt  # Original concept examples
│   ├── USER_GUIDE.md           # Comprehensive user documentation
│   ├── DEVELOPER_GUIDE.md      # Developer documentation
│   ├── QUICK_START.md          # Quick start with use cases
│   ├── GLOSSARY.md             # Terms and definitions
│   └── FAQ.md                  # Frequently asked questions
├── scaffolds/                   # All scaffold templates
│   ├── README.md               # Scaffold index and usage
│   ├── templates/              # Generic category templates
│   │   ├── graph_algorithm_template.md
│   │   ├── divide_conquer_template.md
│   │   ├── greedy_template.md
│   │   ├── backtracking_template.md
│   │   ├── dynamic_programming_template.md
│   │   ├── optimization_template.md
│   │   ├── string_algorithm_template.md
│   │   └── numerical_method_template.md
│   ├── 01_graph/               # Graph algorithm scaffolds
│   ├── 02_divide_conquer/      # Divide & conquer scaffolds
│   ├── 03_greedy/              # Greedy algorithm scaffolds
│   ├── 04_backtracking/        # Backtracking scaffolds
│   ├── 05_dynamic_programming/ # DP scaffolds
│   ├── 06_optimization/        # Optimization scaffolds
│   ├── 07_string/              # String algorithm scaffolds
│   └── 08_numerical/           # Numerical method scaffolds
├── verification/               # Automated verification framework
│   ├── __init__.py            # Package init
│   ├── __main__.py            # Module entry point
│   ├── cli.py                 # Command-line interface
│   ├── config.py              # Pydantic settings and configuration
│   ├── runner.py              # Test orchestrator
│   ├── registry.py            # Scaffold-to-generator/validator mapping
│   ├── llm/                   # LLM integration
│   │   ├── base.py           # Abstract LLM interface
│   │   ├── claude.py         # Claude API implementation
│   │   ├── prompt_builder.py # Scaffold parser and prompt construction
│   │   └── response_parser.py # Response parsing and answer extraction
│   ├── reference/             # Ground truth implementations
│   │   ├── graph.py          # networkx-based graph algorithms
│   │   ├── divide_conquer.py # Binary search, merge sort, quickselect
│   │   ├── greedy.py         # Activity selection, Huffman, Kruskal
│   │   ├── backtracking.py   # N-Queens, Sudoku, Graph Coloring
│   │   ├── dynamic_programming.py # Knapsack, LCS, Edit Distance
│   │   ├── optimization.py   # Gradient descent, SA, GA
│   │   ├── string_algo.py    # KMP, Rabin-Karp, Trie
│   │   └── numerical.py      # Newton-Raphson, Bisection, Monte Carlo
│   ├── generators/            # Test case generators
│   │   ├── base.py           # TestCase, TestSuite, TestCaseGenerator
│   │   └── graph_gen.py      # Graph-specific generators
│   ├── validators/            # Output validators
│   │   ├── base.py           # Validator ABC, ValidationResult
│   │   ├── exact_match.py    # ExactMatchValidator, DictMatchValidator
│   │   ├── numeric_tolerance.py # NumericToleranceValidator
│   │   └── set_equivalence.py # SetEquivalenceValidator, MSTValidator
│   ├── reports/               # Report generation
│   │   └── generator.py      # Markdown report generator
│   └── tests/                 # pytest tests
│       ├── conftest.py       # pytest fixtures
│       └── test_reference.py # Reference implementation tests
├── verify.py                   # Main verification entry point
├── requirements-verification.txt # Verification dependencies
├── pytest.ini                  # pytest configuration
├── .env.example               # API key configuration template
└── .ignore/                    # Source materials (not in git)
```

## Key Concepts

### What is a Scaffold?
A scaffold is a structured prompt template with:
1. **State Definition** - What variables to track
2. **Transitions/Actions** - How state changes
3. **Algorithm Procedure** - Step-by-step instructions
4. **Verification** - How to check correctness

### Algorithm Categories
1. **Graph** - BFS, DFS, Dijkstra, A*, etc.
2. **Divide & Conquer** - Binary search, merge sort
3. **Greedy** - Activity selection, Huffman coding
4. **Backtracking** - N-Queens, Sudoku
5. **Dynamic Programming** - Knapsack, LCS
6. **Optimization** - Gradient descent, simulated annealing
7. **String** - KMP, Rabin-Karp, tries
8. **Numerical** - Newton-Raphson, bisection, Monte Carlo

## Verification Status (December 2025)

### Current Results

| Status | Count | Scaffolds |
|--------|-------|-----------|
| **CERTIFIED (100%)** | 5 | astar, merge_sort, nqueens, subset_sum, topological_sort |
| **PARTIAL (50-82%)** | 6 | kruskal (81.8%), bfs (72.7%), binary_search (72.7%), bellman_ford (54.5%), dfs (54.5%), edit_distance (54.5%) |
| **FAILED (<50%)** | 22 | dijkstra, floyd_warshall, activity_selection, huffman, knapsack_01, lcs, and others |

### Why Scaffolds Fail

Most failures are LLM algorithmic errors, not framework issues:

| Failure Pattern | Affected Scaffolds |
|-----------------|-------------------|
| Priority queue management | dijkstra |
| Matrix operations | floyd_warshall, matrix_chain |
| Greedy choice interpretation | activity_selection, fractional_knapsack |
| Tree construction | huffman, trie |
| Hash calculations | rabin_karp |
| Numerical precision | newton_raphson, bisection |

### Technical Improvements Made (December 2025)

1. **Unicode Encoding Fix** (`verification/cli.py`)
   - Windows cp1252 encoding couldn't handle ✓, ◐, ✗
   - Replaced with ASCII: `[OK]`, `[..]`, `[XX]`, `#`, `-`

2. **MST Validator Fix** (`verification/validators/set_equivalence.py`)
   - Was iterating over dict keys instead of edge list
   - Fixed to handle `{"total_weight": N, "edges": [...]}` format
   - Impact: Kruskal improved from 0% to 81.8%

3. **Activity Selection Parser Fix** (`verification/llm/response_parser.py`)
   - Parser returned extra `activities` field
   - Fixed to return only `{"count": N}`

4. **Validator Mappings** (`verification/registry.py`)
   - Changed activity_selection from "set" to "dict"
   - Changed huffman from "exact" to "dict"

5. **Algorithm-Specific Output Formats** (`verification/llm/prompt_builder.py`)
   - Added 12 new formats: huffman, sudoku, graph_coloring, matrix_chain, trie, monte_carlo, optimization, activity, kruskal, fractional_knapsack, subset_sum, edit_distance

## Common Tasks

### Adding a New Scaffold
1. Identify the algorithm category
2. Use the generic template from `scaffolds/templates/`
3. Fill in the blank sections
4. Add worked example
5. Document failure modes
6. Place in appropriate category folder
7. Update `scaffolds/README.md` index

### Modifying Existing Scaffolds
1. Read the scaffold file completely
2. Understand the state definition
3. Make targeted changes
4. Verify worked example still works
5. Update any affected documentation

### Testing Scaffolds (Manual)
1. Copy scaffold to an LLM prompt
2. Add a specific problem instance
3. Verify LLM follows the structure
4. Check solution correctness
5. Note any failure modes

### Testing Scaffolds (Automated)
Use the verification framework for automated testing:
```bash
python verify.py dijkstra          # Test single scaffold
python verify.py --category graph  # Test category
python verify.py                   # Test all scaffolds
```

### Modifying Verification Code
1. Reference implementations in `verification/reference/`
2. Validators in `verification/validators/`
3. Test generators in `verification/generators/`
4. Run `pytest verification/tests/` to test reference implementations

## Code Style Guidelines

### Markdown Files
- Use ATX-style headers (`#`, `##`, `###`)
- Use fenced code blocks with language hints
- Tables should be pipe-delimited
- Keep lines under 100 characters when possible
- Use consistent indentation (4 spaces in code blocks)

### Scaffold Structure
Every scaffold should have:
```markdown
# [Algorithm Name] Scaffold

## When to Use
[Problem characteristics]

## Scaffold Instructions
[The actual scaffold to copy-paste]

## Worked Example
[Complete example with solution trace]

## Common Failure Modes
[What LLMs get wrong without scaffolding]
```

## Build/Test Commands

### Scaffold Usage (No Build Required)
```bash
# Just markdown files - copy to LLM and use
```

### Verification Framework
```bash
# Install verification dependencies
pip install -r requirements-verification.txt

# Set API key
export ANTHROPIC_API_KEY=your_key_here

# Verify scaffolds
python verify.py list              # List all scaffolds
python verify.py dijkstra          # Verify single scaffold
python verify.py --category graph  # Verify a category
python verify.py                   # Verify ALL scaffolds
python verify.py --mode cert       # Use Opus for certification

# Run reference implementation tests
pytest verification/tests/

# Validate markdown syntax (optional)
markdownlint "**/*.md"
```

## Dependencies

### Core Functionality
- None (pure markdown files)

### Verification Framework
```
pytest>=7.0.0
pytest-asyncio>=0.21.0
anthropic>=0.18.0
networkx>=3.0
numpy>=1.24.0
scipy>=1.10.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
jinja2>=3.1.0
tenacity>=8.2.0
python-dotenv>=1.0.0
```

### Optional
- Markdown linter: `npm install -g markdownlint-cli`
- Markdown preview tool (VS Code with Markdown Preview Enhanced)

## Important Files to Know

| File | Purpose |
|------|---------|
| `scaffolds/README.md` | Main index of all scaffolds |
| `scaffolds/templates/*.md` | Generic templates for creating scaffolds |
| `docs/QUICK_START.md` | Best starting point for new users |
| `docs/USER_GUIDE.md` | Complete user documentation |
| `docs/DEVELOPER_GUIDE.md` | Guide for contributors |
| `docs/VERIFICATION.md` | Verification framework user guide |
| `docs/VERIFICATION_API.md` | Verification framework API reference |
| `verify.py` | Main entry point for verification CLI |
| `verification/cli.py` | CLI implementation |
| `verification/registry.py` | Scaffold-to-generator/validator mapping |
| `verification/reference/*.py` | Ground truth algorithm implementations |
| `verification/validators/*.py` | Output validation logic |

## Contribution Workflow

1. Read `docs/DEVELOPER_GUIDE.md`
2. Choose a scaffold to add or improve
3. Follow the template structure
4. Include worked examples
5. Test with actual LLMs
6. Document failure modes
7. Update index files

## Known Limitations

- Scaffolds are prompts, not code - effectiveness varies by LLM
- Only 5 of 33 scaffolds achieve 100% pass rate with Claude 3 Haiku
- Some algorithms may need model-specific adjustments
- Complex problems may need scaffold combinations
- Verification requires Anthropic API key and incurs API costs

## Future Work / Improvement Opportunities

### High Priority Scaffold Improvements

| Scaffold | Current Rate | Improvement Strategy |
|----------|-------------|---------------------|
| quickselect | 36.4% | Better partition state tracking |
| sudoku | 27.3% | More explicit constraint checking |
| dijkstra | 27.3% | Priority queue state tables |
| lis | 9.1% | Clearer DP state transitions |
| huffman | 9.1% | Step-by-step tree construction |

### Strategies to Improve Pass Rates

1. **Add explicit state tables** - Show table after each iteration
2. **Number every decision point** - Break choices into numbered sub-steps
3. **Add verification checkpoints** - Pause to verify correctness mid-algorithm
4. **Break complex steps into sub-steps** - More granular instructions

### Framework Improvements

1. Multi-model support (GPT-4, Gemini)
2. Enhanced test case generation
3. Interactive debugging mode
4. Parallel test execution

## Contact and Resources

- Original concept: Discovery AI research
- Reference video: https://www.youtube.com/watch?v=r5tAzwQuNAo

## Project Creation

This project was built entirely using:

- **Claude Code** - Anthropic's AI-powered CLI coding assistant
- **Claude Opus 4.5** (`claude-opus-4-5-20251101`) - Anthropic's frontier model

All content - 33 algorithm scaffolds, 8 generic templates, comprehensive documentation (USER_GUIDE, DEVELOPER_GUIDE, QUICK_START with 10 examples, GLOSSARY, FAQ), and project structure - was generated through human-AI collaboration using Claude Code.
