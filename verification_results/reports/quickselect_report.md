# Scaffold Verification Report: quickselect

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:32
- **Pass Rate:** 27.3% (3/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] quickselect_simple_01: Test case quickselect_simple_01

- [FAIL] quickselect_simple_02: Test case quickselect_simple_02

- [PASS] quickselect_simple_03: Test case quickselect_simple_03


### Standard Cases

- [PASS] quickselect_standard_01: Test case quickselect_standard_01

- [PASS] quickselect_standard_02: Test case quickselect_standard_02

- [FAIL] quickselect_standard_03: Test case quickselect_standard_03

- [FAIL] quickselect_standard_04: Test case quickselect_standard_04

- [FAIL] quickselect_standard_05: Test case quickselect_standard_05


### Edge Cases

- [FAIL] quickselect_edge_01: Test case quickselect_edge_01

- [FAIL] quickselect_edge_02: Test case quickselect_edge_02

- [FAIL] quickselect_edge_03: Test case quickselect_edge_03


## Failure Analysis



### quickselect_simple_01
- **Error:** Expected {'value': 2}, got {'value': 4}
- **Expected:** {'value': 2}
- **Actual:** N/A



### quickselect_simple_02
- **Error:** Expected {'value': 2}, got {'value': 4}
- **Expected:** {'value': 2}
- **Actual:** N/A









### quickselect_standard_03
- **Error:** Expected {'value': 70}, got {'value': 54}
- **Expected:** {'value': 70}
- **Actual:** N/A



### quickselect_standard_04
- **Error:** Expected {'value': 44}, got {'value': 55}
- **Expected:** {'value': 44}
- **Actual:** N/A



### quickselect_standard_05
- **Error:** Expected {'value': 49}, got {'value': 34}
- **Expected:** {'value': 49}
- **Actual:** N/A



### quickselect_edge_01
- **Error:** Expected {'value': 47}, got {'value': 11}
- **Expected:** {'value': 47}
- **Actual:** N/A



### quickselect_edge_02
- **Error:** Expected {'value': 38}, got {'value': 30}
- **Expected:** {'value': 38}
- **Actual:** N/A



### quickselect_edge_03
- **Error:** Expected {'value': 27}, got {'value': 35}
- **Expected:** {'value': 27}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.903939