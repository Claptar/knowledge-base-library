---
title: "55. Convergence and the Delta Method (part 2)"
course: "Berkeley Stat 210A"
chapter: 55
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 55. Convergence and the Delta Method (part 2)

## What this covers

This chapter answers a question the course has been able to dodge until now: once we leave models
with the friendly exponential-family structure that made exact, finite-sample calculations
possible, how do we say anything about the distribution of an estimator at all? It builds the
machinery behind essentially every "asymptotically normal, use $\hat\theta \pm z_{\alpha/2}\hat\sigma$"
claim in applied statistics — convergence in probability and in distribution, the continuous
mapping theorem, Slutsky's theorem, and the delta method. It assumes the exponential-family and
sufficiency toolkit from earlier in the course (sufficient statistics, natural parameters, the MLE)
and basic facts about random vectors.

## Why we need asymptotics: logistic regression

Consider fixed-design logistic regression: pairs $(x_i, y_i)$, $i = 1, \dots, n$, with $x_i \in
\mathbb{R}^d$ a fixed (non-random) feature vector (one coordinate set to $1$ for the intercept), and

$$
Y_i \overset{\text{ind.}}{\sim} \text{Bern}(\pi_\beta(x_i)), \qquad
\text{logit}(\pi_\beta(x_i)) = \log \frac{\pi_\beta(x_i)}{1 - \pi_\beta(x_i)} = \beta' x_i.
$$

Writing out the likelihood shows this is an exponential family:

