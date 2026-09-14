---
title: Theorem
source: https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_17_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Theorem

**Source:** [`lecture_17_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Given two independent PPPs with rates λ_ 1 _and λ_ 2 _, the combined process – that is the process with N_ ( _t_ ) = _N_ 1( _t_ ) + _N_ 2( _t_ ) _– is a PPP with rate λ_ 1 + _λ_ 2 _._


Theorem


_Let p_ 1 _, p_ 2 _, . . . be a probability distribution on “colors”_ 1 _,_ 2 _,_ 3 _, . . .. Take a rate-λ PPP, and assign colors to the points, each point independently getting color i with probability pi . Then (i) For each i the process of color-i points is a PPP with rate λpi . (ii) These processes are independent as i varies._


For instance, if we model times of “accidents” as a rate- _λ_ PPP, and then model each accident as “serious” with probability _p_ and “not serious” with probability 1 _− p_ , then

- serious accidents occur as a PPP of rate _λp_

- non-serious accidents occur as a PPP of rate _λ_ (1 _− p_ )

_•_ the two processes are independent. “Independence” here looks intuitively wrong but arises from the assumption that _λ_ is known.

David Aldous Lecture 17

---

[← Ideas from previous lecture.](01-ideas-from-previous-lecture.md) · [Up: contents](index.md) · [Spatial Poisson processes →](03-spatial-poisson-processes.md)
