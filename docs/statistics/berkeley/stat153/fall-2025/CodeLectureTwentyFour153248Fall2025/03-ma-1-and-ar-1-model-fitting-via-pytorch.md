---
title: MA(1) and AR(1) model fitting via PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# MA(1) and AR(1) model fitting via PyTorch

## MA(1) model fitting

The algorithms from PyTorch can also be used to fit classical time series models. Here we illustrate how to fit MA(1) and AR(1) models. We will use the varve dataset from Lecture 21.

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

In Lecture 20, we took logarithms of this dataset, then differenced, and then fitted the MA(1) model. We will now fit this model (as well as AR(1)) using PyTorch (instead of ARIMA).  First let us recall how we fit this using the ARIMA function.

```python
from statsmodels.tsa.arima.model import ARIMA
ylogdiff = np.diff(np.log(yraw))
mamod_ARIMA = ARIMA(ylogdiff, order = (0, 0, 1)).fit()
print(mamod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Tue, 25 Nov 2025   AIC                            887.356
Time:                        16:16:54   BIC                            900.707
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

We next fit the MA(1) model using PyTorch. Below we describe the optimization problem that we need to solve in order to estimate the MA(1) parameters $\mu, \theta, \sigma$. Recall that the MA(1) model is given by
\begin{equation*}
  y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The likelihood is $f_{y_1, \dots, y_n}(y_1, \dots, y_n)$ can be written in terms of the covariance matrix of $y_1, \dots, y_n$. This is somewhat complicated. A simplification trick is to condition on $\epsilon = 0$ i.e., one attempts to write the conditional likelihood:
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
        self.mu = nn.Parameter(torch.tensor(0.0)) #initialized at 0
        self.theta = nn.Parameter(torch.tensor(0.0)) #initialized at 0
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma)

    def forward(self, y): #this function computes the negative log-likelihood given data y
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
ylogdiff_tensor = torch.tensor(ylogdiff, dtype = torch.float32)
mamod = MA1Model()
optimizer = optim.Adam(mamod.parameters(), lr=0.001)
for epoch in range(4000):
    optimizer.zero_grad()
    loss = mamod(ylogdiff_tensor)
    loss.backward()
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
Epoch 400, Loss: 521.1600, mu: -0.0011, theta: -0.3950, sigma: 0.6909
Epoch 500, Loss: 493.3359, mu: -0.0010, theta: -0.4902, sigma: 0.6394
Epoch 600, Loss: 471.5910, mu: -0.0010, theta: -0.5805, sigma: 0.5968
Epoch 700, Loss: 456.2417, mu: -0.0011, theta: -0.6599, sigma: 0.5624
Epoch 800, Loss: 447.1696, mu: -0.0011, theta: -0.7199, sigma: 0.5359
Epoch 900, Loss: 442.9311, mu: -0.0011, theta: -0.7544, sigma: 0.5167
Epoch 1000, Loss: 441.2652, mu: -0.0011, theta: -0.7682, sigma: 0.5038
Epoch 1100, Loss: 440.6577, mu: -0.0012, theta: -0.7719, sigma: 0.4956
Epoch 1200, Loss: 440.4542, mu: -0.0012, theta: -0.7727, sigma: 0.4907
Epoch 1300, Loss: 440.3933, mu: -0.0011, theta: -0.7728, sigma: 0.4880
Epoch 1400, Loss: 440.3770, mu: -0.0011, theta: -0.7728, sigma: 0.4865
Epoch 1500, Loss: 440.3732, mu: -0.0011, theta: -0.7728, sigma: 0.4858
Epoch 1600, Loss: 440.3724, mu: -0.0011, theta: -0.7728, sigma: 0.4854
Epoch 1700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4853
Epoch 1800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 1900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2300, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2400, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2500, Loss: 440.3723, mu: -0.0012, theta: -0.7728, sigma: 0.4852
Epoch 2600, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2800, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2900, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3300, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3400, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3500, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3600, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
```

The following code prints out the estimates given by this code, along with the estimates given by the ARIMA function.

```python
ma1_pars = np.array([mamod.mu.detach().numpy(), mamod.theta.detach().numpy(), np.exp(2*mamod.log_sigma.detach().numpy())]) #mu, theta and sigma^2
print(np.column_stack([mamod_ARIMA.params, ma1_pars]))
#the parameter estimates are quite close to each other
```

```
[[-0.00125667 -0.0011363 ]
 [-0.77099236 -0.77283096]
 [ 0.23528045  0.23539422]]
```

## AR(1) model fitting

