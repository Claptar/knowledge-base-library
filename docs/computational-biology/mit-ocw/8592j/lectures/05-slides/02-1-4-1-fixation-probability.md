---
title: 1.4.1 Fixation probability
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.4.1 Fixation probability

**Source:** `lectures/05-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us denote by Π<sup>∗</sup> (xa, y), the probability that starting a starting composition y is at long time fixed to absorbing state xa, i.e. Π(xa, y) = limt→∞ p(xa, t|y). For our problem, we have two such states with Π0(y) ≡ Π<sup>∗</sup> (0, y) and Π1(y) ≡ Π<sup>∗</sup> (1, y), but keep the more general notation for the time being. These functions must correspond to steady state solutions to Eq. (1.67), and thus obey


After rearranging the above equation to


we can integrate it to


The result of the above integration is related to an intermediate step in calculation of the steady state solution p<sup>∗</sup> of the forward Kolmogorov equation in (1.59). However, as we noted already, in the context of absorbing states the function p<sup>∗</sup> is not normalizable and thus cannot be regarded as a probability. Nonetheless, we can express the results in terms of this function. For example, the probability of fixation, i.e. Π1(y) is obtained with the boundary conditions Π1(0) = 0 and Π1(1) = 1, as


When there is selection, but no mutation, Eq. (1.54) implies


16


Figure 1: Fixation probability

Integrating Π<sup>∗</sup> (y)<sup>′</sup> and adjusting the constants of proportionality by the boundary conditions Π1(0) = 0 and Π1(1) = 1, then leads to the fixation probability of


The fixation probability of a neutral allele is obtained from the above expression in the limit of s → 0 as Π1(y) = y.

When a mutation first appears in a diploid population, it is present in one copy and hence y = 1/(2N). The probability that this mutation is fixed is Π1 = 1/(2N) as long as it is approximately neutral (if 2sN ≪ 1). If it is advantageous (2sN ≫ 1) it will be fixed with probability Π1 = 1 − e<sup>−s</sup> irrespective of the population size! If it is deleterious (2sN ≪−1) it will have a very hard time getting fixed, with a probability that decays with population size as Π1 = e<sup>−(2N−1)|s|</sup> . The probability of loss of the mutation is simply Π0 = 1 − Π1.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [1.4.2 Mean times to fixation/loss →](03-1-4-2-mean-times-to-fixation-loss.md)
