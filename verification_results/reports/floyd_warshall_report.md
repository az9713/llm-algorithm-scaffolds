# Scaffold Verification Report: floyd_warshall

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:28
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] floyd_warshall_simple_01: Test case floyd_warshall_simple_01

- [FAIL] floyd_warshall_simple_02: Test case floyd_warshall_simple_02

- [FAIL] floyd_warshall_simple_03: Test case floyd_warshall_simple_03


### Standard Cases

- [FAIL] floyd_warshall_standard_01: Test case floyd_warshall_standard_01

- [FAIL] floyd_warshall_standard_02: Test case floyd_warshall_standard_02

- [FAIL] floyd_warshall_standard_03: Test case floyd_warshall_standard_03

- [FAIL] floyd_warshall_standard_04: Test case floyd_warshall_standard_04

- [FAIL] floyd_warshall_standard_05: Test case floyd_warshall_standard_05


### Edge Cases

- [FAIL] floyd_warshall_edge_01: Test case floyd_warshall_edge_01

- [FAIL] floyd_warshall_edge_02: Test case floyd_warshall_edge_02

- [FAIL] floyd_warshall_edge_03: Test case floyd_warshall_edge_03


## Failure Analysis



### floyd_warshall_simple_01
- **Error:** Failed to parse LLM response: Could not extract distances from response
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 1, 'C': 4}, 'B': {'A': 1, 'B': 0, 'C': 5}, 'C': {'A': 4, 'B': 5, 'C': 0}}}
- **Actual:** N/A



### floyd_warshall_simple_02
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': 9, 'C': 10}, 'B': {'A': 9, 'B': 0, 'C': 1}, 'C': {'A': 10, 'B': 1, 'C': 0}}, {'A': 0, 'B': 0, 'C': 1})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 9, 'C': 10}, 'B': {'A': 9, 'B': 0, 'C': 1}, 'C': {'A': 10, 'B': 1, 'C': 0}}}
- **Actual:** N/A



### floyd_warshall_simple_03
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': inf, 'C': inf}, 'B': {'A': inf, 'B': 0, 'C': 9}, 'C': {'A': inf, 'B': 9, 'C': 0}}, {'A': 0, 'B': 0, 'C': 9})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': inf, 'C': inf}, 'B': {'A': inf, 'B': 0, 'C': 9}, 'C': {'A': inf, 'B': 9, 'C': 0}}}
- **Actual:** N/A



### floyd_warshall_standard_01
- **Error:** Failed to parse LLM response: Could not extract distances from response
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 10, 'C': 9, 'D': 8}, 'B': {'A': 10, 'B': 0, 'C': 1, 'D': 3}, 'C': {'A': 9, 'B': 1, 'C': 0, 'D': 4}, 'D': {'A': 8, 'B': 3, 'C': 4, 'D': 0}}}
- **Actual:** N/A



### floyd_warshall_standard_02
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': inf, 'C': 12, 'D': 2}, 'B': {'A': inf, 'B': 0, 'C': inf, 'D': inf}, 'C': {'A': 12, 'B': inf, 'C': 0, 'D': 10}, 'D': {'A': 2, 'B': inf, 'C': 10, 'D': 0}}, {'A': 2, 'B': 2, 'C': 10, 'D': 0})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': inf, 'C': 12, 'D': 2}, 'B': {'A': inf, 'B': 0, 'C': inf, 'D': inf}, 'C': {'A': 12, 'B': inf, 'C': 0, 'D': 10}, 'D': {'A': 2, 'B': inf, 'C': 10, 'D': 0}}}
- **Actual:** N/A



### floyd_warshall_standard_03
- **Error:** Failed to parse LLM response: Could not extract distances from response
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': inf, 'C': inf, 'D': 2}, 'B': {'A': inf, 'B': 0, 'C': 7, 'D': inf}, 'C': {'A': inf, 'B': 7, 'C': 0, 'D': inf}, 'D': {'A': 2, 'B': inf, 'C': inf, 'D': 0}}}
- **Actual:** N/A



### floyd_warshall_standard_04
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': 6, 'C': 2, 'D': inf}, 'B': {'A': 6, 'B': 0, 'C': 8, 'D': inf}, 'C': {'A': 2, 'B': 8, 'C': 0, 'D': inf}, 'D': {'A': inf, 'B': inf, 'C': inf, 'D': 0}}, {'A': 0, 'B': 6, 'C': 2, 'D': 8})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 6, 'C': 2, 'D': inf}, 'B': {'A': 6, 'B': 0, 'C': 8, 'D': inf}, 'C': {'A': 2, 'B': 8, 'C': 0, 'D': inf}, 'D': {'A': inf, 'B': inf, 'C': inf, 'D': 0}}}
- **Actual:** N/A



### floyd_warshall_standard_05
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': inf, 'C': inf, 'D': inf}, 'B': {'A': inf, 'B': 0, 'C': 6, 'D': 11}, 'C': {'A': inf, 'B': 6, 'C': 0, 'D': 5}, 'D': {'A': inf, 'B': 11, 'C': 5, 'D': 0}}, {'A': 0, 'B': 6, 'C': 11, 'D': 16})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': inf, 'C': inf, 'D': inf}, 'B': {'A': inf, 'B': 0, 'C': 6, 'D': 11}, 'C': {'A': inf, 'B': 6, 'C': 0, 'D': 5}, 'D': {'A': inf, 'B': 11, 'C': 5, 'D': 0}}}
- **Actual:** N/A



### floyd_warshall_edge_01
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': 2}, 'B': {'A': 2, 'B': 0}}, {'A': 0, 'B': 2})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 2}, 'B': {'A': 2, 'B': 0}}}
- **Actual:** N/A



### floyd_warshall_edge_02
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': 3}, 'B': {'A': 3, 'B': 0}}, {'A': 0, 'B': 0})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 3}, 'B': {'A': 3, 'B': 0}}}
- **Actual:** N/A



### floyd_warshall_edge_03
- **Error:** Value mismatches: [('distance_matrix', {'A': {'A': 0, 'B': 4}, 'B': {'A': 4, 'B': 0}}, {'A': 0, 'B': 4})]
- **Expected:** {'distance_matrix': {'A': {'A': 0, 'B': 4}, 'B': {'A': 4, 'B': 0}}}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.891209