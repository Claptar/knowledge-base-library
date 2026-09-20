---
title: "56. Model Fitting via PyTorch"
course: "Berkeley Stat 153 Fall 2024"
chapter: 56
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 56. Model Fitting via PyTorch

## What this covers

The unifying idea: once a model's negative log-likelihood — or any other loss — is written down as
an explicit function of its parameters and the data, PyTorch's automatic differentiation together
with the Adam optimizer will fit it, whether or not the model has a closed-form estimator. This
chapter works that recipe through on MA(1) and AR(1) (checking the fit against `ARIMA`), on a
piecewise-linear change-of-slope regression (replacing an expensive grid search over breakpoints),
and on a nonlinear autoregression that has no closed-form fit at all. It assumes the MA(1)/AR(1)
models and their likelihoods, the change-of-slope regression model, and basic feedforward networks
(a single hidden layer with a ReLU nonlinearity).

## Fitting a model by writing down its loss

Every example below has the same shape, and it is worth naming once so the four fits read as one
idea repeated rather than four unrelated pieces of code.

1. Wrap the parameters in an `nn.Module`, one `nn.Parameter` per parameter. Anything that must stay
   positive (a variance) is stored on the log scale and exponentiated when it is used; anything
   that must satisfy a hard constraint (AR(1)'s stationarity region $|\phi_1| < 1$) can instead be
   checked directly, with the loss set to $+\infty$ outside it.
2. Write a `forward` method that takes the data and returns a single number — the negative
   log-likelihood if one is available, or a plain loss such as mean squared error if it is not.
3. Hand the module's parameters to `optim.Adam` and repeat the same three lines —
   `zero_grad`, `backward`, `step` — a few thousand times.

Nothing in this loop refers to MA, AR, ARIMA, or neural networks specifically. The four examples
below differ only in step 2: what the loss actually is, and whether it can be written down without
a loop.

## MA(1): a likelihood you have to unroll

Take the (log-differenced) glacial varve thickness series used earlier in the course, and recall
the MA(1) model
$$y_t = \mu + \epsilon_t + \theta\epsilon_{t-1}, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2).$$

Fitting this by maximum likelihood the direct way means writing the joint density of
$y_1,\dots,y_n$ in terms of their $n\times n$ covariance matrix, which is unpleasant. The standard
trick is to condition on $\epsilon_0 = 0$ and factor the resulting conditional likelihood one
observation at a time:
$$f_{y_1\mid \epsilon_0=0}(y_1)\, f_{y_2\mid y_1,\epsilon_0=0}(y_2)\, f_{y_3\mid y_1,y_2,\epsilon_0=0}(y_3)\,\cdots\, f_{y_n\mid y_1,\dots,y_{n-1},\epsilon_0=0}(y_n).$$

Conditioning on $\epsilon_0 = 0$ is what makes each factor tractable: given $y_1,\dots,y_{t-1}$ and
$\epsilon_0=0$, the earlier innovations $\epsilon_1,\dots,\epsilon_{t-1}$ are pinned down exactly by
a recursion. Define $\hat\epsilon_1 = y_1 - \mu$ and, for $t = 2,\dots,n$,
$$\hat\epsilon_t = y_t - \mu - \theta\hat\epsilon_{t-1}.$$
Then $y_t$ given the past is just $\mu + \theta\hat\epsilon_{t-1}$ plus a fresh $N(0,\sigma^2)$
draw, so each conditional density is
$$f_{y_t\mid \dots}(y_t) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{\hat\epsilon_t^2}{2\sigma^2}\right),$$
and the negative log-likelihood collapses to
$$\ell(\mu,\theta,\sigma) = \frac{n}{2}\log(2\pi) + \frac12\sum_{t=1}^n\left(\log\sigma^2 + \frac{\hat\epsilon_t^2}{\sigma^2}\right).$$

The catch is that $\hat\epsilon_t$ depends on $\hat\epsilon_{t-1}$, which depends on
$\hat\epsilon_{t-2}$, and so on — the recursion cannot be vectorized away, so the PyTorch module has
to unroll it in an explicit Python loop:

