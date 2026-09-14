---
title: 6.4. Quadratic functionals
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6.4. Quadratic functionals

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

By a _quadratic Brownian functional_ , we mean primarily a functional of the form


for some positive measure _µ_ ( _ds_ ) on R+. But it is also of interest to consider the more general functionals

for _µ_ and _f_ such that


In terms of the Wiener chaos decomposition (63), these functionals belong to _C_ 0 � _C_ 2. So in full generality, we use the term _quadratic Brownian functional_ to mean any functional of the form


with _c ∈_ R and �0 _∞ ds_ �0 _s_<sup>_duφ_2(</sup><sup>_s, u_)</sup><sup>_<∞_.Wenotethat,withthehelpof</sup> Kahunen-Lo´eve expansions, the laws of such functionals may be decribed via their characteristic functions. These may be expanded as infinite products, which can sometimes be evaluated explicitly in terms of hyperbolic functions or other special functions. See e.g. Neveu [322] Hitsuda [170]. Perhaps the most famous example is L´evy’s stochastic area formula


where _X_ and _Y_ are two independent standard BMs. See L´evy[270] Gaveau [149] Berthuet [22] Biane-Yor [38] for many variations of this formula, some of which are reviewed in Yor [453].

A number of noteworthy identities in law between quadratic Brownian functionals are consequences of the following elementary observation:


for _f ∈ L_<sup>2</sup> (R<sup>2</sup> +<sup>;</sup><sup>_ds dt_).Consequencesofthisobservationincludethefollowing</sup> identity, which was discovered by chemists studying the radius of gyration of random polymers


_J. Pitman and M. Yor/Guide to Brownian motion_

45

where the left side involves centering at mean value of the Brownian path on [0 _,_ 1], while the right side involves a Brownian bridge. The right side is known in empirical process theory to describe the asymptotic distribution of the von Mises statistic [391]. More generally Yor [452] explains how the Cieselski-Taylor identities, which relate the laws of occupation times and hitting times of Brownian motion in various dimensions, may be understood in terms of such identities in law between two quadratic Brownian functionals. See also [451] and [290, Ch. 4].

---

[← 6.3. Additive functionals](65-6-3-additive-functionals.md) · [Up: contents](index.md) · [6.5. Exponential functionals →](67-6-5-exponential-functionals.md)
