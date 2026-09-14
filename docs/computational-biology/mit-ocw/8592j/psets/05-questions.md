---
title: 05 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 05 questions

**Source:** `psets/05-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 5

# Protein Folding

1. Designed Random Energy Model (REM): Consider a protein model in which for a given sequence and structure, the energy is randomly taken from the Gaussian probability density


The total number of structures is Ωstr, while the number of sequences is Ωseq ≫ Ωstr.

(a) A particular sequence has a (unique) native structure of energy EN . Calculate and plot the energy E(T ) of this sequence as a function of temperature T .

(b) For a particular structure, we attempt to design a good sequence by Monte Carlo sampling of representative sequences at a ‘temperature’ τ . Calculate and plot the designed native energies EN (τ ) as a function of the design temperature τ .

*****

2. Charged Random Energy Model: Use the random energy model to investigate the freez­ ing of a charged heteropolymer. Assume that there are g<sup>N</sup> possible globular states of the polymer, whose energies are randomly selected from a Gaussian distribution of mean zero, and variance


The second term in the above formula is a rough estimate of the variations in Coulomb energy from different ways of distributing a charge Q over a volume of size R.

(a) Find the energy Ec at which the entropy vanishes, and the corresponding freezing tem­ perature Tc.

(b) For compact globular states, how should Q<sup>2</sup> scale with N for the freezing temperature to be asymptotically independent of N?

*****

3. Amino-acid interactions: What can we learn by combining the Random Energy Model with commonly used interaction potentials between amino acids?

(a) Find a 20 × 20 matrix of interactions U(a, a<sup>′</sup> ) amongst amino acids, and calculate the mean (U) and variance (U<sup>2</sup> )c of its elements. The commonly used Miyazawa–Jernigan (MJ) interaction matrix can be found in S. Miyazawa and R.L. Jernigen, J. Mol. Biol. 256, 623 (1996). (Table 3 of this publication is available on the web-page for assignments.)

(b) Model the possible configurations of a protein by the ensemble of compact self-avoiding walks on a cubic lattice. (All lattice sites are visited by compact walks.) Calculate the number n of non-polymeric nearest neighbor interactions for such configurations on an N = L × L × L lattice, and deduce the ratio n/N for large N.

1

(c) The number of compact walks on a cubic lattice asymptotically grows as g<sup>N</sup> , with g ≈ 1.85. Use this in conjunction with the results from parts (a) and (b) to estimate the folding temperature Tc of a random sequence of amino-acids, and the corresponding energy Ec. (Optional) (d) Select a protein, find its amino-acid sequence and construct a contact matrix corresponding to its structure. Use the interaction matrix from part (a) to estimate the energy of the native structure, and calculate the ratio EN /Ec.

*****

4. Analysis of protein structures: Calculate φ and ψ torsion angles in Rasmol for a given protein (see the commands below). Make (φ, ψ) “Ramachandran” diagrams by plotting φ along the x and and ψ along the y axis; one (φ, ψ) point for each amino acid.

(a) Do amino acids that are part of different secondary structure elements (helices, sheets) land in the same or different islands on the (φ, ψ) diagram? You can find secondary structure elements in fields HELIX and SHEET of the protein structure file (aka PDB file). Explain your observations.

(b) Find amino acids that have unusual (φ, ψ) angles (i.e. deviate from the many clouds of points). What types of amino acids tend to have “unusial” (φ, ψ) conformation? Discuss. (c) Visualize protein structure in Rasmol, following the sequence of commands below, and select those with “unusual” (φ, ψ) conformation. Do they tend to be close to the ligand? Some sample proteins to explore (PDB files provided on the Assignment page): Hemoglobin (alpha chain) 4HHB A.PDB

Immunoglobulin domain 1TEN.PDB

You can use the following sequence of Rasmol commands to generate a good view of a protein, and the fipsi.dat file of (φ, ψ) angles

set background white

wireframe off ribbons

color structure select ligand cpk color green select protein write RDF fipsi.dat

To select a particular set of amino acids, (e.g. 128 and 156) you can do the following select 128,156 cpk color red

*****

2

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
