---
title: 'Model One: Sinusoid Model'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model One: Sinusoid Model

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

# Prediction error:
pred_error_rms_sinusoid = np.sqrt(np.mean((pred_test - sunspots_test.iloc[:, 1]) ** 2))
print(pred_error_rms_sinusoid)
```

```
79.83531765284938
```

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

← Introduction · [Up: contents](index.md) · [Model Two: The Yule Model →](03-model-two-the-yule-model.md)
