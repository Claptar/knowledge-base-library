---
title: 'Traceback #3'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Traceback #3

**Source:** `psets/03-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|7|
|---|


**(B – 2 points)** Run this sequence through the mfold RNA folding server (default parameters) at: http://mfold.rit.albany.edu/?q=mfold/RNA-Folding-Form

Examine the top two structures it produces by looking at the “pdf”s under “View Individual Structures:”. Notice that they don’t match the structure predicted by the Nussinov algorithm. Examining the examples of real RNA secondary structures shown in lecture (slides 12, 32, 39 of Lecture 11), generate a hypothesis for which criteria used by the mfold algorithm to describe RNA thermodynamics prevents this algorithm from predicting the structure returned by the Nussinov algorithm in part (A). Test your hypothesis by strategically inserting adenosines at locations (e.g. in loops, between stems, across from bulges) necessary in the sequence above and finding the minimum number that must be inserted so that the top mfold-predicted structure has pairs between the same bases as in your Nussinov base pair-maximization structure.


<!-- Start of picture text -->
5’<br>A<br>C G G<br>C G<br>G<br>G C<br>U A<br>U<br>G<br>G G<br>10<br>A<br>A U<br>10 G<br>C G C 3’<br>U<br>3’ dG = 2.00 [Initially 2.00] 14Mar19-13-48-56-dcddac9b93 C 5’<br><!-- End of picture text -->

The top two structures are shown above - the loops in the two hairpins of the Nussinov algorithm-predicted structure are too short (only 1 G each) – real loops must be at least 3 bases long.

Inserting A’s next to the G in the first loop reveals that 3 A’s must be added for the first stem to pair all three given by the Nussinov algorithm (C/G, G/C, A/U). Because the two stems are also too close to one other (no nucleotides between the two G’s at the bases of the loops), one A must be added between these two G’s. Similarly, three A’s must be added to the second loop so it’s large enough to pair the two in that stem (G/C and A/U). With this sequence CGAGAAAUCGAGAGAAAUC, the structure that has the same two stems as the Nussinovderived structure is:


<!-- Start of picture text -->
5’<br>G<br>C G A A<br>G C U A<br>A<br>A<br>10 G<br>G A A<br>C U A<br>A<br><!-- End of picture text -->


<!-- Start of picture text -->
3’<br><!-- End of picture text -->


<!-- Start of picture text -->
dG = -3.50 [Initially -3.30] 14Mar19-13-55-37-4bcffdf8e8<br><!-- End of picture text -->

9

---

[← Folded structure for tracebacks #2 and 3](08-folded-structure-for-tracebacks-2-and-3.md) · [Up: contents](index.md) · [P3. Protein structure with PyRosetta (6 points). →](10-p3-protein-structure-with-pyrosetta-6-points.md)
