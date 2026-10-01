---
title: "33. Scaling and Initialization in PyTorch"
course: "Berkeley Stat 153"
chapter: 33
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 33. Scaling and Initialization in PyTorch

## What this covers

This chapter works through a PyTorch lab that refits three time-series models — a piecewise-linear
trend, a time-varying variance (stochastic volatility) model, and a periodogram-based spectrum
model — by generic gradient descent instead of the closed-form or convex methods used earlier in
the course. The question it answers is practical rather than theoretical: once a model is handed to
a general-purpose optimizer, what determines whether it converges quickly, and whether it finds the
right answer at all? It assumes the model definitions are already known — the piecewise-linear
regression from Lecture 24, the variance model from Lecture 14, and the spectrum model from Lectures
14–15 — and looks only at what changes when they are fit with PyTorch instead.

## The piecewise-linear model as a small network

Recall the change-point regression model:

$$ y_t = \beta_0 + \beta_1 t + \beta_2 (x_t - c_1)_+ + \beta_3(x_t-c_2)_+ + \cdots + \beta_{k+1}(x_t-c_k)_+ + \epsilon_t, $$

with $\epsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2)$, $x_t = t$, and $(z)_+ = \max(z,0)$. The
number of knots $k$ is fixed in advance; the unknowns are the intercept and slopes
$\beta_0,\dots,\beta_{k+1}$ together with the knot locations $c_1,\dots,c_k$. Written this way the
model is exactly a one-layer network with $k$ hidden units, each with a $\mathrm{ReLU}$ activation
shifted by a knot — which is why it can be coded, and trained, as an `nn.Module`.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A piecewise linear curve with two knots, one kink at each knot">
  <line x1="40" y1="180" x2="330" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="335" y="184" font-size="12" fill="currentColor">t</text>
  <polyline points="40,150 140,90 230,130 320,40" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="140" y1="180" x2="140" y2="90" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="230" y1="180" x2="230" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="140" y="196" text-anchor="middle" font-size="12" fill="currentColor">c1</text>
  <text x="230" y="196" text-anchor="middle" font-size="12" fill="currentColor">c2</text>
  <text x="85" y="112" text-anchor="middle" font-size="11" fill="currentColor">slope b1</text>
  <text x="185" y="103" text-anchor="middle" font-size="11" fill="currentColor">slope b1+b2</text>
  <text x="278" y="78" text-anchor="middle" font-size="11" fill="currentColor">slope b1+b2+b3</text>
</svg>
<figcaption>The model as a sum of hinge terms: each knot adds a kink to the fitted line. Because both
the slopes and the knot positions are estimated by gradient descent, the least-squares problem is
non-convex.</figcaption>
</figure>

In PyTorch, knots and coefficients are both `nn.Parameter`s, so both are found by gradient descent
rather than one of them being fixed by the analyst:

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

Fitting by least squares means minimizing

$$ \sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1 t - \beta_2(x_t-c_1)_+ - \cdots - \beta_{k+1}(x_t-c_k)_+\Big)^2, $$

and because the knots are themselves being optimized, this is possibly a non-convex problem — there
is no guarantee gradient descent lands on the global minimum, so how it is started matters.

## Warm-starting a non-convex fit

Rather than starting the knots at arbitrary values, the lab places them at quantiles of $x_t$: for
$k$ knots, at the levels $1/(k+1), \dots, k/(k+1)$. With the knots fixed at these locations, every
$(x_t - c_j)_+$ term becomes an ordinary covariate, so the coefficients $\beta_0,\dots,\beta_{k+1}$
can be found by one ordinary least squares fit — no iteration needed. That OLS solution then
initializes both the coefficients and the knots before gradient descent starts. This recipe —
quantile knots, then OLS for the coefficients, then hand the whole thing to Adam — recurs unchanged
in every model below; only the loss function that Adam minimizes changes.

The training loop itself is the same few lines throughout, regardless of the loss:

```python
optimizer = optim.Adam(model.parameters(), lr=...)
for epoch in range(num_epochs):
    optimizer.zero_grad()          # clear gradients left over from the previous step
    loss = loss_fn(model(x), y)    # loss_fn changes from model to model below
    loss.backward()                # compute d(loss)/d(parameter) for every parameter
    optimizer.step()               # update each parameter using its gradient
```

