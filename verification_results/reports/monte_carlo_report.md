# Scaffold Verification Report: monte_carlo

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:58
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] monte_carlo_simple_01: Test case monte_carlo_simple_01

- [FAIL] monte_carlo_simple_02: Test case monte_carlo_simple_02

- [FAIL] monte_carlo_simple_03: Test case monte_carlo_simple_03


### Standard Cases

- [FAIL] monte_carlo_standard_01: Test case monte_carlo_standard_01

- [FAIL] monte_carlo_standard_02: Test case monte_carlo_standard_02

- [FAIL] monte_carlo_standard_03: Test case monte_carlo_standard_03

- [FAIL] monte_carlo_standard_04: Test case monte_carlo_standard_04

- [FAIL] monte_carlo_standard_05: Test case monte_carlo_standard_05


### Edge Cases

- [FAIL] monte_carlo_edge_01: Test case monte_carlo_edge_01

- [FAIL] monte_carlo_edge_02: Test case monte_carlo_edge_02

- [FAIL] monte_carlo_edge_03: Test case monte_carlo_edge_03


## Failure Analysis



### monte_carlo_simple_01
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.128, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_simple_02
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.228, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_simple_03
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_standard_01
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1396, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_standard_02
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1392, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_standard_03
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.14, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_standard_04
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1528, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_standard_05
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1676, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_edge_01
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.2, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_edge_02
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.14688, 'true_value': 3.141592653589793}
- **Actual:** N/A



### monte_carlo_edge_03
- **Error:** Cannot convert to float: float() argument must be a string or a real number, not 'dict'
- **Expected:** {'estimate': 3.1472, 'true_value': 3.141592653589793}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.901782