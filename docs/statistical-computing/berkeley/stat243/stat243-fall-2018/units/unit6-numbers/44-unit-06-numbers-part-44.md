---
title: Unit 06 — numbers Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 44 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The absolute error in representing the larger number is around 1 _×_ 10 _−_ 5 and the smaller number is smaller than this.

A work-around is to add a set of numbers in increasing order. However, if the numbers are all of similar magnitude, then by the time you add ones later in the summation, the partial sum will be much larger than the new term. A work-around is to add the numbers in a tree-like fashion, so that each addition involves a summation of numbers of similar size.

Given the limited _range_ of computer numbers, be careful when you are:

- Multiplying or dividing many numbers, particularly large or small ones. Never take the product of many large or small numbers as this can cause over- or under-flow. Rather compute on the log scale and only at the end of your computations should you exponentiate. E.g.,


- Challenge: Let’s think about how we can handle the following calculation. Suppose I want to calculate a predictive density (e.g., in a model comparison in a Bayesian context):


First, why do I use the log conditional predictive density? Second, let’s work with an estimate of the unconditional predictive density on the log scale, log _f_ ( _y_<sup>_∗_</sup> _|y, x_ ) _≈_ log _M_<sup><u>1</u></sup> � _mj_ =1<sup>exp(</sup><sup>_vj_).</sup>

21

Now note that _e_<sup>_vj_</sup> may be quite small as _vj_ is the sum of log likelihoods. So what happens if we have terms something like _e_<sup>_−_1000</sup> ? So we can’t exponentiate each individual _vj_ . This is what is known as the “log sum of exponentials” problem (and the solution as the “log-sumexp trick”). Thoughts?

This also comes up with multiclass logistic regression, where you have quantities like this:


Numerical issues come up frequently in linear algebra. For example, they come up in working with positive definite and semi-positive-definite matrices, such as covariance matrices. You can easily get negative numerical eigenvalues even if all the eigenvalues are positive or non-negative. Here’s an example where we use an squared exponential correlation as a function of time (or distance in 1-d), which is _mathematically_ positive definite (i.e., all the eigenvalues are positive) but not numerically positive definite:

xs <- 1:100 dists <- **rdist** (xs)

corMat <- **exp** (- (dists/10)^2) _# this is a p.d. matrix (mathematically)_ **dg** ( **eigen** (corMat)$values[80:100]) _# but not numerically_

---

[← Unit 06 — numbers Part 43 —](43-unit-06-numbers-part-43.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 45 — →](45-unit-06-numbers-part-45.md)
