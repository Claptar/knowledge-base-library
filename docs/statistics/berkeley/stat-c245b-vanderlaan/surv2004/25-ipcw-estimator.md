---
title: IPCW Estimator
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# IPCW Estimator

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This leads to the following estimator:


where _G_<sup>¯</sup> _n_ ( _T_<sup>�</sup> _i_ ) is the Kaplan-Meier estimator of the censoring distribution based on n observations of:


and V now plays the role of the censoring variable.

If there is no delay (so _V_ = _T_ ), then ( _∗_ ) reduces to the Kaplan-Meier estimator. Like the Kaplan-Meier estimator, this IPCW estimator (in absence of covariates) is efficient. Heuristic proof is that if G is estimated efficiently assuming only CAR, then the IPCW estimator is efficient.

In this case, the Kaplan-Meier is the NPMLE estimator of censoring assumes only _CAR_ [ _G_ ( _c|X_ ) = _G_ ( _c_ )].

More detailed proof in paper.

35

---

[← Simple estimator in case of no covariates (W)](24-simple-estimator-in-case-of-no-covariates-w.md) · [Up: contents](index.md) · [Inference - Influence curve →](26-inference---influence-curve.md)
