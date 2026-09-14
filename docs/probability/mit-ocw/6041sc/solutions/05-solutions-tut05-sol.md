---
title: 05 solutions tut05 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/05-solutions-tut05-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 05 solutions tut05 sol

**Source:** `solutions/05-solutions-tut05-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

# Tutorial 5: Solutions

1. (a) Let A be the event that the machine is functional. Conditioned on the random variable Q taking on a particular value q, P(A|Q = q) = q. Using the continuous form of the total probability theorem, the probability of event A is given by:


- (b) Let B be the event that the machine is functional on m out of the last n days. Conditioned on random variable Q taking on value q (a probability q of being functional) the probability of event B is binomial with n trials, m successes, and a probability q of success in each trial. Again using the total probability theorem, the probability of event B is given by:


We then find the distribution on Q conditioned on event B using Bayes rule:


2. Since Y = |X| you can visualize the PDF for any given y as


Also note that since Y = |X|, Y ≥ 0.


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (b) Here we are told X > 0. So there are no negative values of X that need to be considered. Thus,


(c) As explained in the beginning, fY (y) = fX(y) + fX(−y).

3. We want to compute the CDF of the ambulance’s travel time T , P(T ≤ t) = P(|X − Y | ≤ vt), where X and Y are the locations of the ambulance and accident (uniform over [0, l]). Since X and Y are independent, we know:


We can see that P(X − vt ≤ Y ≤ X + vt) corresponds to the integral of the joint density of X and Y over the shaded region in the figure below:


<!-- Start of picture text -->
y<br>y = x+vt<br>l<br>f  (x,y) = 1/l2<br>X,Y<br>vt<br>vt  l  x<br>y = x-vt<br><!-- End of picture text -->

Therefore, because the joint density is uniform over the entire region, we have:


By differentiating the CDF, we find the density of T :


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
