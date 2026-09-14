---
title: predicted populations y{n+1},...,y
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# predicted populations y{n+1},...,y

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_future_md5 = y.iloc[-1] * np.exp(np.cumsum(g_pred_md5))

print("Predicted population at n + 168:", y_future_md5[-1])
```

```
Predicted population at n + 168: 373123.6153089739
```

The prediction is similar (but slightly higher) to that given by Model 4.

```python
plt.plot(np.arange(n), y, label="Observed")
plt.plot(np.arange(n, n + 168), y_future_md5, label="Predicted (model 5)", color = 'red')
plt.plot(np.arange(n, n + 168), y_future_md4, label="Predicted (model 4)", color = 'green')


plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is a plot of the growth rates along with the fitted values for Models 4 and 5.

```python
plt.plot(t, g, label="Observed growth rate")
plt.plot(t, md5.fittedvalues, label="Fitted values for model 5", color = 'red')
plt.plot(t, md4.fittedvalues, label="Fitted values for model 4", color = 'green')

plt.xlabel("Time")
plt.ylabel("Monthly log growth rate")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the fitted slope for Model 5 after the breakpoint is slightly higher than the overall slope obtained from Model 4. This is the reason why Model 5 is giving a slightly larger prediction for future values compared to Model 4.

Below is the plot of residuals for Model 5.

```python
g_residuals = g - md5.fittedvalues
plt.plot(t, g_residuals, label="Residuals")
plt.xlabel("Time")
plt.ylabel("Monthly log growth rate")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Model 6: Two change of slope points

Next we fit a modification of Model 5 which has two change of slope points:
\begin{align*}
   g_t = \beta_0 + + \beta_1 t + \beta_2 (t - c_1)_+ + \beta_3 (t - c_2)_+ + \epsilon_t.
\end{align*}
This fits a curve with two different slopes. Assuming $c_1 < c_2$, the slopes are $\beta_1$ (before $c_1$), $\beta_1 + \beta_2$ (between $c_1$ and $c_2$) and $\beta_1 + \beta_2 + \beta_3$ after $c_2$. We will treat $c_1, c_2$ as unknown and estimate them from the data. We will go over the estimation strategy later in detail (essentially, we go over all values of $c_1, c_2$ and select the ones which give the smallest sum of squares); the code given below computes the estimates.

```python

---

[← Best change point](20-best-change-point.md) · [Up: contents](index.md) · [Growth rates →](22-growth-rates.md)
