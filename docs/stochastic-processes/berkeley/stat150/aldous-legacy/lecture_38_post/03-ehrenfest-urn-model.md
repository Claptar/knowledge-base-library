---
title: Ehrenfest urn model.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_38_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ehrenfest urn model.

**Source:** [`lecture_38_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- 2 _k_ balls, two boxes.

Pick uniform random ball, more to other box. Study _Xn_<sup>(</sup><sup>_k_)</sup> = number of balls in left box after _n_ steps. We know the stationary distribution is Binomial(2 _k,_ 1 _/_ 2). Rescale by defining _Yn_<sup>(</sup> _δ_<sup>_k_)= (</sup><sup>_X_</sup> _n_<sup>(</sup><sup>_k_)</sup> _− k_ ) _/√k_

for _δ_ to be calculated later.

To find the diffusion which is the rescaled limit, what we need to do is to calculate (to first order) the change in mean and variance in one step of the discrete process, then rescale.

David Aldous Lecture 38


and then rescaling give [board]


for _δ_ = 1 _/k_ . This says that the process ( _Yt_<sup>(</sup><sup>_k_)</sup> ) is approximately the diffusion with _µ_ ( _y_ ) = _−y , σ_<sup>2</sup> ( _y_ ) = 1

whose state space is ( _−∞, ∞_ ). This is the **Ornstein-Uhlenbeck process** .

David Aldous Lecture 38


Here is the first interesting piece of “theory” for diffusions. Let ( _Yt_ ) be the diffusion with given drift and variance rate functions _µ_ ( _y_ ) _, σ_<sup>2</sup> ( _y_ ). Let _f_ be a smooth strictly increasing function R _→_ R. Then _Xt_ = _f_ ( _Yt_ ) is also a diffusion, and we can calculate its functions


where _x_ = _f_ ( _y_ ) _, y_ = _f_<sup>_−_1</sup> ( _x_ ). This allows us to use martingale arguments to calculate hitting probabilities. [board]

David Aldous Lecture 38

---

[← Example: Wright-Fisher model with mutation](02-example-wright-fisher-model-with-mutation.md) · [Up: contents](index.md)
