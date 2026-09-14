---
title: Show the predictions and confidence intervals
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Show the predictions and confidence intervals

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

If we want to show the predicted data and confidence intervals for the fitted values, we can use `get_prediction`. We will then produce `pred_summary`, which contains:
* `mean` - fitted values
* `mean_ci_lower`, `mean_ci_upper` - confidence intervals for the mean
* `obs_ci_lower`, `obs_ci_upper` - prediction interval for new observations

```python

---

[← We could also get the coefficients and use these to get yhat instead](06-we-could-also-get-the-coefficients-and-use-these-to-get-yhat.md) · [Up: contents](index.md) · [To show the confidence intervals on the data, we can use the getprediction method →](08-to-show-the-confidence-intervals-on-the-data-we-can-use-the.md)
