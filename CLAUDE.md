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

### Testing Scaffolds
1. Copy scaffold to an LLM prompt
2. Add a specific problem instance
3. Verify LLM follows the structure
4. Check solution correctness
5. Note any failure modes

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

This is a documentation-only project with no build system. Testing is manual:

```bash
# No build required - just markdown files

# To validate markdown syntax (optional):
# Install markdownlint: npm install -g markdownlint-cli
markdownlint "**/*.md"

# To preview markdown locally:
# Use VS Code with Markdown Preview Enhanced extension
# Or use any markdown viewer
```

## Dependencies

- None for core functionality (pure markdown)
- Optional: Markdown linter for validation
- Optional: Markdown preview tool

## Important Files to Know

| File | Purpose |
|------|---------|
| `scaffolds/README.md` | Main index of all scaffolds |
| `scaffolds/templates/*.md` | Generic templates for creating scaffolds |
| `docs/QUICK_START.md` | Best starting point for new users |
| `docs/USER_GUIDE.md` | Complete user documentation |
| `docs/DEVELOPER_GUIDE.md` | Guide for contributors |

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
- Some algorithms may need model-specific adjustments
- Complex problems may need scaffold combinations
- No automated testing (manual verification only)

## Contact and Resources

- Original concept: Discovery AI research
- Reference video: https://www.youtube.com/watch?v=r5tAzwQuNAo

## Project Creation

This project was built entirely using:

- **Claude Code** - Anthropic's AI-powered CLI coding assistant
- **Claude Opus 4.5** (`claude-opus-4-5-20251101`) - Anthropic's frontier model

All content - 33 algorithm scaffolds, 8 generic templates, comprehensive documentation (USER_GUIDE, DEVELOPER_GUIDE, QUICK_START with 10 examples, GLOSSARY, FAQ), and project structure - was generated through human-AI collaboration using Claude Code.
