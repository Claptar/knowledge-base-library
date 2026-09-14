---
title: Residuals
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Residuals

**Source:** [`Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The residuals simply are the differences between the observed data and the fitted values. We use the notation $e$ for the vector of residuals:
\begin{equation*}
  e = y - \hat{y}
\end{equation*}
The $i^{th}$ residual is simply the $i^{th}$ entry of $e$.

```python
residuals = y - fvals

print(np.column_stack([md.resid[:10], residuals[:10]]))
```

```
[[-46.51607406 -46.51607406]
 [-41.36390609 -41.36390609]
 [-35.55856157 -35.55856157]
 [-23.3740286  -23.3740286 ]
 [-15.52029529 -15.52029528]
 [ -7.01034972  -7.01034972]
 [  1.12781999   1.12781999]
 [  3.62722574   3.62722574]
 [ -0.55912056  -0.55912056]
 [ -3.28420702  -3.28420702]]
```

A plot of the residuals against time is an important diagnostic tool which can tell us about the effectiveness of the fitted model.

```python
plt.plot(md.resid)
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Residuals")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From this plot, we see that there are some very large residuals indicating the presence of time points where the model predictions are quite far off from the observed values. This could be because of outliers or some systematic features that the model is missing. Also the residual plot looks quite smooth which indicates that there is some correlation between nearby residuals. This can be better visualized via the **acf (autocorrelation function)** plot (sometimes known as the correlogram) of the residuals.

```python
print(gdp[:10])
gdp['observation_date'][np.argmin(residuals)]
```

```
observation_date      GDP
0       1947-01-01  243.164
1       1947-04-01  245.968
2       1947-07-01  249.585
3       1947-10-01  259.745
4       1948-01-01  265.742
5       1948-04-01  272.567
6       1948-07-01  279.196
7       1948-10-01  280.366
8       1949-01-01  275.034
9       1949-04-01  271.351
'2020-04-01'
```

---

[← Fitted Values](03-fitted-values.md) · [Up: contents](index.md) · [ACF Plot →](05-acf-plot.md)
