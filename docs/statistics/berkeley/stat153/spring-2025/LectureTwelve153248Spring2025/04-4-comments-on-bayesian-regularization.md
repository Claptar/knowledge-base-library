---
title: 4 Comments on Bayesian Regularization
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwelve153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwelve153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Comments on Bayesian Regularization

**Source:** [`LectureTwelve153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwelve153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In practice, the posterior _fτ,σ|_ data( _τ, σ_ ) tends to prefer _τ_ values which are neither too small nor too large. Because


5

and the prior _fτ,σ_ ( _τ, σ_ ) is quite flat, the likelihood _f_ data _|τ,σ_ ( _τ, σ_ ) must prefer values of _τ_ which are neither too small nor too large. Note that there is a big difference between the two likelihoods:


Maximizing _f_ data _|β,σ_ (data) leads to the unregularized least squares estimate which leads to overfitting. On the other hand, maximizing _f_ data _|τ,σ_ (data) often leads to a fairly small estimate of _τ_ ˆ leading to a smooth trend function. The reason for this discrepancy can be understood by noting that


When _τ_ is large, the term _fβ|τ_ ( _β_ ) will be small simply because the normal density with variance _τ_<sup>2</sup> will be flat for large _τ_ . On the other hand, when _τ_ is too small, the weight _fβ|τ_ ( _β_ ) will be significant only for very smooth _β_ s but these _β_ s will have poor values for _f_ data _|β,σ_ (data).

6

---

[← 3 Bayesian approach for dealing with unknown τ and σ](03-3-bayesian-approach-for-dealing-with-unknown-τ-and-σ.md) · [Up: contents](index.md)
