---
title: "39. Bayes Estimation for Frequentists"
course: "Berkeley Stat 210A Fall 2024"
chapter: 39
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 39. Bayes Estimation for Frequentists

## What this covers

The lecture opens by billing itself as Bayes estimation "for frequentists": nothing here requires
believing that $\theta$ is literally random. It answers a narrower, more mechanical question —
given a decision problem (a model $\mathcal P$, a loss $L$), what happens if you average risk over
a measure on $\theta$ instead of asking for one $\theta$ at a time to look good? The answer is that
averaging turns a hard search over all estimators into an easy search over a single value of $d$
for each $x$, and the chapter works this out, characterizes the resulting **Bayes estimator**
under squared error, and runs it through the two standard worked examples (Beta–Binomial,
Normal mean) before extracting the general pattern — conjugate priors in exponential families —
and closing with a look at how a frequentist might pick a prior when nothing is genuinely believed
about $\theta$. It assumes the decision-theoretic vocabulary of risk functions $R(\theta,\delta)$,
comfort with exponential families and sufficiency, and the notion of a UMVU (uniformly minimum
variance unbiased) estimator from earlier in the course.

## Bayes risk

Fix a model $\mathcal P = \{P_\theta : \theta \in \Theta\}$ for data $X$, a loss $L(\theta,d)$, and
the risk $R(\theta,\delta) = \mathbb E_\theta[L(\theta,\delta(X))]$ of an estimator $\delta$. A risk
*function* — one number for every $\theta$ — is hard to compare across estimators unless one
dominates another everywhere. One way to collapse it to a single number is to average it against
some measure $\Lambda$ on $\Theta$, called the **prior**:

$$
r_\Lambda(\delta) = \int_\Theta R(\theta,\delta)\,d\Lambda(\theta),
$$

the **Bayes risk** of $\delta$. For now take $\Lambda$ to be a probability measure ($\Lambda(\Theta)=1$);
later in the course this is relaxed to allow *improper* priors with $\Lambda(\Theta)=\infty$. Two
things are worth noting immediately. First, $\Lambda$ and $c\Lambda$ for any $c>0$ give
functionally equivalent Bayes risks (they only rescale $r_\Lambda$), so only the *shape* of
$\Lambda$ matters. Second — and this is the "for frequentists" point — averaging risk this way
makes sense as a purely technical device for summarizing a risk function, whether or not one is
prepared to say "I believe $\theta \sim \Lambda$."

Writing $\theta \sim \Lambda$ and $X \mid \theta \sim P_\theta$ turns the outer integral into an
expectation over the *joint* distribution of $(\theta, X)$:

$$
r_\Lambda(\delta) = \mathbb E_{\theta\sim\Lambda}[R(\theta,\delta)]
= \mathbb E_{\theta\sim\Lambda}\big[\mathbb E[L(\theta,\delta(X))\mid\theta]\big]
= \mathbb E[L(\theta,\delta(X))],
$$

where the last expectation is with respect to the joint law of $(\theta,X)$. An estimator $\delta$
minimizing $r_\Lambda(\cdot)$ over all estimators is called a **Bayes estimator** (it depends on
$\mathcal P$, $\Lambda$, and $L$ all three). The move that makes this tractable is to apply the
tower property the other way — condition on $X$ first instead of $\theta$:

$$
r_\Lambda(\delta) = \mathbb E\Big[\, \mathbb E[L(\theta,\delta(X)) \mid X]\,\Big].
$$

This rewrites a single hard minimization (search over all functions $\delta$) as an outer average
of many easy ones: for each fixed $x$, choose $d = \delta(x)$ to minimize $\mathbb E[L(\theta,d)\mid X=x]$,
and do this independently for every $x$. Note that this is a coherent thing to do only because
$\delta$ is chosen *after* seeing $X$.

## Prior, posterior, and the Bayes estimator

The usual reading of $\Lambda$ is "belief about $\theta$ before seeing the data." The conditional
distribution $\Lambda(\theta \mid X)$ is then the **posterior**: belief after seeing the data. This
is where the interpretation of "probability" as **epistemic uncertainty** — "I think there is a
50% chance that…" — enters, and where a genuinely Bayesian reading of the machinery starts to
diverge from the "just a device for averaging risk" reading above; the lecture flags this
distinction and defers the discussion to the next lecture.

In densities: write the prior $\lambda(\theta)$, the likelihood $p_\theta(x)$ (equivalently
$p(x\mid\theta)$), the **joint density** $\lambda(\theta)p_\theta(x)$, the **marginal density**

