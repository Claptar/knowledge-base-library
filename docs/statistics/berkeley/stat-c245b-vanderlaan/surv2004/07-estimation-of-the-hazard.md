---
title: Estimation of the hazard
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Estimation of the hazard

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose _T_ 1 _, ..., Tn_ are iid and continuous, there is no censoring, and we want to estimate _λ_ ( _t_ ) nonparametrically. We recall that _λ_ ( _t_ ) = _Sf_ <u>((</u> _tt_ <u>))</u><sup>becauseTiscontinuous,andthenusenonparametric</sup> density estimation for the numerator and the empirical survival function for the denominator.

There are many ways to perform density estimation, but a popular method is _kernel density estimation_ . For this technique we choose a positive number h to be the _bandwidth_ , a density K( _•_ ) centered at zero to be the _kernel_ , and estimate _f_ ( _t_ ) by _fn,h_ ( _t_ ) = _nh_ <u>1</u><sup>Σ</sup> _i_<sup>_n_</sup> =1<sup>_K_(</sup><sup>_<u>Ti</u>_</sup> _h_<sup>_−t_).Typicallythe</sup> density estimates have less bias but more variance as h is decreased toward zero.

---

[← The hazard and survival functions in the continuous setting](06-the-hazard-and-survival-functions-in-the-continuous-setting.md) · [Up: contents](index.md) · [Choice of bandwidth in density estimation →](08-choice-of-bandwidth-in-density-estimation.md)
