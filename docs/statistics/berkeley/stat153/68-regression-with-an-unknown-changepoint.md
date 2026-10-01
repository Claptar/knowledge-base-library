---
title: "68. Regression with an Unknown Changepoint"
course: "Berkeley Stat 153"
chapter: 68
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 68. Regression with an Unknown Changepoint

## What this covers

This chapter asks: if a time series looks like a straight line whose slope changes once, partway
through, how do you find where the change happened — and how sure can you be about it? It assumes
the Bayesian treatment of ordinary linear regression from an earlier lecture in the course: the
Gaussian likelihood for regression coefficients, the flat/log-flat prior on $(\beta,\sigma)$, and
the orthogonal ("Pythagorean") decomposition of the residual sum of squares used to derive it. That
machinery is reused here essentially unchanged; the new ingredient is a changepoint that enters the
model non-linearly.

## The broken-stick model

A time series that changes trend once can be written as

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2),$$

where $(x)_+ = \max(x,0)$ is the positive part of $x$, and $c$ is the unknown changepoint (the
lecture's term for it is left implicit; it is simply "the value of $t$ where the line kinks").
Before $c$, the term $(t-c)_+$ is zero and the series is the line $\beta_0+\beta_1 t$. After $c$,
$(t-c)_+ = t-c$, and substituting turns the model into

$$\beta_0 + \beta_1 t + \beta_2(t-c) = (\beta_0-\beta_2 c) + (\beta_1+\beta_2)t,$$

a line with the same intercept-and-slope shape but slope $\beta_1+\beta_2$ instead of $\beta_1$.
So $\beta_2$ is exactly the *change* in slope at the kink, and $c$ is *where* it happens. Checking
this against the two special cases $c=0$ and $c=1$ gives $\beta_0+(\beta_1+\beta_2)t$ and
$(\beta_0-\beta_2)+(\beta_1+\beta_2)t$ respectively — both instances of the general formula above.

This also shows why $c$ cannot be allowed to sit at the edge of the data. If $c \le 1$, every
observed $t\ge 1$ is past the kink, so the data only ever see the combined slope $\beta_1+\beta_2$
and $\beta_1,\beta_2$ are not separately identifiable. If $c \ge n$, then $(t-c)_+ = 0$ for every
observed $t \le n$: the kink never happens inside the observation window, and the whole series
looks like a single line $\beta_0+\beta_1 t$ with $\beta_2$ invisible. A changepoint model can only
be told apart from an ordinary straight line if there are genuine observations on both sides of the
kink, which is why $c$ is restricted to an interior range — a wide version is $c\in(1,n)$, a
tighter and more realistic one is $c\in(10,n-10)$, since interest is mainly in changepoints away
from the edges.

## Estimating the changepoint by least squares

For a *fixed* value of $c$, the model is an ordinary linear regression of $y$ on the three columns
$1$, $t$, $(t-c)_+$, so it can be fit by least squares. Write

$$RSS(c) = \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \big[y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+\big]^2$$

for the residual sum of squares this regression achieves. $c$ itself does not enter linearly, so it
cannot be estimated by the same normal-equations argument; instead it is found by search:

1. Compute $RSS(c)$ for a grid of candidate values, $c \in \{1,2,\dots,n\}$.
2. Let $\hat c$ be the value that minimizes $RSS(c)$.
3. Fix $c=\hat c$ and run the linear regression of $y$ on $[1,\,t,\,(t-\hat c)_+]$ to get
   $\hat\beta_0,\hat\beta_1,\hat\beta_2$ and $\hat\sigma$.

## Least squares is maximum likelihood, again

Writing $S(\boldsymbol\beta,c) = \sum_t \big[y_t-\beta_0-\beta_1 t-\beta_2(t-c)_+\big]^2$, the
Gaussian likelihood for this model is

$$\prod_{t=1}^n \frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left[-\frac{1}{2\sigma^2}\big(y_t-\beta_0-\beta_1 t-\beta_2(t-c)_+\big)^2\right] \;\propto\; \sigma^{-n}\exp\!\left[-\frac{S(\boldsymbol\beta,c)}{2\sigma^2}\right].$$

This is exactly the likelihood of ordinary linear regression, with the design matrix $X$ replaced
by $X_c$ — the matrix with columns $1$, $t$, $(t-c)_+$, which itself depends on the unknown $c$.
For a fixed $c$, maximizing this over $\boldsymbol\beta$ is the same as minimizing the sum of
squares, so the maximum-likelihood $\boldsymbol\beta$ given $c$ is the least-squares $\hat\beta_c$;
and since $RSS(c)=\min_{\boldsymbol\beta}S(\boldsymbol\beta,c)$, maximizing over $c$ as well again
picks the minimizer of $RSS(c)$. So the joint MLE of $(\boldsymbol\beta,c)$ is precisely the
two-step least-squares procedure above — the same equivalence that holds in ordinary regression.

## A prior for the changepoint

The point estimate $\hat c$ says nothing about how confident to be that the kink is really there
and not, say, one time step over. Quantifying that requires a posterior over $c$, which requires a
prior. For $\beta_0,\beta_1,\beta_2,\sigma$, carry over the prior already used for ordinary linear
regression:

$$\beta_0,\beta_1,\beta_2,\log\sigma \overset{\text{iid}}{\sim} \text{Unif}[-C,C] \text{ as } C\to\infty,$$

which is the usual improper flat prior on the coefficients and on $\log\sigma$. $c$ is not a
regression coefficient — it is a location on the time axis — so it gets its own, independent prior.
Given the identifiability argument above, the natural choice restricts $c$ to the interior of the
observation window: either continuous, $c\sim\text{Unif}(1,n)$, or, if $c$ is only ever going to be
evaluated on the integer grid $\{1,\dots,n\}$, discrete, $c\sim\text{Unif}\{2,3,\dots,n-1\}$. Taking
$\beta_0,\beta_1,\beta_2,\log\sigma,c$ independent, the joint prior density is

$$f(\beta_0,\beta_1,\beta_2,\sigma,c) \;\propto\; \frac{1}{\sigma}\,I\{1<c<n\}\,I\{\sigma>0\}.$$

Multiplying by the likelihood gives the joint posterior over everything:

$$\text{posterior} \;\propto\; \sigma^{-n-1}\exp\!\left[-\frac{S(\boldsymbol\beta,c)}{2\sigma^2}\right] I\{1<c<n\}\,I\{\sigma>0\}.$$

## Marginalizing out $\boldsymbol\beta$ and $\sigma$

What is wanted is the posterior for $c$ *alone* — how much mass sits on each candidate changepoint,
regardless of the values of the other parameters. That means integrating $\boldsymbol\beta$ and
$\sigma$ out of the joint posterior above.

Write $S(\boldsymbol\beta,c) = \|y-X_c\boldsymbol\beta\|^2$, where

$$y=\begin{pmatrix}y_1\\ \vdots \\ y_n\end{pmatrix}, \qquad X_c = \begin{bmatrix}1 & 1 & (1-c)_+ \\ 1 & 2 & (2-c)_+ \\ \vdots & \vdots & \vdots \\ 1 & n & (n-c)_+\end{bmatrix}.$$

Let $\hat{\boldsymbol\beta}_c$ be the least-squares estimate for this fixed $c$, so $RSS(c) =
\|y-X_c\hat{\boldsymbol\beta}_c\|^2$. Because $\hat{\boldsymbol\beta}_c$ solves the normal
equations, the residual $y-X_c\hat{\boldsymbol\beta}_c$ is orthogonal to every column of $X_c$, and
hence to $X_c(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)$ for any $\boldsymbol\beta$. Writing
$y-X_c\boldsymbol\beta = (y-X_c\hat{\boldsymbol\beta}_c) - X_c(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)$
and expanding the squared norm, the cross term vanishes, leaving the Pythagorean identity

$$\|y-X_c\boldsymbol\beta\|^2 = \|y-X_c\hat{\boldsymbol\beta}_c\|^2 + (\boldsymbol\beta-\hat{\boldsymbol\beta}_c)^T X_c^T X_c(\boldsymbol\beta-\hat{\boldsymbol\beta}_c) = RSS(c) + (\boldsymbol\beta-\hat{\boldsymbol\beta}_c)^T X_c^T X_c(\boldsymbol\beta-\hat{\boldsymbol\beta}_c).$$

Substituting into the joint posterior splits it into a piece that depends on $c$ only through
$RSS(c)$, and a Gaussian kernel in $\boldsymbol\beta$ centred at $\hat{\boldsymbol\beta}_c$:

$$\text{posterior} \;\propto\; \sigma^{-n-1}\exp\!\left[-\frac{RSS(c)}{2\sigma^2}\right] \exp\!\left[-\frac{(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)^T X_c^T X_c(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)}{2\sigma^2}\right] I\{\sigma>0\}\,I\{1<c<n\}.$$

**Integrating out $\boldsymbol\beta$.** The Gaussian kernel has the form
$\exp[-\tfrac12(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)^T\Sigma^{-1}(\boldsymbol\beta-\hat{\boldsymbol\beta}_c)]$
with $\Sigma = \sigma^2(X_c^TX_c)^{-1}$, and the standard multivariate Gaussian integral

$$\int_{\mathbb R^p}\exp\!\left[-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)\right]dx = (2\pi)^{p/2}\sqrt{\det\Sigma}$$

