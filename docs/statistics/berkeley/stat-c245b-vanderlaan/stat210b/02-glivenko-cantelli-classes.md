---
title: Glivenko-Cantelli Classes
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Glivenko-Cantelli Classes

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When _F_ is a finite class of functions in _L_<sup>1</sup> ( _P_ ), it is clear from the law of large numbers that _∥Pn − P ∥F →_ 0 almost surely. Whenever this property holds for a class _F_ , we call _F_ a _P-Glivenko-Cantelli class_ . However, not all classes of functions are GlivenkoCantelli. Consider _F_ being the class of all real-valued functions bounded between zero and one. Then for each _n_ , there exists a (random) _fn ∈F_ such that _fn_ = 1( _O_ 1 _, ..., On_ ) so that _Pnfn_ = 1, but we could have _Pfn_ = 0 if _P_ is a continuous distribution. Thus

1

_∥Pn − P ∥F ≥_ 1 for all _n_ , so _F_ is not Glivenko-Cantelli. Basically, the larger the class _F_ , the harder it is for _F_ to be Glivenko-Cantelli.

This leads to the _first major goal of empirical process theory_ : Determine sufficient conditions for _F_ to be Glivenko-Cantelli that are as easy to check as possible, but apply to as large a class _F_ as possible.

---

[← Notation and Basic Setup](01-notation-and-basic-setup.md) · [Up: contents](index.md) · [Convergence in Distribution →](03-convergence-in-distribution.md)
