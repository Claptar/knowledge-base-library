---
title: 2.2. Asymptotic properties
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2023/ps/cao_etal_2015.pdf
licence: BSD-3-Clause
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.2. Asymptotic properties

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/cao_etal_2015.pdf) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We next study the asymptotic properties of _β_<sup>ˆ</sup> , including the bias–variance trade-off with respect to the bandwidth selection. We allow the observations of Xi.·/ and the observations of Yi.·/ to be arbitrarily correlated. We specify our assumptions on the covariance structure as follows. For s, t ∈ [0, _τ_ ],letvar _{_ Y.t/|X.t/ _}_ = _σ{_ t, X.t/ _}_<sup>2</sup> andcov _{_ Y.s/, Y.t/|X.s/, X.t/ _}_ = r _{_ s, t, X.s/, X.t/ _}_ , where _τ_ is the maximum follow-up time. Observe that the conditional variances and correlations of Y are completely unspecified and may depend on X.

We need the following conditions.

_Condition 1._ Ni.t, s/ is independent of .Yi, Xi/ and, moreover, E _{_ dNi.t, s/ _}_ = _λ_ .t, s/ dt ds, where _λ_ .t, s/ is a twice-continuous differentiable function for any 0 ⩽ t, s ⩽ _τ_ . In addition, Borel measure for _G_ = _{λ_ .t, t/> 0, t ∈ [0, _τ_ ] _}_ is strictly positive. For t1̸ = s1 and t2̸ = s2, P _{_ dN.t1, t2/ =

760 _H. Cao, D. Zeng and J. P. Fine_

1|N.s1, s2/ − N.s1−, s2−/ = 1 _}_ = f.t1, t2, s1, s2/ dt1 dt2 where f.t1, t2, s1, s2/ is continuous for t1̸ = s1, and t2̸ = s2 and f.t1 ± , t2 ± , s1 ± , s2±/ exists.

_Condition 2._ If there is a vector _γ_ such that _γ_<sup>T</sup> X.s/ = 0 for any s ∈ _G_ with probability 1, then _γ_ = 0.

_Condition 3._ For any _β_ in a neighbourhood of _β_ 0, the true value of _β_ , E[X.s/ _g{_ X.t/<sup>T</sup> _β}_ ] is continuously twice differentiable in .t, s/ ∈ [0, _τ_ ]<sup>⊗2</sup> and | _g_<sup>′</sup> _{_ X.t/<sup>T</sup> _η}_ | ⩽ q _{_ ∥X.t/∥ _}_ for some q.·/ satisfying that E[∥X.t/∥<sup>4</sup> q _{_ ∥X.t/∥ _}_<sup>2</sup> ] is uniformly bounded in t. Additionally, E _{_ ∥X.t/∥<sup>4</sup> _}_ < ∞. Furthermore, E[X.s1/X.s2/<sup>T</sup> r _{_ t1, t2, X.t1/, X.t2/ _}_ ] and E[X.s1/X.s2/<sup>T</sup> _g {_ X.t1/<sup>T</sup> _β_ 0 _} g{_ X.t2/<sup>T</sup> _β_ 0 _}_ ] are continuously twice differentiable in .s1, s2, t1, t2/ ∈ [0, _τ_ ]<sup>⊗4</sup> . Moreover,


and


_Condition 4._ K.·/ is a symmetric density function satisfying � z<sup>2</sup> K.z/ dz< ∞ and � K.z/<sup>2</sup> dz< ∞. Additionally, nh →∞.

_Condition 5._ nh<sup>5</sup> → 0:

Condition 1 requires that the observation process is independent of both the response and the covariates. We require that _λ_ .s, t/ is positive in a neighbourhood of the diagonal where s = t at some time points, but not all time points, and _λ_ .s, t/ need not be greater than 0 when s̸ = t: Analogous assumptions have been widely utilized with synchronous data, as in Lin and Ying (2001), Yao _et al_ . (2005) and Martinussen and Scheike (2010). We consider the sparse longitudinal set-up where the number of observations Ni.t, s/ has finite expectation but may have infinite support, similarly to Martinussen and Scheike (2010) with synchronous data. This differs from the dense setting that is popular in functional data analysis where Li and Mi →∞ as n →∞ for all i. Condition 2 ensures identifiability of _β_ whereas condition 3 posits smoothness assumptions on the expectation of some functionals of X.s/ and gives additional regularity conditions on the observation intensity _λ_ . The latter condition implies that the covariance function of X.t/ is twice continuously differentiable. Such a condition is not satisfied by processes having independent increments. For Gaussian processes, the implication is that X.t/ has continuous but not necessarily differentiable sample paths with probability 1. In theory, the condition may still allow the actual path of X.s/ to be discontinuous, as with categorical covariates which jump according to a point process, where discontinuities may occur with zero measure. In Section 6, we discuss the possibility of relaxing condition 3. Conditions 4 and 5 specify valid kernels and bandwidths.

