---
title: MA(1) and AR(1) model fitting via PyTorch
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# MA(1) and AR(1) model fitting via PyTorch

The algorithms from PyTorch can also be used to fit classical time series models. Here we illustrate how to fit MA(1) and AR(1) models.

We will use the varve dataset from Lecture 20.

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']

plt.figure(figsize = (12, 6))
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In Lecture 20, we took logarithms of this dataset, then differenced, and then fitted the MA(1) model. We will now fit this model (as well as AR(1)) using PyTorch (instead of ARIMA).

First let us recall how we fit this using ARIMA.

```python
ylogdiff = np.diff(np.log(yraw))
mamod_ARIMA = ARIMA(ylogdiff, order=(0, 0, 1)).fit()

print(mamod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Fri, 25 Apr 2025   AIC                            887.356
Time:                        10:50:24   BIC                            900.707
Sample:                             0   HQIC                           892.541
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0013      0.004     -0.280      0.779      -0.010       0.008
ma.L1         -0.7710      0.023    -33.056      0.000      -0.817      -0.725
sigma2         0.2353      0.012     18.881      0.000       0.211       0.260
===================================================================================
Ljung-Box (L1) (Q):                   9.16   Jarque-Bera (JB):                 7.58
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Below we describe the optimization problem that we need to solve in order to estimate the MA(1) parameters $\mu, \theta, \sigma$. Recall that the MA(1) model is given by
\begin{equation*}
  y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The likelihood is $f_{y_1, \dots, y_n}(y_1, \dots, y_n)$ can be written in terms of the covariance matrix of $y_1, \dots, y_n$. This is somewhat complicated. A simplification trick is to condition on $\epsilon = 0$, i.e., one attempts to write the conditional likelihood:
\begin{equation*}
   f_{y_1, \dots, y_n \mid \epsilon_0 = 0}(y_1, \dots, y_n).
\end{equation*}
This likelihood is much simpler to write by breaking it down as
\begin{equation*}
  f_{y_1 \mid \epsilon_0 = 0}(y_1) f_{y_2 \mid y_1, \epsilon_0 = 0}(y_2) f_{y_3 \mid y_1, y_2, \epsilon_0 = 0}(y_3) \dots f_{y_n \mid y_1, \dots, y_{n-1}, \epsilon_0 = 0}(y_n)
\end{equation*}
Each of the terms above can be written explicitly. Let $\hat{\epsilon}_1 = y_1 - \mu$ and, for $t = 2, \dots, n$,
\begin{equation*}
    \hat{\epsilon}_t = y_t- \mu - \theta \hat{\epsilon}_{t-1}
\end{equation*}
Then
\begin{equation*}
   f_{y_1 \mid \epsilon_0 = 0}(y_1) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right)
\end{equation*}
and
\begin{align*}
  f_{y_t \mid y_1, \dots, y_{t-1}, \epsilon = 0}(y_t) &= f_{y_t \mid \epsilon_1 = \hat{\epsilon}_1, \epsilon_2 = \hat{\epsilon}_2, \dots, \epsilon_{t-1} = \hat{\epsilon}_{t-1}, \epsilon_0 = 0}(y_t) \\
  &= f_{\epsilon_t}(y_t - \mu - \theta \hat{\epsilon}_{t-1}) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right).
\end{align*}
Thus the conditional likelihood given $\epsilon_0 = 0$ is given by
\begin{align*}
   \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right) \right] = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_1^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_t^2}{2 \sigma^2}  \right) \right]
\end{align*}
so that the negative log-likelihood  becomes:
\begin{align*}
   \frac{n}{2} \log (2 \pi) + 0.5 \sum_{t=1}^n \left(\log \sigma^2 + \frac{\hat{\epsilon}_t^2}{\sigma^2} \right).
\end{align*}

```python
class MA1Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mu = nn.Parameter(torch.tensor(0.0))  # initialized at 0
        self.theta = nn.Parameter(torch.tensor(0.0))  # initialized at 0
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma)

    def forward(self, y):
        n = len(y)
        eps_list = []
        eps_prev = y[0] - self.mu  # ε_0
        eps_list.append(eps_prev)
        for t in range(1, n):
            eps_t = y[t] - self.mu - self.theta * eps_prev
            eps_list.append(eps_t)
            eps_prev = eps_t
        eps = torch.stack(eps_list)

        sigma = torch.exp(self.log_sigma)
        nll = (0.5 * n * np.log(2 * np.pi)) + 0.5 * torch.sum(torch.log(sigma**2) + (eps**2) / (sigma**2))
        return nll
