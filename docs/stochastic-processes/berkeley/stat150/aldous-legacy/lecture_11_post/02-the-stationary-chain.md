---
title: The stationary chain
source: https://www.stat.berkeley.edu/~aldous/150/lecture_11_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_11_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The stationary chain

**Source:** [`lecture_11_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_11_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider an irreducible positive-recurrent chain – we know it has a unique stationary distribution _π_ . When we start the chain with initial distribution _π_ we call it the **stationary chain** ( _Xt, t_ = 0 _,_ 1 _,_ 2 _, , . . ._ ) and the starting point for all this theory was that, for the stationary chain,


In fact something stronger is true; for each fixed _k_ ,

( _Xt, Xt_ +1 _, . . . , Xt_ + _k_ ) has the same distribution for each _t ≥_ 0 _._

There is a mental picture “watching a movie” of the process; if we start watching at time _t_ , the stationary property is that the statistical properties of what we see do not depend on the starting time _t_ .

There are several interesting features of the stationary chain. Consider


Then [board]


David Aldous Lecture 11


Next, let’s imaging running the movie backwards. That is, fix _N_ , consider the stationary chain ( _Xt,_ 0 _≤ t ≤ N_ ) and then define


So _X_ 0<sup>_∗_hasdistribution</sup><sup>_π_andwecalculate[board]</sup>


By extending this argument we can show that ( _Xt_<sup>_∗,_0</sup><sup>_≤t≤N_)isitselfa</sup> stationary chain with transition matrix **P**<sup>_∗_</sup> , for


In general **P**<sup>_∗_</sup> is different from **P** but it might be the same. We see


and this was the _detailed balance_ condition. Chains with this property are often called **reversible** .

David Aldous Lecture 11

---

[← The circle of 4 results from previous Lectures. Define the return time](01-the-circle-of-4-results-from-previous-lectures-define-the-re.md) · [Up: contents](index.md)
