---
title: Data Structure
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data Structure

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Let T be the failure time of interest, e.g., time from AIDS diagnosis to death.

- Let C be censoring time, e.g., time from AIDS diagnosis to date of data collection.

- Let V be the time of failure reporting, e.g., time at which death of subject is reported.

- Let _X_ ( _u_ ) = [ _W, R_ ( _u_ ) _, R_ ( _u_ ) _∗ I_ ( _T ≤ t_ )], where _R_ ( _u_ ) = _I_ ( _V ≤ u_ ) and W is a vector of baseline covariates.

- _µ_ = _F_ ( _t_ ) = _P_ ( _T ≤ t_ ).

- Full Data is: _X_<sup>¯</sup> ( _V_ )

- Observed Data is: _Y_ = ( _T_<sup>�</sup> = _min_ ( _V, C_ ) _,_ ∆= _I_ ( _T_<sup>�</sup> = _V_ ) _, X_<sup>¯</sup> ( _T_<sup>�</sup> ))

34

- Note, this is the same as the right-censoring data structure already discussed in class.

---

[← Description](20-description.md) · [Up: contents](index.md) · [Ignoring Delay →](22-ignoring-delay.md)
