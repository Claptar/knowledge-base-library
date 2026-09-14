---
title: Score fisher Part 07 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Score fisher Part 07 —

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

**Example: Exponential family**

It is also illuminating to calculated these quantities for exponential families. Assume we have
$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x).
$$

Then the log-likelihood is $\ell(\eta;X) = \eta'T(X) - A(\eta) + \log h(X)$, and the score is
$$
\nabla \ell(\eta;X) = T(X) - \nabla A(\eta).
$$
Recalling that $\nabla A(\eta) = \EE_\eta T(X)$, we obtain
$$
S_\eta(X) = T(X) - \EE_\eta T(X).
$$
So we indeed see that, up to a constant shift (which is needed for its mean to be zero), the score in an exponential family (at least in the natural parameterization) is none other than the sufficient statistic $T(X)$.

Since $\EE_\eta T(X)$ is nonrandom, the variance is
$$
J(\eta) = \Var_\eta (T(X)) = \nabla^2 A(\eta).
$$

We could alternatively derive the Fisher information by taking a second derivative of the log-likelihood with respect to $\eta$, giving
$$
\nabla^2\ell(\eta;X) = -\nabla^2 A(\eta),
$$
which is deterministically equal to $-\Var_\eta(T(X))$, so we have confirmed the identity $J(\eta) = -\EE_\eta[\nabla^2 \ell(\eta;X)]$.

**Example: Curved exponential family**

Next, consider a curved version of the previous family, parameterized by $\theta \in \RR$:
$$
p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))}h(x),
$$
So, $\eta(\theta)$ is tracing out a one-dimensional curve through the ambient $s$-dimensional parameter space.

Now, the log-likelihood is
$$\ell(\theta;X) = \eta(\theta)'T(x) - A(\eta(\theta))  + \log h(x),$$
and we can obtain its first derivative by applying the chain rule:
$$
\dot{\ell}(\theta;X) = \dot{\eta}(\theta)'(T(X) - \nabla_\eta A(\eta(\theta))),
$$
leading to
$$
S_\theta(X) = \dot{\eta}(\theta)'(T(X) - \EE_\theta T(X)) = \dot{\eta}(\theta)'S_{\eta(\theta)}(X),
$$
where (slightly abusing notation) $S_{\eta}(X)$ is the score in the ambient exponential family. Note here $\dot\eta(\theta)$ is an $s$-vector. Its direction tells us which projection of $T(X)$ is informative for distinguishing parameter values in a local neighborhood of $\theta$, and its magnitude tells us how rapidly we are traversing the parameter space.

Likewise the Fisher information is
$$
J(\theta) = \dot{\eta}(\theta)'J(\eta(\theta))\dot{\eta}(\theta).
$$
It is noteworthy that choosing a "faster" parameterization of the same subfamily will make the Fisher information larger. This is not because the data become any more or less informative about a statistical model when we change the parameterization. Again, we can think of it more as a "unit conversion" issue: the farther $P_{\eta(\theta)}$ is from (say) $P_{\eta(\theta\pm 0.1)}$, the better chance we have of estimating $\theta$ up to a precision of $0.1$.

**Example: Curved Gaussian location family**

As a concrete example of the above, suppose $X_1,\ldots,X_n \simiid N_d(\mu(\theta), I_d)$, for $\theta \in \RR$ and $\mu(\theta) \in \RR^d$: that is, $\mu(\theta)$ is tracing out a curve in the parameter space of the ambient $d$-dimensional Gaussian location model.

In the ambient family, the score is
$$
S_\mu^{(\mu)}(X) = \sum_i X_i - n\mu = n(\overline{X}-\mu),
$$
and the Fisher information is $J^{(\mu)}(\mu) = nI_d$. Thus, in the curved subfamily, we have
$$
S_{\theta}(X) = n\dot\mu(\theta)'(\overline{X}-\mu(\theta)),
$$
and $J(\theta) = n\|\dot\mu(\theta)\|^2$, i.e. the sample size times the parameterization speed. The

---

[← Score fisher Part 06 —](06-score-fisher-part-06.md) · [Up: contents](index.md)
