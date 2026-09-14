---
title: Choice of bandwidth in density estimation
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Choice of bandwidth in density estimation

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The accuracy of kernel density estimation will depend on the choice of bandwidth. Whether it is preferable use a small or large bandwidth depends on the true density, and _likelihood cross-validation_ is a method for adaptively choosing a good bandwidth. Before discussing this further, we must give an aside about inequalities in probability.

Let _f_ 0 denote the true density function of T, and f denote some estimate of this function. We first _<u>f</u>_ <u>(</u> _t_ <u>)</u> introduce _Shannon’s Inequality_ , which states that � _log_ ( _f_<sup>_<u>f</u>_</sup> 0<sup><u>(</u></sup> (<sup>_t_</sup> _t_<sup><u>)</u></sup> )<sup>)</sup><sup>_f_0(</sup><sup>_t_)</sup><sup>_dt≤log_</sup> � _f_ 0( _t_ )<sup>_f_0(</sup><sup>_t_)</sup><sup>_dt_.Thisisa</sup> special case of _Jensen’s Inequality_ , which states that if g is concave then _Ef_ 0 _g_ ( _T_ ) = � _g_ ( _t_ ) _f_ 0( _t_ ) _dt ≤ g_ (� _tf_ 0( _t_ )) = _g_ ( _Ef_ 0 _T_ ). Shannon’s Inequality comes from letting g(t) = log(t), and noting that g(t) is concave.

We next define the _risk_ of f as _R_ ( _f_ ) = _−Ef_ 0 _log_ ( _f_ ( _T_ )). Now, _R_ ( _f_ 0) _− R_ ( _f_ ) = � [ _log_ ( _f_ ( _t_ )) _− log_ ( _f_ 0( _t_ ))] _f_ 0( _t_ ) _dt_ = � _log_ ( _f_<sup>_<u>f</u>_</sup> 0<sup><u>(</u></sup> (<sup>_t_</sup> _t_<sup><u>)</u></sup> )<sup>)</sup><sup>_f_0(</sup><sup>_t_)</sup><sup>_dt≤log_</sup> � _ff_ 0(( _tt_ <u>))</u><sup>_f_0(</sup><sup>_t_)</sup><sup>_dt_=</sup><sup>_log_</sup> � _f_ ( _t_ ) _dt_ = _log_ (1) = 0, by Shannon’s Inequality, implying that _R_ ( _f_ ) _≥ R_ ( _f_ 0) for any f.

Because the risk is minimized at the true density, our intuition is that the kernel density estimate _fn,h_ best approximating _f_ 0 will be the one with the smallest risk: that is, we would like to choose as bandwidth

_h_ 0 = arg min _h_<sup>_−int_log</sup><sup>_fn,h_(</sup><sup>_T_)</sup><sup>_dF_0(</sup><sup>_T_)</sup><sup>_._</sup>

Since the expectation is unknown, this bandwidth is unknown as well. A seemingly natural way to estimate _h_ 0 is to replace the expectation by the empirical mean:


However, it follows that this maximum is achieved at _h_ = 0, which is clearly not a good bandwidth. Apparently, estimating the risk of a candidate density estimator _fn,h_ with the empirical risk estimate is not a good idea: this is due to the fact that _fn,h_ is itself already a function of the data.

Likelihood cross-validation deals with this problem by estimating the conditional risk � log _fn,h_ ( _T_ ) _dF_ 0( _T_ ) by splitting the sample in a training and validation sample, applying the kernel denisty estimator to the training sample, and estimating its conditional risk only with the validation sample. This so called cross-validated risk estimate provides now a sensible criteria for bandwidht selection, and more general, for selection among any set of candidate density estimators such as model-specific maximum likelihood estimators.

3

#### **Lecture 3 Notes**

Huaxia Qin

January 26, 2004

---

[← Estimation of the hazard](07-estimation-of-the-hazard.md) · [Up: contents](index.md) · [Data Adaptive Estimation of a Density →](09-data-adaptive-estimation-of-a-density.md)
