---
title: "57. MLE in Exponential Families"
course: "Berkeley Stat 210A Fall 2024"
chapter: 57
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 57. MLE in Exponential Families

## What this covers

This chapter works out maximum likelihood estimation completely in the one setting where it can be
solved in closed form: the exponential family. It shows how the likelihood equations reduce to
matching a sufficient statistic to its expectation, derives the asymptotic normal distribution of
the MLE from the law of large numbers, the CLT and the delta method, and uses a Poisson example to
warn that "asymptotically optimal" says nothing about finite-sample behavior — the same estimator
can have infinite mean and variance at every finite $n$. It closes by opening the general
(not-necessarily-exponential-family) theory of asymptotic efficiency, a section the lecture does
not finish. It assumes exponential family canonical form (natural parameter, sufficient statistic,
log-partition function), the delta method, weak convergence, and Slutsky's theorem.

## The maximum likelihood estimator

For a dominated family $\mathcal P = \{P_\theta : \theta\in\Theta\}$ with densities $p_\theta$
(with respect to a common dominating measure), the maximum likelihood estimator is the value of
$\theta$ that makes the observed data most probable:
$$
\hat\theta_{\mathrm{MLE}}(X) = \operatorname*{argmax}_{\theta\in\Theta} p_\theta(X) = \operatorname*{argmax}_{\theta\in\Theta} \ell(\theta;X),
$$
where $\ell(\theta;X) = \log p_\theta(X)$ is the log-likelihood.

Two remarks worth keeping in mind before using it:

1. The argmax need not exist, need not be unique, and — even when it exists and is unique — need
   not be computable in closed form.
2. It does not depend on how the model is parametrized or on which dominating measure was chosen,
   and it is *equivariant* under reparametrization: the MLE of $g(\theta)$ is
   $g(\hat\theta_{\mathrm{MLE}})$.

## Solving the likelihood equations in a full exponential family

Take $p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x)$, a full exponential family in canonical (natural
parameter) form. The log-likelihood and score are
$$
\ell(\eta;x) = \eta'T(x) - A(\eta) + \log h(x), \qquad \nabla\ell(\eta;x) = T(x) - \mathbb E_\eta T(X),
$$
using the standard exponential-family fact $\nabla A(\eta) = \mathbb E_\eta T(X)$. Setting the score
to zero, the MLE — if it exists — solves the moment equation
$$
T(x) = \mathbb E_{\hat\eta}T(X).
$$

This equation has at most one solution. The Hessian of the log-likelihood is
$$
\ddot\ell(\eta;x) = -\operatorname{Var}_\eta(T(X)),
$$
a negative semi-definite matrix, so $\ell$ is concave in $\eta$. It fails to be *strictly* concave
only along a direction $v$ for which $v'T(X)$ is almost surely constant — but that means the
parametrization is redundant (not minimal): some linear combination of the coordinates of $T$
carries no information. Ruling that out, $\ell$ is strictly concave and has at most one stationary
point.

Write $\mu(\eta) := \nabla A(\eta) = \mathbb E_\eta T(X)$ for the map from the natural parameter to
the mean of the sufficient statistic. When it is invertible, the MLE is
$$
\hat\eta = \mu^{-1}(T(x)).
$$

## Asymptotic normality of the MLE in a one-parameter exponential family

Now let $X_1,\dots,X_n \stackrel{\mathrm{iid}}\sim e^{\eta T(x) - A(\eta)}h(x)$ with scalar natural
parameter $\eta\in\Xi\subseteq\mathbb R$. The log-likelihood of the sample is itself of exponential
family form with sufficient statistic $\sum_i T(X_i)$, so by the same argument
$$
\hat\eta = \psi^{-1}(\bar T), \qquad \bar T = \frac1n\sum_{i=1}^n T(X_i), \qquad \psi(\eta) := \mu(\eta) = \dot A(\eta).
$$

Assume $\eta$ lies in the interior $\Xi^\circ$. There, $\dot\psi(\eta) = \ddot A(\eta) > 0$ (the
score has strictly negative second derivative, i.e. the Fisher information is positive), so $\psi$
is strictly increasing, $\psi^{-1}$ is continuous, and by the inverse function theorem
$$
(\psi^{-1})'(\mu) = \frac{1}{\dot\psi(\psi^{-1}(\mu))} = \frac{1}{\ddot A(\eta)}.
$$

Two limit theorems for $\bar T$ now carry over to $\hat\eta$:

- **Consistency.** By the law of large numbers, $\bar T \xrightarrow{P_\eta} \mu(\eta)$. Since
  $\psi^{-1}$ is continuous, the continuous mapping theorem gives
  $\hat\eta = \psi^{-1}(\bar T) \xrightarrow{P_\eta} \psi^{-1}(\mu(\eta)) = \eta$.
- **Asymptotic normality.** By the CLT, $\sqrt n(\bar T - \mu(\eta)) \Rightarrow \mathcal N(0,
  \operatorname{Var}_\eta(T(X_1))) = \mathcal N(0, \ddot A(\eta))$.

Applying the delta method to $\hat\eta = \psi^{-1}(\bar T)$,
$$
\sqrt n(\hat\eta - \eta) \Rightarrow \mathcal N\!\left(0, \Big(\frac{1}{\ddot A(\eta)}\Big)^2 \ddot A(\eta)\right) = \mathcal N\!\left(0, \frac{1}{\ddot A(\eta)}\right).
$$

