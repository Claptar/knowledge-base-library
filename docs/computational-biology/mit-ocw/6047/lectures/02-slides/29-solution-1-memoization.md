---
title: 'Solution #1 – Memoization'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution #1 – Memoization

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Create a big dictionary, indexed by aligned seqs – When you encounter a new pair of sequences

   - If it is in the dictionary:

      - Look up the solution

   - If it is not in the dictionary

      - Compute the solution

      - Insert the solution in the dictionary

- Ensures that there is no duplicated work

   - Only need to compute each sub-alignment once!

**Top down approach**

32

---

[← Key insight #3: sub-problems are repeated  reuse!](28-key-insight-3-sub-problems-are-repeated-reuse.md) · [Up: contents](index.md) · [Solution #2 – Dynamic programming →](30-solution-2-dynamic-programming.md)
