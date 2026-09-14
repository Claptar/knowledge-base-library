---
title: 1.2 Debye-Smoluchowski theory
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.2 Debye-Smoluchowski theory

**Source:** `lectures/19-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this section we will compute the on–rate ka. The classical theory of the on–rate of diffusion–limited chemical reactions is due to Debye and Smoluchowski. Assume a spherical container (the cell) of radius R and place the specific target sequence at the center of the

> 1First two sections closely follow discussion in R. F. Bruinsma, Physica A 313, 211-237 (2002)

1

container. Let C(⃗r, t) be the concentration of free repressors. The concentration field obeys the diffusion equation


with D3 the diffusion constant of the protein in cytoplasm. We now want to know when the target sequence is occupied for the first time by a protein. Assume that this will happen when a diffusing protein enters for the first time a small sphere, of radius b ≪ R, at the origin. Protein must find the exact target sequence, thus b ≈ 0.34nm.

We will solve an easier problem by assuming that the small sphere at the origin acts as an absorber. Whenever a diffusing particle hits the small sphere, it disappears (free protein particle becomes bound protein-DNA complex). This approximation is valid, when specific sites on DNA are unoccupied. At the outer radius R we are constantly providing particles to keep concentration at a fixed value CR. This is an easier problem because under these conditions, a time-independent steady-state current I is established of protein molecules diffusing from the outer to the inner sphere. To obtain this current, we must solve Laplaces law:


with the boundary conditions C(R) = CR and C(b) = 0 (because diffusing particles disappear at r = b). Spherical symmetric solution is


where C0 = CR/(1 − b/R) ≈ CR for b ≪ R. The diffusion current density of proteins along the radial inward direction is⃗J = −D3∇C = −D3bC0/r<sup>2</sup> eˆr, so the diffusion current I equals:


Now compare this result with Eq. (2). The left-hand side of Eq. (2) is the number of complexes forming per second and must equal (minus) the incoming current I of free proteins. On the right-hand side we can identify C0 with the free proteins concentration [P ] far from the operator. This leads to


known as the Debye–Smoluchowski rate. If we use for the target radius base-pair distance b ≈ 0.34nm and in vitro measured diffusion rate for lac repressors in water D3 ≈ 3 × 10<sup>−11</sup> m<sup>2</sup> s<sup>−1</sup> we find that on-rate is of order ka ≈ 10<sup>8</sup> M<sup>−1</sup> s<sup>−1</sup> . We expect that actual on-rates are even smaller, because it takes certain time for protein to line up with the target and also diffusion constant D3 is smaller in cytoplasm. Recall that for lac repressor measured onrate ka ≈ 10<sup>10</sup> M<sup>−1</sup> s<sup>−1</sup> is two orders of magnitudes larger than the highest possible rate obtained by diffusion. This implies that proteins use some other mechanism to find specific site quickly.

2

---

[← 1.1 Reaction Kinetics](01-1-1-reaction-kinetics.md) · [Up: contents](index.md) · [1.3 Berg – von Hippel theory →](03-1-3-berg-von-hippel-theory.md)
