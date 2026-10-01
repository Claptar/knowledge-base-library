---
title: "7. Gaussian sequence model"
course: "Berkeley Stat 210A"
chapter: 7
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Gaussian sequence model

## What this covers

This chapter asks how to estimate a $d$-dimensional Gaussian mean $\theta$ under squared-error
loss, and whether the obvious estimator — the data itself — can be beaten. It builds, from
scratch, the machinery (Stein's Lemma and Stein's Unbiased Risk Estimator) needed to answer that
question, and arrives at the James-Stein estimator: the fact that in three or more dimensions the
sample itself is *inadmissible*. It assumes the reader already has the Gaussian sequence model,
sufficiency reductions, and the vocabulary of decision theory (UMVU, Bayes, minimax) from earlier
in the course, together with the multivariate normal and chi-squared distributions and enough
matrix calculus to read a Jacobian.

## The Gaussian sequence model

Recall the *Gaussian sequence model*:
$$X \sim N_d(\theta, I_d), \qquad \theta \in \mathbb{R}^d.$$
This is more general than it looks. If $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} N_d(\theta,\sigma^2 I_d)$
for known $\sigma^2>0$, a sufficiency reduction gives
$$Z = \frac{1}{\sigma\sqrt n}\sum_i X_i \sim N_d(\theta, I_d),$$
so nothing is lost by working with the "vanilla" single-observation model and translating results
back through this transformation.

Throughout, the loss is squared error summed over coordinates,
$$L(\theta,\delta) = \|\delta(X)-\theta\|^2 = \sum_j\big(\delta_j(X)-\theta_j\big)^2,$$
and the risk of an estimator $\delta$ is $\mathrm{MSE}(\theta,\delta) = \mathbb{E}_\theta\|\delta(X)-\theta\|^2$.

The obvious estimator is $\delta_0(X) = X$ itself, and it comes with three independent
certificates of optimality: it is the UMVU estimator of $\theta$; it is the objective Bayes
estimator, since the flat (improper) prior on $\theta$ coincides with the Jeffreys prior, as it
does for any location model; and it is the maximum likelihood estimator. With three such
different arguments converging on the same answer, $X$ looks unbeatable. The rest of this chapter
is about why, once $d\ge 3$, it is not.

## Shrinkage: Bayes, hierarchical, and empirical

If we put a prior $\theta_i \stackrel{\text{iid}}{\sim} N(0,\tau^2)$ on the coordinates, the Bayes
estimator is $\frac{\tau^2}{1+\tau^2}X$. This suggests thinking of the whole family of *linear
shrinkage estimators*
$$\delta_\zeta(X) = (1-\zeta)X, \qquad \zeta \in [0,1],$$
where $\zeta$ is a *shrinkage parameter*: $\zeta = 0$ recovers $X$, and $\zeta = 1/(1+\tau^2)$
recovers the Bayes estimator for a known $\tau^2$.

If $\tau^2$ itself is uncertain, hierarchical Bayes puts a further prior on it and averages: $\zeta$
acquires a posterior given $X$, and the resulting estimator is
$$\delta(X) = \big(1-\mathbb{E}[\zeta\mid X]\big)X = \delta_{\hat\zeta_{\mathrm{Bayes}}(X)}(X),$$
i.e. we estimate the shrinkage factor from the whole data set and plug it back in as a
data-adaptive tuning parameter.

This is one instance of a general pattern that recurs whenever we have many parallel,
structurally identical estimation problems,
$$X_i \sim p_{\theta_i}(x), \qquad \theta_i \sim G, \quad i=1,\dots,d,$$
and it is worth separating the cases:

- a single draw $\theta \sim G$ makes a prior hard to justify on its own;
- with a lot of information already in the likelihood, the prior barely matters;
- with $\theta_i \sim G$ and only $X_i$ informative about $\theta_i$, the prior genuinely helps;
- with *many* such parallel draws, we can even check whether the assumed prior fits.

