---
title: 20 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 slides

**Source:** `recitations/20-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 20: November 18, 2010

1. In your summer internship, you are working for the world’s largest producer of lightbulbs. Your manager asks you to estimate the quality of production, that is, to estimate the probability p that a bulb produced by the factory is defectless. You are told to assume that all lightbulbs have the same probability of having a defect, and that defects in different lightbulbs are independent.

   - (a) Suppose that you test n randomly picked bulbs, what is a good estimate Zn for p, such that Zn converges to p in probability?

   - (b) If you test 50 light bulbs, what is the probability that your estimate is in the range p ± 0.1?

   - (c) The management asks that your estimate falls in the range p ± 0.1 with probability 0.95. How many light bulbs do you need to test to meet this specification?

# 2.


<!-- Start of picture text -->
p Xn  (x)  p Y n  (y)<br>1  1<br>1- ­ 1- ­<br>n  n<br>­1 n ­1n<br>0 1 x  0 n y<br><!-- End of picture text -->

- Let Xn and Yn have the distributions shown above.

- (a) Find the expected value and variance of Xn and Yn.

- (b) What does the Chebyshev inequality tell us about the convergence of Xn? Yn?

- (c) Is Yn convergent in probability? If so, to what value?

- (d) If a sequence of random variables converges in probability to a, does the corresponding sequence of expected values converge to a? Prove or give a counter example.

A sequence of random variables is said to converge to a number c in the mean square, if


   - (e) Use Markov’s inequality to show that convergence in the mean square implies convergence in probability.

   - (f) Give an example that shows that convergence in probability does not imply convergence in the mean square.

3. Random variable X is uniformly distributed between −1.0 and 1.0. Let X1, X2, . . ., be inde­ pendent identically distributed random variables with the same distribution as X. Determine which, if any, of the following sequences (all with i = 1, 2, . . .) are convergent in probability. Give reasons for your answers. Include the limits if they exist.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

(a) Xi Xi (b) Yi = i (c) Zi = (Xi)<sup>i</sup>

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
