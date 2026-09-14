---
title: Lecture 18 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_18_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_18_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 18 — post

**Source:** [`lecture_18_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_18_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 18


David Aldous

9 October 2015

David Aldous

Lecture 18


Lemma


_If_ ( _ξi_ ) _are the points of a rate-_ 1 _PPP on_ [0 _, ∞_ ) _and if G_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) _is continuous, strictly increasing, with g_ ( _x_ ) =<sup>_<u>dG</u>_</sup> _dx and G_ (0) = 0 _, then the points_ ( _G_ ( _ξi_ )) _form another a PPP on_ [0 _, ∞_ ) _with rate λ_ ( _y_ ) = 1 _/g_ ( _G_<sup>_−_1</sup> ( _y_ )) _._


This allows us to construct (mathematically) the PPP with rate function _λ_ ( _t_ ) by solving (for _G_ ) the equation


More usefully, because we know how to simulate the rate-1 PPP on [0 _, ∞_ ) (inter-event times are IID Exponential(1)) this enables us to **simulate** the PPP with rate function _λ_ ( _t_ ). As an example, consider _G_ ( _x_ ) = _ax_<sup>1</sup><sup>_/_2</sup> . Then [board] _λ_ ( _y_ ) = 2 _y /a_<sup>2</sup> . Recall that the distances _D_ 1 _, D_ 2 _, D_ 3 _. . ._ to the origin in a 2-dimensional rate _−λ_ PPP are the points of a PPP on [0 _, ∞_ ) with rate function _λ_ ( _r_ ) = 2 _πλr_ . So we can simulate _D_ 1 _, D_ 2 _, D_ 3 _. . ._ using _G_ ( _x_ ) = _ax_<sup>1</sup><sup>_/_2</sup> with _a_ = ( _πλ_ )<sup>_−_1</sup><sup>_/_2</sup> .

David Aldous Lecture 18


[from earlier class, for constant-rate PPP on [0 _, ∞_ )]

Theorem


_Fix t >_ 0 _and k ≥_ 1 _. Conditional on {N_ ( _t_ ) = _k} the times_ ( _W_ 1 _, W_ 2 _, . . . , Wk_ ) _of events in the PPP are distributed as the order statistics of k IID Uniform_ (0 _, t_ ) _random variables._


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

The analogous result holds in two dimensions.

Theorem


_Let B ⊂_ R<sup>2</sup> _be a region with finite area. Then the rate-λ PPP on B can be constructed as follows._

- _(i) Take N_ ( _B_ ) _with Poisson(λ ×_ area( _B_ ) _) distribution. (ii) Given N_ ( _B_ ) = _n, take n random points independent uniform on B._


David Aldous

Lecture 18


**Question:** How could we simulate a rate- _λ_ PPP on some region _B_ in R<sup>2</sup> . Not obvious how to simulate, but using theory we see two ways. (1) If _B_ is a square then we could use Theorem above. Easy to sample uniformly from square in (x,y)- coordinates.

(2) If _B_ is a disc then we know how to simulate the radial distances _D_ 1 _, D_ 2 _, D_ 3 _, . . ._ . So use polar coordinates ( _Di , θi_ ); intuitively clear the _θi_ are IID uniform on (0 _,_ 2 _π_ ).

David Aldous Lecture 18


**Spatial PPP with varying rate** _λ_ ( _x, y_ ) **.** _N_ ( _A_ ) has Poisson(� _A_<sup>_λ_(</sup><sup>_x, y_)</sup><sup>_dxdy_)distribution.</sup> P( some point in [ _x, x_ + _dx_ ) _×_ [ _y , y_ + _dy_ ] ) = _λ_ ( _x, y_ ) _dxdy_ . For disjoint _A_ 1 _, A_ 2 _, . . ._ the random variables _N_ ( _Ai_ ) are independent. An interesting use of this idea is to combine time with space, as follows. Suppose we have a rate- _λ_ PPP of times of events 0 _< W_ 1 _< W_ 2 _< . . ._ . Suppose that associated with the _i_ ’th event is a R-valued random variable _Yi_ , where ( _Y_ 1 _, Y_ 2 _, . . ._ ) are IID with density _g_ ( _y_ ), independent of ( _Wi_ ). Then we can regard the points ( _W_ 1 _, Y_ 1) _,_ ( _W_ 2 _, Y_ 2) _, . . ._ as a point process on [0 _, ∞_ ) _×_ ( _−∞, ∞_ ).

Theorem ( PK Theorem 5.8)


_The points_ ( _W_ 1 _, Y_ 1) _,_ ( _W_ 2 _, Y_ 2) _, . . . form a Poisson PP with rate λ_ ( _t, y_ ) = _λg_ ( _y_ ) _._


David Aldous Lecture 18


# **[KP] Exercise 5.6.10.**


You want to sell at item before time 1.


Bids arrive at times of a rate-1 PPP; you must accept/reject bis at that time.


Bid amounts _U_ 1 _, U_ 2 _, . . ._ are IID Uniform [0 _,_ 1].

What is a good strategy?

**Strategy A;** Fix a price _θ_ and accept first bid over _θ_ . Analysis [board]:


Intuition suggests it would be better to use a decreasing threshold for accepting a bid.

David Aldous Lecture 18


**Strategy B;** Accept the first bid which (at time _t_ ) is larger than _θ_ ( _t_ ) =<sup><u>1</u></sup> 3<sup>_−_</sup> _−_<sup>_<u>t</u>_</sup> _t_<sup>.</sup> [details on board: outline here].

(a) Points ( _Ti , Ui_ ) are PPP on [0 _,_ 1] _×_ [0 _,_ 1] of rate _λ_ ( _t, u_ ) = _λgU_ ( _u_ ) = 1.

(b) Consider

_g_ ( _t, u_ ) _dtdu_ = P( bid offered and accepted in [ _t, t_ + _dt_ ] _×_ [ _u, u_ + _du_ ]). After a calculation, _g_ ( _t, u_ ) = (1 _−_ 3<sup>_<u>t</u>_)2.</sup>

(c)

E( price received) = _u g_ ( _t, u_ ) _dtdu._ �� _D_ 1

David Aldous Lecture 18

---

[Up: contents](index.md)
