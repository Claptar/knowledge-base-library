---
title: "1. Introduction to Asymptotic Theory"
course: "Berkeley Stat 210A"
chapter: 1
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Introduction to Asymptotic Theory

## What this covers

This chapter opens the asymptotic theory unit. Everything earlier in the course worked with the
*exact* distribution of a finite data set, exploiting special structure of the model — a complete
sufficient statistic, an exponential family, a Gaussian likelihood — to get exact answers. This
chapter asks what to do when that structure isn't enough, and answers it by approximating the
problem with a limit as the sample size $n \to \infty$. It builds the vocabulary needed to make
"approximately" precise: convergence in probability and in distribution, the law of large numbers
and central limit theorem, the continuous mapping theorem, Slutsky's theorem, and the delta
method. It assumes familiarity with exponential families, sufficiency, maximum likelihood, and
Fisher information from earlier in the course, and ordinary probability — expectations,
variances, independence, distribution functions.

## Why exact tools can fail: logistic regression

Take the linear regression setup from the previous lecture and swap the continuous response for a
binary one. With feature vectors $x_i \in \mathbb{R}^d$ and coefficients $\beta \in \mathbb{R}^d$, instead of
$y_i \stackrel{\text{ind.}}{\sim} N(\beta'x_i,\sigma^2)$ we now observe $y_i \stackrel{\text{ind.}}{\sim} \mathrm{Bern}(\mu(\beta'x_i))$,
where $\mu(\eta) = e^\eta/(1+e^\eta)$. Write $\mu_i = \mu(\beta'x_i)$ for the mean response and
$\eta_i = \log\frac{\mu_i}{1-\mu_i} = \beta'x_i$ for the linear predictor.

Unlike linear regression, there is no rotation of $y$ into a canonical basis that preserves the
model's structure — the rotated entries would be neither Bernoulli nor independent. The model is
still an exponential family, though:
$$
p_\beta(y\mid X) = \prod_{i=1}^n \mu_i^{y_i}(1-\mu_i)^{1-y_i}
= \exp\{\beta'X'y - A(\beta;X)\},
$$
with natural parameter $\beta$, complete sufficient statistic $X'y$, and normalizing constant
$A(\beta;X) = -\sum_i \log(1+e^{\beta'x_i})$, which depends only on $\beta$ and the (typically
fixed, or conditioned-on) design matrix $X$.

That exponential-family structure is exactly the kind of thing that made exact calculations work
before — but here it doesn't help.

- **No UMVU estimator can exist.** Any estimator $\hat\beta_j$ is a function on the finite sample
  space $\mathcal Y = \{0,1\}^n$, so it has some largest attainable value, and its expectation can
  never exceed that value — yet $\beta_j$ ranges over all of $\mathbb{R}$. A Bayes estimator is possible,
  but only by committing to a prior on $\beta$.
- **No nontrivial unbiased test exists**, typically. To test $H_0:\beta_j=0$, the exponential
  family suggests conditioning on $X_{-j}'y$ and rejecting for large conditional values of
  $X_j'y$. But if $X_j$ takes continuous values, $X_j'y = \sum_{i:y_i=1}x_{i,j}$ can recover the
  entire vector $y$ exactly, as long as the $2^n$ possible partial sums are distinct. Conditioning
  on $X_{-j}'y$ then leaves nothing random, and the only unbiased test left is the trivial one
  that ignores $y$ and rejects with probability $\alpha$.

So the exact machinery of the course — UMVU theory, exact conditional tests — runs into a wall
here. What rescues the problem is size: if $n$ is large, general-purpose *asymptotic* methods
produce very good estimators, tests, and confidence intervals, even though nothing about them is
exact.

Define the maximum likelihood estimator
$$
\hat\beta_{\mathrm{MLE}} = \operatorname*{argmax}_{\beta\in\mathbb{R}^d} p_\beta(y\mid X)
= \operatorname*{argmax}_{\beta\in\mathbb{R}^d} \beta'X'y - A(\beta;X),
$$
which is easy to compute because the log-likelihood is concave. A future lecture will show that
under mild conditions,
$$
\hat\beta_{\mathrm{MLE}} \approx N_d\big(\beta, J(\beta)^{-1}\big), \qquad
J(\beta) = \operatorname{Var}_\beta\big(\nabla\ell(\beta;y,X)\big) = -\mathbb{E}_\beta \nabla^2\ell(\beta;y,X),
$$
the Fisher information matrix. That is: for large $n$, $\hat\beta_{\mathrm{MLE}}$ is approximately
unbiased and Gaussian, with covariance matching the Cramér–Rao bound. What is more, the *observed*
information — minus the Hessian at the MLE, a quantity you can actually compute from data — is a
good stand-in for the (generally unknown) Fisher information at the true $\beta$:
$$
\widehat\Sigma(y,X) = \big(-\nabla^2\ell(\hat\beta_{\mathrm{MLE}};y,X)\big)^{-1}
\approx \Sigma(\beta) = J(\beta)^{-1}.
$$
For a single coordinate, $\hat\beta_j - \beta_j \approx N(0,\sigma_j^2(\beta))$ for
$\sigma_j^2(\beta) = \Sigma_{jj}(\beta)$, so
$$
Z_j = \frac{\hat\beta_j-\beta_j}{\hat\sigma_j} \approx N(0,1), \qquad \hat\sigma_j^2 = \widehat\Sigma_{jj},
$$
which is exactly what is needed for a test of $H_0:\beta_j=0$ or a confidence interval
$\hat\beta_j \pm z_{\alpha/2}\sqrt{\widehat\Sigma_{jj}}$.

None of this needs $n$ to be astronomically large. Simulating the model $\eta_i = \beta_0+\beta_1
x_i$ with $x_i \sim \mathrm{Unif}(0,1)$, $\beta_0=-2$, $\beta_1=4$, and only $n=100$, $10^4$
replications show the sampling distribution of $\hat\beta_1$ tracking the claimed normal
approximation closely, and the studentized statistic $Z_1 = (\hat\beta_1-\beta_1)/\hat\sigma_1$
tracking a standard normal — though how good the approximation is at a given $n$ depends on the
parameters.

The claim "$\hat\beta_{\mathrm{MLE}}$ approximately follows a Gaussian distribution" is doing a lot
of work in that argument, and it applies well beyond logistic regression. Before it can be proved,
it has to be made precise: what does it mean for one distribution to be approximated by another as
$n\to\infty$?

## Two notions of convergence

Let $X_1,X_2,\dots$ be random variables (or vectors) on a space $\mathcal{X}$ with a distance
$\|x-y\|$ — in practice $\mathcal{X} \subseteq \mathbb{R}^d$, and since all norms on $\mathbb{R}^d$ are equivalent, it
won't matter which one is used.

**Convergence in probability.** $X_n$ converges in probability to a constant $c$, written
$X_n \xrightarrow{p} c$, if
$$
\mathbb{P}(\|X_n-c\| > \epsilon) \to 0 \qquad \text{for every } \epsilon>0.
$$
This is the notion behind **consistency**: in a sequence of statistical models
$\mathcal{P}_n = \{P_{n,\theta}:\theta\in\Theta\}$ with $X_n \sim P_{n,\theta}$, an estimator $\hat\theta_n$
is consistent for $g(\theta)$ if $\hat\theta_n \xrightarrow{p} g(\theta)$, i.e.
$\mathbb{P}_\theta(|\hat\theta_n - g(\theta)| > \epsilon) \to 0$ for every $\epsilon$. (The index $n$ is
usually dropped once the sequence is understood.)

**Convergence in distribution.** $X_n$ converges in distribution to a random variable $X$, written
$X_n \xrightarrow{d} X$ (also called *weak convergence*), if
$$
\mathbb{E}[f(X_n)] \to \mathbb{E}[f(X)] \qquad \text{for every bounded continuous } f:\mathcal{X}\to\mathbb{R}.
$$
For real-valued $X_n, X$ with $F_n(x) = \mathbb{P}(X_n\le x)$, $F(x)=\mathbb{P}(X\le x)$, this is equivalent to
pointwise convergence of the CDFs *at every point where the limit is continuous*:
$$
X_n \xrightarrow{d} X \iff F_n(x) \to F(x) \ \text{ for every } x \text{ at which } F \text{ is continuous.}
$$

The restriction to continuity points is not a technicality that can be dropped. Take
$$
F_n(x) = \begin{cases} 1 & x>0\\ 1-\tfrac1n & x=0 \\ 0 & x<0\end{cases}, \qquad
F(x) = \begin{cases} 1 & x>0 \\ 0 & x \le 0.\end{cases}
$$
Away from $x=0$, $F_n(x)=F(x)$ exactly for every $n$. At $x=0$ itself, $F_n(0)=1-\tfrac1n \to 1$,
not $F(0) = 0$ — the point-mass CDFs *disagree in the limit* exactly at $0$. But $x=0$ is precisely
the one point where $F$ is discontinuous, so this mismatch is invisible to the definition of
convergence in distribution: $X_n \xrightarrow{d} X$ still holds.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Two step-function CDFs that differ only at their single point of discontinuity">
  <line x1="30" y1="175" x2="320" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="170" y1="20" x2="170" y2="175" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3"/>
  <text x="170" y="190" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="320" y="190" text-anchor="middle" font-size="12" fill="currentColor">x</text>

  <line x1="40" y1="155" x2="170" y2="155" stroke="currentColor" stroke-width="2"/>
  <circle cx="170" cy="155" r="3.5" fill="currentColor"/>
  <line x1="170" y1="45" x2="310" y2="45" stroke="currentColor" stroke-width="2"/>
  <circle cx="170" cy="45" r="3.5" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="38" text-anchor="end" font-size="12" fill="currentColor">F</text>

  <circle cx="170" cy="72" r="3.5" fill="currentColor"/>
  <line x1="170" y1="72" x2="196" y2="72" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="200" y="76" font-size="12" fill="currentColor">F_n(0) = 1 - 1/n</text>
</svg>
<figcaption>F_n(0) = 1 - 1/n converges to 1, not to F(0) = 0, yet X_n still converges to X in
distribution: x = 0 is exactly the point where F is discontinuous, and only continuity points of
the limit matter.</figcaption>
</figure>

**Convergence in probability is the stronger notion.** If $X_n \xrightarrow{p} c$, then $X_n \xrightarrow{d} c$
(where $c$ is read as a degenerate random variable). The two directions of that equivalence are
both worth seeing, because together they show convergence in probability *to a constant* and
convergence in distribution *to a constant* actually coincide.

One direction uses a specific test function. Let $f_\epsilon(x) = \max\{1-\|x-c\|/\epsilon, 0\}$ —
a "tent" that equals $1$ at $c$, decreases linearly, and hits $0$ once $\|x-c\|\ge\epsilon$; it is
bounded and continuous. Since $1-f_\epsilon(x) = 1$ whenever $\|x-c\|>\epsilon$ and
$1-f_\epsilon(x)\ge 0$ always,
$$
\mathbb{P}(\|X_n-c\|>\epsilon) \le \mathbb{E}[1-f_\epsilon(X_n)].
$$
So if $X_n \xrightarrow{d} c$ (giving $\mathbb{E}[f_\epsilon(X_n)]\to f_\epsilon(c)=1$, hence
$\mathbb{E}[1-f_\epsilon(X_n)]\to0$), the right side vanishes and $X_n \xrightarrow{p} c$ follows.

The other direction — the one usually quoted as "convergence in probability implies convergence
in distribution" — needs an arbitrary bounded continuous $f$, not just $f_\epsilon$. Fix
$\epsilon>0$ and, by continuity of $f$ at $c$, choose $\delta>0$ so that $\|x-c\|<\delta$ implies
$|f(x)-f(c)|<\epsilon$. Splitting on whether $X_n$ landed inside or outside that ball,
$$
|\mathbb{E}[f(X_n)] - f(c)| \le \big|\mathbb{E}[(f(X_n)-f(c))\mathbf 1_{\|X_n-c\|<\delta}]\big|
+ \big|\mathbb{E}[(f(X_n)-f(c))\mathbf 1_{\|X_n-c\|\ge\delta}]\big|
\le \epsilon + 2\sup|f|\cdot \mathbb{P}(\|X_n-c\|\ge\delta).
$$
Since $X_n \xrightarrow{p} c$, the second term vanishes as $n\to\infty$, and $\epsilon$ was arbitrary, so
$\mathbb{E}[f(X_n)] \to f(c)$ for every such $f$ — exactly $X_n \xrightarrow{d} c$.

## The two workhorse limits

Two classical results will be used repeatedly without re-proving them. For $\bar X_n =
\frac1n\sum_{i=1}^n X_i$:

- **Law of large numbers.** If $\mathbb{E}|X_i|<\infty$ and $\mathbb{E} X_i = \mu$, then $\bar X_n \xrightarrow{p} \mu$.
- **Central limit theorem.** If $\operatorname{Var}(X_i) = \sigma^2 < \infty$, then
  $\sqrt n(\bar X_n - \mu) \xrightarrow{d} N(0,\sigma^2)$.

(Stronger versions of both exist — weaker moment conditions, dependent data — but this is enough
for what follows.)

## Continuous mapping and Slutsky

Two tools convert convergence statements about $X_n$ into convergence statements about functions
or combinations of $X_n$.

**Continuous mapping theorem.** Let $g$ be continuous. Then:

1. $X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)$.
2. $X_n \xrightarrow{p} c \implies g(X_n) \xrightarrow{p} g(c)$.

The proof is immediate from the definitions: if $f$ is bounded continuous, so is $f\circ g$, so
$X_n \xrightarrow{d} X$ gives $\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$ directly. The probability statement is the
special case $X \equiv c$.

**Slutsky's theorem.** Suppose $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{p} c$. Then:

1. $X_n + Y_n \xrightarrow{d} X + c$,
2. $X_n Y_n \xrightarrow{d} cX$,
3. $X_n/Y_n \xrightarrow{d} X/c$, provided $c \ne 0$.

The idea is to first show the *pair* $(X_n,Y_n) \xrightarrow{d} (X,c)$ — which holds because $Y_n$
collapses onto the constant $c$ — and then apply the continuous mapping theorem to the appropriate
function of the pair: $(x,y)\mapsto x+y$, $(x,y)\mapsto xy$, or $(x,y)\mapsto x/y$.

Slutsky's theorem needs one of the two limits to be a *constant*. It is not true in general that
$X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{d} Y$ imply $X_n+Y_n \xrightarrow{d} X+Y$: the distribution of the sum
depends on the joint law of $(X_n,Y_n)$, and marginal convergence says nothing about that joint
law — the correlation between $X_n$ and $Y_n$ in the limit is simply not determined by the two
marginals.

## The delta method

Often the object of interest is not $X_n$ itself but some function of it — a transformed
parameter, a ratio of estimators. The delta method says such a function inherits a CLT, with the
variance scaled by the (squared) derivative.

**Theorem (delta method).** Suppose $\sqrt n(X_n-\mu) \xrightarrow{d} N(0,\sigma^2)$ and $f$ is
differentiable at $\mu$. Then
$$
\sqrt n\big(f(X_n)-f(\mu)\big) \xrightarrow{d} N\big(0,[f'(\mu)]^2\sigma^2\big).
$$

*Proof.* Differentiability at $\mu$ gives $f(X_n) = f(\mu) + f'(\mu)(X_n-\mu) + o(X_n-\mu)$, so
$$
\sqrt n\big(f(X_n)-f(\mu)\big) = f'(\mu)\sqrt n(X_n-\mu) + \sqrt n\, o(X_n-\mu).
$$
Since $\sqrt n(X_n-\mu) \xrightarrow{d} N(0,\sigma^2)$, in particular $X_n-\mu = O_p(n^{-1/2})$, so the
remainder is $o(X_n-\mu) = o_p(n^{-1/2})$ and $\sqrt n\cdot o_p(n^{-1/2}) \xrightarrow{p} 0$. Applying
Slutsky's theorem to the sum of a $\xrightarrow{d}$ term and a $\xrightarrow{p} 0$ term gives
$f'(\mu)\sqrt n(X_n-\mu) + o_p(1) \xrightarrow{d} f'(\mu)\cdot N(0,\sigma^2) = N(0,[f'(\mu)]^2\sigma^2)$. $\square$

Informally: if $X \sim N(\mu,\sigma^2/n)$, then $f(X) \sim N\big(f(\mu),\, [f'(\mu)]^2\sigma^2/n +
o(1/n)\big)$ — a linear approximation to $f$ near $\mu$, propagated through the normal.

**Multivariate version.** If $\sqrt n(X_n-\mu) \xrightarrow{d} N(0,\Sigma)$ for $X_n,\mu\in\mathbb{R}^d$, and
$f:\mathbb{R}^d\to\mathbb{R}^k$ has derivative (Jacobian) $Df(\mu)$ at $\mu$, then
$$
\sqrt n\big(f(X_n)-f(\mu)\big) \xrightarrow{d} N\big(0, Df(\mu)\,\Sigma\, Df(\mu)^T\big),
$$
or informally, for $k=1$, $f(X_n) \sim N\big(f(\mu),\, Df(\mu)\Sigma Df(\mu)^T/n + o(1/n)\big)$.

### Worked example: the ratio of two sample means

Let $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} \mathrm{Unif}[0,\theta]$ and $Y_1,\dots,Y_m \stackrel{\text{i.i.d.}}{\sim}
\mathrm{Unif}[0,\theta]$ independently. What is the large-sample distribution of
$T_n = \bar X/\bar Y$?

Each mean and variance is $\mathbb{E} X_i = \theta/2$, $\operatorname{Var}(X_i) = \theta^2/12$, so by the CLT,
$$
\sqrt n\Big(\bar X - \tfrac\theta2\Big) \xrightarrow{d} N\Big(0,\tfrac{\theta^2}{12}\Big), \qquad
\sqrt m\Big(\bar Y - \tfrac\theta2\Big) \xrightarrow{d} N\Big(0,\tfrac{\theta^2}{12}\Big),
$$
independently. If $n,m\to\infty$ together with $n/m \to c$, rescaling the second statement by
$\sqrt{n/m} \to \sqrt c$ gives $\sqrt n(\bar Y - \theta/2) \xrightarrow{d} N(0, c\theta^2/12)$, and by
independence the pair converges jointly:
$$
\sqrt n\begin{pmatrix}\bar X - \theta/2 \\ \bar Y - \theta/2\end{pmatrix}
\xrightarrow{d} N\left(0, \begin{pmatrix}\theta^2/12 & 0 \\ 0 & c\,\theta^2/12\end{pmatrix}\right).
$$
Apply the multivariate delta method to $g(x,y) = x/y$ at $(\theta/2,\theta/2)$, where
$g(\theta/2,\theta/2) = 1$ and
$$
g_x\Big(\tfrac\theta2,\tfrac\theta2\Big) = \frac{1}{\theta/2} = \frac2\theta, \qquad
g_y\Big(\tfrac\theta2,\tfrac\theta2\Big) = -\frac{\theta/2}{(\theta/2)^2} = -\frac2\theta.
$$
The asymptotic variance is $\big(\tfrac2\theta\big)^2\cdot\tfrac{\theta^2}{12} +
\big(\tfrac2\theta\big)^2\cdot c\,\tfrac{\theta^2}{12} = \tfrac13(1+c)$, so
$$
\sqrt n(T_n - 1) \xrightarrow{d} N\Big(0, \tfrac13\big(1+\tfrac nm\big)\Big),
$$
matching the more elementary route of just adding the (non-normalized) variance contributions of
$\bar X$ and $\bar Y$ through $g$: $\operatorname{Var}(T_n) \approx \big(\tfrac2\theta\big)^2\tfrac{\theta^2}{12n}
+ \big(\tfrac2\theta\big)^2\tfrac{\theta^2}{12m} = \tfrac1{3n}+\tfrac1{3m}$.

**A check, and where the delta method breaks down.** Writing $\bar X = \tfrac\theta2(1+U_n)$ and
$\bar Y = \tfrac\theta2(1+V_n)$ with $U_n = O_p(n^{-1/2})$, $V_n=O_p(m^{-1/2})$ re-expresses the
ratio around the point $(0,0)$ instead of $(\theta/2,\theta/2)$:
$$
T_n = \frac{1+U_n}{1+V_n} = 1 + O_p(n^{-1/2}+m^{-1/2}),
$$
the same order of approximation as before — re-centering the expansion doesn't change the answer.
It is worth noticing, though, that a step like $1/(1+n^{-1/2}) \to 1$ here is just the continuous
mapping theorem applied to the *deterministic* sequence $n^{-1/2}\to0$; it is not an instance of
Slutsky's theorem, which is about a genuinely random numerator divided by something converging in
probability to a nonzero constant. The two theorems can look interchangeable in a calculation like
this one and are not.

This example is also the cleanest place to see why the delta method needs a nonzero derivative.
By the continuous mapping theorem applied to $\sqrt n(T_n-1)\xrightarrow{d} N(0,\sigma^2)$ (with $\sigma^2
= \tfrac13(1+n/m)$ above) and $g(x)=x^2$,
$$
n(T_n-1)^2 \xrightarrow{d} \sigma^2\chi_1^2.
$$
Trying to get this directly from the (first-order) delta method applied to $h(t)=(t-1)^2$ at
$\mu=1$ fails, because $h'(1) = 0$: the linear term vanishes and carries no information about the
limit. In general, when $f'(\mu)\ne0$ fails, go to the next term of the Taylor expansion:
$$
f(X_n) = f(\mu) + f'(\mu)(X_n-\mu) + \tfrac12 f''(\mu)(X_n-\mu)^2 + O_p(n^{-3/2}).
$$
If $f'(\mu)=0$, the second-order term dominates, and — since $\sqrt n(X_n-\mu)\xrightarrow{d}
N(0,\sigma^2)$ makes $n(X_n-\mu)^2 \xrightarrow{d} \sigma^2\chi_1^2$ by continuous mapping —
$$
n\big(f(X_n)-f(\mu)\big) \xrightarrow{d} \tfrac12 f''(\mu)\,\sigma^2\,\chi_1^2.
$$

## Sources

- Course reader, *Introduction to Asymptotic Theory* / *Convergence* / *Delta Method*
  (`reader/asymptotics.qmd` / `.html`), UC Berkeley STAT 210A, Fall 2024, Fall 2025, and Fall 2026
  offerings — CC BY 4.0. The three offerings' reader text is essentially identical; this chapter
  follows the Fall 2024 markdown conversion as the cleanest rendering
  (`docs/statistics/berkeley/stat210a/fall-2024/reader/asymptotics/01-introduction-to-asymptotic-theory.md`,
  `02-convergence.md`, `03-delta-method.md` in the library), cross-checked against the Fall 2025
  (`fall-2025/reader/asymptotics/…`, duplicated under `fall-2025/units/reader/asymptotics/…`) and
  Fall 2026 (`fall-2026/reader/asymptotics/…`) conversions, which carry the same content.
- No slide deck, transcript, or problem set was supplied alongside this reader for this lecture.
- The reader's proof that $\hat\beta_{\mathrm{MLE}}$ is asymptotically normal is explicitly
  deferred to "a future lecture" and is not contained in this material.

---

[Contents](index.md) · [2. Why Bayesian Computation Needs MCMC →](02-why-bayesian-computation-needs-mcmc.md)
