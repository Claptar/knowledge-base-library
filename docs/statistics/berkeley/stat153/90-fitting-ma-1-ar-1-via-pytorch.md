---
title: "90. Fitting MA(1)/AR(1) via PyTorch"
course: "Berkeley Stat 153 Fall 2024"
chapter: 90
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 90. Fitting MA(1)/AR(1) via PyTorch

## What this covers

Every model fit so far in the course has come from a canned routine — `ARIMA(...).fit()` — that
returns parameter estimates without showing how they were found. This chapter opens that routine
up for two of the simplest ARMA models, MA(1) and AR(1): it writes down the Gaussian likelihood by
hand, turns it into a loss function, and minimises that loss by gradient descent (using PyTorch's
automatic differentiation and the Adam optimiser) instead of calling `ARIMA`. It assumes the reader
already knows the MA(1) and AR(1) model definitions, stationarity, and has previously fit these
models to the glacial varve data with `statsmodels`' `ARIMA` (as in the lecture this lab points
back to).

## Recap: fitting MA(1) with ARIMA

The running example is the glacial varve thickness series. As in the earlier lecture, the raw
series is log-transformed and then differenced,
$$y_t = \log(x_t) - \log(x_{t-1}),$$
and an MA(1) model is fit to the differenced series $y_t = \mu + \epsilon_t + \theta\epsilon_{t-1}$
with `ARIMA(ylogdiff, order=(0,0,1))`. That fit gives

| parameter | ARIMA estimate |
|---|---|
| $\mu$ | $-0.0013$ |
| $\theta$ | $-0.7710$ |
| $\sigma^2$ | $0.2353$ |

These numbers are the target the hand-built optimiser below has to reproduce.

## The conditional likelihood trick for MA(1)

The MA(1) model is $y_t = \mu + \epsilon_t + \theta\epsilon_{t-1}$ with
$\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$. Writing down the exact joint density
$f_{y_1,\dots,y_n}(y_1,\dots,y_n)$ means writing down the covariance matrix of
$y_1,\dots,y_n$ induced by the moving-average structure, which is a fully populated (Toeplitz)
matrix, not diagonal — every $y_t$ is correlated with $y_{t-1}$ through the shared $\epsilon_{t-1}$.
That is more machinery than is needed.

The simplification is to **condition on $\epsilon_0 = 0$** and work with

$$f_{y_1,\dots,y_n \mid \epsilon_0=0}(y_1,\dots,y_n)$$

instead of the unconditional joint density. Conditioning on $\epsilon_0$ lets the joint density be
factored by the chain rule into a product of one-step-ahead conditionals,

$$f_{y_1\mid \epsilon_0=0}(y_1)\, f_{y_2\mid y_1,\epsilon_0=0}(y_2)\, f_{y_3 \mid y_1,y_2,\epsilon_0=0}(y_3) \cdots f_{y_n \mid y_1,\dots,y_{n-1},\epsilon_0=0}(y_n),$$

and each factor is a *simple* Gaussian, because knowing $y_1,\dots,y_{t-1}$ and $\epsilon_0=0$ pins
down every innovation up to time $t-1$ exactly. Define $\hat\epsilon_1 = y_1 - \mu$ and, recursively
for $t=2,\dots,n$,
$$\hat\epsilon_t = y_t - \mu - \theta\,\hat\epsilon_{t-1}.$$
Then
$$f_{y_1\mid \epsilon_0=0}(y_1) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{(y_1-\mu)^2}{2\sigma^2}\right)$$
and, for $t\ge 2$,
$$f_{y_t\mid y_1,\dots,y_{t-1},\epsilon_0=0}(y_t) = f_{\epsilon_t}\big(y_t-\mu-\theta\hat\epsilon_{t-1}\big) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{1}{2\sigma^2}\big(y_t-\mu-\theta\hat\epsilon_{t-1}\big)^2\right).$$

Multiplying all $n$ factors and taking $-\log$ of the product gives a negative log-likelihood with
no covariance matrix in it at all:
$$-\log f = \frac{n}{2}\log(2\pi) + \frac12\sum_{t=1}^n \left(\log\sigma^2 + \frac{\hat\epsilon_t^2}{\sigma^2}\right).$$

