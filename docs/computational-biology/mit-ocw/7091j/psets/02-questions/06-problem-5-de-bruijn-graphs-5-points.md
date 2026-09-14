---
title: Problem 5. de Bruijn graphs (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 5. de Bruijn graphs (5 points)

**Source:** `psets/02-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose you are interested in sequencing a particular RNA sequence. You opt to take a next generation sequencing approach and submit your sample to your local sequencing facility. You receive the following set of 6 bp reads in return, which are all in the same orientation.

AGCTGT, CAGCTG, TTCTGC, GCTGTA, TCAGCT, CTGTAT, TGTAGC, TTCAGC, CTGTAG, TTTCAG

- **(A) (1 pt.)** Construct the corresponding de Bruijn graph with k = 5

- **(B) (1 pt.)** Simplify any chains in the graph. Remove any tips present in the graph.

- **(C) (1 pt.)** Identify any bubbles in the graph. Resolve the bubbles by removing the path

   - most likely to be caused by a sequencing error.

- **(D) (1 pt.)** Which read(s) contain sequencing errors? Identify the error(s).

- **(E) (1 pt.)** Write the sequence represented by the de Bruijn graph after the error correction steps.

7


8

---

[← Problem 3. Differential gene expression (4 points)](05-problem-3-differential-gene-expression-4-points.md) · [Up: contents](index.md) · [Problem 6. Modeling and information content of sequence motifs (5 points). →](07-problem-6-modeling-and-information-content-of-sequence-motif.md)
