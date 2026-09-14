---
title: 1 Simple linear regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec06_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec06_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Simple linear regression

**Source:** [`public/lectures/Lec06_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec06_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Last time we spoke about regression models where we have two parameters, _β_ 0 and _β_ 1 that we use to estimate the relationship between our response variable _y_ and our covariate _x_ :


For example, _y_ is height of an adult and _x_ is the height of their parent, or _y_ is the price of chicken and _x_ is time.

## **1.1 Revisiting OLS**

We also talked about ordinary least squares (OLS), which is where we want to solve:


We can do this by differentiating Q with respect to each parameter and setting it equal to zero:

First, for _β_ 0:


1


And for _β_ 1:


Then it follows that:


Notice now how our solution for the slope, _β_ 1, is related to the covariance of _x_ and _y_ and the variance of _x_ !

Another note here is that to calculate _x_ ¯ and _y_ ¯, we often must use the sample means (e.g. across all time points), because we do not have multiple samples for each time point.

## **1.2 Maximum likelihood estimation (MLE)**

We can also calculate these terms using MLE, In this case, we normally assume that the errors are normally distributed i.i.d, e.g.:


The likelihood is expressed as:


To maximize the likelihood, we can maximize the log-likelihood, which is easier to deal with:

2


Since we know the sum of squared error _Q_ =<sup>∑</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi−β_0</sup><sup>_−β_1</sup><sup>_xi_)2=</sup> _S_ ( _β_ 0 _, β_ 1), we can take the derivative with respect to unknown parameters _β_ 0 _, β_ 1, and _σ_ :


These first two equations are the same as what we derived before. However, we now have a new term in which we get the MLE estimate for _σ_ from the third equation (with _β_ 0 and _β_ 1 replaced by _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1, respectively):


From this, we can get _σ_ ˆMLE<sup>2=</sup> _n_<sup><u>1</u></sup><sup>_S_(ˆ</sup><sup>_β_0</sup><sup>_,β_ˆ1).</sup>

But as it turns out, this is a biased estimator (unlike those for _β_ 0 and _β_ 1, which are not! We often instead use a corrected, unbiased estimator of _σ_ ˆ<sup>2</sup> where we divide by _n − p_ , where _p_ is the number of parameters estimated (here, _p_ = 2, one for _β_ 0 and one for _β_ 1). That is:


Let’s look at a simulation to show how this happens!

Next time, we will look at how this extends to multiple linear regression. Later this bias will also become important when we think about regularization.

---

[Up: contents](index.md) · [2 A note on assumptions →](02-2-a-note-on-assumptions.md)