The last two points motivate a *hybrid*, or **empirical Bayes**, approach: rather than putting a
further prior on $G$ and integrating it out (full hierarchical Bayes), treat $G$ as an unknown
fixed quantity, estimate it from the data, and plug the estimate in as though it were known. The
situation where this pays off is exactly the many-parallel-problems case: a single $\theta_i$ has
almost no information behind it, but pooling across all $d$ problems lets the data itself pin down
the shape of the population $G$ the $\theta_i$ are drawn from.

An empirical Bayes approach to $\zeta$ can use any reasonable point estimator in place of the
Bayes posterior mean — the MLE, say, or the UMVU estimator. For $d \ge 3$, the UMVU estimator of
$\zeta = 1/(1+\tau^2)$ turns out to be
$$\hat\zeta_{\mathrm{UMVU}}(X) = \frac{d-2}{\|X\|^2}.$$
This rests on the identity
$$\mathbb{E}[1/Y] = \frac{1}{d-2}, \qquad Y \sim \chi^2_d,\ d>2$$
($\chi^2_d$ being $\mathrm{Gamma}(d/2,2)$), whose proof is deferred to separate handwritten notes
not reproduced here. Plugging $\hat\zeta_{\mathrm{UMVU}}$ into the linear shrinkage family gives
the **James-Stein estimator**,
$$\delta_{\mathrm{JS}}(X) = \left(1-\frac{d-2}{\|X\|^2}\right)X = \delta_{\hat\zeta_{\mathrm{UMVU}}}(X).$$

A completely different, purely method-of-moments route arrives at almost the same place. For the
explicit model $\theta_i \sim N(0,\tau^2)$, $X_i \mid \theta_i \sim N(\theta_i,1)$, the marginal is
$X \sim N(0,(\tau^2+1)I_d)$, so $\|X\|^2$ is sufficient for $\tau^2$, with $\mathbb{E}\|X\|^2 =
d(\tau^2+1)$. Matching moments gives $\hat\tau^2 = \max\{\|X\|^2/d - 1,\, 0\}$, and plugging this
into the Bayes shrinkage factor $\tau^2/(\tau^2+1)$ gives
$$\hat\delta(X) = \left(1-\frac{d}{\|X\|^2}\right)_+ X.$$
This has exactly the shape of $\delta_{\mathrm{JS}}$, but with $d$ in place of $d-2$: a reminder
that "shrink by roughly $1/\|X\|^2$" is the robust idea, while the precise constant depends on
which estimator of the shrinkage factor is used. For $d$ large the two estimators are close, and
either should be nearly optimal.

## The James-Stein paradox

For $d \ge 3$, the James-Stein estimator strictly beats the natural estimator, **everywhere**:
$$\mathrm{MSE}(\theta,\delta_{\mathrm{JS}}) < \mathrm{MSE}(\theta,X) = d \qquad \text{for every } \theta \in \mathbb{R}^d.$$
Equivalently, $\delta_0(X)=X$ is *inadmissible* under squared error loss once $d\ge 3$: there is an
estimator that never does worse, and sometimes does strictly better, at every possible value of
the parameter. (The proof, via SURE, comes later in this chapter; for now, take the inequality as
given and unpack why it is startling.)

It would not be surprising for a Bayes estimator to beat the UMVU estimator *on average* with
respect to some prior over $\theta$ — that is close to the definition of what a good prior buys
you. What is startling is that this holds for *every fixed* $\theta$, including values of $\theta$
that have nothing to do with any prior we used to motivate $\delta_{\mathrm{JS}}$. Recall that $X$
already carries three independent optimality certificates — UMVU, objective Bayes, and (as we
will see later in the course) minimax — and none of them survive $d \ge 3$.

