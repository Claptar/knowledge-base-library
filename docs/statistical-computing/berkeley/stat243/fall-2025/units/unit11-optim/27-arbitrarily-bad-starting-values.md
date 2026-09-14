---
title: Arbitrarily bad starting values
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Arbitrarily bad starting values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

inits = (10, 0, 10000, 0.1)
fit5 = minimize(nll, inits, args=(data), method='Nelder-Mead', options={'disp': True})
fit6 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})
```


```python
#| include: False
#| code-fold: True
#| eval: False

## Real example with US precip data -- not included in 2023 for sake of time.
## In the demo code (not shown here; see the source qmd file), we'll work our way through a real example of optimizing a likelihood for some climate data on extreme precipitation.

import numpy as np
import matplotlib.pyplot as plt

data_file = os.path.join('..', 'data', 'precipData.txt')
y_hundredths = np.genfromtxt(data_file, missing_values = 'NA')  # precip in hundredths of inches
y_hundredths = y_hundredths[~np.isnan(y_hundredths)]
y = y_hundredths / 100  # precip now in inches

npy=31+28+31 # number of days in winter season
cutoff = 1 / 25.4  # Convert 1 mm to inches
thresh = np.percentile(y[y > cutoff], 98,)

---

[← Different starting value (recall non-positive definite Hessian)](26-different-starting-value-recall-non-positive-definite-hessia.md) · [Up: contents](index.md) · [Create a histogram of the data →](28-create-a-histogram-of-the-data.md)
