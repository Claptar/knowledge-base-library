---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabOne153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLabOne153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Linear Regression for Time Series
---

The first topic in the class would be linear regression. We will see some simple examples of this today. Just plain linear regression usually does not work well for time series analysis; so we will see more sophisticated models later on in the course.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

---

[Up: contents](index.md) · [US Population Dataset →](02-us-population-dataset.md)
