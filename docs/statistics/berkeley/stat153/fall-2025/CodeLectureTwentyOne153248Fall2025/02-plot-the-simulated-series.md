---
title: Plot the simulated series
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the simulated series

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(y, color='black')
plt.title("Manually Simulated MA(2) Process (θ₁=0.2, θ₂=0.2)")
plt.xlabel("Time")
plt.ylabel("y_t")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(y, lags = h_max, ax = ax)
ax.set_title("Sample ACF of log differenced varve series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## GDP Growth Rate Data

Our second dataset is the GDP growth rate data. This can be calculated from the raw GDP data by first taking the logarithms, and then differencing the logarithms. Because, this is a common preprocessing, one can directly obtain the growth rate data from FRED (https://fred.stlouisfed.org/series/A191RP1Q027SBEA).

```python
gdp = pd.read_csv("GDP_12Nov2025.csv")
print(gdp.head())
y = gdp['GDP'].to_numpy()
plt.plot(y, color = 'black')
plt.xlabel('Quarter')
plt.show()
```

```
observation_date      GDP
0       1947-01-01  243.164
1       1947-04-01  245.968
2       1947-07-01  249.585
3       1947-10-01  259.745
4       1948-01-01  265.742
```

*(1 figure omitted — see the original notebook.)*

We cannot fit MA models directly to this dataset. So we do the usual preprocessing by first taking logarithms and then differences.

```python
ylog = np.log(y)
ylogdiff = np.diff(ylog)*100
plt.plot(ylogdiff, color = 'black')
plt.xlabel('Quarter')
plt.title('Differenced Logarithm of GDP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us compute the sample acf of this dataset.

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(ylogdiff, lags = h_max, ax = ax)
ax.set_title("Sample ACF of GDP percent change")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are two spikes sticking out at lags 1 and 2. This indicates that MA(2) is a reasonable model. We fit MA(2) by using the ARIMA function as follows.

```python
mamod = ARIMA(ylogdiff, order = (0, 0, 2)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(0, 0, 2)   Log Likelihood                -503.717
Date:                Sat, 15 Nov 2025   AIC                           1015.435
Time:                        22:14:36   BIC                           1030.419
Sample:                             0   HQIC                          1021.423
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.5418      0.118     13.081      0.000       1.311       1.773
ma.L1          0.1893      0.026      7.250      0.000       0.138       0.240
ma.L2          0.2232      0.060      3.749      0.000       0.107       0.340
sigma2         1.4628      0.039     37.788      0.000       1.387       1.539
===================================================================================
Ljung-Box (L1) (Q):                   0.18   Jarque-Bera (JB):              6483.73
Prob(Q):                              0.67   Prob(JB):                         0.00
Heteroskedasticity (H):               1.59   Skew:                            -0.03
Prob(H) (two-sided):                  0.02   Kurtosis:                        25.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Fitting MA models is more complicated compared to fitting AR models. This can lead to some numerical issues. For example, in the above code if you fit the MA(2) model to ylogdiff = np.diff(np.log(y)), you might get a warning saying the optimization for computing the MLE is not converging. The warning seems to go away if you work with np.diff(np.log(y))*100 (now you are multiplying by 100).

## AR Models

Let us now see if AR models can be fit to the GDP growth rate data. The sample PACF gives an indication of a good value of $p$ for which AR($p$) is reasonable.

```python
p_max = 40
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_pacf(ylogdiff, lags = p_max)
plt.title("Sample PACF of diff(log(GDP))*100")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can fit the AR model using AutoReg (as we have been doing previously). We can also use the ARIMA function with order $(p, 0, 0)$ (you will see in the Monday section).

```python
from statsmodels.tsa.ar_model import AutoReg
armod = AutoReg(ylogdiff, lags = 2).fit()
print(armod.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                     AutoReg(2)   Log Likelihood                -499.916
Method:               Conditional MLE   S.D. of innovations              1.207
Date:                Sat, 15 Nov 2025   AIC                           1007.833
Time:                        22:14:39   BIC                           1022.792
Sample:                             2   HQIC                          1013.812
                                  313
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.9099      0.125      7.293      0.000       0.665       1.154
y.L1           0.2100      0.056      3.780      0.000       0.101       0.319
y.L2           0.2010      0.056      3.616      0.000       0.092       0.310
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.7686           +0.0000j            1.7686            0.0000
AR.2           -2.8136           +0.0000j            2.8136            0.5000
-----------------------------------------------------------------------------
```

AutoReg fit a causal stationary model (because the roots have moduli strictly larger than 1) to the data.

This AR(2) model fit the equation (below $x_t$ is $\left(\log(GDP_t) - \log(GDP_{t-1}) \right) * 100$).
\begin{equation*}
   x_t = 0.9099 + 0.21 x_{t-1} + 0.2010 x_{t-2} + \delta_t
\end{equation*}
where $\delta_t \overset{\text{i.i.d}}{\sim} N(0, 1.207^2)$
But when we used the MA(2) model, we got the equation:
\begin{equation*}
x_t = 1.5418 + \epsilon_t + 0.1893 \epsilon_{t-1} + 0.2232 \epsilon_{t-2}
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, 1.4628)$. Since both these models are fit to the same dataset, it makes sense to ask if they are similar models in some sense. This is actually true, and it can be verified in a few ways. First note that the mean of the MA(2) model is clearly 1.5418. For computing the mean of the AR(2) model $x_t = 0.9099 + 0.21 x_{t-1} + 0.2010 x_{t-2} + \delta_t$, take expectation on both sides ($\delta_t$ has mean zero and, by stationarity each of $x_t$, $x_{t-1}$ and $x_{t-2}$ have the same mean $\mu$) to get
\begin{align*}
   \mu = 0.9099 + 0.21 \mu + 0.2010 \mu \implies \mu = \frac{0.9099}{1 - 0.21 - 0.201} = 1.5446
\end{align*}
So the two means are almost the same.

```python
print(armod.params[0]/(1 - armod.params[1] - armod.params[2]))
```

```
1.5446358356501164
```

Next let us compute the AutoCovariance values of the two models. There is an inbuilt function called \texttt{arma_acovf} which computes autocovariance.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_acovf

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [---- AR(2) model ---- →](03------ar-2-model.md)
