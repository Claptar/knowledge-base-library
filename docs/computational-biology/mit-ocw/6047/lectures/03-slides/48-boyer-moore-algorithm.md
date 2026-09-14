---
title: Boyer-Moore algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Boyer-Moore algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

T= b a a b x c a b a b a d

P= a b a b x

- Three fundamental ideas:

   1. Right-to-left comparison

   2. Alphabet-based shift rule

   3. Preprocessing-based shift rule

- Results in:

   - Very good algorithm in practice

   - Rule 2 results in large shifts and sub-linear time

      - for larger alphabets, ex: English text

   - Rule 3 ensures worst-case linear behavior

      - even in small alphabets, ex: DNA sequences

53

---

[← Knuth-Morris-Pratt running time](47-knuth-morris-pratt-running-time.md) · [Up: contents](index.md) · [The Z algorithm →](49-the-z-algorithm.md)
