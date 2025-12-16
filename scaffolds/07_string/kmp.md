# KMP (Knuth-Morris-Pratt) Pattern Matching Scaffold

## When to Use
- Searching for pattern in text
- Multiple pattern occurrences
- When O(n+m) time is needed (not O(nm))
- Pattern preprocessing is worthwhile
- Streaming text (can't go back)

---

## Scaffold Instructions (paste this to LLM)

```
Solve the following pattern matching problem using KMP Algorithm.

1) Problem Restatement
- Given: text T of length n, pattern P of length m
- Goal: find all occurrences of P in T
- Efficiency: O(n + m) time

2) State Definition (Failure Function)
lps[i] = length of longest proper prefix of P[0..i]
         that is also a suffix of P[0..i]

"Proper" means prefix ≠ entire string.

Example: P = "ABAB"
- lps[0] = 0 (single char, no proper prefix)
- lps[1] = 0 ("AB" - no matching prefix/suffix)
- lps[2] = 1 ("ABA" - "A" is both prefix and suffix)
- lps[3] = 2 ("ABAB" - "AB" is both prefix and suffix)

3) Building the LPS Array
a) lps[0] = 0, length = 0, i = 1
b) While i < m:
   - If P[i] == P[length]:
     - length++, lps[i] = length, i++
   - Else if length > 0:
     - length = lps[length - 1] (fall back)
   - Else:
     - lps[i] = 0, i++

4) Searching Using LPS
a) i = 0 (text index), j = 0 (pattern index)
b) While i < n:
   - If T[i] == P[j]:
     - i++, j++
   - If j == m:
     - Found match at index (i - j)
     - j = lps[j - 1] (continue searching)
   - Else if i < n and T[i] != P[j]:
     - If j > 0:
       - j = lps[j - 1]
     - Else:
       - i++

5) Key Insight
When mismatch occurs at P[j], we know P[0..j-1] matched.
LPS tells us longest prefix of pattern that's still valid.
No need to re-compare those characters.

6) Verification Protocol
- Each reported position: T[pos..pos+m-1] == P
- Time complexity: O(n + m)
- No characters in text compared more than twice
```

---

## Worked Example

### Problem
Find all occurrences of P = "ABABC" in T = "ABABABABC"

### Expected Scaffold Application

**1) Problem Restatement**
- Text: "ABABABABC" (length 9)
- Pattern: "ABABC" (length 5)
- Find all starting positions of pattern in text

**2-3) Build LPS Array**

P = "ABABC"

| i | P[0..i] | Longest proper prefix = suffix | lps[i] |
|---|---------|--------------------------------|--------|
| 0 | A       | "" (none)                      | 0      |
| 1 | AB      | "" (A≠B)                       | 0      |
| 2 | ABA     | "A"                            | 1      |
| 3 | ABAB    | "AB"                           | 2      |
| 4 | ABABC   | "" (can't extend)              | 0      |

**LPS computation trace:**
```
i=1: P[1]='B' vs P[0]='A' → mismatch, lps[1]=0
i=2: P[2]='A' vs P[0]='A' → match, length=1, lps[2]=1
i=3: P[3]='B' vs P[1]='B' → match, length=2, lps[3]=2
i=4: P[4]='C' vs P[2]='A' → mismatch
     length = lps[1] = 0
     P[4]='C' vs P[0]='A' → mismatch, lps[4]=0
```

**LPS = [0, 0, 1, 2, 0]**

**4) Search Phase**

T = "ABABABABC"
P = "ABABC"

| Step | i | j | T[i] | P[j] | Match? | Action                      |
|------|---|---|------|------|--------|-----------------------------|
| 1    | 0 | 0 | A    | A    | Yes    | i++, j++                    |
| 2    | 1 | 1 | B    | B    | Yes    | i++, j++                    |
| 3    | 2 | 2 | A    | A    | Yes    | i++, j++                    |
| 4    | 3 | 3 | B    | B    | Yes    | i++, j++                    |
| 5    | 4 | 4 | A    | C    | No     | j = lps[3] = 2              |
| 6    | 4 | 2 | A    | A    | Yes    | i++, j++                    |
| 7    | 5 | 3 | B    | B    | Yes    | i++, j++                    |
| 8    | 6 | 4 | A    | C    | No     | j = lps[3] = 2              |
| 9    | 6 | 2 | A    | A    | Yes    | i++, j++                    |
| 10   | 7 | 3 | B    | B    | Yes    | i++, j++                    |
| 11   | 8 | 4 | C    | C    | Yes    | i++, j++                    |
| 12   | 9 | 5 | -    | -    | j==m   | **MATCH at position 4!**    |

**5) Result**
Pattern "ABABC" found at position **4** in "ABABABABC"

**Verification:**
T[4..8] = "ABABC" ✓

### Final Answer
Pattern found at index: **4**

---

## Visualization of LPS Skip

When we had mismatch at i=4, j=4:
```
Text:    A B A B A B A B C
Pattern: A B A B C
             ^ mismatch at C

We know "ABAB" matched. LPS[3]=2 tells us "AB" is both prefix and suffix.
So we can align pattern's "AB" prefix with the "AB" we just matched:

Text:    A B A B A B A B C
Pattern:     A B A B C
```

This is the key insight: no backtracking in text!

---

## Common Failure Modes

1. **Wrong LPS computation** → off-by-one errors, wrong fallback
2. **Not handling length=0 case** → must reset to 0, not keep falling back
3. **Forgetting to continue after match** → j = lps[j-1] after match
4. **Index confusion** → i is text index, j is pattern index
5. **Not handling empty pattern** → edge case, matches everywhere
6. **Confusing prefix with suffix** → proper prefix is strictly smaller
