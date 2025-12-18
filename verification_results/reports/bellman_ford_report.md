# Scaffold Verification Report: bellman_ford

## Summary

- **Status:** PARTIAL
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:27
- **Pass Rate:** 54.5% (6/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [PASS] bellman_ford_simple_01: Test case bellman_ford_simple_01

- [PASS] bellman_ford_simple_02: Test case bellman_ford_simple_02

- [FAIL] bellman_ford_simple_03: Test case bellman_ford_simple_03


### Standard Cases

- [FAIL] bellman_ford_standard_01: Test case bellman_ford_standard_01

- [FAIL] bellman_ford_standard_02: Test case bellman_ford_standard_02

- [PASS] bellman_ford_standard_03: Test case bellman_ford_standard_03

- [FAIL] bellman_ford_standard_04: Test case bellman_ford_standard_04

- [PASS] bellman_ford_standard_05: Test case bellman_ford_standard_05


### Edge Cases

- [FAIL] bellman_ford_edge_01: Test case bellman_ford_edge_01

- [PASS] bellman_ford_edge_02: Test case bellman_ford_edge_02

- [PASS] bellman_ford_edge_03: Test case bellman_ford_edge_03


## Failure Analysis







### bellman_ford_simple_03
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 10, 'C': 19, 'D': 28}, {'A': 0, 'B': 10, 'C': 11, 'D': 20})]
- **Expected:** {'distances': {'A': 0, 'B': 10, 'C': 19, 'D': 28}}
- **Actual:** N/A



### bellman_ford_standard_01
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 1, 'D': 2, 'C': 3, 'E': 8, 'G': 13, 'F': 13}, {'A': 0, 'B': 1, 'C': 3, 'D': 2, 'E': 16, 'F': 21, 'G': 24})]
- **Expected:** {'distances': {'A': 0, 'B': 1, 'D': 2, 'C': 3, 'E': 8, 'G': 13, 'F': 13}}
- **Actual:** N/A



### bellman_ford_standard_02
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 1, 'F': 3, 'G': 5, 'C': 9, 'D': 18, 'E': 20}, {'A': 0, 'B': 1, 'C': 9, 'D': 18, 'E': 20, 'F': 3, 'G': 29})]
- **Expected:** {'distances': {'A': 0, 'B': 1, 'F': 3, 'G': 5, 'C': 9, 'D': 18, 'E': 20}}
- **Actual:** N/A





### bellman_ford_standard_04
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 6, 'C': 10, 'D': 13, 'E': 15, 'F': 19, 'G': 22}, {'A': 0, 'B': 6, 'C': 10, 'D': 13, 'E': 15, 'F': 19, 'G': 28})]
- **Expected:** {'distances': {'A': 0, 'B': 6, 'C': 10, 'D': 13, 'E': 15, 'F': 19, 'G': 22}}
- **Actual:** N/A





### bellman_ford_edge_01
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 8, 'C': 11, 'D': 16, 'E': 19, 'F': 23, 'G': 32, 'J': 38, 'H': 41, 'I': 46}, {'A': 0, 'B': 8, 'C': 11, 'D': 16, 'E': 19, 'F': 23, 'G': 32, 'H': 41, 'I': 46, 'J': 56})]
- **Expected:** {'distances': {'A': 0, 'B': 8, 'C': 11, 'D': 16, 'E': 19, 'F': 23, 'G': 32, 'J': 38, 'H': 41, 'I': 46}}
- **Actual:** N/A







---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.885180