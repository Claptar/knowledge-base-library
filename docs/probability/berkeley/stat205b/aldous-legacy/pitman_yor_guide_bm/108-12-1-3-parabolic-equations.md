---
title: 12.1.3. Parabolic equations
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12.1.3. Parabolic equations

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Following is a list of PDE’s of parabolic type related to BM(R<sup>_δ_</sup> ). For _u_ : [0 _, ∞_ ) _×_ R<sup>_δ_</sup> _→_ R, write _u_ = _u_ ( _t, x_ ), let _ut_ := _∂u/∂t_ , and let ∆denote the Laplacian, and _∇_ the gradient, acting on the variable _x_ . Assume the initial boundary condition _u_ (0 _, x_ ) = _f_ ( _x_ ). Then


is solved by


for _g_ : [0 _, ∞_ ) _×_ R<sup>_δ_</sup> _→_ R is solved by


where _c_ = _c_ ( _x_ ) _∈_ R is solved by


for _b_ = _b_ ( _x_ ) _∈_ R is solved by


Equation (114) is the classical _heat equation_ , discussed already in Section 4.3. See [210, _§_ 4.3] for the one-dimensional case, and Doob [99] for a more extensive discussion.

Equation (118) is the variant when Brownian motion _B_ is replaced by a BM with drift _b_ , which may be realized as the solution of the SDE


It is a nice result, due to Zvonkin [459], for dimension _δ_ = 1 and VeretennikovKrylov [425] for _δ_ = 2 _,_ 3 _, . . ._ , that for _b_ Borel bounded, equation (120) has a unique strong solution; that the solution is unique in law is a consequence

65

_J. Pitman and M. Yor/Guide to Brownian motion_

of Girsanov’s theorem. The right side of (119) equals E<sup>_x_</sup> [ _f_ ( _Xt_ )] for ( _Xt_ ) the solution of (120).

The expression on the right side of (117) is the celebrated _Feynman-Kac formula_ . See [217] for a historical review, and [189] for further discussion of the case _δ_ = 1 using Brownian excursion theory to analyse


A well known application of the Feynman-Kac formula is Kac’s derivation of L´evy’s arcsine law for the distribution of �0 _t_<sup>1(</sup><sup>_Bs>_0)</sup><sup>_ds_for</sup><sup>_B_aBM(R).Kac</sup> also studied the law of �0 _t_<sup>_|Bs|ds_bythesamemethod.SeeBiane-Yor[37]and</sup> [342] for related results. Extensions of the Feynman-Kac formula to more general Markov processes are discussed in [372] [357] [131].

---

[← 12.1.2. The Dirichlet problem](107-12-1-2-the-dirichlet-problem.md) · [Up: contents](index.md) · [12.1.4. The Neumann problem →](109-12-1-4-the-neumann-problem.md)
