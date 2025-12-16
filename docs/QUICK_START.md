# Quick Start Guide - 10 Hands-On Examples

## Welcome!

This guide gets you using algorithmic scaffolds in **10 minutes or less**. Each example is self-contained and builds your confidence step by step.

**What you'll do:** Copy a scaffold, paste it into an AI assistant, add a problem, and see the magic happen.

**What you need:** Access to ChatGPT, Claude, or any AI assistant.

---

## How This Guide Works

Each example follows this pattern:
1. **The Problem** - A real-world scenario
2. **The Scaffold** - What to copy (simplified version)
3. **Your Prompt** - Exactly what to type
4. **Expected Result** - What the AI should produce

**Tip:** Start with Example 1 and work through in order. Each builds on previous concepts.

---

## Example 1: Finding the Shortest Route (BFS)

### The Problem
You're planning a trip and want to find the route with the **fewest stops** between cities.

```
Cities and connections:
- New York → Boston
- New York → Philadelphia
- Boston → Portland
- Philadelphia → Washington DC
- Washington DC → Richmond
- Portland → Burlington

Question: What's the route from New York to Burlington with fewest stops?
```

### The Scaffold (Copy This)

```
I need you to find the shortest path (fewest edges) using BFS.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Start node: ___
   - Goal node: ___
   - This is an unweighted graph (all edges = 1 hop)

2) SET UP state:
   - queue = [start]
   - visited = {start}
   - parent = {start: None}

3) BFS LOOP:
   While queue not empty:
   a) current = dequeue front of queue
   b) If current == goal: STOP, reconstruct path
   c) For each neighbor of current not in visited:
      - Add to visited
      - Set parent[neighbor] = current
      - Enqueue neighbor

4) RECONSTRUCT PATH:
   Trace parent pointers from goal back to start

5) VERIFY:
   - Count hops in path
   - Confirm each connection exists

Show your work at each step with clear state updates.
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Cities and connections:
- New York connects to: Boston, Philadelphia
- Boston connects to: Portland
- Philadelphia connects to: Washington DC
- Washington DC connects to: Richmond
- Portland connects to: Burlington

Find: Shortest route from New York to Burlington
```

### Expected Result

The AI should show:
- Step-by-step BFS execution
- State updates at each iteration
- Final path: **New York → Boston → Portland → Burlington**
- Distance: **3 hops**

**Congratulations!** You've used your first scaffold!

---

## Example 2: Scheduling Meetings (Activity Selection)

### The Problem
You have multiple meetings but only one conference room. Find the **maximum number of non-overlapping meetings**.

```
Meetings:
- Team standup: 9:00-9:30
- Project review: 9:15-10:30
- Client call: 10:00-11:00
- Lunch meeting: 11:30-12:30
- Training: 12:00-13:30
- Interview: 13:00-14:00
- Planning: 14:00-15:00
```

### The Scaffold (Copy This)

```
I need you to select maximum non-overlapping activities using the GREEDY approach.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Activities with start and end times
   - Goal: maximize number of activities
   - Constraint: no overlapping times

2) GREEDY STRATEGY:
   Sort by END TIME (earliest first)
   Why: finishing early leaves most room for future activities

3) SELECTION PROCESS:
   selected = []
   last_end_time = 0

   For each activity in sorted order:
       If activity.start >= last_end_time:
           Add to selected
           last_end_time = activity.end

4) OUTPUT:
   List selected activities
   Count how many

5) VERIFY:
   - Check no two selected activities overlap
   - Confirm we couldn't add any more

Show the sorted list and selection process step by step.
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Meetings (name: start-end):
- Team standup: 9:00-9:30
- Project review: 9:15-10:30
- Client call: 10:00-11:00
- Lunch meeting: 11:30-12:30
- Training: 12:00-13:30
- Interview: 13:00-14:00
- Planning: 14:00-15:00

Find: Maximum number of non-overlapping meetings
```

### Expected Result

The AI should:
1. Sort by end time
2. Select meetings one by one
3. Final selection: **Team standup, Client call, Lunch meeting, Planning** (4 meetings)

