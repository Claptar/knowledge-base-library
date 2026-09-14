---
title: 'Computing alignments recursively: M[i,j]=F(smaller)'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computing alignments recursively: M[i,j]=F(smaller)

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- <u>Local update rules, only look at neighboring cells:</u> – Compute next alignment based on previous alignment

   - Just like Fibonacci numbers:  F[i] = F[i-1] + F[i-2]

   - Table lookup avoids repeated computation

- Computing the score of a cell from smaller neighbors M( i-1, j  ) -  gap <u>i-1 i</u>

- – M(i,j) = max{ M( i-1, j-1) + score } j-1 M(  i ,  j-1) -  gap j **(i,j)**

   - Only three possibilities for extending by one nucleotide: a gap in one species, a gap in the other, a (mis)match

- Compute scores for prefixes of increasing length – Start with prefixes of length 1, extend by one each time, until all prefixes have been computed

   - When you reach bottom right, alignment score of S1[1..m] and S2[1..n] is alignment of full S1 and full S2

– (Can then trace back to construct optimal path to it)

37

---

[← DP approach: iteratively grow best alignment soltn](32-dp-approach-iteratively-grow-best-alignment-soltn.md) · [Up: contents](index.md) · [Dynamic Programming for sequence alignment →](34-dynamic-programming-for-sequence-alignment.md)