There is also nothing special about shrinking toward $0$. For any fixed $\theta_0 \in \mathbb{R}^d$,
$$\tilde\delta(X) = \theta_0 + \left(1-\frac{d-2}{\|X-\theta_0\|^2}\right)(X-\theta_0)$$
also dominates $X$. This follows from translation invariance: set $Y = X-\theta_0 \sim
N_d(\mu,I_d)$ with $\mu = \theta-\theta_0$; then $\tilde\delta$ is exactly the James-Stein
estimator for $\mu$ built from $Y$, translated back. So $\tilde\delta$ dominates $\hat\mu_0(Y)=Y$
as an estimator of $\mu$, which is the same statement as $\tilde\delta$ dominating $X$ as an
estimator of $\theta$ — and since $\theta_0$ was arbitrary, we could shrink toward *any* fixed
point and still improve on $X$ at every $\theta$. Since we might as well take $n=1$ (by the
sufficiency reduction above), this is really a statement about a single $d$-dimensional Gaussian
observation: whatever $\theta$ actually is — even something like $\theta = (50, 10, 94, \dots)$,
with no structure relating its coordinates — shrinking toward $0$, or toward anything else, helps.

This result was a shock when it first appeared in the 1950s. For a long time it was treated as a
curiosity — a strange corner case of decision theory rather than practical advice. It is now
understood to carry a much broader message: shrinkage is generally a good idea in
higher-dimensional estimation problems, even without any Bayesian model to justify it, and even
when the coordinates being shrunk together have nothing to do with one another.

## Why shrinkage should help: a frequentist derivation

Even without any Bayesian machinery, we can ask directly: among the linear shrinkage estimators
$\delta_\zeta(X) = (1-\zeta)X$, which $\zeta$ minimizes the frequentist risk, for a *given* (but
unknown) $\theta$? For a single coordinate, the bias-variance decomposition gives
$$\mathbb{E}_\theta\big[(\theta_i-\delta_i(X))^2\big] = \big(\theta_i - \mathbb{E}_\theta[(1-\zeta)X_i]\big)^2 + \mathrm{Var}_\theta\big[(1-\zeta)X_i\big] = (\zeta\theta_i)^2 + (1-\zeta)^2,$$
and summing over the $d$ coordinates,
$$\mathrm{MSE}(\theta;\delta_\zeta) = \zeta^2\|\theta\|^2 + d(1-\zeta)^2,$$
squared bias plus variance. This is a quadratic in $\zeta$ with positive leading coefficient, so
it is minimized where its derivative vanishes:
$$0 = 2\zeta\|\theta\|^2 - 2(1-\zeta)d \quad\Longrightarrow\quad \zeta^*(\theta) = \frac{d}{d+\|\theta\|^2} = \frac{1}{1+\|\theta\|^2/d},$$
which has exactly the shape of the Bayes-optimal $1/(1+\tau^2)$, with $\|\theta\|^2/d$ playing the
role of $\tau^2$.

Two things follow. First, $\zeta^*(\theta) > 0$ always: *some* shrinkage helps, no matter what
$\theta$ is. Second, the correct amount of shrinkage depends on $\|\theta\|^2$, which we don't
know — as $\|\theta\|^2 \to \infty$ the correct $\zeta$ goes to $0$, so any fixed $\zeta$ is wrong
(too aggressive) for large enough $\theta$. What we need is an estimator that estimates roughly
the right amount of shrinkage from the data itself, without ever overshooting badly — and to check
whether an estimator with a data-dependent $\hat\zeta(X)$ succeeds at this, we need a way to
compute its risk that doesn't require already knowing $\theta$. That tool is Stein's Unbiased Risk
Estimator, and it is built from Stein's Lemma.

## Stein's Lemma

