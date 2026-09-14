---
title: Plot a line at the maximum alpha. This should be in the middle
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot a line at the maximum alpha. This should be in the middle

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.axvline(alphas[allRcorrs.mean(2).mean(1).argmax()])
plt.xlabel('Alpha')
plt.ylabel('Correlation')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Show predictions

Now we will show the predicted versus actual activity for all electrodes. If these are well-modeled by the STRF, you should see that the predicted and actual activity look fairly similar. If a larger regularization value alpha was chosen, the predicted activity will tend to look smoother.

```python

---

[← Regularization parameters (alphas - also sometimes called lambda)](19-regularization-parameters-alphas---also-sometimes-called-lam.md) · [Up: contents](index.md) · [How much time to show? →](21-how-much-time-to-show.md)
