# Scaffold Verification Guide

This guide explains how to use the automated verification framework to validate that the algorithm scaffolds produce correct results when used with LLMs.

## Table of Contents

1. [Current Certification Status](#current-certification-status)
2. [Overview](#overview)
3. [Quick Start](#quick-start)
4. [Commands Reference](#commands-reference)
5. [Understanding Results](#understanding-results)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Usage](#advanced-usage)
9. [Known Issues and Future Work](#known-issues-and-future-work)

---

## Current Certification Status

**Last verified:** December 2025
**Model:** Claude 3 Haiku (dev mode)
**Total scaffolds:** 33

### Summary

| Status | Count | Scaffolds |
|--------|-------|-----------|
| **CERTIFIED (100%)** | 5 | astar, merge_sort, nqueens, subset_sum, topological_sort |
| **PARTIAL (≥50%)** | 6 | kruskal (81.8%), bfs (72.7%), binary_search (72.7%), bellman_ford (54.5%), dfs (54.5%), edit_distance (54.5%) |
| **FAILED (<50%)** | 22 | See detailed breakdown below |

### Detailed Status by Category

#### Graph Algorithms (7 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **astar** | 100% | CERTIFIED | Best performing graph algorithm |
| **topological_sort** | 100% | CERTIFIED | Excellent for dependency ordering |
| **bfs** | 72.7% | PARTIAL | Works well for unweighted shortest paths |
| **dfs** | 54.5% | PARTIAL | Good for exploration tasks |
| **bellman_ford** | 54.5% | PARTIAL | Handles negative weights |
| **dijkstra** | 27.3% | FAILED | LLM struggles with priority queue updates |
| **floyd_warshall** | 0% | FAILED | Matrix operations challenging for LLM |

#### Divide & Conquer (3 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **merge_sort** | 100% | CERTIFIED | Excellent for sorting tasks |
| **binary_search** | 72.7% | PARTIAL | Works well for basic searches |
| **quickselect** | 36.4% | FAILED | Partition logic often incorrect |

#### Greedy (4 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **kruskal** | 81.8% | PARTIAL | MST calculations mostly correct |
| **activity_selection** | 0% | FAILED | LLM misinterprets greedy choice |
| **huffman** | 9.1% | FAILED | Tree construction challenging |
| **fractional_knapsack** | 0% | FAILED | Value-to-weight ratio errors |

#### Backtracking (4 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **nqueens** | 100% | CERTIFIED | Best performing puzzle solver |
| **subset_sum** | 100% | CERTIFIED | Excellent constraint satisfaction |
| **sudoku** | 27.3% | FAILED | Complex constraint checking |
| **graph_coloring** | 0% | FAILED | Chromatic number calculations fail |

#### Dynamic Programming (5 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **edit_distance** | 54.5% | PARTIAL | Works for shorter strings |
| **lis** | 9.1% | FAILED | Subsequence tracking issues |
| **knapsack_01** | 0% | FAILED | DP table construction errors |
| **lcs** | 0% | FAILED | Subsequence reconstruction fails |
| **matrix_chain** | 0% | FAILED | Optimal parenthesization complex |

#### Optimization (4 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **gradient_descent** | 0% | FAILED | Numerical precision issues |
| **simulated_annealing** | 0% | FAILED | Temperature/probability calculations |
| **genetic_algorithm** | 0% | FAILED | Complex state management |
| **hill_climbing** | 0% | FAILED | Local optima detection |

#### String (3 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **kmp** | 54.5% | PARTIAL | Failure function often correct |
| **rabin_karp** | 0% | FAILED | Hash calculations problematic |
| **trie_operations** | 0% | FAILED | Tree operations challenging |

#### Numerical (3 scaffolds)

| Scaffold | Pass Rate | Status | Notes |
|----------|-----------|--------|-------|
| **newton_raphson** | 0% | FAILED | Iteration/convergence issues |
| **bisection** | 0% | FAILED | Boundary condition handling |
| **monte_carlo** | 0% | FAILED | Random sampling interpretation |

### Recommendations for Users

**High confidence scaffolds (start here):**
- `astar` - Navigation, pathfinding with heuristics
- `merge_sort` - Sorting data
- `nqueens` - Placement puzzles
- `subset_sum` - Finding combinations that sum to target
- `topological_sort` - Task ordering with dependencies

**Good scaffolds with some limitations:**
- `bfs` - Shortest paths in unweighted graphs
- `binary_search` - Searching sorted data
- `kruskal` - Minimum spanning trees
- `dfs` - Graph exploration
- `edit_distance` - String similarity (shorter strings)

**Use with caution (verify results manually):**
- All other scaffolds may produce incorrect results

---

## Overview

### What is Verification?

The verification framework tests whether scaffolds actually work - that is, whether an LLM using a scaffold produces correct algorithmic results.

### How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    VERIFICATION PIPELINE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. TEST GENERATION                                              │
│     ┌──────────────┐                                            │
│     │ Reference    │  Uses networkx, numpy, scipy to            │
│     │ Implementation│  generate test cases with known answers   │
│     └──────────────┘                                            │
│            ↓                                                     │
│  2. PROMPT BUILDING                                              │
│     ┌──────────────┐                                            │
│     │ Scaffold +   │  Combines scaffold template with            │
│     │ Test Case    │  specific test case input                   │
│     └──────────────┘                                            │
│            ↓                                                     │
│  3. LLM EXECUTION                                                │
│     ┌──────────────┐                                            │
│     │ Claude API   │  Sends prompt to Claude, gets response     │
│     └──────────────┘                                            │
│            ↓                                                     │
│  4. RESPONSE PARSING                                             │
│     ┌──────────────┐                                            │
│     │ Extract      │  Parses structured answer from              │
│     │ Answer       │  LLM's natural language response            │
│     └──────────────┘                                            │
│            ↓                                                     │
│  5. VALIDATION                                                   │
│     ┌──────────────┐                                            │
│     │ Compare      │  Checks if LLM answer matches               │
│     │ Results      │  ground truth from reference impl           │
│     └──────────────┘                                            │
│            ↓                                                     │
│  6. REPORTING                                                    │
│     ┌──────────────┐                                            │
│     │ Generate     │  Creates markdown reports with              │
│     │ Reports      │  pass/fail status and details               │
│     └──────────────┘                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### What Gets Tested

Each scaffold is tested with ~11 test cases:
- **3 Simple cases**: Basic functionality
- **5 Standard cases**: Normal complexity
- **3 Edge cases**: Boundary conditions

---

## Quick Start

### Step 1: Install Dependencies

```bash
pip install -r requirements-verification.txt
```

This installs:
- `anthropic` - Claude API client
- `networkx` - Graph algorithms (ground truth)
- `numpy` - Numerical computations
- `scipy` - Scientific computing
- `pytest` - Testing framework
- Other supporting libraries

### Step 2: Configure API Key

**Option A: Environment Variable (Recommended)**
```bash
# Linux/Mac
export ANTHROPIC_API_KEY=your_key_here

# Windows (Command Prompt)
set ANTHROPIC_API_KEY=your_key_here

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your_key_here"
```

**Option B: Create .env File**
```bash
cp .env.example .env
# Edit .env and add your key:
# VERIFY_ANTHROPIC_API_KEY=your_key_here
```

### Step 3: Run Verification

```bash
# List all available scaffolds
python verify.py list

# Verify a single scaffold (good for testing)
python verify.py dijkstra

# Verify all scaffolds in a category
python verify.py --category graph

# Verify ALL 33 scaffolds
python verify.py

# Use Opus model for final certification
python verify.py --mode cert
```

### Step 4: View Results

Results are saved to `verification_results/`:

```
verification_results/
├── data/                    # Raw JSON results
│   ├── dijkstra.json
│   ├── bfs.json
│   └── ...
└── reports/                 # Human-readable reports
    ├── dijkstra_report.md
    ├── bfs_report.md
    └── CERTIFICATION_SUMMARY.md
```

---

## Commands Reference

### List Scaffolds

```bash
python verify.py list
```

Shows all 33 scaffolds organized by category:
- graph (7): bfs, dfs, dijkstra, astar, bellman_ford, floyd_warshall, topological_sort
- divide_conquer (3): binary_search, merge_sort, quickselect
- greedy (4): activity_selection, huffman, kruskal, fractional_knapsack
- backtracking (4): n_queens, sudoku, graph_coloring, subset_sum
- dynamic_programming (5): knapsack_01, lcs, edit_distance, lis, matrix_chain
- optimization (4): gradient_descent, simulated_annealing, genetic_algorithm, hill_climbing
- string (3): kmp, rabin_karp, trie
- numerical (3): newton_raphson, bisection, monte_carlo

### Verify Specific Scaffold

```bash
python verify.py dijkstra
python verify.py bfs dfs          # Multiple scaffolds
```

### Verify by Category

```bash
python verify.py --category graph
python verify.py --category dynamic_programming
python verify.py --category backtracking
```

### Verify All Scaffolds

```bash
python verify.py                  # All scaffolds, dev mode
python verify.py --mode cert      # All scaffolds, certification mode
```

### Regenerate Reports

```bash
python verify.py report           # Regenerate from existing data
```

---

## Understanding Results

### Certification Status

| Status | Pass Rate | Meaning |
|--------|-----------|---------|
| **CERTIFIED** | ≥90% | Scaffold works reliably. Ready for production use. |
| **PARTIAL** | 50-89% | Scaffold works but has issues. May need refinement. |
| **FAILED** | <50% | Scaffold has significant problems. Needs investigation. |

### Report Structure

Each scaffold report contains:

```markdown
# Dijkstra Verification Report

## Summary
- Status: CERTIFIED
- Pass Rate: 100.0%
- Tests Passed: 11/11

## Test Results

### Simple Cases
| Test ID | Result | Expected | Actual |
|---------|--------|----------|--------|
| dijkstra_simple_01 | PASS | {...} | {...} |

### Standard Cases
[...]

### Edge Cases
[...]

## Failure Analysis
[Only if there are failures]
```

### Interpreting Failures

When a test fails, check:

1. **Expected vs Actual**: Did the LLM get a different answer?
2. **Parsing Issue**: Did the LLM output in unexpected format?
3. **Edge Case**: Is this a boundary condition the scaffold doesn't handle?

---

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | (required) | Your Anthropic API key |
| `VERIFY_ANTHROPIC_API_KEY` | - | Alternative API key variable |
| `VERIFY_DEV_MODEL` | claude-3-haiku-20240307 | Model for dev mode |
| `VERIFY_CERT_MODEL` | claude-3-opus-20240229 | Model for cert mode |
| `VERIFY_CURRENT_MODE` | dev | Default mode (dev/cert) |

### .env File Example

```bash
# Required
VERIFY_ANTHROPIC_API_KEY=sk-ant-api03-...

# Optional overrides
VERIFY_DEV_MODEL=claude-3-haiku-20240307
VERIFY_CERT_MODEL=claude-3-opus-20240229
VERIFY_CURRENT_MODE=dev
```

### Development vs Certification Mode

| Mode | Model | Speed | Cost | Use Case |
|------|-------|-------|------|----------|
| `dev` | Claude Haiku | Fast | ~$0.01/scaffold | Development, iteration |
| `cert` | Claude Opus | Slower | ~$0.50/scaffold | Final certification |

**Recommendation:**
- Use `dev` mode while developing/iterating on scaffolds
- Use `cert` mode only for final certification runs

---

## Troubleshooting

### Common Issues

#### "ANTHROPIC_API_KEY not set"

**Solution:** Set your API key using one of these methods:
```bash
export ANTHROPIC_API_KEY=your_key_here
# OR
echo "VERIFY_ANTHROPIC_API_KEY=your_key" > .env
```

#### Rate Limit Errors

**Solution:** The framework includes automatic retry with exponential backoff. If issues persist:
1. Wait a few minutes
2. Reduce parallel calls by setting `VERIFY_PARALLEL_LLM_CALLS=1` in .env

#### Test Failures

**Solution:**
1. Check the individual scaffold report in `verification_results/reports/`
2. Look at "Expected vs Actual" to understand the discrepancy
3. Consider if it's a parsing issue (output format) vs algorithmic error

#### Module Not Found Errors

**Solution:**
```bash
pip install -r requirements-verification.txt
```

#### Permission Errors

**Solution:** Ensure you have write access to the project directory for results.

### Getting Help

1. Check the report in `verification_results/reports/`
2. Review the raw JSON data in `verification_results/data/`
3. Run with verbose output: `python verify.py dijkstra -v`

---

## Advanced Usage

### Running Tests Programmatically

```python
import asyncio
from verification.runner import VerificationRunner
from verification.registry import get_all_generators, get_validator_for_scaffold

async def verify_scaffold(name: str):
    runner = VerificationRunner()
    generator = get_all_generators()[name]
    validator = get_validator_for_scaffold(name)

    test_suite = generator.generate_suite()
    results = await runner.run_test_suite(name, test_suite, validator)

    print(f"Pass rate: {results.pass_rate * 100:.1f}%")
    return results

asyncio.run(verify_scaffold("dijkstra"))
```

### Custom Test Cases

```python
from verification.generators.base import TestCase, TestSuite

custom_case = TestCase(
    id="custom_01",
    scaffold="dijkstra",
    tier="custom",
    input={
        "vertices": ["A", "B", "C"],
        "edges": [["A", "B", 1], ["B", "C", 2]],
        "source": "A"
    },
    expected={
        "distances": {"A": 0, "B": 1, "C": 3}
    }
)

suite = TestSuite(scaffold="dijkstra", test_cases=[custom_case])
```

### Testing Reference Implementations

```bash
# Run all reference implementation tests
pytest verification/tests/

# Run with verbose output
pytest -v verification/tests/test_reference.py
```

---

## Reference Implementation Libraries

The verification framework uses these trusted libraries as ground truth:

| Category | Library | Notes |
|----------|---------|-------|
| Graph algorithms | networkx | Industry-standard graph library |
| Numerical methods | scipy | Scientific computing |
| General computation | numpy | Array operations |
| DP/Greedy/Backtracking | Custom | Verified implementations |

---

## Estimated Costs

Using default settings (~11 test cases per scaffold):

| Model | Per Scaffold | All 33 Scaffolds |
|-------|-------------|------------------|
| Haiku (dev) | ~$0.01 | ~$0.30 |
| Opus (cert) | ~$0.50 | ~$15.00 |

**Cost-saving tips:**
- Start with single scaffolds: `python verify.py dijkstra`
- Use `--category` to verify incrementally
- Only use `--mode cert` for final certification

---

---

## Known Issues and Future Work

### Technical Improvements Made (December 2025)

The verification framework received significant updates to improve reliability:

1. **Unicode Encoding Fix**
   - **Issue:** Windows cp1252 encoding couldn't handle Unicode symbols (✓, ◐, ✗)
   - **Fix:** Replaced with ASCII equivalents `[OK]`, `[..]`, `[XX]`, `#`, `-`
   - **Impact:** Framework now works reliably on Windows

2. **MST Validator Fix**
   - **Issue:** MSTValidator iterated over dict keys instead of edge list
   - **Fix:** Properly handles `{"total_weight": N, "edges": [...]}` format
   - **Impact:** Kruskal scaffold improved from 0% to 81.8%

3. **Activity Selection Parser Fix**
   - **Issue:** Parser returned extra `activities` field not expected by validator
   - **Fix:** Parser now returns only `{"count": N}` to match expected format
   - **Impact:** Cleaner validation, though LLM still computes wrong values

4. **Validator Mappings Updated**
   - Changed `activity_selection` from "set" to "dict" validator
   - Changed `huffman` from "exact" to "dict" validator
   - **Impact:** Proper comparison of structured outputs

5. **Algorithm-Specific Output Formats**
   - Added 12 new output formats in prompt builder
   - Each scaffold now has a tailored output format
   - **Impact:** Better LLM response structure, easier parsing

### Why Some Scaffolds Fail

Most failures are **LLM algorithmic errors**, not framework issues. Common causes:

| Failure Pattern | Scaffolds Affected | Root Cause |
|-----------------|-------------------|------------|
| **Priority queue mismanagement** | dijkstra, astar (some cases) | LLM loses track of which node to process next |
| **Matrix operations** | floyd_warshall, matrix_chain | LLM struggles with multi-dimensional state |
| **Greedy choice errors** | activity_selection, fractional_knapsack | LLM selects wrong "best" option |
| **Tree construction** | huffman, trie | Building trees from frequency data |
| **Hash calculations** | rabin_karp | Modular arithmetic and rolling hashes |
| **Numerical precision** | newton_raphson, bisection | Convergence criteria and float handling |

### Future Work

#### High Priority
1. **Scaffold improvements for failed algorithms**
   - Add more explicit state tracking
   - Include step-by-step verification prompts
   - Consider breaking complex scaffolds into phases

2. **Better LLM prompting strategies**
   - Experiment with few-shot examples
   - Test chain-of-thought variations
   - Try different output format instructions

3. **Multi-model support**
   - Add GPT-4 integration
   - Add Gemini integration
   - Compare performance across models

#### Medium Priority
4. **Enhanced test case generation**
   - Add more edge cases for failing scaffolds
   - Generate adversarial test cases
   - Add regression tests for fixed issues

5. **Interactive debugging**
   - Step-by-step execution mode
   - Pause and inspect LLM reasoning
   - Manual correction interface

#### Low Priority
6. **Performance optimization**
   - Parallel test execution
   - Caching of common operations
   - Reduced API calls for similar tests

### Contributing to Improvements

If you want to help improve scaffold pass rates:

1. **Analyze failure reports** in `verification_results/reports/`
2. **Identify patterns** in LLM errors
3. **Propose scaffold modifications** that address root causes
4. **Test changes** with `python verify.py <scaffold>`
5. **Submit improvements** with before/after pass rates

---

## Next Steps

- [Developer Guide](DEVELOPER_GUIDE.md#automated-verification-framework) - Adding new scaffolds to verification
- [FAQ](FAQ.md#verification-framework) - Common questions about verification
