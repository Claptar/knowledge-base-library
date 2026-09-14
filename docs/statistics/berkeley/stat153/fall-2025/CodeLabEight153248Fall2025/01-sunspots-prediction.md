---
title: Sunspots Prediction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEight153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspots Prediction

**Source:** [`CodeLabEight153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We evaluate the prediction accuracy of some simple models for the sunspots dataset.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header=None, sep=';')
print(sunspots.head())

y = sunspots.iloc[:,1].values
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

Let us split the dataset into two parts (training and test). We will fit models to the training data, and evaluate their prediction accuracy on the test dataset.

```python
splitnumber = 250
sunspots_train = sunspots.iloc[:splitnumber, :].copy()
sunspots_test = sunspots.iloc[splitnumber:, :].copy()

#print(sunspots_train)
#print(sunspots_test)

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

*(1 figure omitted — see the original notebook.)*

### Model One: Sinusoid Model

Our first model is the simple sinusoidal model that we studied way back in Lectures 5-8:
\begin{equation*}
  y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The post estimate for $f$ can be obtained by the follwoing code

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
pred_test = (
    md.params[0] + md.params[1] * (np.cos(2 * np.pi * fhat * t_future))
    + md.params[2] * (np.sin(2 * np.pi * fhat * t_future))
)

---

[Up: contents](index.md) · [Prediction error →](02-prediction-error.md)
