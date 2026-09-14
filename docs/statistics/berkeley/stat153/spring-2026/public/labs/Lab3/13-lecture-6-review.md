---
title: Lecture 6 review
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 6 review

**Source:** [`public/labs/Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now as in Lecture 6, we are going to start with a known function $y = \beta_0 + \beta_1 x + w_t$. We will assume that $w_t$ is noise taken from a Gaussian distribution $\sim N(0, \sigma^2)$. Here we will choose arbitrary values for each of these.

We will draw samples from this function and then compute our estimated $\beta_0$, $\beta_1$, and $\sigma^2$ through the MLE functions we derived in lecture.

```python
beta0 = # FILL IN
beta1 = # FILL IN
sigma2 = # FILL IN

---

[← Make sure we get the new time index as well](12-make-sure-we-get-the-new-time-index-as-well.md) · [Up: contents](index.md) · [n is the number of time points →](14-n-is-the-number-of-time-points.md)
