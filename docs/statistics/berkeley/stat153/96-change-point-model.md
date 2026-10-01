---
title: "96. Change-point model"
course: "Berkeley Stat 153"
chapter: 96
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 96. Change-point model

## What this covers

A time series can hold a constant level and then, at some unknown time, jump to a different level.
This chapter asks how to locate that jump — the **change-point** — and how much to trust the
location once it is found. It assumes familiarity with ordinary least squares, maximum likelihood
for a linear model, and the standard Bayesian treatment of linear regression (a posterior over
$\beta$ and $\sigma$ obtained by integrating a flat/reference prior against the likelihood). The
running example is a simulated series built to have a known change-point, so every estimate below
can be checked against the truth that generated it.

## The change-point regression model

Consider

$$
y_t = \beta_0 + \beta_1 I\{t > c\} + \epsilon_t .
$$

$I\{t > c\}$ is the indicator function, equal to $1$ when $t > c$ and $0$ otherwise, so the mean
function $\beta_0 + \beta_1 I\{t > c\}$ equals $\beta_0$ up to time $c$ and $\beta_0 + \beta_1$
after it. The series holds one level until time $c$, then switches to a second level — $c$ is the
change-point, and $\beta_1$ is the size of the jump.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A time series holding one level, jumping to a second level at the change-point c">
  <line x1="40" y1="190" x2="380" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="380" y="207" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <text x="26" y="35" text-anchor="end" font-size="12" fill="currentColor">y_t</text>
  <line x1="210" y1="190" x2="210" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="210" y="22" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <line x1="40" y1="140" x2="210" y2="140" stroke="currentColor" stroke-width="2"/>
  <line x1="210" y1="80" x2="380" y2="80" stroke="currentColor" stroke-width="2"/>
  <text x="60" y="132" font-size="12" fill="currentColor">&#946;&#8320;</text>
  <text x="220" y="72" font-size="12" fill="currentColor">&#946;&#8320; + &#946;&#8321;</text>
  <g fill="currentColor" fill-opacity="0.6">
    <circle cx="55" cy="132" r="2.2"/><circle cx="70" cy="148" r="2.2"/><circle cx="85" cy="136" r="2.2"/>
    <circle cx="100" cy="145" r="2.2"/><circle cx="115" cy="130" r="2.2"/><circle cx="130" cy="150" r="2.2"/>
    <circle cx="145" cy="138" r="2.2"/><circle cx="160" cy="144" r="2.2"/><circle cx="175" cy="133" r="2.2"/>
    <circle cx="190" cy="147" r="2.2"/>
    <circle cx="225" cy="72" r="2.2"/><circle cx="240" cy="88" r="2.2"/><circle cx="255" cy="76" r="2.2"/>
    <circle cx="270" cy="86" r="2.2"/><circle cx="285" cy="70" r="2.2"/><circle cx="300" cy="90" r="2.2"/>
    <circle cx="315" cy="78" r="2.2"/><circle cx="330" cy="84" r="2.2"/><circle cx="345" cy="73" r="2.2"/>
    <circle cx="360" cy="87" r="2.2"/>
  </g>
</svg>
<figcaption>The change-point model: a series that holds level $\beta_0$ until time $c$, then jumps
to $\beta_0+\beta_1$, plus noise. Estimating $c$ means finding the break that best separates the
two levels.</figcaption>
</figure>

If $c$ were known, this would be ordinary linear regression with design matrix

$$
X_c = \begin{pmatrix} 1 & I\{1 > c\} \\ 1 & I\{2 > c\} \\ 1 & I\{3 > c\} \\ \vdots & \vdots \\ 1 & I\{n > c\} \end{pmatrix} .
$$

The one thing that keeps this from being an ordinary regression problem is that $c$ itself is
unknown, and it enters the model through the indicator rather than linearly — so it cannot be
estimated by the usual normal equations. That is what makes the model nonlinear, and $c$, $\beta_0$,
$\beta_1$ and $\sigma$ all have to be estimated from $y_1,\dots,y_n$ together.

## Estimating the change point by profile RSS

The unknown $c$ only ever takes one of finitely many values ($c \in \{1,\dots,n-1\}$, say), so it
can be handled by a discrete search rather than by calculus. For each candidate value of $c$, fit
the two remaining parameters by least squares and record the residual sum of squares:

$$
RSS(c) := \min_{\beta_0,\beta_1} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1 I\{t>c\}\bigr)^2 .
$$

This is the *profile* residual sum of squares — for each fixed $c$ the inner minimization is an
ordinary OLS fit, so $RSS(c)$ is cheap to compute for every candidate. The MLE of the change-point
is the value that minimizes this profile:

$$
\hat c = \arg\min_c RSS(c).
$$

Once $\hat c$ is fixed, $\beta_0,\beta_1$ are just the OLS estimates from the regression with
$X_{\hat c}$, exactly as in ordinary linear regression with a known design. The noise variance is
then estimated the usual two ways, the MLE and the unbiased version:

$$
\hat\sigma_{\mathrm{MLE}} = \sqrt{\frac{RSS(\hat c)}{n}}, \qquad
\hat\sigma_{\mathrm{unbiased}} = \sqrt{\frac{RSS(\hat c)}{n-2}} .
$$

**Worked example.** A series of length $n=10000$ was simulated with mean $0$ for the first half,
mean $0.4$ for the second half, and independent $N(0,1)$ noise (so the true change-point is
$c=5000$). Plotting $RSS(c)$ against every candidate $c$ from $1$ to $n-1$ gives a curve with a
sharp trough near the true break; minimizing it gives $\hat c = 5045$. Plugging that in:

- $\hat\beta_0 = -0.019$ against a true value of $0$, and $\hat\beta_1 = 0.422$ against a true
  value of $0.4$;
- $\hat\sigma_{\mathrm{MLE}} = 1.006$ and $\hat\sigma_{\mathrm{unbiased}} = 1.006$, against a true
  $\sigma = 1$.

Overlaying the fitted step function $\hat\beta_0 + \hat\beta_1 I\{t>\hat c\}$ on the raw data shows
it tracking the two levels closely, with the fitted break sitting a little to the right of the true
one — an error of $45$ out of $10000$ points.

## Bayesian inference for the change point

The profile-RSS estimate gives a single best guess for $c$, but not a sense of how sure that guess
is. A Bayesian treatment answers this by putting a posterior distribution over $c$ itself, treating
it as a discrete parameter ranging over the candidate values. The (unnormalized) posterior is

$$
p(c \mid y) \;\propto\; |X_c^\top X_c|^{-1/2} \left(\frac{1}{RSS(c)}\right)^{(n-p)/2},
\qquad p = 2,
$$

where $|X_c^\top X_c|$ is the determinant of $X_c^\top X_c$. The shape of this is plausible from
what was already computed: the term $RSS(c)^{-(n-p)/2}$ rewards exactly the values of $c$ that
minimize the profile residual sum of squares from the previous section, and does so increasingly
sharply as $n$ grows — so the posterior concentrates around the same $\hat c$ that the MLE finds.
The determinant term corrects for how well-determined $\beta_0,\beta_1$ are under the split that
$c$ induces; it does not depend on the fit quality directly, only on the design.

Because $RSS(c)$ raised to a large negative power and a determinant raised to $-1/2$ vary over many
orders of magnitude, the computation is done on the log scale for numerical stability:

$$
\log p(c\mid y) \;\overset{c}{=}\; \frac{p-n}{2}\log RSS(c) \;-\; \tfrac{1}{2}\log|X_c^\top X_c|,
$$

and the plot of this log-posterior against $c$ looks like the RSS profile, as expected. To recover
an actual probability distribution over the candidate values of $c$, exponentiate after subtracting
the maximum (to avoid overflow) and normalize so the values sum to one:

$$
\tilde p(c) = \exp\bigl(\log p(c\mid y) - \max_c \log p(c\mid y)\bigr), \qquad
p(c\mid y) = \frac{\tilde p(c)}{\sum_c \tilde p(c)}.
$$

**Sampling the full posterior.** Once $p(c\mid y)$ is a normalized discrete distribution, drawing
from the joint posterior of $(c,\beta_0,\beta_1,\sigma)$ is a three-step hierarchical sampler:

1. Draw $c$ from the discrete distribution $p(c \mid y)$ just computed.
2. Given that $c$, draw $\sigma$ from the standard linear-model conditional posterior: draw a
   $\chi^2_{n-p}$ random variable and set $\sigma = \sqrt{RSS(c)/\chi^2_{n-p}}$ (a scaled inverse
   chi-squared draw).
3. Given $c$ and that $\sigma$, draw $(\beta_0,\beta_1)$ from
   $N\bigl(\hat\beta(c),\, \sigma^2 (X_c^\top X_c)^{-1}\bigr)$, where $\hat\beta(c)$ is the OLS
   estimate under $X_c$.

**Worked example, continued.** With $2000$ posterior draws from the $n=10000$ series above, the
sampled change-points cluster tightly in a narrow band around $5000$ — reflecting how sharply the
log-posterior peaks when $n$ is this large — and overlaying every draw's fitted step function on
the raw data produces a bundle of near-identical curves, all close to the single MLE fit found
earlier. The Bayesian analysis does not move the point estimate; it quantifies how little
uncertainty is left about $c$ once ten thousand observations are available.

