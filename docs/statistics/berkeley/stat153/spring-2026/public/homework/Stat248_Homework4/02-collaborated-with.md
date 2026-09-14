---
title: Collaborated with
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Collaborated with

**Source:** [`public/homework/Stat248_Homework4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Due April 23 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

*Instructions:* Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

**Note: For this homework, if you are in the graduate section of the course you also have an assignment due soon for the final project, so you have the option of completing at least 5 out of 6 questions to receive full credit.**

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

```python
# Some imports that might be useful to you
import numpy as np
!pip install h5py
!pip install astsa
import h5py
import astsa # Necessary for loading data for some Qs (may need to do !pip install astsa)
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima.model import ARIMA
```

# Q1. MA model properties

For an MA(1), $x_t =w_t + \theta w_{t−1}$, show that $\rho_x(1)| \leq 1/2$ for any number $\theta$. For which values of $\theta$ does $\rho_x(1)$ attain its maximum and minimum?

**Answer:** Fill in here

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

# Q3. AR(2) model and characteristic polynomial

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

# Q4. Stationarity of ARIMA models

Suppose

$y_t = \beta_0 + \beta_1 t + \cdots + \beta_q t^q + x_t, \quad \beta_q\neq 0$

where $x_t$ is stationary.

Q4a. First, show that $\nabla^k x_t$ is stationary for any $k=1,2,\dots $.

**Answer:** Fill in

Q4b. Next show that $\nabla^k y_t$ is not stationary for $k < q$, but is stationary for $k \geq q$.

**Hint:** Use the following *Lemma*: For any integer $m \geq 0$, $\nabla t^m$ is a polynomial $t$ of degree $m-1$ (when $m\geq 1$), and $\nabla$ of a constant is 0.

**Answer:** Fill in

# Q5. Fitting an ARIMA model

Q5a. Fit an ARIMA($p,d,q$) model to the global temperature data `gtemp_land`, loaded from `astsa` as below. Perform all the necessary diagnostics for the model, and decide on an appropriate model. Comment on why you decided on the model.

```python
gtemp_land = astsa.load_gtemp_land()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Plot the data and diagnostics, decide on model
```

**Answer:** An ARIMA(0,1,1) should fit the data well. We know we need to do differencing because the original time series is not stationary (it has a trend / appears to be growing with time). After applying $d=1$ order differencing, we calculate the ACF and PACF and see a peak in the ACF and a slower tail off in the PACF, which suggests an MA term. The order of the MA term is found through the peak in the ACF (where it cuts off), which is 1.

Q5b. After deciding on the model, forecast (with 95% CI) the next 10 years, and comment on what you found. Hint: you should use `trend='t'` if using the ARIMA function from statsmodels. Also use the method `get_forecast` once you fit your model to perform the forecasting.

```python
model = ARIMA(## FILL IN...

fc = model.get_forecast(steps=10)

# Get mean and confidence intervals and print them
# FILL IN

# Plot the original data and the forecast including shaded confidence intervals.
```

# Q6. The covariance matrix $X^T X$ and time-lagged ridge regression

In the lecture on time lagged regression and in the lab, you saw an example of performing a regression using spectrogram features at multiple time lags as the inputs to a regression model. The figure below shows $X^T X$ for an 80-band spectrogram at 20 time delays. Columns are ordered frequency-fastest: the first 80 columns correspond to all 80 frequency bins at delay 0, the next 80 columns are all 80 frequency bins at delay 1, and so on.

Q6a. What does the value of `covmat[0,1]` represent (in words, in terms of frequency and delay)? What about `covmat[0,81]`? Next, describe two visible structural features of `covmat`. How would covmat look different if the spectrogram were white noise?

```python
# Run this cell to load and show the stimulus covariance matrix
import h5py
with h5py.File('covmat.hf5', 'r') as hf:
    covmat = hf['covmat'][:]

plt.imshow(covmat);
```

**Answer**: Write your answer to Q6a here.

Q6b. When we fit ridge regression, we penalize this matrix by adding a regularization term to the diagonal, i.e. $X^T X + \lambda I$. Recall that for ridge, the beta estimate is given by $\hat{\beta} = (X^T X + \lambda I)^-1 X^T y$. Looking at `covmat`, why is regularization especially important for this design matrix? Refer to the structural features you identified in Q6a.

**Answer:** Answer to Q6b.

---

[← Stat248 Homework4 Part 01 —](01-stat248-homework4-part-01.md) · [Up: contents](index.md)
