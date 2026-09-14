---
title: '[From last class]'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_19_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_19_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [From last class]

**Source:** [`lecture_19_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_19_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we have a rate- _λ_ PPP of times of events 0 _< W_ 1 _< W_ 2 _< . . ._ . Suppose that associated with the _i_ ’th event is a R-valued random variable _Yi_ , where ( _Y_ 1 _, Y_ 2 _, . . ._ ) are IID with density _g_ ( _y_ ), independent of ( _Wi_ ). Then we can regard the points ( _W_ 1 _, Y_ 1) _,_ ( _W_ 2 _, Y_ 2) _, . . ._ as a point process on [0 _, ∞_ ) _×_ ( _−∞, ∞_ ).

Theorem ( PK Theorem 5.8)


_The points_ ( _W_ 1 _, Y_ 1) _,_ ( _W_ 2 _, Y_ 2) _, . . . form a Poisson PP with rate λ_ ( _t, y_ ) = _λg_ ( _y_ ) _._


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Question;** what is the distribution of _Z_ = min( _W_ 1 + _Y_ 1 _, W_ 2 + _Y_ 2 _, . . ._ )? **Answer** [board]


[PK] page 370 gives a “crack failure” story for this question.

David Aldous Lecture 19


**Question:** Take a rate- _λ_ PPP on the plane R<sup>2</sup> . For each point of the PPP, draw a circle of radius _R_ , where _R >_ 0 is random with density function _f_ ( _r_ ), independent for different points. What is the distribution of _Q_ = number of circles covering the origin? **Answer** [board] _Q_ has Poisson distribution with mean _λ_ �0 _∞ πr_<sup>2</sup> _f_ ( _r_ ) _dr_ . This is [PK] problem 5.5.7.

David Aldous Lecture 19

---

[← Today’s topics](01-today-s-topics.md) · [Up: contents](index.md) · [Some models of coincidences. →](03-some-models-of-coincidences.md)
