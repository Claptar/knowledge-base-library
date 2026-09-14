---
title: (a) When z ≥ 0
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/12-solutions-rec12-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (a) When z ≥ 0

**Source:** `solutions/12-solutions-rec12-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Page 1 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

When z < 0:


Hence,


(b) Solving using the total probability theorem, we have:


First when z < 0, we have:


Page 2 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Then, when z ≥ 0 we have:


3. (a) We have X = Rcos(Θ) and Y = Rsin(Θ). Recall that in polar coordinates, the differential area is dA = dxdy = rdrdθ. So


Page 3 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

(b)


(c)


Note: The PDF of R<sup>2</sup> is exponentially distributed with parameter λ = 1/2. This is a very convenient way to generate normal random variables from independent uniform and exponential random variables. We can generate an arbitrary random variable X with CDF FX by first generating a uniform random variable and then passing the samples from the uniform distribution through the function FX −1 . But since we don’t have a closed-form expression for the CDF of a normal random variable, this method doesn’t work. However,

Page 4 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

we do have a closed-form expression for the exponential distribution. Therefore, we can generate an exponential distribution with parameter 1/2 and we can generate a uniform distribution in [0, 2π], and with these two distributions we can generate standard normal distributions.

4. Problem 4.20, page 250 in text. See text for the proof.

An alternative proof is given below:

Consider the problem of picking a parameter α to minimize the expected squared difference between two random variables X and Y . Consider


with Y = 0. We start with a variational calculation to find α that minimizes J(α). The value of α which minimizes J(α) is found by setting the first derivative of J(α) to zero (since, for Y = 0, dαd<sup>22</sup> J(α) = 2E[Y 2] > 0).


<!-- Start of picture text -->
dJ<br>dα  =0<br>α<br>J() α<br><!-- End of picture text -->


Page 5 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

Then


Rearranging this expression gives the Schwarz inequality for expected values:


Note that in the above derivation, we assumed Y = 0 so that E[Y<sup>2</sup> ] > 0. If we assume Y = 0 then the Schwarz inequality will hold with equality since then E[XY ] = 0 and E[Y<sup>2</sup> ] = 0.

Page 6 of 6

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 12 solutions rec12 sol Part 02 —](02-12-solutions-rec12-sol-part-02.md) · [Up: contents](index.md)
