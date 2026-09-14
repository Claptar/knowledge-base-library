---
title: Cross-validation
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Cross-validation

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

12. (3 pts)
Recall the R code from lecture that performs time series cross-validation to
evaluate the mean absolute error (MAE) of predictions from the linear regression
of cardiovascular mortality on 4-week lagged particulate levels. Adapt this to
evaluate the MAE of predictions from the regression of cardiovascular mortality
on 4-week lagged particulate levels and 4-week lagged temperature (2 features).
Fit each regression model using a trailing window of 200 time points (not all
past). Plot the predictions, and print the MAE on the plot, following the code
from lecture.

    Additionally (all drawn on the same figure), plot the fitted values on the
training set. By the training set here, we mean what is also called the "burn-in
set" in the lecture notes, and indexed by times 1 through `t0` in the code. The
fitted values should come from the initial regression model that is fit to the
burn-in set. These should be plotted in a different color from the predictions
made in time series cross-validation pass. Print the MAE from the fitted values
the training set somewhere on the plot (and label this as "Training MAE" to
clearly differentiate it).

13. (2 pts)
Repeat the same exercise as in Q12 but now with multiple lags per variable: use
lags 4, 8, 12 for each of particulate level and temperature (thus 6 features in
total). Did the training MAE go down? Did the cross-validated MAE go down?
Discuss. Hint: you may find it useful to know that `lm()` can take a predictor
matrix, as in `lm(y ~ x)` where `x` is a matrix; in this problem, you can form
the predictor matrix by calling `cbind()` on the lagged feature vectors.

14. (2 pts)
Repeat once more the same exercise as in the last question but now with many
lags per variable: use lags 4, 5, ..., through 50 for each of particulate level
and temperature (thus 47 x 2 = 94 features in total). Did the training MAE go
down? Did the cross-validated MAE go down? Are you surprised? Discuss.

---

[← Metrics matter](05-metrics-matter.md) · [Up: contents](index.md) · [More features, the merrier? →](07-more-features-the-merrier.md)