$$
q(x) = \int_\Theta \lambda(\theta)\,p_\theta(x)\,d\theta,
$$

and the **posterior density**

$$
\lambda(\theta\mid x) = \frac{\lambda(\theta)\,p_\theta(x)}{q(x)}.
$$

The Bayes estimator is defined entirely in terms of the posterior:

$$
\delta_\Lambda(x) = \arg\min_d\, \mathbb E[L(\theta,d)\mid X=x]
= \arg\min_d \int_\Theta L(\theta,d)\,\lambda(\theta\mid x)\,d\theta.
$$

Solve for it "one $x$ at a time": the posterior at $x$ is all that is needed to produce
$\delta_\Lambda(x)$, independently of what the posterior looks like at any other $x$.

## Characterizing the Bayes estimator

The pointwise recipe above is not just *a* way to build an estimator with small Bayes risk — under
mild conditions it is *the* Bayes estimator, and every Bayes estimator agrees with it almost
everywhere. Precisely:

> Suppose $X\mid\theta \sim P_\theta$, the loss is nonnegative, $L(\theta,d)\ge 0$, and some
> estimator $\delta_0$ already has finite Bayes risk, $r_\Lambda(\delta_0) < \infty$. Let
> $\delta_\Lambda(x)$ denote a (measurable) choice of $\arg\min_d \mathbb E[L(\theta,d)\mid X=x]$
> at each $x$. Then $r_\Lambda(\delta_\Lambda) < \infty$ and $\delta_\Lambda$ is Bayes; moreover an
> estimator $\delta$ is Bayes with $r_\Lambda(\delta) < \infty$ **if and only if**
> $\delta(x) \in \arg\min_d \mathbb E[L(\theta,d)\mid X=x]$ for almost every $x$.

**Proof.** Write $E_x(d) = \mathbb E[L(\theta,d)\mid X=x]$.

*($\Leftarrow$, the pointwise minimizer is Bayes.)* For any competing estimator $\delta$,
pointwise (a.s. in $X$), $E_X(\delta(X)) \ge E_X(\delta_\Lambda(X))$, since $\delta_\Lambda(X)$ was
chosen to minimize $E_X(\cdot)$. Take expectations over $X$ (tower property):
$r_\Lambda(\delta) \ge r_\Lambda(\delta_\Lambda)$. Taking $\delta = \delta_0$ in particular shows
$r_\Lambda(\delta_\Lambda) \le r_\Lambda(\delta_0) < \infty$. So $\delta_\Lambda$ attains the
smallest Bayes risk among all estimators, with that risk finite.

*($\Rightarrow$, a Bayes estimator must be a pointwise minimizer a.e.)* Suppose $\delta$ is Bayes
with $r_\Lambda(\delta) < \infty$, and suppose toward a contradiction that
$\delta(x) \notin \arg\min_d E_x(d)$ on a set of positive probability. Then there is some
$\varepsilon > 0$ for which

$$
A_\varepsilon = \Big\{\, x : E_x(\delta(x)) > \varepsilon + \inf_d E_x(d) \,\Big\}
$$

still has $\mathbb P(X \in A_\varepsilon) > 0$. Build a competitor $\delta^*$: on $A_\varepsilon$
pick $\delta^*(x)$ within $\varepsilon$ of the infimum, $E_x(\delta^*(x)) \le E_x(\delta(x)) - \varepsilon$;
elsewhere set $\delta^* = \delta$. Then everywhere
$E_x(\delta(x)) - E_x(\delta^*(x)) \ge \varepsilon\,\mathbf 1\{x\in A_\varepsilon\}$, and taking
expectations,

$$
r_\Lambda(\delta) - r_\Lambda(\delta^*) \ge \varepsilon\,\mathbb P(X\in A_\varepsilon) > 0,
$$

contradicting that $\delta$ already had the smallest possible Bayes risk. So the bad set has
probability $0$. $\blacksquare$

## Squared error and the posterior mean

Take $L(\theta,d) = (g(\theta)-d)^2$ for some target functional $g(\theta)$. Add and subtract the
posterior mean of $g(\theta)$ inside the square:

$$
\mathbb E[(g(\theta)-d)^2 \mid X]
= \mathbb E\big[(g(\theta) - \mathbb E[g(\theta)\mid X])^2 \mid X\big]
+ (\mathbb E[g(\theta)\mid X] - d)^2
= \operatorname{Var}(g(\theta)\mid X) + (\mathbb E[g(\theta)\mid X]-d)^2.
$$

