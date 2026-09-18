---
title: Q2. ARMA model parameterization
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q2. ARMA model parameterization

Repeat the following numerical exercise three times. Generate n = 500 observations from the ARMA model given by

$$x_t = 0.9x_{t−1} +w_t − 0.9w_{t−1}$$

with $w_t \sim iid N(0,1)$. You can simulate the data using the python function `ArmaProcess`. Note that the AR coefficients are passed in as `[1, -phi_1, ...]` (with the sign flipped for `phi`), whereas the MA coefficients are passed in as `[1, theta_1, ...]` (no sign flip). Plot the simulated data each time, compute the sample ACF and PACF of the simulated data, and fit an ARMA(1,1) model to the data. What happened and how do you explain the results?

```python
def generate_AR(phi1, theta1, n=500):
    ar1 = ## FILL IN
    ma1 = ## FILL IN
    AR_object = ArmaProcess(ar1, ma1)
    simulated_data = AR_object.generate_sample(nsample=n)
    return simulated_data

phi1 = 0.9
theta1 = -0.9
pp=1
for repeat in np.arange(3):
    data=generate_AR(phi1, theta1)
    model = ARIMA(#FILL IN)
    print(model.summary())

    plt.subplot(3,3,pp)
    plt.plot(data)
    pp+=1

    ax=plt.subplot(3,3,pp)
    # Plot the ACF

    pp+=1

    ax=plt.subplot(3,3,pp)
    # Plot the PACF

    pp+=1
```

**Answer** fill in text here

## Q3. AR(2) model and characteristic polynomial

Q3a. For the AR(2) model given by $x_t=-0.9x_{t-2} + w_t$, write out the characteristic polynomial and find its roots.

**Answer:** Fill in

Q3b. Now using the following code to generate some simulated data, add code to plot the ACF and the PACF. Comment on how the roots of the characteristic polynomial relate to what you see here.

```python
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess

# Generate an AR(2) process: $x_t=-0.9x_{t-2} + w_t$
ar2 = np.array([1, 0, 0.9])
ma = np.array([1])
AR_object = ArmaProcess(ar2, ma)

# Generate 10000 samples
np.random.seed(42)
simulated_data = AR_object.generate_sample(nsample=10000)

# 2. Plot the ACF
# FILL IN

# 3. Plot the PACF
# FILL IN
```

**Answer:** add your text here

## Q4. Stationarity of ARIMA models

Suppose

$y_t = \beta_0 + \beta_1 t + \cdots + \beta_q t^q + x_t, \quad \beta_q\neq 0$

where $x_t$ is stationary.

Q4a. First, show that $\nabla^k x_t$ is stationary for any $k=1,2,\dots $.

**Answer:** Fill in

Q4b. Next show that $\nabla^k y_t$ is not stationary for $k < q$, but is stationary for $k \geq q$.

**Hint:** Use the following *Lemma*: For any integer $m \geq 0$, $\nabla t^m$ is a polynomial $t$ of degree $m-1$ (when $m\geq 1$), and $\nabla$ of a constant is 0.

**Answer:** Fill in

---

[← Stat 248 - Homework 4 - YOUR NAME HERE](01-stat-248---homework-4---your-name-here.md) · [Up: contents](index.md) · [Q5. Fitting an ARIMA model →](03-q5-fitting-an-arima-model.md)
