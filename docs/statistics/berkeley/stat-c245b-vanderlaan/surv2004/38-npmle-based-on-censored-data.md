---
title: NPMLE based on censored data
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# NPMLE based on censored data

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _X_ 1 _, X_ 2 _, . . . , Xn_ be _n i.i.d. X ∼ FX ∈M_ , where _M_ is non-parametric, and _Y_ 1 _, Y_ 2 _, . . . , Yn_ be _n i.i.d._ observations _Y_ = _φ_ ( _C, X_ ) _∼ PFX ,G_ . Assume CAR on _G_ . As in the case when we were dealing

51

with finite dimensional real-valued parameter, we maximize the log-likelihood ratio of the observed data:


Suppose we restrict to or know that _FX_ domain is a finite and discrete set of points _{x_ 1 _, . . . , xm}_ : _FX ∈ D_ = � _p_ = ( _p_ 1 _, . . . , pm_ ) :<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_pj_= 1</sup> �. Hence, _FX_ is a multinomial distribution _M_ ( _n, p_ 1 _, . . . , pm_ ). Let _nj_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_I_(</sup><sup>_Xi_=</sup><sup>_xj_).ThuswecanusethegeneralEM-alg,becausethemultinomialdistribu-</sup> tion is a member of the exponential family of distributions.

1. In step _k_ = 0 initialize _p_<sup>0</sup> = (1 _/m, . . . ,_ 1 _/m_ );

2. For _k_ = 1 _,_ 2 _, . . ._ until convergence:


Setting


and using the constraint<sup>�</sup> _pj_ = 1 leads to the following result:


which is an example of a _self-consistency equation_ introduced in the previous lecture.

NPMLE found using EM-alg is not necessarily consistent. One such interesting example is the NPLME of the bivariate survival function subject to censoring. Typically, this kind of problems arise in studies of twins with a certain disease. Let _T_ = ( _T_ 1 _, T_ 2) be the bivariate survival time of a randomly drawn twin pair from a population with unknown survival distribution _S_ 0 to be estimated. Assume that each pair is subject to right censoring which will be denoted with _C_ = ( _C_ 1 _, C_ 2). For each twin we observe the minimum of the censoring and survival time, as well as if the observation is censored or not:


52

The data can be thought of as occupying points, half-lines and quadrants in the plane as shown in fig. 1 below.

Assuming that the model for bivariate survival function is non-parametric, the NPMLE satisfies the self-consistency equations solved by the EM-alg. In the initialization step, the algorithm assigns mass of 1 _/n_ for each observation. Then for all censored pairs, i.e. those that are represented as half-lines and quadrants, their mass is redistributed over the associated region of coarsening _C_ ( _Yi_ ), according to an estimate of the conditional distribution which is obtained over all uncensored observations that fall into _C_ ( _Yi_ ). This is repeated with the new masses until the algorithm converges. If the time is on a continuous scale then the half-lines a.s. do not contain any (uncensored) observations, hence the conditional distribution for singly-censored observations can not be estimated properly, and as a consequence the NPMLE for bivariate right-censored data is inconsistent.

In series of papers Van der Laan[1994, 1995] proposed a way to repair the consistency of the NPMLE, by employing the following strategy: for each of the singly-censored observations replace the half-line with (half-)strip of width _h_ parallel to the half-line (as shown in the picture) and estimate the conditional distribution from all uncensored observations with bigger time-to-event than that of the singly-censored observation, hence allowing the EM-alg to redistribute the mass 1 _/n_ over such a half-strip. This estimator is asymptotically efficient when _h →∞_ and is asymptotically unbiased even if _h_ is fixed.

---

[← 3 The EM-Algorithm For Computing The MLE of a Full Data Model Based on Censored Data](37-3-the-em-algorithm-for-computing-the-mle-of-a-full-data-mode.md) · [Up: contents](index.md) · [References →](39-references.md)
