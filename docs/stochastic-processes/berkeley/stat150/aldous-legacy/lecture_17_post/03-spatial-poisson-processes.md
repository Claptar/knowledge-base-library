---
title: Spatial Poisson processes
source: https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_17_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spatial Poisson processes

**Source:** [`lecture_17_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have been imagining the line [0 _, ∞_ ) as “time”, but the mathematics is the same for 1-dimensional space – for instance, positions of accidents along a highway.

More interesting to consider random points in 2-dimensional space. Here the rate _λ_ will be the mean number of points per unit area. Write _N_ ( _A_ ) for the number of points in a region _A_ . The rate- _λ_ PPP on R<sup>2</sup> is defined by the properties

_N_ ( _A_ ) has Poisson( _λ ×_ area( _A_ )) distribution. For disjoint _A_ 1 _, A_ 2 _, . . ._ the random variables _N_ ( _Ai_ ) are independent. This is used as a model of “purely random” points.

David Aldous Lecture 17


In a rate- _λ_ PPP on R<sup>2</sup> , let _Dk_ be the distance from the origin to the _k_ ’th closest point.

Here are some results about this [board]. _D_ 1 has density _fD_ 1 ( _x_ ) = 2 _πλx_ exp( _−πλx_<sup>2</sup> ). _D_ 1 _, D_ 2 _, D_ 3 _. . ._ are the points of a PPP on [0 _, ∞_ ) with rate function _λ_ ( _r_ ) = 2 _πλr_ .

David Aldous Lecture 17


**The PPP with rate function** _λ_ ( _t_ ) **.**

Start with the informal description in terms of infinitesimal intervals: (a’) P( event during [ _t, t_ + _dt_ ]) = _λ_ ( _t_ ) _dt_ (b’) What happens in disjoint time intervals is independent.

We can then deduce the other description. Write Λ( _t_ ) = �0 _t_<sup>_λ_(</sup><sup>_u_)</sup><sup>_du_.</sup>

(a) _N_ ( _s, t_ ) has Poisson(Λ( _t_ ) _−_ Λ( _s_ )) distribution. (b) For disjoint intervals ( _s_ 1 _, t_ 1) _,_ ( _s_ 2 _, t_ 2) _, . . . ,_ ( _sk , tk_ ) the random variables _N_ ( _s_ 1 _, t_ 1) _, N_ ( _s_ 2 _, t_ 2) _, . . . , N_ ( _sk , tk_ ) are independent.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

We can explain this via a general result and then a special result. [board]

## Lemma


_If_ ( _ξi_ ) _are the points of a PPP (in time or space, and maybe varying rate) then for any function G the points_ ( _G_ ( _ξi_ )) _form another PPP (typically with varying rate)._


## Lemma


_If_ ( _ξi_ ) _are the points of a rate-_ 1 _PPP on_ [0 _, ∞_ ) _and if G_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) _is continuous, strictly increasing, with g_ ( _x_ ) =<sup>_<u>dG</u>_</sup> _dx_<sup>_andG_(0) = 0</sup><sup>_,thenthepoints_</sup> ( _G_ ( _ξi_ )) _form another a PPP on_ [0 _, ∞_ ) _with rate λ_ ( _y_ ) = 1 _/g_ ( _G_<sup>_−_1</sup> ( _y_ )) _._


David Aldous Lecture 17

---

[← Theorem](02-theorem.md) · [Up: contents](index.md)