---

## Example 3: Searching a Phonebook (Binary Search)

### The Problem
Find a name in a sorted phonebook using **binary search** (much faster than checking every entry).

```
Phonebook (sorted alphabetically):
1. Adams
2. Brown
3. Davis
4. Garcia
5. Johnson
6. Martinez
7. Miller
8. Smith
9. Taylor
10. Wilson

Find: Miller
```

### The Scaffold (Copy This)

```
I need you to find an item in a sorted list using BINARY SEARCH.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Sorted array of n items
   - Target value to find
   - Goal: find index or confirm not present

2) SET UP state:
   - lo = 0 (first index)
   - hi = n-1 (last index)
   - target = [value to find]

3) BINARY SEARCH LOOP:
   While lo <= hi:
   a) mid = (lo + hi) / 2 (round down)
   b) If array[mid] == target: FOUND at index mid
   c) If array[mid] < target: lo = mid + 1 (search right half)
   d) If array[mid] > target: hi = mid - 1 (search left half)

4) If loop ends without finding: NOT PRESENT

5) VERIFY:
   - Check that array[result] == target
   - Count how many comparisons were made

Show lo, hi, mid at each step.
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Phonebook (index: name):
0: Adams
1: Brown
2: Davis
3: Garcia
4: Johnson
5: Martinez
6: Miller
7: Smith
8: Taylor
9: Wilson

Find: Miller
```

### Expected Result

The AI should show:
- Iteration 1: lo=0, hi=9, mid=4, Johnson < Miller, search right
- Iteration 2: lo=5, hi=9, mid=7, Smith > Miller, search left
- Iteration 3: lo=5, hi=6, mid=5, Martinez < Miller, search right
- Iteration 4: lo=6, hi=6, mid=6, **Miller found at index 6!**
- Only **4 comparisons** instead of 7 (linear search would need 7)

---

## Example 4: Packing a Suitcase (0/1 Knapsack)

### The Problem
You're packing for a trip with a **weight limit**. Each item has a weight and a value. Maximize total value without exceeding the limit.

```
Suitcase capacity: 10 kg

Items:
- Laptop: 4 kg, value 10
- Camera: 2 kg, value 6
- Books: 5 kg, value 8
- Clothes: 3 kg, value 5
- Snacks: 1 kg, value 2
```

### The Scaffold (Copy This)

```
I need you to solve 0/1 KNAPSACK using DYNAMIC PROGRAMMING.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - n items, each with weight and value
   - Capacity W (maximum total weight)
   - Goal: maximize value, can't split items

2) DP STATE DEFINITION:
   dp[i][w] = max value using first i items with capacity w

3) BASE CASE:
   dp[0][w] = 0 for all w (no items = no value)

4) RECURRENCE:
   For each item i (1 to n):
       For each capacity w (0 to W):
           If weight[i] > w:
               dp[i][w] = dp[i-1][w]  (can't take item)
           Else:
               dp[i][w] = max(
                   dp[i-1][w],                    (skip item)
                   dp[i-1][w-weight[i]] + value[i] (take item)
               )

5) ANSWER: dp[n][W]

6) RECONSTRUCT which items were taken:
   Trace back through the dp table

7) VERIFY:
   - Total weight <= capacity
   - Total value matches dp[n][W]

Show the dp table and reconstruction.
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Capacity: 10 kg

Items (name: weight, value):
1. Laptop: 4 kg, value 10
2. Camera: 2 kg, value 6
3. Books: 5 kg, value 8
4. Clothes: 3 kg, value 5
5. Snacks: 1 kg, value 2

Find: Maximum value combination that fits in 10 kg
```

### Expected Result

The AI should:
1. Build a DP table (6 rows × 11 columns)
2. Show the filling process
3. Find maximum value: **21** (Laptop + Camera + Clothes + Snacks = 4+2+3+1 = 10 kg)
4. Verify the solution

---

## Example 5: Solving a Mini Sudoku (Backtracking)

