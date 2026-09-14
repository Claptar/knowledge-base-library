---
title: 'pred: predictions'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# pred: predictions

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

beta, corrs, valphas, allRcorrs, valinds, pred, _ = cv_ridge(xtraind, ytrain, xtestd, ytest,
                                                               alphas, nfolds, chunklen, nchunks,
                                                               use_corr=use_corr,  single_alpha = single_alpha,
                                                               use_svd=False)
```

## Check alpha values

We will now check the best regularization parameter $\alpha$ for each channel. This will plot each electrode as a curve, with each correlation value vs. alpha. For most "good" electrodes there will be a peak value in the middle of the range of alphas. If your model is consistently showing that the average best $\alpha$ is the smallest or largest value, you should widen your range appropriately and re-run the model.

```python
fig = plt.figure()
plt.semilogx(alphas, allRcorrs.mean(2))  # Log space alphas

---

[← valinds: indices for cross validation](21-valinds-indices-for-cross-validation.md) · [Up: contents](index.md) · [Plot a line at the maximum alpha. This should be in the middle →](23-plot-a-line-at-the-maximum-alpha-this-should-be-in-the-middl.md)