(The cross term vanishes because, conditionally on $X$, $\mathbb E[g(\theta)\mid X]-d$ is a
constant that factors out of the remaining conditional expectation of $g(\theta)-\mathbb E[g(\theta)\mid X]$,
which is zero by the definition of the conditional mean.) The first term does not depend on $d$,
so the expression is minimized uniquely at

$$
\delta_\Lambda(x) = \mathbb E[g(\theta)\mid X=x]:
$$

**under squared error loss, the Bayes estimator is the posterior mean.**

A useful variant is **weighted squared error**, $L(\theta,d) = w(\theta)(g(\theta)-d)^2$ — for
example $w(\theta)=1/\theta^2$ gives squared *relative* error, $\big(\tfrac{\theta-d}{\theta}\big)^2$.
Expanding as a quadratic in $d$,

$$
\mathbb E[(d-g(\theta))^2 w(\theta)\mid X]
= d^2\,\mathbb E[w(\theta)\mid X] - 2d\,\mathbb E[w(\theta)g(\theta)\mid X] + \mathbb E[w(\theta)g(\theta)^2\mid X],
$$

and the last term does not involve $d$. This is minimized at the **weighted posterior mean**

$$
\delta_\Lambda(x) = \frac{\mathbb E[w(\theta)g(\theta)\mid X]}{\mathbb E[w(\theta)\mid X]}.
$$

## Example: Beta–Binomial

Take $X\mid\theta \sim \operatorname{Binom}(n,\theta)$ and put a $\operatorname{Beta}(\alpha,\beta)$
prior on $\theta$ — here $\theta$ is genuinely the random variable being integrated against. The
marginal distribution of $X$ this induces is called the **Beta-Binomial**. The posterior is found
by multiplying prior and likelihood and dropping everything that does not depend on $\theta$:

$$
\lambda(\theta\mid x) \propto_\theta \theta^{\alpha-1}(1-\theta)^{\beta-1}\cdot \theta^x(1-\theta)^{n-x}
= \theta^{x+\alpha-1}(1-\theta)^{n-x+\beta-1},
$$

so $\theta \mid X=x \sim \operatorname{Beta}(x+\alpha,\, n-x+\beta)$, and the posterior mean is

$$
\mathbb E[\theta\mid X] = \frac{X+\alpha}{n+\alpha+\beta}
= \underbrace{\frac{X}{n}}_{\text{UMVU}}\cdot\frac{n}{n+\alpha+\beta}
+ \underbrace{\frac{\alpha}{\alpha+\beta}}_{\text{prior mean}}\cdot\frac{\alpha+\beta}{n+\alpha+\beta}.
$$

This is a **convex combination** of the data-based UMVU estimator $X/n$ and the prior mean
$\alpha/(\alpha+\beta)$. The natural reading: $k=\alpha+\beta$ behaves like a number of
"pseudo-trials" already folded into the prior, with $\alpha$ of them "pseudo-successes" — the
prior contributes exactly as much information as $k$ extra coin flips would. (This is the source
of the estimator $\frac{X+3}{n+6}$ seen earlier in the course, at Lecture 2 — not included in this
material, but recognizable now as $\alpha=\beta=3$.)

## Example: Normal mean

Take $X\mid\theta \sim N(\theta,\sigma^2)$ with a $N(\mu,\tau^2)$ prior on $\theta$. Multiplying
densities and collecting terms linear and quadratic in $\theta$,

$$
\lambda(\theta\mid x) \propto_\theta \exp\left\{-\frac{(x-\theta)^2}{2\sigma^2} - \frac{(\theta-\mu)^2}{2\tau^2}\right\}
\propto_\theta \exp\Big\{ \theta\underbrace{\Big(\tfrac{x}{\sigma^2}+\tfrac{\mu}{\tau^2}\Big)}_{b}
- \theta^2\underbrace{\Big(\tfrac{\sigma^{-2}+\tau^{-2}}{2}\Big)}_{a^2} \Big\},
$$

and completing the square in $\theta$ identifies the posterior as Gaussian:

$$
\theta \mid X=x \;\sim\; N\!\left(\frac{x\sigma^{-2}+\mu\tau^{-2}}{\sigma^{-2}+\tau^{-2}},\; \frac{1}{\sigma^{-2}+\tau^{-2}}\right).
$$

