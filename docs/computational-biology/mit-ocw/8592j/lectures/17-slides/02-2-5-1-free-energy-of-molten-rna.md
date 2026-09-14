---
title: 2.5.1 Free energy of molten RNA
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.5.1 Free energy of molten RNA

**Source:** `lectures/17-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Using variants of Eq. (2.97), it is possible to follow how the secondary structure denatures as a function of temperature. Presumably at some temperature Tm the native structure disappears in favor of a molten state resembling a branched polymer. The nature of the melting process should depend strongly on the RNA sequence and its native structure. In the next section we shall explore this melting for the simple case of an RNA hairpin. In its molten phase, RNA can explore a variety of structures reflecting the competition between energy gain of pairing and the resulting loss of entropy. To estimate the fraction of bound pairs in the molten phase, we can neglect variations in binding energy, setting εij = ε and a corresponding Boltzmann weight of q ≡ e<sup>−βε</sup> ≥ 1. Once sequence variations are removed, the constrained partition function will depend only on segment length, i.e. Zi,j = Zm(|j − i| +1), and Eq. (2.97) simplifies to


It is possible to solve the above recursion (by changing to an ensemble of variable length N). However, a more informative solution is obtained by considering the “mountain” representation of planar graphs in Fig. 2.5. The correct weight for each graph is obtained by assigning a factor of 1 for each horizontal step, and<sup>√</sup> q to a vertical step (up or down). Each configuration can then be regarded as a Markovian random walk with these weights, and the additional requirement that it never goes below the starting point. The constraint (for an island/mountain landscape, or correct formulation of parentheses) is thus equivalent to a barrier to the random walk at a position one step below the starting point. The problem of a random walk with a so-called absorbing barrier can be solved in several ways– a quite elegant solution is presented by Chandrasekhar in Rev. Mod. Phys. 15, 1 (1943). Let us first ignore the constraint: The partition function for all paths of N steps starting at the origin is simply (1 + 2<sup>√</sup> q)<sup>N</sup> , accounting for all three possibilities in each step. Similarly, adding the uncorrelated fluctuations in each step, leads to a variance σ<sup>2</sup> = N(2<sup>√</sup> q)/(1 + 2<sup>√</sup> q). In the limit of large N, and appealing to the central limit theorem, the net weight of the subset of walks ending at a height h after N steps is obtained as


If we were to ask the question of what fraction of these random walks return to the origin (h = 0), we would obtain the expected result of Ω(N) ∝ g<sup>N</sup> /N<sup>c</sup> with the ‘loop closure’ exponent of c = 1/2 for our one-dimensional random walks. Of course for counting planar graphs, we need the smaller subset of walks that return to the origin without ever passing to h < 0, and need to subtract all undesired walks from our sum.

Chandrasekhar’s solution to this problem is closely related to the method of images in electrostatics. The image of the starting point (h = 0) with respect to the forbidden state

57

Image removed due to copyright restrictions. Please see: Chandrasekhar, S.  "Stochastic Problems in Physics and Astronomy." _Rev. Mod. Phys_ . 15, no.1(1943): 1-89.

(h = −1) is located at h = −2. Consider all walks that start at this image point and end at h = 0. Each such walk W<sup>∗</sup> must cross the ‘mirror’ plane at h = −1 at least once. We can construct a related ensemble of walks W<sup>′</sup> which are the reflection of these walks in the mirror-plane (thus starting at the original point h = 0) up to the point of first intersecting the forbidden state at h = −1, and after which following they follow the path of W<sup>∗</sup> . We note that the ensemble W<sup>′</sup> consists of precisely the paths starting and ending at h = 0 which violate the non-crossing condition. As these paths are in one to one correspondence to W<sup>∗</sup> , we simply need to subtract them from the sum in Eq. (2.99) to get the correct number of non-crossing paths. Since W<sup>∗</sup> is the ensemble of walks with an end to end excursion of h = 2, we obtain


The Gaussian approximation is only valid for large N, and we should similarly expand the difference in brackets above to get the final form


The most important consequence of the constraint is the change of the exponent c from 1/2 to 3/2. The fraction of bound pairs is merely determined by the probability of going up or

58

down at any step, and thus given by


which changes continuously from 1 at large q (low temperatures) to 2/3 as q → 1 at high temperatures.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2.5.2 Melting of a hairpin →](03-2-5-2-melting-of-a-hairpin.md)