```

```python
ylogdiff_tensor = torch.tensor(ylogdiff, dtype=torch.float32)
```

```python
mamod = MA1Model()
```

```python
optimizer = optim.Adam(mamod.parameters(), lr=0.001)

for epoch in range(4000):
    # Zero gradient
    optimizer.zero_grad()

    # Compute loss
    loss = mamod(ylogdiff_tensor)

    # Compute gradient
    loss.backward()

    # Update parameters
    optimizer.step()

    if epoch % 100 == 0:
        sigma = torch.exp(mamod.log_sigma).item()
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}, mu: {mamod.mu.item():.4f}, "
              f"theta: {mamod.theta.item():.4f}, sigma: {sigma:.4f}")
```

```
Epoch 0, Loss: 686.6678, mu: -0.0010, theta: -0.0010, sigma: 0.9990
Epoch 100, Loss: 637.9557, mu: -0.0011, theta: -0.1006, sigma: 0.9050
Epoch 200, Loss: 593.8228, mu: -0.0011, theta: -0.1994, sigma: 0.8229
Epoch 300, Loss: 554.7609, mu: -0.0010, theta: -0.2977, sigma: 0.7518
Epoch 400, Loss: 521.1600, mu: -0.0010, theta: -0.3950, sigma: 0.6909
Epoch 500, Loss: 493.3359, mu: -0.0010, theta: -0.4902, sigma: 0.6394
Epoch 600, Loss: 471.5909, mu: -0.0011, theta: -0.5805, sigma: 0.5968
Epoch 700, Loss: 456.2418, mu: -0.0010, theta: -0.6599, sigma: 0.5624
Epoch 800, Loss: 447.1696, mu: -0.0011, theta: -0.7199, sigma: 0.5359
Epoch 900, Loss: 442.9311, mu: -0.0011, theta: -0.7544, sigma: 0.5167
Epoch 1000, Loss: 441.2652, mu: -0.0011, theta: -0.7682, sigma: 0.5038
Epoch 1100, Loss: 440.6577, mu: -0.0011, theta: -0.7719, sigma: 0.4956
Epoch 1200, Loss: 440.4542, mu: -0.0011, theta: -0.7727, sigma: 0.4907
Epoch 1300, Loss: 440.3932, mu: -0.0011, theta: -0.7728, sigma: 0.4880
Epoch 1400, Loss: 440.3770, mu: -0.0011, theta: -0.7728, sigma: 0.4865
Epoch 1500, Loss: 440.3733, mu: -0.0011, theta: -0.7728, sigma: 0.4858
Epoch 1600, Loss: 440.3724, mu: -0.0011, theta: -0.7728, sigma: 0.4854
Epoch 1700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4853
Epoch 1800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 1900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2300, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2400, Loss: 440.3724, mu: -0.0012, theta: -0.7728, sigma: 0.4852
Epoch 2500, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2600, Loss: 440.3723, mu: -0.0012, theta: -0.7728, sigma: 0.4852
Epoch 2700, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2900, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3300, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3400, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3500, Loss: 440.3723, mu: -0.0012, theta: -0.7728, sigma: 0.4852
Epoch 3600, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
```

The following code prints out the estimates given by this code, with the estimates given by the ARIMA function.

```python
ma1_pars = np.array([mamod.mu.detach().numpy(),
                     mamod.theta.detach().numpy(),
                     np.exp(2 * mamod.log_sigma.detach().numpy())])
# mu, theta and sigma^2

