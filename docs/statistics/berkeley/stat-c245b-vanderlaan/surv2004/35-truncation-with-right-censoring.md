---
title: Truncation with Right Censoring
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Truncation with Right Censoring

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Assume: _T ⊥_ ( _C, C_<sup>_∗_</sup> ) T _∼_ F _C_<sup>_∗_</sup> _∼ G_<sup>_∗_</sup> C _∼_ G We observe ( _T_<sup>˜</sup> = _min_ ( _T, C_ ) _, △_ = _I_ ( _T ≤ C_ ) _, C_<sup>_∗_</sup> )) _| T > C_<sup>_∗_</sup> _, C > C_<sup>_∗_</sup> Where ( _T_<sup>_′_</sup> _, C_<sup>_′_</sup> _, C_<sup>_∗′_</sup> ) has distribution ( _T, C, C_<sup>_∗_</sup> ) _| T > C_<sup>_∗_</sup> _, C > C_<sup>_∗_</sup> Define _T_<sup>˜</sup><sup>_′_</sup> = _min_ ( _T_<sup>_′_</sup> _, C_<sup>_′_</sup> ) and _△_<sup>_′_</sup> = _I_ ( _T_<sup>_′_</sup> _≤ C_<sup>_′_</sup> )

We want to estimate S(t) = Pr(T _>_ t) Express S(t) as distribution of data based on n i.i.d. ( _T_<sup>˜</sup> _i_<sup>_′, △′_</sup> _i_<sup>_, C_</sup> _i_<sup>_∗′_)fori= 1</sup><sup>_, . . . , n_</sup>


48


Using the Functional Delta Method

---

[← Example](34-example.md) · [Up: contents](index.md) · [Quantiles of F →](36-quantiles-of-f.md)
