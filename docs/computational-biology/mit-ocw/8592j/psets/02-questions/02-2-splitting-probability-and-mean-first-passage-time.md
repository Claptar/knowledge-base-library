---
title: 2. Splitting probability and mean first passage time
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Splitting probability and mean first passage time

**Source:** `psets/02-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) Consider a particle diffusing without a drift (v = 0, D = const) on an interval [0, 1] that has adsorbing boundaries. The particle starts at 0 < x < 1 and diffuses until it gets adsorbed by either of the boundaries. Using backward Kolmogorov equations calculate the probabilities of adsorption (splitting probabilities) by either boundary Π0(y) and Π1(y).

(b) Obtain the expression for the mean first passage time t(y) through either boundary (survival time). Find the location ymax that provides the longest mean life-time for the particle.

(c) (Optional) Consider a generalization of the same problem to two dimensions, with two concentric circles of radii R0 < R1 centered at the origin. A particle starts a 2D diffusion

1

(without a drift) at distance R (R0 < R < R1) from the origin. Use the general form of the equations for slitting probabilities ∇<sup>2</sup> Π = 0 and mean exit time D∇<sup>2</sup> t = −1 to calculate Π0(R), Π1(R) and t(R). Find the initial distance Rmax that provides the longest life-time. Compare to result obtained for one dimension.

(d) (Optional) Consider the same problem in three dimensions with two concentric spheres. Compare results in 1D, 2D and 3D. How do the split of probabilities between the inner and the outer boundaries, and Rmax change as the dimensionality of the system increases from 1 to 3?

*****

3. Number of gapped alignments: The following problem is taken from Chapter 2 of Durbin et. al., which provides the needed background on sequence alignments.

(a) Show that the number of ways of intercalating two sequences of lengths n and m to produce a sequence of length n + m, while preserving the order of symbols is � n+mm�. For example (B1, A1, B2, B3, A2) is a possible intercalation of (A1, A2) with (B1, B2, B3). (Note a similarity to number of ways of distributing m quanta of energy between n + 1 harmonic oscillators.)

(b) By taking alternating symbols from the upper and lower sequences in an alignment, then discarding the gap characters, show that there is a one-to-one correspondence between gapped alignments of two sequences and intercalated sequences of the type described in part (a). The example in part (a) thus corresponds to the alignment � B−1 AB12 −B3A−2 �. Hence obtain the number of possible gapped alignments between two sequences of length n. (c) Use Stirling’s approximation (x! ≈ √2πx<sup>x+1/2</sup> e<sup>−x</sup> ) to simplify the expression for the number of alignments of two sequences of length n. *****

4. Alignments: Calculate the dynamic programming matrices and the optimal global and local alignments for the DNA sequences GAATTC and GATTA, scoring +1.5 for a match, -1 for a mismatch, and with a penalty of 2 for each gap. Do you get different alignments? Do you notice ambiguity in the global alignment?

*****

5. Random Sequences and BLAST: Sequence alignments can be performed online using the programs and data provided by the National Center for Biotechnology Information (NCBI). To better understand the underlying program, read the paper on BLAST, Gapped BLAST and PSI-BLAST: a new generation of protein database search programs, by Altschul SF, Madden TL, Schaffer AA, Zhang J, Zhang Z, Miller W, Lipman DJ, Nucleic Acids Res. 25, 3389-3402 (1997). (This paper is available on the course web-page in the Assignment section.)

(a) Generate a random amino acid sequence and run it against a database of non-redundant sequences employing BLAST (http://www.ncbi.nlm.nih.gov/BLAST/); use the standard protein-protein BLAST [blastp]. Repeat your runs for several times and for sequences of different length (10-1500 amino acids). Did you find any “false homologous” in the database?

2

(b) Generate a random amino acid sequence with amino acid frequencies from the table below and with PERIODICITY of hydrophobic and non-hydrophobic residues. (Hint: the first 10 amino acids in the table below are hydrophobic.) Run these sequences using BLAST. Interpret your results.

(c) Take an amino acid sequence (a protein of your choice, or one of proteins suggested below) and introduce X% of random mutations. Run mutated proteins against the database using BLAST or PSI-BLAST (same web page). Try different frequency of mutations (X = 0, · · · 100%). What level of mutations is tolerated by BLAST? by PSI-BLAST? Interpret your results.

(d) (Optional) Introduce X% of mutations such that a hydrophobic amino acid is substituted by a random hydrophobic one and a polar is substituted by a polar one. Run using BLAST. Did the threshold level for X change?

Table of Amino Acid Frequencies, and their single letter designation (in parenthesis) CYS 1.660 (C) MET 2.370 (M) PHE 4.100 (F) ILE 5.810 (I) LEU 9.430 (L) VAL 6.580 (V) TRP 1.240 (W) TYR 3.190 (Y) ALA 7.580 (A) GLY 6.840 (G) THR 5.670 (T) SER 7.130 (S) GLN 3.970 (Q) ASN 4.440 (N) GLU 6.360 (E) ASP 5.270 (D) HIS 2.240 (H) ARG 5.160 (R) LYS 5.940 (K) PRO 4.920 (P)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Some suggested sequences →](03-some-suggested-sequences.md)
