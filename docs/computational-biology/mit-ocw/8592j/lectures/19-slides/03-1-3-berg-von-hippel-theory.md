---
title: 1.3 Berg – von Hippel theory
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.3 Berg – von Hippel theory

**Source:** `lectures/19-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In 1980s Berg and von Hippel proposed that proteins use combination of 1D (sliding) and 3D (jumps) diffusion to quickly find the target site on the DNA (Figure 1). Proteins are able


<!-- Start of picture text -->
TF<br><!-- End of picture text -->

Figure 1: Schematics of 1D/3D search for target site on the DNA. Dashed lines represent 3D diffusion trajectories and thick lines are 1D sliding footprints.

to bind to any site on the DNA and then diffuse along the DNA (sliding). Once proteins detach from the DNA, they diffuse around until they attach to another site on the DNA (jump). Proteins keep sliding and jumping until they find the specific target site, where they get stuck because binding to the specific target site Es ∼ 20 − 25kBT is a lot stronger than binding to a non-specific site Ens ∼ 5 − 10kBT .

During jumps it is reasonable to assume that protein can attach to any site on the DNA with equal probability, because DNA is in very compact form and even if two DNA segments are close in real space, they could be very far apart in the DNA sequence. Sliding events are thus independent and they start at uniformly distributed random positions along the DNA sequence. Probability that protein finds the target location in one sliding event is q = n/M, where n is number of visited sited during each sliding event and M is total number of sites on the DNA.

First we consider unrealistic case where every sliding event takes a fixed amount of time τ1 and fixed number of sites n are visited by protein. The probability that single protein will find the target in exactly NR rounds of sliding and jumping is p(NR) = q(1 − q)<sup>NR−1</sup> , where the 1 − q factor reflects the probability that protein didn’t find the target in first NR − 1 rounds and factor q reflects the probability that protein has found the target in the last round. The average number of rounds needed for protein to find the target is:


3

The average search time for protein to find the target site is:


where τ3 is average time of 3D jump.

In reality sliding events don’t take fixed amount of time. Protein detach from the DNA with rate kd<sup>(ns)</sup> = 1/τ1 and time of each sliding event is taken from exponential distribution ρ(τ1) = exp(−τ1/τ1)/τ1. During sliding event every visited site is important, because protein is immediately trapped in specific site. Therefore we need to take the average distance between the leftmost and rightmost site to estimate the number of visited sites n(τ1) = �16D1τ1/πb<sup>2</sup> , where b is basepair distance, and not just the distance between the start and end site of the sliding, which would give �2D1τ1/b<sup>2</sup> . The average number of rounds needed for protein to find the target in this case is:


where τ1,i is time protein spent during ith sliding event and bracket denotes averaging over all possible sliding times τ1,i. Sliding events are independent and this equation can be simplified:


where we used ⟨n⟩ = �0∞<sup>n(τ1)ρ(τ1)dτ1=2</sup> �D1τ1/b<sup>2</sup> . Calculating average search time is a bit more complicated:


It is interesting to evaluate the optimal sliding time τ1<sup>(opt)</sup> that minimizes the average search time.


For τ1 > τ1<sup>(opt)</sup> , protein spends too much time sliding. In the other case τ1 < τ1<sup>(opt)</sup> is jumping a lot and spends too much time with 3D diffusion. Protein dissociation rate from the DNA

4

kd<sup>(ns)</sup> = 1/τ1 strongly depends on the binding strength Ens (homework), which depends on the salt concentration in the cytoplasm. Increasing the salt concentration reduces the nonspecific binding energy Ens since this interaction is predominantly electrostatic. One would expect that at standard physiological conditions τ1 is close to the optimal value τ3, but it turns out that protein spends more time sliding than jumping τ1 > τ3. Typical measured sliding time for lac repressor is τ1 ∼ 10<sup>−3</sup> s, while we can estimate the typical jumping time τ3 ∼ V/D3L ∼ 10<sup>−4</sup> s, where V ∼ 1µm<sup>3</sup> is volume of the E. coli, L = Mb ∼ 1mm is DNA length and D3 ≈ 3 × 10<sup>−11</sup> m<sup>2</sup> s<sup>−1</sup> measured diffusion constant in the cytoplasm. Using these results and measured diffusion constant D1 ≈ 5 × 10<sup>−14</sup> m<sup>2</sup> s<sup>−1</sup> we can estimate the average search time:


When np proteins are searching for target site simultaneously it is important to know the search time of the fastest of the np proteins, because once the first protein binds the target site, gene expression is shut down. Search time for a single protein to find the target site is exponentially distributed: ρ1(ts) = exp(−ts/⟨ts⟩)/⟨ts⟩. Distribution of search times for the fastest of the np proteins is obtained by standard extreme value distribution.


The mean search time of the fastest of the np proteins to find the target location goes as ⟨ts⟩/np. There could be of the order of np ∼ 100 copies of proteins searching for target at the same time, which greatly speeds up the search time of proteins for the target site.

5

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 1.2 Debye-Smoluchowski theory](02-1-2-debye-smoluchowski-theory.md) · [Up: contents](index.md)
