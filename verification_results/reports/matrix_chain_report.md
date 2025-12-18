# Scaffold Verification Report: matrix_chain

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:47
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] matrix_chain_simple_01: Test case matrix_chain_simple_01

- [FAIL] matrix_chain_simple_02: Test case matrix_chain_simple_02

- [FAIL] matrix_chain_simple_03: Test case matrix_chain_simple_03


### Standard Cases

- [FAIL] matrix_chain_standard_01: Test case matrix_chain_standard_01

- [FAIL] matrix_chain_standard_02: Test case matrix_chain_standard_02

- [FAIL] matrix_chain_standard_03: Test case matrix_chain_standard_03

- [FAIL] matrix_chain_standard_04: Test case matrix_chain_standard_04

- [FAIL] matrix_chain_standard_05: Test case matrix_chain_standard_05


### Edge Cases

- [FAIL] matrix_chain_edge_01: Test case matrix_chain_edge_01

- [FAIL] matrix_chain_edge_02: Test case matrix_chain_edge_02

- [FAIL] matrix_chain_edge_03: Test case matrix_chain_edge_03


## Failure Analysis



### matrix_chain_simple_01
- **Error:** Expected {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}, got {'min_operations': 18000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}
- **Actual:** N/A



### matrix_chain_simple_02
- **Error:** Expected {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}, got {'min_operations': 18000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}
- **Actual:** N/A



### matrix_chain_simple_03
- **Error:** Expected {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}, got {'min_operations': 18000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 4500, 'parenthesization': '((A1 × A2) × A3)'}
- **Actual:** N/A



### matrix_chain_standard_01
- **Error:** Expected {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}, got {'min_operations': 26000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}
- **Actual:** N/A



### matrix_chain_standard_02
- **Error:** Expected {'min_operations': 30000, 'parenthesization': '(((A1 × A2) × A3) × A4)'}, got {'min_operations': 18000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 30000, 'parenthesization': '(((A1 × A2) × A3) × A4)'}
- **Actual:** N/A



### matrix_chain_standard_03
- **Error:** Expected {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}, got {'min_operations': 26000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}
- **Actual:** N/A



### matrix_chain_standard_04
- **Error:** Failed to parse LLM response: Could not extract matrix chain result from response
- **Expected:** {'min_operations': 30000, 'parenthesization': '(((A1 × A2) × A3) × A4)'}
- **Actual:** N/A



### matrix_chain_standard_05
- **Error:** Expected {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}, got {'min_operations': 26000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 26000, 'parenthesization': '((A1 × (A2 × A3)) × A4)'}
- **Actual:** N/A



### matrix_chain_edge_01
- **Error:** Expected {'min_operations': 0, 'parenthesization': 'A1'}, got {'min_operations': 4000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 0, 'parenthesization': 'A1'}
- **Actual:** N/A



### matrix_chain_edge_02
- **Error:** Expected {'min_operations': 6000, 'parenthesization': '(A1 × A2)'}, got {'min_operations': 6000, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 6000, 'parenthesization': '(A1 × A2)'}
- **Actual:** N/A



### matrix_chain_edge_03
- **Error:** Expected {'min_operations': 2010, 'parenthesization': '((A1 × A2) × ((A3 × A4) × (A5 × A6)))'}, got {'min_operations': 7500, 'parenthesization': 'track split point k for each (i,j)'}
- **Expected:** {'min_operations': 2010, 'parenthesization': '((A1 × A2) × ((A3 × A4) × (A5 × A6)))'}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.900424