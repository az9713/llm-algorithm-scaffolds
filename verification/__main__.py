"""
Entry point for running verification as a module.

Usage:
    python -m verification list
    python -m verification verify
    python -m verification verify dijkstra
    python -m verification report
"""

from .cli import main

if __name__ == "__main__":
    main()
