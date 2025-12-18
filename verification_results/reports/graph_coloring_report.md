# Scaffold Verification Report: graph_coloring

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:41
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] graph_coloring_simple_01: Test case graph_coloring_simple_01

- [FAIL] graph_coloring_simple_02: Test case graph_coloring_simple_02

- [FAIL] graph_coloring_simple_03: Test case graph_coloring_simple_03


### Standard Cases

- [FAIL] graph_coloring_standard_01: Test case graph_coloring_standard_01

- [FAIL] graph_coloring_standard_02: Test case graph_coloring_standard_02

- [FAIL] graph_coloring_standard_03: Test case graph_coloring_standard_03

- [FAIL] graph_coloring_standard_04: Test case graph_coloring_standard_04

- [FAIL] graph_coloring_standard_05: Test case graph_coloring_standard_05


### Edge Cases

- [FAIL] graph_coloring_edge_01: Test case graph_coloring_edge_01

- [FAIL] graph_coloring_edge_02: Test case graph_coloring_edge_02

- [FAIL] graph_coloring_edge_03: Test case graph_coloring_edge_03


## Failure Analysis



### graph_coloring_simple_01
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 0, 'D': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_simple_02
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 0, 'D': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_simple_03
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 0, 'D': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 1, 'D': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_standard_01
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}, got {'coloring': {'A': 2, 'B': 1, 'C': 3, 'D': 1, 'E': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_standard_02
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}, got {'coloring': {'A': 2, 'B': 1, 'C': 3, 'D': 1, 'E': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_standard_03
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}, got {'coloring': {'A': 2, 'B': 1, 'C': 3, 'D': 1, 'E': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_standard_04
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}, got {'coloring': {'A': 2, 'B': 1, 'C': 3, 'D': 1, 'E': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_standard_05
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}, got {'coloring': {'A': 2, 'B': 1, 'C': 3, 'D': 1, 'E': 1}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2}, 'found': True}
- **Actual:** N/A



### graph_coloring_edge_01
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 2}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}
- **Actual:** N/A



### graph_coloring_edge_02
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 2}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}
- **Actual:** N/A



### graph_coloring_edge_03
- **Error:** Expected {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}, got {'coloring': {'A': 0, 'B': 1, 'C': 2}, 'found': True}
- **Expected:** {'coloring': {'A': 1, 'B': 2, 'C': 3}, 'found': True}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.894590