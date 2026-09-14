---
title: Understanding the Radon-Nikodym theorem.
source: https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/lecture_1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Understanding the Radon-Nikodym theorem.

**Source:** [`lecture_1.pdf`](https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Physical **density** is mass per unit volume, as a local limit for heterogeneous material. In the setting of two PMs _µ, ν_ on ( _S, S_ ) we would like to define density as


but this definition doesn’t work very generally. However, assuming _S_ = _σ_ ( _Bi ,_ 1 _≤ i < ∞_ ) (countably generated), we have finite fields _Fn_ = _σ_ ( _Bi ,_ 1 _≤ i ≤ n_ ) and we can define


which is finite when _ν ≪ µ_ , that is


Key point: ( _Xn_ ) is a martingale w.r.t. ( _S, S, µ_ ).


Key point: ( _Xn_ ) is a martingale w.r.t. ( _S, S, µ_ ). And assumption _ν ≪ µ_ implies (easy: by contradiction)

_∀ε >_ 0 _∃δ_ ( _ε_ ) _>_ 0 such that _µ_ ( _A_ ) _< δ_ ( _ε_ ) implies _ν_ ( _A_ ) _< ε_

This implies ( _Xn_ ) is uniformly integrable, and MG convergence says there is a limit function _f_


which has the desired “density” property


So we can indeed get the density as some particular limit


But not canonical.

---

[← Another secret. .](03-another-secret.md) · [Up: contents](index.md) · [Conditioning and MT →](05-conditioning-and-mt.md)
