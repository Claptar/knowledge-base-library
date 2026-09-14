---
title: INSERT CODE HERE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# INSERT CODE HERE

**Source:** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Q6. Ridge regression vs. LASSO

**Q6a. Suppose you are modeling sunspot counts (from Q3) as a sum of $K=100$ sinusoidal components (200 regressors: a cosine and sine for each frequency). Without running any models yet, describe why OLS is likely to overfit this model, and how ridge regression and lasso would each address this differently. What happens to the 200 coefficients, and how would they look (qualitatively) different? (3 points)**

**Q6b. Now fit the OLS model using statsmodels with 100 frequencies, and plot the result for y vs t (the original data) and y_hat (OLS) vs t. In another plot, plot the $\beta$ coefficients and comment on their structure (are they positive, negative, mostly zero? Anything notable?). (4 points)**

```python

---

[← Some imports that will probably be helpful for you](02-some-imports-that-will-probably-be-helpful-for-you.md) · [Up: contents](index.md) · [FILL IN CODE →](04-fill-in-code.md)