```python
class MA1Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mu = nn.Parameter(torch.tensor(0.0))
        self.theta = nn.Parameter(torch.tensor(0.0))
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma)

    def forward(self, y):
        n = len(y)
        eps_list = []
        eps_prev = y[0] - self.mu
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

$\sigma$ is stored as `log_sigma` and exponentiated, so the optimizer never has to worry about
straying into $\sigma \le 0$. Training with `optim.Adam(lr=0.001)` for 4000 epochs on the 633
log-differenced observations lands here, matching the values `ARIMA(0,0,1)` reports on the same
series:

| | $\mu$ | $\theta$ | $\sigma^2$ |
|---|---|---|---|
| `ARIMA` (statsmodels) | $-0.001257$ | $-0.77099$ | $0.235280$ |
| PyTorch (Adam, 4000 epochs) | $-0.001136$ | $-0.77283$ | $0.235394$ |

The two fits agree to three significant figures, which is the point: the gradient-based fit is not
an approximation to the ARIMA answer, it is the same maximum-likelihood estimate reached by a
different route.

## AR(1): a likelihood you can vectorize

The AR(1) model, $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$, is stationary when $|\phi_1| < 1$,
in which case $y_1$ itself has the stationary marginal distribution rather than an arbitrary
starting value. The exact (not merely conditional) likelihood is
$$\frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{1-\phi_1^2}{2\sigma^2}\left(y_1 - \frac{\phi_0}{1-\phi_1}\right)^2\right)\left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^{n-1}\exp\left(-\frac{1}{2\sigma^2}\sum_{t=2}^n (y_t - \phi_0 - \phi_1 y_{t-1})^2\right).$$

The first factor is the density of $y_1$ under its stationary marginal (mean
$\phi_0/(1-\phi_1)$, variance shrunk by $\sqrt{1-\phi_1^2}$); the rest is the product of $n-1$
ordinary one-step-ahead conditional densities. Unlike the MA(1) case, every term here is a direct
function of $y_t$ and $y_{t-1}$ — no recursion is needed, since $y_{t-1}$ is already sitting in the
data as a shifted vector. That means the whole log-likelihood can be written in one vectorized pass:

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
            return torch.tensor(float("inf")), None       # outside the stationary region

        y1_mean = phi0 / (1 - phi1)
        part1 = -0.5 * n * torch.log(torch.tensor(2 * torch.pi))
        part2 = -n * torch.log(sigma)
        part3 = 0.5 * torch.log(1 - phi1**2)
        part4 = -(1 - phi1**2) / (2 * sigma**2) * (y[0] - y1_mean)**2
        part5 = -(1 / (2 * sigma**2)) * torch.sum((y[1:] - phi0 - phi1 * y[:-1])**2)
        log_likelihood = part1 + part2 + part3 + part4 + part5
        return -log_likelihood, log_likelihood
```

Note the two different ways the two constraints are handled: $\sigma > 0$ is enforced by a smooth
reparametrization (`log_sigma`), while $|\phi_1| < 1$ is enforced by a hard rejection — the loss
simply becomes infinite outside the stationary region, which keeps Adam from wandering there as
long as it does not start there.

Training this module for 4000 epochs reproduces `ARIMA(1,0,0)` just as closely as MA(1) did:

| | $\phi_0$ | $\phi_1$ | $\sigma^2$ |
|---|---|---|---|
| `ARIMA` (statsmodels) | $-0.001022$ | $-0.39696$ | $0.279279$ |
| PyTorch (Adam, 4000 epochs) | $-0.001421$ | $-0.39696$ | $0.279277$ |

The lecture's own observation is worth keeping: the AR(1) code trains **much faster** than the
MA(1) code, for exactly the structural reason above — the AR(1) loss is a single vectorized
expression, while the MA(1) loss has to unroll a length-$n$ Python loop to compute the innovations
one at a time. The same two model classes extend, with more parameters and (for MA) more of that
unrolling, to general AR($p$) and MA($q$).

## Trading a grid search for two more parameters

The change-of-slope regression model from an earlier lecture is
$$y_t = \beta_0 + \beta_1 x_t + \beta_2\,\mathrm{ReLU}(x_t - c_1) + \beta_3\,\mathrm{ReLU}(x_t - c_2) + \epsilon_t, \qquad x_t = t,$$
fit to a monthly series of total U.S. construction spending (TTLCONS, January 1993 to February
2025, 386 observations). The model is linear in $\beta_0,\dots,\beta_3$ once the knots $c_1,c_2$
are fixed, but the knots themselves enter nonlinearly. The method used earlier in the course was a
grid search: for every candidate pair $(c_1,c_2)$ on an integer grid, fit an OLS with those knots
held fixed, record the residual sum of squares, and keep the minimizing pair. On this data that
search tries on the order of $380^2 \approx 1.4\times 10^5$ OLS fits, landing on $c_1=225$,
$c_2=175$ with $R^2 = 0.980$.

