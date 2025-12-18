# Scaffold Verification Report: kmp

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:54
- **Pass Rate:** 36.4% (4/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] kmp_simple_01: Test case kmp_simple_01

- [FAIL] kmp_simple_02: Test case kmp_simple_02

- [FAIL] kmp_simple_03: Test case kmp_simple_03


### Standard Cases

- [PASS] kmp_standard_01: Test case kmp_standard_01

- [FAIL] kmp_standard_02: Test case kmp_standard_02

- [PASS] kmp_standard_03: Test case kmp_standard_03

- [PASS] kmp_standard_04: Test case kmp_standard_04

- [FAIL] kmp_standard_05: Test case kmp_standard_05


### Edge Cases

- [PASS] kmp_edge_01: Test case kmp_edge_01

- [FAIL] kmp_edge_02: Test case kmp_edge_02

- [FAIL] kmp_edge_03: Test case kmp_edge_03


## Failure Analysis



### kmp_simple_01
- **Error:** Expected {'matches': [10]}, got {'matches': [0, 5, 10, 15]}
- **Expected:** {'matches': [10]}
- **Actual:** N/A



### kmp_simple_02
- **Error:** Expected {'matches': [10]}, got {'matches': [0, 5, 10, 15]}
- **Expected:** {'matches': [10]}
- **Actual:** N/A



### kmp_simple_03
- **Error:** Expected {'matches': [10]}, got {'matches': [0, 5, 10, 15]}
- **Expected:** {'matches': [10]}
- **Actual:** N/A





### kmp_standard_02
- **Error:** Expected {'matches': [0, 9, 13]}, got {'matches': [0]}
- **Expected:** {'matches': [0, 9, 13]}
- **Actual:** N/A







### kmp_standard_05
- **Error:** Expected {'matches': [0, 9, 13]}, got {'matches': [1, 9, 15]}
- **Expected:** {'matches': [0, 9, 13]}
- **Actual:** N/A





### kmp_edge_02
- **Error:** Expected {'matches': [0, 9, 13]}, got {'matches': [0]}
- **Expected:** {'matches': [0, 9, 13]}
- **Actual:** N/A



### kmp_edge_03
- **Error:** Expected {'matches': [0, 9, 13]}, got {'matches': [1, 9, 15]}
- **Expected:** {'matches': [0, 9, 13]}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.896671