### The Problem
Solve a 4×4 mini Sudoku puzzle using backtracking.

```
Rules: Each row, column, and 2×2 box must contain 1, 2, 3, 4 exactly once.

Puzzle (0 = empty):
1 0 | 0 4
0 0 | 1 0
----+----
0 1 | 0 0
4 0 | 0 1
```

### The Scaffold (Copy This)

```
I need you to solve SUDOKU using BACKTRACKING.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Grid with some cells filled
   - Constraints: each row, column, and box has no repeats
   - Goal: fill all empty cells

2) STATE:
   - grid: current state of puzzle
   - empty_cells: list of cells to fill

3) BACKTRACKING PROCEDURE:
   find_solution(grid):
       cell = first_empty_cell(grid)
       If no empty cell: SOLVED, return True

       For digit in 1,2,3,4:
           If is_valid(cell, digit):
               PLACE digit in cell
               If find_solution(grid): return True
               REMOVE digit (backtrack)

       Return False (no valid digit works)

4) VALIDITY CHECK:
   is_valid(cell, digit):
   - digit not in same row
   - digit not in same column
   - digit not in same 2×2 box

5) SHOW each placement attempt and backtrack

6) VERIFY final solution:
   - All rows have 1,2,3,4
   - All columns have 1,2,3,4
   - All boxes have 1,2,3,4
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this 4×4 Sudoku:

1 _ | _ 4
_ _ | 1 _
----+----
_ 1 | _ _
4 _ | _ 1

Where _ means empty. Fill with 1, 2, 3, or 4.
Each row, column, and 2×2 box must have each digit exactly once.
```

### Expected Result

The AI should:
1. Try digits systematically
2. Backtrack when stuck
3. Find solution:
```
1 3 | 2 4
2 4 | 1 3
----+----
3 1 | 4 2
4 2 | 3 1
```

---

## Example 6: Finding Square Root (Newton-Raphson)

### The Problem
Calculate the square root of 10 to 4 decimal places using Newton-Raphson method.

### The Scaffold (Copy This)

```
I need you to find a SQUARE ROOT using NEWTON-RAPHSON.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Find x such that x² = n
   - This means finding root of f(x) = x² - n

2) NEWTON-RAPHSON FORMULA:
   x_new = x - f(x)/f'(x)
   For f(x) = x² - n:
   x_new = x - (x² - n)/(2x)
   Simplifies to: x_new = (x + n/x) / 2

3) ALGORITHM:
   a) Start with initial guess x₀
   b) Iterate: x_{n+1} = (x_n + n/x_n) / 2
   c) Stop when |x_{n+1} - x_n| < tolerance

4) SHOW each iteration:
   - Current x value
   - Calculation of next x
   - Difference from previous

5) VERIFY:
   - Square the final answer
   - Check it's close to n
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Find: √10 (square root of 10)
Initial guess: x₀ = 3
Tolerance: 0.0001 (stop when change < 0.0001)
Show 4 decimal places in your answer.
```

### Expected Result

The AI should show iterations:
- x₀ = 3
- x₁ = (3 + 10/3)/2 = 3.1667
- x₂ = (3.1667 + 10/3.1667)/2 = 3.1623
- x₃ = 3.1623 (converged!)
- **Answer: √10 ≈ 3.1623**
- Verify: 3.1623² = 10.0001 ≈ 10 ✓

---

## Example 7: Finding Longest Common Text (LCS)

### The Problem
Find the longest sequence of characters that appears in both strings (in order, but not necessarily consecutive).

```
String 1: ABCDGH
String 2: AEDFHR

What characters appear in both, in the same order?
```

### The Scaffold (Copy This)