For the construction-spending series used first (monthly, $n=278$, from
[FRED's TLCOMCONS series](https://fred.stlouisfed.org/series/TLCOMCONS) — related to but not
identical to the series used in Lecture 24), with $k=4$ knots this warm start gives knots at
$56.4, 111.8, 167.2, 222.6$ and coefficients $(52168,\ 628.2,\ -1505.2,\ 1506.5,\ -264.7,\ 565.3)$.

## Learning rate: too slow, too fast, and unstable

The learning rate is the step size taken along the gradient at each update: too small and
convergence is slow but stable, too large and updates can overshoot the minimum. On the unscaled
construction-spending data, minimizing mean squared error with Adam, three settings were compared
over up to 300,000 epochs:

- $\text{lr}=0.01$: convergence is slow — it takes on the order of 300,000 epochs to reach the
  smallest loss found ($\approx 46{,}047{,}484$).
- $\text{lr}=0.1$: still slow, but reaches essentially the same loss by about 150,000 epochs.
- $\text{lr}=1$: never settles down — the loss keeps oscillating even once it is near its smallest
  value, rather than converging.

None of these is fast, on data of this size. That turns out to be a property of the data's scale,
not of the model or the optimizer.

## Scaling: the same fit, in far fewer iterations

Standardize both variables before fitting, $y_{\text{scaled}} = (y-\bar y)/s_y$ and
$x_{\text{scaled}} = (x-\bar x)/s_x$, and repeat exactly the same procedure: quantile knots, OLS
warm start, Adam. With $k=4$ knots the OLS warm start now gives knots at $(-1.04,-0.35,0.35,1.04)$
and coefficients $(2.27,\ 1.87,\ -4.49,\ 4.49,\ -0.79,\ 1.69)$ — all of comparable size, unlike the
unscaled fit above, where the intercept ($\approx 52{,}000$) and the slopes ($\approx 500$–$1500$)
differed by two orders of magnitude.

Fitting the scaled data with $\text{lr}=0.01$ converges in around 8,000 epochs — more than an order
of magnitude faster than the best of the three unscaled runs — and the loss is stable rather than
oscillating. Undoing the standardization on the fitted values, $\hat y = \hat y_{\text{scaled}}
\cdot s_y + \bar y$, recovers exactly the curve obtained by fitting the raw data directly. Scaling
changes nothing about *what* is fitted, only how quickly Adam gets there, which is why, in the
lab's own words, "scaling is almost always recommended."

## Reusing the model for a variance parameter

The variance (stochastic volatility) model from Lecture 14 assumes
$y_t \overset{\text{ind}}{\sim} N(0,\tau_t^2)$. Its negative log-likelihood is

$$ \sum_{t=1}^n \left(\log \tau_t + \frac{y_t^2}{2\tau_t^2}\right), $$

and reparametrizing by $\alpha_t = \log \tau_t$ turns it into

$$ \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2\alpha_t}\right). $$

Minimizing this with no constraint on $\alpha_t$ gives $\alpha_t = \log|y_t|$ for every $t$ —
complete overfitting, since one free parameter is spent per observation. The fix from Lecture 14 is
to force $\alpha_t$ to be smooth, writing it in the same piecewise-linear form as before, now as a
function of $t$ rather than of $y_t$:

$$ \alpha_t = \beta_0 + \beta_1 t + \beta_2(t-c_1)_+ + \cdots + \beta_{k+1}(t-c_k)_+. $$

With $k$ small, this constraint on its own is enough to prevent overfitting, so no extra
regularization penalty is added to the objective.

The lab tests this on a simulated series: a fixed smooth function

$$ \alpha(x) = \sin(15x) + e^{-x^2/2} + \tfrac12(x-0.5)^2 + 2\log(x+0.1), \qquad x \in [0,1], $$

evaluated at $n=2000$ equally spaced points to give the true $\alpha_t$, with $\tau_t = e^{\alpha_t}$
and $y_t$ drawn independently from $N(0,\tau_t^2)$. The same `PiecewiseLinearModel` class is reused
unchanged — only the loss becomes the negative log-likelihood above, evaluated at the model's output
in the role of $\alpha_t$:

```python
loss = torch.sum(y_pred + (y_torch**2) / 2 * torch.exp(-2 * y_pred))
```

With $k=8$ knots, quantile initial knots, and an OLS warm start (regressing $\log|y_t|$ on the same
hinge basis), Adam with $\text{lr}=0.01$ brings the loss from about $1876$ down to about $372$ over
20,000 epochs, and the recovered $\hat\alpha_t$ tracks the true curve well.

One detail carried over from the setup: only $x_t$ (time) is standardized here, not $y_t$. Unlike
the least-squares model above, this model is **not** invariant to rescaling both $x$ and $y$
together, so $y_t$ is left on its original scale.

## Spectrum estimation with the same trick

The spectrum model from Lectures 14–15 treats the periodogram ordinates $I(j/n)$, for
$j=1,\dots,m$ with $m$ the largest integer below $n/2$, as

$$ I(j/n) \overset{\text{ind}}{\sim} f(j/n)\,\eta_j, \qquad \eta_j \overset{\text{iid}}{\sim} \mathrm{Exp}(1), $$