$$
p_\beta(y \mid x) = \prod_{i=1}^n \pi_\beta(x_i)^{y_i} (1 - \pi_\beta(x_i))^{1 - y_i}
= \prod_{i=1}^n e^{(\beta' x_i) y_i + \log(1 - \pi_\beta(x_i))}
= e^{\beta' X' y + A(\beta; x)},
$$

where $X$ is the $n \times d$ design matrix with rows $x_i'$. The sufficient statistic is $T(y) =
X'y$ and the natural parameter is $\beta$ itself.

This looks like exactly the setting where the exact, finite-sample machinery built so far should
apply. It doesn't, cleanly:

- To test $H_0: \beta_1 = 0$, the natural idea by analogy with conditioning arguments elsewhere in
  exponential families is to condition on $X_{-1}'Y$, the sufficient statistic for the remaining
  coordinates. But this conditions on (part of) $Y$ itself — there is no clean way to strip out
  $\beta_1$ that leaves a nuisance-free distribution known exactly.
- To estimate $\beta$: a UMVUE generically does not exist for this family. A Bayes estimator needs
  a prior on all of $\beta \in \mathbb{R}^d$ — a genuine modelling choice, not something the
  exponential-family structure hands you for free.

So software packages fall back on general-purpose *asymptotic* methods. The MLE is

$$
\hat\beta_{\text{MLE}}(x, y) = \operatorname*{argmax}_{\beta \in \mathbb{R}^d} \ell(\beta; x, y),
\qquad \ell(\beta; x, y) = \beta' X' y - A(\beta; x) \quad (\text{concave in } \beta),
$$

and the claim used everywhere downstream is that, for large $n$,

$$
\hat\beta_{\text{MLE}} \approx N\big(\beta,\ \mathcal{J}(\beta)^{-1}\big)
$$

— asymptotically unbiased and asymptotically efficient — where $\mathcal{J}(\beta) =
-\mathbb{E}_\beta[\nabla^2 \ell(\beta; x, y)]$ is the Fisher information. The observed information
$-\nabla^2 \ell(\hat\beta; x, y)$ is itself a plug-in estimate of $\mathcal{J}(\beta)$ (this is
exactly a law-of-large-numbers statement, made precise below), giving the estimated covariance

$$
\hat\Sigma = \big(-\nabla^2 \ell(\hat\beta; x, y)\big)^{-1} \approx \Sigma(\beta) = \mathcal{J}(\beta)^{-1}.
$$

From here, a Wald statistic

$$
Z_j = \frac{\hat\beta_j - \beta_j}{\hat\sigma_j} \approx N(0, 1), \qquad \sigma_j^2 = \Sigma_{jj},
$$

gives both a test of $H_0: \beta_j = 0$ (reject when $\hat\beta_j / \hat\sigma_j$ is extreme) and,
by inverting $|Z_j| < z_{\alpha/2}$, the familiar confidence interval $\beta_j \in \hat\beta_j \pm
z_{\alpha/2} \hat\sigma_j$.

Everything up to this point in the course has been finite-sample, exploiting special structure of
the model (an exponential family) to compute things exactly. For "generic" models this exact
computation is intractable or impossible — but the actual problem can often be approximated by a
simpler one that *is* tractable, typically by taking a Gaussian limit as the number of observations
$n \to \infty$. That approximation is only useful if it is good at realistic sample sizes; the rest
of this chapter builds the tools that turn "$\hat\beta \approx N(\beta, \mathcal{J}(\beta)^{-1})$"
into a theorem rather than a hope, and exposes the traps in applying it.

## Two notions of convergence

Let $X_1, X_2, \dots \in \mathbb{R}^d$ be a sequence of random vectors. Two kinds of limiting
behaviour matter here.

**Convergence in probability.** $X_n$ converges in probability to a constant $c \in \mathbb{R}^d$,
written $X_n \overset{P}{\to} c$, if

$$
\mathbb{P}(\|X_n - c\| > \varepsilon) \to 0 \quad \text{for every } \varepsilon > 0.
$$

(The norm could be any distance on any space $\mathcal{X}$; nothing here is special to
$\mathbb{R}^d$.) The idea is that $X_n$ eventually concentrates arbitrarily close to the fixed
point $c$.

**Convergence in distribution.** $X_n$ converges in distribution (equivalently, *weakly*) to a
random variable $X$, written $X_n \Rightarrow X$ or $X_n \overset{d}{\to} X$, if

$$
\mathbb{E} f(X_n) \to \mathbb{E} f(X) \quad \text{for every bounded, continuous } f : \mathcal{X} \to \mathbb{R}.
$$

For real-valued random variables this has a familiar characterization in terms of CDFs: writing
$F_n(x) = \mathbb{P}(X_n \le x)$ and $F(x) = \mathbb{P}(X \le x)$,

$$
X_n \Rightarrow X \iff F_n(x) \to F(x) \text{ for every } x \text{ at which } F \text{ is continuous.}
$$

Restricting to continuity points of $F$ is not a technicality that can be dropped. Take $X_n
\overset{\text{a.s.}}{=} 1/n$ (a point mass at $1/n$) and $X \overset{\text{a.s.}}{=} 0$. Then $X_n
\Rightarrow X$: $F_n(x) = \mathbf{1}\{1/n \le x\} \to \mathbf{1}\{0 \le x\} = F(x)$ for every $x \ne
0$, and $F$ has a jump exactly at $x = 0$, the one point excluded.

### Convergence in probability as a special case

Convergence in probability is convergence in distribution to a point mass — the case where the
fluctuation around the limit disappears entirely, not just its spread. Precisely:

**Proposition.** $X_n \overset{P}{\to} c$ if and only if $X_n \Rightarrow \delta_c$.

**Proof.**

($\Leftarrow$) Let $f_\varepsilon(x) = \min\big(1, \|x - c\|/\varepsilon\big)$, a bounded continuous
function with $f_\varepsilon(x) \ge \mathbf{1}\{\|x - c\| > \varepsilon\}$ for every $x$. Then

$$
\mathbb{P}(\|X_n - c\| > \varepsilon) \le \mathbb{E} f_\varepsilon(X_n) \to \mathbb{E} f_\varepsilon(c) = 0.
$$

($\Rightarrow$) Fix a bounded continuous $f$; note $\mathbb{E} f(\delta_c) = f(c)$. Given
$\varepsilon > 0$, continuity of $f$ at $c$ gives $d(\varepsilon) > 0$ with $\|x - c\| \le
d(\varepsilon) \implies |f(x) - f(c)| \le \varepsilon$. Splitting on whether $X_n$ lands within
$d(\varepsilon)$ of $c$,

$$
\big|\mathbb{E} f(X_n) - f(c)\big| \le \varepsilon + \mathbb{P}(\|X_n - c\| > d(\varepsilon)) \cdot
\sup_x |f(x) - f(c)| \le 2\varepsilon \sup|f|
$$

for $n$ large enough, and $\varepsilon$ was arbitrary. $\blacksquare$

### Consistency

This gives the right language for consistency. In a sequence of statistical models $\mathcal{P}_n
= \{P_{n,\theta} : \theta \in \Theta\}$ with $X_n \sim P_{n,\theta}$, an estimator sequence
$\delta_n(X_n)$ is **consistent** for $g(\theta)$ if

$$
\delta_n(X_n) \overset{P_\theta}{\to} g(\theta), \qquad \text{i.e.} \qquad
\mathbb{P}_\theta\big(\|\delta_n(X_n) - g(\theta)\| > \varepsilon\big) \to 0 \text{ for every } \varepsilon > 0.
$$

The index $n$ on the model and the data is usually dropped once the sequence is understood.

## Two limit theorems

Let $X_1, X_2, \dots$ be iid random vectors and $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$.

**Law of large numbers.** If $\mathbb{E}|X_i| < \infty$ and $\mathbb{E} X_i = \mu$, then
$\bar{X}_n \overset{P}{\to} \mu$ (in fact $\bar{X}_n \overset{\text{a.s.}}{\to} \mu$).

**Central limit theorem.** If $\mathbb{E} X = \mu \in \mathbb{R}^d$ and $\operatorname{Var}(X) =
\Sigma$ is finite, then

$$
\sqrt{n}(\bar{X}_n - \mu) \Rightarrow N(0, \Sigma).
$$

Stronger versions of both exist, but these are generally enough for what follows.

## Moving limits through functions: continuous mapping and Slutsky

The LLN and CLT describe $\bar{X}_n$ itself; most quantities of interest are functions of it, so we
need to know when a limit survives being passed through a function.

**Continuous mapping theorem.** Let $g$ be continuous. If $X_n \Rightarrow X$ then $g(X_n)
\Rightarrow g(X)$. If $X_n \overset{P}{\to} c$ then $g(X_n) \overset{P}{\to} g(c)$.

*Proof.* If $f$ is bounded and continuous, so is $f \circ g$. If $X_n \Rightarrow X$, then
$\mathbb{E} f(g(X_n)) \to \mathbb{E} f(g(X))$ for every such $f$, which is exactly $g(X_n)
\Rightarrow g(X)$. The convergence-in-probability statement is the special case $X \sim \delta_c$,
via the Proposition above. $\blacksquare$

Continuous mapping only handles a single sequence pushed through one function. Combining an
in-distribution limit with an in-probability limit needs a second theorem:

**Slutsky's theorem.** Suppose $X_n \Rightarrow X$ and $Y_n \overset{P}{\to} c$. Then

$$
X_n + Y_n \Rightarrow X + c, \qquad X_n Y_n \Rightarrow cX, \qquad X_n / Y_n \Rightarrow X/c \ \ (c \ne 0).
$$

*Proof idea.* Show that the pair converges jointly, $(X_n, Y_n) \Rightarrow (X, c)$, then apply the
continuous mapping theorem to $(x,y) \mapsto x+y$, $xy$, or $x/y$. $\blacksquare$

The joint convergence step is exactly where Slutsky earns its keep: it is *not* generally true that
$X_n \Rightarrow X$ and $Y_n \Rightarrow Y$ implies $(X_n, Y_n) \Rightarrow (X, Y)$ without saying
something about the joint distribution — two sequences can each converge marginally while their
dependence does anything at all in the limit. Slutsky's theorem is the one special case where the
joint limit is free: because $Y_n$ collapses to a constant, there is no dependence left to specify.

## The delta method

Often the CLT gives $\sqrt{n}(X_n - \mu) \Rightarrow N(0, \sigma^2)$ for some statistic $X_n$, but
the quantity of interest is $f(X_n)$ for a smooth $f$, not $X_n$ itself.

**Theorem (delta method).** If $\sqrt{n}(X_n - \mu) \Rightarrow N(0, \sigma^2)$ and $f$ is
differentiable at $\mu$, then

$$
\sqrt{n}\big(f(X_n) - f(\mu)\big) \Rightarrow N\big(0,\ \dot{f}(\mu)^2 \sigma^2\big).
$$

Informally: $X_n \approx N(\mu, \sigma^2/n) \implies f(X_n) \approx N\big(f(\mu),\ \dot{f}(\mu)^2
\sigma^2/n\big)$.

*Proof.* By differentiability at $\mu$,

$$
f(X_n) = f(\mu) + \dot{f}(\mu)(X_n - \mu) + o(X_n - \mu),
$$

so

$$
\sqrt{n}\big(f(X_n) - f(\mu)\big) = \dot{f}(\mu) \cdot \sqrt{n}(X_n - \mu) +
\underbrace{\sqrt{n} \cdot o(X_n - \mu)}_{\overset{P}{\to} 0}.
$$

The first term converges in distribution to $N(0, \dot{f}(\mu)^2\sigma^2)$ by continuous mapping
(multiplying by the constant $\dot{f}(\mu)$); the second term vanishes in probability because
$X_n - \mu \overset{P}{\to} 0$ shrinks faster than $1/\sqrt{n}$. Slutsky's theorem then gives the
limit of the sum. $\blacksquare$

Nothing here requires the normalizing rate to be $\sqrt{n}$ — the only ingredient the proof
actually uses is $X_n - \mu \overset{P}{\to} 0$; whatever rate makes $X_n - \mu$ vanish carries
through in exactly the same way.

**Multivariate version.** If $\sqrt{n}(X_n - \mu) \Rightarrow N_d(0, \Sigma)$ and $f : \mathbb{R}^d
\to \mathbb{R}^k$ has Jacobian

$$
Df(x) = \begin{pmatrix} -\nabla f_1(x)- \\ \vdots \\ -\nabla f_k(x)- \end{pmatrix}
$$

existing at $\mu$, then

$$
\sqrt{n}\big(f(X_n) - f(\mu)\big) \approx \sqrt{n}\, Df(\mu)(X_n - \mu) \approx
N\big(0,\ Df(\mu)\, \Sigma\, Df(\mu)'\big),
$$

which for $k = 1$ reads $N\big(0,\ \nabla f(\mu)' \Sigma \nabla f(\mu)\big)$.

## Where the delta method needs care

Take $X_1, \dots, X_n \overset{\text{iid}}{\sim} (\mu, \sigma^2)$ and, independently, $Y_1, \dots,
Y_n \overset{\text{iid}}{\sim} (\nu, \tau^2)$. What is the large-$n$ distribution of $(\bar{X} +
\bar{Y})^2$?

**Point convergence isn't enough.** Since $\bar{X} \overset{P}{\to} \mu$ and $\bar{Y}
\overset{P}{\to} \nu$, continuous mapping gives $(\bar{X} + \bar{Y})^2 \overset{P}{\to} (\mu +
\nu)^2$ — correct, but it only names the limit, not a scale on which to see fluctuations around it.

**Delta method.** With $f(x,y) = (x+y)^2$, so $\partial f/\partial x = \partial f/\partial y =
2(x+y)$, and $\sqrt{n}(\bar{X} - \mu, \bar{Y} - \nu) \Rightarrow N(0, \operatorname{diag}(\sigma^2,
\tau^2))$, the multivariate delta method gives

$$
f(\bar{X}, \bar{Y}) \approx N\Big(f(\mu,\nu),\ \nabla f' \begin{pmatrix} \sigma^2 & 0 \\ 0 & \tau^2
\end{pmatrix} \nabla f \,/\, n\Big) = N\Big((\mu+\nu)^2,\ \frac{4(\mu+\nu)^2(\sigma^2+\tau^2)}{n}\Big),
$$

or, on the $\sqrt{n}$ scale,

$$
\sqrt{n}\big((\bar{X}+\bar{Y})^2 - (\mu+\nu)^2\big) \Rightarrow N\big(0,\ 4(\mu+\nu)^2(\sigma^2+\tau^2)\big).
$$

**The degenerate case.** What if $\mu + \nu = 0$? The previous display still technically holds — it
just says $\sqrt{n}(\bar{X}+\bar{Y})^2 \overset{P}{\to} 0$, a statement with no useful content,
since the variance $4(\mu+\nu)^2(\sigma^2+\tau^2)$ collapses to $0$. But $(\bar{X}+\bar{Y})^2$ does
have a nondegenerate limit at the right rate; the delta method's linear approximation was simply
the wrong tool to find it, because its gradient vanishes exactly where $\mu + \nu = 0$.

Here is the correct route, and it uses continuous mapping, *not* Slutsky. By the CLT and continuous
mapping (adding the two coordinates of a jointly convergent Gaussian vector),

$$
\sqrt{n}\bar{X} + \sqrt{n}\bar{Y} \Rightarrow N(0, \sigma^2 + \tau^2),
$$

and squaring — again continuous mapping, applied to the limit of the joint sum — gives

$$
n(\bar{X}+\bar{Y})^2 \Rightarrow (\sigma^2+\tau^2)\chi_1^2.
$$

Slutsky does not apply to this step: Slutsky needs one of the two pieces to collapse to a constant,
and here neither $\sqrt{n}\bar{X}$ nor $\sqrt{n}\bar{Y}$ does — both stay genuinely random in the
limit. The tool doing the work is continuous mapping applied to the jointly convergent pair, not
Slutsky's theorem.

## Higher-order delta method

The general pattern behind the degenerate case: expand further,

$$
f(X_n) \approx \underbrace{f(\mu)}_{O(1)} + \underbrace{\dot{f}(\mu)(X_n-\mu)}_{O_p(n^{-1/2})} +
\underbrace{\frac{\ddot{f}(\mu)}{2}(X_n-\mu)^2}_{O_p(n^{-1})} + \cdots
$$

When $\dot{f}(\mu) = 0$, the first-order term that normally dominates vanishes, and the
*second*-order term sets the scale instead — which is why the correct normalization becomes $n$
rather than $\sqrt{n}$:

$$
n\big(f(X_n) - f(\mu)\big) \approx \frac{\ddot{f}(\mu)}{2}\big(\sqrt{n}(X_n-\mu)\big)^2 \approx
\frac{\ddot{f}(\mu)\sigma^2}{2} \chi_1^2.
$$

This is exactly what happened above with $f(x,y) = (x+y)^2$ at $\mu + \nu = 0$: the first
derivative $2(\mu+\nu)$ vanished, so the limit came from the quadratic term instead, and the
$\chi_1^2$ shape — rather than Gaussian — is the signature of that.

## Sources

- Berkeley STAT210A, Fall 2024, handwritten lecture notes for "Lecture 19: Asymptotics",
  reconstructed to markdown by a model from a PDF with no text layer (equations unverified against
  the original scan; licensed CC BY 4.0):
  - `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture19-asymptotics/01-example.md`
    — the logistic-regression motivating example, the MLE, and the Wald test/interval.
  - `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture19-asymptotics/02-convergence.md`
    — convergence in probability and in distribution, the point-mass proposition and its proof,
    consistency, the LLN and CLT, continuous mapping, Slutsky's theorem, and the delta method
    statement and proof.
  - `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture19-asymptotics/03-delta-method.md`
    — the $(\bar{X}+\bar{Y})^2$ worked example and the higher-order delta method.
- The Fall 2025 and Fall 2026 handwritten notes filed under the same lecture number
  (`fall-2025/handwritten/lecture19-asymptotics.md`, `fall-2026/handwritten/lecture19-asymptotics.md`)
  are OCR-truncated duplicates of the same outline and opening example — both files cut off
  mid-equation partway through the logistic-regression setup. Fall 2024 is the complete version of
  the lecture and is what this chapter follows throughout.
- No slides, transcript, or problem set were supplied for this lecture; nothing beyond the three
  Fall 2024 notes files above was used.

---

[← 54. One-Sample T-Test and the Linear Model](54-one-sample-t-test-and-the-linear-model.md) · [Contents](index.md) · [56. Convergence and the Delta Method (part 3) →](56-convergence-and-the-delta-method-part-3.md)
