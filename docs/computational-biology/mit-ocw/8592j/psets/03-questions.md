---
title: 03 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 03 questions

**Source:** `psets/03-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 3

Extreme Values

1. Optimized Gaussians: Let x = max{r1, r2, · · · , rN } be the largest of N independent, identically distributed Gaussian variables. Specifically, each r is distributed according to


(a) Find the cumulative probability, PN (x) that the maximum is less than or equal to x. (b) Show that in the limit of N ≫ 1, x<sup>∗</sup> , the most likely value of x, can be obtained from either expression


and behaves as x<sup>∗</sup> ≃ √2σ<sup>2</sup> ln N.

(c) By expanding the solution to part (a) around x<sup>∗</sup> , and expressing the first order expansion as an exponential (i.e. replacing 1 + δ with e<sup>δ</sup> ), show that the probability distribution for x approaches a Gumbel form, and identify the corresponding parameters.

*****

2. Homodimers versus heterodimers: In Phys. Rev. Lett. 97, 178101 (2006), Lukatsky, Zeldovich and Shakhnovich note that proteins are more likely to pair and interact as homodimers (two identical components) than heterodimers (with two distinct parts). They offer a statistical justification for this preference which is partly based on the charecteristics of extreme values. The simplified and analytically tractable model presented in this problem captures this aspect of the explanation.

We shall assume that the protein binding interfaces are circular rings of exactly N aminoacids. For a given ring, the amino-acids are selected randomly. A heterodimer is constructed by placing two such rings (a and b) in contact, and the resulting binding energy is


Note that the two rings can be bound after relative shifts by s = 1, 2, · · · , N, and the molecules rotate to achieve the location of minimal energy.

There are two ways to obtain a homodimer: The two sequences can be shifted and matched (not shown in the figure), in which case


1


<!-- Start of picture text -->
b N-1<br>Heterodimer interface: b N b 1 b 2<br>a N<br>a 1 a a<br>2 3<br>a 4<br>a 3<br>Homodimer interface: a 2 a 1<br>a N<br>a 1<br>a 2 a 3<br><!-- End of picture text -->

However, since the rings are at the interface of a larger protein, such matching is generally not possible. The correct arrangement (as in the figure) is to rotate one of the two rings, and then join them, such that


Throughout this problem assume that due to the addition of many pairwise interactions (N ≫ 1), the energies Es are Gaussian random variables, and that


(a) For the heteropolymers, find the mean �E<sup>a,b�</sup> for N ≫ 1, and comment on the form of the probability distribution for E<sup>a,b</sup> .

(b) For the un-rotated homodimers, find the probability distribution for E<sup>a,a</sup> , and its mean value. (Hint: Note the number of distinct realization of s.)

(c) For the rotated homodimers, find the probability distribution for E<sup>a,aR</sup> , and its mean value. (Hint: Note the number of distinct interaction terms.)

(d) For randomly selected choices, which ensemble is likely to lead to (i) best binding; (ii) worst binding? If sequences are specifically designed to achieve optimal binding, is there any advantage to homodimers?

2

# *****

3. Thymic selection of T-cell receptors: T cells are part of the adaptive immune system; their job is to examine short peptides cut from larger proteins and presented on the surface of cells in blood stream. The strength of binding between a receptor complex on the T- cell, and the peptide presented on another (major histocompatibility) complex, is used to determine whether the peptide comes from a self-protein or is part of a foreign pathogen protein. Pathogens are recognized when the variable T cell receptors (TCRs) bind strongly to foreign peptides; TCRs bind weakly to self-peptides and are thus self-tolerant. To ensure self-tolerance (thereby avoiding auto-immune response), the subset of T cells released to the blood stream is culled from a much larger candidate set in the thymus. In this problem, a simplified model of thymic selection of TCRs is mapped to an extreme value problem.


<!-- Start of picture text -->
T cell<br>TCR<br>APELFNTPDI<br>peptide VDVCLPFERG<br>MHC<br><!-- End of picture text -->

We shall assume that the relevant binding energy for discriminating between self and foreign peptides is due to an interface of N amino-acids from the peptide, and the TCR. The starting model thus resembles the previous problem, with


where t ≡ (t1, t2, · · · , tN ) and p ≡ (p1, p2, · · · , pN ) indicate the sequences of amino-acids on the TCR and the peptide respectively. A given thymocyte (immature T cell) has some TCR sequence t; it moves around the thymus encountering cells presenting peptides from self-proteins. We shall assume that each thymocyte encounters M such peptides {p<sup>(α)</sup> } for α = 1, 2, · · · , M. It is released into the blood stream only if two conditions are met: ⋆ It must not bind any self-peptide too strongly. This condition, known as negative selection will be modeled by the requirement E(t, p<sup>(α)</sup> ) > En for all α (negative energies correspond to stronger binding). ⋆ It must bind at least one self-peptide moderately. This positive selection will be indicated by requiring Ep > E(t, p<sup>(β)</sup> ) > En for some β.

(a) Show that the above selection criteria are equivalent to En < Emin(t) < Ep, where Emin(t) ≡ min{E(t, p<sup>(α)</sup> )} is the strongest binding energy.

3

(b) For a given TCR amino-acid ti, let us set


For large N, what is the probability distribution for E(t, p) (for a given t encountering a random peptide).

(c) What is the probability distribution for Emin(t)?

- (d) Show that for ln M ∝ N, the distribution for Emin(t) is very narrow, centered around a value proportional to N, while its width does not grow with N. *****

4. Gapless alignment: Consider a scheme for aligning DNA sequences in which a score s = 1 is assigned to a match, while s = 0 for a transversion (A↔G or T↔C) and s = −µ for a transition (e.g. A↔C). (Assume all four nucleotides occur with equal frequency.)

(a) Find the parameter λ(µ) that appears in the Gumbel distribution for the statistics of such random gapless alignments.

(b) Show that alignments are possible only for µ > µc, and plot λ as a function of µ.

*****

4

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
