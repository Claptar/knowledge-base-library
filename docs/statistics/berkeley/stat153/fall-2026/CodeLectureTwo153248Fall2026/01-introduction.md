---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

---
title: Linear Regression Models fit to the US population data
---

The first topic in this course is "Multiple Linear Regression" for time series. Linear regression can be used in many ways for time series analysis, with basic applications in trend estimation and prediction/forecasting. We shall illustrate this today through the US population data.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

## US Population Dataset

This dataset is downloaded from FRED and gives monthly population of the United States in thousands.

```python
uspop = pd.read_csv('POPTHM_27Aug2026.csv')
print(uspop.head(10))
print(uspop.tail(10))
```

```
observation_date  POPTHM
0       1959-01-01  175818
1       1959-02-01  176044
2       1959-03-01  176274
3       1959-04-01  176503
4       1959-05-01  176723
5       1959-06-01  176954
6       1959-07-01  177208
7       1959-08-01  177479
8       1959-09-01  177755
9       1959-10-01  178026
    observation_date  POPTHM
801       2025-10-01  342366
802       2025-11-01  342439
803       2025-12-01  342495
804       2026-01-01  342540
805       2026-02-01  342581
806       2026-03-01  342627
807       2026-04-01  342680
808       2026-05-01  342746
809       2026-06-01  342822
810       2026-07-01  342909
```

Let us set the index of each row to be the corresponding month, so the plots are easier to interpret.

```python
uspop['observation_date'] = pd.to_datetime(uspop['observation_date'])
uspop.set_index('observation_date', inplace = True)
print(uspop)
```

```
POPTHM
observation_date
1959-01-01        175818
1959-02-01        176044
1959-03-01        176274
1959-04-01        176503
1959-05-01        176723
...                  ...
2026-03-01        342627
2026-04-01        342680
2026-05-01        342746
2026-06-01        342822
2026-07-01        342909

[811 rows x 1 columns]
```

Here is a plot of the dataset.

```python
plt.figure(figsize=(6, 4))
plt.plot(uspop['POPTHM'], label = "population")
plt.xlabel("Time (monthly)")
plt.ylabel("Population (thousands)")
plt.title("Population of the United States")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Based on this dataset, suppose we want to answer the following prediction (or forecasting) question: what would be the population of the United States in July 2040? The last month in the observed data is July 2026 (i.e., month $n$ corresponds to July 2026), so July 2040 would be month $n + 14*12 = n + 168$.

Let us attempt to answer this question by fitting simple models based on linear regression to the observed data. Before fitting models, let us first note some available answers to this question. There are population projections available from the Census Bureau, as well as from the United Nations. The Census Bureau projection for the US population in July 2040 is 355.309 million. The UN projection is 370.209 million.

Let $y_t$ denote the population of the United States for month $t$. The first model is simply: $y_t = \beta_0 + \beta_1 t + \epsilon_t$. This is just linear regression with time $t$ as the covariate.

---

[Up: contents](index.md) · [Model 1: $yt = \beta0 + \beta1 t + \epsilont$ →](02-model-1.md)
