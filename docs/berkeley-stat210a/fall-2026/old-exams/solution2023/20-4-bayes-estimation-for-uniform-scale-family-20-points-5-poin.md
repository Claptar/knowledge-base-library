---
title: 4. Bayes estimation for Uniform Scale family (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Bayes estimation for Uniform Scale family (20 points, 5 points / part).

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- The Unif[0 _, θ_ ] distribution for _θ >_ 0 has density


Its mean and variance are _θ/_ 2 and _θ_<sup>2</sup> _/_ 12.

- The Pareto distribution with minimum value _x_ 0 _>_ 0 and shape parameter _α >_ 0 is called Pareto( _x_ 0 _, α_ ) and has density


Its mean is _ααx−_ <u>01</u><sup>if</sup><sup>_α>_1andisinfiniteotherwise,anditsvarianceis</sup> ( _α−_ 1) _θ_ <u>0</u><sup>22</sup><sup>_α_</sup> ( _α−_ 2)<sup>if</sup><sup>_α >_2 and infinite otherwise.</sup>

Assume that we observe a uniformly distributed random variable


Assume for parts (a) - (b) below that the relevant loss is the standard squared error loss _L_ ( _θ, θ_<sup>ˆ</sup> ) = ( _θ_<sup>ˆ</sup> _− θ_ )<sup>2</sup> .

- (a) Show that _θ ∼_ Pareto( _θ_ 0 _, α_ ) is conjugate to this family and find the posterior distribution and Bayes estimator for _θ_ .

---

[← Solution](19-solution.md) · [Up: contents](index.md) · [Solution →](21-solution.md)
