---
title: Unit 11 — optim Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 11 — optim Part 05 —

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7

##### **uphill to local maximum, gradient view**


<!-- Start of picture text -->
1<br>34567891<br>2<br>f'(x)<br>0 1 2 3 4 5 6<br>x<br>nearly diverges, gradient view<br>31<br>567891<br>4<br>2 f'(x)<br>0 1 2 3 4 5 6<br>x<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br><!-- End of picture text -->

**uphill to local maximum, function view**


<!-- Start of picture text -->
345678912<br>1<br>f(x)<br>0 1 2 3 4 5 6<br>x<br>1.0<br>0.5<br>f(x) 0.0<br>−1.0<br><!-- End of picture text -->

**nearly diverges, function view**


<!-- Start of picture text -->
2 1<br>3<br>4 567891 f(x)<br>0 1 2 3 4 5 6<br>1.0<br>0.5<br>f(x) 0.0<br>−1.0<br><!-- End of picture text -->


<!-- Start of picture text -->
x<br><!-- End of picture text -->

**better starting point, gradient view**


<!-- Start of picture text -->
1<br>2 34567891<br>f'(x)<br>0 1 2 3 4 5 6<br>x<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br><!-- End of picture text -->

**better starting point, function view**


<!-- Start of picture text -->
1 f(x)<br>234567891<br>0 1 2 3 4 5 6<br>x<br>1.0<br>0.5<br>f(x) 0.0<br>−1.0<br><!-- End of picture text -->

One nice, general idea is to use a fast method such as Newton’s method _safeguarded_ by a robust, but slower method. Here’s how one can do this for N-R, safeguarding with a bracketing method such as bisection. Basically, we check the N-R proposed move to see if N-R is proposing a step outside of where the root is known to lie based on the previous steps and the gradient values for those steps. If so, we could choose the next step based on bisection.

Another approach is backtracking. If a new value is proposed that yields a larger value of the function, backtrack to find a value that reduces the function. One possibility is a line search but given that we’re trying to reduce computation, a full line search is often unwise computationally (also in the multivariate Newton’s method, we are in the middle of an iterative algorithm for which

8

we will just be going off in another direction anyway at the next iteration). A basic approach is to keep backtracking in halves. A nice alternative is to fit a polynomial to the known information about that slice of the function, namely _f_ ( _xt_ +1), _f_ ( _xt_ ), _f_<sup>_′_</sup> ( _xt_ ) and _f_<sup>_′′_</sup> ( _xt_ ) and find the minimum of the polynomial approximation.

---

[← 3 Univariate function optimization](04-3-univariate-function-optimization.md) · [Up: contents](index.md) · [4 Convergence ideas →](06-4-convergence-ideas.md)
