---
title: 24 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 24 slides

**Source:** `recitations/24-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 24 December 7, 2010

1. A blackbody at temperature θ radiates photons of all wavelengths, described by its characteristic spectrum. This problem will have you estimate θ, which is fixed but unknown. The PMF for the number of photons K in a given wavelength range and a fixed very short time interval is given by,


Z(θ) is a normalization factor for the probability distribution (the physicists call it the partition function). You are given the task of determining the temperature of the body to two significant digits by photon counting in non-overlapping time intervals of duration one second. The photon emissions in non-overlapping time intervals are statistically independent from each other.

- (a) Determine the normalization factor Z(θ).

- (b) Compute the expected value of the photon number measured in any 1 second time interval, µK = Eθ[K], and its variance, varθ(K) = σK<sup>2.</sup>

- (c) You count the number ki of photons detected in n non-overlapping 1 second time intervals. Find the maximum likelihood estimator, θ<sup>ˆ</sup> n, for temperature θ. Note, it might be useful to introduce the average photon number sn = n 1<sup>�</sup> n i=1<sup>ki. In order to keep the analysis simple</sup> we assume that the body is hot, i.e. θ ≫ 1. You may use the approximation: e1/θ1 `−` 1<sup>≈θforθ≫1.</sup>

In the following questions we wish to estimate the mean of the photon count in a one second time interval using the estimator K<sup>ˆ</sup> , which is given by,


   - σ ˆ

   - (d) Find the number of samples n for which the noise to signal ratio for K<sup>ˆ</sup> , (i.e., µKK ˆ ), is 0.01.

   - (e) Find a 95% confidence interval for the mean photon count estimate for the situation in part (d). (You may use the central limit theorem.)

2. Given the five data pairs (xi,yi) in the table below,


we want to construct a model relating x and y. We consider a linear model


and a quadratic model


where Wi and Vi represent additive noise terms, modeled by independent normal random variables with mean zero and variance σ12 and σ22, respectively.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

- (a) Find the ML estimates of the linear model parameters.

- (b) Find the ML estimates of the quadratic model parameters.

Note: You may use the regression formulas and the connection with ML described in pages 478-479 of the text. However, the regression material is outside the scope of the final.

The figure below shows the data points (xi, yi), i = 1, . . . , 5, the estimated linear model


and the estimated quadratic model


<!-- Start of picture text -->
y  = 4.09x  2 − 3.07.<br><!-- End of picture text -->


<!-- Start of picture text -->
500<br>Sample data points<br>400<br>300<br>Estimated first-order model<br>Y 200<br>100<br>Estimated second-order model<br>0<br>-100<br>0 2 4 6 8 10 12<br>X<br><!-- End of picture text -->

Image by MIT OpenCourseWare.

Figure 1: Regression Plot

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
