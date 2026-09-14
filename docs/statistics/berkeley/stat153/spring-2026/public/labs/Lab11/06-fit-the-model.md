---
title: Fit the model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit the model

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
endog = df[['WBC', 'PLT', 'HCT']].values.astype(float)

mod = BloodSSM(endog)
res = mod.fit(disp=False, maxiter=2000, method='powell', cov_type='robust')
print(res.summary())
```

Notice here that you may get errors related to the covariance matrix being singular or near-singular. The Ljung-Box test tests whether our one-step-ahead prediction errors are serially correlated - if these p-values are less than 0.05, then we do have correlations left in our model that we're missing out on. Here it seems like that's not the case, so that's good news.

On the other hand, there are a number of other assumptions that we aren't meeting. The standard errors here are all close to zero, which means the confidence intervals are likely not trustworthy. Although there are other diagnostics here that are maybe concerning, this is often the case with real biological data. One thing we could try is to force the dynamics to be simpler (i.e. only allow for diagonal terms in $\Phi$), and see if this helps.

## Extract and interpret estimated matrices

In this scenario, we are estimating $\Phi$, $Q$, $R$, so we will print those here and talk about how to interpret them.

```python

---

[← Look at the raw data and see what is missing](05-look-at-the-raw-data-and-see-what-is-missing.md) · [Up: contents](index.md) · [Helper to extract Q or R from Cholesky parameters →](07-helper-to-extract-q-or-r-from-cholesky-parameters.md)
