---
title: Unit 11 — optim Part 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 11 — optim Part 08 —

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

x0 <- 2.5 _# good starting point_ **fp** (x0) ## [1] -0.5984721 **fpp** (x0) ## [1] 0.8011436 x1 <- x0 - **fp** (x0)/ **fpp** (x0) xvals <- **c** (x0, **rep** (NA,9)) **for** (t **in** 2:10){ xvals[t]=xvals[t-1]- **fp** (xvals[t-1])/ **fpp** (xvals[t-1]) } xvals ## [1] 2.500000 3.247022 3.141200 3.141593 3.141593 3.141593 3.141593 ## [8] 3.141593 3.141593 3.141593 _## converges quickly_ **plot** (xs, **f** (xs), type = 'l', xlab = 'x', ylab = "f'(x)", lwd = 2, main = 'converges to minimum, better starting point') **lines** (xs, **fp** (xs)) **lines** (xs, **fpp** (xs), lty = 2) **legend** ('bottomright', lty = **c** (1,1,2), lwd = **c** (2, 1, 1), legend = **c** ("f(x)", "f'(x)", 'f"(x)'), bty = 'n') **points** (xvals, **fp** (xvals), pch = **as.character** (1: **length** (xvals)), col = 'red')

10


<!-- Start of picture text -->
uphill to local maximum<br>45678913<br>f(x)<br>f'(x)<br>1 f"(x)<br>0 1 2 3 4 5 6<br>x<br>converges to minimum, nearly diverges<br>2<br>4<br>567891<br>f(x)<br>3 f'(x)<br>1 f"(x)<br>0 1 2 3 4 5 6<br>x<br>converges to minimum, better starting point<br>2<br>34567891<br>f(x)<br>1 f'(x)<br>f"(x)<br>0 1 2 3 4 5 6<br>x<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br>1.0<br>0.5<br>f'(x) 0.0<br>−1.0<br><!-- End of picture text -->

One nice, general idea is to use a fast method such as Newton’s method _safeguarded_ by a robust, but slower method. Here’s how one can do this for N-R, safeguarding with a bracketing method such as bisection. Basically, we check the N-R proposed move to see if N-R is proposing a step outside of where the root is known to lie based on the previous steps and the gradient values for those steps. If so, we could choose the next step based on bisection.

Another approach is backtracking. If a new value is proposed that yields a larger value of the function, backtrack to find a value that reduces the function. One possibility is a line search but given that we’re trying to reduce computation, a full line search is often unwise computationally

11

(also in the multivariate Newton’s method, we are in the middle of an iterative algorithm for which we will just be going off in another direction anyway at the next iteration). A basic approach is to keep backtracking in halves. A nice alternative is to fit a polynomial to the known information about that slice of the function, namely _f_ ( _xt_ +1), _f_ ( _xt_ ), _f_<sup>_′_</sup> ( _xt_ ) and _f_<sup>_′′_</sup> ( _xt_ ) and find the minimum of the polynomial approximation.

---

[← Unit 11 — optim Part 07 —](07-unit-11-optim-part-07.md) · [Up: contents](index.md) · [4 Convergence ideas →](09-4-convergence-ideas.md)
