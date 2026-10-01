---
title: "29. Canonical Form"
course: "Berkeley Stat 210A"
chapter: 29
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 29. Canonical Form

## What this covers

This chapter introduces exponential families of distributions and puts them in **canonical
form**: a density written as $e^{\eta'T(x)-A(\eta)}h(x)$. It then shows why this form is useful —
differentiating the normalizing constant $A$ with respect to the natural parameter $\eta$ hands
you the mean and variance (more generally, all cumulants) of the sufficient statistic $T(X)$ for
free, without ever computing an integral by hand. It assumes familiarity with densities relative
to a dominating measure $\mu$, and with moment-generating functions.

## Exponential families and canonical form

An **$s$-parameter exponential family** is a family of distributions $\mathcal{P} = \{P_\eta :
\eta \in \Xi\}$ on a sample space $\mathcal{X}$ (not necessarily a subset of $\mathbb{R}^n$) whose
densities with respect to a common dominating measure $\mu$ take the form

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x),$$

where

| symbol | role |
| :--- | :--- |
| $T : \mathcal{X} \to \mathbb{R}^s$ | the **sufficient statistic** |
| $h : \mathcal{X} \to \mathbb{R}$ | the **carrier**, or base density |
| $\eta \in \Xi \subseteq \mathbb{R}^s$ | the **natural parameter** |
| $A : \mathbb{R}^s \to \mathbb{R}$ | the **log-partition function** (normalizing constant) |

