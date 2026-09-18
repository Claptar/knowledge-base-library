---
title: Q3. Sinusoidal regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q3. Sinusoidal regression

**Q3a. Fit a sinusoidal regression $y = R \cos (2\pi f t +\phi) + \epsilon$ to the sunspots dataset from ASTSA assuming one major oscillation frequency $f$. Do a grid search over possible values of $f$, explaining how you chose this range, then evaluate what is the best $f$ and fit the regression via OLS. Report the $\beta$ parameters, then re-derive $R$ and $\phi$. Comment on the units for these measurements and verify that they make sense for the problem. Also plot your predicted sunspot data on top of the true data and label. (7 points)**

```python
sunspots = astsa.load_sunspotz()
t = sunspots['Time']
y = sunspots['Value']

plt.plot(t,y)
plt.xlabel('Time (year)')
plt.ylabel('Sunspots')

# INSERT CODE HERE
```

```
Text(0, 0.5, 'Sunspots')
```

*(1 figure omitted — see the original notebook.)*

**Q3b. Perform the regression again using the best two sinusoids, starting with your estimate from part (a) as the first sinusoid. Report the parameters as before and show the predicted vs. actual data.  (3 points)**

```python
## INSERT CODE HERE
```

**Q3c. Comment on the structure of the residuals after these two regressions. Are the residuals (weakly) stationary? (2 points)**

## Q4. Cross-validation part 1

**Suppose you use cross-validation to select between two models, but your dataset has repeated measurements from the same subjects (as in our finger-tapping data). If you split randomly into folds, explain why your CV estimate of prediction error will be optimistically biased. What would you do instead? (2 points)**

## Q5. Cross-validation part 2

**Explain why using $R^2$ on training data to select between models with different numbers of predictors is misleading. How does cross-validation address this problem, and why is it more aligned with what we actually care about (prediction on new data)? (3 points)**

---

[← Q2. Choosing covariates for multiple linear regression](02-q2-choosing-covariates-for-multiple-linear-regression.md) · [Up: contents](index.md) · [Q6. Ridge regression vs. LASSO →](04-q6-ridge-regression-vs-lasso.md)