The following theorem, which is established in Appendix A, states the asymptotic properties of _β_<sup>ˆ</sup> .

_Theorem 1._ Under conditions 1–4, the asymptotic distribution of _β_<sup>ˆ</sup> satisfies


where A. _β_ 0/ = �s<sup>E[X.s/</sup><sup>_g_′</sup><sup>_{_X.s/T</sup><sup>_β_0</sup><sup>_}_X.s/T]</sup><sup>_λ_.s, s/ds,</sup><sup>_β_0 is the true regression coefficient and</sup> C is a constant, which can be found in Appendix A. The asymptotic variance


_Analysis of Asynchronous Data_ 761

The asymptotic results do not depend on _λ_ .s, t/ for s̸= t as we are dealing with asynchronous data in which the response and covariates are never ‘perfectly’ matched, i.e. there is zero measure associated with identical observation times. The variance depends critically on the joint density of the observation times on the diagonal, which determines how quickly information accumulates from an asynchronous response and covariates across subjects. For the case where synchronous data occur with positive probability, synchronous data methods may be employed with the synchronous portion of the data and will yield improved convergence rates relatively to the methods proposed above for pure asynchronous data.

If the bandwidth is further restricted by condition 5, then the asymptotic bias in condition (5) vanishes and _β_<sup>ˆ</sup> is consistent.

_Corollary 1._ Under conditions 1–5, _β_<sup>ˆ</sup> is consistent and converges to a mean 0 normal distribution given in theorem 1.

Forstatisticalinference,itischallengingtoestimatethevarianceinequation(6)directly,owing to the time varying quantities _σ_ and _λ_ , which are difficult to estimate well without imposing additional assumptions on the covariate and response processes. In practice, we estimate Σ by


and estimate the variance of _β_<sup>ˆ</sup> by the sandwich formula

This approach has been adopted by Cheng and Wei (2000) and Lin and Ying (2001) with synchronous data as well.

_Corollary 2._ Under conditions 1–5, the sandwich formula consistently estimates the variance of _β_<sup>ˆ</sup> :

Our method depends on the selection of the bandwidth. Theoretically speaking, condition 4 says that the bandwidth cannot be too small (smaller than O.n<sup>−1</sup> /); otherwise, the variance will be quite large. However, to eliminate the asymptotic bias, we require a small bandwidth. Theorem 1 indicates that the bias is of order O.n<sup>1=2</sup> h<sup>5=2</sup> /, so we should choose bandwidth h = o.n<sup>−1=5</sup> /. With this choice of bandwidth, we achieve a rate of convergence o.n<sup>2=5</sup> /, which is slower than the parametric n<sup>1=2</sup> rate of convergence for synchronous data under model (1).

We propose a data-adaptive bandwidth selection procedure despite the fact that traditional cross-validation methods are not applicable owing to asynchronous measurement times for the covariates and response. On the basis of condition (5), we first regress _β_<sup>ˆ</sup> .h/ on h<sup>2</sup> in a reasonable range of h to obtain the slope estimate C<sup>ˆ</sup> . To obtain the variance, we split the data randomly into two parts and obtain regression coefficient estimates _β_<sup>ˆ</sup> 1.h/ and _β_<sup>ˆ</sup> 2.h/ based on each halfsample. The variance of _β_<sup>ˆ</sup> .h/ is then estimated by V.h/<sup>ˆ</sup> = _{β_<sup>ˆ</sup> 1.h/ − _β_<sup>ˆ</sup> 2.h/ _}_<sup>2</sup> =4. Using both C<sup>ˆ</sup> and Vˆ h, we thus calculate the mean-squared error as Cˆ 2h4 + V.h/ˆ on the basis of theorem 1. Finally, we select the optimal bandwidth h minimizing this mean-squared error.

Our numerical studies show that small bias may be achieved for bandwidths between n<sup>−1</sup> and n<sup>−1=2</sup> , with stable variance estimation and confidence interval coverage for bandwidths larger than n<sup>−4=5</sup> . Within this range, the bias diminishes as the sample size increases, as predicted by theorem 1. Methods based on asynchronous data are generally less efficient than those based on

762 _H. Cao, D. Zeng and J. P. Fine_

synchronous data, with the information in synchronous data dominating that in asynchronous data. Numerical studies (which are not reported) demonstrate that, in moderate sample sizes, asynchronous data may yield comparable but reduced efficiency when there are a large number of observation times for the covariate process.

---

[← 2.1. Estimation](04-2-1-estimation.md) · [Up: contents](index.md) · [3. Time-dependent coefficients →](06-3-time-dependent-coefficients.md)
