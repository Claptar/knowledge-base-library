---
title: Legend (one entry per type)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Legend (one entry per type)

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Implementing rolling cross validation

As we discussed in class, our forecasts get worse the longer we try to project out over time. Another way we might want to look at this, therefore, is through rolling cross validation. Let's look at  this for the best model, ARMA(2,1).

```python
start_forecast = 700
order = (2,0,1)

results_rolling = {}
all_forecast = []

---

[← Split our data into training and test data](11-split-our-data-into-training-and-test-data.md) · [Up: contents](index.md) · [Keep adding data to the forecast, starting our forecast at startforecast →](13-keep-adding-data-to-the-forecast-starting-our-forecast-at-st.md)
