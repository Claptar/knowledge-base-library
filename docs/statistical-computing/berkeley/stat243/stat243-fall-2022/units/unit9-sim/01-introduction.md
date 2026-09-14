---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit9-sim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit9-sim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

[PDF](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.pdf){.btn .btn-primary}


References:

-   Gentle: Computational Statistics
-   Monahan: Numerical Methods of Statistics

Videos (optional):

There are various videos from 2020 in the bCourses Media Gallery that you
can use for reference if you want to.

  - Video 1. Random number generation, part 1
  - Video 2. Random number generation, part 2
  - Video 3. Rejection sampling
  - Video 4. Importance sampling

Many (most?) statistical papers include a simulation (i.e., Monte Carlo)
study. Many papers on machine learning methods also include a simulation
study. The basic idea is that closed-form mathematical analysis of the properties of
a statistical or machine learning method/model is often hard to do. Even
if possible, it usually involves approximations or simplifications. A
canonical situation in statistics is that we have an asymptotic result
and we want to know what happens in finite samples, but often we do not
even have the asymptotic result. Instead, we can estimate mathematical
expressions using random numbers. So we design a simulation study to
evaluate the method/model or compare multiple methods. The result is
that the researcher carries out an experiment (on the computer, sometimes called *in silico*), generally varying
different factors to see what has an effect on the outcome of interest.

The basic strategy generally involves simulating data and then using the
method(s) on the simulated data, summarizing the results to
assess/compare the method(s).

Most simulation studies aim to approximate an integral, generally an
expected value (mean, bias, variance, MSE, probability, etc.). In low
dimensions, methods such as Gaussian quadrature are best for estimating
an integral but these methods don't scale well (we'll discuss this in
Unit 12 on integration/differentiation), so in higher dimensions we
often use Monte Carlo techniques.

To be more concrete:

-   If we have a *method for estimating a model parameter* (including
    uncertainty), such as a regression coefficient, what properties do
    we want the method to have and what criteria could we use?

-   If we have a *prediction method* (including prediction uncertainty),
    what properties do we want the method to have and what criteria
    could we use?

-   If we have a *method for doing a hypothesis test*, what criteria
    would we use to assess the hypothesis test? What properties do we
    want the test to have?

-   If we have a *method for finding a confidence interval or a prediction interval*, what
    criteria would we use to assess the interval?

---

[Up: contents](index.md) · [1. Monte Carlo considerations →](02-1-monte-carlo-considerations.md)
