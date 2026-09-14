---
title: Survival Analysis
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Survival Analysis

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The most basic setup in a field of statistics known as _survival analysis_ is as follows. We are interested a random variable 0 _≤ T_ with cumulative distribution function _F_ and survival function _S_ = 1 _− F_ . Here _T_ is often called a _survival time_ or _failure time_ . We would like to estimate _S_ , but aren’t able to observe _n_ i.i.d. copies of _T_ . Instead we observe _n_ i.i.d. copies of _O_ = ( _T,_<sup>˜</sup> ∆) _∼ P_ , where _T_<sup>˜</sup> = min( _T, C_ ) and ∆= 1( _T ≤ C_ ) for 0 _≤ C ∼ G ⊥ F_ a _censoring time_ . As usual, _Pn_ denotes the empirical distribution. For simplicity, we will here assume that _F_ and _G_ represent continuous distributions. The most common application is where the survival time _T_ measures the time untill death or recurrence of illness in a medical study, and the censoring time _C_ is the time at which the subject drops out of the study or is unavailable for follow-up. Another common application is in _reliability analysis_ where _T_ measures the length of time a product such as a car lasts before breaking down. The assumption that _T ⊥ C_ (meaning _T_ and _C_ are independent) is fairly strong, and there are many examples where it is violated, but it can be slightly weakened to a so called _coarsening at random_ assumption discussed in van der Laan and Robins. But without coarsening at random, essentially nothing can be said about the distribution of _T_ .

---

[← Product Integrals and Cumulative Hazards](21-product-integrals-and-cumulative-hazards.md) · [Up: contents](index.md) · [Identifiability and Estimation in Survival Analysis →](23-identifiability-and-estimation-in-survival-analysis.md)
