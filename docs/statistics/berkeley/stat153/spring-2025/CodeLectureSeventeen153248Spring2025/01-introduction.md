---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSeventeen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureSeventeen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureSeventeen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSeventeen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: AR Models -- Estimation and Predictions
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

We fit AR models by OLS of $Y$ on $X$ where $Y$ is the vector consisting of $y_{p+1}, \dots y_n$ and $X$ consists of rows $1, y_{t-1}, \dots, y_{t-p}$ for $t = p+1, \dots, n$. This gives rise to estimates $\hat{\phi}_0, \hat{\phi}_1, \dots, \hat{\phi}_p$ which are  also known as Conditional MLEs or Conditional Least Squares Estimates (conditional here refers to conditioning on $y_1, \dots, y_p$).

---

[Up: contents](index.md) · [Dataset One: California Population →](02-dataset-one-california-population.md)
