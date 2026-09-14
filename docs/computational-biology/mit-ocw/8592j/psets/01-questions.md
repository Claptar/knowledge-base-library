---
title: 01 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 questions

**Source:** `psets/01-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 1

Probability

1. Open Reading Frames: Assume that the nucleotides A, G, T, C occur with equal proba­ bility (and independently) along a segment of DNA.

(a) From the genetic code calculate the probability ps that a randomly chosen triplet of bases corresponds to a stop signal.

(b) What is the probability for an open reading frame (ORF) of length N, i.e. a sequence of N non-stop triplets followed by a stop codon?

(c) The genome of E-coli has roughly 5 × 106 bases per strand, and is in the form of a closed loop. If the bases were random, how many ORFs of length 600 (a typical protein size) would be expected on the basis of chance. (Note that there are six possible reading frames.)

*****

(Optional) 2. ORFs in E. coli: To compute the actual distribution of ORFs in E. coli you will need to download the complete sequence of its genome from ftp://ftp.ncbi.nih.gov/genbank/genomes/Bacteria/ Escherichia − coli −K −12 −substr − 1655/U00096.fna .

This file is also posted on the Assignments web-page.

(a) Write a program that goes through all consecutive (non-overlapping) triplets looking for stop codons. (Make sure you use the genetic code for DNA in the 5’-3’ direction.) Record the distance L between consecutive stop codons. Repeat this computation for the 3 different reading frames (0, +1, +2) in this direction. (You may skip calculations for the reverse strand, that is complementary to the given one and proceeding in the opposite direction.) (b) Plot the distribution for the ORF lengths L calculated above, and compare it to that for random sequences.

(c) Estimate a cut-off value Lcut, above which the ORFs are statistically significant, i.e. the number of observed ORFs with L > Lcut is much greater than expected by chance. *****

3. Point mutations in DNA: Since the four nucleotides in DNA have different chemical compositions and energetics, they could mutate at different rates. We shall explore whether, without natural selection at work, such preferential mutation may lead to different compo­ sitions of nucleotides.

(a) Consider a simple model in which all transversions (i.e. mutations between purines A and G, or between pyramidines T and C) occur with probability q, while transitions (i.e. any mutation from a purine to a pyrimidine or vice versa) occur with probability p, in each generation. Write down the 4 × 4 (Markov) transition matrix, Π1, that relates the frequencies of nucleotides (pA, pG, pT, pC) from one generation to the next. (Make sure that the normalization condition pA + pG + pT + pC = 1 is preserved.)

(b) Find the eigenvalues of the transition matrix Π1. (Hint: You should be able to simply guess the eigenvectors by considering the symmetries of the matrix.)

1

(c) Find the matrix Πt<sup>= Π</sup> t1<sup>, describing the evolution of probabilities aftertgenerations.</sup> (d) Show that in steady state (after many duplications), all nucleotides occur with the same frequency. Estimate the number of generations (as a function of p and q) needed to reach such a steady state.

(e) You should be able to convince yourself that for any model in which mutation rates between pairs of bases are the same in the forward and backward directions, all nucleotides are equally likely in the steady state. However, in the human genome the nucleotides C and G occur less often than A and T. This is partly due to methylation of successive CG pairs which makes them more susceptible to mutations. To mimic this asymmetry, consider an unrealistic model in which transitions from A to C and T to G occur with probability p+, while the reverse transitions (from C to A or G to T) occur at a lower probability of p−. (The other transitions occur at rate p, and transversions at rate q as before.) Write the modified transfer matrix corresponding to this model, and obtain the resulting frequencies of nucleotides in steady state.

*****

(Optional) 4. Correlations in the E. coli genome: In the models examined in the previous problem, point mutations at each position on the DNA occur at rates independent of other locations. Consequently, they predict pXY = pXpY, where pXY is the joint probability of finding nucleotides X and Y, at different locations. Test this hypothesis on the genome of E. coli (available on the course web-page) as follows:

(a) Calculate the frequencies of the four nucleotides in the genome.

(b) Write a program to count all 16 possible pairs of neighboring bases (e.g AT); hence obtain (1) the joint probabilities pXY, and construct the 4 × 4 matrix of correlations cXY = pXY/(pXpY).

(c) Repeat the above calculation for nucleotides that are further neighbors, and find the corresponding matrices c(XY<sup>n</sup> )<sup>(e.g. consider next nearest neighbor locationsjandj+ 2 to</sup> (2) calculate cXY). How do correlations decay as a function of the separation n?

*****

5. Activation/deactivation reaction: Many molecules in biology can be made active or inactive through the addition of a phosphate group. The enzyme that adds the phosphate group is usually termed a kinase, while a phosphatase removes this group. Let us consider a case where a finite number N of such molecules within a cell can be exchanged between the two forms at rates a and b, i.e.


where we have folded the probabilities to encounter the enzymes in the reaction rates. (a) Write down the Master equation that governs the evolution of the probabilities p(NA = n, NB = N − n, t).

(b) Assuming that initially all molecules are in state A, i.e. p(n, t = 0) = δn,N , find p(n, t) at all times. You may find it easier to guess the solution, but should then check that it satisfies the equations obtained before.

2

# *****

(Optional) 6. Human polymorphisms: Explore the data on gene polymorphism in human population from the Seattle SNP database, one of the largest collections of polymorphisms in humans. Each entry reports a polymorphism (e.g A/G) and its frequency x in individuals of European or African descent (ED and AD). Some information from this data is provided on the course web-page in the form of the file cSNPsAfricanEuropean.dat, which contains these frequencies (each line has information about one polymorphism ordered as AD-freq, ED-freq).

(a) 1. Make the histogram of x and compare it to the steady–state distribution f (x) obtained in the class. Make conclusions about the value of Nµ. Does the theoretical formula fit these distributions? (Hint: You may want to consider only alleles with x < 0.5 by replacing x > 0.5 with 1 − x).

(b) Compare f (x) for African and European populations. Do you see any difference? As­ suming µ = 10<sup>−8</sup> estimate the effective population size N for the two populations by fitting f (x) to the data. (Hint: use roughly 20-30 bins for 0 < x < 0.5, and ignore very rare polymorphisms). Although this method is not the best for estimation of the population size, it gives you an idea about the relative size of the population size in the two populations.

(c) Compare the frequencies of synonymous and non-synonymous mutations. Do they fit the theoretical f (x)? Which ones are more frequent and why? (The corresponding data are provided in the file cSNPsAfricanEuropeanType.dat.)

*****

3

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
