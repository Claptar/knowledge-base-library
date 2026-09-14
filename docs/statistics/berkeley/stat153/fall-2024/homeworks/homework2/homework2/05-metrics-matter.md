---
title: Metrics matter
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Metrics matter

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

10. (4 pts)
Below is some code to generate data `y` and predictions `yhat1` and `yhat2` from
two hypothetical models. Plot the predictions from each model as a line overlaid
on top of the original data. Give each line its own color, and use a legend to
denote which model it refers to. Then compute and report the mean absolute error
(MAE) and mean absolute percentage error (MAPE), as defined in lecture, for each
model. Discuss and explain what you find.

```r
set.seed(0)
x = 1:50
y = rpois(n = 50, lambda = c(rep(5, 25), 5 + exp(0:24 * 0.2)))
yhat1 = c(rep(6.5, 25), 6.5 + exp(0:24 * 0.2))
yhat2 = c(rep(5, 25), 5 + exp(0:24 * 0.18))
```

11. (4 pts)
Define a new vector of predictions `yhat3` from a third hypothetical model, by
starting with those `yhat2` from the second model, and changing the multiplier
in the exponent for the last 25 predictions from `0.18` to `0.22`. As in the
last question, plot `yhat2` and `yhat3` as colored lines overlaid on top of the
data and clearly mark them with a legend. Also, compute and compare the MAE and
MAPE of the third model versus the second. It should be worse according to both
metrics. Finally, for each of `yhat2` and `yhat3`, compute what is known as mean
absolute relative error (MARE):
$$
\mathrm{MARE} = 100 \times \frac{1}{N} \sum_{t=1}^N \frac{|y_t - \hat{y}_t|}
{|\hat{y}_t|}
$$
Discuss and explain what you find.

---

[← Covariance calculations](04-covariance-calculations.md) · [Up: contents](index.md) · [Cross-validation →](06-cross-validation.md)
