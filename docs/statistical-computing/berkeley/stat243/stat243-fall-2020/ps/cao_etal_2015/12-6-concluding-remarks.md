---
title: 6. Concluding remarks
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6. Concluding remarks

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this paper, we proposed kernel-weighted estimating equations for generalized linear models

768 _H. Cao, D. Zeng and J. P. Fine_


<!-- Start of picture text -->
400 600 800 1000 1200 1400<br>Days<br>4<br>2<br>0<br>Beta(t)<br>−2<br>−4<br>−6<br><!-- End of picture text -->

**Fig. 2.** Trajectory of time varying coefficient estimation with a data-adaptive bandwidth based on model (12): _h_ D 102 days

with asynchronous longitudinal data. The methods include estimators for models with either timeinvariantcoefficient _β_ ortime-dependentcoefficient _β_ .t/.Theproceduresweredevelopedby extending the univariate counting process framework for the observation process for synchronous data to a bivariate counting process set-up that is appropriate for asynchronous data. The resulting theory demonstrates that the rates of convergence that are achieved with asynchronous data are generally slower than those achieved with synchronous data and that, even under the time-independent model (1), parametric rates of convergence are not achievable.

To borrow information from nearby points, we require the covariance function of X.t/ to be twice continuously differentiable for t = s: These assumptions are sufficient for our theoretical arguments and are similar to those required for synchronous data for estimation of _β_ .t/, where at least some smoothness of X.t/ is needed. One may relax the continuous differentiability assumption such that the covariance function of X.t/ is continuously differentiable from either the left-hand or right-hand side. This relaxation allows a more general class of X.t/, including processes with independent increments, such as Poisson processes and Brownian motion. The trade-off is that the resulting kernel-weighted estimators will have an asymptotic bias which is of the order h instead of h<sup>2</sup> as stated in theorem 1, and the resulting convergence rates and optimal bandwidths may differ. The theoretical justification for these results requires non-trivial modifications of the proofs in this paper and are left for further research.

Global approaches like functional data analysis (Yao _et al_ ., 2005; Sent¨urk and Muller, 2010) or basis approximations (Zhou _et al_ ., 2008) for synchronized data provide added structure for incorporating correlation between observations in the estimation procedure. The extension to asynchronous data does not appear to have been studied in the literature. Given the slow rates of convergence for the local method, the extent to which global methods will improve efficiency is unclear. Additional assumptions may be required to achieve such gains and may

_Analysis of Asynchronous Data_ 769

be more restrictive than the minimal set of conditions that are specified in theorems 1 and 2. A deeper investigation of these issues is clearly warranted but is beyond the scope of the current paper.

In this paper, we did not consider the partially time-dependent model, in which some coefficients are time invariant and some coefficients are time dependent. As in earlier work on this model with synchronous data, a two-step procedure may be useful for estimation. This merits further investigation.

The asymptotic theory for _β_<sup>ˆ</sup> .t/ under model (2) in Section 3 is pointwise. The construction of simultaneous confidence intervals and hypothesis tests for the time-dependent coefficients would be useful in applications, like the HIV study. This requires a careful theoretical study of the uniform convergence properties of the estimator like in Zhou and Wu (2010). Future work is planned.

---

[← 5. Application to human immunodeficiency virus data](11-5-application-to-human-immunodeficiency-virus-data.md) · [Up: contents](index.md) · [Acknowledgements →](13-acknowledgements.md)
