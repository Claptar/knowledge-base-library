---
title: Model parameter counts
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model parameter counts

Now let's look at model performance as a function of number of parameters. What do you notice about the comparison between AR, MA, and ARMA models for the same number of parameters for this dataset?

```python
fig, ax = plt.subplots(figsize=(10, 5))

colors = {'AR': '#2196F3', 'MA': '#FF9800', 'ARMA': '#4CAF50'}

for name, res in results.items():
    # Determine model type and parameter count
    order = models_to_test[name]
    p, d, q = order
    nparams = p + q
    mtype = 'ARMA' if (p > 0 and q > 0) else ('AR' if p > 0 else 'MA')

    ax.scatter(nparams, res['rmse'], c=colors[mtype], s=100, zorder=3, edgecolors='white')
    ax.annotate(name, (nparams, res['rmse']), textcoords="offset points", xytext=(6, 6), fontsize=10)

# Legend (one entry per type)
for mtype, color in colors.items():
    if any((mtype == 'AR' and 'AR(' in n and 'ARMA' not in n) or
           (mtype == 'ARMA' and 'ARMA' in n) or
           (mtype == 'MA' and 'MA(' in n and 'ARMA' not in n)
           for n in results):
        ax.scatter([], [], c=color, s=100, label=mtype, edgecolors='white')

ax.set(xlabel='Number of parameters (p + q)', ylabel='RMSE (lower is better)',
       title='Model Comparison: Forecast Error vs. Parsimony')
ax.legend(fontsize=12)
ax.set_xticks([1,2,3,4])
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Discussion

Let's look at the plot above:

1. **Among pure AR models**, how many lags do you need to get competitive? Is that parsimonious?
2. **Among pure MA models**, can they match the AR performance? How many lags?
3. **Compare to ARMA** How many total parameters do the best ARMA models use compared to the best pure AR?
4. **The parsimony argument**: ARMA(2,1) uses 3 parameters. What's the best pure AR can do with 3 parameters? With 7? (you may need to run some more)

---

[← Heart Rate Variability](01-heart-rate-variability.md) · [Up: contents](index.md) · Implementing rolling cross validation →
