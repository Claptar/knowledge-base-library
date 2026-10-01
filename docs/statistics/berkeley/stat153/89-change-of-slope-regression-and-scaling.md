---
title: "89. Change-of-Slope Regression and Scaling"
course: "Berkeley Stat 153"
chapter: 89
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 89. Change-of-Slope Regression and Scaling

## What this covers

A lab exercise in fitting a **change-of-slope model** — a continuous piecewise-linear regression
with unknown breakpoints — by writing it as a tiny PyTorch model and minimizing squared error with
gradient descent. It assumes you already know ordinary least squares and have seen the
change-of-slope (broken-stick) model fit by fixing the knots in advance; the question here is what
happens once the knot locations themselves become parameters to be estimated, and it answers a
second, more general question along the way: why the same optimization problem, on the same data,
can take orders of magnitude longer to converge (or fail to settle at all) depending on nothing but
the units the variables are measured in.

## The change-of-slope model

The model fit is

$$
y_t = \beta_0 + \beta_1 t + \beta_2 (x_t - c_1)_+ + \beta_3(x_t-c_2)_+ + \dots + \beta_{k+1}(x_t-c_k)_+ + \epsilon_t,
$$

with $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$ and $x_t = t$. The number of knots $k$
is fixed in advance (here $k=4$); the unknowns are the $k+2$ coefficients $\beta_0,\dots,\beta_{k+1}$
**and** the $k$ knot locations $c_1,\dots,c_k$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A continuous piecewise-linear function whose slope changes only at the knots c1 and c2">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="30,150 120,120 200,40 280,65" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="120" y1="170" x2="120" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="200" y1="170" x2="200" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="120" y="185" text-anchor="middle" font-size="12" fill="currentColor">c1</text>
  <text x="200" y="185" text-anchor="middle" font-size="12" fill="currentColor">c2</text>
  <text x="310" y="174" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="18" y="24" text-anchor="middle" font-size="12" fill="currentColor">y</text>
</svg>
<figcaption>The change-of-slope model: a straight line whose slope is free to change at each knot,
via added hinge terms $\beta_{j+1}(x_t - c_j)_+$.</figcaption>
</figure>

If the knots were known, this is ordinary least squares: the hinge terms $(x_t-c_j)_+$ are just
more columns of the design matrix, and the objective

$$
\sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1 t - \beta_2(x_t-c_1)_+ - \dots -\beta_{k+1}(x_t-c_k)_+\Big)^2
$$

is convex in the $\beta$'s. But treating the $c_j$'s as free parameters too makes the objective
**possibly non-convex**: the fitted curve depends on the knots in a piecewise, non-smooth way, and
there can be several local minima. The optimizer used to attack it is gradient descent, or a
variant such as Adam, and — as with any non-convex problem — initialization matters for whether it
lands in a good minimum.

## Writing the model as a PyTorch module

The model is small enough to write out directly as a custom `nn.Module`. `torch.relu(x - c)` is
exactly the hinge function $(x-c)_+$, so the forward pass is a direct transcription of the model
equation:

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))
        # When a tensor is wrapped in nn.Parameter and assigned as an attribute to a nn.Module,
        # it is automatically registered as a parameter of that module.

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

Both `beta` and `knots` are wrapped in `nn.Parameter`, which is what makes PyTorch track gradients
through them and update both simultaneously — the knot locations are fit by the same gradient
descent that fits the coefficients, not chosen by search over a grid. The knots are re-sorted on
every forward pass, so the labeling of which knot is "first" can move around during training
without the hinge terms becoming inconsistent.

## Initializing the parameters

Because the joint problem is non-convex, initialization is what keeps the optimizer out of bad
local minima. The strategy used is:

1. Place the initial knots $c_1,\dots,c_k$ at the sample quantiles of $x_t$ at levels
   $1/(k+1),\dots,k/(k+1)$ — evenly spaced through the range of the data.
2. With those knots held fixed, run an ordinary least squares regression of $y$ on
   $1, t, (x_t-c_1)_+,\dots,(x_t-c_k)_+$. This step is convex, so it has a well-defined answer, and
   its coefficients become $\beta_0,\dots,\beta_{k+1}$'s initial values.

```python
k = 4
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_raw, quantile_levels)

n = len(y_raw)
X = np.column_stack([np.ones(n), x_raw])
for j in range(k):
    xc = ((x_raw > knots_init[j]).astype(float)) * (x_raw - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_raw, X).fit()
beta_init = md_init.params.values
```

On the raw data (monthly total construction spending, in millions of dollars, $t=1,\dots,277$) this
gives knots at $[56.4, 111.8, 167.2, 222.6]$ and coefficients

$$
\beta_{\text{init}} = [52167.9,\ 628.2,\ -1505.2,\ 1506.5,\ -264.7,\ 565.3].
$$

The point to notice — it is flagged explicitly because it is the hinge of the whole chapter — is
that these values sit on very different scales: the intercept is tens of thousands, the slope terms
are hundreds, and the hinge coefficients are similar in magnitude to the linear slope. A single
learning rate has to move all of these together.

## The training loop and the learning rate

Once a model instance is built from these initial values, fitting proceeds by the standard PyTorch
pattern: zero the accumulated gradients, compute the loss, back-propagate, and step the optimizer.

