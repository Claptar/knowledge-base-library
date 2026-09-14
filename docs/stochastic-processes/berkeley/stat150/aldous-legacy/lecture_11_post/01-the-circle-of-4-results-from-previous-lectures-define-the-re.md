---
title: The circle of 4 results from previous Lectures. Define the return time
source: https://www.stat.berkeley.edu/~aldous/150/lecture_11_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_11_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The circle of 4 results from previous Lectures. Define the return time

**Source:** [`lecture_11_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_11_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Fix a reference state _b_ .


David Aldous Lecture 11


Theorem _If the chain is irreducible, positive-recurrent and aperiodic, then for any initial distribution_ P( _X_ ( _t_ ) = _j_ ) _→ πj as t →∞ where π is the unique stationary distribution._


Theorem _Write t−_ 1 _Ni_ ( _t_ ) = � 11( _X_ ( _s_ )= _i_ ) = _number of visits to i before t. s_ =0 _If the chain is irreducible and positive-recurrent, then for any initial distribution t_<sup>_−_1</sup> _Ni_ ( _t_ ) _→ πi a.s. as t →∞._ Note this implies but is stronger than previous fact E[ _t_<sup>_−_1</sup> _Ni_ ( _t_ )] _→ πi_ as _t →∞._


David Aldous Lecture 11


A final result is rather subtle. Note we only need this when the state space is infinite.

Proposition


_If irreducible, if there exists a probability distribution π satisfying π_ = _π_ **P** _, then the chain is positive-recurrent._


Then we can apply previous theorems and this _π_ is the unique stationary distribution.

See texts for proofs. I want to focus on what these results say, in our specific examples.

David Aldous

Lecture 11


An important setting where we can do explicit calculations is **birth-and-death chains** (note [PK] calls these “general random walk”.) Here the state space is either _{_ 0 _,_ 1 _, . . . , N}_ or _{_ 0 _,_ 1 _,_ 2 _, . . .}_ and the transitions are of the form


when _i_ is not an endpoint of the state space. There are two different cases for endpoints.

In the **absorbing** case we set _p_ 00 = 1, and (finite case) _pNN_ = 1. In the **reflecting** case we set _p_ 01 = _p_ 0 _>_ 0 _, p_ 00 = 1 _− p_ 0, and (finite case) _pN,N−_ 1 = _qN >_ 0 _, pN,N_ = 1 _− qN_ .

We first consider the reflecting case. Here the chain is irreducible. So by our Theorems, in the finite case the chain has a stationary distribution. We can calculate the stationary distribution by solving the detailed balance equations.

[board]

David Aldous

Lecture 11


**Conclusion** . Define _w_ 0 = 1 and


If _w < ∞_ , which is certain in the finite case, then the chain is positive-recurrent and the stationary distribution is


Note we used the final Proposition in the infinite case. If _w_ = _∞_ one can show [outline on board] the chain is not positive-recurrent.

A simple special case is where _pi_ = _p, qi_ = 1 _− p_ for all _i_ . Here _wi_ = ( _p/_ 1 _− p_ )<sup>_i_</sup> . So for _p <_ 1 _/_ 2, we see _π_ is the shifted Geometric( _θ_ ) distribution for _θ_ = 1 _−_ _<u>p</u>_ 1 _−p_<sup>.</sup>

David Aldous

Lecture 11


Now consider the absorbing case. This is [PK] Problem 3.6.1 with slightly different setup. [board] **Conclusion.** for 0 _≤ i ≤ N_ , _j−_ 1 _<u>qk</u>_ P _i_ ( _TN < T_ 0) =<sup>_D_</sup><sup><u>(</u></sup><sup>_i_</sup><sup><u>)</u></sup> _D_ ( _i_ ) = � _i_ � _. D_ ( _N_ )<sup>_,_</sup> _j_ =1 _k_ =1 _pk_

One can also calculate, in a similar way, a formula for the mean time E _i_ min( _T_ 0 _, TN_ ) – see [KP].

David Aldous Lecture 11

---

[Up: contents](index.md) · [The stationary chain →](02-the-stationary-chain.md)
