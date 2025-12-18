"""
Base test case generator interface.
"""

import json
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class TestCase:
    """A single test case for scaffold verification."""

    id: str
    """Unique identifier for this test case."""

    scaffold: str
    """Scaffold name (e.g., 'dijkstra', 'knapsack_01')."""

    tier: str
    """Test tier: 'simple', 'standard', or 'edge'."""

    input: dict[str, Any]
    """Input data for the test case."""

    expected: dict[str, Any]
    """Expected output from the algorithm."""

    description: str = ""
    """Human-readable description of what this tests."""

    metadata: dict[str, Any] = field(default_factory=dict)
    """Additional metadata."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "scaffold": self.scaffold,
            "tier": self.tier,
            "input": self.input,
            "expected": self.expected,
            "description": self.description,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TestCase":
        """Create from dictionary."""
        return cls(
            id=data["id"],
            scaffold=data["scaffold"],
            tier=data["tier"],
            input=data["input"],
            expected=data["expected"],
            description=data.get("description", ""),
            metadata=data.get("metadata", {}),
        )


@dataclass
class TestSuite:
    """Collection of test cases for a scaffold."""

    scaffold: str
    """Scaffold name."""

    version: str = "1.0"
    """Version of the test suite."""

    seed: int = 42
    """Random seed used for generation."""

    generated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    """When the test suite was generated."""

    test_cases: list[TestCase] = field(default_factory=list)
    """List of test cases."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "scaffold": self.scaffold,
            "version": self.version,
            "seed": self.seed,
            "generated_at": self.generated_at,
            "test_cases": [tc.to_dict() for tc in self.test_cases],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TestSuite":
        """Create from dictionary."""
        return cls(
            scaffold=data["scaffold"],
            version=data.get("version", "1.0"),
            seed=data.get("seed", 42),
            generated_at=data.get("generated_at", ""),
            test_cases=[TestCase.from_dict(tc) for tc in data.get("test_cases", [])],
        )

    def save(self, path: Path) -> None:
        """Save to JSON file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, path: Path) -> "TestSuite":
        """Load from JSON file."""
        with open(path, "r", encoding="utf-8") as f:
            return cls.from_dict(json.load(f))


class TestCaseGenerator(ABC):
    """Abstract base class for test case generators."""

    def __init__(self, seed: int = 42):
        """Initialize with random seed."""
        self.seed = seed
        random.seed(seed)

    @property
    @abstractmethod
    def scaffold_name(self) -> str:
        """Return the scaffold this generator is for."""
        pass

    @abstractmethod
    def generate_simple(self, count: int = 3) -> list[TestCase]:
        """Generate simple test cases (small inputs, easy to verify)."""
        pass

    @abstractmethod
    def generate_standard(self, count: int = 5) -> list[TestCase]:
        """Generate standard test cases (moderate complexity)."""
        pass

    @abstractmethod
    def generate_edge_cases(self, count: int = 3) -> list[TestCase]:
        """Generate edge case test cases (boundary conditions)."""
        pass

    def generate_suite(
        self,
        simple_count: int = 3,
        standard_count: int = 5,
        edge_count: int = 3,
    ) -> TestSuite:
        """Generate a complete test suite."""
        random.seed(self.seed)

        test_cases = []
        test_cases.extend(self.generate_simple(simple_count))
        test_cases.extend(self.generate_standard(standard_count))
        test_cases.extend(self.generate_edge_cases(edge_count))

        return TestSuite(
            scaffold=self.scaffold_name,
            seed=self.seed,
            test_cases=test_cases,
        )

    def _make_id(self, tier: str, index: int) -> str:
        """Create a unique test case ID."""
        return f"{self.scaffold_name}_{tier}_{index:02d}"
