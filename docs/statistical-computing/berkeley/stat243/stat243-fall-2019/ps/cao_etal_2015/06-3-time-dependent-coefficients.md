---
title: 3. Time-dependent coefficients
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Time-dependent coefficients

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The observed data are the same as in Section 2. Suppose that we are interested in estimating the coefficient _β_ .t/ in model (2) at a fixed time point t. Similarly to synchronous data, in the asynchronous set-up, neither the response Y.t/ nor the covariate X.t/ is generally observed at time t. However, one may utilize measurements of these variables which are taken close in time to t to estimate _β_ .t/. Kernel weighting is employed to downweight measurements of Y.t/ and X.t/ on the basis of their distance from t. Recall that, in Section 2, a single bandwidth was used to weight on the basis of the distance between the covariate and response measurements. The main difference in this section is that two bandwidths are needed to weight separately on the basis of the distance of the response measurement from time t and the distance of the covariate measurement from time t. Fitting model (2) with synchronous data requires only a single bandwidth, since the response and covariate are always measured at the same time points.

The doubly kernel-weighted estimating equation for _β_ .t/ is


where Kh1,h2 .t, s/ = K.t=h1, s=h2/=.h1h2/ and K.t, s/ is a bivariate kernel function, say, the product of univariate Epanechnikov kernels K.t, s/ = 0:5625.1 − t<sup>2</sup> /+.1 − s<sup>2</sup> /+. We solve equation (7) to obtain an estimate for _β_ .t/, which is denoted as _β_<sup>ˆ</sup> .t/. Computationally, the Newton–Raphson iterative method can be utilized after choosing Kh1,h2 and fixing the bandwidths. As this estimating equation leads to separate estimates of _β_ .t/ at each time point t, the resulting inferential procedures that are described below are pointwise and not simultaneous. To obtain the trajectory of _β_<sup>ˆ</sup> .t/, one solves equation (7) on a dense grid of time points in .0, _τ_ /.

To derive the large sample properties of the estimator, we need the following assumptions.

_Condition 1_<sup>′</sup> _._ Ni.t, s/ is independent of .Yi, Xi/ and, moreover, E _{_ dNi.t, s/ _}_ = _λ_ .t, s/ dt ds, where _λ_ .t, s/ is twice continuous differentiable for any 0 ⩽ t, s ⩽ _τ_ and is strictly positive for t = s. For t1̸ = s1, t2̸ = s2, P _{_ dN.t1, t2/ = 1|N.s1, s2/ − N.s1− , s2−/ = 1 _}_ = f.t1, t2, s1, s2/ dt1 dt2 where f.t1, t2, s1, s2/ is continuous for t1̸ = s1 and t2̸ = s2 and f.t1 ± , t2 ± , s1 ± , s2±/ exists.

_Condition 2_<sup>′</sup> _._ For any fixed time point t, if there is a vector _γ_ such that _γ_<sup>T</sup> X.t/ = 0, then _γ_ = 0.

_Condition 3_<sup>′</sup> _._ E[X.s1/ _g{_ X.s2/<sup>T</sup> _β_ .s3/ _}_ ] is continuously twice differentiable in .s1, s2, s3/ ∈ s[0, _τ_ ]<sup>⊗3</sup> and | _g_<sup>′</sup> _{_ X.t/<sup>T</sup> _η}_ | ⩽ q _{_ ∥X.t/∥ _}_ for some q.·/ satisfying that E[∥X.t/∥<sup>4</sup> q _{_ ∥X.t/∥<sup>2</sup> _}_ ] is uniformly bounded in t. Moreover, E[X.t1/X.s1/<sup>T</sup> r _{_ s2, t2, X.s2/, X.t2/ _}_ ] is continuously twice differentiablein .t1, s1, t2, s2/ ∈ [0, _τ_ ]<sup>⊗4</sup> and E[X.t1/X.s1/<sup>T</sup> _g{_ X.t2/<sup>T</sup> _β_ 0.t/ _}g{_ X.s2/<sup>T</sup> _β_ 0.t/ _}_ ]iscontinuously twice differentiable in .t1, s1, t2, s2, t/ ∈ [0, _τ_ ]<sup>⊗5</sup> .