print(np.column_stack([mamod_ARIMA.params, ma1_pars]))
# the parameter estimates are quite close to each other
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
# Fit the model
armod = AR1Model()
optimizer = optim.Adam(armod.parameters(), lr=0.001)

for epoch in range(3000):
    # Zero gradient
    optimizer.zero_grad()

    # Compute loss
    loss = armod(ylogdiff_tensor)

    # Compute gradient
    loss.backward()

    # Update parameters
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: phi0={armod.phi0.item():.4f}, phi1={armod.phi1.item():.4f}, sigma={torch.exp(armod.log_sigma).item():.4f}, loss={loss.item():.4f}")
```

```
Epoch 0: phi0=-0.0010, phi1=0.4990, sigma=0.9990, loss=754.7678
Epoch 100: phi0=-0.0008, phi1=0.3977, sigma=0.9057, loss=708.1990
Epoch 200: phi0=-0.0009, phi1=0.2938, sigma=0.8257, loss=664.1494
Epoch 300: phi0=-0.0010, phi1=0.1895, sigma=0.7572, loss=623.2971
Epoch 400: phi0=-0.0011, phi1=0.0874, sigma=0.6989, loss=586.7548
Epoch 500: phi0=-0.0011, phi1=-0.0099, sigma=0.6502, loss=555.8716
Epoch 600: phi0=-0.0012, phi1=-0.0992, sigma=0.6108, loss=531.7949
Epoch 700: phi0=-0.0011, phi1=-0.1778, sigma=0.5804, loss=514.9111
Epoch 800: phi0=-0.0013, phi1=-0.2431, sigma=0.5587, loss=504.4892
Epoch 900: phi0=-0.0014, phi1=-0.2943, sigma=0.5445, loss=498.8905
Epoch 1000: phi0=-0.0014, phi1=-0.3318, sigma=0.5362, loss=496.2641
Epoch 1100: phi0=-0.0014, phi1=-0.3575, sigma=0.5318, loss=495.1721
Epoch 1200: phi0=-0.0014, phi1=-0.3742, sigma=0.5298, loss=494.7625
Epoch 1300: phi0=-0.0015, phi1=-0.3844, sigma=0.5289, loss=494.6224
Epoch 1400: phi0=-0.0014, phi1=-0.3904, sigma=0.5286, loss=494.5786
Epoch 1500: phi0=-0.0014, phi1=-0.3936, sigma=0.5285, loss=494.5660
Epoch 1600: phi0=-0.0014, phi1=-0.3954, sigma=0.5285, loss=494.5628
Epoch 1700: phi0=-0.0014, phi1=-0.3962, sigma=0.5285, loss=494.5621
Epoch 1800: phi0=-0.0015, phi1=-0.3967, sigma=0.5285, loss=494.5620
Epoch 1900: phi0=-0.0014, phi1=-0.3968, sigma=0.5285, loss=494.5618
Epoch 2000: phi0=-0.0014, phi1=-0.3969, sigma=0.5285, loss=494.5619
Epoch 2100: phi0=-0.0014, phi1=-0.3969, sigma=0.5285, loss=494.5619
Epoch 2200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2600: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
```

```python
ar1_pars = np.array([armod.phi0.detach().numpy(),
                     armod.phi1.detach().numpy(),
                     np.exp(2 * armod.log_sigma.detach().numpy())])
# mu, theta and sigma^2

print(np.column_stack([armod_ARIMA.params, ar1_pars]))
```

```
[[-0.00102183 -0.00127035]
 [-0.39696193 -0.39696154]
 [ 0.27927876  0.27927745]]
```

It is possible to extend these methods to fit AR($p$) and MA($q$) for more general $p$ and $q$ using PyTorch. The PyTorch seems to work just as well as ARIMA. In the above, the PyTorch seems to take much longer time but this is only because we are running the method for a few thousand epochs. The actual convergence seems to have happened much earlier.

---

[← Fitting Change of Slope Models via Pytorch: importance of scaling](01-fitting-change-of-slope-models-via-pytorch-importance-of-sca.md) · [Up: contents](index.md)
