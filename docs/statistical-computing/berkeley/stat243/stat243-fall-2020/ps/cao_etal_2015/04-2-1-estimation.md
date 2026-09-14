---
title: 2.1. Estimation
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1. Estimation

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose that we have a random sample of n subjects. For the ith subject, let Yi.t/ be the response

_Analysis of Asynchronous Data_ 759

variable at time t and let Xi.t/ be a p × 1 vector of possibly time-dependent covariates. The response Yi.t/ may be a continuous, categorical or count variable, whereas the covariate Xi.t/ may include time-independent covariates, such as an intercept term, in addition to time varying covariates. The main requirement for the validity of the methods presented below is that, if the time varying covariates in Xi.t/ are multivariate, then the different covariates are measured at the same time points. Precise conditions on Xi.t/ are provided in the theoretical discussion in Section 2.2 and do not differ considerably from those needed for estimation with synchronous data.

We now focus on the regression model (1) that relates Yi.t/ to Xi.t/ through a time invariant coefficient. To estimate _β_ , we propose to use kernel weighting in a working independence generalized estimating equation (Diggle _et al._ , 2002) which has previously been developed for synchronous data. The resulting estimating equation is


Using counting process notation, this is equivalent to


where Kh.t/ = K.t=h/=h, K.t/ is a symmetric kernel function, which is usually taken to be the Epanechnikov kernel K.t/ = 0:75.1 − t<sup>2</sup> /+, and h is the bandwidth.

The kernel weighting accounts for the fact that the covariate and response are mismatched and permits contributions to Un. _β_ / from all possible pairings of response and covariate observations. It requires that the observation times Tij and Sik, i = 1, ::: , n, should be close for some but not all subjects. The theoretical results that are presented below require only that these observation times are close for a very small fraction of the overall sample of n individuals. If the observation times for covariate and response are close to each other, then the kernel weight is close to 1; however, if the observation times are far apart, then the contribution to the estimating equation (3) may be 0. In general, the relative contribution to Un. _β_ / is determined by the closeness of the covariate and response measurement times. Note that, for a response measured at a particular time Tij, there may be multiple Siks at which covariates are measured which contribute to the estimating equation. We solve Un. _β_ / = 0 to obtain an estimate for _β_ , which is denoted by _β_<sup>ˆ</sup> . Regarding the computations, once the kernel function K has been chosen and the bandwidth has been fixed, the estimating equation can be solved by using a standard Newton–Raphson implementation for generalized linear models, with good convergence properties.

---

[← 2. Time invariant coefficient](03-2-time-invariant-coefficient.md) · [Up: contents](index.md) · [2.2. Asymptotic properties →](05-2-2-asymptotic-properties.md)
