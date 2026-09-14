---
title: 3 On Parameter Estimation in MA( q )
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 On Parameter Estimation in MA( q )

**Source:** [`LectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Even though MA( _q_ ) models are, in some ways, simpler than AR( _p_ ) models, parameter estimation is much more complicated compared to AR( _p_ ). We will not study this topic (and simply rely on the `ARIMA` function for fitting these models to data). But here, I will just illustrate the difficulties involved in the simplest case _q_ = 1 i.e., the MA(1) model.

For estimation, the main step is to write down the likelihood. The joint density of _y_ 1 _, . . . , yn_ is multivariate normal with mean vector _m_ := ( _µ, . . . , µ_ )<sup>_T_</sup> and covariance matrix Σ where Σ equals the _n × n_ matrix whose ( _i, j_ )<sup>_th_</sup> entry is given by


The likelihood is therefore


3

where _y_ is the _n ×_ 1 vector with components _y_ 1 _, . . . , yn_ . This is a function of the unknown parameters _µ, θ, σ_ which can be estimated by maximizing the logarithm of the likelihood. The presence of Σ<sup>_−_1</sup> makes this computationally expensive. Some (exact or approximate) formula should be used for Σ<sup>_−_1</sup> so that one does not need to invert an _n × n_ matrix every time the log-likelihood is to be computed.

---

[← 2 Sample ACF](02-2-sample-acf.md) · [Up: contents](index.md) · [4 AR( p ) models →](04-4-ar-p-models.md)
