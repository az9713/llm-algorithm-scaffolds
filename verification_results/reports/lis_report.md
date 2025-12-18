# Scaffold Verification Report: lis

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:46
- **Pass Rate:** 9.1% (1/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [PASS] lis_simple_01: Test case lis_simple_01

- [FAIL] lis_simple_02: Test case lis_simple_02

- [FAIL] lis_simple_03: Test case lis_simple_03


### Standard Cases

- [FAIL] lis_standard_01: Test case lis_standard_01

- [FAIL] lis_standard_02: Test case lis_standard_02

- [FAIL] lis_standard_03: Test case lis_standard_03

- [FAIL] lis_standard_04: Test case lis_standard_04

- [FAIL] lis_standard_05: Test case lis_standard_05


### Edge Cases

- [FAIL] lis_edge_01: Test case lis_edge_01

- [FAIL] lis_edge_02: Test case lis_edge_02

- [FAIL] lis_edge_03: Test case lis_edge_03


## Failure Analysis





### lis_simple_02
- **Error:** Value mismatches: [('sequence', [10, 22, 33, 41, 60, 80], [10, 22, 33, 50, 60, 80])]
- **Expected:** {'length': 6, 'sequence': [10, 22, 33, 41, 60, 80]}
- **Actual:** N/A



### lis_simple_03
- **Error:** Value mismatches: [('sequence', [10, 22, 33, 41, 60, 80], [10, 22, 33, 50, 60, 80])]
- **Expected:** {'length': 6, 'sequence': [10, 22, 33, 41, 60, 80]}
- **Actual:** N/A



### lis_standard_01
- **Error:** Value mismatches: [('sequence', [4, 14, 87, 95], [4, 18, 36, 95])]
- **Expected:** {'length': 4, 'sequence': [4, 14, 87, 95]}
- **Actual:** N/A



### lis_standard_02
- **Error:** Value mismatches: [('sequence', [4, 12, 28, 30, 65, 78], [70, 12, 28, 30, 65, 78])]
- **Expected:** {'length': 6, 'sequence': [4, 12, 28, 30, 65, 78]}
- **Actual:** N/A



### lis_standard_03
- **Error:** Value mismatches: [('sequence', [26, 29, 58, 76], [76, 58, 26, 1])]
- **Expected:** {'length': 4, 'sequence': [26, 29, 58, 76]}
- **Actual:** N/A



### lis_standard_04
- **Error:** Value mismatches: [('sequence', [20, 28, 44], [20, 28, 98])]
- **Expected:** {'length': 3, 'sequence': [20, 28, 44]}
- **Actual:** N/A



### lis_standard_05
- **Error:** Value mismatches: [('sequence', [13, 34, 59, 69], [13, 46, 78, 94])]
- **Expected:** {'length': 4, 'sequence': [13, 34, 59, 69]}
- **Actual:** N/A



### lis_edge_01
- **Error:** Value mismatches: [('length', 5, 6), ('sequence', [11, 38, 47, 74, 85], [11, 71, 74, 81, 85, 91])]
- **Expected:** {'length': 5, 'sequence': [11, 38, 47, 74, 85]}
- **Actual:** N/A



### lis_edge_02
- **Error:** Value mismatches: [('sequence', [11, 13, 36, 59, 82], [30, 38, 49, 59, 82])]
- **Expected:** {'length': 5, 'sequence': [11, 13, 36, 59, 82]}
- **Actual:** N/A



### lis_edge_03
- **Error:** Value mismatches: [('length', 4, 8), ('sequence', [27, 35, 78, 82], [10, 22, 35, 78, 82, 83, 86, 90])]
- **Expected:** {'length': 4, 'sequence': [27, 35, 78, 82]}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.899722