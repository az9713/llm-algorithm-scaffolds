# Verification Framework API Reference

This document provides detailed API documentation for the verification framework. Use this reference when extending the framework or integrating it into other tools.

## Table of Contents

1. [Module Overview](#module-overview)
2. [Core Classes](#core-classes)
3. [LLM Integration](#llm-integration)
4. [Reference Implementations](#reference-implementations)
5. [Generators](#generators)
6. [Validators](#validators)
7. [Registry](#registry)
8. [Configuration](#configuration)
9. [Reports](#reports)

---

## Module Overview

```
verification/
├── __init__.py            # Package initialization
├── __main__.py            # Module entry point (python -m verification)
├── cli.py                 # Command-line interface
├── config.py              # Pydantic settings
├── runner.py              # Test orchestration
├── registry.py            # Scaffold-to-component mapping
├── llm/                   # LLM integration
│   ├── base.py           # Abstract interfaces
│   ├── claude.py         # Claude implementation
│   ├── prompt_builder.py # Prompt construction
│   └── response_parser.py # Response parsing
├── reference/             # Ground truth implementations
├── generators/            # Test case generators
├── validators/            # Output validators
└── reports/               # Report generation
```

---

## Core Classes

### TestCase

Represents a single test case.

```python
from verification.generators.base import TestCase

class TestCase:
    id: str              # Unique identifier (e.g., "dijkstra_simple_01")
    scaffold: str        # Scaffold name (e.g., "dijkstra")
    tier: str            # Test tier: "simple", "standard", "edge"
    input: dict          # Input parameters for the algorithm
    expected: dict       # Expected output (ground truth)
```

**Example:**
```python
test = TestCase(
    id="dijkstra_simple_01",
    scaffold="dijkstra",
    tier="simple",
    input={
        "vertices": ["A", "B", "C"],
        "edges": [["A", "B", 1], ["B", "C", 2]],
        "source": "A"
    },
    expected={
        "distances": {"A": 0, "B": 1, "C": 3}
    }
)
```

### TestSuite

Collection of test cases for a scaffold.

```python
from verification.generators.base import TestSuite

class TestSuite:
    scaffold: str           # Scaffold name
    test_cases: List[TestCase]  # List of test cases
```

**Example:**
```python
suite = TestSuite(
    scaffold="dijkstra",
    test_cases=[test1, test2, test3]
)
```

### TestResult

Result of running a single test case.

```python
from verification.runner import TestResult

class TestResult:
    test_case: TestCase       # The test case that was run
    passed: bool              # Whether the test passed
    actual: dict              # Actual output from LLM
    expected: dict            # Expected output
    llm_response: str         # Raw LLM response
    validation_message: str   # Message from validator
    error: Optional[str]      # Error message if failed
```

### ScaffoldResults

Aggregated results for a scaffold.

```python
from verification.runner import ScaffoldResults

class ScaffoldResults:
    scaffold: str                 # Scaffold name
    results: List[TestResult]     # Individual test results
    pass_rate: float              # Fraction of tests passed (0.0-1.0)
    status: str                   # "CERTIFIED", "PARTIAL", or "FAILED"
```

**Status thresholds:**
- `CERTIFIED`: pass_rate >= 0.90
- `PARTIAL`: 0.50 <= pass_rate < 0.90
- `FAILED`: pass_rate < 0.50

---

## LLM Integration

### LLMProvider (Abstract Base Class)

```python
from verification.llm.base import LLMProvider

class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate a response for the given request."""
        pass

    @abstractmethod
    async def generate_with_retry(
        self, request: LLMRequest, max_retries: int = 3
    ) -> LLMResponse:
        """Generate with automatic retry on failure."""
        pass
```

### LLMRequest

```python
from verification.llm.base import LLMRequest

class LLMRequest:
    prompt: str              # The prompt to send
    model: str               # Model identifier
    max_tokens: int = 4096   # Maximum tokens in response
    temperature: float = 0.0 # Temperature (0.0 for deterministic)
```

### LLMResponse

```python
from verification.llm.base import LLMResponse

class LLMResponse:
    content: str             # The response text
    model: str               # Model used
    usage: dict              # Token usage statistics
```

### ClaudeProvider

Claude API implementation.

```python
from verification.llm.claude import ClaudeProvider

provider = ClaudeProvider(api_key="sk-ant-...")
response = await provider.generate(request)
```

**Key Methods:**
- `generate(request)` - Single generation
- `generate_with_retry(request, max_retries=3)` - With exponential backoff

### PromptBuilder

Constructs prompts from scaffolds and test cases.

```python
from verification.llm.prompt_builder import PromptBuilder

builder = PromptBuilder(scaffolds_dir="scaffolds/")

# Build a prompt
prompt = builder.build_prompt(
    scaffold_name="dijkstra",
    test_input={
        "vertices": ["A", "B", "C"],
        "edges": [["A", "B", 1], ["B", "C", 2]],
        "source": "A"
    }
)
```

**Key Methods:**
- `build_prompt(scaffold_name, test_input)` - Build complete prompt
- `get_scaffold_content(scaffold_name)` - Get raw scaffold markdown
- `format_input(scaffold_name, test_input)` - Format test input

### ScaffoldParser

Parses scaffold markdown files.

```python
from verification.llm.prompt_builder import ScaffoldParser

parser = ScaffoldParser()
sections = parser.parse(markdown_content)
# Returns dict with keys: "when_to_use", "scaffold_instructions", "worked_example", etc.
```

### ResponseParser

Extracts structured answers from LLM responses.

```python
from verification.llm.response_parser import ResponseParser

parser = ResponseParser()
result = parser.parse(scaffold_name="dijkstra", response=llm_response)
# Returns dict like {"distances": {"A": 0, "B": 1, "C": 3}}
```

**Scaffold-specific parsing methods:**
- `parse_dijkstra(response)` - Parse Dijkstra output
- `parse_bfs(response)` - Parse BFS output
- `parse_knapsack(response)` - Parse Knapsack output
- ... (one for each scaffold type)

---

## Reference Implementations

### Graph Algorithms

```python
from verification.reference.graph import (
    bfs,
    dfs,
    dijkstra,
    astar,
    bellman_ford,
    floyd_warshall,
    topological_sort
)

# Dijkstra example
result = dijkstra(
    vertices=["A", "B", "C", "D"],
    edges=[["A", "B", 1], ["B", "C", 2], ["A", "C", 4]],
    source="A"
)
# Returns: {"distances": {"A": 0, "B": 1, "C": 3, "D": inf}}

# BFS example
result = bfs(
    vertices=["A", "B", "C"],
    edges=[["A", "B"], ["B", "C"]],
    source="A"
)
# Returns: {"distances": {"A": 0, "B": 1, "C": 2}}
```

### Divide and Conquer

```python
from verification.reference.divide_conquer import (
    binary_search,
    merge_sort,
    quickselect
)

# Binary search
result = binary_search(array=[1, 3, 5, 7, 9], target=5)
# Returns: {"index": 2, "found": True}

# Merge sort
result = merge_sort(array=[3, 1, 4, 1, 5])
# Returns: {"sorted": [1, 1, 3, 4, 5]}
```

### Greedy Algorithms

```python
from verification.reference.greedy import (
    activity_selection,
    huffman_coding,
    kruskal_mst,
    fractional_knapsack
)

# Activity selection
result = activity_selection(
    activities=[(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10)]
)
# Returns: {"selected": [(1, 4), (5, 7), (6, 10)], "count": 3}
```

### Backtracking

```python
from verification.reference.backtracking import (
    n_queens,
    solve_sudoku,
    graph_coloring,
    subset_sum
)

# N-Queens
result = n_queens(n=4)
# Returns: {"solutions": [[1, 3, 0, 2], ...], "count": 2}

# Sudoku
result = solve_sudoku(grid=[[5,3,0,...], ...])
# Returns: {"solution": [[5,3,4,...], ...], "solvable": True}
```

### Dynamic Programming

```python
from verification.reference.dynamic_programming import (
    knapsack_01,
    longest_common_subsequence,
    edit_distance,
    longest_increasing_subsequence,
    matrix_chain_multiplication
)

# 0/1 Knapsack
result = knapsack_01(
    weights=[10, 20, 30],
    values=[60, 100, 120],
    capacity=50
)
# Returns: {"max_value": 220, "selected_items": [0, 2]}
```

### Optimization

```python
from verification.reference.optimization import (
    gradient_descent,
    simulated_annealing,
    genetic_algorithm,
    hill_climbing
)

# Gradient descent
result = gradient_descent(
    f=lambda x: x**2,
    df=lambda x: 2*x,
    x0=5.0,
    learning_rate=0.1
)
# Returns: {"minimum": 0.0, "iterations": 50}
```

### String Algorithms

```python
from verification.reference.string_algo import (
    kmp_search,
    rabin_karp,
    trie_operations
)

# KMP search
result = kmp_search(text="AABAACAADAABAAABAA", pattern="AABA")
# Returns: {"positions": [0, 9, 13]}
```

### Numerical Methods

```python
from verification.reference.numerical import (
    newton_raphson,
    bisection,
    monte_carlo_integration
)

# Newton-Raphson
result = newton_raphson(
    f=lambda x: x**2 - 2,
    df=lambda x: 2*x,
    x0=1.0
)
# Returns: {"root": 1.414..., "iterations": 5}
```

---

## Generators

### TestCaseGenerator (Abstract Base Class)

```python
from verification.generators.base import TestCaseGenerator

class TestCaseGenerator(ABC):
    scaffold: str  # Name of the scaffold

    @abstractmethod
    def generate_simple(self) -> List[TestCase]:
        """Generate simple test cases."""
        pass

    @abstractmethod
    def generate_standard(self) -> List[TestCase]:
        """Generate standard complexity test cases."""
        pass

    @abstractmethod
    def generate_edge_cases(self) -> List[TestCase]:
        """Generate edge case test cases."""
        pass

    def generate_suite(self) -> TestSuite:
        """Generate complete test suite."""
        cases = (
            self.generate_simple() +
            self.generate_standard() +
            self.generate_edge_cases()
        )
        return TestSuite(scaffold=self.scaffold, test_cases=cases)
```

### UniversalGenerator

Auto-generates test cases using reference implementations.

```python
from verification.registry import UniversalGenerator

generator = UniversalGenerator(scaffold_name="dijkstra")
suite = generator.generate_suite()
```

---

## Validators

### Validator (Abstract Base Class)

```python
from verification.validators.base import Validator, ValidationResult

class ValidationResult:
    is_valid: bool           # Whether validation passed
    message: str             # Human-readable message
    details: dict            # Additional details

class Validator(ABC):
    @abstractmethod
    def validate(self, actual: Any, expected: Any) -> ValidationResult:
        """Validate actual output against expected."""
        pass
```

### ExactMatchValidator

For exact value comparisons.

```python
from verification.validators.exact_match import ExactMatchValidator

validator = ExactMatchValidator()
result = validator.validate(actual=5, expected=5)
# result.is_valid == True
```

### DictMatchValidator

For dictionary comparisons with flexible key matching.

```python
from verification.validators.exact_match import DictMatchValidator

validator = DictMatchValidator()
result = validator.validate(
    actual={"A": 0, "B": 1},
    expected={"A": 0, "B": 1}
)
```

### PathMatchValidator

For path comparisons (order-sensitive).

```python
from verification.validators.exact_match import PathMatchValidator

validator = PathMatchValidator()
result = validator.validate(
    actual=["A", "B", "C"],
    expected=["A", "B", "C"]
)
```

### NumericToleranceValidator

For floating-point comparisons with tolerance.

```python
from verification.validators.numeric_tolerance import NumericToleranceValidator

validator = NumericToleranceValidator(tolerance=1e-6)
result = validator.validate(actual=1.4142135, expected=1.4142136)
# result.is_valid == True (within tolerance)
```

### SetEquivalenceValidator

For unordered set comparisons.

```python
from verification.validators.set_equivalence import SetEquivalenceValidator

validator = SetEquivalenceValidator()
result = validator.validate(
    actual={1, 2, 3},
    expected={3, 1, 2}
)
# result.is_valid == True (same elements)
```

### MSTValidator

For Minimum Spanning Tree validation.

```python
from verification.validators.set_equivalence import MSTValidator

validator = MSTValidator()
result = validator.validate(
    actual={"edges": [("A", "B"), ("B", "C")], "total_weight": 5},
    expected={"edges": [("B", "C"), ("A", "B")], "total_weight": 5}
)
```

### CompositeValidator

Combines multiple validators.

```python
from verification.validators.base import CompositeValidator

validator = CompositeValidator([
    DictMatchValidator(),
    NumericToleranceValidator(tolerance=0.01)
])
```

---

## Registry

The registry maps scaffolds to their generators and validators.

### SCAFFOLD_REGISTRY

```python
from verification.registry import SCAFFOLD_REGISTRY

# Dict[str, List[str]] - category -> scaffold names
SCAFFOLD_REGISTRY = {
    "graph": ["bfs", "dfs", "dijkstra", "astar", "bellman_ford", "floyd_warshall", "topological_sort"],
    "divide_conquer": ["binary_search", "merge_sort", "quickselect"],
    "greedy": ["activity_selection", "huffman", "kruskal", "fractional_knapsack"],
    "backtracking": ["n_queens", "sudoku", "graph_coloring", "subset_sum"],
    "dynamic_programming": ["knapsack_01", "lcs", "edit_distance", "lis", "matrix_chain"],
    "optimization": ["gradient_descent", "simulated_annealing", "genetic_algorithm", "hill_climbing"],
    "string": ["kmp", "rabin_karp", "trie"],
    "numerical": ["newton_raphson", "bisection", "monte_carlo"]
}
```

### VALIDATOR_REGISTRY

```python
from verification.registry import VALIDATOR_REGISTRY

# Dict[str, str] - scaffold -> validator type
VALIDATOR_REGISTRY = {
    "dijkstra": "dict_match",
    "bfs": "dict_match",
    "kruskal": "mst",
    "newton_raphson": "numeric",
    # ...
}
```

### Factory Functions

```python
from verification.registry import (
    get_all_generators,
    get_validator_for_scaffold,
    get_scaffolds_by_category
)

# Get all generators
generators = get_all_generators()
# Returns Dict[str, TestCaseGenerator]

# Get validator for a scaffold
validator = get_validator_for_scaffold("dijkstra")
# Returns Validator instance

# Get scaffolds in a category
scaffolds = get_scaffolds_by_category("graph")
# Returns ["bfs", "dfs", "dijkstra", ...]
```

---

## Configuration

### VerificationSettings

Pydantic settings class for configuration.

```python
from verification.config import VerificationSettings

settings = VerificationSettings()

# Access settings
settings.anthropic_api_key  # API key
settings.dev_model          # Model for dev mode
settings.cert_model         # Model for cert mode
settings.current_mode       # "dev" or "cert"
settings.results_dir        # Output directory
settings.scaffolds_dir      # Scaffolds directory
```

**Environment Variables:**
- `ANTHROPIC_API_KEY` or `VERIFY_ANTHROPIC_API_KEY`
- `VERIFY_DEV_MODEL`
- `VERIFY_CERT_MODEL`
- `VERIFY_CURRENT_MODE`

---

## Reports

### ReportGenerator

Generates markdown certification reports.

```python
from verification.reports.generator import ReportGenerator

generator = ReportGenerator(output_dir="verification_results/reports")

# Generate single scaffold report
generator.generate_scaffold_report(scaffold_results)

# Generate summary report
generator.generate_summary_report(all_results)
```

### Report Templates

Reports use Jinja2 templates:

```python
SCAFFOLD_REPORT_TEMPLATE = """
# {{ scaffold }} Verification Report

## Summary
- Status: {{ status }}
- Pass Rate: {{ pass_rate }}%
- Tests Passed: {{ passed }}/{{ total }}

## Test Results
{% for result in results %}
- {{ result.test_case.id }}: {{ "PASS" if result.passed else "FAIL" }}
{% endfor %}
"""
```

---

## VerificationRunner

Main orchestrator for running verification.

```python
from verification.runner import VerificationRunner, run_verification

# Async usage
runner = VerificationRunner()
results = await runner.run_test_suite(
    scaffold_name="dijkstra",
    test_suite=suite,
    validator=validator
)

# Sync wrapper
results = run_verification(
    scaffold_names=["dijkstra", "bfs"],
    mode="dev"
)
```

**Key Methods:**
- `run_test_suite(scaffold_name, test_suite, validator)` - Run tests for one scaffold
- `run_single_test(test_case, validator)` - Run single test case

---

## CLI Module

### VerificationCLI

Command-line interface class.

```python
from verification.cli import VerificationCLI, main

cli = VerificationCLI()
cli.list_scaffolds()           # List all scaffolds
cli.verify(["dijkstra"])       # Verify specific scaffolds
cli.verify_category("graph")   # Verify category
cli.generate_reports()         # Generate reports

# Entry point
main()  # Parses sys.argv and runs commands
```

---

## Error Handling

### Custom Exceptions

```python
from verification.llm.base import (
    LLMError,
    RateLimitError,
    AuthenticationError
)

try:
    response = await provider.generate(request)
except RateLimitError:
    # Handle rate limiting
    await asyncio.sleep(60)
except AuthenticationError:
    # Handle auth failure
    print("Invalid API key")
except LLMError as e:
    # Handle other LLM errors
    print(f"LLM error: {e}")
```

---

## Usage Examples

### Complete Verification Flow

```python
import asyncio
from verification.runner import VerificationRunner
from verification.registry import get_all_generators, get_validator_for_scaffold
from verification.reports.generator import ReportGenerator

async def verify_all():
    runner = VerificationRunner()
    generators = get_all_generators()
    report_gen = ReportGenerator()

    all_results = []

    for scaffold_name, generator in generators.items():
        validator = get_validator_for_scaffold(scaffold_name)
        suite = generator.generate_suite()
        results = await runner.run_test_suite(scaffold_name, suite, validator)

        all_results.append(results)
        report_gen.generate_scaffold_report(results)

    report_gen.generate_summary_report(all_results)

asyncio.run(verify_all())
```

### Custom Validation

```python
from verification.validators.base import Validator, ValidationResult

class MyCustomValidator(Validator):
    def __init__(self, tolerance: float = 0.1):
        self.tolerance = tolerance

    def validate(self, actual: dict, expected: dict) -> ValidationResult:
        # Custom validation logic
        if abs(actual["value"] - expected["value"]) <= self.tolerance:
            return ValidationResult(
                is_valid=True,
                message="Within tolerance",
                details={"difference": abs(actual["value"] - expected["value"])}
            )
        return ValidationResult(
            is_valid=False,
            message="Outside tolerance",
            details={"actual": actual, "expected": expected}
        )
```

---

## See Also

- [Verification Guide](VERIFICATION.md) - User documentation
- [Developer Guide](DEVELOPER_GUIDE.md#automated-verification-framework) - Adding scaffolds
- [FAQ](FAQ.md#verification) - Common questions
