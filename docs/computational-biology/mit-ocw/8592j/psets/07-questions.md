---
title: 07 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/07-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 questions

**Source:** `psets/07-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 8.592J–HST.452J: Statistical Physics in Biology

Assignment # 7

Protein–DNA Interactions

1. Weight matrices: You are given a set of binding sites for the E. Coli purine repressor, PurR (see file purR sites.txt on the assignment page).

- (a) Build a weight matrix for wi(b) for base b at position i for PurR. Calculate the infor­ mation content of the set.

(b) Write a program that feeds random DNA sequences into the weight matrix, and con­ struct a histogram for the resulting weights. Use this histogram to compute the probability distribution of specific binding energies, assuming an effective evolutionary “temperature” equal to the ambient temperature T<sup>∗</sup> = 1/(kBλ) = T .

(c) Assume a binding threshold slightly above the average binding energy of the given set of sites. Find all the sequences in the E. coli genome (included on the Assignment page) having binding energy below this threshold. Have you located all the input sequences? Try to move the threshold. How many false-positives do you find? You can consult the provided gene table of E. coli (gene table.txt) to find out if the detected sequences have any regulatory function.

(d) Consider a simpler model of protein-DNA recognition, where the consensus sequence of DNA of length L provides the highest affinity (the lowest energy of binding), and each mismatch increases the binding energy by a constant ǫ. Calculate the information content of such motif. What is the probability of finding the consensus site in random DNA? How is the probability related to the information content?

*****

2. Target site location: Complex transcription machinery in cells is regulated by a set of protein molecules–transcription factors (TFs) whose functions can be described as:

• Receiving a control signal- This can be the binding or unbinding of a ligand, resulting in initiation or shutting down of the transcription machinery.

• Finding a specific site on the DNA and binding to it.


<!-- Start of picture text -->
TF<br><!-- End of picture text -->

(a) Suppose the protein has to locate a unique binding site on a genome of length M. It may do so by alternately diffusing in solution, and sliding along the DNA, as depicted in Fig. 1. Given a typical TF diameter of 10nm and cytoplasm dynamic viscosity of approximately

1

0.1 g s<sup>−1</sup> cm<sup>−1</sup> , estimate D3d for a TF in cytoplasm. (For 1D sliding, one can assume D1d ≈ 0.1 ∗ D3d.)

(b) Consider the mechanism of search by sliding and 3D diffusion discussed on the lecture. In addition to theses processes, a protein can make occasional hops, i.e. once it dissociates from DNA, it associates again at the same place. Calculate the total search time, assuming that upon dissociation a protein will make a hop with a probability p ≈ 0.9.

(c) Given the 1D diffusion coefficient D1d, obtain the optimal target location time tloc. The dissociation rate of the proteins from DNA is controlled by the nonspecific binding energy Ens. Estimate Ens for the optimal target location time. Assume D1d = 1µm<sup>2</sup> /sec, τ3d = 10<sup>−3</sup> sec. Find the location time for M = 10<sup>6</sup> base-pairs.

*****

3. Protein-DNA interaction through bending: In the worm-like chain (WLC) model, the energy cost of deformed piece of DNA of length L is


where κ is the bending modulus and R(s) is the local curvature radius. Proteins specifically bound to DNA introduce local “kinks” in the DNA structure. Consider the experimental setup in figure below.


<!-- Start of picture text -->
protein<br>θ (s)<br>DNA  F<br>X<br><!-- End of picture text -->

(a) Express the local curvature radius through the local inclination angle θ(s). Modify the above Hamiltonian to include the applied force F and write it down as H[θ(s)].

(b) By minimizing H, find the equation for θ(s). Assuming θ is small, solve the equation and calculate the extension X of the DNA as a function of F . Invert the relation and plot the function F (X).

(c) Calculate the energy cost of the DNA deformation. Given that near the protein, θ = 0.5 and that the energy of specific binding is 20 kBT , estimate the force at which the protein will “pop” from the DNA. Plot the modified force–extension curve.

*****

2

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
