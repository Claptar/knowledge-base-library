---
title: The naïve string-matching algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The naïve string-matching algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• NAÏVE STRING MATCHING

1

2 3 4 5

– n  length[T]

– m length[P]

– **for** shift  0 **to** n

- **do if** P[1..m] == T[shift+1 .. shift+m]

   - **then** print “Pattern occurs with shift” shift

Running time:

O(n) O(m)

- Where the test operation in line 4: – Tests each position in turn

   - If match, continue testing

• else: stop

- Running time ~ number of comparisons number of shifts (with one comparison each) + number of successful character comparisons

37

---

[← Basic string definitions](32-basic-string-definitions.md) · [Up: contents](index.md) · [Comparisons made with naïve algorithm →](34-comparisons-made-with-naïve-algorithm.md)
