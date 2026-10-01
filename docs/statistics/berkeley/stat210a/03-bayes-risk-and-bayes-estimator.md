---
title: "3. Bayes Risk and Bayes Estimator"
course: "Berkeley Stat 210A"
chapter: 3
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Bayes Risk and Bayes Estimator

## What this covers

This chapter answers a question left open once risk functions and admissibility have been
introduced: many estimators are admissible and their risk functions cross, so how do you actually
choose one? The route taken here is to average the risk over a distribution on the parameter
space — the *Bayes risk* — and characterize the minimizer of that average, the *Bayes estimator*,
through the posterior distribution. It assumes the risk function $R(\theta,\delta) =
\mathbb{E}_\theta[L(\theta,\delta(X))]$ and the admissibility discussion that motivates averaging
it, standard manipulation of conditional expectations and densities, and the named exponential
families (Binomial, Beta, Poisson, Gamma, Normal).

## From risk functions to Bayes risk

Risk functions of different admissible estimators cross, so no single estimator dominates on
every $\theta$. One way to force a single number out of a risk function is to average it against
a measure $\pi$ on the parameter space $\Theta$, called the *prior*. This gives the **Bayes risk**
of an estimator $\delta$ with respect to $\pi$:

$$
r(\pi,\delta) = \int_\Theta R(\theta,\delta)\,d\pi(\theta).
$$

If $\pi(\Theta)=\infty$, the prior is *improper*; otherwise it is normalized so $\pi(\Theta)=1$ and
called *proper*. A proper prior is a probability measure, and the Bayes risk is then literally an
expectation over $\theta \sim \pi$:

$$
r(\pi,\delta) = \mathbb{E}_\pi[R(\theta,\delta)] = \mathbb{E}_\pi\big[\mathbb{E}_\theta[L(\theta,\delta(X))]\big] = \mathbb{E}[L(\theta,\delta(X))],
$$

where the last expectation is over the *joint* law of $(\theta,X)$ with $\theta\sim\pi$ and
$X\mid\theta \sim P_\theta$. An estimator $\delta_\pi$ minimizing $r(\pi,\delta)$ over all $\delta$
is called a **Bayes estimator**; it depends on both the prior $\pi$ and the loss $L$.

The names "prior" and "posterior" suggest an epistemic story — belief about $\theta$ before seeing
data, updated afterward. Nothing in the mathematics forces that reading. Even a committed
frequentist, or someone using a $\pi$ that corresponds to nobody's actual beliefs, can use this
machinery: $\pi$ is just a weighting that reduces a risk function to a scalar, and $r(\pi,\delta)$
is mathematically identical to the average-case risk whether or not $\pi$ is believed.

## Prior, likelihood, posterior

Write the prior as a density $\pi(\theta)$ and the likelihood as $p(x\mid\theta)$. Then

- joint density: $p(\theta,x) = \pi(\theta)\,p(x\mid\theta)$,
- marginal density of the data: $q(x) = \int_\Theta p(\theta,x)\,d\theta$,
- posterior density: $\pi(\theta\mid x) = \dfrac{p(\theta,x)}{q(x)}$ — Bayes' rule.

The reason to bother naming the posterior is that the Bayes estimator can then be found one $x$
at a time, using only $\pi(\theta\mid x)$:

$$
\delta_\pi(x) = \arg\min_d\, \mathbb{E}[L(\theta,d)\mid X=x] = \arg\min_d \int_\Theta L(\theta,d)\,\pi(\theta\mid x)\,d\theta.
$$

## Characterizing the Bayes estimator

That display is a definition of a candidate, not yet a theorem: it says how to build an estimator
by minimizing the *conditional* risk pointwise, but it doesn't yet say that doing so also
minimizes the *marginal* Bayes risk $r(\pi,\delta)$. That equivalence is what licenses solving the
problem $x$ by $x$ instead of searching over whole functions $\delta$ at once, and it is worth
seeing the argument.

**Theorem.** Suppose $r(\pi,\delta_0)<\infty$ for some estimator $\delta_0$, and write
$E_x(d) = \mathbb{E}[L(\theta,d)\mid X=x]$. Then an estimator $\delta_\pi$ has finite Bayes risk
and is Bayes with respect to $\pi$ if and only if

$$
\delta_\pi(x) \in \arg\min_d E_x(d) \qquad \text{for almost every } x.
$$

*Proof.* ($\Leftarrow$) If $\delta$ is any other estimator, the hypothesis gives
$E_X(\delta_\pi(X)) \le E_X(\delta(X))$ almost surely, and marginalizing over $X$ yields
$r(\pi,\delta_\pi) \le r(\pi,\delta)$ for every $\delta$. Taking $\delta=\delta_0$ shows
$r(\pi,\delta_\pi) \le r(\pi,\delta_0) < \infty$.

