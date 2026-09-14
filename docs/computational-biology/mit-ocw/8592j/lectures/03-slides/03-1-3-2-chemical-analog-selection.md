---
title: 1.3.2 Chemical analog & Selection
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.3.2 Chemical analog & Selection

**Source:** `lectures/03-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Through the reactions in Eq. (1.25), we introduced a chemical reaction that mimicks a mutating population. Consider a system where a reaction between molecules A and B can lead to two outcomes:<sup>2</sup>


at rates c and d. In a “mean-field” approximation the number of A molecules changes as


Equation (1.47) predicts steady states NA<sup>∗= 0forc < d,N</sup> A<sup>∗= Nforc > d,whileanycom-</sup> position is permitted for the symmetric case of c = d. As we shall demonstrate, fluctuations modify the latter conclusion.

As before, let us denote NA = n, NB = N − NA, and follow the change in composition after a single reaction. The number of A particles may change by ±1 with rates


where the product is over the number of possible pairs of A-B particles that can participate in the reaction. The diagonal terms are again obtained from the normalization condition in Eq. (1.14) resulting in the Master equation

dp(n, t)

= d(n+1)(N−n−1)p(n+1)+c(n−1)(N−n+1)p(n−1)−dn(N−n)p(n)−cn(N−n)p(n) , dt


for 0 < n < N, and with boundary terms


When the number N is large, it is reasonable to take the continuum limit and construct a Kolmogorov equation for the fraction x = n/N ∈ [0, 1]. The rates in Eq. (1.48) change n by ±1, and hence


while


> 2In a sense these reactions mimic the mating process in which the offspring of a heterozygote (a diploid organism with different alleles A1 and A2) and a homozygote (say with two copies of allele A1) may be either heterozygote (A1A2) or homozygote (A1A1).

12

Comparison with Eqs.(1.43) and Eq. (1.45) indicates that the above reaction has the same behavior as binomial selection provided that c = d = 1/(4N). Indeed the superficial difference in factor of N between the two cases is because in the latter we followed the reactions one at a time (at rate c = d), while in the former we computed the transition probabilities after a whole generation (N steps of reproduction and removal). The selection process characterized by Eq.(1.40) treats the two alleles as completely equivalent. In reality one allele may provide some advantage to individuals carrying it. If so, there should be a selection process by which individuals with this allele are more likely to reproduce, on average increasing their population in the next generation. This would then cause a drift in the appropriate Kolmogorov equation. The population genetics perspective on selection will be covered in detail by Professor Mirny. It turns out that this prescription is mathematically equivalent to the binary reaction of Eq. (1.46) with c̸ = d. In future lectures, selection is quantified by a parameter s, which is related to c and d by


In the following, we shall employ the nomenclature of population genetics, such that

---

[← 1.3.1 Binomial selection](02-1-3-1-binomial-selection.md) · [Up: contents](index.md) · [1.3.3 Steady states →](04-1-3-3-steady-states.md)
