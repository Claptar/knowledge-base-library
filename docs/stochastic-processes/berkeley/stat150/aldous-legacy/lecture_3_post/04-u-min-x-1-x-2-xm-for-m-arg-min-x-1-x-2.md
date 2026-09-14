---
title: U = min( X 1 , X 2) = XM for M = arg min( X 1 , X 2)
source: https://www.stat.berkeley.edu/~aldous/150/lecture_3_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_3_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# U = min( X 1 , X 2) = XM for M = arg min( X 1 , X 2)

**Source:** [`lecture_3_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_3_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

We showed


So similarly


and by summing


These formulas imply that _U_ = min( _X_ 1 _, X_ 2) has Exponential( _λ_ 1 + _λ_ 2) distribution and is **independent** of _M_ = arg min( _X_ 1 _, X_ 2).

David Aldous Lecture 3


At the end we used a conceptual fact. Given two random variables _Y , Z_ – say _Y_ discrete and _Z_ continuous, we know and often use the product formula:

if _Y_ and _Z_ independent then ( _∗_ ) P( _Z < z, Y_ = _y_ ) = P( _Z < z_ ) _×_ P( _Y_ = _y_ ) _._

The converse is also true: if (*) holds for all _z, y_ then _Y_ and _Z_ are independent.

David Aldous

Lecture 3


Recall how we find the distributions of minima/maxima. The event _{_ min( _X_ 1 _, X_ 2) _> x}_ is the event _{X_ 1 _> x, X_ 2 _> x}_ , so in this example P(min( _X_ 1 _, X_ 2) _> x_ ) = P( _X_ 1 _> x_ ) _×_ P( _X_ 2 _> x_ ) = exp( _−_ ( _λ_ 1 + _λ_ 2) _x_ )

which repeats the fact that min( _X_ 1 _, X_ 2) has Exponential( _λ_ 1 + _λ_ 2) distribution. The same argument for maxima tells us P(max( _X_ 1 _, X_ 2) _≤ x_ ) = P( _X_ 1 _≤ x_ ) _×_ P( _X_ 2 _≤ x_ ) = (1 _− e_<sup>_−λ_1</sup><sup>_x_</sup> ) (1 _− e_<sup>_−λ_2</sup><sup>_x_</sup> )

and so max( _X_ 1 _, X_ 2) has density function _λ_ 1 _e_<sup>_−λ_1</sup><sup>_x_</sup> + _λ_ 1 _e_<sup>_−λ_2</sup><sup>_x_</sup> _−_ ( _λ_ 1 + _λ_ 2) _e_<sup>_−_(</sup><sup>_λ_1+</sup><sup>_λ_2)</sup><sup>_x_</sup> _._

David Aldous

Lecture 3

---

[← Use general formula](03-use-general-formula.md) · [Up: contents](index.md) · [Review of conditioning. →](05-review-of-conditioning.md)
