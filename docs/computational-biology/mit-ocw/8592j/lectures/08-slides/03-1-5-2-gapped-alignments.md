---
title: 1.5.2 Gapped alignments
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/08-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.5.2 Gapped alignments

**Source:** `lectures/08-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Comparison of biological sequences indicates that in the process of evolution sequences not only mutate, but also lose or gain elements. Consequently, useful alignments must allow for gaps and insertions (more so for more evolutionary divergent sequences). In the scoring

25

process, it is typical to add a cost that is linear in the size of the gap (and sometimes extra costs for the end-points of the gap). Dynamic programming algorithms can be constructed (e.g. below) to deal with gapped alignments, but obtaining analytical results is now much harder. Empirically, it can be verified that the PDF for the score of random gapped local alignments is still Gumbel distributed. This result could again be justified by noting that local alignments rely of selecting the best score amongst a large number. The shape of the ‘islands’ is now slightly different, and their statistics is harder to obtain, as discussed below.

Gaps/insertation can be incorporated in the earlier diagrammatic representation by sideway steps from one column x to another. The sideway step does not advance along the coordinate corresponding to the sequence with gap, but progresses over the characters of the other sequence. As depicted below, these resulting trajectories are still pointed downwards, but may include transverse excursions. Such directed paths occur in many contexts in physics from flux lines in superconductors to domain walls in two-dimensional magnets.


In the spirit of statistical physics we may even introduce a fuzzier version of alignment corresponding to a finite temperature β<sup>−1</sup> . We can then regards the scores as (negative) energies used to construct Boltzmann weights e<sup>βS</sup> to various paths. Now consider the constrained partition function

W (x, t) = sum of all paths’ Boltzmann weights from (0, 0) to (x, t). (1.114)

We can use a so-called transfer matrix to recursively compute this quantity by

W (x, t) = e<sup>βs(x,y)</sup> W (x, t − 2) + e<sup>−βg</sup> [W (x + 1, t − 1) + W (x − 1, t − 1)] . (1.115)

The first term is the contribution from the configuration that goes down along the same x, while the remaining two come from neighboring columns (at a cost g in gap energy).

The above transfer matrix is the finite temperature analog of dynamic programming, and indeed in the limit of β →∞, the sum in Eq. (1.115) is dominated by the largest term, leading to (W (x, t) = exp [βS(x, t)])

S(x, t) = max {S(x, t − 2) + s(x, t), S(x + 1, t − 1) − g, S(x − 1, t − 1) − g} . (1.116)

This analogy has been used to obtain certain results for gapped alignment, but will not be pursued further here.

26

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 1.5.1 Significance of gapless alignments](02-1-5-1-significance-of-gapless-alignments.md) · [Up: contents](index.md)
