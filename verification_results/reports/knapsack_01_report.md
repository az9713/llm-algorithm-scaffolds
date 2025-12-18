# Scaffold Verification Report: knapsack_01

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:43
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] knapsack_01_simple_01: Test case knapsack_01_simple_01

- [FAIL] knapsack_01_simple_02: Test case knapsack_01_simple_02

- [FAIL] knapsack_01_simple_03: Test case knapsack_01_simple_03


### Standard Cases

- [FAIL] knapsack_01_standard_01: Test case knapsack_01_standard_01

- [FAIL] knapsack_01_standard_02: Test case knapsack_01_standard_02

- [FAIL] knapsack_01_standard_03: Test case knapsack_01_standard_03

- [FAIL] knapsack_01_standard_04: Test case knapsack_01_standard_04

- [FAIL] knapsack_01_standard_05: Test case knapsack_01_standard_05


### Edge Cases

- [FAIL] knapsack_01_edge_01: Test case knapsack_01_edge_01

- [FAIL] knapsack_01_edge_02: Test case knapsack_01_edge_02

- [FAIL] knapsack_01_edge_03: Test case knapsack_01_edge_03


## Failure Analysis



### knapsack_01_simple_01
- **Error:** Value mismatches: [('value', 9, 13), ('items', [1, 2], [1, 3])]
- **Expected:** {'value': 9, 'items': [1, 2]}
- **Actual:** N/A



### knapsack_01_simple_02
- **Error:** Value mismatches: [('value', 9, 13), ('items', [1, 2], [1, 3])]
- **Expected:** {'value': 9, 'items': [1, 2]}
- **Actual:** N/A



### knapsack_01_simple_03
- **Error:** Value mismatches: [('value', 9, 12), ('items', [1, 2], [1, 3, 4])]
- **Expected:** {'value': 9, 'items': [1, 2]}
- **Actual:** N/A



### knapsack_01_standard_01
- **Error:** Value mismatches: [('value', 18, 17), ('items', [0, 1, 3], [1, 3])]
- **Expected:** {'value': 18, 'items': [0, 1, 3]}
- **Actual:** N/A



### knapsack_01_standard_02
- **Error:** Value mismatches: [('value', 59, 14), ('items', [0, 5, 6, 7], [0])]
- **Expected:** {'value': 59, 'items': [0, 5, 6, 7]}
- **Actual:** N/A



### knapsack_01_standard_03
- **Error:** Value mismatches: [('value', 34, 11), ('items', [2, 3, 4], [1, 2, 3])]
- **Expected:** {'value': 34, 'items': [2, 3, 4]}
- **Actual:** N/A



### knapsack_01_standard_04
- **Error:** Value mismatches: [('value', 56, 21), ('items', [0, 1, 2, 4], [1, 3])]
- **Expected:** {'value': 56, 'items': [0, 1, 2, 4]}
- **Actual:** N/A



### knapsack_01_standard_05
- **Error:** Value mismatches: [('value', 37, 29), ('items', [0, 1, 2, 4], [0, 5])]
- **Expected:** {'value': 37, 'items': [0, 1, 2, 4]}
- **Actual:** N/A



### knapsack_01_edge_01
- **Error:** Value mismatches: [('items', [1, 2, 4], [2, 4, 6])]
- **Expected:** {'value': 33, 'items': [1, 2, 4]}
- **Actual:** N/A



### knapsack_01_edge_02
- **Error:** Value mismatches: [('value', 46, 20), ('items', [0, 1, 2, 3], [0, 1, 3, 6])]
- **Expected:** {'value': 46, 'items': [0, 1, 2, 3]}
- **Actual:** N/A



### knapsack_01_edge_03
- **Error:** Value mismatches: [('value', 38, 49), ('items', [0, 1, 4], [0, 2, 3, 4])]
- **Expected:** {'value': 38, 'items': [0, 1, 4]}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.897316