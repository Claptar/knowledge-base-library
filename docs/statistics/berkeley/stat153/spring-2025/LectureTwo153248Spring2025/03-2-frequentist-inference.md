---
title: 2 Frequentist Inference
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Frequentist Inference

**Source:** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Frequentist inference is most commonly done via Maximum Likelihood Estimators. The MLEs for _β_ 0 _, β_ 1 _, σ_ are obtained by maximizing the likelihood. From the expression (1) for the likelihood, the following is a natural strategy for maximizing it: (a) first maximize over _β_ 0 _, β_ 1 for fixed _σ_ . This is equivalent to minimizing _S_ ( _β_ 0 _, β_ 1) and will lead to the MLEs _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1. (b) Plug in the values _β_ 0 = _β_<sup>ˆ</sup> 0 and _β_ 1 = _β_<sup>ˆ</sup> 1 in (1) and then maximize over _σ_ .

_β_ ˆ0 and _β_ ˆ1 are therefore given by the minimizers of _S_ ( _β_ 0 _, β_ 1). It is left as an exercise to verify that

where


To get the MLE for _σ_ , we need to maximize


It is left as an exercise to show that


The quantities _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _,_ ˆ _σ_ provide point estimates of the unknown parameters _β_ 0 _, β_ 1 and _σ_ . More work is needed for uncertainty quantification. For this, one attempts to deduce the distribution of _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _,_ ˆ _σ_ . This can be done in closed form. As an example, for _β_<sup>ˆ</sup> 1, we have


One can also check that, jointly, _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 have the following bivariate normal distribution:


2

These formulae are easier to deduce if we use matrix notation (which we shall do when we look at multiple linear regression next week). The distribution of _σ_ ˆMLE is given by:


where _χ_<sup>2</sup> _n−_ 2<sup>denotesthechi-squareddistributionwith</sup><sup>_n −_2degreesoffreedom.Themean</sup> of the chi-squared distribution equals its degrees of freedom which implies that


Therefore the MLE for _σ_<sup>2</sup> is not unbiased (in contrast, the MLEs _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 are unbiased). It is easy to correct the bias leading to the following unbiased estimator of _σ_<sup>2</sup> :


Usage of ˆ _σ_ unbiased is much more common than that of ˆ _σ_ MLE (note that ˆ _σ_ unbiased is not unbiased for _σ_ ; rather the square of _σ_ ˆunbiased is unbiased for _σ_<sup>2</sup> ).

Another important fact is that ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1) and _σ_ ˆunbiased<sup>2areindependent.</sup>

These facts are used to derive the following confidence interval for _β_ 1:


where _tn−_ 2 _,α/_ 2 is the positive point such that P _{tn−_ 2 _≥ tn−_ 2 _,α/_ 2 _}_ = _α/_ 2 (i.e., the _t_ -distribution with _n −_ 2 degrees of freedom assigns probability mass _α/_ 2 to the right of _tn−_ 2 _,α/_ 2). (2) is a valid confidence interval because:


where _tn−_ 2 is the _t_ -distribution with _n −_ 2 degrees of freedom.

---

[← 1 Simple Linear Regression](02-1-simple-linear-regression.md) · [Up: contents](index.md) · [3 Bayesian Inference →](04-3-bayesian-inference.md)
