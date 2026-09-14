---
title: 'DP approach: iteratively grow best alignment soltn'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DP approach: iteratively grow best alignment soltn

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_i_

S1 <mark>A C G T C A T C A</mark>

S2 <mark>T A G T G T C A</mark> _j_

- Compute all alignment scores from the bottom up – Define M[i,j] prefix alignment score of S1[1..i] and S2[1..j]

   - Fill up table recursively from smaller to bigger alignments

- Express alignment of S1[1..i+1] and S2[1..j+1]  M[i+1,j+1] – One of three possibilities: (1) extend alignment from M[i,j] (2) extend from M[i-1,j], or (3) extend from M[i,j-1]

   - Only a local computation, takes O(1) time!

- Proof of correctness (cut-and-paste argument from 6.006) – Best alignment of S1[1..i+1] and S2[1..j+1] must be composed of best alignments of smaller prefix

   - Proof: otherwise could replace sub and get better overall

36

---

[← Key insight #5: Optimal alignment  Matrix path](31-key-insight-5-optimal-alignment-matrix-path.md) · [Up: contents](index.md) · [Computing alignments recursively: M[i,j]=F(smaller) →](33-computing-alignments-recursively-m-i-j-f-smaller.md)
