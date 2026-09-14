---
title: 11 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/tutorials/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 slides

**Source:** `tutorials/11-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Tutorial 11

1. Continuous random variables X and Y have a joint PDF given by

   - 2/3 if (x, y) belongs to the closed shaded region

   - fX,Y (x, y) = 0 otherwise

   - �


<!-- Start of picture text -->
y<br>2<br>1<br>1 2  x<br><!-- End of picture text -->

We want to estimate Y based on X.

   - (a) Find the LMS estimator g(X) of Y .

   - (b) Calculate the conditional mean squared error E �(Y − g(X))<sup>2</sup> | X = x�.

   - (c) Calculate the mean squared error E �(Y − g(X))<sup>2</sup> �. Is it the same as E [var(Y |X)]?

   - (d) Derive L(X), the linear LMS estimator of Y based on X.

   - (e) How do you expect the mean squared error of L(X) to compare to that of g(X)?

   - (f) What problem do you expect to encounter, if any, if you try to find the MAP estimator for Y based on observations of X.

2. Consider a noisy channel over which you send messages consisting of 0s and 1s to your friend. It is known that the channel independently flips each bit sent with some fixed probability p; however the value of p is unknown. You decide to conduct some experiments to estimate p and seek your friend’s help. Your friend, cheeky as she is, insists that you send her messages consisting of three bits each (which you will both agree upon in advance); for each message, she will only tell you the total number of bits in that message that were flipped. Let X denote the number of bits flipped in a particular three-bit message.

   - (a) Find the PMF of X.

   - (b) Derive the ML estimator for p based on X1, . . . , Xn, the numbers of bits flipped in the first n three-bit messages.

   - (c) Is the ML estimator unbiased?

   - (d) Is the ML estimator consistent?

   - (e) You send n = 100 three-bit messages and find that the total number of bits flipped is 20. Construct a 95% confidence interval for p. If necessary, you may use a conservative bound on the variance of the number of bits flipped.

   - (f) What are some other ways to estimate the variance. How do you expect your confidence interval to change with different estimates of the variance.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