removes it, contributing a factor $(2\pi)^{p/2}\sqrt{\det(\sigma^2(X_c^TX_c)^{-1})}$, where $p$ is
the number of columns of $X_c$ ($p=3$ here). Since $\det(\sigma^2 A) = \sigma^{2p}\det A$ for a
$p\times p$ matrix $A$, this factor is $\propto \sigma^p\,|X_c^TX_c|^{-1/2}$, and the posterior for
$(\sigma,c)$ becomes

$$\text{posterior}_{\sigma,c} \;\propto\; \sigma^{-n+p-1}\,|X_c^TX_c|^{-1/2}\exp\!\left[-\frac{RSS(c)}{2\sigma^2}\right] I\{\sigma>0\}\,I\{1<c<n\}.$$

**Integrating out $\sigma$.** This uses the same trick as in ordinary linear regression: for any
constant $A>0$,

$$\int_0^\infty \sigma^{-m-1}\exp\!\left(-\frac{A}{2\sigma^2}\right)d\sigma \;\propto\; A^{-m/2},$$

via the substitution $\sigma/\sqrt A = t$ (which rescales $\sigma$ out of the exponent, leaving an
integral over $t$ that does not depend on $A$). Applying it with $m=n-p$ and $A=RSS(c)$,

$$\int_0^\infty \sigma^{-n+p-1}\exp\!\left(-\frac{RSS(c)}{2\sigma^2}\right)d\sigma \;\propto\; \left(\frac{1}{RSS(c)}\right)^{(n-p)/2}.$$

