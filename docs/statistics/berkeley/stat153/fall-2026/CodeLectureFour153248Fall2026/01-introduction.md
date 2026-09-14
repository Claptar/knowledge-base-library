---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFour153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureFour153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Multiple Linear Regression for Time Series
---

Multiple linear regression applies to data consisting of an $n \times 1$ vector $y$ and an $n \times (m+1)$ matrix $X$ whose first column is all ones. In the (univariate) time series context, $y$ denotes the observed values of the time series. There are two ways of creating $X$:
1. The covariates are given by various functions of the time. For example, the first covariate could be the time index, the second covariate could be the square of the time index, the third covariate could be some other function of time etc.
2. Auto-Regression: Here the covariates would be the lagged values of the observed time series.
Here are examples of both these kinds of regressions.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

---

[Up: contents](index.md) · [Example of Regression with functions of time: USA Accidents Dataset →](02-example-of-regression-with-functions-of-time-usa-accidents-d.md)
