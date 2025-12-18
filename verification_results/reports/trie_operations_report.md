# Scaffold Verification Report: trie_operations

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:56
- **Pass Rate:** 45.5% (5/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [PASS] trie_operations_simple_01: Test case trie_operations_simple_01

- [PASS] trie_operations_simple_02: Test case trie_operations_simple_02

- [PASS] trie_operations_simple_03: Test case trie_operations_simple_03


### Standard Cases

- [FAIL] trie_operations_standard_01: Test case trie_operations_standard_01

- [FAIL] trie_operations_standard_02: Test case trie_operations_standard_02

- [FAIL] trie_operations_standard_03: Test case trie_operations_standard_03

- [FAIL] trie_operations_standard_04: Test case trie_operations_standard_04

- [FAIL] trie_operations_standard_05: Test case trie_operations_standard_05


### Edge Cases

- [PASS] trie_operations_edge_01: Test case trie_operations_edge_01

- [PASS] trie_operations_edge_02: Test case trie_operations_edge_02

- [FAIL] trie_operations_edge_03: Test case trie_operations_edge_03


## Failure Analysis









### trie_operations_standard_01
- **Error:** Expected {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}, got {'results': [True, False, True, "['hello", 'help', 'heap']}
- **Expected:** {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}
- **Actual:** N/A



### trie_operations_standard_02
- **Error:** Expected {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}, got {'results': [True, False, True, "['hello", 'help', 'heap']}
- **Expected:** {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}
- **Actual:** N/A



### trie_operations_standard_03
- **Error:** Expected {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}, got {'results': [True, False, True, "['hello", 'help', 'heap']}
- **Expected:** {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}
- **Actual:** N/A



### trie_operations_standard_04
- **Error:** Expected {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}, got {'results': [True, False, True, "['hello", 'help', 'heap']}
- **Expected:** {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}
- **Actual:** N/A



### trie_operations_standard_05
- **Error:** Expected {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}, got {'results': [True, False, True, "['hello", 'help', 'heap']}
- **Expected:** {'results': [True, False, True, ['hello', 'help'], ['deal', 'dealer', 'dear']]}
- **Actual:** N/A







### trie_operations_edge_03
- **Error:** Expected {'results': [['test', 'testing', 'tested', 'tester']]}, got {'results': [True]}
- **Expected:** {'results': [['test', 'testing', 'tested', 'tester']]}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.908023