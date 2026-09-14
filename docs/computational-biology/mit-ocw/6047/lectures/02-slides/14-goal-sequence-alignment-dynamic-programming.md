---
title: 'Goal: Sequence Alignment / Dynamic Programming'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Goal: Sequence Alignment / Dynamic Programming

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Introduction to sequence alignment

   - Comparative genomics and molecular evolution

   - From Bio to CS: Problem formulation

– Why it’s hard: Exponential number of alignments 2. Introduction to principles of dynamic programming – Computing Fibonacci numbers: Top-down vs. bottom-up – Repeated sub-problems, ordering compute, table lookup

   - DP recipe: (1) Parameterization, (2) sub-problem space, (3) traversal order, (4) recursion formula, (5) trace-back

3. DP for sequence alignment

   - Additive score, building up a solution from smaller parts

   - Prefix matrix: finite subproblems, exponential paths

- Duality: each entryprefix alignment score; pathaligmnt

- 4. Advanced topics: Dynamic Programming variants

   - Linear-time bounded DP(heuristic). Linear-space DP. Gaps

   - Importance of parameterization: 2-D vs. 4-D decomposition

17

**A simple introduction to the principles of Dynamic Programming**

Turning exponentials into polynomials

18

---

[← How many alignments are there?](13-how-many-alignments-are-there.md) · [Up: contents](index.md) · [Computing Fibonacci Numbers →](15-computing-fibonacci-numbers.md)
