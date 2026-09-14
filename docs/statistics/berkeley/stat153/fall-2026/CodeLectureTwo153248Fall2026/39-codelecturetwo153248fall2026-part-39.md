---
title: CodeLectureTwo153248Fall2026 Part 39 —
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLectureTwo153248Fall2026 Part 39 —

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

residuals = md7.resid

plt.figure(figsize=(12, 4))

plt.plot(t, residuals)
plt.axhline(0, linestyle="--")

plt.xlabel("Time (months)")
plt.ylabel("Residual")
plt.title("Model 7 Residuals")

plt.show()


print("Prediction 168 months ahead:", y_future[-1])
```

```
Prediction 168 months ahead: 356954.5625958116
```

*(2 figures omitted — see the original notebook.)*

The prediction for July 2040 given by this model is 356.954 million, which is quite close to the prediction given by the Census Bureau.

Below is the plot for the growth rates along with the fitted regression curve.

```python
plt.figure(figsize=(12, 5))

plt.plot(t, g, label="Observed growth rates")
plt.plot(t, g_fitted, label="Fitted growth rates")

plt.axvline(c1_hat, linestyle="--", label="Change point 1")
plt.axvline(c2_hat, linestyle="--", label="Change point 2")

plt.xlabel("Time (months)")
plt.ylabel("Monthly log growth rate")
plt.title("Model 7: Piecewise Linear Model for Population Growth")
plt.legend()

plt.show()
```

*(1 figure omitted — see the original notebook.)*

This model fits a smaller slope for the data after time October 1996. This is the reason for its smaller prediction compared to the other models.

Overall message from this notebook is that there are several ways of using linear regression for time series forecasting, and different models yield different predictions. The idea of working with **differenced** data is quite common in time series analysis, and yields good results often. Differencing means working with $x_t - x_{t-1}$ instead of $x_t$. In the above analysis, we worked with growth rates which are the result of differencing applied to $\log y_t$. We shall work with differenced data in many applications in this course.

---

[← Plot residuals](38-plot-residuals.md) · [Up: contents](index.md)
