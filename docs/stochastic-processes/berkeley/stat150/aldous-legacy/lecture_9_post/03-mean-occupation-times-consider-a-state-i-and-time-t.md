---
title: Mean occupation times. Consider a state i and time t .
source: https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_9_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mean occupation times. Consider a state i and time t .

**Source:** [`lecture_9_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_t−_ 1 � 11( _X_ ( _s_ )= _i_ ) = number of visits to _i_ before _t s_ =0 _t−_ 1 <u>1</u> _t_ � 11( _X_ ( _s_ )= _i_ ) = proportion of time at _i_ before _t s_ =0 _t−_ 1 E[<sup><u>1</u></sup> _t_ � 11( _X_ ( _s_ )= _i_ )] = mean proportion of time at _i_ before _t s_ =0 _t−_ 1 =<sup><u>1</u></sup> _t_ � P( _X_ ( _s_ ) = _i_ ) _. s_ =0

From algebra/calculus, if _a_ ( _t_ ) _→ a_ ( _∞_ ) then<sup><u>1</u></sup> _t_ � _ts−_ =01<sup>_a_(</sup><sup>_s_)</sup><sup>_→a_(</sup><sup>_∞_).</sup> **Conclusion. For a Markov chain, if** _µ_ ( _t_ ) _→ π_ **then** (mean proportion of time at _i_ before _t_ ) _→ πi ._

David Aldous Lecture 9


We can extend this idea by imagining **costs** _c_ ( _i_ ) (or gains). That is, suppose spending unit time in state _i_ incurs a cost _c_ ( _i_ ). Then, by summing over all states _i_ .


In our earlier context of setting up first-step analysis of hitting times E _i TA_ , we can also consider the mean total cost up to time _TA_ – see [PK] sec. 3.4.2.

David Aldous Lecture 9


We now come to the central part of theory for Markov chains. Everyone says this theory in slightly different ways. See [PK] section 4.4; also a concise theory treatment with proofs is in [BZ] sections 5.3 - 5.4. Assume irreducible; state space may be finite or countable infinite.

David Aldous

Lecture 9


Recall _Ti_ = min _{t ≥_ 0 : _Xt_ = _i}_ and define also the **return time**


Fix a reference state _b_ .

Theorem _Suppose irreducible. (a) If state space is finite then_ E _bTb_<sup>+</sup><sup>_< ∞._</sup> _(b) Suppose_ E _bTb_<sup>+</sup><sup>_< ∞.Define_</sup> _Tb_<sup>+</sup> _a_ ( _b, i_ ) = E _b_ � **1** ( _X_ ( _s_ )= _i_ ) _s_ =1 = _mean number of visits to i before returning to b. So a_ ( _b, b_ ) = 1 _. Then πi_ =<sup>_a_</sup><sup><u>(</u></sup><sup>_b, i_</sup><sup><u>)</u></sup> E _bTb_<sup>+</sup>


_is a stationary distribution, and is the_ **only** _stationary distribution._


David Aldous Lecture 9

---

[← Stationary distributions](02-stationary-distributions.md) · [Up: contents](index.md) · [Discussion. →](04-discussion.md)
