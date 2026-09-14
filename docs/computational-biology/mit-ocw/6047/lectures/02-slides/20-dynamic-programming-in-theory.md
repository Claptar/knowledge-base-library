---
title: Dynamic Programming in Theory
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Dynamic Programming in Theory

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Hallmarks of Dynamic Programming

   - **Optimal substructure:** Optimal solution to problem (instance) contains optimal solutions to sub-problems

   - **Overlapping subproblems:** Limited number of distinct subproblems, repeated many many times

- Typically for optimization problems (unlike Fib example) – Optimal choice made locally:  max( subsolution score)

   - Score is typically added through the search space

   - Traceback common, find optimal path from indiv. choices

- Middle of the road in range of difficulty – Easier: greedy choice possible at each step

   - DynProg: requires a traceback to find that optimal path

   - Harder: no opt. substr., e.g. subproblem dependencies

24

---

[← Lessons from iterative Fibonacci algorithm](19-lessons-from-iterative-fibonacci-algorithm.md) · [Up: contents](index.md) · [Hallmarks of optimization problems →](21-hallmarks-of-optimization-problems.md)
