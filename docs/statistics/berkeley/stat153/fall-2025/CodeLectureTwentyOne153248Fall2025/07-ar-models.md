---
title: AR Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# AR Models

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

# ---- AR(2) model ----
ar = np.array([1, -0.21, -0.2010])   # AR polynomial
ma = np.array([1])                   # no MA terms
sigma2 = 1.207**2

acov_ar2 = arma_acovf(ar=ar, ma=ma, sigma2=sigma2, nobs=20)

# ---- MA(2) model ----
ar2 = np.array([1])
ma2 = np.array([1, 0.1893, 0.2232])
sigma2_ma = 1.4628

acov_ma2 = arma_acovf(ar=ar2, ma=ma2, sigma2=sigma2_ma, nobs=20)

# ---- Plot both ----
plt.figure(figsize=(8,5))

lags = np.arange(len(acov_ar2))

plt.stem(lags, acov_ar2, markerfmt='bo', label="AR(2)")
plt.stem(lags, acov_ma2, markerfmt='ro', label="MA(2)")

plt.title("Autocovariance Comparison: AR(2) vs MA(2)")
plt.xlabel("Lag")
plt.ylabel("Gamma(h)")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The autocovariances of the two models are somewhat close to each other. This suggests that the AR(2) and MA(2) models are not very different from each other.

---

[← GDP Growth Rate Data](06-gdp-growth-rate-data.md) · [Up: contents](index.md) · [ARIMA Modeling →](08-arima-modeling.md)