($\Rightarrow$) If instead $r(\pi,\delta_\pi)=\infty$, then $\delta_0$ already has smaller Bayes
risk and $\delta_\pi$ is not Bayes; so assume $r(\pi,\delta_\pi)<\infty$ but $\delta_\pi(x)$ fails
to minimize $E_x(\cdot)$ on a set of positive probability. Then for some $\varepsilon>0$ the set

$$
A_\varepsilon = \{x:\ E_x(\delta_\pi(x)) - \inf_d E_x(d) > \varepsilon\}
$$

has $\mathbb{P}(X\in A_\varepsilon)>0$. Build a competitor $\delta^*$: on $A_\varepsilon$, choose
$\delta^*(x)$ with $E_x(\delta^*(x)) \le \min\{E_x(\delta_\pi(x))-\varepsilon,\ E_x(\delta_0(x))\}$;
off $A_\varepsilon$, set $\delta^*(x)=\delta_\pi(x)$. Then everywhere
$E_x(\delta_\pi(x)) - E_x(\delta^*(x)) \ge \varepsilon\, 1\{x\in A_\varepsilon\}$, and taking
expectations,

$$
r(\pi,\delta_\pi) - r(\pi,\delta^*) \ge \varepsilon\,\mathbb{P}(X\in A_\varepsilon) > 0,
$$

so $\delta^*$ beats $\delta_\pi$, contradicting that $\delta_\pi$ was Bayes. $\blacksquare$

The mechanism the proof turns on is that $\delta$ can be chosen freely and independently at each
$x$: minimizing $r(\pi,\delta) = \int E_x(\delta(x))\,q(x)\,dx$ over *functions* decouples into
minimizing the integrand $E_x(d)$ over $d$ separately at every $x$, because nothing ties the
choice made at one $x$ to the choice made at another.

## Squared error loss: the Bayes estimator is the posterior mean

Take $L(\theta,d) = (g(\theta)-d)^2$ for some functional $g$ of interest — $g(\theta)=\theta$ is
the usual case, but $g$ need not be the identity. Add and subtract $\mathbb{E}[g(\theta)\mid X]$
inside the square:

$$
\mathbb{E}[(g(\theta)-d)^2 \mid X] = \mathrm{Var}(g(\theta)\mid X) + \big(\mathbb{E}[g(\theta)\mid X] - d\big)^2,
$$

the cross term vanishing because it has zero conditional expectation given $X$. Only the second
term depends on $d$, and it is minimized — driven to zero — by

$$
\delta_\pi(X) = \mathbb{E}[g(\theta)\mid X],
$$

the **posterior mean** of $g(\theta)$. Substituting back shows the Bayes risk itself equals
$\mathbb{E}[\mathrm{Var}(g(\theta)\mid X)]$: the average, over the data, of how much uncertainty
about $g(\theta)$ remains after conditioning.

## Weighted squared error loss

Different values of $\theta$ sometimes deserve different weight. Caring about *relative* error
$\left(\frac{g(\theta)-d}{g(\theta)}\right)^2$, for instance, corresponds to the weight
$w(\theta) = g(\theta)^{-2}$. For the general weighted loss $L(\theta,d) = w(\theta)(g(\theta)-d)^2$,

$$
\mathbb{E}[w(\theta)(g(\theta)-d)^2 \mid X] = d^2\,\mathbb{E}[w(\theta)\mid X] - 2d\,\mathbb{E}[w(\theta)g(\theta)\mid X] + \mathbb{E}[w(\theta)g(\theta)^2\mid X],
$$

a quadratic in $d$ minimized at

$$
\delta_\pi(X) = \frac{\mathbb{E}[w(\theta)g(\theta)\mid X]}{\mathbb{E}[w(\theta)\mid X]}.
$$

Ordinary squared error is the special case $w \equiv 1$.

## Conjugate priors

Computing a posterior in general means integrating $\pi(\theta)p(x\mid\theta)$ over $\theta$ to
find the normalizing constant $q(x)$, which is not always tractable. A family of priors
$\mathcal{Q}$ is **conjugate** to a likelihood family $\{P_\theta\}$ if, whenever the prior is
chosen from $\mathcal{Q}$, the posterior lands back in $\mathcal{Q}$ too, for every $x$. This is
why the Beta and Gamma families pair so naturally with the Binomial and Poisson likelihoods.

### Beta–Binomial

Let $\theta \sim \mathrm{Beta}(\alpha,\beta)$ and $X\mid\theta \sim \mathrm{Binomial}(n,\theta)$.
The posterior only needs to be tracked up to proportionality in $\theta$:

$$
\pi(\theta\mid x) \propto \theta^{\alpha-1}(1-\theta)^{\beta-1}\cdot\theta^{x}(1-\theta)^{n-x} = \theta^{x+\alpha-1}(1-\theta)^{n-x+\beta-1},
$$