## The posterior for the changepoint

Putting the two integrals together, the marginal posterior of $c$ is

$$\pi(c\mid y) \;\propto\; |X_c^TX_c|^{-1/2}\left(\frac{1}{RSS(c)}\right)^{(n-p)/2} I\{1<c<n\},$$

with $p$ the number of columns of $X_c$ ($p=3$ for the single-changepoint model). Two forces are
visible in this formula: smaller $RSS(c)$ (a better-fitting kink) raises the posterior, as expected,
but it is weighted by $|X_c^TX_c|^{-1/2}$, a term coming purely from marginalizing out
$\boldsymbol\beta$ that does not appear in the least-squares criterion at all. In practice, since
neither $RSS(c)$ nor $|X_c^TX_c|$ has a closed form as a function of $c$, this is not evaluated
analytically:

1. Take a grid of candidate values of $c$ (restricted to the interior range discussed above, e.g.
   $c\in\{2,\dots,n-1\}$).
2. At each grid point compute the unnormalized posterior $|X_c^TX_c|^{-1/2}\big(1/RSS(c)\big)^{(n-p)/2}$.
3. Normalize the resulting heights so they sum to one, giving an approximate probability for each
   grid value of $c$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Bar chart of the unnormalized posterior evaluated at three neighbouring candidate changepoints">
  <line x1="40" y1="180" x2="280" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <rect x="60" y="112.5" width="40" height="67.5" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="140" y="105" width="40" height="75" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="220" y="52.5" width="40" height="127.5" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="80" y="103" text-anchor="middle" font-size="12" fill="currentColor">4.5</text>
  <text x="160" y="95" text-anchor="middle" font-size="12" fill="currentColor">5</text>
  <text x="240" y="43" text-anchor="middle" font-size="12" fill="currentColor">8.5</text>
  <text x="80" y="198" text-anchor="middle" font-size="12" fill="currentColor">64</text>
  <text x="160" y="198" text-anchor="middle" font-size="12" fill="currentColor">65</text>
  <text x="240" y="198" text-anchor="middle" font-size="12" fill="currentColor">66</text>
  <text x="160" y="214" text-anchor="middle" font-size="12" fill="currentColor">candidate changepoint c</text>