```python
optimizer = optim.Adam(md_nn.parameters(), lr=1)
loss_fn = nn.MSELoss()

for epoch in range(300000):
    optimizer.zero_grad()
    # Without zeroing the gradients before each iteration, gradients from previous
    # iterations would accumulate, leading to incorrect updates of the model's parameters.

    y_pred = md_nn(x_raw_torch)
    loss = loss_fn(y_pred, y_raw_torch)

    loss.backward()
    # .backward() computes the gradient of the loss with respect to every parameter
    # that contributed to it.

    optimizer.step()
    # .step() updates the parameters using the gradients just computed.
```

The learning rate is the hyperparameter that controls how far each step moves the parameters along
the gradient. Too small, and convergence is safe but slow; too large, and updates can overshoot the
minimum and the loss can fail to settle. Running this on the raw, unscaled data at a few different
learning rates shows both failure modes:

- at $\text{lr}=0.01$, the algorithm converges, but only after roughly 300{,}000 epochs;
- at $\text{lr}=0.1$, still slow — convergence around 150{,}000 epochs;
- at $\text{lr}=1$, the algorithm never settles down: it keeps oscillating even after reaching
  close to the smallest loss it will reach.

The printed run above is the $\text{lr}=1$ case, over 300{,}000 epochs on the raw data. The loss
starts at about $80.9$ million, falls quickly for the first few thousand epochs, and then spends the
rest of the run creeping down from about $46.3$ million to about $46.05$ million — punctuated
throughout by sudden spikes back up (loss jumping to $46.4$–$47.1$ million for a single printed
epoch before dropping back), which is exactly the oscillation the third bullet describes. Three
hundred thousand epochs is a lot of computation to spend not fully converging.

## Why scaling fixes it

The diagnosis is the one flagged above: the initial coefficients — and hence the gradients Adam has
to work with — live on wildly different scales, because $y$ is measured in tens of thousands of
dollars and $t$ runs from $1$ to $277$. Standardizing both variables before fitting,

```python
y_scaled = (y_raw - np.mean(y_raw)) / (np.std(y_raw))
x_scaled = (x_raw - np.mean(x_raw)) / (np.std(x_raw))
```

and repeating the same quantile-knot / OLS-coefficient initialization on the standardized data gives
knots $[-1.035, -0.345, 0.345, 1.035]$ and coefficients

$$
\beta_{\text{init}} = [2.266,\ 1.874,\ -4.489,\ 4.493,\ -0.789,\ 1.686],
$$

all now comparable in magnitude — a direct, checkable sign that the scaling did what it was meant to
do. Rebuilding the model on this initialization and training with $\text{lr}=0.01$:

```python
optimizer = optim.Adam(md_nn.parameters(), lr=0.01)
for epoch in range(20000):
    optimizer.zero_grad()
    y_pred = md_nn(x_torch)
    loss = loss_fn(y_pred, y_torch)
    loss.backward()
    optimizer.step()
```

the loss starts at $0.112$, drops to about $0.066$ within a couple of thousand epochs, and is
essentially flat at about $0.064$ by roughly $8{,}000$ iterations — with only small, brief bumps
rather than the large spikes seen on the raw scale. Compare the cost: a stable fit in about $8{,}000$
iterations at $\text{lr}=0.01$, against $150{,}000$–$300{,}000$ iterations (and, at $\text{lr}=1$,
never fully stable) needed on the raw scale.

To compare the fitted curve back on the original scale, invert the standardization applied to $y$:

$$
\hat y_t = \hat y_t^{\text{scaled}} \cdot \mathrm{sd}(y) + \overline{y}.
$$

Plotting this against the fit obtained directly on the raw data, the two curves are close — scaling
does not change what function is being fit, only how quickly and how stably the optimizer gets
there. That is the reason scaling is recommended as a near-automatic first step before fitting any
model by gradient descent: it is not about the model or the data being wrong on the raw scale, it is
about giving a single shared learning rate a fair chance to move every parameter sensibly.

## Sources

- The change-of-slope model, the `PiecewiseLinearModel` PyTorch class, the quantile/OLS
  initialization, the training loop, the learning-rate comparison (lr $=0.01, 0.1, 1$), the
  standardization step, and the final scaled/unscaled comparison are all from the single supplied
  notebook: `Lab13.ipynb`, Stat 153 (UC Berkeley), Spring 2025 — converted at
  `docs/statistics/berkeley/stat153/spring-2025/Lab13/01-fitting-change-of-slope-models-via-pytorch-importance-of-sca.md`.
  All numerical values quoted (initial knots and coefficients, epoch/loss traces on both scales) are
  the values printed in that notebook's own output cells.
- The dataset is FRED series `TLCOMCONS` (Total Construction Spending, monthly, millions of
  dollars), `TLCOMCONS_23April2025.csv`, https://fred.stlouisfed.org/series/TLCOMCONS.
- The notebook notes that this dataset is "slightly different" from the one used in **Lecture 24**
  of the same course (FRED series `TTLCONS`, https://fred.stlouisfed.org/series/TTLCONS), where the
  same change-of-slope model was apparently fit — that lecture is referred to but was not supplied
  here.

---

[← 88. ARIMA Fitting and Model Selection](88-arima-fitting-and-model-selection.md) · [Contents](index.md) · [90. Fitting MA(1)/AR(1) via PyTorch →](90-fitting-ma-1-ar-1-via-pytorch.md)
