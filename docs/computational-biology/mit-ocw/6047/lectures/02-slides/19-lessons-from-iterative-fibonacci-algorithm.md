---
title: Lessons from iterative Fibonacci algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lessons from iterative Fibonacci algorithm

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

fib_table F[1] 1 F[2] 1 F[3] 2 F[4] 3 F[5] 5 F[6] 8 F[7] 13 F[8] 21 F[9] 34 F[10] 55 F[11] 89 F[12] **?**

- What did the iterative solution do? – Reveal identical sub-problems

   - Order computation to enable result reuse

   - Systematically filled-in table of results

   - Expressed larger problems from their subparts

- Ordering of computations matters

   - Naïve top-down approach very slow

      - results of smaller problems not available

      - repeated work

   - Systematic bottom-up approach successful

      - Systematically solve each sub-problem

      - Fill-in table of sub-problem results in order.

      - Look up solutions instead of recomputing

23

---

[← Computing Fibonacci numbers: Bottom up](18-computing-fibonacci-numbers-bottom-up.md) · [Up: contents](index.md) · [Dynamic Programming in Theory →](20-dynamic-programming-in-theory.md)
