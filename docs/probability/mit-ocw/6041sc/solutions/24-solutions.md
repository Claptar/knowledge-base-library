---
title: 24 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/24-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 24 solutions

**Source:** `solutions/24-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Recitation 24: Solutions December 7, 2010

1. (a) Normalization of the distribution requires:


(b) Rewriting pK(k; θ) as:


the probability distribution for the photon number is a geometric probability distribution with probability of success p = 1 − e<sup>−1/θ</sup> , and it is shifted with 1 to the left since it starts with k = 0. Therefore the photon number expectation value is


and its variance is


(c) The joint probability distribution for the ki is


The log likelihood is −n · log Z(θ) − 1/θ<sup>�n</sup> i=1 ki. We find the maxima of the log likelihood by setting the derivative with respect to the parameter θ to zero:


or


For a hot body, θ ≫ 1 and e1/θ1−1<sup>≈θ, we obtain</sup>


Thus the maximum likelihood estimator Θ<sup>ˆ</sup> n for the temperature is given in this limit by the sample mean of the photon number

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


- (d) According to the central limit theorem, the sample mean for large enough n (in the limit) approaches a Gaussian distribution with standard deviation our root mean square error


To allow only for 1% relative root mean square error in the temperature, we need<sup><u>σK</u></sup> < ~~√~~ <u>n</u> 0.01µK. With σK<sup>2=</sup> µ2 K + µK it follows that


In general, for large temperatures, i.e. large mean photon numbers µK ≫ 1, we need about 10,000 samples.

- (e) The 95% confidence interval for the temperature estimate for the situation in part (d), i.e.


is


2. (a) Using the regression formulas of Section 9.2, we have


where


The resulting ML estimates are


(b) Using the same procedure as in part (a), we obtain


Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

where


which for the given data yields


Figure 1 shows the data points (xi, yi), i = 1, . . . , 5, the estimated linear model


and the estimated quadratic model


<!-- Start of picture text -->
y  = 4.09x  2  − 3.07.<br>500<br>Sample data points<br>400<br>300<br>Estimated first-order model<br>Y 200<br>100<br>Estimated second-order model<br>0<br>-100<br>0 2 4 6 8 10 12<br>X<br><!-- End of picture text -->

Image by MIT OpenCourseWare.

Figure 1: Regression Plot

†Required for 6.431; optional for 6.041

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
