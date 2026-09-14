---
title: One more example
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# One more example

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's look at one more example from the Shumway and Stoffer book. This dataset gives the thickness of the yearly varves collected from one location in Massachusetts for 634 years (beginning 11,834 years ago!). Varves are sedimentary deposits of sand and silt that are deposited by melting glaciers during the spring melting seasons (see Example 2.8 of the Shumway-Stoffer book, 5th edition). These deposits can be used as proxies for paleoclimatic parameters, such as temperature, because, in a warm year, more sand and silt are deposited from the receding glacier.

```python
varve_data = pd.read_csv('varve.csv')

yraw = varve_data['x']
#plt.figure(figsize = (10, 8))
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## More plot diagnostics

From just looking at the plot, it appears that the variance may be nonstationary. We can also look at the QQ-plot, which shows us whether the data come from an underlying distribution (default: normal), and whether they violate the assumption of homoscedasticity. Here, we'll see that the QQ plot deviates significantly from the line, so we probably do need a variance stabilizing transform (like the logarithm).

```python
from statsmodels.graphics.gofplots import qqplot

plt.figure()
qqplot(yraw, fit=True, line="45");
```

```
<Figure size 1200x400 with 0 Axes>
```

*(1 figure omitted — see the original notebook.)*

If we log-transform the data, this will be better behaved.

```python
#Log transform the data first
ylog = np.log(yraw)
#plt.figure(figsize = (12, 6))
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure()
qqplot(ylog, fit=True, line="45");
```

```
<Figure size 1200x400 with 0 Axes>
```

*(1 figure omitted — see the original notebook.)*

## ACF and PACF

In addition to the log transform, we're going to difference our data, then look at the ACF and PACF to see what to do next.

```python
ylogdiff = np.diff(ylog)
#plt.figure(figsize = (12, 6))
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(ylogdiff, lags=40, ax=axes[0], title='ACF - diff(log(thickness))')
plot_pacf(ylogdiff, lags=40, ax=axes[1], title='PACF - diff(log(thickness))', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Function |  AR(p)    | MA(q)                | ARMA(p,q)
---------|-----------|----------------------|----------
ACF      | tails off | cuts off after lag q | tails off
PACF     | cuts off after lag p | tails off | tails off

*What kind of model should we try?*

```python
h = 20
y_train = ylog[:-h]
y_test = ylog[-h:]

times = np.arange(len(ylog))
times_train = times[:-h]
times_test = times[-h:]

---

[← What does this mean?](22-what-does-this-mean.md) · [Up: contents](index.md) · [---- 3. Model grid ---- →](24------3-model-grid.md)
