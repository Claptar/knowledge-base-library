---
title: P2. RNA secondary structure prediction (5 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions-pset3-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/03-questions-pset3-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P2. RNA secondary structure prediction (5 points).

**(A - 3 points)** Use the Nussinov algorithm to find the secondary structure that maximizes the number of Watson-Crick base-pairs in the following RNA sequence (show your work):

CGAGUCGGAGUC

---

**(B – 2 points)** Run this sequence through the mfold RNA folding server (default parameters) at:

http://mfold.rit.albany.edu/?q=mfold/RNA-Folding-Form

Examine the top two structures it produces by looking at the "pdf"s under "View Individual Structures:". Notice that they don't match the structure predicted by the Nussinov algorithm. Examining the examples of real RNA secondary structures shown in lecture (slides 12, 32, 39 of Lecture 11), generate a hypothesis for which criteria used by the mfold algorithm to describe RNA thermodynamics prevents this algorithm from predicting the structure returned by the Nussinov algorithm in part (A). Test your hypothesis by strategically inserting adenosines at locations (e.g. in loops, between stems, across from bulges) necessary in the sequence above and finding the minimum number that must be inserted so that the top mfold-predicted structure has pairs between the same bases as in your Nussinov base pair-maximization structure.

---

---

[← P1. Gibbs Sampler (10 Points).](01-p1-gibbs-sampler-10-points.md) · [Up: contents](index.md) · [P3. Protein Structure with PyRosetta (6 Points). →](03-p3-protein-structure-with-pyrosetta-6-points.md)
