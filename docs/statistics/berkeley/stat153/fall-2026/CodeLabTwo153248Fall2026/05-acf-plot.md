---
title: ACF Plot
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ACF Plot

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Given a time series dataset $z_1, \dots, z_n$ and a **lag** h, define
\begin{equation}
   r_h := \frac{\sum_{t=1}^{n-h} (z_t - \bar{z})(z_{t+h} - \bar{z})}{\sum_{t=1}^n (z_t - \bar{z})^2}
\end{equation}
for $h = 0, 1, 2, \dots$. Here $\bar{z}$ is simply the mean of $z_1, \dots, z_n$. The acf plot graphs $h$ on the x-axis and $r_h$ on the y-axis. The quantity $r_h$ is known as the **sample autocorrelation** of the data at lag $h$ (acf stands for "Autocorrelation Function"). When $n$ is large and $h$ is small, $r_h$ approximates the sample correlation in the bivariate dataset $(z_1, z_{h+1}), (z_2, z_{h+2}), \dots, (z_{n-h}, z_n)$. The actual formula for the sample correlation in the bivariate dataset $(z_1, z_{h+1}), (z_2, z_{h+2}), \dots, (z_{n-h}, z_n)$ is:
\begin{equation}
   \frac{\sum_{t=1}^{n-h} (z_t - \bar{z}^{(1)})(z_{t+h} - \bar{z}^{(2)})}{\sqrt{\sum_{t=1}^{n-h} (z_t - \bar{z}^{(1)})^2}\sqrt{\sum_{t=1}^{n-h} (z_{t+h} - \bar{z}^{(2)})^2}} ~~~ \text{ where } \bar{z}^{(1)} = \frac{\sum_{t=1}^{n-h} z_t}{n-h} ~~ \text{ and } ~~ \bar{z}^{(2)} = \frac{\sum_{t=1}^{n-h} z_{t+h}}{n-h}.
\end{equation}
If we now use the simple approximations $\bar{z}^{(1)} \approx \bar{z}$ and $\bar{z}^{(2)} \approx \bar{z}$ and replace the sums in the denominator to range over all $t = 1, \dots, n$ (as opposed to $t = 1, \dots, n-h$), we get the formulat for $r_h$. These approximations are reasonable when $n$ is large and $h$ is small.

The ACF plot tells us about the size of the correlations between the successive values of given time series. Note that $r_0$ is always equal to 1. So we are really looking at the size of $r_h$ for $h \geq 1$.

Here is the ACF plot for the residuals of the regression fitted to the GDP data.

```python
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(md.resid, lags = 50)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation Function of Residuals")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This plot reveals that the residuals have significant autocorrelations. Note the presence of the blue shaded region that is automatically supplied by the plot. This is supposed to help us assess the size of the autocorrelations. The idea is that even if the data is i.i.d $N(0, \sigma^2)$ so that there  is are no autocorrelations, by randomness, some of the computed sample autocorrelations will be nonzero. The typical size of these **null** autocorrelations is indicated by the blue shaded region. The implication is that we should only consider the size of an autocorrelation as significantly different from zero if it sticks out of the blue regions.

```python
iidz = np.random.normal(size = 400)
plot_acf(iidz, lags = 50)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Sample autocorrelations of i.i.d noise")
plt.show()
#note that the acf value at h = 0 is always 1
```

*(1 figure omitted — see the original notebook.)*

Let us get back to the ACF plot of the residuals from the model fit to the GDP data. There are significant autocorrelations at small lags (especially $h = 1, 2, 3$). The implication of this is the following. Suppose we want to predict the GDP for the future quarter immediately following the last data observation. We can use the predicted value given by the model. But the last residual value is about 2548 which is quite larger than zero. Because of significant positive autocorrelation at lag 1, we would expect the next residual value to be quite positive as well. This means that we should adjust the predicted value given by the model upwards by about 2548 for a better forecast. This makes sense from the plot of the data and fitted values as well. We shall study such procedures later in the course.

```python
#the value of the last residual
md.resid[n-1]
```

```
2548.0506349557836
```

---

[← Residuals](04-residuals.md) · [Up: contents](index.md) · [Residual Sum of Squares (RSS) and Residual df →](06-residual-sum-of-squares-rss-and-residual-df.md)
