---
title: • Setting up dynamic programming
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# • Setting up dynamic programming

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Find ‘matrix’ parameterization (# dimensions, variables)

2. Make sure sub-problem space is finite! (not exponential) • If not all subproblems are used, better off using memoization

• If reuse not extensive, perhaps DynProg is not right solution!

3. Traversal order: sub-results ready when you need them • Computation order matters!  (bottom-up, but not always obvious)

**4. Recursion formula:  larger problems = F(subparts)**

5. Remember choices: typically F() includes min() or max()

- Need representation for storing pointers, is this polynomial !

- • Then start computing

   1. Systematically fill in table of results, find optimal score

2. Trace-back from optimal score, find optimal solution

26

---

[← Dynamic Programming in Practice](22-dynamic-programming-in-practice.md) · [Up: contents](index.md) · [Goal: Sequence Alignment / Dynamic Programming →](24-goal-sequence-alignment-dynamic-programming.md)
