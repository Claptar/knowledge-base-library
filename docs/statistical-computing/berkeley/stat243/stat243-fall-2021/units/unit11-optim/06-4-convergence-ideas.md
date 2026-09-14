---
title: 4 Convergence ideas
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Convergence ideas

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Convergence metrics**

We might choose to assess whether _f_<sup>_′_</sup> ( _xt_ ) is near zero, which should assure that we have reached the critical point. However, in parts of the domain where _f_ ( _x_ ) is fairly flat, we may find the derivative is near zero even though we are far from the optimum. Instead, we generally monitor _|xt_ +1 _− xt|_ (for the moment, assume _x_ is scalar). We might consider absolute convergence: _|xt_ +1 _−_ _<u>|xt</u>_ <u>+1</u> _−xt| xt| < ϵ_ or relative convergence, _< ϵ_ . Relative convergence is appealing because it _|xt|_ accounts for the scale of _x_ , but it can run into problems when _xt_ is near zero, in which case one can use<sup>_<u>|xt</u>_</sup><sup><u>+1</u></sup><sup>_−xt|_</sup> _< ϵ_ . We would want to account for machine precision in thinking about setting _|xt|_ + _ϵ ϵ_ . For relative convergence a reasonable choice of _ϵ_ would be to use the square root of machine epsilon or about 1 _×_ 10<sup>_−_8</sup> . This is the _reltol_ argument in _optim()_ in R. Problems with the optimization may show up in a convergence measure that fails to decrease or cycles (oscillates). Software generally has a stopping rule that stops the algorithm after a fixed number of iterations; these can generally be changed by the user. When an algorithm stops because of the stopping rule before the convergence criterion is met, we say the algorithm has failed to converge. Sometimes we just need to run it longer, but often it indicates a problem with the function being optimized or with your starting value.

For multivariate optimization, we use a distance metric between _xt_ +1 and _xt_ , such as _∥xt_ +1 _− xt∥p_ , often with _p_ = 1 or _p_ = 2.

### **4.2 Starting values**

Good starting values are important because they can improve the speed of optimization, prevent divergence or cycling, and prevent finding local optima.

Using random or selected multiple starting values can help with multiple optima (aka multimodality).

Here’s a function (the Rastrigin function) with multiple optima that is commonly used for testing methods that claim to work well for multimodal problems. This is a hard function to optimize with respect to, particularly in higher dimensions (one can do it in higher dimensions

9

than 2 by simply making the _x_ vector longer but having the same structure). In particular Rastrigin with 30 dimensions is considered to be very hard.

rastrigin <- **function** (x) { A <- 10 n <- **length** (x) **return** (A*n + **sum** (x^2 - A * **cos** (2*pi*x))) } const <- 5.12 nGrid <- 100 gr <- **seq** (-const, const, len = nGrid) xs <- **expand.grid** (x1 = gr, x2 = gr) y <- **apply** (xs, 1, rastrigin) **require** (fields) **image.plot** (gr, gr, **matrix** (y, nGrid, nGrid), col= **tim.colors** (32))


<!-- Start of picture text -->
80<br>60<br>40<br>20<br>0<br>−4 −2 0 2 4<br>gr<br>4<br>2<br>gr 0<br>−2<br>−4<br><!-- End of picture text -->

One R package that may be useful for multi-modal problems is _DEoptim_ , which implements

10

an evolutionary algorithm (genetic algorithms are one kind of evolutionary algorithm). It would be interesting to try an evolutionary algorithm on a test function like this.

### **4.3 Convergence rates**

Let _ϵt_ = _|xt − x_<sup>_∗_</sup> _|_ . If the limit


exists for _β >_ 0 and _c̸_ = 0, then a method is said to have order of convergence _β_ . This basically measures how big the error at the _t_ + 1th iteration is relative to that at the _t_ th iteration, with the approximation that _|ϵt_ +1 _| ≈ c|ϵt|_<sup>_β_</sup> .

Bisection doesn’t formally satisfy the criterion needed to make use of this definition, but roughly speaking it has linear convergence ( _β_ = 1), so the magnitude of the error decreases by a factor of _c_ at each step. Next we’ll see that N-R has quadratic convergence ( _β_ = 2), which is fast.

To analyze convergence of N-R, consider a Taylor expansion of the gradient at the minimum, _x_<sup>_∗_</sup> , around the current value, _xt_ :


for some _ξt ∈_ [ _x_<sup>_∗_</sup> _, xt_ ]. Making use of the N-R update equation: _xt_ +1 = _xt −_<sup>_<u>f</u>′_</sup><sup><u>(</u></sup><sup>_xt_</sup><sup><u>)</u></sup> _f_<sup>_′′_</sup> ( _xt_ )<sup>to substitute ,</sup> and some algebra, we have


If the limit of the ratio on the right hand side exists and is equal to _c_ :


then we see that _β_ = 2.

If _c_ were one, then we see that if we have _k_ digits of accuracy at _t_ , we’d have 2 _k_ digits at _t_ + 1 (e.g., _|ϵt|_ = 0 _._ 01 results in _|ϵt_ +1 _|_ = 0 _._ 0001), which justifies the characterization of quadratic convergence being fast. In practice _c_ will moderate the rate of convergence. The smaller _c_ the better, so we’d like to have the second derivative be large and the third derivative be small. The expression also indicates we’ll have a problem if _f_<sup>_′′_</sup> ( _xt_ ) = 0 at any point [think about what this corresponds to graphically - what is our next step when _f_<sup>_′′_</sup> ( _xt_ ) = 0?]. The characteristics of the derivatives determine the domain of attraction (the region in which we’ll converge rather than diverge) of the minimum.

11

Givens and Hoeting show that using the secant-based approximation to the second derivative in N-R has order of convergence, _β ≈_ 1 _._ 62.

Here’s an example of convergence comparing bisection and N-R:

**options** (digits = 10) f <- **function** (x) **cos** (x) fp <- **function** (x) - **sin** (x) fpp <- **function** (x) - **cos** (x) xstar <- pi _# known minimum ## N-R_ x0 <- 2 xvals <- **c** (x0, **rep** (NA,9)) **for** (t **in** 2:10){ xvals[t] <- xvals[t-1] - **fp** (xvals[t-1]) / **fpp** (xvals[t-1]) } **print** (xvals) ## [1] 2.000000000 4.185039863 2.467893675 3.266186278 3.140943912 3.141592654 ## [7] 3.141592654 3.141592654 3.141592654 3.141592654 _## bisection_ bisecStep <- **function** (interval, fp){ xt <- **mean** (interval) **if** ( **fp** (interval[1]) * **fp** (xt) <= 0) interval[2] <- xt **else** interval[1] **return** (interval) } nIt <- 30 a0 <- 2; b0 <- (3*pi/2) - (xstar - a0) _## have b0 be as far from min as a0 for fair comparison with N-R_ interval <- **matrix** (NA, nr = nIt, nc = 2) interval[1, ] <- **c** (a0, b0) **for** (t **in** 2:nIt){ interval[t, ] <- **bisecStep** (interval[t-1, ], fp) } **rowMeans** (interval) ## [1] 2.785398163 3.178097245 2.981747704 3.079922475 3.129009860 3.153553552

12

---

[← Unit 11 — optim Part 05 —](05-unit-11-optim-part-05.md) · [Up: contents](index.md) · [Unit 11 — optim Part 07 — →](07-unit-11-optim-part-07.md)