The PyTorch idea is to notice what a piecewise-linear function with $k$ knots actually *is*: it is
what a single hidden layer network with $k$ ReLU units computes when every input-to-hidden weight
is pinned at $1$ and the bias of hidden unit $j$ is $-c_j$, since $\mathrm{ReLU}(1\cdot x - c_j)$ is
exactly $\mathrm{ReLU}(x - c_j)$. Once you see the knots as a layer's biases, there is no reason to
search over them on a grid — treat them as ordinary learnable parameters and let autograd
differentiate through the ReLUs (which is fine almost everywhere, the one non-differentiable point
per knot is measure zero and never landed on exactly by a continuous optimizer):

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

Two practical points matter as much as the model itself here. First, $x_t$ (month index, up to
386) and $y_t$ (millions of dollars, in the low millions) are rescaled to mean 0, standard
deviation 1 before fitting — on the raw scale the loss surface is badly conditioned and Adam
struggles. Second, the loss is non-convex in the knot locations (moving a knot past a data point
changes which residuals it touches), so a cold start at $\mathrm{knots}=0,\ \beta=0$ risks getting
stuck. The fix used here is a warm start: place the $k$ knots at the quantiles
$\tfrac1{k+1},\dots,\tfrac{k}{k+1}$ of the scaled covariate (splitting the data into $k+1$ roughly
equal groups), fit one OLS with those knots held fixed to get an initial $\hat\beta$, and only then
hand both knots and $\beta$ to Adam. The lecture's own caution is worth repeating verbatim: *"Run
this code a few times to be sure of convergence, especially for non-convex optimization
problems."*

With $k=2$ knots, Adam (lr $=0.01$, MSE loss, 20{,}000 epochs) lands within rounding of what the
grid search found, on the scaled data:

| | $c_1$ | $c_2$ | loss |
|---|---|---|---|
| grid search (fixed knots, OLS) | $0.283$ | $-0.166$ | $0.01959$ |
| PyTorch (knots as parameters) | $-0.168$ | $0.286$ | $0.01958$ |

(The two knot values are simply swapped between the rows — the model is symmetric in the knots,
and `forward` sorts them before use — so this is the same optimum found two ways: an exhaustive
search over a discrete grid, and a gradient-based search over a continuum, with the second no
longer paying the $O(n^2)$ cost of refitting an OLS at every grid point.)

## A nonlinear autoregression: letting a network find the shape

This example continues a NAR($p$) construction introduced earlier in the same lecture (with its
own "Example One") that is not part of the material behind this chapter; what follows starts from
the code as given, fitting a single hidden layer network to lagged values and comparing it against
a linear AR($p$) fit and against the true generating function.

The simulated series has $n=1450$ points, with dynamics that depend only on the fifth lag:
$$y_i = \frac{2y_{i-5}}{1+0.8\,y_{i-5}^2} + \epsilon_i, \qquad \epsilon_i \overset{\text{i.i.d.}}{\sim}\mathrm{Unif}(-1,1),$$
with $y_1,\dots,y_4$ drawn independently from $\mathrm{Unif}(-1,1)$ to start the recursion. Write
$g(x) = 2x/(1+0.8x^2)$ for the true nonlinear map. Although the process only depends on $y_{t-5}$,
the fitted model is given all five lags $y_{t-1},\dots,y_{t-5}$ as input and has to discover on its
own that only one of them matters.

The model is a single hidden layer network with $p=5$ inputs and $k=6$ hidden units,
$$\hat y_t = \beta_0 + \sum_{j=1}^{k}\beta_j\,\mathrm{ReLU}\big(w_j^\top x_t + b_j\big), \qquad x_t = (y_{t-1},\dots,y_{t-p}),$$
built from a lagged design matrix and fit by minimizing mean squared error with Adam (lr $=0.01$,
10{,}000 epochs). Training loss settles near $0.331$. That number is worth checking against the
irreducible noise: $\epsilon\sim\mathrm{Unif}(-1,1)$ has variance $\tfrac{1}{3}\approx 0.333$, so a
training loss this close to $1/3$ means the network has essentially recovered $g$ from the fifth
lag and is left fitting pure noise — there is no more signal left to extract.

The real test is forecasting. From the last available window of five values, the fitted network is
iterated forward: predict the next value, drop the oldest lag, append the prediction, and repeat.

