---
title: Sunspots prediction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspots prediction

**Source:** [`Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We evaluate the prediction accuracy of some simple models for the sunspots dataset.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
print(sunspots.head())

y = sunspots.iloc[:, 1].values
n = len(y)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
print(n)
```

```
0     1    2  3  4
0  1700.5   8.3 -1.0 -1  1
1  1701.5  18.3 -1.0 -1  1
2  1702.5  26.7 -1.0 -1  1
3  1703.5  38.3 -1.0 -1  1
4  1704.5  60.0 -1.0 -1  1
325
```

*(1 figure omitted — see the original notebook.)*

Let us split the dataset into two parts (training and test). We will fit models to the training data, and evaluate their prediction accuracy on the test set.

```python
splitnumber = 250
sunspots_train = sunspots.iloc[:splitnumber, :].copy()
sunspots_test = sunspots.iloc[splitnumber:, :].copy()

print(sunspots_train)
print(sunspots_test)

tme_train = sunspots_train.iloc[:,0]
tme_test = sunspots_test.iloc[:,0]
tme = sunspots.iloc[:,0]

y =  sunspots_train.iloc[:,1].values

plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

```
0      1     2    3  4
0    1700.5    8.3  -1.0   -1  1
1    1701.5   18.3  -1.0   -1  1
2    1702.5   26.7  -1.0   -1  1
3    1703.5   38.3  -1.0   -1  1
4    1704.5   60.0  -1.0   -1  1
..      ...    ...   ...  ... ..
245  1945.5   55.3   6.6  365  1
246  1946.5  154.3  11.1  365  1
247  1947.5  214.7   9.8  365  1
248  1948.5  193.0   9.3  366  1
249  1949.5  190.7   9.2  365  1

[250 rows x 5 columns]
          0      1     2      3  4
250  1950.5  118.9   7.3    365  1
251  1951.5   98.3   6.6    365  1
252  1952.5   45.0   4.5    366  1
253  1953.5   20.1   3.0    365  1
254  1954.5    6.6   1.7    365  1
..      ...    ...   ...    ... ..
320  2020.5    8.8   4.1  14440  1
321  2021.5   29.6   7.9  15233  1
322  2022.5   83.2  14.2  15258  1
323  2023.5  125.5  19.2  13286  1
324  2024.5  154.7  22.1  11952  0

[75 rows x 5 columns]
```

*(1 figure omitted — see the original notebook.)*

### Model One: Sinusoid Model

Our first model is the simple sinusoidal model that we studied way back in Lectures 5-8:
\begin{equation*}
  y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The point estimate for $f$ can be obtained by the follwoing code

```python
def rss(f):
    n = len(y)
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss

allfvals = np.arange(0.01, 0.5, .0001) #much finer grid
rssvals = np.array([rss(f) for f in allfvals])
fhat = allfvals[np.argmin(rssvals)]

print(fhat)
print(1/fhat)
```

```
0.08989999999999951
11.123470522803176
```

The predictions with this model are obtained as follows.

```python
n = len(y)
x = np.arange(1, n+1)
xcos = np.cos(2 * np.pi * fhat * x)
xsin = np.sin(2 * np.pi * fhat * x)
X = np.column_stack([np.ones(n), xcos, xsin])

md = sm.OLS(y, X).fit()

t_future = np.arange(n+1, n+len(tme_test) + 1)
pred_test = (md.params[0]
             + md.params[1] * (np.cos(2 * np.pi * fhat * t_future))
             + md.params[2] * (np.sin(2 * np.pi * fhat * t_future)))

---

[Up: contents](index.md) · [Prediction error →](02-prediction-error.md)
