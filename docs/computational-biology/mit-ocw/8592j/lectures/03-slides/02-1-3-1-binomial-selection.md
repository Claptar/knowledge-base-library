---
title: 1.3.1 Binomial selection
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.3.1 Binomial selection

**Source:** `lectures/03-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider a population with two forms of an allele, say A1 and A2 corresponding to blue or brown eye colors. The probability for a spontaneous mutation to occur that changes the allele for eye color is extremely small, and effectively µ1 = µ2 = 0 in Eq. (1.23). Yet the proportions of the two alleles in the population does change from generation to generation. One reason is that some individuals do not reproduce and leave no descendants, while others reproduce many times and have multiple descendants. This is itself a stochastic process and the major source of rapid changes in allele proportions. In principle this effect also leads to variations in population size. In practice, and to simplify computations, it is typically assumed that the size of the population is fixed.

10

In the model of binomial selection, the process or reproduction from one generation to the next is assumed to be as follows: Let us assume that in a population of N alleles, N1 = n are A1, and N − n are A2. The population at the next generation may have m individuals with allele A1, and the probability for such a transition is


This probability is like reaching into a bag with n balls of blue color and N −m balls of brown color, recording the color of the ball and throwing it back. After repeating the process N times, the probability that the blue color is recorded m times is given by the above binomial distribution. (The probability of getting a blue ball in each trial is simply n/N, and 1 − n/N for brown.) Clearly some balls can be picked up multiple times (multiple descendants), while some balls are never picked (no offspring).

Regarding Rmn as the probability to obtain random variable m, given initial n, it is easy to deduce from standard properties of the binomial distribution that


while


We can construct a continuum evolution equation by setting x = n/N ∈ [0, 1], and replacing p(n, t + 1) − p(n, t) ≈ dp(x)/dt, where t is measured in number of generations. Clearly, from Eq. (1.41), there is no drift


while the diffusion coefficient is given by


A light variant of binomial selection is also applicable to mating of diploid organism. For two alleles, there are three genotypes of A1A1, A1A2, and A2A2 in proportions of x11, x12, and x22 respectively. To mimic a mating event, pick one allele of one individual, another allele from a second individual. Set aside the resulting offspring and return the parents to the initial pool. Repeat the process N times to construct the new generation. For each offspring the probability of selecting allele A1 is x11 + x12/2, while allele A2 is selected with probability x22 + x12/2. If the initial population is in Hardy–Weinberg equilibrium, the relative genotype frequencies are related to the proportions of the two alleles simply by x11 = x<sup>2</sup> , x12 = 2x1x2, and x22 = x<sup>2</sup> 2<sup>.Thematingprocessisthusagainequivalenttotheprocessweconsidered</sup> earlier for haploids, with A1 and A2 chosen with probabilities of x and 1 − x respectively. Since, in a diploid population of N individuals, the number of alleles is 2N, the previous result is simply modified to


11

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [1.3.2 Chemical analog & Selection →](03-1-3-2-chemical-analog-selection.md)