_Condition 4_<sup>′</sup> _._ The kernel function K.x, y/ is a symmetric bivariate density function for x and y. In addition, � |x<sup>3</sup> y|K.x, y/dx dy< ∞, � |xy<sup>3</sup> | K.x, y/ dx dy< ∞, � x<sup>2</sup> y<sup>2</sup> K.x, y/ dx dy< ∞ and � K.x, y/<sup>2</sup> dx dy< ∞. Moreover, nh1h2 →∞.

_Condition 5_<sup>′</sup> _._ .nh1h2/<sup>1=2</sup> .h<sup>2</sup> 1<sup>+h2</sup> 2<sup>/→0.</sup>

_Analysis of Asynchronous Data_ 763

Conditions 1<sup>′</sup> –5<sup>′</sup> are similar in spirit to conditions 1–5 in Section 2. Condition 1<sup>′</sup> strengthens condition 1, requiring that, to estimate _β_ .t/ at time t, _λ_ .t, t/> 0: Condition 2<sup>′</sup> is a modified identifiability assumption for _β_ .t/ at time t: Condition 3<sup>′</sup> posits the requirements on the covariance function of the covariate process, with the implications similar to those discussed in Section 2. Conditions 4<sup>′</sup> and 5<sup>′</sup> are provided for the kernel function and the bandwidth.

We establish the asymptotic distribution of _β_<sup>ˆ</sup> .t/ in the following theorem.

_Theorem 2._ Under conditions 1<sup>′</sup> –4<sup>′</sup> , the asymptotic distribution of _β_<sup>ˆ</sup> .t/ for any fixed time point t ∈ .0, _τ_ / based on solving Un _{β_ .t/ _}_ in equation (7) is


where B _{β_ 0.t/, t _}_ = _λ_ .t, t/E[X.t/ _g_<sup>′</sup> _{_ X.t/<sup>T</sup> _β_ 0.t/ _}_ X.t/<sup>T</sup> ], _β_ 0.t/ is the true coefficient function and D1.t/, D2.t/ and D3.t/ are known functions, whose specific forms can be found in Appendix A. The variance function is


If the bandwidth is further restricted by condition 5<sup>′</sup> , then the asymptotic bias in equation (8) vanishes and _β_<sup>ˆ</sup> .t/ is consistent for _β_ 0.t/, as stated in the following corollary.

_Corollary 3._ Under conditions 1<sup>′</sup> –5<sup>′</sup> _β_<sup>ˆ</sup> .t/ is consistent and converges to the zero-mean normal distribution given in theorem 2 for any t ∈ .0, _τ_ /.

For any fixed time point t, the variance estimator for _β_<sup>ˆ</sup> .t/ may be obtained by expanding the estimating equation (7) similarly to the time invariant case.

_Corollary 4._ Under conditions 1<sup>′</sup> –5<sup>′</sup> , for any fixed time point t ∈ .0, _τ_ /, the sandwich formula consistently estimates the variance of _β_<sup>ˆ</sup> .t/.

If we let h = h1 = h2, on the basis of condition 4<sup>′</sup> , a valid bandwidth is larger than O.n<sup>−1=2</sup> /. In contrast, theorem 2 indicates that the bias is of order O.n<sup>1=2</sup> h<sup>3</sup> /, so we should choose bandwidth h = o.n<sup>−1=6</sup> /. With this choice of bandwidth, we achieve o.n<sup>1=3</sup> / rate of convergence, which is slower than the o.n<sup>2=5</sup> / rate of convergence for the synchronous case with time-dependent coefficient (Martinussen and Scheike, 2010). In general, similarly to model (1), asynchronous estimators for model (2) converge more slowly and are less efficient than those based on synchronous data.

Our numerical studies show that bandwidths near n<sup>−1=2</sup> perform well with moderate sample sizes. As with model (1), the automation of bandwidth selection for estimation of _β_ .t/ is challenging with asynchronous data because the calculation of error criteria for use in crossvalidation is unclear. Our suggested procedure calculates the integrated mean-squared error. This is accomplished through calculating mean-squared errors separately at time points of interest by adapting the approach for time-independent coefficients in Section 2. We then sum them to obtain integrated mean-square errors and choose the bandwidth that minimizes this summation. This procedure performs well in the simulation studies.

---

[← 2.2. Asymptotic properties](05-2-2-asymptotic-properties.md) · [Up: contents](index.md) · [4. Numerical studies →](07-4-numerical-studies.md)
