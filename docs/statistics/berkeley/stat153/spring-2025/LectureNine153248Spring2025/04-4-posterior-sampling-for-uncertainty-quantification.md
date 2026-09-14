---
title: 4 Posterior Sampling for Uncertainty Quantification
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Posterior Sampling for Uncertainty Quantification

**Source:** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A useful way of visualizing the uncertainty is to draw posterior samples from the unknown parameters, and then plot the corresponding fitted values along with the observed data. The algorithm for drawing the posterior samples is as follows.

1. Obtain samples _c_<sup>(1)</sup> _, . . . , c_<sup>(</sup><sup>_N_)</sup> by sampling, with replacement, from the set of possible values of _c_ : _{_ 2 _, . . . , n}_ with probability weights given by the posterior pmf _π_ ( _c |_ data). For this, one can use, for example, the choice function in `np.random.default` ~~`r`~~ `ng()` .

2. For each _j_ = 1 _, . . . , N_ ,

   - a) Fix _c_ = _c_<sup>(</sup><sup>_j_)</sup> .

   - b) Calculate _RSS_ ( _c_ ) and _β_<sup>ˆ</sup> _c_ by implementing linear regression with fixed _c_ .

   - c) Generate a chi-squared random variable _χ_<sup>2</sup> with _n −_ 3 degrees of freedom. Take _σ_<sup>(</sup><sup>_j_)</sup> = ~~�~~ _RSS_ ( _c_ ) _/χ_<sup>2</sup> .

   - d) Take _β_<sup>(</sup><sup>_j_)</sup> to be a generated random vector from the multivariate normal distribution with mean _β_<sup>ˆ</sup> _c_ and covariance ( _σ_<sup>(</sup><sup>_j_)</sup> )<sup>2</sup> ( _Xc_<sup>_TXc_)</sup><sup>_−_1.</sup>

Suppose the posterior samples are given by ( _c_<sup>(</sup><sup>_j_)</sup> _, β_ 0<sup>(</sup><sup>_j_)</sup><sup>_, β_</sup> 1<sup>(</sup><sup>_j_)</sup><sup>_, β_</sup> 2<sup>(</sup><sup>_j_)</sup><sup>_, σ_(</sup><sup>_j_))for</sup><sup>_j_=1</sup><sup>_, . . . , N_.The</sup> corresponding fitted values are given by:

_t �→ β_ 0<sup>(</sup><sup>_j_)</sup> + _β_ 1<sup>(</sup><sup>_j_)</sup><sup>_t_+</sup><sup>_β_</sup> 2<sup>(</sup><sup>_j_)ReLU(</sup><sup>_t −c_(</sup><sup>_j_))</sup>

3

for _t_ = 1 _, . . . , n_ . These can be plotted along with the original data.

One can also plot vertical lines corresponding to _c_<sup>(</sup><sup>_j_)</sup> to visualize uncertainty in the changeof-slope time point parameter _c_ .

The 95% approximate credible intervals for each parameter can be obtained by computing the 2.5th and 97.5th percentiles of the corresponding posterior samples.

Suppose you want to obtain posterior samples for _yt_<sup>_∗_</sup> for a future time point _t_<sup>_∗_</sup> . One can follow the algorithm listed above with one additional step to generate _yt_<sup>(</sup><sup>_∗j_)</sup><sup>_, j_=1</sup><sup>_, . . . , N_as</sup> follows:

1. Obtain samples _c_<sup>(1)</sup> _, . . . , c_<sup>(</sup><sup>_N_)</sup> by sampling, with replacement, from the set of possible values of _c_ : _{_ 2 _, . . . , n}_ with probability weights given by the posterior pmf _π_ ( _c |_ data). For this, one can use, for example, the choice function in `np.random.default` ~~`r`~~ `ng()` .

2. For each _j_ = 1 _, . . . , N_ ,

   - a) Fix _c_ = _c_<sup>(</sup><sup>_j_)</sup> .

   - b) Calculate _RSS_ ( _c_ ) and _β_<sup>ˆ</sup> _c_ by implementing linear regression with fixed _c_ .

   - c) Generate a chi-squared random variable _χ_<sup>2</sup> with _n −_ 3 degrees of freedom. Take _σ_<sup>(</sup><sup>_j_)</sup> = ~~�~~ _RSS_ ( _c_ ) _/χ_<sup>2</sup> .

   - d) Take _β_<sup>(</sup><sup>_j_)</sup> to be a generated random vector from the multivariate normal distribution with mean _β_<sup>ˆ</sup> _c_ and covariance ( _σ_<sup>(</sup><sup>_j_)</sup> )<sup>2</sup> ( _Xc_<sup>_TXc_)</sup><sup>_−_1.</sup>

   - e) Generate _yt_<sup>(</sup><sup>_∗j_)from the normal distribution with mean</sup><sup>_β_</sup> 0<sup>(</sup><sup>_j_)+</sup><sup>_β_</sup> 1<sup>(</sup><sup>_j_)</sup><sup>_t∗_+</sup><sup>_β_</sup> 2<sup>(</sup><sup>_j_)ReLU(</sup><sup>_t∗−_</sup> _c_<sup>(</sup><sup>_j_)</sup> ) and variance ( _σ_<sup>(</sup><sup>_j_)</sup> )<sup>2</sup> .

---

[← 3 Uncertainty Quantification for c, β 0 , β 1 , β 2 , σ](03-3-uncertainty-quantification-for-c-β-0-β-1-β-2-σ.md) · [Up: contents](index.md) · [5 More Changes of Slope →](05-5-more-changes-of-slope.md)
