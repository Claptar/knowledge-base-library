---
title: 'Model 4: Modeling growth rate'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model 4: Modeling growth rate

This model directly works with the monthly growth rates (defined by $g_t$ below) as opposed to working with $y_t$ or $\log y_t$.
\begin{align*}
   g_t = \log y_t - \log y_{t-1}.
\end{align*}
Our model is:
\begin{align*}
   g_t = \beta_0 + \beta_1 t + \epsilon_t
\end{align*}

The key point is that forecasting the growth rates forces the future
population path to be built starting from the last observed population
value.

Suppose the last observed population is $y_n$, corresponding to July
2026. Since
\begin{align*}
    g_t = \log y_t - \log y_{t-1},
\end{align*}
we can rewrite this as
\begin{align*}
    \log y_t = \log y_{t-1} + g_t.
\end{align*}

After fitting the model
\begin{align*}
    g_t = \beta_0 + \beta_1 t + \epsilon_t,
\end{align*}
the forecast for the next month's growth rate is
\begin{align*}
    \widehat{g}_{n+1}
    =
    \widehat{\beta}_0
    +
    \widehat{\beta}_1(n+1).
\end{align*}

The August 2026 population forecast is then constructed as
\begin{align*}
    \log \widehat{y}_{n+1}
    =
    \log y_n + \widehat{g}_{n+1},
\end{align*}
or equivalently,
\begin{align*}
    \widehat{y}_{n+1}
    =
    y_n \exp\left(\widehat{g}_{n+1}\right).
\end{align*}

Thus, the forecast explicitly starts from the observed July 2026
population $y_n$. Since monthly population growth rates are typically
quite small, $\exp(\widehat{g}_{n+1})$ will usually be close to $1$.
Consequently,
\begin{align*}
    \widehat{y}_{n+1} \approx y_n,
\end{align*}
with the difference corresponding to approximately one month's
predicted population growth.

For forecasts further into the future, we have
\begin{align*}
    \log \widehat{y}_{n+h}
    =
    \log y_n
    +
    \sum_{j=1}^{h} \widehat{g}_{n+j},
\end{align*}
and therefore
\begin{align*}
    \widehat{y}_{n+h}
    =
    y_n
    \exp\left(
        \sum_{j=1}^{h} \widehat{g}_{n+j}
    \right).
\end{align*}

Thus, every future forecast is anchored at the last observed population
value $y_n$.

By contrast, if we directly fit a model such as
\begin{align*}
    y_t = \beta_0 + \beta_1 t + \epsilon_t
\end{align*}
or
\begin{align*}
    \log y_t = \beta_0 + \beta_1 t + \epsilon_t,
\end{align*}
the fitted regression line is not required to pass through the final
observation $y_n$. Consequently, the extrapolated value at time $n+1$
can lie noticeably above or below the last observed population value.
This can create an artificial-looking jump between the last observation
and the first prediction.

The growth-rate model avoids this problem because the August 2026
forecast is obtained by starting with the actual July 2026 population
and applying exactly one month's predicted growth. Notice that the model
does not force the August prediction to equal the July population.
Rather, it forces the forecast to start from the July population and
then evolve according to the predicted monthly growth rates.

The code below fits this linear regression model on the growth rates.

```python
g = np.diff(ylog)
x = np.arange(1, len(g) + 1)
X = np.column_stack([np.ones(len(g)), x])
md4 = sm.OLS(g, X).fit()
print(md4.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.448
Model:                            OLS   Adj. R-squared:                  0.448
Method:                 Least Squares   F-statistic:                     656.5
Date:                Tue, 01 Sep 2026   Prob (F-statistic):          1.91e-106
Time:                        19:31:00   Log-Likelihood:                 5735.4
No. Observations:                 810   AIC:                        -1.147e+04
Df Residuals:                     808   BIC:                        -1.146e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0011   1.43e-05     79.733      0.000       0.001       0.001
x1         -7.846e-07   3.06e-08    -25.622      0.000   -8.45e-07   -7.24e-07
==============================================================================
Omnibus:                      115.141   Durbin-Watson:                   0.135
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              411.500
Skew:                           0.643   Prob(JB):                     4.40e-90
Kurtosis:                       6.246   Cond. No.                         937.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

Below we plot the fitted values on the growth rates data $g_t$.

```python
#Plotting growth rates and fitted values:
plt.figure(figsize=(6, 4))
plt.plot(g, label = "growth rates")
plt.plot(md4.fittedvalues, label = "fitted values")
plt.xlabel("Time (monthly)")
plt.ylabel("Growth rates")
plt.title("Growth Rates of the Log Population with fitted values")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There is a clear declining trend on the growth rates that is captured by the fitted regression line. There is a richer structure in the growth rates though which the single regression line does not fully capture; so there is a scope for more sophisticated models that can be fit to the growth rates data.

Below are the residuals obtained after fitting the regression line to the growth rates.

```python
#Plotting residuals:
plt.figure(figsize=(6, 4))
plt.plot(md4.resid, label = "residuals")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the Growth Rate Model")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are still some linear patterns in these residuals which can be potentially explained by more sophisticated models.

Here is the prediction for this model for the population in July 2040.

```python
n = len(ylog)
x_future = np.arange(n, n + 168)
X_future = np.column_stack([np.ones(168), x_future])

g_pred = md4.predict(X_future)
y_pred = y.iloc[-1] * np.exp(g_pred.sum())

print(y_pred)
```

```
369282.4340955185
```

This prediction is closer to the United Nations projection of 370.209 million.

Below is the plot of the predictions along with the observed dataset. It can be clearly seen that there is no jump between where the observed data ends and the predictions start.

```python
y_future_md4 = y.iloc[-1] * np.exp(np.cumsum(g_pred))

plt.plot(np.arange(n), y, label="Observed")
plt.plot(np.arange(n, n + 168), y_future_md4, label="Predicted", color = 'red')

plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$](04-model-3.md) · [Up: contents](index.md) · [Model 5: $gt = \beta0 + \beta1 t + \beta2 (t - c)+ + \epsilont$. →](06-model-5.md)
