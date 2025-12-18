# Scaffold Verification Report: dijkstra

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:24
- **Pass Rate:** 27.3% (3/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] dijkstra_simple_01: Test case dijkstra_simple_01

- [PASS] dijkstra_simple_02: Test case dijkstra_simple_02

- [FAIL] dijkstra_simple_03: Test case dijkstra_simple_03


### Standard Cases

- [FAIL] dijkstra_standard_01: Test case dijkstra_standard_01

- [FAIL] dijkstra_standard_02: Test case dijkstra_standard_02

- [FAIL] dijkstra_standard_03: Test case dijkstra_standard_03

- [FAIL] dijkstra_standard_04: Test case dijkstra_standard_04

- [FAIL] dijkstra_standard_05: Test case dijkstra_standard_05


### Edge Cases

- [FAIL] dijkstra_edge_01: Test case dijkstra_edge_01

- [PASS] dijkstra_edge_02: Test case dijkstra_edge_02

- [PASS] dijkstra_edge_03: Test case dijkstra_edge_03


## Failure Analysis



### dijkstra_simple_01
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 2, 'C': 3, 'D': 8}, {'A': 5, 'B': 2, 'C': 3, 'D': 8})]
- **Expected:** {'distances': {'A': 0, 'B': 2, 'C': 3, 'D': 8}}
- **Actual:** N/A





### dijkstra_simple_03
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 10, 'C': 19, 'D': 28}, {'A': 0, 'B': 10, 'C': 11, 'D': 20})]
- **Expected:** {'distances': {'A': 0, 'B': 10, 'C': 19, 'D': 28}}
- **Actual:** N/A



### dijkstra_standard_01
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 1, 'D': 2, 'C': 3, 'E': 8, 'G': 13, 'F': 13}, {'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 8, 'F': 13, 'G': 12})]
- **Expected:** {'distances': {'A': 0, 'B': 1, 'D': 2, 'C': 3, 'E': 8, 'G': 13, 'F': 13}}
- **Actual:** N/A



### dijkstra_standard_02
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 1, 'F': 3, 'G': 5, 'C': 9, 'D': 18, 'E': 20}, {'A': 0, 'B': 1, 'C': 9, 'D': 12, 'E': 10, 'F': 3, 'G': 5})]
- **Expected:** {'distances': {'A': 0, 'B': 1, 'F': 3, 'G': 5, 'C': 9, 'D': 18, 'E': 20}}
- **Actual:** N/A



### dijkstra_standard_03
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 4, 'D': 5, 'C': 8, 'E': 9}, {'A': 0, 'B': 4, 'C': 8, 'D': 5, 'E': 12})]
- **Expected:** {'distances': {'A': 0, 'B': 4, 'D': 5, 'C': 8, 'E': 9}}
- **Actual:** N/A



### dijkstra_standard_04
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 6, 'C': 10, 'D': 13, 'E': 15, 'F': 19, 'G': 22}, {'A': 0, 'B': 6, 'C': 10, 'D': 9, 'E': 11, 'F': 15, 'G': 18})]
- **Expected:** {'distances': {'A': 0, 'B': 6, 'C': 10, 'D': 13, 'E': 15, 'F': 19, 'G': 22}}
- **Actual:** N/A



### dijkstra_standard_05
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 6, 'C': 7, 'D': 11, 'E': 12, 'F': 18}, {'A': 0, 'B': 6, 'C': 7, 'D': 9, 'E': 10, 'F': 16})]
- **Expected:** {'distances': {'A': 0, 'B': 6, 'C': 7, 'D': 11, 'E': 12, 'F': 18}}
- **Actual:** N/A



### dijkstra_edge_01
- **Error:** Value mismatches: [('distances', {'A': 0, 'B': 8, 'C': 11, 'D': 16, 'E': 19, 'F': 23, 'G': 32, 'J': 38, 'H': 41, 'I': 46}, {'A': 0, 'B': 1, 'C': 4, 'D': 9, 'E': 12, 'F': 16, 'G': 8, 'H': 10, 'I': 15, 'J': 31})]
- **Expected:** {'distances': {'A': 0, 'B': 8, 'C': 11, 'D': 16, 'E': 19, 'F': 23, 'G': 32, 'J': 38, 'H': 41, 'I': 46}}
- **Actual:** N/A







---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.889581