<figure>
<svg viewBox="0 0 640 200" role="img" aria-label="Chain of residuals produced by the MA(1) conditioning trick">
  <defs>
    <marker id="arrow-ma1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>
  <text x="220" y="45" text-anchor="middle" font-size="13" fill="currentColor">y&#8321;</text>
  <text x="380" y="45" text-anchor="middle" font-size="13" fill="currentColor">y&#8322;</text>
  <text x="540" y="45" text-anchor="middle" font-size="13" fill="currentColor">y&#8323;</text>
  <text x="600" y="45" text-anchor="middle" font-size="13" fill="currentColor">&#8943;</text>
  <line x1="220" y1="60" x2="220" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <line x1="380" y1="60" x2="380" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <line x1="540" y1="60" x2="540" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <text x="60" y="155" text-anchor="middle" font-size="12" fill="currentColor">&#603;&#772;&#8320;=0</text>
  <text x="220" y="155" text-anchor="middle" font-size="12" fill="currentColor">&#603;&#772;&#8321;</text>
  <text x="380" y="155" text-anchor="middle" font-size="12" fill="currentColor">&#603;&#772;&#8322;</text>
  <text x="540" y="155" text-anchor="middle" font-size="12" fill="currentColor">&#603;&#772;&#8323;</text>
  <text x="600" y="155" text-anchor="middle" font-size="12" fill="currentColor">&#8943;</text>
  <line x1="95" y1="150" x2="185" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <line x1="255" y1="150" x2="345" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <line x1="415" y1="150" x2="505" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-ma1)"/>
  <text x="140" y="138" text-anchor="middle" font-size="11" fill="currentColor">&#8722;&#952;</text>
  <text x="300" y="138" text-anchor="middle" font-size="11" fill="currentColor">&#8722;&#952;</text>
  <text x="460" y="138" text-anchor="middle" font-size="11" fill="currentColor">&#8722;&#952;</text>
</svg>
<figcaption>Each residual is built from the current observation and the previous residual scaled
by $-\theta$. Conditioning on $\epsilon_0=0$ replaces the full covariance matrix of
$y_1,\dots,y_n$ with this chain of one-step Gaussian conditionals.</figcaption>
</figure>

## Turning the negative log-likelihood into a loss function

The three unknowns are $\mu$, $\theta$ and $\sigma$. Since gradient descent is unconstrained but
$\sigma$ must stay positive, the model optimises $\log\sigma$ instead of $\sigma$ directly and
exponentiates it wherever $\sigma$ is needed — a standard reparameterisation to remove a positivity
constraint. A PyTorch module implementing this holds `mu`, `theta` and `log_sigma` as learnable
parameters, and its forward pass is exactly the recursion above followed by the negative
log-likelihood formula:

```python
class MA1Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mu = nn.Parameter(torch.tensor(0.0))
        self.theta = nn.Parameter(torch.tensor(0.0))
        self.log_sigma = nn.Parameter(torch.tensor(0.0))

    def forward(self, y):
        n = len(y)
        eps_prev = y[0] - self.mu          # epsilon-hat_1
        eps_list = [eps_prev]
        for t in range(1, n):
            eps_t = y[t] - self.mu - self.theta * eps_prev
            eps_list.append(eps_t)
            eps_prev = eps_t
        eps = torch.stack(eps_list)

        sigma = torch.exp(self.log_sigma)
        nll = 0.5 * n * np.log(2 * np.pi) + 0.5 * torch.sum(torch.log(sigma**2) + eps**2 / sigma**2)
        return nll
```

Minimising `nll` — by zeroing gradients, calling `loss.backward()` and stepping an `Adam`
optimiser (learning rate $0.001$) for 4000 epochs — is maximum likelihood estimation done by
hand: the loss is literally the negative log-likelihood derived above, and there is no closed-form
solution being used anywhere, only gradients.

## Gradient descent recovers the ARIMA estimates

Training starts at $\mu=\theta=0$, $\sigma=1$ with loss $\approx 686.7$, and the loss falls
steadily as $\theta$ moves toward $-0.77$. By around epoch 1300 the loss and all three parameters
have essentially stopped moving (loss $\approx 440.37$), even though the loop runs on to epoch
4000. The final estimates match the ARIMA fit closely:

| parameter | ARIMA | Adam (PyTorch) |
|---|---|---|
| $\mu$ | $-0.001257$ | $-0.001139$ |
| $\theta$ | $-0.770992$ | $-0.772831$ |
| $\sigma^2$ | $0.235280$ | $0.235394$ |

The two routes — a canned quasi-Newton fit inside `statsmodels` and 1300-odd steps of Adam on a
loss function written out by hand — land on the same maximum-likelihood estimates.

## AR(1): a likelihood in closed form

The AR(1) case does not need the conditioning trick, because the AR(1) process has a genuinely
closed-form full likelihood in the stationary case. As given (Equation (6) in the Lecture 17
notes), the full likelihood of $y_1,\dots,y_n$ under
$y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$, $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$,
$|\phi_1| < 1$, is

$$
\frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{1-\phi_1^2}{2\sigma^2}\left(y_1-\frac{\phi_0}{1-\phi_1}\right)^2\right)
\left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^{n-1}
\exp\left(-\frac{1}{2\sigma^2}\sum_{t=2}^n (y_t-\phi_0-\phi_1 y_{t-1})^2\right).
$$

