---
title: Bone marrow transplant example
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/21_state_space_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/21_state_space_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Bone marrow transplant example

As an example, we can look at changes in different biomedical markers when a cancer patient undergoes a bone marrow transplant. We have three variables:

* log(white blood cell count) [WBC] (essential for immune function)
* log(platelet) [PLT] (essential for blood clotting)
* hematocrit [HCT] (percentage of red blood cells in total blood volume)

These three variables measure distinct aspects of bone marrow function. A transplant is successful when the new marrow is incorporated and starts producing all three of these.

Unfortunately, as is the case with many real-world datasets (especially those with longitudinal follow up), many data points are missing - approximately 40% in this case. The missing values mostly occur after the 35th day. We can use a state space approach to model these three variables and estimate the missing values. Prior work has shown that platelet count at 100 days post transplant is a good indicator of subsequent long term survival, so we may also want to look at this.

We can model these three variables using the state equation:

$$
\begin{aligned}
\begin{pmatrix}
x_{t1} \\
x_{t2} \\
x_{t3}
\end{pmatrix}
&=&
\begin{pmatrix}
\phi_{11} & \phi_{12} & \phi_{13} \\
\phi_{21} & \phi_{22} & \phi_{23}\\
\phi_{31} & \phi_{32} & \phi_{33}\\
\end{pmatrix}
\begin{pmatrix}
x_{t-1,1} \\
x_{t-1,2} \\
x_{t-1,3} \\
\end{pmatrix} +
\begin{pmatrix}
w_{t1}\\
w_{t2}\\
w_{t3}\\
\end{pmatrix}
\end{aligned}
$$

The diagonal values of the $\Phi$ matrix give you how much each marker's own recent value predicts its next value. For example, $\phi_{11}$ near 1 means the marker WBC is highly persistent and changes slowly from day to day. On the other hand a value near 0 would indicate today's value has little to do with yesterday (which would be strange for blood markers and might signal a problem with the data collection).

The off-diagonal entries $\phi_{ij}$ are coefficients that show how much yesterdays value of marker $j$ predicts today's value of marker $i$. The matrices thus represent three stacked regressions, for example:

$x_{t1} = \phi_{11} x_{t-1,1} + \phi_{12} x_{t-1, 2} + \phi_{13} x_{t-1,3} + w_{t1}$

Meaning today's log(WBC) value is a weighted sum of yesterday's WBC, platelets, and hematocrit, plus some noise.

* $\phi_{11}$ is the effect of component 1 yesterday on component 1 today
* $\phi_{12}$ is the effect of component 2 yesterday on component 1 today
* $\phi_{13}$ is the effect of component 3 yesterday on component 1 today
* $\phi_{21}$ is the effect of component 1 yesterday on component 2 today
* $\phi_{22}$ is the effect of component 2 yesterday on component 2 today

We then have the observation equations $y_t = A_t x_t + v_t$, where the $3 \times 3$ matrix $A_t$ is either the identity matrix or zero matrix depending on whether a blood sample was taken on that day.

For such a model, we would fit the unknown values through expectation maximization (EM) or through maximum likelihood methods:

* $\Phi$ - $(3 \times 3)$ matrix, 9 parameters
* $Q$ - $(3 \times 3)$ symmetric state noise covariance matrix (so only 6 parameters, diagonals and one set of off-diagonals)
* $R$ - $(3 \times 3)$ symmetric observation noise covariance matrix (so only 6 parameters, diagonals and one set of off-diagonals - often assumed diagonal)
* $\mu_0, \sigma_0$: mean and covariance of initial state $x_0$ ($3+6=9$ parameters - may be fixed according to some prior)
* $A$ - usually fixed as $I$, but may be fit

In python, we can use `statsmodels.tsa.statespace` to fit these models.

## Filtering, smoothing, and forecasting

For state space models, we want to estimate our underlying unobserved signal $x_t$ given the data $y_{1:s} = {y_1, \dots, y_s}$ to time $s$. In practice, the steps for the state space models include:

1. Filtering, where we estimate $x_t$ using measurements up through time $t$ (here $s$=$t$)
2. Prediction/forecasting, where we have $st$. This allows us to estimate $x_t$ using the entire dataset, including observations after $t$. This can be used to better estimate missing values.

## Other examples

* Estimating global warming/global temperatures $x_t$ from land and sea temperature measurements $y_t$
* Brain computer interfaces (BCI) - we want to infer intended cursor velocity ($x_t$) from brain measurements from 100 electrodes in motor cortex $y_t$
* Health - we want to estimate true blood glucose level $x_t$ from $y_t$ intermittent measurements from a continuous glucose monitor with some sensor drift.
* Finance - we want to measure volatility $x_t$ of the S&P500 on day $t$, we observe $y_t$ daily log returns

## Advantages of state space models

What are the advantages of state space models as opposed to other models we've discussed in this class?

1. They deal well with missing data and don't require every time point to be observed. You can still get estimates of the latent state for those missing time points.
2. We can separate process noise from measurement noise. In ARIMA models, we have just one noise term (innovations/shocks). For real scientific applications, we may have noisy sensors where the measurement reading's error is distinct from underlying noise in the true signal.
3. We can have time-varying parameters (unlike fixed $\beta$ in a regression model).

---

[← Linear Gaussian Model](02-linear-gaussian-model.md) · [Up: contents](index.md)
