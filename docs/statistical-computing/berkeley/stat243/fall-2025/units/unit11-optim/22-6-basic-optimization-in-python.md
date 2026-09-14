---
title: 6. Basic optimization in Python
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Basic optimization in Python

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Core optimization functions

Scipy provides various useful optimization functions via `scipy.optimize`, including many of the algorithms discussed in this unit.

- `minimize_scalar` implements golden section search (`golden`) and interpolation combined with golden section search (`brent`, akin to `optimize` in R).
- `minimize` implements various methods for multivariate optimization including Nelder-Mead and BFGS. You can choose which
    method you prefer and can try multiple methods. You can supply a
    gradient function for use with the Newton-related
    methods but it can also calculate numerical derivatives on the fly.
- One can provide a variety of nonlinear, linear, and simple bounds constraints as well, though certain types of constraints can only be used with certain algorithms.

Here's a very basic example of using `minimize` with the Mauna Loa CO2 example we saw earlier when hand-coding Newton-Raphson. Here we'll include the unknown variance as an additional parameter so we have a full likelihood. And as mentioned previously, we could profile out $\beta_0$ and $\beta_1$ and $\sigma^2$, but we won't do that here so as to illustrate multivariate Newton-Raphson.

```python
#| eval: False

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize

data = pd.read_csv(os.path.join('..','data', 'co2_annmean_mlo.csv'),
    header = 0, names = ['year','co2','unc'])

## Center years for better numerical behavior
data.year = data.year - np.mean(data.year)

beta2_init = 50
implicit_covar = np.exp(data.year/beta2_init)

X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params

def nll(params, data):
    # params[3] is log of sigma^2 to address constraint
    n = len(data.year)
    fitted = params[0] + params[1] * np.exp(data.year / params[2])
    return (n/2)*params[3] + 0.5 * np.sum((data.co2 - fitted)**2) / np.exp(params[3])

sigma2_init = np.mean((data.co2-model.fittedvalues)**2)

inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))

---

[← Shrinkage](21-shrinkage.md) · [Up: contents](index.md) · [Optimization using Nelder-Mead →](23-optimization-using-nelder-mead.md)
