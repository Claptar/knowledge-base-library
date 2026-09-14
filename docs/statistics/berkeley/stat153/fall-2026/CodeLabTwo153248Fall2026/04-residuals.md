---
title: Residuals
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Residuals

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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
 [-15.52029528 -15.52029529]
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

From this plot, we see that there are some very large residuals indicating the presence of time points where the model predictions are quite far off from the observed values. This could be because of outliers or some systematic features that the model is missing. Also the residual plot looks quite smooth which indicates that there is some correlation between nearby residuals. This can be better visualized via the **acf plot** (sometimes known as the correlogram) of the residuals.

---

[← Fitted Values](03-fitted-values.md) · [Up: contents](index.md) · [ACF Plot →](05-acf-plot.md)