Next let us fit the AR(1) model using PyTorch. Note that the full likelihood in the AR(1) model (stationary case) is given by (see Equation (7) in the notes for Lecture 17):
\begin{align*}
\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2 \pi}
      \sigma} \exp \left(-\frac{1 - \phi_1^2}{2 \sigma^2} \left(y_1 -
        \frac{\phi_0}{1 - \phi_1} \right)^2 \right) \left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n (y_t -
    \phi_0 - \phi_1 y_{t-1})^2 \right).
\end{align*}
Below we first fit AR(1) using ARIMA, and then fit it by maximizing the log of the likelihood written above.

```python
armod_ARIMA = ARIMA(ylogdiff, order = (1, 0, 0)).fit()
print(armod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(1, 0, 0)   Log Likelihood                -494.562
Date:                Tue, 25 Nov 2025   AIC                            995.124
Time:                        16:20:33   BIC                           1008.475
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
        #If the model is non-stationary, return infinite negative log-likelihood (and None for log-likelihood)
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

        log_likelihood = part1 + part2 + part3 + part4 + part5
        negative_log_likelihood = -log_likelihood  # because we minimize

        return negative_log_likelihood, log_likelihood
```

```python
# Fit the model
armod = AR1Model()
optimizer = optim.Adam(armod.parameters(), lr=0.001)

for epoch in range(4000):
    loss, loglike = armod(ylogdiff_tensor)
    optimizer.zero_grad() #removes previously calculated gradients
    loss.backward() #calculates gradients
    optimizer.step() #updates parameters using gradients

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: phi0={armod.phi0.item():.4f}, phi1={armod.phi1.item():.4f}, sigma={torch.exp(armod.log_sigma).item():.4f}, loss={loss.item():.4f}")
```

```
Epoch 0: phi0=-0.0010, phi1=-0.0010, sigma=0.9990, loss=686.6678
Epoch 100: phi0=-0.0012, phi1=-0.0996, sigma=0.9050, loss=638.2626
Epoch 200: phi0=-0.0013, phi1=-0.1913, sigma=0.8231, loss=595.9210
Epoch 300: phi0=-0.0013, phi1=-0.2703, sigma=0.7529, loss=561.3080
Epoch 400: phi0=-0.0014, phi1=-0.3307, sigma=0.6942, loss=535.2979
Epoch 500: phi0=-0.0014, phi1=-0.3691, sigma=0.6464, loss=517.4683
Epoch 600: phi0=-0.0014, phi1=-0.3880, sigma=0.6091, loss=506.3111
Epoch 700: phi0=-0.0014, phi1=-0.3948, sigma=0.5812, loss=499.9816
Epoch 800: phi0=-0.0014, phi1=-0.3965, sigma=0.5612, loss=496.7854
Epoch 900: phi0=-0.0014, phi1=-0.3969, sigma=0.5478, loss=495.3693
Epoch 1000: phi0=-0.0014, phi1=-0.3969, sigma=0.5393, loss=494.8214
Epoch 1100: phi0=-0.0014, phi1=-0.3969, sigma=0.5342, loss=494.6358
Epoch 1200: phi0=-0.0014, phi1=-0.3970, sigma=0.5313, loss=494.5806
Epoch 1300: phi0=-0.0014, phi1=-0.3970, sigma=0.5298, loss=494.5661
Epoch 1400: phi0=-0.0014, phi1=-0.3970, sigma=0.5291, loss=494.5627
Epoch 1500: phi0=-0.0014, phi1=-0.3970, sigma=0.5287, loss=494.5620
Epoch 1600: phi0=-0.0014, phi1=-0.3970, sigma=0.5286, loss=494.5619
Epoch 1700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 1800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 1900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2000: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2100: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2600: phi0=-0.0015, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3000: phi0=-0.0015, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3100: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3600: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
```

```python
ar1_pars = np.array([armod.phi0.detach().numpy(), armod.phi1.detach().numpy(), np.exp(2*armod.log_sigma.detach().numpy())]) #mu, theta and sigma^2
print(np.column_stack([armod_ARIMA.params, ar1_pars]))
```

```
[[-0.00102183 -0.00142138]
 [-0.39696193 -0.39696237]
 [ 0.27927876  0.27927739]]
```

It is possible to extend these methods to fit AR($p$) and MA($q$) for more general $p$ and $q$ using PyTorch. The PyTorch method seems to work just as well as ARIMA. Note that the AR code works much faster than the MA code. This is because the it takes longer to write the likelihood for the MA model comapared to the AR model.

---

← Adding a Regularizer · [Up: contents](index.md) · Nonlinear AutoRegression →
