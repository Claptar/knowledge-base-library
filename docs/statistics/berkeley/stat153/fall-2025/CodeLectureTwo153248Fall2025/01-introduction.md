---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Simple Linear Regression for Time Series
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

We shall fit simple linear regression models to the Consumer Price Index (CPI) Data (downloaded from https://fred.stlouisfed.org/series/CPIAUCSL). Changes in the CPI are used to measure Inflation.

```python
## Inflation (Consumer Price Index)
cpi = pd.read_csv('CPIAUCSL_01September2025.csv')
print(cpi)
```

```
observation_date  CPIAUCSL
0         1947-01-01    21.480
1         1947-02-01    21.620
2         1947-03-01    22.000
3         1947-04-01    22.000
4         1947-05-01    21.950
..               ...       ...
938       2025-03-01   319.615
939       2025-04-01   320.321
940       2025-05-01   320.580
941       2025-06-01   321.500
942       2025-07-01   322.132

[943 rows x 2 columns]
```

```python
cpi['observation_date'] = pd.to_datetime(cpi['observation_date'])
cpi.set_index('observation_date', inplace = True)
print(cpi)
```

```
CPIAUCSL
observation_date
1947-01-01          21.480
1947-02-01          21.620
1947-03-01          22.000
1947-04-01          22.000
1947-05-01          21.950
...                    ...
2025-03-01         319.615
2025-04-01         320.321
2025-05-01         320.580
2025-06-01         321.500
2025-07-01         322.132

[943 rows x 1 columns]
```

```python
plt.figure(figsize=(8,6))
plt.plot(cpi.index, cpi['CPIAUCSL'], label='CPI')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.title('Consumer Price Index (CPI)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [CPI Regression with Time as Covariate →](02-cpi-regression-with-time-as-covariate.md)
