"""
Pytest configuration and fixtures for verification tests.
"""

import os
from pathlib import Path

import pytest

# Skip LLM tests if no API key
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line(
        "markers", "llm: tests that require LLM API calls"
    )
    config.addinivalue_line(
        "markers", "slow: tests that take a long time to run"
    )


def pytest_collection_modifyitems(config, items):
    """Skip LLM tests if API key not available."""
    if not os.environ.get("ANTHROPIC_API_KEY") and not os.environ.get("VERIFY_ANTHROPIC_API_KEY"):
        skip_llm = pytest.mark.skip(reason="ANTHROPIC_API_KEY not set")
        for item in items:
            if "llm" in item.keywords:
                item.add_marker(skip_llm)


@pytest.fixture
def scaffolds_dir():
    """Get path to scaffolds directory."""
    return Path(__file__).parent.parent.parent / "scaffolds"


@pytest.fixture
def results_dir(tmp_path):
    """Get temporary results directory."""
    return tmp_path / "results"


@pytest.fixture
def test_data_dir():
    """Get path to test data directory."""
    return Path(__file__).parent / "data"
