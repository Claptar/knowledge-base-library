---
title: Cross-validation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/10_regularization_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/10_regularization_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Cross-validation

How can we avoid overfitting? One way is to seek models that minimize the MSE on *held out data*, that is, data that was not used to train our model.

How do we choose this in practice? For cross validation in general, we might choose to use something like *k-fold cross validation*, which is where we split the data into *k* chunks, train on $k-1$ of those sets, and compute test error based on the last fold. However, in time series there are a few things to consider:

* Often we want to train on past data to predict future data (so randomly permuting time doesn't make sense)
* We also need to preserve the autocorrelation structure in time series data, so we should not randomly choose some percentage of observations. We want to chunk the data in a way that maintains the temporal order in the fitting.

In the past, cross-validation was not used as it was computationally prohibitive to test many possible training/test splits of the data. Nowadays this is not an issue, and cross-validation can be a very clean way to test model performance without requiring:

* normally distributed errors
* homoscedasticity
* correct model specification
* known numbers of parameters

It works for any model without you needing to know anything about the error distribution. This is why this is more popularly used now as compared to parametric approaches such as AIC and BIC (which assume Gaussian errors).

## Alternative fitting procedures

So what do we do in these cases where we have potentially many parameters and few observations, but we want an accurate and interpretable model? We can constrain or *shrink* the coefficients to reduce the variance of our estimates at the cost of slightly increasing bias. This also can allow for improved model interpretability - by forcing some coefficients to be very small or to zero, we can more easily interpret our model by removing irrelevant covariates.

We will discuss these next time when we talk about *ridge regression* and *LASSO regression*, also called *L2* and *L1* regularization, respectively.

---

[← Improving upon the linear model](01-improving-upon-the-linear-model.md) · [Up: contents](index.md)