so that $f(j/n)$ — the power at frequency $j/n$ — is the parameter of interest. The likelihood
$\prod_j f(j/n)^{-1}\exp(-I(j/n)/f(j/n))$ gives the negative log-likelihood

$$ \sum_{j=1}^m \left(\frac{I(j/n)}{f(j/n)} + \log f(j/n)\right), $$

and, exactly as for the variance model, reparametrizing $\alpha_j = \log f(j/n)$ turns this into

$$ \sum_{j=1}^m \big(I(j/n)\,e^{-\alpha_j} + \alpha_j\big). $$

Unconstrained minimization again just interpolates the data ($\alpha_j = \log I(j/n)$), so $\alpha_j$
is constrained to be piecewise linear in the frequency index $j$ — same model class, same warm
start, same optimizer, with the loss now written directly in terms of the periodogram rather than
its square:

```python
loss = torch.sum(y_pred + y_torch * torch.exp(-y_pred))
```

**Sunspot numbers.** Fit with $k=10$ knots, this converges cleanly — loss from about $1231$ to about
$1198$ over 20,000 epochs — and the resulting log-spectrum estimate lines up closely with a convex
comparison method from Lectures 14–15: a LASSO/trend-filtering estimator that penalizes the sum of
absolute second differences of $\alpha_j$ and is solved as a convex program (with `cvxpy`) rather
than by gradient descent.

## When the initialization is wrong: the earthquake example

The same recipe applied to an earthquake-vibration series — ground-floor acceleration measurements
under an active mass driver control system, open-loop condition, from a MathWorks signal-processing
tutorial — does not work out of the box. With $k=10$ knots placed at quantiles of the frequency
index, the loss decreases smoothly (from about $-35{,}967$ to about $-41{,}548$ over 20,000 epochs),
but the resulting estimate misses the three dominant peaks that the convex LASSO estimate finds in
the log periodogram.

The diagnosis is initialization, not the optimizer: the quantile knots are not near the peaks, so
nothing in the parametrization is positioned to represent them, and gradient descent has no way to
move the knots far enough on its own to compensate. Locating the peaks and troughs of the LASSO
estimate first (`scipy.signal.find_peaks`, giving peaks near frequency-index positions $55, 176,
284$ and troughs near $118, 229$), and placing new knots close to those positions — roughly
$50, 120, 175, 230, 285, 340, 400, 500$ — before re-running Adam with a smaller $\text{lr}=0.001$,
reduces the loss much further, to about $-41{,}908$, and brings the PyTorch estimate into close
agreement with the LASSO estimate.

The lesson drawn directly from the comparison: fitting these models by gradient descent is
flexible — the same few lines of PyTorch cover a least-squares trend, a volatility model, and a
spectrum model just by swapping the loss function — but it is a non-convex optimization, and its
result depends sensitively on where it starts. The convex formulation used in Lectures 14–15 does
not have this problem, at the cost of being restricted to a form (the LASSO/trend-filtering
penalty) where convexity is available.

## Sources

- Both parts of this chapter come from the same converted notebook, `CodeLabThirteen153248Fall2025.ipynb`
  (berkeley-stat153, fall 2025, CC BY 4.0):
  - [`01-piecewise-linear-model-via-pytorch-importance-of-scaling.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) —
    the construction-spending piecewise-linear fit, the learning-rate comparison, and the
    scaled-vs-unscaled comparison.
  - [`02-more-model-fitting-using-pytorch.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) —
    the variance-model simulation and the spectrum-model examples (sunspots, earthquake).
- Data: [FRED series TLCOMCONS](https://fred.stlouisfed.org/series/TLCOMCONS) (construction
  spending); a sunspot-number series (`SN_y_tot_V2.0.csv`); an earthquake acceleration series from
  the MathWorks MATLAB tutorial
  ["Practical Introduction to Frequency-Domain Analysis"](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html).
- Referred to but not contained in this material, and assumed as background: the piecewise-linear
  regression model and its original PyTorch fit, together with the MA(1)-type and AR(1) examples,
  from **Lecture 24**; the derivation of the variance model's negative log-likelihood and the
  overfitting result $\alpha_t=\log|y_t|$, from **Lecture 14**; and the spectrum model, the
  periodogram, and the convex LASSO/trend-filtering spectrum estimator used for comparison, from
  **Lectures 14–15**. Also referred to but not reproduced: [FRED series TTLCONS](https://fred.stlouisfed.org/series/TTLCONS),
  the series used for the analogous fit (on log-transformed data) in Lecture 24.

---

[← 32. Causal Stationary AR(2) Example](32-causal-stationary-ar-2-example.md) · [Contents](index.md) · [34. Inference in Sinusoid Models →](34-inference-in-sinusoid-models.md)
