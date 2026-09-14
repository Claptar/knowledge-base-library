---
title: Preprocessing using logarithms and differences
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwenty153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing using logarithms and differences

**Source:** [`CodeLectureTwenty153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

If we want to fit stationary AR models to this GNP dataset, we can first preprocess the data by taking logarithms, and then by taking differences of the logarithms. Note that differenced log data (multiplied by 100) leads to percentage change interpretation. In other words, $100 \left(\log \text{GNP}_t - \log \text{GNP}_{t-1} \right)$ represents the percent change in GNP from one quarter to the next.

Here is a plot of the logarithms of the data.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of GNP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we take differences and multiply by 100.

```python
ylogdiff = (np.diff(np.log(y))) * 100
plt.plot(ylogdiff, color = 'black')
plt.title('Diff(Log(Quarterly GNP))')
plt.ylabel('Value')
plt.xlabel('Quarter')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us fit AR(1) to this log-differenced data.

```python
armd_logdiff = AutoReg(ylogdiff, lags = 1).fit()
print(armd_logdiff.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                     AutoReg(1)   Log Likelihood                -512.052
Method:               Conditional MLE   S.D. of innovations              1.249
Date:                Fri, 07 Nov 2025   AIC                           1030.104
Time:                        15:11:31   BIC                           1041.333
Sample:                             1   HQIC                          1034.591
                                  313
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.1596      0.110     10.519      0.000       0.943       1.376
y.L1           0.2487      0.055      4.536      0.000       0.141       0.356
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            4.0208           +0.0000j            4.0208            0.0000
-----------------------------------------------------------------------------
```

This fitted AR(1) clearly has $|\hat{\phi}_1| < 1$ so it corresponds to a causal-stationary regime.

### Causal Stationarity for AR($p$) with $p \geq 2$

When $p \geq 2$, causal-stationarity is determined by the roots of the AR polynomial $\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p$. Specifically, the AR($p$) is causal stationary if every root of the AR polynomial has modulus strictly larger than 1.

For our first example, consider the AR(1) model that we fitted to the data $y_t = 100 \left(\log \text{GNP}_t - \log \text{GNP}_{t-1} \right)$. This model is:
\begin{align*}
    y_t = 1.1596 + 0.2487 y_{t-1} + \epsilon_t.
\end{align*}
This is AR(1) with $\phi_1$ coefficient 0.2487 which has magnitude strictly smaller than 1. So it is a causal stationary model. We can also rewrite this model as:
\begin{align*}
   100 \left( \log \text{GNP}_t - \log \text{GNP}_{t-1}\right) = 1.1596 + 24.87 \left( \log \text{GNP}_{t-1} - \log \text{GNP}_{t-2} \right) + \epsilon_t.
\end{align*}
If $G_t := 100 \log \text{GNP}_t$, then the above model in terms of $G_t$ becomes:
\begin{align*}
    G_t - G_{t-1} = 1.1596 + 0.2487 \left(G_{t-1} - G_{t-2} \right) + \epsilon_t
\end{align*}
which is equivalen to
\begin{align*}
    G_t = 1.1596 + 1.2487 G_{t-1} - 0.2487 G_{t-2} + \epsilon_t.
\end{align*}
This is an AR(2) model and we can ask whether this AR(2) model is causal stationary. For this, we need to calculate the roots of the AR(2) polynomial:
\begin{align*}
   1 - 1.1487 z - 0.2487 z^2.
\end{align*}
Its roots are given by
\begin{align*}
   \frac{1.1487 \pm \sqrt{1.1487^2 + 4 \times 0.2487}}{2 \times (-0.2487)}
\end{align*}
These can be computed in python as follows.

```python
coeffs = [-0.2487, -1.1487, 1]
roots = np.roots(coeffs) #these are roots of the quadratic
print(roots)
#The magnitudes of the roots are calculated as:
print(np.abs(roots))
```

```
[-5.3678854   0.74906754]
[5.3678854  0.74906754]
```

One of the roots has magnitude strictly larger than 1, while the other has magnitude strictly smaller than 1. Hence this AR(2) model is not causal-stationary. This makes sense because this AR(2) model is for $G_t = 100 \log \text{GNP}_t$ which is predominantly an increasing dataset. So we cannot expect a stationary model for this data.

When we fit an AR($p$) model using AutoReg, the summary displays roots of the corresponding fitted AR polynomial along with their moduli. If all moduli are strictly larger than 1, then the model is causal stationary.

Below we fit an AR($p$) model with $p \geq 2$ to the percent change (100 times differences of logs) GNP dataset.

```python
p = 2
armd_logdiff = AutoReg(ylogdiff, lags = p).fit()
print(armd_logdiff.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                     AutoReg(2)   Log Likelihood                -504.061
Method:               Conditional MLE   S.D. of innovations              1.224
Date:                Fri, 07 Nov 2025   AIC                           1016.123
Time:                        15:41:21   BIC                           1031.082
Sample:                             2   HQIC                          1022.102
                                  313
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.9181      0.126      7.292      0.000       0.671       1.165
y.L1           0.1971      0.055      3.553      0.000       0.088       0.306
y.L2           0.2077      0.056      3.742      0.000       0.099       0.317
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.7704           +0.0000j            1.7704            0.0000
AR.2           -2.7192           +0.0000j            2.7192            0.5000
-----------------------------------------------------------------------------
```

Note that the moduli are both strictly larger than 1, so this is a causal stationary AR model. Note that this model is for the percent changes of GNP (and not for GNP or log(GNP) directly).

---

[← AR(p) Models and Stationarity](01-ar-p-models-and-stationarity.md) · [Up: contents](index.md) · [How to determine the order of $p$ for AR(p) →](03-how-to-determine-the-order-of-for-ar-p.md)
