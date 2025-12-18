# Scaffold Verification Report: huffman

## Summary

- **Status:** FAILED
- **Model:** claude-3-haiku-20240307
- **Test Date:** 2025-12-17 23:34
- **Pass Rate:** 0.0% (0/11)
- **Total Tokens:** 0

## Test Results by Tier

### Simple Cases

- [FAIL] huffman_simple_01: Test case huffman_simple_01

- [FAIL] huffman_simple_02: Test case huffman_simple_02

- [FAIL] huffman_simple_03: Test case huffman_simple_03


### Standard Cases

- [FAIL] huffman_standard_01: Test case huffman_standard_01

- [FAIL] huffman_standard_02: Test case huffman_standard_02

- [FAIL] huffman_standard_03: Test case huffman_standard_03

- [FAIL] huffman_standard_04: Test case huffman_standard_04

- [FAIL] huffman_standard_05: Test case huffman_standard_05


### Edge Cases

- [FAIL] huffman_edge_01: Test case huffman_edge_01

- [FAIL] huffman_edge_02: Test case huffman_edge_02

- [FAIL] huffman_edge_03: Test case huffman_edge_03


## Failure Analysis



### huffman_simple_01
- **Error:** Value mismatches: [('total_bits', 224, 530), ('codes', {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}, {'a': '00', 'b': '01', 'c': '10', 'd': '110', 'e': '111', 'f': '1'})]
- **Expected:** {'total_bits': 224, 'codes': {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}}
- **Actual:** N/A



### huffman_simple_02
- **Error:** Value mismatches: [('total_bits', 224, 530), ('codes', {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}, {'a': '00', 'b': '01', 'c': '10', 'd': '110', 'e': '111', 'f': '1'})]
- **Expected:** {'total_bits': 224, 'codes': {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}}
- **Actual:** N/A



### huffman_simple_03
- **Error:** Value mismatches: [('total_bits', 224, 530), ('codes', {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}, {'a': '00', 'b': '01', 'c': '10', 'd': '110', 'e': '111', 'f': '1'})]
- **Expected:** {'total_bits': 224, 'codes': {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}}
- **Actual:** N/A



### huffman_standard_01
- **Error:** Value mismatches: [('total_bits', 159, 276), ('codes', {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}, {'a': '0', 'b': '110', 'c': '1110', 'd': '11110', 'e': '11111', 'f': '1111', 'g': '11100', 'h': '11101'})]
- **Expected:** {'total_bits': 159, 'codes': {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}}
- **Actual:** N/A



### huffman_standard_02
- **Error:** Value mismatches: [('total_bits', 159, 340), ('codes', {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}, {'a': '0', 'b': '110', 'c': '1110', 'd': '11110', 'e': '11111', 'f': '1111', 'g': '11100', 'h': '11101'})]
- **Expected:** {'total_bits': 159, 'codes': {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}}
- **Actual:** N/A



### huffman_standard_03
- **Error:** Value mismatches: [('total_bits', 159, 276), ('codes', {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}, {'a': '0', 'b': '110', 'c': '1110', 'd': '11110', 'e': '11111', 'f': '1111', 'g': '11100', 'h': '11101'})]
- **Expected:** {'total_bits': 159, 'codes': {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}}
- **Actual:** N/A



### huffman_standard_04
- **Error:** Value mismatches: [('total_bits', 159, 276), ('codes', {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}, {'a': '0', 'b': '110', 'c': '1110', 'd': '11110', 'e': '11111', 'f': '1111', 'g': '11100', 'h': '11101'})]
- **Expected:** {'total_bits': 159, 'codes': {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}}
- **Actual:** N/A



### huffman_standard_05
- **Error:** Value mismatches: [('total_bits', 159, 224), ('codes', {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}, {'a': '10', 'b': '1111', 'c': '110', 'd': '010', 'e': '011', 'f': '111', 'g': '000', 'h': '001'})]
- **Expected:** {'total_bits': 159, 'codes': {'c': '00', 'f': '01', 'b': '10', 'a': '110', 'e': '1110', 'd': '11110', 'g': '111110', 'h': '111111'}}
- **Actual:** N/A



### huffman_edge_01
- **Error:** Value mismatches: [('codes', {'a': '0'}, {'a': ''})]
- **Expected:** {'total_bits': 100, 'codes': {'a': '0'}}
- **Actual:** N/A



### huffman_edge_02
- **Error:** Value mismatches: [('codes', {'b': '0', 'a': '1'}, {'a': '0', 'b': '1'})]
- **Expected:** {'total_bits': 20, 'codes': {'b': '0', 'a': '1'}}
- **Actual:** N/A



### huffman_edge_03
- **Error:** Value mismatches: [('total_bits', 40, 80), ('codes', {'c': '00', 'a': '01', 'd': '10', 'b': '11'}, {'a': '00', 'b': '01', 'c': '10', 'd': '11'})]
- **Expected:** {'total_bits': 40, 'codes': {'c': '00', 'a': '01', 'd': '10', 'b': '11'}}
- **Actual:** N/A



---

Generated with [Claude Code](https://claude.com/claude-code) on 2025-12-18T00:00:21.895982