The function $A$ is not a free choice: once $h$ and $T$ are fixed, $A$ is forced by the requirement
that $p_\eta$ integrate to $1$ for every $\eta$,
$$\int_\mathcal{X} p_\eta \, d\mu = 1 \quad \forall \eta
\;\;\Longrightarrow\;\; A(\eta) = \log\left[\int_\mathcal{X} e^{\eta' T(x)} h(x)\, d\mu(x)\right] \le \infty.$$

The structure is clearest when three reductions are made, each without loss of generality:

- $T(x) = x$ — this is the **sufficiency reduction**: replace $x$ by its sufficient statistic;
- $h(x) \equiv 1$ — absorb $h$ into the dominating measure $\mu$;
- $\theta = \eta$ — parameterize directly by the natural parameter.

With all three in force, the family is in **canonical form**:
$$p_\eta(x) = e^{\eta' x - A(\eta)}.$$

The density is **log-linear** in $\eta$, and that is deliberately stronger than asking it to be
linear: statistical calculations multiply and divide densities far more often than they add or
subtract them. Multiplying or dividing densities is what you do to

- combine evidence from independent observations,
- form $\text{prior} \times \text{likelihood}$ in a Bayesian calculation,
- compute a conditional probability (divide a joint by a marginal),
- form a likelihood ratio,
- compute a relative density (Radon–Nikodym derivative).

Addition of densities, by contrast, is what produces a *mixture* — a genuinely different
operation. A log-linear form turns all of the multiplicative operations above into addition and
subtraction of the exponent $\eta' T(x)$, which is why canonical form is the convenient one to
compute in.

## The natural parameter space

The **natural parameter space** is the set of all $\eta$ for which $p_\eta$ is normalizable:
$$\Xi_1 = \{\eta : A(\eta) < \infty\}.$$

$\Xi_1$ is determined entirely by $T$, $h$, and $\mu$ — it is not a modeling choice. The family
$\Xi$ actually used can be any subset of $\Xi_1$, $\Xi \subseteq \Xi_1$, but it can never be
larger.

$A(\eta)$ is always a convex function of $\eta$, and consequently $\Xi_1$, its effective domain, is
always a convex set.

## Worked example: the Poisson family

Take $X \sim \mathrm{Poisson}(\lambda)$, so $p_\lambda(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}$ for
$x = 0, 1, 2, \dots$. Rewriting the exponent,
$$p_\lambda(x) = \exp\{(\log \lambda)\, x - \lambda\}\, \frac{1}{x!},$$
which is already in the form $e^{\eta T(x) - A(\eta)} h(x)$ with
$$\eta(\lambda) = \log \lambda, \qquad T(x) = x, \qquad A(\eta) = \lambda = e^{\eta}, \qquad h(x) =
\frac{1}{x!}.$$

This example is carried through the rest of the chapter.

## Differentiating under the integral sign

Write the defining identity for $A$ as
$$e^{A(\eta)} = \int e^{\eta' T(x)} h(x)\, d\mu(x). \tag{$*$}$$

Differentiating both sides of $(*)$ with respect to $\eta$, and pulling the derivative inside the
integral, produces a stream of identities relating derivatives of $A$ to moments of $T(X)$. Pulling
the derivative through the integral sign is *not* automatic — it requires a regularity condition.

**Regularity condition (Keener, Thm 2.4).** For $f : \mathcal{X} \to \mathbb{R}$, let
$$\Xi_f = \left\{\eta \in \mathbb{R}^s : \int |f|\, e^{\eta' T} h\, d\mu < \infty\right\}.$$
Then $g(\eta) = \int f\, e^{\eta'T} h\, d\mu$ has continuous partial derivatives of every order for
$\eta$ in the interior of $\Xi_f$, and they may be computed by differentiating under the integral
sign. In particular, on the interior of $\Xi_1$, $A(\eta)$ has partial derivatives of all orders.

**First derivative.** Differentiating $(*)$ once with respect to $\eta_j$,
$$\frac{\partial}{\partial \eta_j} e^{A(\eta)} = \frac{\partial}{\partial \eta_j} \int e^{\eta'
T(x)} h(x)\, d\mu(x)$$
$$e^{A(\eta)} \frac{\partial A}{\partial \eta_j}(\eta) = \int T_j(x)\, e^{\eta' T(x) - A(\eta)}
h(x)\, d\mu(x),$$
and the right-hand side, after cancelling $e^{A(\eta)}$, is exactly $\mathbb{E}_\eta[T_j(X)]$.
Hence
$$\nabla A(\eta) = \mathbb{E}_\eta[T(X)].$$

**Second derivative.** Differentiating $(*)$ twice with respect to $\eta_j, \eta_k$, and using the
product rule on the left (since differentiating $e^{A(\eta)}$ twice brings down both a second
derivative of $A$ and the product of the two first derivatives),
$$e^{A(\eta)}\left(\frac{\partial^2 A}{\partial \eta_j \partial \eta_k} +
\underbrace{\frac{\partial A}{\partial \eta_j}}_{\mathbb{E}[T_j]}
\underbrace{\frac{\partial A}{\partial \eta_k}}_{\mathbb{E}[T_k]}\right) = \int T_j T_k\, e^{\eta'
T - A(\eta)} h\, d\mu = \mathbb{E}[T_j T_k],$$
so that
$$\frac{\partial^2 A}{\partial \eta_j \partial \eta_k}(\eta) = \mathbb{E}[T_jT_k] -
\mathbb{E}[T_j]\mathbb{E}[T_k] = \mathrm{Cov}_\eta(T_j, T_k),$$
$$\nabla^2 A(\eta) = \mathrm{Var}_\eta(T(X)) \in \mathbb{R}^{s \times s}.$$

The gradient of the log-partition function is the mean of the sufficient statistic, and its
Hessian is the covariance matrix of the sufficient statistic — both read off without doing an
integral.

**Poisson, continued.** With $T(X) = X$ and $A(\eta) = e^\eta\, (= \lambda)$,
$$\mathbb{E}_\eta[X] = \frac{d}{d\eta} e^\eta = e^\eta = \lambda, \qquad
\mathrm{Var}_\eta(X) = \frac{d^2}{d\eta^2} e^\eta = e^\eta = \lambda,$$
recovering the familiar fact that a Poisson's mean and variance coincide. The identities are
differential in $\eta$, the *natural* parameter — differentiating $A$ with respect to $\lambda$
directly gives the wrong answer, because the identities $\nabla A = \mathbb{E}[T]$ and $\nabla^2 A
= \mathrm{Var}(T)$ were derived by differentiating the defining identity $(*)$ with respect to
$\eta$, not with respect to whatever parameter the family happens to be dressed up in.

## Moment- and cumulant-generating functions

The same differentiation trick, carried to all orders, says that the $k$-th order moments of
$T(X)$ can be obtained by differentiating $(*)$ $k$ times and then dividing by $e^{A(\eta)}$. This
is exactly what a moment-generating function packages. Concretely,
$$M_\eta^{T(X)}(u) = \mathbb{E}_\eta\left[e^{u'T(X)}\right] = \int e^{u'T}\, e^{\eta'T -
A(\eta)}\, h\, d\mu = e^{A(\eta+u) - A(\eta)} \underbrace{\int e^{(\eta+u)'T - A(\eta+u)} h\,
d\mu}_{=1},$$
so
$$M_\eta^{T(X)}(u) = e^{A(\eta+u) - A(\eta)}.$$

This is useful both for reading off moments of $T(X)$ directly and for finding the distribution of
a sum of independent random variables (via the multiplicativity of moment-generating functions
under convolution).

The **cumulant-generating function** is its log,
$$K_\eta^T(u) = \log M_\eta^T(u) = A(\eta + u) - A(\eta),$$
which is why $A$ itself is sometimes called the cumulant function — it *is* the cumulant-generating
function of $T(X)$ evaluated at a shift of the natural parameter, up to the additive constant
$A(\eta)$.

## Other parameterizations

It is often more convenient to index the same family by a parameter $\theta$ that is not the
natural parameter itself, writing
$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x), \qquad B(\theta) = A(\eta(\theta)).$$

Many familiar families are exponential families only after some algebraic massaging to expose this
form; the lecture begins working through the normal family, $X \sim N(\mu, \sigma^2)$ with $\theta
= (\mu, \sigma^2)$, as such an example, but the source material breaks off at the start of that
derivation (see Sources).

## Sources

Both sections of this chapter are drawn from the handwritten lecture notes for *lecture04:
exponential families*, Berkeley STAT210A, Fall 2024 — no slide deck or transcript was supplied for
this lecture:

- Exponential families, canonical form, the natural parameter space, and the Poisson example: from
  `01-canonical-form.md` (sections "Exponential Families" through the Poisson worked example).
- The differentiation identities, the Keener regularity theorem, the mean/variance-from-$A$
  derivation, the moment- and cumulant-generating function identities, and the start of the
  "Other Parameterizations" discussion: from `02-differential-identities.md`.

Two things the lecture pointed at but did not fully contain, kept out of this chapter accordingly:

- **Keener, Thm 2.4** is cited by name for the differentiation-under-the-integral regularity
  condition; the notes state the theorem but the underlying textbook proof is not part of this
  material.
- The exercise proving that $A(\eta)$'s convexity forces $\Xi_1$ to be convex is referenced in the
  notes as "HW 1 Prob. 2" — an assigned homework problem, not contained in the supplied material,
  so it is reported here only as a pointer, not reproduced.
- The worked example casting the normal family $N(\mu,\sigma^2)$ into canonical/other-parameter
  form is cut off mid-derivation in `02-differential-identities.md` (the source PDF page appears to
  end there); only the setup ($\theta = (\mu,\sigma^2)$) survives, and the chapter reports no more
  than that rather than completing the derivation.

Both source files are machine reconstructions of a handwritten PDF with no text layer (`fidelity:
reconstructed`, `route: llm`), licensed CC BY 4.0; the conversion notes flag that every equation in
them is unverified against the original scan.

---

[← 28. Statistical models and decisions](28-statistical-models-and-decisions.md) · [Contents](index.md) · [30. Sufficient Statistics and Factorization →](30-sufficient-statistics-and-factorization.md)
