---
title: Linear-time string matching
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Linear-time string matching

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- When looking for exact matches of a pattern (no gaps)

- Karp-Rabin algorithm (probabilistic linear time): – Interpret String numerically

   - Start with ‘broken’ version of the algorithm

   - Progressively fix it to make it work

- Deterministicc linear-time solutions exist (not this term): – Z-algorithm / fundamental pre-processing, Gusfield

   - Boyer-Moore and Knuth-Morris-Pratt algorithms are earliest instantiations, similar in spirit

   - Suffix trees: beautiful algorithms, many different variations and applications, limited use in CompBio

   - Suffix arrays: practical variation, Gene Myers

19

---

[← Today’s Goal: Diving deeper into alignments](15-today-s-goal-diving-deeper-into-alignments.md) · [Up: contents](index.md) · [Karp-Rabin algorithm →](17-karp-rabin-algorithm.md)
