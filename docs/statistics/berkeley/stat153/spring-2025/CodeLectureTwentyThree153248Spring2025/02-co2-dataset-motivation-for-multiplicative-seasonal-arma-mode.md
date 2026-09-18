---
title: co2 dataset (Motivation for Multiplicative Seasonal ARMA models)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# co2 dataset (Motivation for Multiplicative Seasonal ARMA models)

Next we study seasonal and multiplicative seasonal ARMA models. The following dataset provides some motivation for considering these models.

```python
co2 = pd.read_csv('co2_TSA.csv')
print(co2)
#This is a simple time series dataset from the R package TSA
#TSA is an R package that is written by the authors of the book "Time Series Analysis with Applications in R (second edition)"
#by Jonathan Cryer and Kung-Sik Chan
#This dataset gives the monthly co2 levels in Alert, Canada from January 1994 to December 2004 (132 observations in total for 11 years)
y = co2['x']
plt.figure(figsize = (12, 7))
plt.plot(y)
plt.xlabel('Time (months)')
plt.ylabel('co2 level')
plt.title('Monthly co2 levels in Alert, Canada')
plt.show()
```

```
Unnamed: 0       x
0             1  363.05
1             2  364.18
2             3  364.87
3             4  364.47
4             5  364.32
..          ...     ...
127         128  368.69
128         129  368.55
129         130  373.39
130         131  378.49
131         132  381.62

[132 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

Before fitting stationary ARMA models, we first preprocess the data by differencing. We first take the seasonal difference: $\nabla_s y_t = y_t - y_{t-s}$ where $s = 12$.

```python
#Seasonal differencing: y_t - y_{t-12}
ydiff12 = y.diff(periods = 12) #this works when y is a pandas series (it will not work when y is a np array for example)
plt.figure(figsize = (12, 7))
plt.plot(ydiff12)
plt.xlabel('Time (months)')
plt.ylabel('value')
plt.title('Seasonal Differences of Monthly co2 levels in Alert, Canada')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that there will be NAs corresponding to the first 12 observations. The presence of these NAs might cause issues with subsequent functions (such as plot_acf and plot_pacf).

```python
#there will be NAs in the first twelve entries of ydiff12
print(ydiff12)
```

```
0       NaN
1       NaN
2       NaN
3       NaN
4       NaN
       ...
127    0.72
128    0.00
129    1.11
130    0.74
131    1.63
Name: x, Length: 132, dtype: float64
```

Below we use '.dropna()' to remove NAs before plotting ACF and PACF.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ydiff12.dropna(), lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
axes[0].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plot_pacf(ydiff12.dropna(), lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
axes[1].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Based on the plot of $\nabla_s y_t$, it appear that there are still some trends in the dataset. So we difference one more time before fitting stationary models.

```python
#We now take one more differencing; this time regular differencing
y2d = ydiff12.diff()
plt.figure(figsize = (12, 7))
plt.plot(y2d)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The sample ACF and PACF of this data is plotted using the code below.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(y2d.dropna(), lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
axes[0].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plot_pacf(y2d.dropna(), lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
axes[1].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The ACF has a large negative autocorrelation at lag one, and then a bunch of small autocorrelations followed by nonnegligible ones at lags 11, 12, 13. If we want to use an MA(q) model here, then $q = 13$ would be reasonable. But that model will have quite a few parameters. It would be preferable to have a simpler MA model with fewer parameters that has an ACF similar to the above sample ACF. To get such a model, we need to learn about seasonal and multiplicative seasonal ARMA models.

---

[← ACF and PACF of ARMA processes](01-acf-and-pacf-of-arma-processes.md) · [Up: contents](index.md) · [Seasonal ARMA models →](03-seasonal-arma-models.md)
