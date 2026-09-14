---
title: Estimating the influence curve
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Estimating the influence curve

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The influence curve for the IPCW estimator is:


where


This can be estimated as:


Finally, estimate _Fn_ ( _t|T_<sup>�</sup> _> u_ ) be repeating the IPCW sample for each censoring time (u) using only those subjects for which _T_<sup>�</sup> _> u_

The variance of the IPCW estimator can be estimated as:


Of course, this whole procedure is typically repeated for many _t_ .

---

[← Inference - Influence curve](26-inference---influence-curve.md) · [Up: contents](index.md) · [Long Delays →](28-long-delays.md)