Recall that for a single observation from this family, $J_1(\eta) = \operatorname{Var}_\eta(T(X_i))
= \ddot A(\eta)$ is exactly the Fisher information carried by one observation. So the asymptotic
distribution of the MLE is
$$
\hat\eta \;\approx\; \mathcal N\!\left(\eta, \frac{1}{nJ_1(\eta)}\right):
$$
asymptotically unbiased, asymptotically Gaussian, and asymptotically attaining the Cramér–Rao lower
bound — equivalently, the correlation between $\bar T$ and $\hat\eta$ tends to $1$.

## A cautionary example: the Poisson MLE has infinite moments

The asymptotic statement above is exactly that — asymptotic. Take $X_1,\dots,X_n
\stackrel{\mathrm{iid}}\sim \operatorname{Pois}(\theta)$ and reparametrize by $\eta=\log\theta$. The
MLE is $\hat\eta=\log\bar X$, and $\sqrt n(\bar X - \theta)\Rightarrow \mathcal N(0,\theta)$, so the
delta method gives
$$
\sqrt n(\hat\eta-\eta) = \sqrt n(\log\bar X - \log\theta) \Rightarrow \mathcal N\!\left(0, \theta\cdot\frac1{\theta^2}\right) = \mathcal N(0,\theta^{-1}).
$$

But at every finite $n$ and every $\theta>0$,
$$
\mathbb P_\theta(\hat\eta=-\infty) = \mathbb P_\theta(X_1=0)^n = e^{-\theta n} > 0,
$$
because $\log 0 = -\infty$. Consequently $\mathbb E\hat\eta=-\infty$ and
$\operatorname{Var}(\hat\eta)=\infty$ for every finite $n$: an estimator that is asymptotically
optimal can have embarrassing finite-sample moments.

## Why the pathology doesn't spoil the asymptotic claim

That the mean and variance of $\hat\eta$ are infinite for every $n$ looks like it should contradict
convergence to a normal limit, but it does not, because weak convergence only constrains the bulk of
the distribution, not an event of vanishing probability. The general statement:

**Proposition.** If $\mathbb P(B_n)\to 0$, $X_n\Rightarrow X$, and $Z_n$ is an arbitrary sequence of
random variables, then
$$
X_n\mathbf 1_{B_n^c} + Z_n\mathbf 1_{B_n} \;\Rightarrow\; X.
$$

*Proof.* For any $\varepsilon>0$, $\mathbb P(\|Z_n\mathbf 1_{B_n}\|>\varepsilon) \le \mathbb
P(B_n)\to 0$, so $Z_n\mathbf 1_{B_n}\xrightarrow{P}0$. Also $\mathbf 1_{B_n^c}\xrightarrow{P}1$.
Slutsky's theorem then gives the claim. $\blacksquare$

Here $B_n = \{X_1=\dots=X_n=0\}$ has $\mathbb P_\theta(B_n)=e^{-\theta n}\to0$, and on $B_n$ the
estimator does whatever it does ($-\infty$, in this case) — arbitrarily badly, with no effect on the
limiting distribution. Moments, unlike convergence in distribution, are sensitive to exactly this
kind of vanishing-probability event, which is why $\mathbb E\hat\eta$ and $\operatorname{Var}\hat\eta$
can blow up while $\hat\eta$ still converges in distribution to a normal law.

## Toward a general theory: Fisher information for iid samples

The good behavior found above is not special to exponential families. The lecture begins setting up
the general case: $X_1,\dots,X_n\stackrel{\mathrm{iid}}\sim p_\theta$, $\theta\in\Theta\subseteq
\mathbb R^d$, with $p_\theta$ smooth in $\theta$ (e.g. twice continuously differentiable with
integrable derivatives — a condition that can be relaxed). Writing
$$
\ell_1(\theta;X_i) = \log p_\theta(X_i), \qquad \ell_n(\theta;X) = \sum_{i=1}^n \ell_1(\theta;X_i),
$$
the Fisher information from one observation and from the whole sample are
$$
J_1(\theta) = \operatorname{Var}_\theta(\nabla\ell_1(\theta;X_i)) = -\mathbb E\big[\nabla^2\ell_1(\theta;X_i)\big], \qquad J_n(\theta) = \operatorname{Var}_\theta(\nabla\ell_n(\theta;X)) = nJ_1(\theta),
$$
the second equality using independence across the $X_i$. The lecture note breaks off mid-definition
at this point — "we say an estimator $\hat\theta_n$ is **" — so the definition of asymptotic
efficiency this machinery was building toward is not recorded here.

## Sources

- All material: handwritten lecture notes, `lecture21-F24.md` (Berkeley STAT 210A, Fall 2024
  handwritten notes), covering the lecture's own outline — "Maximum Likelihood Estimator",
  "Asymptotic Distribution of MLE", "Consistency of MLE". The source is a model's reconstruction of
  a scanned handwritten PDF with no text layer (`fidelity: reconstructed`); every equation above
  should be read as a transcription of that reconstruction, not independently verified.
- The note itself ends mid-sentence, inside the definition of an asymptotically efficient estimator
  for the general (non-exponential-family) setting. That definition, and the general consistency and
  asymptotic-normality theorems the lecture's outline promises, are not contained in this lecture's
  material and so are not reconstructed here.

---

[← 56. Convergence and the Delta Method (part 3)](56-convergence-and-the-delta-method-part-3.md) · [Contents](index.md) · [58. MLE: Consistency and Efficiency →](58-mle-consistency-and-efficiency.md)
