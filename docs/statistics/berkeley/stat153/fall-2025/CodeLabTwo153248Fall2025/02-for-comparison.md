---
title: For comparison
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# For comparison

**Source:** [`CodeLabTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

gamma = np.array([300.0, -3.0, 0.1, 0.001])
z = np.dot(X, gamma) + np.random.normal(0, 1, X.shape[0])

sim_model = sm.OLS(z, X).fit()
print(sim_model.params)

plt.plot(sim_model.resid)
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Residuals")
plt.show()
```

```
[ 2.99767066e+02 -2.99623705e+00  9.99834849e-02  1.00002346e-03]
```

*(1 figure omitted — see the original notebook.)*

### ACF Plot

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
2548.0506349268508
```

### Residual Sum of Squares (RSS) and Residual df

Two other commonly used terms (in connection with residuals) are the Residual Sum of Squares (RSS) and the Residual Degrees of Freedom. The RSS is simply the sum of the squares of the residuals:
\begin{equation*}
   \text{RSS} = \sum_{i=1}^n e_i^2 = \sum_{t=1}^n \left(y_t - \hat{\beta}_0 - \hat{\beta}_1 t - \hat{\beta}_2 t^2 - \hat{\beta}_3 t^3 \right)^2
\end{equation*}
RSS is simply equal to the smallest possible of the sum of squares criterion $S(\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3)$ (recall from lecture that $S(\beta_0, \beta_1, \beta_2, \beta_3) = \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2 t^2 - \beta_3 t^3)^2$).

The vector of residuals has the following important property: $X^T e = 0$. This can be proved as follows:
\begin{equation*}
   X^T e = X^T (y - \hat{y}) = X^T (y - X \hat{\beta}) = X^T (y - X (X^T X)^{-1} X^T y) = X^T y - X^T X (X^T X)^{-1} X^T y = X^T y - X^T y = 0.
\end{equation*}
$X^T e = 0$ means that the dot product between every column of $X$ and $e$ equals 0. In our regression model for GDP, $X^T e = 0$ is equivalent to:
\begin{equation*}
   \sum_{t = 1}^n e_t = 0 ~~~~  \sum_{t = 1}^n t e_t = 0 ~~~~  \sum_{t = 1}^n t^2 e_t = 0 ~~~~  \sum_{t = 1}^n t^3 e_t = 0
\end{equation*}
Even though there are $n$ residuals $e_1, \dots, e_n$, they have to satisfy the above four equality constraints. Therefore, the effective number of 'free' residuals is $n-4$. Thus the residual degrees of freedom equals $n-4$.

More generally, the residual df equals the number of observations ($n$) minus the number of columns in the $X$ matrix.

### Estimate of $\sigma$: the residual standard error

The estimate of $\sigma$ is given by:
\begin{equation*}
   \hat{\sigma} = \sqrt{\frac{RSS}{n-4}} = \sqrt{\frac{S(\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3)}{n-4}}
\end{equation*}
This quantity is sometimes called the Residual Standard Error. The value of the Residual Standard Error can be used to assess the size of the residuals (residuals much larger than say twice the Residual Standard Error indicate points where the model fits particularly poorly).

```python
rss = np.sum(md.resid ** 2)
rse = np.sqrt(rss/(n - 4))

print(rse)
```

```
550.9932711741245
```

This intuitively means that residuals with magnitude above 1100 are points where the model fits particularly poorly. From a look at the plot of the residuals against time, there are many residuals which are this large in magnitude.

### Standard Errors of the coefficient estimates

The standard errors corresponding to $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3$ are the square roots of the diagonal entries of $\hat{\sigma}^2 (X^T X)^{-1}$. They are given by md.bse as verified below.

```python
sebetahat_squared = (rse ** 2)*(np.diag(XTX_inverse))
sebetahat = np.sqrt(sebetahat_squared)

print(np.array([md.bse, sebetahat]))
```

```
[[1.26498064e+02 3.50560340e+00 2.60867093e-02 5.49661580e-05]
 [1.26498064e+02 3.50560340e+00 2.60867093e-02 5.49661580e-05]]
```

### t-statistic and confidence intervals for the coefficients

The $t$-statistic for each coefficient is simply the estimate divided by the standard error. The confidence interval for $\beta_j$ is given by:
\begin{equation*}
   \left[\hat{\beta}_j - t_{\alpha/2, n-4} \text{ standard error of } \hat{\beta}_j, \hat{\beta}_j + t_{\alpha/2, n-4} \text{ standard error of } \hat{\beta}_j  \right]
\end{equation*}
where $t_{\alpha/2, n-4}$ is the point beyond the $t$-distribution with $n-4$ degrees of freedom gives probability mass $\alpha/2$. The above formula is the result of:
\begin{equation*}
   \frac{\beta_j - \hat{\beta}_j}{\text{ standard error of } \hat{\beta}_j} \mid \text{ data } \sim t-\text{distribution with} ~n-4 \text{ d.f}
\end{equation*}
The above statement can also be interpreted in a frequentist sense (then the conditional on data will be removed and the randomness will be over the data with fixed $\beta_j$).

```python
from scipy.stats import t

alpha = 0.05
qt = t.ppf(1 - (alpha/2), n-4) #area to the right equaling alpha/2 is the same as area to the left equaling 1-alpha/2
print(qt)

cilower = md.params - md.bse*qt
ciupper = md.params + md.bse*qt
print(np.column_stack([cilower, ciupper]))
print(md.summary())
```

```
1.9677212881552213
[[ 4.32711446e+01  5.41097010e+02]
 [-9.47864205e+00  4.31745880e+00]
 [ 2.45922503e-02  1.27254997e-01]
 [ 5.56525463e-04  7.72841622e-04]]
                            OLS Regression Results
==============================================================================
Dep. Variable:                    GDP   R-squared:                       0.995
Model:                            OLS   Adj. R-squared:                  0.995
Method:                 Least Squares   F-statistic:                 2.000e+04
Date:                Sun, 14 Sep 2025   Prob (F-statistic):               0.00
Time:                        14:37:42   Log-Likelihood:                -2402.2
No. Observations:                 311   AIC:                             4812.
Df Residuals:                     307   BIC:                             4827.
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        292.1841    126.498      2.310      0.022      43.271     541.097
x1            -2.5806      3.506     -0.736      0.462      -9.479       4.317
x2             0.0759      0.026      2.910      0.004       0.025       0.127
x3             0.0007    5.5e-05     12.093      0.000       0.001       0.001
==============================================================================
Omnibus:                       74.600   Durbin-Watson:                   0.095
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              746.989
Skew:                           0.635   Prob(JB):                    6.21e-163
Kurtosis:                      10.485   Cond. No.                     4.63e+07
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.63e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
```

### Visualizing Uncertainty

It was showed in Lecture 4 that the posterior distribution of $\beta$ (this is the vector of coefficients) is given by
\begin{equation*}
   \beta \mid \text{data} \sim t_{4} \left(\hat{\beta}, \hat{\sigma}^2 (X^T X)^{-1}, n - 4 \right)
\end{equation*}
From the definition of the $t$-distribution above, we also know that the distribution above coincides with the distribution of
\begin{equation*}
    \hat{\beta} + \frac{Z}{\sqrt{V/(n-4)}}
\end{equation*}
where $Z \sim N(0, \hat{\sigma}^2 (X^T X)^{-1})$ and $V \sim \chi^2_{n-4}$ are independent. Using this, we can generate vectors $\beta$ from their posterior distribution and then plot the regression curves corresponding to the different generated $\beta$ vectors. This will give us an idea of the uncertainty underlying the coefficients.

```python
N = 200 #this the number of posterior samples that we shall draw
Sigma_mat = (rse ** 2)*(XTX_inverse)
#print(Sigma_mat)

from scipy.stats import chi2, multivariate_normal

chi_samples = chi2(df = n-4).rvs(N)
norm_samples = multivariate_normal(cov = Sigma_mat, allow_singular = True).rvs(N)
post_samples = np.tile(betahat, (N, 1)) + norm_samples / np.sqrt(chi_samples / (n-4))[:, None]
#print(post_samples)

plt.figure(figsize = (10, 6))
plt.plot(y, linewidth = 1, color = 'black')
for k in range(N):
    fvalsnew = np.dot(X, post_samples[k])
    plt.plot(fvalsnew, color = 'red', linewidth = 1)
plt.xlabel('Time (quarterly)')
plt.ylabel('Billions of dollars')
plt.title('GDP data with Fitted values along with uncertainty')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Even though $N = 200$ regression curves have been plotted, they are still fairly clustered together. This suggests that the uncertainty in these estimates is fairly small.

### Other comments

When analyzing such a dataset, it is also common to work with logs instead of the raw GDP numbers directly i.e., take $y = \log (GDP)$. Another common approach is to work with difference of logs (this is interpreted as the GDP growth rate): $y_t = \log(GDP_t) - \log(GDP_{t-1})$. For prediction purposes, note that if you predict a future value of the difference of the logs, then this predicted value can be used to also obtain a prediction for the original data.

---

[← Linear Regression Details](01-linear-regression-details.md) · [Up: contents](index.md)
