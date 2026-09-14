---
title: 2.3 Interacting Polymers
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.3 Interacting Polymers

**Source:** `lectures/10-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The polymeric properties discussed so far arose from the flexibility of the covalent bonds that join adjacent monomers. There are also interactions between any other pairs (triplets, etc.) of monomers which depend on their spatial vicinity and that favor certain spatial configurations. Indeed, it is such interactions, typically due to hydrogen bonds, that enable proteins to fold and assume specific shapes. There are competing effects due to thermal fluctuations and competition with solvent interactions.


Some of the ingredients of polymer interactions in a solvent is present in the very simple model of chain configurations on a (say square) lattice. The set of random walks on the square lattice that do not step back to the previous site grows with the number of steps N as 3<sup>N</sup> . One simple consequence of interactions is that it is physically impossible to visit a previously occupied site. The constraint of excluded volume prunes the random walks to a smaller subset of so-called self-avoiding walks. The number of self-avoiding walks also grows exponentially as g<sup>N</sup> with g < 3 (g ≈ 2.64).

A simple way to incorporate interactions on a lattice is to count the number of (nonpolymeric) nearest-neighbor pairs, and assign energy


where mm, ms, and ss stand for monomer-monomer, monomer-solvent, and solvent-solvent pairs respectively, with Npair and ǫpair indicating the corresponding number and bondenergies. As two initially separate monomers are brought into contact, two ms bonds are replaced by one mm bond and one ss bond, leading to a change in energy of δǫ = ǫmm + ǫss − 2ǫms. The preference of the monomers to aggregate in solvent is thus captured by the dimensionless “Flory–Huggins” parameter


A negative χ leads to separation of monomers, while a positive χ encourages their aggregation.

38


In a more realistic model, the interactions between molecules vary continuously as a function of their relative separation and orientation in space. The dependence on orientation is particularly relevant to hydrogen bonding, while the van der Waals attraction mainly depends on the separation. Just as in Eq. (2.8), an effective potential V(r) between monomers is in principle obtained by integrating over all positions (and orientations) of the solvent particles. In the usual case where the monomers are larger than the solvent molecules, the effective potential is attractive at large distances and has a hard repulsive core at short distances. For a good solvent the potential is weak, while a strong attractive potential favors aggregation of monomers in a bad solvent. The quality of solvent also changes as a function of temprature due to entropic contributions of its constituents. The larger entropy of solvent molecules typically improves the quality of a solvent at higher temperatures.

## 2.3.1 Mean-field estimate of the partition function

To calculate the properties of a polymer in solvent– e.g. to determine if it is in its native form or a denatured state at some temperature– we need to compute the free energy of the molecule and it environment. Computation of the partition function is a hard task, even for the highly simplified models we have introduced so far. We shall instead rely upon an approximate expression obtained in a mean-field/variational treatment. Let us assume that the most likely configurations of an interacting homopolymer have a typical size R. The partition of N monomers confined to a sphere of radius R is then estimated as


The first line in Eq. (2.44) pertains to the entropy of the polymer, the first term encodes the exponential growth in the number of configurations of an unconstrained polymer– the

39

precise value of g is in fact irrelevant to the considerations that follow. The second term approximates the reduction in the number of configurations when the polymer is constrained to a size R. The effect of this reduction is included as a Hookian spring, motivated by the result in Eq. (2.40) for the end-to-end probability of a non-interacting polymer.

The second line in Eq. (2.44) approximates the effect of interactions and is broken into two parts. The first part encodes the reduction in phase space due to excluded volume constraints: the first monomer is unconstrained, the volume available to the second is reduced by the fraction (a/R)<sup>3</sup> due to the volume excluded by the first, and so on. The reductions due to the excluded volume make a contribution to the free energy proportional to


The attractive part of the interaction, for homopolymers, is given by


Assuming a uniform mean-density, n(⃗r) = n = N/V = N/(4πR<sup>3</sup> /3), leads to


where we have integrated over the center of mass of the pair to get the volume V , and ignored any contributions from the surface. In the spirit of Flory-Huggins, we introduce a dimensionless parameter χ, via


to capture of the net effect of attractions, and such that


The resulting free energy, with R as a variational parameter,


will next be used to explore the phases of the interacting homopolymer.

40

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 2.2 Fluctuating Polymers](01-2-2-fluctuating-polymers.md) · [Up: contents](index.md)
