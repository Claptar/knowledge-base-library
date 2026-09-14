---
title: 2.2 Fluctuating Polymers
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.2 Fluctuating Polymers

**Source:** `lectures/10-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The basic molecules of life (DNA, RNA, proteins, · · · ) are hetero-polymers, formed by the covalent bonding of a sequence of elementary units (nucleic acids, amino-acids) in long chains. A homo-polymer, as in many synthetic organic molecules, is constructed by joining N ≫ 1 copies of the same monomer. A simple example is polyethylene,


The degree of polymerization, i.e. the the number of repeated units, can be quite large, ranging from a few hundred for proteins, 10<sup>4</sup> − 10<sup>5</sup> for polyethelene, to as big as 10<sup>9</sup> for some DNA. Typically the covalent bonds holding the polymer together are strong and cannot be broken at room temperature. There can, however, be flexibility in aligning/bending successive monomers, resulting in a large number of configurations degrees of freedom for polymers, indicating that a statistical description of the problem is fruitful. Such a statistical perspective is useful for describing general properties common to both synthetic and natural polymers. For example, at very high (not necessarily physiological) temperatures all polymers will be in a swollen (denatured) state to take maximum advantage of entropy. The heterogeneity of the sequence is irrelevant in such a phase, and we shall thus initially focus on the fluctuations of a homo-polymer.

## 2.2.1 Rotational isomers

Successive carbon–carbon bonds in the chain can be in different relative orientations, called rotational isomers. In polyethelene, the low energy trans conformation leads to a parallel alignment of bonds. There are two higher energy gauche states which form an angle of 2π/3 between successive bonds. Assuming an energy difference ∆between the trans, and the gauche states, at a temperature T , the probabilities of these outcomes satisfiy the Boltzmann weight


34

For (CH2)<sup>N</sup> , ∆is quite small (roughly 500 cal/mole or 1/3kBT ), and the polymer is very flexible at room temperature. For other polymers ∆ > kBT , and gauche states with probability


are relatively rare. A typical configuration then consists of long straight segments with few bends. The probability of a straight segment of n monomers is p<sup>n</sup> t<sup>(1−pt), where pt= 1−2p(g)</sup> is the probability of a trans bond. The average length of straight segments is thus ⟨n⟩a, where a is the bond length (monomer size), and


The typical size of these linear segments is proportional to the persistence of the polymer. The persistence length characterizes the decay of orientational correlations along the chain. In the above simplified model, let us denote the orientation of the bonds by the set of vectors {⃗t1,⃗t2, · · · ,⃗tN }, with⃗tj ·⃗tj = a<sup>2</sup> . Assuming that the (two) gauche states produce a relative bond angle φ, we have


where the last expression is valid in the limit of β∆ ≫ 1 where a gauche state is very unlikely. In the same approximation, the correlation between bonds that are further apart is given by


where we have included only configurations with one gauche bond. The orientation correlations decay exponentially as e<sup>−ℓ/ξp</sup> , where ℓ = na is the counter-length along the polymer, and the persistence length ξp is given by


## 2.2.2 Worm-like chain

For a rigid polymer such as double-stranded DNA a kink causing a finite rotational angle is energetically costly and does not occur. The loss of angular correlations at long distances then occurs from the accumulation of small changes from one monomer to the next. If we indicate as before a polymer configuration by the set of vectors {⃗t1,⃗t2, · · · ,⃗tN }, we can approximate the energy of a nearly straight configuration by


Since in a typical configuration⃗t changes slowly, it is useful to go over to a continuum limit in which the discrete monomer index i is replaced by the continuous arc-length s ∈ [0, L = Na]. Using �ti −⃗ti+1�2 = 2 − 2⃗ti ·⃗ti+1, we then can write


where κ = J/a is the coefficient of bending rigidity. (Note that |d⃗t/ds| = 1/R(s), where R(s) is the local radius of curvature.)

Ignoring the initial energy of the “ground state” configuration, it is common to write the energy in dimensionless form as


with βκ = ξp. We have anticipated that the bending rigidity is related to the persistence length. In fact, it can be shown (e.g. by using transfer matrices) that for the discrete model of Eq. (2.30)


and thus in the continuum limit


with ξp ≈ βκ for βJ ≫ 1. This, so called worm-like chain model is frequently invoked as a description of double-stranded DNA, where ξp is in the range of 50-100nm.

## 2.2.3 Entropic elasticity

The flexibility of long polymers arises from the statistical fluctuations of segments larger than the persistence length. The important parameter that governs the number of configurations is thus not the degree of polymerization N, but the number of unconstrained degrees of freedom, or the Kuhn length NK ≈ Na/(2ξp). To see this explicitly, let us consider the end to end separation of the polymer, given by


36

Because of rotational symmetry (there is no cost for rotating the entire polymer), ⟨⃗R⟩ = 0, and its variance is given by


We shall assume that the orientational correlations decay as a simple exponential (this is only asymptotically correct), i.e.


As the correlation function is the same for every pair of points separated by a distance k, and as there are (N − k) such pairs along the chain


The geometric series are easily performed, and for N ≫ 1 (where only the term proportional to N is significant), we obtain


The approximations in the second line rely on ξp ≫ a. The very last expression indicates that the behavior of the variance is the same as that of NK ≡ (Na/2ξp) independent rods of length 2ξp, i.e. the same variance is obtained for a collection of NK freely–jointed rods, each of length 2ξp. Indeed the correlations between these Kuhn segments is sufficiently small that in the limit of NK ≫ 1, we expect the Central Limit Theorem to hold, leading to the probability distribution function


The final probability distribution is identical to the Boltzmann weight of a Hookian spring of strength J connecting the end points of the polymer, and the result of entropic fluctuations can be interpreted as conferring an elastic bond between the ends of the polymer with spring coefficient


37

---

[Up: contents](index.md) · [2.3 Interacting Polymers →](02-2-3-interacting-polymers.md)
