---
title: 2 Predictions given by AR ( p ) models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEighteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEighteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Predictions given by AR ( p ) models

**Source:** [`LectureEighteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEighteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One important goal of time series analysis is prediction also known as forecasting: given the observed data _y_ 1 _, . . . , yn_ , what can we say about the future observations _yn_ +1 _, . . . , yn_ + _k_ for some _k ≥_ 1? In the Bayesian context, prediction is done via the joint probability distribution of


conditional on the observed data _y_ 1 _, . . . , yn_ . For example, point predictions can be obtained by the conditional expectations:


Uncertainty quantification for the predictions can be done via the conditional variances:


Let us focus on point predictions using conditional expectations for now. We shall deal with uncertainty quantification for the predictions in the next class. The conditional expectations can be written as


for _i_ = 1 _, . . . , n_ .

Let us first calculate


for fixed parameters _θ_ . These can be calculated recursively for _i_ = 1 _,_ 2 _, . . ._ as follows. Assuming the validity of the model equation (1) also for _t > n_ , we get


3

We thus have the following recursion for the predictions _y_ ˆ _n_ + _i_ ( _θ_ ):


If we initialize this recursion with


then (5) can be evaluated in sequence for _i_ = 1 _,_ 2 _, . . ._ to calculate _y_ ˆ _n_ + _i_ ( _θ_ ) for all _i ≥_ 1.

Let us get back to the conditional expectation (4):


To compute the integral above, we can do one of two things:

1. We can first generate posterior samples _θ_<sup>(1)</sup> _, . . . , θ_<sup>(</sup><sup>_N_)</sup> from the posterior _fθ|y_ 1 _,...,yn_ ( _θ_ ). Then (7) is approximated as


2. For a simpler approach, we can use the fact that the posterior density _fθ|y_ 1 _,...,yn_ ( _θ_ ) is usually highly concentrated around the point estimate _θ_<sup>ˆ</sup> = ( _β,_<sup>ˆ</sup> ˆ _σ_ ). We can then ignore the small uncertainty of _θ_ around _θ_<sup>ˆ</sup> to write


This second method avoids posterior sampling is faster and simpler.

---

[← 1 AR models: estimation, inference and prediction](01-1-ar-models-estimation-inference-and-prediction.md) · [Up: contents](index.md) · [3 Prediction Uncertainty →](03-3-prediction-uncertainty.md)
