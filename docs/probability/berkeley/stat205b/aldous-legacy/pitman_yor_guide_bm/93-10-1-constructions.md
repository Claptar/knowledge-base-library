---
title: 10.1. Constructions
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10.1. Constructions

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A Riemannian manifold _M_ is a manifold equipped with a Riemannian metric. Starting from this structure, there are various expressions for the LaplaceBeltrami operator ∆, and the Levi-Civita connection. Closely associated with the Laplace-Beltrami operator is the fundamental solution of the heat equation on _M_ derived from 2<sup><u>1</u>∆.Thisdefinesasemigroupoftransitionprobabilityop-</sup> erators from which one can construct a Brownian motion on _M_ . Alternatively, the Brownian motion on _M_ with generator 2<sup><u>1</u>∆canbeconstructedbysolvinga</sup> martingale problem associated with<sup><u>1</u></sup> 2<sup>∆.Notethatingeneralthepossibilityof</sup> explosion must be allowed: the _M_ -valued Brownian motion _B_ may be defined only up to some random _explosion time e_ ( _B_ ).

_J. Pitman and M. Yor/Guide to Brownian motion_

59

At least two other constructions of Brownian motion on _M_ may be considered, one known as _extrinsic_ , the other as _intrinsic_ . Some examples of the extrinsic construction appear in the work of Lewis and van den Berg [272] [420]. In general, this construction relies on Nash’s embedding of _M_ as a submanifold of R<sup>_ℓ_</sup> , with the induced metric. Following Hsu [171, Ch. 3], let _{ξα,_ 1 _≤ α ≤ ℓ}_ be the standard orthonormal basis in R<sup>_ℓ_</sup> , let _Pα_ be the orthogonal projection of _ξα_ onto _TxM_ , the tangent space at _x ∈ M_ . Then _Pα_ is a vector field on _M_ , and the Laplace-Beltrami operator ∆can be written as


and the Brownian motion started at _x ∈ M_ may be constructed as the solution of the Stratonovich SDE


where ( _W_<sup>_α_</sup> _,_ 1 _≤ α ≤ ℓ_ ) is a BM in R<sup>_ℓ_</sup> . See also Rogers and Williams [373] and Stroock [409, Ch. 4] for further development of the extrinsic approach.

The intrinsic approach to construction of BM on a manifold involves a lot more differential geometry. See Stroock [409, Chapters 7 and 8] and other texts listed in the references, which include the theory of semimartingales on manifolds, as developed by L. Schwartz, P. A. Meyer and M. Emery.

---

[← 10. Brownian motion on manifolds](92-10-brownian-motion-on-manifolds.md) · [Up: contents](index.md) · [10.2. Radial processes →](94-10-2-radial-processes.md)
