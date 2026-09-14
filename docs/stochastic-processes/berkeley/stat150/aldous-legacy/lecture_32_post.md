---
title: Lecture 32 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_32_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_32_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 32 — post

**Source:** [`lecture_32_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_32_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 32


David Aldous

16 November 2015

David Aldous

Lecture 32


A family of RVs ( _G_ ( _t_ )) is called **Gaussian** or a **Gaussian process** if the joint distribution of any finite set of these RVs is multivariate Normal. From STAT134 facts about multivariate Normal distributions we can read off facts about Gaussian processes.


If a process is known to be Gaussian, then its distribution is determined by its mean/covariance structure, that is by the functions E _G_ ( _t_ ) and c _ov_ ( _G_ ( _s_ ) _, G_ ( _t_ )).


A RV defined as a linear combination _X_ =<sup>�</sup> _i_<sup>_aiG_(</sup><sup>_ti_)or</sup> _X_ = � _a_ ( _t_ ) _G_ ( _t_ ) _dt_ has Normal distribution, and including _X_ in the original family ( _G_ ( _t_ )) preserves the Gaussian property. Within a Gaussian family, if one RV is uncorrelated with a subfamily, then it is independent of that subfamily.

Standard BM ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is the Gaussian process with [board]

E _B_ ( _t_ ) = 0; E[ _B_ ( _s_ ) _B_ ( _t_ )] = min( _s, t_ ) _._

David Aldous Lecture 32


The **Brownian bridge** process ( _B_<sup>_o_</sup> ( _t_ ) _,_ 0 _≤ t ≤_ 1) is defined to have the (*) conditional distribution of standard BM over [0 _,_ 1] given _B_ (1) = 0. We can construct (mathematically) this process by a trick. Define ( _∗∗_ ) _B_<sup>_o_</sup> ( _t_ ) = _B_ ( _t_ ) _− tB_ (1) _,_ 0 _≤ t ≤_ 1 _._

Working with this definition we see [board] ( _B_<sup>_o_</sup> ( _t_ )) is a Gaussian process; _B_<sup>_o_</sup> (0) = _B_<sup>_o_</sup> (1) = 0. E _B_<sup>_o_</sup> ( _t_ ) = 0.


E[ _B_<sup>_o_</sup> ( _s_ ) _B_<sup>_o_</sup> ( _t_ )] = _s_ (1 _− t_ ) _,_ 0 _≤ s ≤ t ≤_ 1. E[ _B_<sup>_o_</sup> ( _t_ ) _B_ (1)] = 0.

The final point implies that ( _B_<sup>_o_</sup> ( _t_ ) _,_ 0 _≤ t ≤_ 1) is independent of _B_ (1). So the unconditional distribution of ( _B_<sup>_o_</sup> ( _t_ ) _,_ 0 _≤ t ≤_ 1) is the same as its conditional distribution given _B_ (1) = 0, and then construction (**) fits the original description (*).

David Aldous

Lecture 32


This had two interesting consequences.


The first identity here tell us that for Brownian bridge


has distribution


David Aldous Lecture 32


Brownian bridge arises in Statistics as the scaling limit of empirical distributions.

[board and [PK] sec 8.3.3]

David Aldous Lecture 32


**Example.** What is the distribution of _V_ = �01<sup>_a_(</sup><sup>_t_)</sup><sup>_Bo_(</sup><sup>_t_)</sup><sup>_dt_?</sup>

We know _V_ has Normal, mean 0, distribution: what is the variance? The “trick” is to write _V_<sup>2</sup> as

so then


Note: this is not “stochastic integration” (stochastic calculus) but is just ordinary calculus.

David Aldous Lecture 32


Somewhat analogous to Brownian bridge, we define **Brownian meander** ( _B_<sup>+</sup> ( _t_ ) _,_ 0 _≤ t ≤_ 1) be the BM ( _B_ ( _t_ ) _,_ 0 _≤ t ≤_ 1) conditioned on ( _B_ ( _t_ ) _≥_ 0 _,_ 0 _≤ t ≤_ 1). This is harder to study explicitly, but the second formula in the Proposition tells us

P( _B_<sup>+</sup> (1) _> b_ ) = exp( _−b_<sup>2</sup> _/_ 2) _, b >_ 0 _._

David Aldous Lecture 32

---

[Up: contents](index.md)