**Theorem (univariate).** Let $X \sim N(\theta,\sigma^2)$ and let $h:\mathbb{R}\to\mathbb{R}$ be
differentiable with $\mathbb{E}|h'(X)| < \infty$. Then
$$\mathrm{Cov}(X,h(X)) = \mathbb{E}[(X-\theta)h(X)] = \sigma^2\,\mathbb{E}[h'(X)].$$

*Proof.* First take $\theta=0,\sigma^2=1$. Using $\phi'(x) = -x\phi(x)$ for the standard normal
density,
$$\mathbb{E}[Xh(X)] = \int_{-\infty}^{\infty} xh(x)\phi(x)\,dx = -\int_{-\infty}^{\infty} h(x)\phi'(x)\,dx = \int_{-\infty}^{\infty} h'(x)\phi(x)\,dx = \mathbb{E}[h'(X)],$$
integrating by parts and discarding the boundary term $\big[-h(x)\phi(x)\big]_{-\infty}^{\infty}$
(a fully careful account of this step, splitting the integral at $0$ so that a possibly nonzero
$h(0)$ causes no trouble, is left to handwritten notes not reproduced here). For general
$\theta,\sigma^2$, write $X = \theta+\sigma Z$ with $Z\sim N(0,1)$, and apply the $\theta=0,
\sigma^2=1$ case to $k(z) := h(\theta+\sigma z)$, whose derivative is $k'(z) = \sigma h'(\theta+\sigma z)$:
$$\mathbb{E}[(X-\theta)h(X)] = \sigma\,\mathbb{E}[Zh(\theta+\sigma Z)] = \sigma\,\mathbb{E}[Zk(Z)] = \sigma\,\mathbb{E}[k'(Z)] = \sigma^2\,\mathbb{E}[h'(\theta+\sigma Z)] = \sigma^2\,\mathbb{E}[h'(X)]. \qquad\blacksquare$$

The content of the lemma: for a Gaussian variable, the covariance of $X$ with a nonlinear function
of itself reduces to an expected derivative — no fresh integration by parts is needed every time
we want a new such covariance.

We will need the multivariate version. For $h:\mathbb{R}^d\to\mathbb{R}^d$ differentiable, write
$Dh \in \mathbb{R}^{d\times d}$ for its Jacobian, $(Dh(x))_{ij} = \partial h_i/\partial x_j(x)$, and
$\|A\|_F = \big(\sum_{ij}A_{ij}^2\big)^{1/2}$ for the **Frobenius norm** of a matrix $A$.

**Theorem (multivariate).** Let $X \sim N_d(\theta,\sigma^2 I_d)$ and $h:\mathbb{R}^d\to\mathbb{R}^d$
differentiable with $\mathbb{E}\|Dh(X)\|_F < \infty$. Then
$$\mathbb{E}[(X-\theta)^Th(X)] = \sigma^2\,\mathbb{E}[\mathrm{tr}(Dh(X))] = \sigma^2\sum_i \mathbb{E}\left[\frac{\partial h_i}{\partial x_i}(X)\right].$$

The proof reduces to the univariate case coordinate by coordinate. Condition on $X_{-i}$ (all
coordinates but the $i$-th): given $X_{-i}=x_{-i}$, the coordinate $X_i$ is still $N(\theta_i,
\sigma^2)$ (the coordinates of $X$ are independent), and $h_i(X)$, viewed as a function of $x_i$
alone with the rest held fixed, is exactly the kind of univariate function the lemma applies to.
So
$$\mathbb{E}\big[(X_i-\theta_i)h_i(X)\mid X_{-i}\big] = \sigma^2\,\mathbb{E}\left[\frac{\partial h_i}{\partial x_i}(X) \,\middle|\, X_{-i}\right],$$
and taking expectations over $X_{-i}$ and summing over $i=1,\dots,d$ gives the claim, since
$\sum_i (X_i-\theta_i)h_i(X) = (X-\theta)^Th(X)$ and $\sum_i \partial h_i/\partial x_i(X) =
\mathrm{tr}(Dh(X))$. (The same argument, kept in matrix form rather than summed, gives the
outer-product identity $\mathbb{E}[(X-\theta)h(X)^T] = \sigma^2\,\mathbb{E}[Dh(X)]$, of which the
trace identity above is just the trace of both sides.)

## Stein's Unbiased Risk Estimator (SURE)

Write any estimator as a correction to $X$: $\delta(X) = X - h(X)$ for some differentiable
$h:\mathbb{R}^d\to\mathbb{R}^d$. Expanding the squared error (taking $\sigma^2=1$),
$$\|\delta(X)-\theta\|^2 = \|(X-\theta)-h(X)\|^2 = \|X-\theta\|^2 - 2(X-\theta)^Th(X) + \|h(X)\|^2.$$
Taking expectations, $\mathbb{E}_\theta\|X-\theta\|^2 = d$, and Stein's Lemma turns the cross term
into $2\,\mathbb{E}_\theta[\mathrm{tr}(Dh(X))]$, giving
$$\mathrm{MSE}(\theta,\delta) = \mathbb{E}_\theta\Big[\,d - 2\,\mathrm{tr}(Dh(X)) + \|h(X)\|^2\,\Big].$$
The quantity inside the expectation,
$$\hat R(X) := d - 2\,\mathrm{tr}(Dh(X)) + \|h(X)\|^2,$$
is therefore an **unbiased estimator of the risk of $\delta$** — and, crucially, it depends only
on the data $X$, never on the unknown $\theta$. This is Stein's Unbiased Risk Estimator (SURE). It
turns the question "does this data-dependent shrinkage estimator have good risk?" into a calculus
exercise: differentiate $h$, take a trace, and average.

As a check, for the *fixed* linear shrinkage estimator $\delta(X) = (1-c)X$ we have $h(X) = cX$,
$Dh = cI_d$, so
$$\hat R(X) = d - 2cd + c^2\|X\|^2.$$
Averaging, and using $\mathbb{E}_\theta\|X\|^2 = \|\theta\|^2+d$, gives $\mathrm{MSE}(\theta,\delta)
= d(1-c)^2 + c^2\|\theta\|^2$ — exactly the bias-variance formula above with $\zeta=c$, confirming
that the SURE machinery reproduces the one answer we can already check directly.

Now let $c$ vary, and consider the family $\delta(X) = \left(1-\dfrac{c}{\|X\|^2}\right)X$, i.e.
$h(X) = \dfrac{c}{\|X\|^2}X$. Differentiating $h_i(x)=cx_i/\|x\|^2$ gives
$$\mathrm{tr}(Dh(X)) = \frac{c(d-2)}{\|X\|^2}, \qquad \|h(X)\|^2 = \frac{c^2}{\|X\|^2},$$
so
$$\hat R(X) = d + \frac{c^2 - 2c(d-2)}{\|X\|^2}.$$
Averaging, $\mathrm{MSE}(\theta) = d + \big(c^2-2c(d-2)\big)\,\mathbb{E}_\theta[1/\|X\|^2]$, and
since $\mathbb{E}_\theta[1/\|X\|^2]>0$, this is minimized over *fixed* $c$ at
$$c^\ast = d-2,$$
independent of $\theta$. This is a second, independent route to exactly the James-Stein constant
$d-2$ found earlier from the UMVU estimator of $\zeta$ — one route Bayesian, one route pure
frequentist risk minimization within a family, and they agree.

With $c=d-2$, $h(X) = \dfrac{d-2}{\|X\|^2}X$, the exact risk of $\delta_{\mathrm{JS}}$ works out to
$$\hat R(X) = d - \frac{(d-2)^2}{\|X\|^2}, \qquad \mathrm{MSE}(\theta,\delta_{\mathrm{JS}}) = d - (d-2)^2\,\mathbb{E}_\theta\left[\frac{1}{\|X\|^2}\right].$$
At $\theta=0$, $\|X\|^2 \sim \chi^2_d$ and $\mathbb{E}_0[1/\|X\|^2] = 1/(d-2)$, giving the strikingly
simple
$$\mathrm{MSE}(0,\delta_{\mathrm{JS}}) = d - (d-2) = 2,$$
independent of $d$: the risk of estimating a $d$-dimensional zero vector is just $2$, however large
$d$ is, against a risk of $d$ for $X$ itself. For $\theta \ne 0$, $\|X\|^2$ is non-central
$\chi^2_d$ with $\mathbb{E}_\theta\|X\|^2 = \|\theta\|^2+d$, and Jensen's inequality applied to the
strictly convex function $x\mapsto 1/x$ gives $\mathbb{E}_\theta[1/\|X\|^2] > 1/(\|\theta\|^2+d)$,
so
$$\mathrm{MSE}(\theta,\delta_{\mathrm{JS}}) < d - \frac{(d-2)^2}{\|\theta\|^2+d}.$$
So $\delta_{\mathrm{JS}}$ strictly beats $X$ (risk $d$) at every $\theta$, with the largest
advantage at $\theta=0$ (a gap of $d-2$) and a shrinking, but never vanishing, advantage as
$\|\theta\|\to\infty$ — exactly the pattern the frequentist bias-variance calculation predicted,
except that it now holds honestly at every fixed $\theta$, not just in an average sense.

$\delta_{\mathrm{JS}}$ is not the end of the story either — it is itself inadmissible. Whenever
$\|X\|^2 < d-2$, it overshoots and shrinks *past* zero, flipping the sign of each coordinate
relative to $X$, which is clearly wasteful. Truncating the shrinkage factor at zero,
$$\delta_+(X) = \left(1-\frac{d-2}{\|X\|^2}\right)_+X,$$
strictly dominates $\delta_{\mathrm{JS}}$. A version used more often in practice shrinks slightly
more aggressively,
$$\delta_{\mathrm{JS}+}(X) = \left(1-\frac{d-3}{\|X\|^2}\right)_+X,$$
which dominates $X$ for $d \ge 4$.

The paradox is worth sitting with rather than only computing. Taken to its logical extreme it
sounds absurd — should every unrelated quantity being estimated at Berkeley be pooled together
just because there happen to be several of them? The honest answer is that the improvement is
about the *aggregate*, not the coordinate: shrinkage improves the *total* risk
$\mathbb{E}\|\hat\theta-\theta\|^2$ summed over coordinates, but the risk of an individual
coordinate, $\mathbb{E}[(\hat\theta_i-\theta_i)^2]$, can get worse. What James-Stein exploits is
genuinely a property of the sum, and whether that is the quantity you actually care about is a
modeling choice, not a mathematical inevitability.

## Sources

- Berkeley STAT 210A course reader, the chapter covering the Gaussian sequence model, Stein's
  Lemma, SURE, and the James-Stein estimator. The same text was supplied in four copies, used here
  interchangeably as a single source: `fall-2024/reader/empirical-bayes/01–05` (`.qmd` source),
  `fall-2025/reader/empirical-bayes/01–06` and its exact duplicate at
  `fall-2025/units/reader/empirical-bayes/01–06` (`.html` source), and `fall-2026/reader/empirical-bayes/01–05`
  (`.qmd` source). The fall-2024 and fall-2026 copies are word-for-word identical; the two
  fall-2025 copies are word-for-word identical to each other and to fall-2024/2026, except that
  fall-2025 splits the second page into a separate "Stein's Unbiased Risk Estimator" section and
  an "Empirical Bayes" section, where fall-2024/2026 keep them as one page.
- No slides or lecture transcript were supplied for this chapter — the course reader is the sole
  source.
- The reader text itself defers three arguments to separate handwritten notes that were not
  supplied here: the identity $\mathbb{E}[1/Y]=1/(d-2)$ for $Y\sim\chi^2_d$ used to derive
  $\hat\zeta_{\mathrm{UMVU}}$; the fully careful, boundary-term version of the univariate Stein's
  Lemma proof; and the multivariate Stein's Lemma proof (a short conditioning argument is given in
  the reader text and reproduced here in full, in the section above).

---

[← 6. Convergence and the Delta Method (part 1)](06-convergence-and-the-delta-method-part-1.md) · [Contents](index.md) · [8. Statistical Models and Estimation →](08-statistical-models-and-estimation.md)