</svg>
<figcaption>The unnormalized posterior evaluated at three neighbouring grid points; dividing each
height by the sum over the whole grid turns them into approximate posterior probabilities.</figcaption>
</figure>

This grid-and-normalize step is also what makes precise what "the posterior probability that
$c=65$" means. On a continuum $c\in(1,n)$, $\pi(c\mid y)$ is a probability *density*, so its value
at a single point such as $c=65$ is not itself a probability — the probability of landing on any
one exact real number is zero. It is only after committing to a grid (e.g. the integers) and
normalizing the heights on that grid that a genuine probability, such as $\mathbb P(c=65\mid
\text{data})$, is attached to a specific candidate value; a nearby value not on the grid, such as
$c=65.05$, has no such probability under that discretization at all.

## Two changepoints

The same construction extends directly to a model with two kinks:

$$y_t = \beta_0 + \beta_1 t + \beta_2(t-c_1)_+ + \beta_3(t-c_2)_+ + \varepsilon_t.$$

Define $RSS(c_1,c_2) = \min_{\boldsymbol\beta}\|y - X_{c_1,c_2}\boldsymbol\beta\|^2$ exactly as
before, now with a design matrix $X_{c_1,c_2}$ carrying four columns: $1$, $t$, $(t-c_1)_+$ and
$(t-c_2)_+$. Nothing in the marginalization argument above used the fact that there was only one
changepoint, so it goes through unchanged and gives

$$\pi(c_1,c_2\mid y) \;\propto\; |X_{c_1,c_2}^TX_{c_1,c_2}|^{-1/2}\left(\frac{1}{RSS(c_1,c_2)}\right)^{(n-p)/2},$$

now with $p=4$ (the number of columns of $X_{c_1,c_2}$).

## Sources

- Handwritten lecture notes, Stat 153 (UC Berkeley, Fall 2025), "Lecture Six" — the sole source for
  this chapter. Reconstructed by a model from a handwritten PDF with no text layer; the notes file
  itself flags every equation as unverified against the original scan, so it is worth checking the
  page images directly before citing a specific formula.
  `docs/statistics/berkeley/stat153/fall-2025/HandwrittenNotesLectureSix153248Fall2025.md`.
- No slide deck, transcript, or problem set was supplied alongside these notes.
- The Bayesian treatment of ordinary linear regression that this lecture builds on — the flat prior
  on $(\beta_0,\beta_1,\beta_2,\log\sigma)$ and the Pythagorean/orthogonal decomposition of the
  residual sum of squares — is referred to as "the previous prior we used in linear regression" and
  was covered in an earlier lecture not included in this material.

---

[← 67. Frequency and Breakpoint Estimation](67-frequency-and-breakpoint-estimation.md) · [Contents](index.md) · [69. Autoregression and Yule's AR(2) →](69-autoregression-and-yule-s-ar-2.md)
