---
title: How many alignments are there?
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# How many alignments are there?

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### S1 <mark>A C G T C A T C A</mark>

S2


<mark>T A G T G T C A</mark>

- Longest ‘non-boring’ alignment: n+m entries – Otherwise a gap will be aligned to a gapcondense

- Alignment is equivalent to gap placement – (n+m choose n) ways to choose S1 placement

   - At each position yes/no answer of placing character

   - Exponential number of possible placements

- Exponential number of sequence alignment – Enumerating and scoring each of them not an option

   - Need faster solution for finding best alignment

Need **polynomial** algorithm to find best alignment amongst an **exponential** number of possible alignments!

 DP

16

---

[← Formulation 4: Varying gap cost models](12-formulation-4-varying-gap-cost-models.md) · [Up: contents](index.md) · [Goal: Sequence Alignment / Dynamic Programming →](14-goal-sequence-alignment-dynamic-programming.md)
