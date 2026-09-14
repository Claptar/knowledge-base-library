---
title: 'Karp-Rabin algorithm: Putting it all together'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Karp-Rabin algorithm: Putting it all together

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

T= 2 3 5 9 0 2 3 1 4 1 5 2 6 7 3 9 9 2 1 y1 = 23,590 y7 = 31,415 y2 = 35,902 **`compute x (mod p)`** y3 = 59,023 `for i in [1..n]:` **`compute yi (mod p) (using yi-1)`** P= 3 1 4 1 5 `if` **`x == yi`** `:` **`if P==S[i..]:`** x = 31,415 `print “match at` **`S[i]`** `”` **`else: (spurious hit)`**

- Key idea: Semi-numerical computation (this actually works) – **Idea: Interpret strings as numbers => fast comparison** (other semi-numerical methods:  Fast Fourier Transform,  Shift-And)

      - (this actually works)

- To make it work:

   - **(a) Compute next number based on previous one**  **O(1) (b) Hashing (mod p)**  **keep the numbers small**  **O(1)**

   - **(c) Dealing with collisions**  **Randomized p, expected run time**  **O(1) exp**

25

---

[← (c) Dealing with collisions, due to hashing](21-c-dealing-with-collisions-due-to-hashing.md) · [Up: contents](index.md) · [Today’s Goal: Diving deeper into alignments →](23-today-s-goal-diving-deeper-into-alignments.md)