so $\theta\mid X=x \sim \mathrm{Beta}(x+\alpha,\ n-x+\beta)$, with posterior mean — the Bayes
estimator under squared error —

$$
\mathbb{E}[\theta\mid X] = \frac{X+\alpha}{n+\alpha+\beta}.
$$

This carries the same *pseudo-observation* reading used for shrinkage estimators: it behaves as
if $k=\alpha+\beta$ extra trials had been observed, of which $\alpha$ were successes, combined
with the $n$ real trials. Rearranging makes this a weighted average of the sample proportion and
the pseudo-observation rate, weighted by relative sample size:

$$
\mathbb{E}[\theta\mid X] = \frac{X}{n}\cdot\frac{n}{n+k} + \frac{\alpha}{k}\cdot\frac{k}{n+k}.
$$

Taking $\alpha=\beta=1$ gives the uniform prior on $[0,1]$, and the resulting estimator
$\frac{X+1}{n+2}$ minimizes the Bayes risk $\int_0^1 R(\theta,\delta)\,d\theta$ over *every*
estimator $\delta$ — a checkable optimality claim, not just a heuristic.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Beta prior and binomial likelihood combining into a Beta posterior that sits between them">
  <line x1="30" y1="170" x2="310" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="192" text-anchor="middle" font-size="12" fill="currentColor">theta</text>

  <path d="M 80 170 C 115 170 132.5 115 150 115 C 167.5 115 185 170 220 170"
        fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3"/>
  <text x="72" y="105" font-size="12" fill="currentColor">prior</text>

  <path d="M 175 170 C 202.5 170 217.75 75 230 75 C 242.25 75 257.5 170 285 170"
        fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3"/>
  <text x="255" y="68" font-size="12" fill="currentColor">likelihood</text>

  <path d="M 145 170 C 170 170 183.5 70 195 70 C 206.5 70 220 170 245 170 Z"
        fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="2"/>
  <text x="176" y="58" font-size="12" fill="currentColor">posterior</text>
</svg>
<figcaption>The Beta prior and binomial likelihood, each drawn as a density-shaped bump in theta,
combine into the Beta posterior (shaded): it sits between them, and is narrower than the prior
because the data have added information — the mechanism behind the pseudo-observation weighted
average above.</figcaption>
</figure>

### Normal mean

Let $X\mid\theta \sim N(\theta,\sigma^2)$ with $\sigma^2$ known, and $\theta \sim N(\mu,\tau^2)$.
Multiplying the two densities and completing the square in $\theta$ shows the posterior is again
Gaussian:

$$
\theta\mid X=x \ \sim\ N\!\left(\frac{x\sigma^{-2}+\mu\tau^{-2}}{\sigma^{-2}+\tau^{-2}},\ \frac{1}{\sigma^{-2}+\tau^{-2}}\right).
$$

This reads most cleanly in terms of *precision* (reciprocal variance): the posterior precision is
the **sum** of the prior and likelihood precisions, and the posterior mean is the
precision-weighted average of the data and the prior mean:

$$
\mathbb{E}[\theta\mid X] = X\cdot\frac{\sigma^{-2}}{\sigma^{-2}+\tau^{-2}} + \mu\cdot\frac{\tau^{-2}}{\sigma^{-2}+\tau^{-2}}.
$$

With an i.i.d. sample $X_1,\dots,X_n \sim N(\theta,\sigma^2)$, sufficiency reduces the data to
$\bar X \sim N(\theta,\sigma^2/n)$, and the same formula gives

$$
\theta\mid X \ \sim\ N\!\left(\frac{n\bar X + k\mu}{n+k},\ \frac{\sigma^2}{n+k}\right), \qquad k=\frac{\sigma^2}{\tau^2},
$$

the pseudo-observation picture again: the prior behaves like $k$ extra observations averaging
$\mu$.

### Poisson–Gamma

Let $X\mid\theta \sim \mathrm{Poisson}(\theta)$ and $\theta \sim \mathrm{Gamma}(\alpha,\beta)$. The
same kind of density multiplication gives, for an i.i.d. sample,

$$
\theta \mid X_1,\dots,X_n \ \sim\ \mathrm{Gamma}\Big(\alpha + \textstyle\sum_i X_i,\ \ \beta+n\Big),
$$

with $\alpha$ read as pseudo-counts and $\beta$ as pseudo-exposure: the shape parameter
accumulates observed counts, and the rate parameter accumulates observed "time" or "trials".

## Why exponential families always have a conjugate prior

