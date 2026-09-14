---
title: 4.1. Time invariant coefficient
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/cao_etal_2015.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.1. Time invariant coefficient

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/cao_etal_2015.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We first study the performance of the estimator for the time invariant coefficient in model (1). We generate 1000 data sets, each consisting of n = 100,400, 900 subjects. The number of observation times for the response Y.t/ was Poisson distributed with intensity rate 5, and similarly for the number of observation times for the covariate X.t/. With these two numbers of measurements, the observation times for the response and covariate are generated from the uniform distribution Unif(0,1) independently. The covariate process is Gaussian, with values at fixed time points being multivariate normal with mean 0, variance 1 and correlation exp.−|tij − tik|/, where tij is the jth measurement time and tik is the kth measurement time for the response, both on subject i. Whereas realizations of this Gaussian process may not be differentiable on the diagonal, the resulting expectations in conditions 3 and 3<sup>′</sup> are bounded and smoothly differentiable, as required for the validity of the asynchronous estimator. At the data-generating stage, to generate the response, we include the response observation times with the covariate observation times when generating the covariates that are needed for simulating responses at the response observation times. The responses were generated from


where _β_ 0 is the intercept, _β_ 1 is a time-independent coefficient and ".t/ is Gaussian, with mean 0, variance 1 and cov _{_ ".s/, ".t/ _}_ = 2<sup>−|t−s|</sup> . Once the response has been generated, we remove the covariate measurements at the response observation times from the observed covariate values. In this simulation, we set _β_ 0 = 0:5 and _β_ 1 = 1:5 and assess the performance of _β_<sup>ˆ</sup> 1. The results are very similar for other choices of _β_ s. Under a logistic regression model for a binary response, the simulation set-up is similar to that for the continuous response except that the link function is _g_ .x/ = exp.x/= _{_ 1 + exp.x/ _}_ and the response variable is generated through Y.t/ = I.Unif.0,1/ ⩽ 1=[1 + exp _{_ − _β_ 0 − X.t/ _β_ 1 _}_ ]/.

On the basis of our theory, we use different bandwidths in the range of .n<sup>−1=5</sup> , n<sup>−1</sup> / when solving equation (3) to find _β_<sup>ˆ</sup> 1. The kernel function is the Epanechnikov kernel, which is K.x/ = 0:75.1 − x<sup>2</sup> /+. Similar results were obtained by using other kernels. We evaluate the accuracies of the asymptotic approximations by calculating the average bias, the average relative bias and the empirical standard deviation of _β_<sup>ˆ</sup> 1 across the 1000 data sets. We also calculate a modelbased standard error and the corresponding 0:95 confidence interval based on the normal approximation. The automated bandwidth procedure that was described in Section 2 was also employed for estimation.

Table 1 summarizes the main results over 1000 simulations, where ‘auto’ means bandwidths based on the adaptive selection procedure, ‘BD’ represents different bandwidths, ‘Bias’ is the empirical bias, ‘RB’ is Bias divided by the true _β_ 1, ‘SD’ is the sample standard deviation, ‘SE’ is the average of the standard error estimates and ‘CP’ represents the coverage probability of the 95% confidence interval for _β_ 1. We observe that as the sample size increases the bias decreases and is small, that the empirical and model-based standard errors tend to agree reasonably well and that the coverage is close to the nominal 0.95-level. The performance improves with larger sample sizes.

---

[← 4. Numerical studies](07-4-numerical-studies.md) · [Up: contents](index.md) · [4.2. Time-dependent coefficient →](09-4-2-time-dependent-coefficient.md)
