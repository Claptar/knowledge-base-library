---
title: 16 slides
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 16 slides

**Source:** `lectures/16-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 2.4 DNA structure

DNA molecules come in a wide range of length scales, from roughly 50,000 monomers in a λ-phage, 6 × 10<sup>9</sup> for human, to 9 × 10<sup>10</sup> nucleotides in the lily. The latter would be around thirty meters long if fully stretched. If we consider DNA as a random (non-self avoiding) chain of persistence length ξp ≈ 50 nm, its typical size would be Rg ≈ �L · Rp, coming to approximately 0.2 mm in human. Excluded volume effects would further increase the extent of the polymer. This is much larger than the size of a typical cell, and thus DNA within cells has to be highly compactified. Eukaryotes organize DNA by wrapping the chain around histone proteins (nucleosomes), which are then packed together.

At the microscopic level the double helix is held together through Watson–Crick pairs, G–C and A–T, the former (with a binding energy of around 4kBT ) being roughly twice as strong as the latter. At finite temperatures, this energy gain competes with the loss of entropy that comes with braiding the two strands. Indeed at temperatures of around 80<sup>◦</sup> C the double strand starts to unravel, denaturing (melting) into bubbles where the two strands are apart. Regions of DNA that are rich in A–T open up at lower temperatures, those with high G–C content at higher temperatures. These events are observed as separate blips in ultraviolet absorption as a function of temperature for short DNA molecules, but overlap and appear as a continuous curve in very long DNA.

There are software packages that predict the way in which a specific DNA sequence unravels as a function of temperature. The underlying approach is the calculation of free energies for a given sequence based on some model of the binding energies, e.g. by adding energy gains from stacking successive Watson-Crick pairs. Another component is the gain in entropy upon forming a bubble, which is observed experimentally to depend on the length l of the denatured fragment as


The logarithmic dependence is a consequence of loop closure, and can be justified as follows. The two single-stranded segments forming a bubble can be regarded as a loop of length 2l. Let us consider an open polymer of length 2l, and the probability that the two end-points are separated by a distance⃗r. For non-interacting random walks the number of configurations of length 2l and end-to-end separation⃗r is easily obtained by appropriate extension of Eq. (2.40) to


where we have further generalized to the case of random walks in d space dimensions. The number of configurations of a bubble is now obtained by integrating over all positions of the intermediate point as


with g = g1<sup>2andc = d/2.</sup>

48

For the more realistic case of self-avoiding polymers, scaling considerations suggest


We can understand this dependence by noting that in the absence of the loop closure constraint the end-point is likely to be anywhere in a volume of size roughly R<sup>d</sup> ∝ l<sup>dν</sup> , and that brining the ends together reduces the number of choices by this volume factor. As we shall see shortly, the parameter g is important in determining the value of the denaturation temperature, while c controls the nature (sharpness) of the transition.

## 2.4.1 The Poland–Scheraga model for DNA Denaturation

Strictly speaking, the denaturation of DNA can be regarded as a phase transition only in the limit where the number of monomers N is infinite. In practice, the crossover in behavior occurs over an interval that becomes narrower with large N, so that it is sharp enough to be indistinguishable from a real singularity, say for N ∼ 10<sup>6</sup> . We shall describe here a simplified model for DNA denaturation due to Poland and Scheraga<sup>1</sup> . Configurations of partially melted DNA are represented in this model as as alternating sequence of doublestranded segments (rods), and single-stranded loops (bubbles).


Ignoring any interactions between the segments, each configuration is assigned a probability


where we have assumed that the first segment is a rod of length l1, the second a bubble formed from two single strands of length l2, and so on. The double stranded segments are energetically favored, but carry little entropy. To make analytical computations feasible, we shall ignore the variations in binding energy for different nucleotides, and assign an average energy ǫ < 0 per double-stranded bond. (In this sense, this is a model for denaturation of a DNA homo-polymer.) The weight of a rod segment of length l is thus


> 1D. Poland and H. A. Scheraga, “Phase transitions in one dimension and the helix-coil transition in polyamino acids,” J. Chem. Phys. 45, 1456 (1966).

49

The single-stranded portions are more flexible, and provide an entropic advantage that is modeled according to a weight similar to Eqs. (2.73-2.74), as


Clearly the above weight cannot be valid for strands shorter than a persistence length, but better describes longer bubbles.

For DNA of length L the segment lengths are constrained such that


and the partition function, normalizing the weights in Eq. (2.75), is given by


where the prime indicates the constraint in Eq. (2.78). As usual in statistical physics, such a global constraint can be removed by moving to a different ensemble in which the number of monomers is not fixed, but a DNA of length L is assigned an additional weight of z<sup>L</sup> . (The quantity z is like a “fugacity,” related to a chemical potential µ by z = e<sup>βµ</sup> .) In such an ensemble, the appropriate partition function is


Since L can now take any value, we can sum over the {li} independently without any constraint, to obtain


The result is thus a product of alternating contributions from rods and bubbles. For each rod segment, we get a contribution


while the contribution from a bubble is


The result for bubbles has been expressed in terms of the functions fn<sup>+(x),frequentlyen-</sup> countered in describing the ideal Bose gas in the grand canonical ensemble. We recall some

50

properties of these functions. First, note that taking the logarithmic derivative lowers the index by one, as


Second, each fn<sup>+(x)isanincreasingfunctionofitsargument,andconvergentuptox=1,</sup> at which point

where ζn is the well-known Riemann zeta-function. The zeta-function is well behaved for c > 1, and indeed for c < 1, fc<sup>+(x)divergesis(1 −x)c−1forx →1.2</sup>

Next, we must sum over all possible numbers of bubbles in between two rod segments as end points, leading to


This is a just geometric series, easily summed to


The logarithm of the sum provides a useful thermodynamic free energy,


from which we can extract physical observables. For example, while the length L is a random variable in this ensemble, for a given z, its distribution is narrowly peaked around the expectation value


We can also compute the fraction of the polymer that is in the denatured state. Since each double-strand bond contributes a factor w to the weight, the number of bound pairs NB has a mean value


Taking the ratio of NB and L gives the fraction of the polymer in the native state as


> 2Furthering the mathematical analogy between DNA melting and Bose-Einstein condensation, note that when the bubble is treated as a random walk, c = d/2, implying that B(z) is only finite for d ≤ 2. Indeed, d = 2 is also a critical dimension for Bose-Einstein condensation.

51

Equation (2.91) is not particularly illuminating in its current form, because it gives Θ in terms of z, which we introduced as a mathematical device for removing the constraint of length in the partition function. For meaningful physical results we need to solve for z as a function of L by inverting Eq. (2.90). This task is simplified in the thermodynamic limit where L, NB →∞, while their ratio is finite. From Eqs. (2.90-2.91), we see that this limit is obtained by setting the denominator in these expressions equal to zero, i.e. from the condition


The type of phase behavior resulting from Eqs. (2.92-2.91), and the very existence of a transition, depend crucially on the parameter c, and we can distinguish between the following three cases:

(a) For c < 1, the function fc<sup>+(zg)goestoinfinityatz=1/g.Therighthandsideof</sup> Eq. (2.92) is a decreasing function of z that goes to zero at z = 1/w. We can graphically solve this equation by looking for the intersection of the curves representing these functions. As temperature goes up, 1/w = e<sup>βǫ</sup> increases towards unity, and the intersection point moves to the right. However, there is no singularity and a finite solution z < 1/g exists at all temperatures. This solution can then be substituted into Eq. (2.91) resulting in a native fraction that decreases with temperature, but never goes to zero. There is thus no denaturation transition in this case.


(b) For 1 ≤ c ≤ 2, the function fc<sup>+(zg) reachesa finite value of ζcat zg= 1.The two curves</sup> intersect at this point for zc = 1/g and wc = g/(1 + ζc). For all values of w ≤ wc, z remains fixed at 1/g. The derivative of fc<sup>+(zg),proportional tof</sup> c<sup>+</sup> −1<sup>(zg)from Eq.(2.84), divergesas</sup> its argument approaches unity, such that


From the occurrence of fc<sup>+</sup> −1<sup>(zg)inthedenominatorofEq.(2.91), weobservethatΘiszero</sup> for w ≤ wc, i.e. the polymer is fully denatured. On approaching the transition point from

52

the other side, Θ goes to zero continuously. Indeed, Eq. (2.93) implies that a small change 1 δw ≡ w−wc is accompanied by a much smaller change in z, such that δz ≡ (zc−z) ∝ (δw) c−1 . Since fc<sup>+</sup> −1<sup>(zg)∝(1 −zg)c−2,weconcludefromEq.(2.91)thatthenativefractiongoesto</sup> zero as


For a loop treated as a random walk in three dimensions, c = 3/2 and β = 1, i.e. the


denatured fraction disappears linearly. Including self-avoidance with c = 3ν ≈ 1.8 leads to β ≈ 1/4 and a much sharper transition. (c) For c > 2, the function fc<sup>+</sup> −1<sup>(zg)approachesafinitelimitofζc−1atthetransitionpoint.</sup> The transition is now discontinuous, with Θ jumping to zero from Θc = (1+ζc)/(1+ζc+ζc−1). Including the effects of self-avoidance within a single loop increases the value of c from 1.5 to


1.8. In reality there are additional effects of excluded volume between the different segments. It has been argued that including the interactions between the different segments (single and

53

double-strands) further increases the value of c to larger than 2, favoring a discontinuous melting transition.<sup>3</sup>

A justification of the role of the exponent c in controlling the nature/existence of the phase transition can be gleaned by examining the behavior of a single bubble. Examining the competition between entropy and energy suggests that the probability (weight) of a loop of length ℓ = 2l is proportional to


The probability broadens to include larger values of ℓ as (g/w) → 1.

(a) For c < 1, the above probability cannot be normalized if arbitrarily large values of ℓ are included. Thus at any ration of (g/w), the probability has to be cut-off at some maximum ℓ, and the typical size of a loop remains finite.

(b) For 1 ≤ c ≤ 2 the probability can indeed be normalized including all values of ℓ (the normalization is fc<sup>+(g/w)),buttheaveragesizeoftheloop(relatedtof</sup> c<sup>+</sup> −1<sup>(g/w))diverges</sup> as (g/w) → 1 signaling a continuous phase transition.

(c) For c > 2, the probability is normalizable, and the loop size remains finite as (g/w) → 1. There is a limiting loop size at the transition point suggesting a discontinuity.

> 3Y. Kafri, D. Mukamel, and L. Peliti, Phys. Rev. Lett. 85, 4988 (2000).

54

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[Up: contents](../index.md)
