---
title: Average |CCF| across features, then show per-electrode traces + mean
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Average |CCF| across features, then show per-electrode traces + mean

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ccf_abs = np.abs(ccf).mean(axis=1)  # [n_elec, n_lags]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(lags_s, ccf_abs.T, color='gray', alpha=0.3, lw=0.8)
ax.plot(lags_s, ccf_abs.mean(0), color='C0', lw=2, label='mean across elecs')
ax.axvline(0, color='k', ls='--', lw=0.8)
ax.set_xlabel('lag (s)  [positive = spectrogram leads neural]')
ax.set_ylabel('|CCF|, averaged across spec features')
ax.set_title('Stimulus–response cross-correlation envelope')
ax.legend()
plt.tight_layout()
plt.show()
```

## Create delay matrices

We now have the prerequisite matrices to perform our regression (`ytrain` and `xtrain`, and cross-validation test set `ytest` and `xtest`). To include time delays, we can set up a stacked matrix of our stimulus at different time delays. This actually has a special name -- it's called a [Toeplitz matrix](http://en.wikipedia.org/wiki/Toeplitz_matrix)). As a toy example, say we have a spectrogram with n time points and 3 frequencies.

$$
\begin{bmatrix}
    x_{1,1} & x_{1,2} & x_{1,3} \\
    x_{2,1} & x_{2,2} & x_{2,3} \\
    x_{3,1} & x_{3,2} & x_{3,3} \\
    \vdots & \vdots & \vdots \\
    x_{n,1} & x_{n,2} & x_{n,3} \\
\end{bmatrix}
$$

Our stacked delay matrix would look something like this:

$$
\begin{bmatrix}
    x_{1,1} & x_{1,2} & x_{1,3} & 0 & 0 & 0 & 0 & 0 & 0 & \ldots & 0 & 0 & 0 \\
    x_{2,1} & x_{2,2} & x_{2,3} & x_{1,1} & x_{1,2} & x_{1,3} & 0 & 0 & 0 & \ldots & 0 & 0 & 0 \\
    x_{3,1} & x_{3,2} & x_{3,3} & x_{2,1} & x_{2,2} & x_{2,3} & x_{1,1} & x_{1,2} & x_{1,3} & \ldots & 0 & 0 & 0 \\
    x_{4,1} & x_{4,2} & x_{4,3} & x_{3,1} & x_{3,2} & x_{3,3} & x_{2,1} & x_{2,2} & x_{2,3} & \ldots & 0 & 0 & 0 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
    x_{n,1} & x_{n,2} & x_{n,3} & x_{n-1,1} & x_{n-1,2} & x_{n-1,3} & x_{n-2,1} & x_{n-2,2} & x_{n-2,3} & \ldots & x_{n-d+1,1} & x_{n-d+1,2} & x_{n-d+1,3} \\
\end{bmatrix}
$$

```python

---

[← Plotting lag relationships](11-plotting-lag-relationships.md) · [Up: contents](index.md) · [Create the delayed matrices →](13-create-the-delayed-matrices.md)