```
I need you to find the LONGEST COMMON SUBSEQUENCE using DP.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Two strings X and Y
   - Find longest sequence that appears in both (in order)
   - Characters don't need to be consecutive

2) DP STATE:
   dp[i][j] = length of LCS of X[0..i-1] and Y[0..j-1]

3) BASE CASE:
   dp[0][j] = 0 (empty X)
   dp[i][0] = 0 (empty Y)

4) RECURRENCE:
   If X[i-1] == Y[j-1]:
       dp[i][j] = dp[i-1][j-1] + 1 (extend match)
   Else:
       dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (best without one char)

5) BUILD TABLE row by row

6) ANSWER: dp[len(X)][len(Y)]

7) RECONSTRUCT the actual subsequence:
   Trace back through table

8) VERIFY by checking both strings contain the subsequence
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

String X: ABCDGH
String Y: AEDFHR

Find: Longest common subsequence
```

### Expected Result

The AI should:
1. Build a 7×7 table
2. Find LCS length: **3**
3. Reconstruct: **ADH**
4. Verify: ABCDGH contains A...D...H, AEDFHR contains A...D...H ✓

---

## Example 8: Cheapest Flight Route (Dijkstra)

### The Problem
Find the **cheapest** flight route from NYC to LA.

```
Flights (from → to: price):
NYC → Chicago: $150
NYC → Atlanta: $120
Chicago → Denver: $140
Chicago → LA: $300
Atlanta → Dallas: $100
Atlanta → Denver: $200
Dallas → LA: $180
Denver → LA: $150
```

### The Scaffold (Copy This)

```
I need you to find the SHORTEST (cheapest) PATH using DIJKSTRA.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE the problem:
   - Weighted graph (cities and flight costs)
   - Find minimum cost path from source to destination

2) STATE:
   - distances: map of city → cheapest known cost to reach
   - visited: set of finalized cities
   - parent: map for path reconstruction
   - priority_queue: cities to process, ordered by distance

3) INITIALIZATION:
   distances[source] = 0
   distances[all others] = ∞
   priority_queue = [(0, source)]

4) DIJKSTRA LOOP:
   While priority_queue not empty:
   a) Extract city with minimum distance
   b) If already visited, skip
   c) Mark as visited
   d) For each neighbor:
      new_dist = distances[current] + edge_cost
      If new_dist < distances[neighbor]:
          distances[neighbor] = new_dist
          parent[neighbor] = current
          Add (new_dist, neighbor) to priority_queue

5) RECONSTRUCT PATH from destination to source

6) VERIFY:
   - Sum edge costs along path
   - Confirm equals reported distance
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Flights (from → to: price):
NYC → Chicago: $150
NYC → Atlanta: $120
Chicago → Denver: $140
Chicago → LA: $300
Atlanta → Dallas: $100
Atlanta → Denver: $200
Dallas → LA: $180
Denver → LA: $150

Find: Cheapest route from NYC to LA
```

### Expected Result

The AI should find:
- **Path: NYC → Atlanta → Dallas → LA**
- **Cost: $120 + $100 + $180 = $400**
- This beats NYC → Chicago → Denver → LA ($150 + $140 + $150 = $440)

---

## Example 9: Text Pattern Search (KMP)

### The Problem
Find all occurrences of "ABA" in "ABABAABABABA".

### The Scaffold (Copy This)

```
I need you to find PATTERN OCCURRENCES using KMP algorithm.

FOLLOW THESE STEPS EXACTLY:

1) RESTATE:
   - Text T (to search in)
   - Pattern P (to find)
   - Goal: all starting positions where P appears in T

2) BUILD FAILURE FUNCTION for pattern:
   failure[i] = length of longest proper prefix of P[0..i]
                that is also a suffix

   failure[0] = 0
   For i = 1 to len(P)-1:
       j = failure[i-1]
       While j > 0 and P[i] != P[j]:
           j = failure[j-1]
       If P[i] == P[j]: j++
       failure[i] = j

3) SEARCH:
   i = 0 (position in text)
   j = 0 (position in pattern)
   matches = []

   While i < len(T):
       If T[i] == P[j]:
           i++, j++
           If j == len(P):
               Match at position i - j
               j = failure[j-1]
       Else:
           If j > 0: j = failure[j-1]
           Else: i++

4) VERIFY each match by checking T[pos:pos+len(P)] == P
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Text: ABABAABABABA
Pattern: ABA

Find: All positions where ABA appears
```

