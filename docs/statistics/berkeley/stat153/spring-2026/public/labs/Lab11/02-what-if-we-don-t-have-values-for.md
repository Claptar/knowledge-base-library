---
title: What if we don't have values for $\Phi$?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# What if we don't have values for $\Phi$?

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

On Tuesday, we also talked about state space models for measurements taken from bone marrow transfusion patients. Here we have measures of white blood cell count (WBC), platelets (PLT), and hematocrit (HCT) over 91 days. Early on in the dataset, there are measurements for each day, but as time goes on the measurements become more infrequent.

We'd like to use a Kalman filter to estimate the states of each of these (WBC, PLT, HCT) while looking at interactions between them. We will fit the $\Phi$, $Q$, $R$, $\mu_0$, and $\sigma_0$ using maximum likelihood estimation (MLE).

```python

---

[← Lab 11](01-lab-11.md) · [Up: contents](index.md) · [Load the data →](03-load-the-data.md)
