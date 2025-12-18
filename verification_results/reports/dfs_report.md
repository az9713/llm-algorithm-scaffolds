# Scaffold Verification Report: dfs

## Summary

- **Status:** PARTIAL
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:23
- **Pass Rate:** 54.5% (6/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] dfs_simple_01: Test case dfs_simple_01

- [FAIL] dfs_simple_02: Test case dfs_simple_02

- [FAIL] dfs_simple_03: Test case dfs_simple_03


### Standard Cases

- [PASS] dfs_standard_01: Test case dfs_standard_01

- [PASS] dfs_standard_02: Test case dfs_standard_02

- [PASS] dfs_standard_03: Test case dfs_standard_03

- [FAIL] dfs_standard_04: Test case dfs_standard_04

- [FAIL] dfs_standard_05: Test case dfs_standard_05


### Edge Cases

- [PASS] dfs_edge_01: Test case dfs_edge_01

- [PASS] dfs_edge_02: Test case dfs_edge_02

- [PASS] dfs_edge_03: Test case dfs_edge_03


## Failure Analysis



### dfs_simple_01
- **Error:** Different path: expected ['A', 'D'], got ['A', 'B', 'C', 'D']
- **Expected:** ['A', 'D']
- **Actual:** N/A



### dfs_simple_02
- **Error:** Different path: expected ['A', 'C', 'D'], got ['A', 'B', 'C', 'D']
- **Expected:** ['A', 'C', 'D']
- **Actual:** N/A



### dfs_simple_03
- **Error:** Different path: expected ['A', 'C', 'D'], got ['A', 'B', 'C', 'D']
- **Expected:** ['A', 'C', 'D']
- **Actual:** N/A









### dfs_standard_04
- **Error:** Different path: expected ['A', 'G'], got ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Expected:** ['A', 'G']
- **Actual:** N/A



### dfs_standard_05
- **Error:** Different path: expected ['A', 'F', 'G', 'H'], got ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
- **Expected:** ['A', 'F', 'G', 'H']
- **Actual:** N/A









---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.888771