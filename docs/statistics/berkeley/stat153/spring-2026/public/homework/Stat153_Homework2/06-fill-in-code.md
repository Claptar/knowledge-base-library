---
title: FILL IN CODE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# FILL IN CODE

**Source:** [`public/homework/Stat153_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

**Q6e. Re-fit the Ridge model using three different regularization values `alpha = [0.1, 100, 1000]`, and plot the resulting predictions on top of one another and on top of the original data (on the same plot), with each labeled. What do you notice about how the prediction changes as alpha varies? What about the coefficients? (3 points)**

```python
for alpha in [0.1, 100, 1000]:
    # FILL IN CODE HERE
```

**Q6f. Repeat Q6e but with LASSO, using `alpha = [0.1, 5, 10]`. Plot the resulting predictions for each of these `alpha` values on top of the true data and comment on how this differs from ridge (or not). What about the coefficients? (3 points)**

```python
for alpha in [0.1, 5, 10]:
    # FILL IN CODE HERE
```

## Q7. Cross-validation for time series

Above, you used time series cross-validation to select regularization parameter `alpha` for both ridge and lasso. Explain why the optimal `alpha` values will generally differ by orders of magnitude for ridge and lasso, and why this does not mean one method is "more regularized" than the other. ( 2points)

---

[← FILL IN CODE](05-fill-in-code.md) · [Up: contents](index.md)
