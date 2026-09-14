---
title: 1.2. Definitions
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.2. Definitions

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This section records the basic definition of a Brownian motion _B_ , along with some common variations in terminology which we use for some purposes. The basic definition of _B_ , as a random continuous function with a particular family of finite-dimensional distributions, is motivated in Section 2 by the appearance of this process as a limit in distribution of rescaled random walk paths.

Let (Ω _, F,_ P) be a probability space. A stochastic process ( _B_ ( _t, ω_ ) _, t ≥_ 0 _, ω ∈_ Ω) is a _Brownian motion_ if

- (i) For fixed each _t_ , the random variable _Bt_ = _B_ ( _t, ·_ ) has Gaussian distribution with mean 0 and variance _t_ .

- (ii) The process _B_ has _stationary independent increments_ .

- (iii) For each fixed _ω ∈_ Ω, the path _t → B_ ( _t, ω_ ) is continuous.

The meaning of (ii) is that if 0 _≤ t_ 1 _< t_ 2 _< ... < tn_ , then _Bt_ 1 _, Bt_ 2 _−Bt_ 1 _, ..., Btn − Btn−_ 1 are independent, and the distribution of _Bti − Bti−_ 1 depends only on _ti − ti−_ 1. According to (i), this distribution is normal with mean 0 and variance _ti − ti−_ 1. We say simply that _B_ is _continuous_ to indicate that _B_ has continuous paths as in (iii). Because of the convolution properties of normal distributions, the joint distribution of _Xt_ 1 _, ..., Xtn_ are consistent for any _t_ 1 _< ... < tn_ . By Kolmogorov’s consistency theorem [43, Sec. 36], given such a consistent family of finite dimensional distributions, there exists a process ( _Xt, t ≥_ 0 ) satisfying (i) and (ii), but the existence of such a process with continuous paths is not obvious. Many proofs of existence of such a process can be found in the literature. For the derivation from Kolmogorov’s criterion for sample path continuity, see [370, _§_ , Theorem (1.8)]. Freedman [139] offers a more elementary approach via the following steps:

- Step 1: Construct _Xt_ for _t ∈ D_ = _{_ dyadic rationals _}_ = _{_ 2<sup>_<u>kn</u>}_.</sup>

- Step 2: Show for almost all _ω_ , _t → X_ ( _t, ω_ ) is uniformly continuous on _D ∩_ [0 _, T_ ] for any finite T.

- Step 3: For such _ω_ , extend the definition of _X_ ( _t, ω_ ) to _t ∈_ [0 _, ∞_ ) by continuity.

_J. Pitman and M. Yor/Guide to Brownian motion_

5

---

[← 1.1. History](05-1-1-history.md) · [Up: contents](index.md) · [• Step 4: Check that (i) and (ii) still hold for the process so defined. →](07-step-4-check-that-i-and-ii-still-hold-for-the-process-so-def.md)
