# Frequently Asked Questions (FAQ)

## Table of Contents

1. [Getting Started](#getting-started)
2. [Using Scaffolds](#using-scaffolds)
3. [Choosing the Right Scaffold](#choosing-the-right-scaffold)
4. [Troubleshooting](#troubleshooting)
5. [Understanding Results](#understanding-results)
6. [AI Assistant Questions](#ai-assistant-questions)
7. [Technical Questions](#technical-questions)
8. [Verification Framework](#verification-framework)
9. [Contributing](#contributing)

---

## Getting Started

### Q: What exactly is an algorithmic scaffold?

**A:** A scaffold is a structured set of instructions that tells an AI assistant how to solve a problem step by step. Instead of letting the AI figure out the approach on its own (where it might make mistakes), the scaffold provides:

1. What information to track (state)
2. What steps to follow (procedure)
3. When to stop (termination)
4. How to check the answer (verification)

Think of it like giving someone IKEA furniture instructions instead of just showing them the finished product.

---

### Q: Do I need to understand algorithms to use scaffolds?

**A:** No! That's the beauty of scaffolds. The scaffold contains all the algorithm knowledge - you just need to:

1. Identify your problem type (use our guides)
2. Copy the right scaffold
3. Add your specific problem details
4. Let the AI do the work

Of course, understanding the algorithm helps you verify results, but it's not required.

---

### Q: What do I need to get started?

**A:** Just two things:

1. **These scaffold files** - Download or access the project
2. **An AI assistant** - ChatGPT, Claude, Gemini, or similar

No programming, no installation, no special software.

---

### Q: Which AI assistant should I use?

**A:** Any modern LLM works. Here's a comparison:

| AI | Strengths | Considerations |
|-----|-----------|----------------|
| **GPT-4** | Best at complex reasoning | May need subscription |
| **Claude** | Excellent at following instructions | Great for detailed traces |
| **Gemini Pro** | Good mathematical ability | Good free tier |
| **GPT-3.5** | Fast, widely available | May struggle with complex scaffolds |

**Recommendation:** Start with whatever you have access to. If results are poor, try a more capable model.

---

### Q: Where do I start?

**A:** Follow this path:

1. Read this FAQ (you're doing it!)
2. Try [Quick Start Guide](QUICK_START.md) - Example 1 (takes 5 minutes)
3. Do Examples 2-5 in the Quick Start
4. Try a scaffold on your own problem
5. Read [User Guide](USER_GUIDE.md) for deeper understanding

---

## Using Scaffolds

### Q: How do I copy a scaffold correctly?

**A:** Follow these steps:

1. **Open the scaffold file** (e.g., `scaffolds/01_graph/dijkstra.md`)
2. **Find "Scaffold Instructions"** section
3. **Select all text** in that section
4. **Copy** (Ctrl+C on Windows, Cmd+C on Mac)
5. **Paste** into your AI chat
6. **Add** your specific problem after the scaffold

**Important:** Copy the entire Scaffold Instructions section, not just parts of it.

---

### Q: Can I modify the scaffolds?

**A:** Yes, but be careful:

**Safe modifications:**
- Simplifying language
- Removing unnecessary parts for simple problems
- Adding more detail for complex problems

**Risky modifications:**
- Removing state variables (may break algorithm)
- Changing the order of steps
- Removing verification

**Recommendation:** Use scaffolds as-is until you're comfortable with how they work.

---

### Q: How do I format my problem for the AI?

**A:** Be clear and structured. Compare:

**Bad:**
```
there's a graph with some cities and i need to find the best way to get somewhere
```

**Good:**
```
Graph:
- Nodes: A, B, C, D, E
- Edges:
  - A → B (cost 4)
  - A → C (cost 2)
  - B → D (cost 3)
  - C → D (cost 1)
  - D → E (cost 5)

Find: Shortest path from A to E
```

**Tips:**
- List all nodes
- List all edges with costs (if weighted)
- Clearly state what you're looking for
- Use consistent formatting

---

### Q: The scaffold is really long. Do I need all of it?

**A:** Usually yes, but it depends:

**For learning:** Use the full scaffold to see all steps
**For simple problems:** You might skip the verification section
**For repeated use:** Once you're familiar, you can shorten

**Warning:** Shortening too much often leads to errors. When in doubt, use the full scaffold.

---

### Q: Can I use scaffolds for problems not in the examples?

**A:** Absolutely! That's the whole point. The scaffolds are general-purpose.

**Example:** The Dijkstra scaffold works for:
- Flight routes (cities = nodes, flights = edges)
- Network routing (computers = nodes, connections = edges)
- Game pathfinding (positions = nodes, moves = edges)
- Any weighted graph shortest-path problem

The worked example in each scaffold shows ONE application, but the scaffold works for any problem of that type.

---

## Choosing the Right Scaffold

### Q: How do I know which scaffold to use?

**A:** Ask yourself these questions:

**Is it a path/route problem?**
- All connections equal weight → BFS
- Connections have different costs → Dijkstra
- Some costs can be negative → Bellman-Ford
- You have a distance estimate to goal → A*

**Is it a scheduling problem?**
- Select maximum non-overlapping → Activity Selection
- Order tasks with dependencies → Topological Sort

**Is it a selection/optimization problem?**
- Items can be split → Fractional Knapsack (Greedy)
- Items are whole → 0/1 Knapsack (DP)
- Constraints must all be satisfied → Backtracking

**Is it a search problem?**
- Data is sorted → Binary Search
- Data is unsorted → Linear search or sort first

See [User Guide - Finding the Right Scaffold](USER_GUIDE.md#finding-the-right-scaffold) for complete decision trees.

---

### Q: What if multiple scaffolds seem to fit?

**A:** Consider these factors:

1. **Exactness of requirement:**
   - Need THE optimal answer → DP or exhaustive search
   - Good answer is fine → Greedy or heuristic

2. **Problem size:**
   - Small (< 20 items) → Backtracking is fine
   - Large → Need efficient algorithm (DP, Greedy)

3. **Constraints:**
   - Positive weights only → Dijkstra
   - Negative weights possible → Bellman-Ford

**When unsure:** Try the simpler scaffold first. If it doesn't work, try the more sophisticated one.

---

### Q: What if there's no scaffold for my problem?

**A:** Options:

1. **Check if a similar scaffold works** - Many problems can be transformed
2. **Use a generic template** - `scaffolds/templates/` has category templates
3. **Create your own** - Follow the [Developer Guide](DEVELOPER_GUIDE.md)
4. **Ask for help** - Describe your problem in project discussions

---

## Troubleshooting

### Q: The AI didn't follow the scaffold - it just answered directly.

**A:** This happens sometimes. Try:

1. **Add explicit instruction:**
   ```
   IMPORTANT: Follow the scaffold step by step.
   Show your state after each step.
   Do not skip ahead to the answer.
   ```

2. **Start fresh:** Begin a new conversation

3. **Be more explicit:**
   ```
   Step 1: First, restate the problem.
   Step 2: Then, initialize the state.
   [etc.]
   ```

4. **Try a different AI:** Some models follow instructions better than others

---

### Q: The AI made an error in the middle of the solution.

**A:** This is recoverable:

**Option 1: Point out the error**
```
I think there's an error in step 3. You said distance[C] = 5,
but it should be distance[C] = 3 because the edge A→C has weight 3.
Please continue from step 3 with the corrected value.
```

**Option 2: Ask for verification**
```
Please verify step 3. Check that distance[C] is calculated correctly.
```

**Option 3: Start over**
```
Let's start over. Please be extra careful with the state updates this time.
```

---

### Q: The AI says it can't do this or doesn't understand.

**A:** Try these approaches:

1. **Rephrase as hypothetical:**
   ```
   Let's work through a Dijkstra example together.
   Imagine we have this graph...
   ```

2. **Start with the worked example:**
   ```
   First, let me show you an example from the scaffold, then we'll do my problem.
   [Include worked example from scaffold]
   ```

3. **Break into smaller steps:**
   ```
   Let's do this one step at a time.
   First, just tell me: what is the initial state?
   ```

4. **Use a more capable model:** GPT-4 or Claude handle complex scaffolds better than GPT-3.5

---

### Q: The answer seems wrong. How do I check?

**A:** Several approaches:

1. **Manual verification:**
   - For paths: Add up edge weights, verify they match
   - For selections: Check constraints are satisfied
   - For puzzles: Verify all rules are followed

2. **Ask the AI to verify:**
   ```
   Please verify this answer by:
   1. Tracing through the solution path
   2. Checking all constraints
   3. Confirming no better solution exists
   ```

3. **Try a simple case:**
   - If unsure about a complex problem, try a simple version first
   - Compare AI's answer to your hand calculation

4. **Use an online calculator:**
   - Many algorithms have online visualizers
   - Verify against known correct implementations

---

### Q: The AI gives different answers each time.

**A:** LLMs can be non-deterministic. To improve consistency:

1. **Use temperature 0** if your AI allows it
2. **Be more explicit** in the scaffold
3. **Ask for verification** at the end
4. **Run multiple times** and compare

If answers vary significantly, the problem might be ambiguous or the scaffold might need more clarity.

---

## Understanding Results

### Q: What does the "state" mean in scaffold outputs?

**A:** State is all the information the algorithm tracks at any moment. For example, in Dijkstra:

```
State after processing node B:
- Current node: B
- Distances: {A: 0, B: 2, C: 4, D: ∞, E: ∞}
- Visited: {A, B}
- Parent: {A: None, B: A}
```

This tells you:
- We just processed B
- Shortest known distances to each node
- Which nodes are finalized
- How to reconstruct the path

---

### Q: How do I read the step-by-step trace?

**A:** Each step should show:

1. **What's happening:** "Processing node B"
2. **State before:** Current values of all variables
3. **Actions taken:** What updates were made
4. **State after:** New values after updates

**Example:**
```
STEP 3: Process node B (distance 2)
  - Check neighbor C: current dist(C) = 4, new dist = 2 + 1 = 3
  - 3 < 4, so update: dist(C) = 3, parent(C) = B
  - Check neighbor D: current dist(D) = ∞, new dist = 2 + 5 = 7
  - 7 < ∞, so update: dist(D) = 7, parent(D) = B
  - Mark B as visited

State after step 3:
  distances: {A: 0, B: 2, C: 3, D: 7}
  visited: {A, B}
```

---

### Q: What does "verification" mean at the end?

**A:** Verification confirms the answer is correct. It typically includes:

1. **Solution reconstruction:** Show the full solution (path, selection, etc.)
2. **Constraint checking:** Verify all rules are followed
3. **Optimality confirmation:** Explain why no better solution exists

**Example verification for shortest path:**
```
VERIFICATION:
1. Path: A → B → C → E
2. Edge check: A-B exists ✓, B-C exists ✓, C-E exists ✓
3. Total cost: 2 + 1 + 4 = 7
4. This matches the reported distance ✓
5. No shorter path exists because all nodes are processed ✓
```

---

## AI Assistant Questions

### Q: Why do scaffolds work with AI?

**A:** AI assistants (LLMs) are good at:
- Following clear instructions
- Performing calculations
- Tracking explicit state

But they struggle with:
- Implicit state management
- Systematic search without guidance
- Knowing when to backtrack

Scaffolds bridge this gap by making everything explicit.

---

### Q: Are some AIs better than others for scaffolds?

**A:** Yes, generally:

**Best performance:**
- GPT-4, GPT-4 Turbo
- Claude 2, Claude 3
- Gemini Pro

**Good performance:**
- GPT-3.5 Turbo (for simpler scaffolds)
- Open-source models (Llama 2 70B, Mixtral)

**May struggle:**
- Smaller models
- Heavily rate-limited free tiers

---

### Q: Can I use scaffolds with local/offline AI models?

**A:** Yes! Scaffolds are just text prompts. Any LLM can use them:

- **Ollama** with Llama 2, Mistral, etc.
- **LM Studio** with various models
- **Hugging Face** models
- Any API-accessible model

Larger models (13B+ parameters) generally work better.

---

## Technical Questions

### Q: What's the difference between BFS and Dijkstra?

**A:**

| Aspect | BFS | Dijkstra |
|--------|-----|----------|
| Edge weights | All equal (or 1) | Can vary |
| Data structure | Queue | Priority Queue |
| Metric | Fewest edges | Lowest total weight |
| Example | Fewest subway stops | Cheapest flight route |

**Use BFS when:** All edges are equal (or unweighted)
**Use Dijkstra when:** Edges have different weights

---

### Q: What's the difference between Greedy and Dynamic Programming?

**A:**

| Aspect | Greedy | DP |
|--------|--------|-----|
| Approach | Take best now | Consider all options |
| Speed | Usually faster | May be slower |
| Optimality | Not always optimal | Always optimal (when applicable) |
| When it works | Greedy choice property | Overlapping subproblems |

**Use Greedy when:** Local best leads to global best (activity selection)
**Use DP when:** Need to consider trade-offs (0/1 knapsack)

---

### Q: When should I use backtracking vs DP?

**A:**

| Aspect | Backtracking | DP |
|--------|--------------|-----|
| Problem type | Constraint satisfaction | Optimization |
| Goal | Find valid solution(s) | Find optimal solution |
| Example | Sudoku, N-Queens | Knapsack, LCS |
| Approach | Try and undo | Build up solutions |

**Use Backtracking when:** You need ANY solution that satisfies constraints
**Use DP when:** You need the BEST solution among valid ones

---

### Q: What does O(n log n) mean?

**A:** It's a measure of efficiency. As input size (n) grows:

- **O(n):** Time grows proportionally (2x input = 2x time)
- **O(n log n):** Time grows a bit faster (2x input ≈ 2.2x time)
- **O(n²):** Time grows with square (2x input = 4x time)

**n log n** is considered very efficient. Most comparison-based sorting algorithms achieve this.

**Practical meaning:**
- n=1,000: ~10,000 operations
- n=1,000,000: ~20,000,000 operations

---

## Verification Framework

### Q: What is the verification framework?

**A:** The verification framework is an automated testing system that validates whether scaffolds produce correct results when used with LLMs. It:

1. Generates test cases using trusted libraries (networkx, numpy, scipy)
2. Sends scaffold + test case to Claude
3. Parses the LLM's response
4. Validates against ground truth
5. Produces certification reports

See [Verification Guide](VERIFICATION.md) for details.

---

### Q: What is the current status of scaffold verification?

**A:** As of December 2025:

| Status | Count | Examples |
|--------|-------|----------|
| **CERTIFIED (100%)** | 5 | astar, merge_sort, nqueens, subset_sum, topological_sort |
| **PARTIAL (50-82%)** | 6 | kruskal, bfs, binary_search, bellman_ford, dfs, edit_distance |
| **FAILED (<50%)** | 22 | dijkstra, floyd_warshall, knapsack_01, lcs, and others |

**Recommendation:** Start with certified scaffolds for the best experience.

---

### Q: Why do so many scaffolds fail verification?

**A:** Most failures are **LLM algorithmic errors**, not framework problems. Common issues:

| Issue | Affected Scaffolds |
|-------|-------------------|
| Priority queue management | dijkstra |
| Matrix operations | floyd_warshall, matrix_chain |
| Greedy choice interpretation | activity_selection, fractional_knapsack |
| Tree construction | huffman, trie |
| Hash calculations | rabin_karp |
| Numerical precision | newton_raphson, bisection |

These represent opportunities to improve scaffold designs to better guide LLMs.

---

### Q: How can I help improve failing scaffolds?

**A:**

1. Analyze failure reports in `verification_results/reports/`
2. Identify patterns in LLM errors
3. Propose scaffold modifications:
   - Add more explicit state tables
   - Break complex steps into sub-steps
   - Add verification checkpoints
4. Test with `python verify.py <scaffold>`
5. Submit improvements with before/after pass rates

See [Developer Guide - Improving Failing Scaffolds](DEVELOPER_GUIDE.md#improving-failing-scaffolds) for strategies.

---

### Q: Do I need the verification framework to use scaffolds?

**A:** No! The verification framework is completely optional. You can use scaffolds by simply copying them into any AI assistant.

The verification framework is for:
- Developers who want to validate scaffold correctness
- Quality assurance before releasing new scaffolds
- Generating certification documentation

---

### Q: How do I run verification?

**A:** Three simple steps:

```bash
# 1. Install dependencies
pip install -r requirements-verification.txt

# 2. Set your API key
export ANTHROPIC_API_KEY=your_key_here

# 3. Run verification
python verify.py dijkstra          # Single scaffold
python verify.py --category graph  # All graph algorithms
python verify.py                   # All 33 scaffolds
```

---

### Q: What does "CERTIFIED" mean?

**A:** Certification status indicates scaffold reliability:

| Status | Pass Rate | Meaning |
|--------|-----------|---------|
| CERTIFIED | ≥90% | Works reliably, ready for use |
| PARTIAL | 50-89% | Works but may have edge case issues |
| FAILED | <50% | Has significant problems |

---

### Q: How much does verification cost?

**A:** Costs depend on the model used:

| Mode | Model | Per Scaffold | All 33 Scaffolds |
|------|-------|-------------|------------------|
| `dev` (default) | Claude Haiku | ~$0.01 | ~$0.30 |
| `cert` | Claude Opus | ~$0.50 | ~$15.00 |

**Tip:** Use `dev` mode for iteration, `cert` mode only for final certification.

---

### Q: Why does verification use Claude only?

**A:** The initial implementation focuses on Claude for:
- Consistent, reproducible results
- High-quality instruction following
- API simplicity

Future versions may add support for other LLMs (GPT-4, Gemini, etc.).

---

### Q: A scaffold failed verification. What should I do?

**A:** Follow these steps:

1. **Check the report**: `verification_results/reports/<scaffold>_report.md`
2. **Look at failures**: Compare "Expected" vs "Actual" values
3. **Identify the issue**:
   - **Parsing error**: LLM output format unexpected
   - **Algorithm error**: LLM got wrong answer
   - **Edge case**: Scaffold doesn't handle boundary conditions
4. **Fix the scaffold** or **adjust the test**

---

### Q: Can I add verification for my custom scaffold?

**A:** Yes! See [Developer Guide - Adding to Verification](DEVELOPER_GUIDE.md#adding-a-new-scaffold-to-verification) for:

1. Adding reference implementation
2. Registering the scaffold
3. Adding output format
4. Adding response parser

---

### Q: Where are verification results stored?

**A:** Results are saved to `verification_results/`:

```
verification_results/
├── data/                    # Raw JSON results
│   ├── dijkstra.json
│   └── ...
└── reports/                 # Markdown reports
    ├── dijkstra_report.md
    └── CERTIFICATION_SUMMARY.md
```

---

### Q: How do I regenerate reports without re-running tests?

**A:**
```bash
python verify.py report
```

This regenerates markdown reports from existing JSON data.

---

### Q: What libraries are used as ground truth?

**A:**

| Category | Library |
|----------|---------|
| Graph algorithms | networkx |
| Numerical methods | scipy |
| General computation | numpy |
| DP/Greedy/Backtracking | Custom verified implementations |

These are industry-standard, well-tested libraries.

---

## Contributing

### Q: How can I contribute to this project?

**A:** Several ways:

1. **Add scaffolds:** Create scaffolds for algorithms not covered
2. **Improve existing:** Better explanations, more examples
3. **Fix errors:** Correct mistakes in scaffolds
4. **Add documentation:** Help make things clearer
5. **Share feedback:** Report what works and what doesn't

See [Developer Guide](DEVELOPER_GUIDE.md) for details.

---

### Q: I found an error in a scaffold. What do I do?

**A:**

1. **Verify it's an error:** Test with multiple AIs
2. **Document the error:** Note what went wrong
3. **Report it:** Open an issue or contact maintainers
4. **Suggest fix:** If you know the correction, include it

---

### Q: Can I use these scaffolds in my own projects?

**A:** Yes! This project is for educational and research purposes. You can:

- Use scaffolds in your work
- Modify them for your needs
- Share them with others
- Build on them for your own tools

Attribution appreciated but not required.

---

## Still Have Questions?

- Check the [Glossary](GLOSSARY.md) for term definitions
- Read the full [User Guide](USER_GUIDE.md)
- Try more examples in [Quick Start](QUICK_START.md)
- Review specific scaffolds in the `scaffolds/` folder
