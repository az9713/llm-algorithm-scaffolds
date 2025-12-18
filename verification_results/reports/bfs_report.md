# Scaffold Verification Report: bfs

## Summary

- **Status:** PARTIAL
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:22
- **Pass Rate:** 72.7% (8/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [PASS] bfs_simple_01: Test case bfs_simple_01

- [FAIL] bfs_simple_02: Test case bfs_simple_02

- [PASS] bfs_simple_03: Test case bfs_simple_03


### Standard Cases

- [PASS] bfs_standard_01: Test case bfs_standard_01

- [PASS] bfs_standard_02: Test case bfs_standard_02

- [FAIL] bfs_standard_03: Test case bfs_standard_03

- [FAIL] bfs_standard_04: Test case bfs_standard_04

- [PASS] bfs_standard_05: Test case bfs_standard_05


### Edge Cases

- [PASS] bfs_edge_01: Test case bfs_edge_01

- [PASS] bfs_edge_02: Test case bfs_edge_02

- [PASS] bfs_edge_03: Test case bfs_edge_03


## Failure Analysis





### bfs_simple_02
- **Error:** Different path: expected ['A', 'C', 'D'], got ['A', 'B', 'D']
- **Expected:** ['A', 'C', 'D']
- **Actual:** N/A









### bfs_standard_03
- **Error:** Different path: expected ['A', 'B', 'C', 'D', 'E', 'F', 'G'], got ['A', 'B', 'G']
- **Expected:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Actual:** N/A



### bfs_standard_04
- **Error:** Different path: expected ['A', 'G'], got ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Expected:** ['A', 'G']
- **Actual:** N/A











---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.886051