The posterior mean is a **precision-weighted average** of $x$ and $\mu$, and the posterior
variance is the reciprocal of the sum of the prior and data precisions — the posterior is at least
as precise as either input alone:

$$
\mathbb E[\theta\mid X] = X\cdot\frac{\sigma^{-2}}{\sigma^{-2}+\tau^{-2}} + \mu\cdot\frac{\tau^{-2}}{\sigma^{-2}+\tau^{-2}}.
$$

For an i.i.d. sample $X_1,\dots,X_n \mid \theta \overset{\text{iid}}{\sim} N(\theta,\sigma^2)$ with
the same prior, sufficiency reduces the data to $\bar X\mid\theta \sim N(\theta,\sigma^2/n)$, and
the same computation with $\sigma^2/n$ in place of $\sigma^2$ gives

$$
\mathbb E[\theta\mid X] = \bar X\cdot\frac{n}{n+\sigma^2/\tau^2} + \mu\cdot\frac{\sigma^2/\tau^2}{n+\sigma^2/\tau^2}.
$$

Exactly as before, $k=\sigma^2/\tau^2$ plays the role of a number of "pseudo-observations" at the
prior mean $\mu$: if $n \gg k$, "data swamps prior"; if $n \ll k$, "prior swamps data."

<figure>
<svg viewBox="0 0 380 170" role="img" aria-label="The posterior mean sliding from the prior mean toward the data statistic as the sample size grows">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="110" x2="340" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="60" cy="110" r="5" fill="currentColor"/>
  <text x="60" y="95" text-anchor="middle" font-size="12" fill="currentColor">prior mean</text>
  <text x="60" y="135" text-anchor="middle" font-size="11" fill="currentColor">weight k/(n+k)</text>
  <circle cx="320" cy="110" r="5" fill="currentColor"/>
  <text x="320" y="95" text-anchor="middle" font-size="12" fill="currentColor">data statistic</text>
  <text x="320" y="135" text-anchor="middle" font-size="11" fill="currentColor">weight n/(n+k)</text>
  <circle cx="120" cy="110" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="270" cy="110" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="128" y1="110" x2="262" y2="110" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
  <text x="195" y="155" text-anchor="middle" font-size="12" fill="currentColor">posterior mean, as n grows</text>
</svg>
<figcaption>In both worked examples the posterior mean is a convex combination of the prior mean
and a data statistic, weighted n : k. As the real sample size n grows past the "pseudo-sample
size" k contributed by the prior, the estimate slides from the prior mean toward the data.</figcaption>
</figure>

In both examples: the prior and the likelihood have the same functional form in $\theta$, and the
posterior comes out of the same family as the prior. When this happens, the prior is called
**conjugate** to the likelihood. It is most common — and most tractable — in exponential families.

## Conjugate priors, in general

