---
title: 1.1 Reaction Kinetics
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.1 Reaction Kinetics

**Source:** `lectures/19-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

> 1 The rate of change with time of the concentration of a protein–DNA complex is the sum of two terms. A positive contribution due to complex formation between a previously free specific site on a DNA molecule and a previously free protein, and a negative contribution due to complex break-up. At sufficiently low concentrations, the first term must be proportional to the probability of finding the a specific sites on the DNA molecule and a free protein molecule at the same site, and the second term must be proportional to the concentration of the complex:


Let us apply this equation to E. coli bacteria and lac repressors introduced in previous lectures. In vitro experiments on repressor–DNA solutions (containing the operator target sequence) report that on-rate is ka ∼ 10<sup>10</sup> M<sup>−1</sup> s<sup>−1</sup> under standard conditions.

Suppose that at times t < 0 there are no repressor–DNA complexes because the concentration of lactose is high and repressors are in inactive state. At time t = 0, the lactose concentration drops to zero. How long will it take the activated lac repressors to locate the specific operator sequence and switch-off gene expression? There are only a few operator sequences per E. coli. Assuming a volume of 1µm<sup>3</sup> , the (initial) concentration of unoccupied operator sequences [DNA] is of order 1/µm<sup>3</sup> or about 10<sup>−9</sup> M (concentrations are usually presented in molar units M = 6 × 10<sup>26</sup> m<sup>−3</sup> ). According to Eq. (1), for early times t, the concentration of occupied operator sequences will grow linearly in time as


where we have identified τ = 1/(ka[P |DNA]) as the characteristic time scale for a free repressor to locate the operator sequence. For the measured value of ka, this search time is of order τ ∼ 0.1s.

---

[Up: contents](index.md) · [1.2 Debye-Smoluchowski theory →](02-1-2-debye-smoluchowski-theory.md)
