---
title: 'From Bio to CS: Formalizing the problem'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# From Bio to CS: Formalizing the problem

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Define set of evolutionary operations (insertion, deletion, mutation) – Symmetric operations allow time reversibility (part of design choice)


<!-- Start of picture text -->
Human  Mouse<br>x  y  x  y<br>x+y<br>Human  Mouse  Human  Mouse<br><!-- End of picture text -->

- (Exception: methylated CpG dinucleotides  TpG/CpA non-symmetric)


<!-- Start of picture text -->
• Define optimality criterion (min number, min cost)<br>–Impossible to infer exact series of operations (Occam’s razor: find min)<br>Many possible transformations<br>Human  Mouse<br>Minimum cost transformation(s)<br><!-- End of picture text -->

- Design algorithm that achieves that optimality (or approximates it) –Tractability of solution depends on assumptions in the formulation


<!-- Start of picture text -->
Bio  Predictability  Algorithms  CS<br>Assumptions<br>Relevance  Tradeoffs<br>Implementation Tractability<br>Correctness<br>Computability<br>Special cases<br><!-- End of picture text -->

Note: Not all decisions are conflicting (some are both relevant and tractable) (e.g. Pevzner vs. Sankoff and directionality in chromosomal inversions)

11

---

[← Goal of alignment: Infer edit operations](07-goal-of-alignment-infer-edit-operations.md) · [Up: contents](index.md) · [Formulation 1: Longest common substring →](09-formulation-1-longest-common-substring.md)
