---
title: 'Example: Wright-Fisher model with mutation'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_38_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example: Wright-Fisher model with mutation

**Source:** [`lecture_38_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- _k_ genes per generation


each gene is allele A or allele B


each gene is a copy of a uniform random gene from the previous generation, except that . . .


A mutates to B with probability _α/k_

B mutates to A with probability _β/k_ Write _Xn_<sup>(</sup><sup>_k_)</sup> for number of A alleles in generation _n_ .

We want to rescale the process by considering the **proportion** of genes that are A, and to take 1 generation as a time interval _δ_ in “rescaled time units” – _δ_ depends on _k_ and we will calculate later what it is. So the rescaled process is

_Yn_<sup>(</sup> _δ_<sup>_k_)=</sup><sup>_k−_1</sup><sup>_X_</sup> _n_<sup>(</sup><sup>_k_)</sup><sup>_._</sup>

David Aldous

Lecture 38


To find the diffusion which is the rescaled limit (as _k →∞_ ), what we need to do is to calculate (to first order) the change in mean and variance in one step (generation, in this example) of the discrete process, then rescale.

In this example we have [board]


Restating this in terms of _Y_ = _X /k_ we see [board]


where we have chosen _δ_ = 1 _/k_ . This says that the process ( _Yt_<sup>(</sup><sup>_k_)</sup> ) is approximately the diffusion with


whose state space is [0 _,_ 1].

David Aldous Lecture 38

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Ehrenfest urn model. →](03-ehrenfest-urn-model.md)