The pattern generalizes. Suppose $X_1,\dots,X_n \mid \eta \overset{\text{iid}}{\sim} p_\eta(x) = e^{\eta'T(x)-A(\eta)}h(x)$,
an $s$-dimensional exponential family with natural parameter $\eta \in \Xi \subseteq \mathbb R^s$.
Fix a carrier density $\lambda_0(\eta)$ on the parameter space and define, for $(\mu,k)$ ranging
over an $(s+1)$-dimensional family,

$$
\lambda_{\mu,k}(\eta) = e^{\,k\mu'\eta - kA(\eta) - B(k\mu,k)}\,\lambda_0(\eta),
$$

with $B$ the log normalizing constant. This is itself an exponential family in $\eta$, with
sufficient statistic $\big(\eta,\,-A(\eta)\big) \in \mathbb R^{s+1}$ and natural parameter
$(k\mu,\,k)$ — a prior built as if $\eta$ had already produced $k$ pseudo-observations whose
sufficient statistic averaged to $\mu$. Multiplying by the actual likelihood of $n$ real i.i.d.
draws,

$$
\lambda(\eta \mid x_1,\dots,x_n) \propto_\eta
\Big(\textstyle\prod_i e^{\eta'T(x_i)-A(\eta)}h(x_i)\Big)\cdot e^{k\mu'\eta - kA(\eta) - B(k\mu,k)}\lambda_0(\eta)
\propto_\eta e^{(k\mu+\sum T(x_i))'\eta - (k+n)A(\eta)}\lambda_0(\eta)
= \lambda_{\mu_{\text{post}},\,k+n}(\eta),
$$

with

$$
\mu_{\text{post}} = \frac{k\mu + n\bar T}{k+n}, \qquad \bar T(x) = \frac1n\sum_{i=1}^n T(x_i).
$$

The posterior lands back in the *same* $(s+1)$-parameter family, with the pseudo-sample-size
updated from $k$ to $k+n$ and the pseudo-mean updated to $\mu_{\text{post}}$ — a weighted average
of $\bar T$ (the UMVUE computed from the actual data, since $T$ is complete sufficient) and $\mu$
(the "UMVUE" one would get from $k$ pseudo-observations at the prior's value):

$$
\mu_{\text{post}} = \bar T \cdot \frac{n}{k+n} + \mu \cdot \frac{k}{k+n},
$$

and $\mu_{\text{post}}$ is often exactly the Bayes estimator for $\mathbb E_\eta T$. This is the
same $k$-and-$\mu$ bookkeeping seen twice already: $k=\alpha+\beta$, $\mu = \alpha/(\alpha+\beta)$
for Beta–Binomial; $k=\sigma^2/\tau^2$, $\mu$ the prior mean for the Gaussian.

| Likelihood | Conjugate prior |
| :--- | :--- |
| $X_i\mid\theta \sim \operatorname{Binom}(1,\theta) = \theta^x(1-\theta)^{1-x}$ | $\theta \sim \operatorname{Beta}(\alpha,\beta) = \theta^{\alpha-1}(1-\theta)^{\beta-1}\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ |
| $X_i\mid\theta \sim N(\theta,\sigma^2)$, $\sigma^2$ known | $\theta \sim N(\mu,\tau^2)$ |
| $X_i\mid\theta \sim \operatorname{Pois}(\theta)$, $x=0,1,\dots$ | $\theta \sim \operatorname{Gamma}(\nu,s)$, $\theta>0$, density $\dfrac{1}{\Gamma(\nu)s^\nu}\theta^{\nu-1}e^{-\theta/s}$ |

Working the Gamma/Poisson pair by hand: for $X_i\mid\theta \overset{\text{iid}}{\sim}\operatorname{Pois}(\theta)$
and $\theta\sim\operatorname{Gamma}(\nu,s)$,

$$
\lambda(\theta\mid x) \propto_\theta \theta^{\nu-1+\sum x_i}\, e^{-(s^{-1}+n)\theta}
= \operatorname{Gamma}\!\Big(\nu+\textstyle\sum x_i,\; (s^{-1}+n)^{-1}\Big),
$$

matching the general formula with $k = s^{-1}$ and $\mu = \nu s$ (the prior mean). The carrier here
is $\lambda_0(\theta) = \theta^{-1}$, which is not itself a normalizable density — a reminder that
the carrier only has to make the *tilted* family $\lambda_{\mu,k}$ proper for $k>0$, not be a prior
in its own right.

## Why be Bayes? The flexibility argument

For *any* $\Lambda$, $\mathcal P$, $L$, and target $g(\theta)$, the Bayes estimator is defined by
the same one-line recipe,

$$
\delta_\Lambda(x) = \arg\min_d \int L(\theta,d)\,\lambda(\theta\mid x)\,d\theta,
$$

which reduces the estimation problem to a (possibly hard) computation. The posterior is a
"one-stop shop": once it is known, every question about how to estimate anything under any loss
has the same recipe applied to it. In particular there is no need for the special structure that
other estimation theories lean on — no exponential-family-plus-complete-sufficient-statistic
requirement, no need for the target to be U-estimable, no need for the loss to be convex or
otherwise well-behaved. This buys highly expressive modeling and estimation. The price is that the
whole enterprise is now limited by the ability to actually *do* the computation — evaluate that
integral, or the analogous one defining the posterior itself.

## A frequentist alternative to specifying a prior

Choosing $\Lambda$ to encode genuine prior belief is one motivation for the whole machinery; a
second, distinct motivation is to use a "default" or **vague** prior that is not meant to encode
belief at all, precisely to remove the subjectivity of choosing one — though this immediately
raises the question of what the resulting posterior is then supposed to mean.

The simplest default is the **flat prior**, $\lambda(\theta) \propto_\theta 1$ on $\Theta$,
read as "indifference" — but indifference *in this particular parameterization*. It is often
improper ($\Lambda(\Theta)=\infty$) but usually still yields a well-defined, proper posterior. For
example, a flat prior on $\mathbb R$ for $\theta$ with $X\mid\theta\sim N(\theta,\sigma^2)$ gives a
posterior proportional to the likelihood alone,

$$
\lambda(\theta\mid x) \propto_\theta p_\theta(x) \propto_\theta N(x,\sigma^2),
$$

i.e. posterior mean $=x$, the MLE — exactly the $k=0$ limit ($\tau^2\to\infty$) of the
pseudo-observation formula above: a prior with no pseudo-observations contributes nothing.

A flat prior is not invariant to reparameterization, though: flat in $\theta$ is generally not
flat in some bijective reparametrization $g(\theta)$. The **Jeffreys prior**,

$$
\lambda(\theta) \propto_\theta |J(\theta)|^{1/2},
$$

built from the Fisher information $J(\theta)$, fixes this: it is invariant to parameterization,
and it puts higher density where $P_\theta$ is "changing faster" — where the model moves more, in
distribution, per unit change in $\theta$. For $X\mid\theta \sim \operatorname{Binom}(n,\theta)$,
$J(\theta) = n/(\theta(1-\theta))$, so

$$
\lambda(\theta) \propto_\theta \Big(\theta(1-\theta)\Big)^{-1/2} \;\propto_\theta\; \operatorname{Beta}\!\left(\tfrac12,\tfrac12\right),
$$

which blows up as $\theta \to 0$ or $1$. The reason it should: two pairs of parameter values that
are about the same raw distance apart can correspond to very different amounts of statistical
change. Comparing Kullback–Leibler divergences (figures as given in the source, approximate),
$D_{\mathrm{KL}}(0.001 \,\|\, 0.01)$ comes out roughly $35\times$ larger than
$D_{\mathrm{KL}}(0.49\,\|\,0.5)$, even though $|\Delta\theta|$ is about $0.009$–$0.01$ in both
pairs: near the boundary, a small move in $\theta$ changes the Binomial distribution far more than
the same-sized move near $\theta=1/2$ does. A flat prior in $\theta$ treats those two moves as
equally likely a priori; the Jeffreys prior, by weighting by $\sqrt{J(\theta)}$, does not.

## Sources

- Lecture 9, "Bayes Estimation," Berkeley STAT 210A. The lecture is recorded near-identically
  across three offerings; this chapter follows the fall-2025/fall-2026 write-ups for the main
  development (they agree word for word) and draws the closing section from fall-2024, which is
  the only one of the three that carries it in this material:
  - Bayes risk, prior/posterior, the Bayes-estimator existence-and-characterization theorem, and
    the posterior-mean result: `fall-2025/handwritten/lecture09-bayesestimation/01-frequentist-motivation.md`
    and `02-bayes-estimator.md` (identical in fall-2026's `01-` and `02-` files).
  - Beta–Binomial example: `fall-2025/.../03-example-beta-binomial.md` (= fall-2026's `03-`,
    = fall-2024's `02-example-beta-binomial.md`).
  - Normal-mean example (single observation and i.i.d. sample) and the definition of conjugacy:
    `fall-2025/.../04-example-normal-mean.md` (= fall-2026's `04-`, = fall-2024's
    `03-example-normal-mean.md`).
  - General conjugate-prior construction, the table of conjugate pairs, the Gamma/Poisson
    computation, and the "flexibility of Bayes" argument: `fall-2025/.../05-conjugate-priors.md`
    (= fall-2026's `05-`; the same material also closes fall-2024's `03-example-normal-mean.md`).
  - Flat and Jeffreys priors ("Source #2: 'objective' or 'vague' prior"): only in fall-2024's
    `03-example-normal-mean.md`, at the end.
  - The lecture explicitly points back to an estimator $\frac{X+3}{n+6}$ from "Lecture 2" of the
    same course when discussing the Beta–Binomial pseudo-count interpretation; that lecture is not
    part of the supplied material.
  - The lecture also flags that the "belief" reading of the prior, and what a probability
    statement about $\theta$ (epistemic uncertainty) means, is picked up "next time" — not covered
    here.
- All of the above notes are marked by their own front matter as model-reconstructed from a
  handwritten PDF with no text layer (`fidelity: reconstructed`), with every displayed equation
  flagged by the source itself as unverified; the numeric Kullback–Leibler figures in the Jeffreys
  prior example should be read with that caveat in mind.
- No slides, transcript, or exercises were supplied for this lecture.

---

[← 38. Fisher Information and Cramér–Rao Bound](38-fisher-information-and-cram-r-rao-bound.md) · [Contents](index.md) · [40. Where does $\Lambda$ come from? →](40-where-does-lambda-come-from.md)
