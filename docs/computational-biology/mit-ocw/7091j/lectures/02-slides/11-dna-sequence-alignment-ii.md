---
title: DNA Sequence Alignment II
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DNA Sequence Alignment II

**Source:** `lectures/02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Determining significance of nucleotide local alignments

Q: 1   ttgacctagatgagatgtcgttcacttttactcaggtacagaaaa 45 |||| |||||||||||| | |||||||||||| || ||||||||| S: 403 ttgatctagatgagatgccattcacttttactgagctacagaaaa 447 Identify high scoring segments whose score S exceeds a cutoff x using a **local alignment** algorithm (e.g., BLAST) Scores follow an extreme value (aka Gumbel) distribution:

P(S > x) = 1 - exp[-KMN e<sup>-λx</sup> ]

For sequences/databases of length M, N where K, λ are positive parameters that depend on the score matrix and the composition of the sequences being compared

Conditions: expected score is negative, but positive scores possible

Karlin & Altschul 1990

20

### Extreme Value (Gumbel) Distribution


21

---

[← DNA Sequence Alignment I: Motivation](10-dna-sequence-alignment-i-motivation.md) · [Up: contents](index.md) · [DNA Sequence Alignment III →](12-dna-sequence-alignment-iii.md)
