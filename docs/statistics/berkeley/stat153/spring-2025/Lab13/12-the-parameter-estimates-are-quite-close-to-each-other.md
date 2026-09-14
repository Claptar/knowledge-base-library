---
title: the parameter estimates are quite close to each other
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# the parameter estimates are quite close to each other

**Source:** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
[[-0.00125667 -0.00113865]
 [-0.77099236 -0.77283102]
 [ 0.23528045  0.23539422]]
```

Next let us fit the AR(1) model using PyTorch. Note that the full likelihood in the AR(1) model (stationary case) is given by (see Equation (6) in the notes for Lecture 17):
\begin{align*}
\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2 \pi}
      \sigma} \exp \left(-\frac{1 - \phi_1^2}{2 \sigma^2} \left(y_1 -
        \frac{\phi_0}{1 - \phi_1} \right)^2 \right) \left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n (y_t -
    \phi_0 - \phi_1 y_{t-1})^2 \right).
\end{align*}

Below we first fit AR(1) using ARIMA, and then fit it by maximizing the log of the likelihood written above.

```python
armod_ARIMA = ARIMA(ylogdiff, order=(1, 0, 0)).fit()
print(armod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(1, 0, 0)   Log Likelihood                -494.562
Date:                Fri, 25 Apr 2025   AIC                            995.124
Time:                        10:52:14   BIC                           1008.475
Sample:                             0   HQIC                          1000.309
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0010      0.015     -0.067      0.946      -0.031       0.029
ar.L1         -0.3970      0.036    -10.989      0.000      -0.468      -0.326
sigma2         0.2793      0.015     18.916      0.000       0.250       0.308
===================================================================================
Ljung-Box (L1) (Q):                   5.88   Jarque-Bera (JB):                 5.22
Prob(Q):                              0.02   Prob(JB):                         0.07
Heteroskedasticity (H):               0.77   Skew:                            -0.17
Prob(H) (two-sided):                  0.05   Kurtosis:                         3.29
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
class AR1Model(nn.Module):
    def __init__(self):
        super().__init__()
        # Learnable parameters: phi0 (intercept), phi1 (AR coefficient), log_sigma (for positivity)
        self.phi0 = nn.Parameter(torch.tensor(0.0))
        self.phi1 = nn.Parameter(torch.tensor(0.0))
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma) to ensure sigma > 0

    def forward(self, y):
        n = len(y)
        sigma = torch.exp(self.log_sigma)
        phi0 = self.phi0
        phi1 = self.phi1

        if torch.abs(phi1) >= 1:
            return torch.tensor(float("inf")), None

        # Stationary mean of y_1
        y1_mean = phi0 / (1 - phi1)

        # Compute log-likelihood parts
        part1 = -0.5 * n * torch.log(torch.tensor(2 * torch.pi))
        part2 = -n * torch.log(sigma)
        part3 = 0.5 * torch.log(1 - phi1**2)
        part4 = - (1 - phi1**2) / (2 * sigma**2) * (y[0] - y1_mean)**2
        part5 = - (1 / (2 * sigma**2)) * torch.sum((y[1:] - phi0 - phi1 * y[:-1])**2)

        negative_log_likelihood = -(part1 + part2 + part3 + part4 + part5)

        return negative_log_likelihood
```

```python

---

[← mu, theta and sigma^2](11-mu-theta-and-sigma-2.md) · [Up: contents](index.md) · [Fit the model →](13-fit-the-model.md)
