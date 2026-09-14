---
title: First fix the number of knots
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# First fix the number of knots

**Source:** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

k = 4

quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_scaled, X).fit()

beta_init = md_init.params.values

print(knots_init)
print(beta_init)
```

```
[-1.03549894 -0.34516631  0.34516631  1.03549894]
[ 2.26579783  1.87350378 -4.48916248  4.49298465 -0.7894067   1.68596401]
```

Now the $\beta$ coefficients are of the same scale.

```python
md_nn = PiecewiseLinearModel(knots_init=knots_init, beta_init=beta_init)
```

```python
optimizer = optim.Adam(md_nn.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(20000):
    # Zero gradients
    optimizer.zero_grad()

    # Compute loss
    y_pred = md_nn(x_torch)
    loss = loss_fn(y_pred, y_torch)

    # Compute gradient
    loss.backward()

    # Update parameters
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

```
Epoch 0, Loss: 0.1118
Epoch 100, Loss: 0.0899
Epoch 200, Loss: 0.0809
Epoch 300, Loss: 0.0764
Epoch 400, Loss: 0.0739
Epoch 500, Loss: 0.0719
Epoch 600, Loss: 0.0704
Epoch 700, Loss: 0.0693
Epoch 800, Loss: 0.0684
Epoch 900, Loss: 0.0677
Epoch 1000, Loss: 0.0671
Epoch 1100, Loss: 0.0667
Epoch 1200, Loss: 0.0663
Epoch 1300, Loss: 0.0664
Epoch 1400, Loss: 0.0657
Epoch 1500, Loss: 0.0655
Epoch 1600, Loss: 0.0653
Epoch 1700, Loss: 0.0651
Epoch 1800, Loss: 0.0652
Epoch 1900, Loss: 0.0649
Epoch 2000, Loss: 0.0653
Epoch 2100, Loss: 0.0646
Epoch 2200, Loss: 0.0645
Epoch 2300, Loss: 0.0644
Epoch 2400, Loss: 0.0644
Epoch 2500, Loss: 0.0643
Epoch 2600, Loss: 0.0642
Epoch 2700, Loss: 0.0642
Epoch 2800, Loss: 0.0641
Epoch 2900, Loss: 0.0641
Epoch 3000, Loss: 0.0641
Epoch 3100, Loss: 0.0641
Epoch 3200, Loss: 0.0640
Epoch 3300, Loss: 0.0640
Epoch 3400, Loss: 0.0640
Epoch 3500, Loss: 0.0640
Epoch 3600, Loss: 0.0639
Epoch 3700, Loss: 0.0639
Epoch 3800, Loss: 0.0639
Epoch 3900, Loss: 0.0639
Epoch 4000, Loss: 0.0639
Epoch 4100, Loss: 0.0638
Epoch 4200, Loss: 0.0642
Epoch 4300, Loss: 0.0638
Epoch 4400, Loss: 0.0638
Epoch 4500, Loss: 0.0638
Epoch 4600, Loss: 0.0638
Epoch 4700, Loss: 0.0638
Epoch 4800, Loss: 0.0637
Epoch 4900, Loss: 0.0637
Epoch 5000, Loss: 0.0637
Epoch 5100, Loss: 0.0637
Epoch 5200, Loss: 0.0637
Epoch 5300, Loss: 0.0637
Epoch 5400, Loss: 0.0637
Epoch 5500, Loss: 0.0637
Epoch 5600, Loss: 0.0637
Epoch 5700, Loss: 0.0637
Epoch 5800, Loss: 0.0640
Epoch 5900, Loss: 0.0637
Epoch 6000, Loss: 0.0637
Epoch 6100, Loss: 0.0637
Epoch 6200, Loss: 0.0637
Epoch 6300, Loss: 0.0637
Epoch 6400, Loss: 0.0637
Epoch 6500, Loss: 0.0637
Epoch 6600, Loss: 0.0637
Epoch 6700, Loss: 0.0637
Epoch 6800, Loss: 0.0637
Epoch 6900, Loss: 0.0637
Epoch 7000, Loss: 0.0637
Epoch 7100, Loss: 0.0636
Epoch 7200, Loss: 0.0636
Epoch 7300, Loss: 0.0636
Epoch 7400, Loss: 0.0636
Epoch 7500, Loss: 0.0636
Epoch 7600, Loss: 0.0636
Epoch 7700, Loss: 0.0639
Epoch 7800, Loss: 0.0636
Epoch 7900, Loss: 0.0636
Epoch 8000, Loss: 0.0637
Epoch 8100, Loss: 0.0637
Epoch 8200, Loss: 0.0637
Epoch 8300, Loss: 0.0636
Epoch 8400, Loss: 0.0636
Epoch 8500, Loss: 0.0637
Epoch 8600, Loss: 0.0636
Epoch 8700, Loss: 0.0636
Epoch 8800, Loss: 0.0636
Epoch 8900, Loss: 0.0636
Epoch 9000, Loss: 0.0637
Epoch 9100, Loss: 0.0637
Epoch 9200, Loss: 0.0636
Epoch 9300, Loss: 0.0636
Epoch 9400, Loss: 0.0636
Epoch 9500, Loss: 0.0637
Epoch 9600, Loss: 0.0637
Epoch 9700, Loss: 0.0637
Epoch 9800, Loss: 0.0637
Epoch 9900, Loss: 0.0636
Epoch 10000, Loss: 0.0636
Epoch 10100, Loss: 0.0636
Epoch 10200, Loss: 0.0636
Epoch 10300, Loss: 0.0636
Epoch 10400, Loss: 0.0636
Epoch 10500, Loss: 0.0637
Epoch 10600, Loss: 0.0637
Epoch 10700, Loss: 0.0637
Epoch 10800, Loss: 0.0636
Epoch 10900, Loss: 0.0636
Epoch 11000, Loss: 0.0636
Epoch 11100, Loss: 0.0636
Epoch 11200, Loss: 0.0637
Epoch 11300, Loss: 0.0636
Epoch 11400, Loss: 0.0637
Epoch 11500, Loss: 0.0636
Epoch 11600, Loss: 0.0636
Epoch 11700, Loss: 0.0636
Epoch 11800, Loss: 0.0636
Epoch 11900, Loss: 0.0637
Epoch 12000, Loss: 0.0637
Epoch 12100, Loss: 0.0636
Epoch 12200, Loss: 0.0638
Epoch 12300, Loss: 0.0636
Epoch 12400, Loss: 0.0637
Epoch 12500, Loss: 0.0636
Epoch 12600, Loss: 0.0636
Epoch 12700, Loss: 0.0636
Epoch 12800, Loss: 0.0636
Epoch 12900, Loss: 0.0637
Epoch 13000, Loss: 0.0637
Epoch 13100, Loss: 0.0636
Epoch 13200, Loss: 0.0636
Epoch 13300, Loss: 0.0637
Epoch 13400, Loss: 0.0636
Epoch 13500, Loss: 0.0636
Epoch 13600, Loss: 0.0636
Epoch 13700, Loss: 0.0636
Epoch 13800, Loss: 0.0636
Epoch 13900, Loss: 0.0636
Epoch 14000, Loss: 0.0636
Epoch 14100, Loss: 0.0636
Epoch 14200, Loss: 0.0636
Epoch 14300, Loss: 0.0636
Epoch 14400, Loss: 0.0636
Epoch 14500, Loss: 0.0636
Epoch 14600, Loss: 0.0636
Epoch 14700, Loss: 0.0637
Epoch 14800, Loss: 0.0637
Epoch 14900, Loss: 0.0637
Epoch 15000, Loss: 0.0636
Epoch 15100, Loss: 0.0636
Epoch 15200, Loss: 0.0637
Epoch 15300, Loss: 0.0636
Epoch 15400, Loss: 0.0636
Epoch 15500, Loss: 0.0637
Epoch 15600, Loss: 0.0637
Epoch 15700, Loss: 0.0636
Epoch 15800, Loss: 0.0637
Epoch 15900, Loss: 0.0637
Epoch 16000, Loss: 0.0637
Epoch 16100, Loss: 0.0636
Epoch 16200, Loss: 0.0636
Epoch 16300, Loss: 0.0636
Epoch 16400, Loss: 0.0637
Epoch 16500, Loss: 0.0636
Epoch 16600, Loss: 0.0636
Epoch 16700, Loss: 0.0636
Epoch 16800, Loss: 0.0636
Epoch 16900, Loss: 0.0636
Epoch 17000, Loss: 0.0637
Epoch 17100, Loss: 0.0636
Epoch 17200, Loss: 0.0636
Epoch 17300, Loss: 0.0637
Epoch 17400, Loss: 0.0636
Epoch 17500, Loss: 0.0636
Epoch 17600, Loss: 0.0636
Epoch 17700, Loss: 0.0636
Epoch 17800, Loss: 0.0637
Epoch 17900, Loss: 0.0637
Epoch 18000, Loss: 0.0637
Epoch 18100, Loss: 0.0636
Epoch 18200, Loss: 0.0636
Epoch 18300, Loss: 0.0636
Epoch 18400, Loss: 0.0636
Epoch 18500, Loss: 0.0636
Epoch 18600, Loss: 0.0637
Epoch 18700, Loss: 0.0636
Epoch 18800, Loss: 0.0637
Epoch 18900, Loss: 0.0636
Epoch 19000, Loss: 0.0636
Epoch 19100, Loss: 0.0636
Epoch 19200, Loss: 0.0636
Epoch 19300, Loss: 0.0636
Epoch 19400, Loss: 0.0636
Epoch 19500, Loss: 0.0638
Epoch 19600, Loss: 0.0636
Epoch 19700, Loss: 0.0636
Epoch 19800, Loss: 0.0636
Epoch 19900, Loss: 0.0640
```

Now the convergence is much faster (after about 8000 iterations). Let us plot the fitted values on the original scale.

```python
nn_fits_with_scaling = md_nn(x_torch).detach().numpy()
nn_fits_with_scaling_original_scale = (nn_fits_with_scaling * np.std(y_raw)) + np.mean(y_raw)

plt.figure(figsize = (12, 6))
plt.plot(x_raw, y_raw, color = 'blue', label = 'Data')
plt.plot(x_raw, nn_fits_with_scaling_original_scale, color = 'green', label = 'PyTorch Fitted Values (With Scaling)')
plt.plot(x_raw, nn_fits, color = 'red', label = 'PyTorch Fitted Values (Without Scaling)')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is quite close to what we got by running the code on the original raw data. But the convergence of the algorithm is much faster with scaling. This is why scaling is almost always recommended.

## MA(1) and AR(1) model fitting via PyTorch

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

---

[← but is detached from the computation graph.](09-but-is-detached-from-the-computation-graph.md) · [Up: contents](index.md) · [mu, theta and sigma^2 →](11-mu-theta-and-sigma-2.md)
