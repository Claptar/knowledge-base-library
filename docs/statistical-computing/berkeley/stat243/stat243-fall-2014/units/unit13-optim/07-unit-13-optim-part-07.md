---
title: Unit 13 — optim Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit13-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — optim Part 07 —

**Source:** [`units/unit13-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**points** (xvals, **fp** (xvals), pch = **as.character** (1: **length** (xvals)), col = 'red')


<!-- Start of picture text -->
3<br>1<br>1<br>3<br>4 567891 234567891<br>1<br>2<br>2<br>−15 −5 0 5 10 15 0 1 2 3 4 5 6<br>xs xs<br>1.0<br>0.4<br>0.5<br>0.2<br>0.0 0.0<br>f(xs)<br>fp(xs)<br>−0.5<br>−0.4<br>−1.0<br><!-- End of picture text -->

_<mark># and we've found a maximum rather than a minimum...</mark>_

One nice, general idea is to use a fast method such as Newton’s method _safeguarded_ by a robust, but slower method. Here’s how one can do this for N-R, safeguarding with a bracketing method such as bisection. Basically, we check the N-R proposed move to see if N-R is proposing

8

a step outside of where the root is known to lie based on the previous steps and the gradient values for those steps. If so, we could choose the next step based on bisection.

Another approach is backtracking. If a new value is proposed that yields a larger value of the function, backtrack to find a value that reduces the function. One possibility is a line search but given that we’re trying to reduce computation, a full line search is often unwise computationally (also in the multivariate Newton’s method, we are in the middle of an iterative algorithm for which we will just be going off in another direction anyway at the next iteration). A basic approach is to keep backtracking in halves. A nice alternative is to fit a polynomial to the known information about that slice of the function, namely _f_ ( _xt_ +1), _f_ ( _xt_ ), _f_<sup>_′_</sup> ( _xt_ ) and _f_<sup>_′′_</sup> ( _xt_ ) and find the minimum of the polynomial approximation.

---

[← Unit 13 — optim Part 06 —](06-unit-13-optim-part-06.md) · [Up: contents](index.md) · [4 Convergence ideas →](08-4-convergence-ideas.md)