<figure>
<svg viewBox="0 0 460 240" role="img" aria-label="Recursive multi-step forecasting: the network's own prediction is fed back in as the newest lag while the oldest lag is dropped.">
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <g font-size="11" fill="currentColor">
    <rect x="90" y="20" width="300" height="34" fill="none" stroke="currentColor"/>
    <line x1="150" y1="20" x2="150" y2="54" stroke="currentColor"/>
    <line x1="210" y1="20" x2="210" y2="54" stroke="currentColor"/>
    <line x1="270" y1="20" x2="270" y2="54" stroke="currentColor"/>
    <line x1="330" y1="20" x2="330" y2="54" stroke="currentColor"/>
    <text x="120" y="41" text-anchor="middle">y(t-5)</text>
    <text x="180" y="41" text-anchor="middle">y(t-4)</text>
    <text x="240" y="41" text-anchor="middle">y(t-3)</text>
    <text x="300" y="41" text-anchor="middle">y(t-2)</text>
    <text x="360" y="41" text-anchor="middle">y(t-1)</text>
  </g>

  <line x1="240" y1="54" x2="240" y2="90" stroke="currentColor" marker-end="url(#arrowhead)"/>

  <rect x="170" y="92" width="140" height="36" fill="none" stroke="currentColor"/>
  <text x="240" y="114" text-anchor="middle" font-size="12" fill="currentColor">network</text>

  <line x1="240" y1="128" x2="240" y2="160" stroke="currentColor" marker-end="url(#arrowhead)"/>

  <rect x="210" y="162" width="60" height="30" fill="none" stroke="currentColor"/>
  <text x="240" y="182" text-anchor="middle" font-size="12" fill="currentColor">ŷ(t)</text>

  <path d="M270,177 C 430,177 430,60 390,42" fill="none" stroke="currentColor" marker-end="url(#arrowhead)"/>
  <text x="392" y="120" font-size="11" fill="currentColor">append</text>

  <path d="M90,37 C 50,37 50,5 20,5" fill="none" stroke="currentColor" marker-end="url(#arrowhead)"/>
  <text x="5" y="220" font-size="11" fill="currentColor">drop oldest</text>
</svg>
<figcaption>One step of the recursive forecast: the current window of five lags feeds the fitted
network, the predicted value is appended on the right and the oldest lag is dropped on the left,
and the shifted window becomes the input for the next step.</figcaption>
</figure>

The same recursion is run three ways over $40$ future steps: with the fitted network, with a linear
AR($5$) model fit by `statsmodels`' `AutoReg`, and — since the data is simulated and $g$ is known —
with the true $g$ and no injected noise, giving an oracle forecast to compare against. Measuring
each model's forecast against the oracle by mean squared error:

| forecast | MSE against the true $g$ |
|---|---|
| linear AR($5$) | $0.4958$ |
| nonlinear AR (network, $p=5,k=6$) | $0.003173$ |

the linear model's forecast error is about $156$ times larger. Plotting the network's fitted
values against $y_{t-5}$ (sorted) reproduces the shape of $g(x)=2x/(1+0.8x^2)$ closely, which is
the actual explanation for the gap: the improvement is not from the extra unused lags, it is from
the network having learned the right nonlinear shape in the one lag that matters, which a linear
AR($p$) model cannot represent at any $p$.

## Sources

- MA(1) and AR(1) derivations, code and results: `03-ma-1-and-ar-1-model-fitting-via-pytorch.md`
  (Berkeley STAT 153, Fall 2025, "Model Fitting using PyTorch" notebook, section 1). The varve
  dataset and its log-and-difference transform are referenced from earlier lectures (20 and 21) not
  included here; the AR(1) exact likelihood is referenced as "Equation (7) in the notes for Lecture
  17", also not included here.
- Nonlinear autoregression example ("Example Two"): `05-example-two.md`, section 2 of the same
  notebook. This section presupposes an earlier subsection of the same lecture, "Nonlinear
  AutoRegression" (which introduces the NAR($p$) model and its own "Example One"), not part of the
  material supplied for this chapter.
- Piecewise-linear change-of-slope example: `01-ttlcons-dataset.md` (Berkeley STAT 153, Spring
  2025, the same "Model Fitting using PyTorch" lecture slot in a different semester, using a
  different worked example). The change-of-slope model and its grid-search fitting method are
  referenced from "Lecture 9", not included here.

All three files are lossless conversions of the course's own Jupyter notebooks
(`CodeLectureTwentyFour153248Fall2025.ipynb` and `CodeLectureTwentyFour153248Spring2025.ipynb`),
licensed CC BY 4.0.

---

[← 55. Nonlinear Autoregression and Overfitting](55-nonlinear-autoregression-and-overfitting.md) · [Contents](index.md) · [57. Identifying and Fitting ARIMA Models →](57-identifying-and-fitting-arima-models.md)
