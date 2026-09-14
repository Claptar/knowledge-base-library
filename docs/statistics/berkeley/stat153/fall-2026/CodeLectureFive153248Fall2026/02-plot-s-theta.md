---
title: Plot S(theta)
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFive153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot S(theta)

**Source:** [`CodeLectureFive153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

theta = np.linspace(-10, 12, 500)
S_values = np.array([S(t) for t in theta])

plt.figure(figsize=(7, 5))
plt.plot(theta, S_values)
plt.axvline(theta_hat, linestyle="--", label=rf"$\hat{{\theta}}={theta_hat}$")
plt.scatter(theta_hat, S(theta_hat), zorder=3)

plt.xlabel(r"$\theta$")
plt.ylabel(r"$S(\theta)$")
plt.title(r"Squares Function $S(\theta)=\sum_i (y_i-\theta)^2$")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we plot the function $S(\hat{\theta})/S(\theta)$ as a function of $\theta$.

```python

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Plot S(thetahat) / S(theta) →](03-plot-s-thetahat-s-theta.md)