The first factor is the exact marginal density of the stationary first observation,
$y_1 \sim N\!\left(\frac{\phi_0}{1-\phi_1}, \frac{\sigma^2}{1-\phi_1^2}\right)$; the remaining
factor is the product of the ordinary one-step-ahead Gaussian conditionals
$y_t \mid y_{t-1} \sim N(\phi_0+\phi_1 y_{t-1}, \sigma^2)$ for $t=2,\dots,n$. No approximation is
needed because both pieces are already simple Gaussians — unlike the MA(1) case, there is no
covariance matrix to avoid.

Taking $-\log$ of the whole expression gives the loss to minimise:

$$
-\log L = \frac{n}{2}\log(2\pi) + n\log\sigma - \tfrac12\log(1-\phi_1^2)
+ \frac{1-\phi_1^2}{2\sigma^2}\left(y_1-\frac{\phi_0}{1-\phi_1}\right)^2
+ \frac{1}{2\sigma^2}\sum_{t=2}^n (y_t-\phi_0-\phi_1 y_{t-1})^2.
$$

## Fitting AR(1) by gradient descent

Two constraints show up that MA(1) did not have: $\sigma>0$, handled the same way as before by
optimising $\log\sigma$; and stationarity, $|\phi_1|<1$, needed for $\sqrt{1-\phi_1^2}$ to be
defined at all. The module enforces the second one crudely but effectively — by returning an
infinite loss whenever $|\phi_1|\ge 1$, which Adam's gradient steps simply avoid:

```python
class AR1Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.phi0 = nn.Parameter(torch.tensor(0.0))
        self.phi1 = nn.Parameter(torch.tensor(0.0))
        self.log_sigma = nn.Parameter(torch.tensor(0.0))

    def forward(self, y):
        n = len(y)
        sigma = torch.exp(self.log_sigma)
        phi0, phi1 = self.phi0, self.phi1

        if torch.abs(phi1) >= 1:
            return torch.tensor(float("inf"))

        y1_mean = phi0 / (1 - phi1)
        part1 = -0.5 * n * torch.log(torch.tensor(2 * torch.pi))
        part2 = -n * torch.log(sigma)
        part3 = 0.5 * torch.log(1 - phi1**2)
        part4 = -(1 - phi1**2) / (2 * sigma**2) * (y[0] - y1_mean)**2
        part5 = -(1 / (2 * sigma**2)) * torch.sum((y[1:] - phi0 - phi1 * y[:-1])**2)

        return -(part1 + part2 + part3 + part4 + part5)
```

Fitting `ARIMA(ylogdiff, order=(1,0,0))` gives $\phi_0=-0.0010$, $\phi_1=-0.3970$,
$\sigma^2=0.2793$. Training the module above with Adam (learning rate $0.001$, again started from
$\phi_0=\phi_1=0,\sigma=1$) has essentially converged by epoch 1700–1800, and agrees with ARIMA to
several decimal places:

| parameter | ARIMA | Adam (PyTorch) |
|---|---|---|
| $\phi_0$ | $-0.001022$ | $-0.001270$ |
| $\phi_1$ | $-0.396962$ | $-0.396962$ |
| $\sigma^2$ | $0.279279$ | $0.279277$ |

## Beyond MA(1) and AR(1)

The same two ingredients — write the (conditional or exact) Gaussian negative log-likelihood as a
function of the parameters, reparameterise any positivity or stationarity constraint so gradient
descent stays feasible, and minimise with an optimiser like Adam — extend directly to AR($p$) and
MA($q$) for general $p,q$. Gradient-based fitting reaches the same estimates as `ARIMA`; the only
reason it appears slower here is that the training loops above were run for several thousand
epochs out of caution, when the parameters had actually stopped moving hundreds of epochs earlier.

## Sources

- **Lab material**: [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb),
  Berkeley STAT 153, Spring 2025, section "MA(1) and AR(1) model fitting via PyTorch" (the whole
  chapter). Converted copy at
  `docs/statistics/berkeley/stat153/spring-2025/Lab13/02-ma-1-and-ar-1-model-fitting-via-pytorch.md`.
- **Referred to but not contained**: the varve dataset and its log-difference-then-MA(1) treatment
  are said to come from "Lecture 20"; the exact AR(1) full-likelihood formula is cited as
  "Equation (6) in the notes for Lecture 17." Neither lecture's notes were supplied with this lab,
  so their derivations are not reproduced here — only the formulas the lab itself states and uses.

---

[← 89. Change-of-Slope Regression and Scaling](89-change-of-slope-regression-and-scaling.md) · [Contents](index.md) · [91. LSTM Forecasting for Time Series →](91-lstm-forecasting-for-time-series.md)
