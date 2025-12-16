# Rabin-Karp String Matching Scaffold

## When to Use
- Pattern matching with hashing
- Multiple pattern search
- Plagiarism detection
- When average O(n+m) is acceptable (worst case O(nm))
- Rolling hash applications

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following pattern matching problem using Rabin-Karp Algorithm.

1) Problem Restatement
- Given: text T of length n, pattern P of length m
- Goal: find all occurrences of P in T
- Method: compare hash values, verify on match

2) Hash Function Definition
For string S of length m with characters S[0..m-1]:

hash(S) = (S[0]×d^(m-1) + S[1]×d^(m-2) + ... + S[m-1]×d^0) mod q

Where:
- d = alphabet size (e.g., 256 for ASCII)
- q = large prime (e.g., 101, 997, 10^9+7)
- S[i] = numeric value of character

3) Rolling Hash Update
When sliding window by 1:
old_hash = hash(T[i..i+m-1])
new_hash = hash(T[i+1..i+m])

new_hash = (d × (old_hash - T[i]×d^(m-1)) + T[i+m]) mod q

This removes T[i], shifts left, adds T[i+m].

4) Algorithm Procedure
a) Compute pattern_hash = hash(P)
b) Compute h = d^(m-1) mod q (for rolling hash)
c) Compute initial text_hash = hash(T[0..m-1])
d) For i = 0 to n-m:
   - If text_hash == pattern_hash:
     - Verify character by character (avoid false positives)
     - If match: report position i
   - Compute next text_hash using rolling hash

5) Handling Hash Collisions
Hash match ≠ string match (hash collision possible)
MUST verify actual characters when hashes match.

6) Verification Protocol
- Each reported position: actual string comparison confirms
- Rolling hash correctly updated
- Modular arithmetic handles negative remainders
```

---

## Worked Example

### Problem
Find P = "ABC" in T = "AABCABC"
Use d = 256 (ASCII), q = 101

### Expected Scaffold Application

**1) Problem Restatement**
- Text: "AABCABC" (length 7)
- Pattern: "ABC" (length 3)
- Use rolling hash to find matches

**2) Hash Computation**

Pattern hash:
```
hash("ABC") = (65×256² + 66×256¹ + 67×256⁰) mod 101
            = (65×65536 + 66×256 + 67) mod 101
            = (4259840 + 16896 + 67) mod 101
            = 4276803 mod 101
            = 38
```

**3) Precompute h = d^(m-1) mod q**
```
h = 256² mod 101 = 65536 mod 101 = 95
```

**4) Algorithm Execution**

**Initial window T[0..2] = "AAB":**
```
hash("AAB") = (65×256² + 65×256 + 66) mod 101
            = (4259840 + 16640 + 66) mod 101
            = 4276546 mod 101
            = 35
```

| i | Window | text_hash | pattern_hash | Match? | Action |
|---|--------|-----------|--------------|--------|--------|
| 0 | AAB    | 35        | 38           | No     | Roll   |
| 1 | ABC    | 38        | 38           | **Hash match!** | Verify |
| - | -      | -         | -            | "ABC"=="ABC" ✓ | **Found at 1** |
| 2 | BCA    | ?         | 38           | No     | Roll   |
| 3 | CAB    | ?         | 38           | No     | Roll   |
| 4 | ABC    | 38        | 38           | **Hash match!** | Verify |
| - | -      | -         | -            | "ABC"=="ABC" ✓ | **Found at 4** |

**Rolling hash example (i=0 to i=1):**
```
Old: "AAB", hash = 35
Remove 'A' (65), add 'C' (67):
new_hash = (256 × (35 - 65×95) + 67) mod 101
         = (256 × (35 - 6175) + 67) mod 101
         = (256 × (-6140) + 67) mod 101

Handle negative: -6140 mod 101 = -6140 + 61×101 = -6140 + 6161 = 21
new_hash = (256 × 21 + 67) mod 101
         = (5376 + 67) mod 101
         = 5443 mod 101
         = 38 ✓
```

**5) Results**
Pattern "ABC" found at positions: **1** and **4**

**6) Verification**
- T[1..3] = "ABC" == "ABC" ✓
- T[4..6] = "ABC" == "ABC" ✓

### Final Answer
Pattern found at indices: **1, 4**

---

## Multiple Pattern Search

Rabin-Karp excels at searching for multiple patterns:

1. Compute hash of each pattern
2. Store in hash table
3. For each window in text:
   - Check if window hash is in hash table
   - If yes, verify against matching pattern(s)

Useful for: plagiarism detection, dictionary matching

---

## Spurious Hits (False Positives)

Example: Different strings, same hash (collision)
```
hash("AB") = 16461 mod 101 = 2
hash("K")  = ... might also equal 2
```

Always verify when hashes match!

---

## Common Failure Modes

1. **Not verifying on hash match** → false positives
2. **Negative modulo handling** → must add q if negative
3. **Integer overflow** → use modular arithmetic throughout
4. **Wrong h value** → h = d^(m-1) mod q, not d^m
5. **Not precomputing h** → recomputing is expensive
6. **Choosing small q** → more collisions, more verifications