## Multiple change points

The model extends directly to $k$ change-points by adding one indicator per break:

$$
y_t = \beta_0 + \beta_1 I\{t>c_1\} + \beta_2 I\{t>c_2\} + \beta_3 I\{t>c_3\} + \epsilon_t
$$

for $k=3$, and similarly for other $k$. $RSS(c_1,c_2,c_3)$ is defined exactly as before — minimize
over all the $\beta$'s for fixed $(c_1,c_2,c_3)$ — and the MLE is the triple that minimizes it.

**Worked example.** A series of length $n=400$ was simulated in four blocks of $100$ with means
$0,\ 1.5,\ -1,\ 0$ and $N(0,1)$ noise, so the true change-points are $c_1=100$, $c_2=200$,
$c_3=300$. A full joint grid search — evaluating $RSS(c_1,c_2,c_3)$ over a $51\times51\times51$
grid of candidates around each true value — found its minimum at $(100, 198, 300)$ with
$RSS \approx 432.68$, close to the truth. This grid search took about $49$ seconds on an ordinary
laptop, because it fits an OLS regression at every one of the $51^3$ grid points; a joint search
over $k$ change-points costs a number of regressions that grows as (grid size)$^k$, which quickly
becomes impractical as $k$ grows.

## A faster sequential algorithm

A much cheaper alternative estimates the change-points one at a time rather than jointly. First
find $\hat c_1$ exactly as in the single change-point model, ignoring that there may be more than
one break:

$$
\hat c_1 = \arg\min_{c_1} \min_{\beta_0,\beta_1} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1 I\{t>c_1\}\bigr)^2 .
$$

Then fix $\hat c_1$ and search for a second break on top of it:

$$
\hat c_2 = \arg\min_{c_2} \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1 I\{t>\hat c_1\} - \beta_2 I\{t>c_2\}\bigr)^2 ,
$$

and finally fix both $\hat c_1$ and $\hat c_2$ and search for a third:

$$
\hat c_3 = \arg\min_{c_3} \min_{\beta_0,\beta_1,\beta_2,\beta_3} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1 I\{t>\hat c_1\} - \beta_2 I\{t>\hat c_2\} - \beta_3 I\{t>c_3\}\bigr)^2 .
$$

Each step is a single change-point search over the full grid of candidates, so the whole procedure
costs $k$ one-dimensional searches instead of one $k$-dimensional search.

Run on the same three-change-point series, this gives $\hat c_1 = 198$, then (fixing $198$)
$\hat c_2 = 100$, then (fixing $198$ and $100$) $\hat c_3 = 300$. Notice that the first step does
not recover the temporally first change-point at $t=100$: a single-change-point search finds
whichever break reduces the residual sum of squares the most overall, and here that is the jump
from mean $0$ to mean $1.5$ at $t=200$ — the largest jump in the series — not the earliest one. The
second and third steps then pick up the remaining two breaks. Despite finding them in a different
order, the final set of estimates, $\{100, 198, 300\}$, agrees exactly with the full joint grid
search — obtained in a small fraction of the time.

## Sources

- Notes: `docs/statistics/berkeley/stat153/spring-2025/Lab5.md` (converted from
  `Lab5.ipynb`, Berkeley Stat 153, Spring 2025, CC BY 4.0) — the sole source for this chapter. It
  supplies the single change-point model and its indicator-function design matrix, the profile-RSS
  definition and worked simulation ($n=10000$, $\hat c = 5045$), the Bayesian posterior for $c$
  and its log-scale computation, the hierarchical posterior sampler (draw $c$, then $\sigma$ from
  a scaled inverse chi-squared, then $\beta$ from a multivariate normal), the three-change-point
  model and its joint-grid-search example ($n=400$, true breaks at $100,200,300$), and the faster
  sequential estimation algorithm with its worked result ($\hat c_1=198,\ \hat c_2=100,\
  \hat c_3=300$).
- No slides, transcript, or exercises were supplied for this lecture; the notebook's own code and
  commentary are reproduced above as prose and results rather than as code. Figures referenced in
  the source notebook (the raw series, the RSS and posterior curves, the fitted and sampled step
  functions) were not available as images and are described from the surrounding text and printed
  output instead of reproduced.

---

[← 95. Inference in Nonlinear Regression Models](95-inference-in-nonlinear-regression-models.md) · [Contents](index.md) · [97. High-dimensional regression for change-points →](97-high-dimensional-regression-for-change-points.md)
