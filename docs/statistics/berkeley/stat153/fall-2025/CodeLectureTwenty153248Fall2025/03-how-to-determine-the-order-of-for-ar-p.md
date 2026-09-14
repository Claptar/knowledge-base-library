---
title: How to determine the order of $p$ for AR(p)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwenty153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# How to determine the order of $p$ for AR(p)

**Source:** [`CodeLectureTwenty153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here is the method: Calculate PACF(h) for each $h = 1, 2, 3, \dots$. The PACF(h) is defined as the estimate of $\phi_h$ when the AR(h) model is fit to the observed time series data. In other words, PACF(1) is the estimate of $\phi_1$ when AR(1) is fit to the data, PACF(2) is the estimate of $\phi_2$ when AR(2) is fit to the data, and so on. If PACF(h) becomes negligible after a particular value of $h$ (say after $h = p$), then we use $p$ as the AR order.

Here is the function for calculating the PACF.

```python
def sample_pacf(dt, p_max):
    pautocorr = []
    for p in range(1, p_max + 1):
        armd = AutoReg(dt, lags = p).fit()
        phi_p = armd.params[-1]
        pautocorr.append(phi_p)
    return pautocorr
```

Below we apply it to the percent change GNP dataset.

```python
p_max = 50
sample_pacf_vals = sample_pacf(ylogdiff, p_max)
markerline, stemline, baseline = plt.stem(range(1, p_max + 1), sample_pacf_vals)
markerline.set_marker("None")
plt.xlabel("p")
plt.ylabel('Partial Correlation')
plt.title("Sample Partial Auto Correlation")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the plot above, we see that the PACF(h) values become somewhat negligible when $h = \geq 3$. Based on this, $p = 3$ is a reasonable choice for fitting AR($p$) to the percent change GNP data.

Statsmodel has an inbuilt function for calculating PACF. Below, we compute this for the percent change GNP data, and check whether it gives the same values as our function.

```python
from statsmodels.tsa.stattools import pacf
pacf_values = pacf(ylogdiff, nlags=p_max, method = 'ols')
print(np.column_stack([sample_pacf_vals, pacf_values[1:]])) #check that these values match exactly
```

```
[[ 0.24870755  0.24870755]
 [ 0.20772295  0.20772295]
 [-0.01181547 -0.01181547]
 [-0.05004494 -0.05004494]
 [-0.03595239 -0.03595239]
 [ 0.00802459  0.00802459]
 [ 0.08230295  0.08230295]
 [ 0.0316824   0.0316824 ]
 [ 0.09574666  0.09574666]
 [ 0.09594221  0.09594221]
 [ 0.03584216  0.03584216]
 [ 0.00112678  0.00112678]
 [-0.03725445 -0.03725445]
 [ 0.05155244  0.05155244]
 [ 0.07745691  0.07745691]
 [ 0.11526705  0.11526705]
 [ 0.09917843  0.09917843]
 [ 0.08106869  0.08106869]
 [ 0.04302832  0.04302832]
 [ 0.05237025  0.05237025]
 [-0.05067918 -0.05067918]
 [ 0.01267157  0.01267157]
 [-0.08404734 -0.08404734]
 [ 0.09698737  0.09698737]
 [ 0.14416186  0.14416186]
 [-0.07836845 -0.07836845]
 [-0.02209264 -0.02209264]
 [ 0.06157982  0.06157982]
 [-0.02871973 -0.02871973]
 [-0.02974936 -0.02974936]
 [-0.02387845 -0.02387845]
 [ 0.0406917   0.0406917 ]
 [ 0.03228025  0.03228025]
 [ 0.00545047  0.00545047]
 [ 0.00125922  0.00125922]
 [-0.0416868  -0.0416868 ]
 [-0.02112732 -0.02112732]
 [-0.12050451 -0.12050451]
 [-0.10229888 -0.10229888]
 [-0.01385521 -0.01385521]
 [-0.06736392 -0.06736392]
 [ 0.13019911  0.13019911]
 [ 0.0214844   0.0214844 ]
 [ 0.0473848   0.0473848 ]
 [ 0.0398027   0.0398027 ]
 [-0.04117905 -0.04117905]
 [-0.15896129 -0.15896129]
 [-0.07691234 -0.07691234]
 [ 0.01057553  0.01057553]
 [-0.08638415 -0.08638415]]
```

There is also an inbuilt function for plotting pacf values. This plot gives values for PACF($h$) for $h = 0, 1, 2, \dots$ with the default value for PACF($0$) = 1.

```python
from statsmodels.graphics.tsaplots import plot_pacf
fig, axes = plt.subplots()
plot_pacf(ylogdiff, lags = p_max, ax = axes)
axes.set_title("Sample PACF of diff_log_GDP Series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In comparison to our plot of the sample_pacf values, the inbuilt PACF plot from statsmodels will look slightly different (even though it is plotting the same values). The differences are: (a) it also plots the value 1 at lag 0, (b) it gives a shaded region that can be used to assess whether values are negligible or not.

---

[← Preprocessing using logarithms and differences](02-preprocessing-using-logarithms-and-differences.md) · [Up: contents](index.md)
