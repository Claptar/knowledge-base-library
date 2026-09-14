---
title: Algorithmic variations (save time and/or space)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Algorithmic variations (save time and/or space)

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### `AGTGCCCTGGAACCCTGACGGTGGGTCACAAAACTTCTGGA`


- Save time:  Bounded-space computation

   - Space: O(k*m)

   - Time:   O(k*m), where k = radius explored

   - Heuristic

      - Not guaranteed optimal answer

      - Works very well in practice

   - Practical interest


<!-- Start of picture text -->
AGTGACCTGGGAAGACCCTGACCCTGGGTCACAAAACTC<br><!-- End of picture text -->

###### `AGTGCCCTGGAACCCTGACGGTGGGTCACAAAACTTCTGGA`


- Save space:  Linear-space computation – Save only one col / row / diag at a time

   - Computes optimal score easily

   - Theoretical interest

      - Effective running time slower

      - Optimal answer guaranteed

   - Recursive call modification allows traceback

7

---

[← Computing alignments recursively: M[i,j]=F(smaller)](04-computing-alignments-recursively-m-i-j-f-smaller.md) · [Up: contents](index.md) · [Finding optimal path using only linear space →](06-finding-optimal-path-using-only-linear-space.md)