All three examples share a pattern worth stating in general. Suppose $X_1,\dots,X_n$ are i.i.d.
from an $s$-parameter exponential family $p_\eta(x) = \exp(\eta'T(x)-A(\eta))h(x)$. For any base
density $\pi_0$, and any $k\in\mathbb{R}$, $\mu\in\mathbb{R}^s$, define

$$
\pi_{\mu,k}(\eta) = \exp\big(k\mu'\eta - kA(\eta) - B(k\mu,k)\big)\,\pi_0(\eta).
$$

Since $\eta$ is now the random variable rather than a parameter, this is itself an
$(s+1)$-parameter exponential family, with sufficient statistic $(\eta,\,-A(\eta))$ and natural
parameter $(k\mu,\,k)$. Multiplying by the likelihood of the $n$ observations,

$$
\pi(\eta\mid x) \ \propto\ \exp\Big(\big(k\mu+\textstyle\sum_i T(x_i)\big)'\eta - (k+n)A(\eta)\Big)\pi_0(\eta) \ \propto\ \pi_{\mu_{\mathrm{post}}(x),\,n+k}(\eta),
$$

where

$$
\mu_{\mathrm{post}}(x) = \frac{n\bar T(x) + k\mu}{n+k}, \qquad \bar T(x) = \frac{1}{n}\sum_i T(x_i).
$$

The posterior stays in the same family, with hyperparameters updated by exactly the
pseudo-observation rule seen in every example above: $k$ becomes $n+k$, and $\mu$ is replaced by
the weighted average of the data's sufficient statistic and the old $\mu$. Two caveats carry over
from the worked examples: $\mu_{\mathrm{post}}(x)$ coincides with the posterior mean
$\mathbb{E}_\eta[T(X)]$ in many cases, but this is not automatic in general, and the normalizing
constant $B(k\mu,k)$ need not have a closed form even when everything else does.

## Sources

All material is from the "Bayes Estimation" reader chapter of Berkeley STAT 210A, which recurs
across three offerings with the same content split two ways: a fuller prose treatment (fall-2025
and fall-2026 readers, essentially identical) and a terser outline treatment (fall-2024 reader and
the fall-2025 `units/reader` copy). Where they overlap, the prose treatment is used below as the
clearer of the two; the outline treatment supplies one worked example the prose version omits.

- Bayes risk, the prior/posterior setup, and the characterization theorem (with full proof in both
  directions): `docs/statistics/berkeley/stat210a/fall-2025/reader/bayes-estimation/01-1-frequentist-motivation-for-a-bayes-estimator.md`
  and `02-2-bayes-estimator.md` (identical content in `fall-2026/reader/bayes-estimation/01-...md`
  and `02-bayes-estimator.md`). The same result, stated without the epistemic discussion and with
  a shorter proof sketch, appears in `fall-2024/reader/bayes-estimation/01-bayes-risk-and-bayes-estimator.md`
  and `fall-2025/units/reader/bayes-estimation/01-1-bayes-risk-and-bayes-estimator.md`.
- Squared error and weighted squared error loss: same files as above (`02-2-bayes-estimator.md` /
  `02-bayes-estimator.md`), matching the terser statement in
  `fall-2024/reader/bayes-estimation/01-bayes-risk-and-bayes-estimator.md` (squared error only) and
  `fall-2025/units/reader/bayes-estimation/01-1-bayes-risk-and-bayes-estimator.md`.
- Beta–Binomial and Normal-mean conjugate examples, the precision interpretation, the i.i.d.
  extension, and the general exponential-family conjugate-prior construction:
  `fall-2025/reader/bayes-estimation/03-3-conjugate-priors.md` (identical in
  `fall-2026/reader/bayes-estimation/03-conjugate-priors.md`). The interactive Beta-Binomial
  visualization described in that source (prior/likelihood/posterior density sliders) is
  represented above as a static diagram rather than reproduced as code.
- The Poisson–Gamma example and the "pseudo-counts / pseudo-exposure" phrasing, and an alternate
  (equivalent) general statement of exponential-family conjugacy via a function $u(\theta)$:
  `fall-2024/reader/bayes-estimation/03-conjugate-priors.md` and
  `fall-2025/units/reader/bayes-estimation/03-4-conjugate-priors.md` — the Poisson–Gamma pair does
  not appear in the fuller fall-2025/2026 treatment and is included here as it is the only source
  for it; the alternate general form was judged redundant with the version given above and is not
  reproduced separately.
- Also referenced in the source but not supplied here: "Lecture 2" on estimator risk,
  admissibility, and the shrinkage/pseudo-observation estimators that motivate averaging the risk
  in the first place.
- No exercises accompanied this reader chapter in any of the three offerings.

---

[← 2. Why Bayesian Computation Needs MCMC](02-why-bayesian-computation-needs-mcmc.md) · [Contents](index.md) · [4. Where Does the Prior Come From? →](04-where-does-the-prior-come-from.md)