### Expected Result

The AI should:
1. Build failure function: [0, 0, 1]
2. Find matches at positions: **0, 2, 6, 8, 10**
3. Show: ABABAABABABA
   - [ABA]BAABABABA (pos 0)
   - AB[ABA]ABABABA (pos 2)
   - etc.

---

## Example 10: Monte Carlo Pi Estimation

### The Problem
Estimate the value of π using random points.

### The Scaffold (Copy This)

```
I need you to ESTIMATE PI using MONTE CARLO simulation.

FOLLOW THESE STEPS EXACTLY:

1) CONCEPT:
   - Square of side 2, centered at origin: x,y in [-1,1]
   - Circle of radius 1 inscribed in square
   - Area ratio: (π × 1²) / (2²) = π/4
   - So: π = 4 × (points in circle / total points)

2) ALGORITHM:
   inside_circle = 0
   total_points = N

   For i = 1 to N:
       x = random number in [-1, 1]
       y = random number in [-1, 1]
       If x² + y² <= 1:
           inside_circle++

   estimated_pi = 4 × inside_circle / total_points

3) SIMULATE with sample points (show at least 10)

4) CALCULATE final estimate

5) VERIFY by comparing to actual π ≈ 3.14159
```

### Your Prompt

Copy the scaffold above, then add:

```
Now solve this problem:

Simulate N = 20 random points to estimate π.

Use these "random" coordinates (I'm providing them):
Point 1: (0.2, 0.3)
Point 2: (0.8, 0.9)
Point 3: (-0.4, 0.2)
Point 4: (0.6, 0.7)
Point 5: (-0.1, -0.5)
Point 6: (0.95, 0.1)
Point 7: (-0.3, -0.3)
Point 8: (0.5, 0.5)
Point 9: (-0.8, 0.6)
Point 10: (0.1, 0.9)
Point 11: (-0.7, -0.7)
Point 12: (0.4, -0.2)
Point 13: (0.9, 0.4)
Point 14: (-0.2, 0.8)
Point 15: (0.3, -0.6)
Point 16: (-0.5, 0.5)
Point 17: (0.7, -0.4)
Point 18: (-0.6, -0.1)
Point 19: (0.0, 0.7)
Point 20: (0.2, -0.9)

For each point, check if x² + y² <= 1 (inside circle).
Then estimate π.
```

### Expected Result

The AI should:
1. Check each point: x² + y² <= 1?
2. Count points inside circle (should be around 15-16)
3. Estimate: π ≈ 4 × (inside/20)
4. Compare to actual π ≈ 3.14159

---

## What You've Learned

Congratulations! You've now used scaffolds for:

| Example | Algorithm | Category |
|---------|-----------|----------|
| 1 | BFS | Graph |
| 2 | Activity Selection | Greedy |
| 3 | Binary Search | Divide & Conquer |
| 4 | 0/1 Knapsack | Dynamic Programming |
| 5 | Sudoku | Backtracking |
| 6 | Newton-Raphson | Numerical Methods |
| 7 | LCS | Dynamic Programming |
| 8 | Dijkstra | Graph |
| 9 | KMP | String |
| 10 | Monte Carlo | Numerical Methods |

## Next Steps

1. **Try variations** - Change the numbers in these examples
2. **Explore full scaffolds** - The files in `scaffolds/` have more detail
3. **Read the User Guide** - For comprehensive coverage
4. **Create your own problems** - Apply scaffolds to real scenarios

## Quick Reference

When you need a scaffold, remember:
- **Shortest path (unweighted)** → BFS
- **Shortest path (weighted)** → Dijkstra
- **Search sorted data** → Binary Search
- **Schedule/select without conflict** → Activity Selection (Greedy)
- **Optimize with constraints** → Knapsack (DP)
- **Puzzle with constraints** → Backtracking
- **Find pattern in text** → KMP
- **Numerical approximation** → Newton-Raphson or Monte Carlo

Happy problem-solving!
