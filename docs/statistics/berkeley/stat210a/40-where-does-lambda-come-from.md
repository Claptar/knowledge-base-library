---
title: "40. Where does $\\Lambda$ come from?"
course: "Berkeley Stat 210A Fall 2024"
chapter: 40
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 40. Where does $\Lambda$ come from?

## What this covers

This chapter asks a question a Bayesian analysis usually skips past: once you have committed to a
prior $\Lambda$ on the parameter $\theta$, turning it into a posterior is just calculus — but where did
$\Lambda$ come from in the first place, and does it matter? The lecture works through the main answers
on offer, what each one buys and what it costs, and two worked examples (a Gaussian sequence model, and
a Gaussian hierarchical model) that show the choice of prior mattering enormously in one case and hardly
at all in another. It assumes the ordinary Bayes decision-theory setup — prior, likelihood, posterior,
Bayes risk, the notation $\delta_\Lambda$ for a Bayes rule — together with Fisher information, UMVU
estimation, and the standard conjugate families (Beta–Binomial, Normal–Normal).

## Interpretations of probability

Before asking where a *prior* comes from, it is worth asking where any probability model comes from —
what does it mean, in the world, for something to be "random" at all? The lecture separates three
answers, which are commonly blended together without being noticed:

1. **Long-run frequency over repeated trials.** Flipping a coin many times, or firing electrons at a
   double slit: probability names a stable proportion that would emerge over (real or hypothetical)
   repetition. In Heraclitus's phrase, you can never step into the same river twice — each trial is a
   fresh physical event, and "probability" is a property of the whole ensemble, not of any one trial.

2. **Systematic random sampling from a population.** Surveying 500 randomly chosen voters, or randomly
   assigning subjects to treatment and control: here the randomness is not a property of the world
   being measured, it is manufactured by the experimenter's own actions (the randomization device), and
   the resulting probability statements are about that procedure.

3. **Subjective uncertainty about a single, non-repeatable outcome.** Whether a particular president is
   re-elected, the true mass of the Higgs boson, whether $P=NP$, or whether the $100$th digit of $\pi$
   is a $5$ — none of these are repeated trials or the output of an experimenter's randomization, yet
   people assign them probabilities, sometimes with enough shared reasoning to reach broad
   intersubjective agreement even though nothing "random" happens physically.

These interpretations interact rather than partition the world cleanly. A "random" sample is only
random if the sampling mechanism really is unpredictable to the people using it; if the device used to
choose it is a deterministic pseudo-random generator, the randomness in survey sampling quietly reduces
to interpretation 3 — everyone agrees to treat the output as unpredictable because no one present knows
the seed, which is a statement about shared ignorance, not about the physical process.

## The Bayesian's own version of the question

A frequentist procedure is built from a *model* $\mathcal P = \{P_\theta : \theta\in\Theta\}$ alone. A
Bayesian procedure adds a second ingredient, a prior $\Lambda$ on $\Theta$ with density $\lambda$, and
the standard objection is that this extra ingredient is not "given" the way $\mathcal P$ supposedly is —
so where does it come from? The Bayesian rejoinder is that this cuts both ways: where does $\mathcal P$
come from, either? Committing to a sampling model is already a modeling choice, exactly as committing
to a prior is. Keeping that symmetry in mind, the lecture works through four sources people actually use
for $\Lambda$.

### Source #1: subjective belief

Take the prior to encode the analyst's own considered beliefs about $\theta$ before seeing the data.

- **For:** it genuinely brings all the analyst's relevant background knowledge to bear, and the
  resulting posterior has a completely straightforward interpretation — it is just the analyst's
  updated belief.
- **Against:** exactly because of that, the posterior is now *subjective* — a report that says "I
  think..." sits awkwardly in something presented as an objective scientific finding — and eliciting a
  real subjective distribution is hard once $\theta$ is high-dimensional or $\mathcal P$ is
  nonparametric.

**Example.** Flip a coin 20 times and see 7 heads. The MLE is $\hat\theta = 0.35$, but most people's
instinct is that $\theta=0.5$ is still the better guess. That instinct *is* a prior: a belief,
independent of this data, that manufactured coins tend to be close to fair. Sketching that belief as a
density gives something concentrated near $\theta=1/2$ and small near the ends — nothing like a flat
density on $[0,1]$.

### Source #2: "objective" or "vague" priors

The opposite strategy: use some default, mechanically-generated prior specifically so that no one's
personal belief enters the calculation. This removes the subjectivity objection, but at a price — once
no one's belief is encoded, it becomes unclear what the resulting posterior actually represents.

**The flat prior.** $\lambda(\theta)\propto_\theta 1$ on $\Theta$: every value of $\theta$ (in this
parameterization) gets equal density, meant to encode "indifference." It is frequently improper —
$\Lambda(\Theta) = \infty$ — but the resulting posterior is usually still a legitimate probability
distribution.

*Worked example.* Let $\theta$ have a flat prior on $\mathbb R$ and $X\mid\theta\sim N(\theta,\sigma^2)$.
Then
$$
\begin{aligned}
\lambda(\theta\mid x) &\propto_\theta p_\theta(x) \\
&= \frac{1}{\sqrt{2\pi}\,\sigma}\, e^{-(x-\theta)^2/2\sigma^2} \\
&\propto_\theta N(x,\sigma^2),
\end{aligned}
$$
so the posterior is a normal density in $\theta$ centered at $x$: the flat prior contributes nothing but
its own normalizing constant, and the posterior just reads off the likelihood.

**The Jeffreys prior.** $\lambda(\theta) \propto_\theta |J(\theta)|^{1/2}$, where $J$ is the Fisher
information: put more prior mass where $P_\theta$ is changing *faster* as $\theta$ varies, i.e. where
data can most sharply tell nearby parameter values apart. Unlike the flat prior, this is invariant to
which parameterization $\theta$ is written in. Heuristically, for small $\varepsilon$,
$$
\Lambda([\theta,\theta+\varepsilon)) \approx \varepsilon\,\lambda(\theta) \propto_\theta \varepsilon\sqrt{J(\theta)} \approx \sqrt{D_{\mathrm{KL}}\!\left(P_\theta \,\|\, P_{\theta+\varepsilon}\right)}
$$
— the Jeffreys prior weights an interval of $\theta$ by roughly how distinguishable, in
Kullback–Leibler divergence, the parameter values inside it are from their neighbors (left in the
course as a homework exercise).

*Worked example.* For $X\mid\theta\sim\mathrm{Binom}(n,\theta)$, $J(\theta) = n/(\theta(1-\theta))$, so
$$
\lambda(\theta) \propto_\theta J(\theta)^{1/2} = \left(\frac{n}{\theta(1-\theta)}\right)^{1/2} \propto_\theta \mathrm{Beta}\!\left(\tfrac12,\tfrac12\right),
$$
which *blows up* as $\theta\to 0$ or $\theta \to 1$ — the opposite shape from the subjective prior in
source #1. This is not a mistake: KL divergence between two nearby binomial parameters is much larger
near the boundary than near the middle — the notes record roughly
$D_{\mathrm{KL}}(0.001\,\|\,0.01) \approx 35 \times D_{\mathrm{KL}}(0.49\,\|\,0.5)$ (about
$7n\times10^{-3}$ against $2n\times10^{-4}$) — so a Jeffreys prior treats the region near $0$ and $1$ as
genuinely more informative territory, and stacks prior mass there accordingly.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A subjective prior on a coin's bias peaked at one half, next to the Jeffreys prior for the same binomial model, which grows without bound near zero and one">
  <line x1="40" y1="180" x2="335" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="345" y="184" font-size="12" fill="currentColor">θ</text>
  <text x="40" y="196" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="180" y="196" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>
  <text x="320" y="196" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="40" y="14" text-anchor="middle" font-size="10" fill="currentColor">∞</text>
  <text x="320" y="14" text-anchor="middle" font-size="10" fill="currentColor">∞</text>
  <path d="M40,178 C90,178 110,150 140,100 C160,65 165,40 180,40 C195,40 200,65 220,100 C250,150 270,178 320,178" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M40,20 C55,60 70,90 100,130 C130,160 150,168 180,168 C210,168 230,160 260,130 C290,90 305,60 320,20" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="180" y="30" text-anchor="middle" font-size="11" fill="currentColor">subjective prior</text>
  <text x="95" y="145" text-anchor="middle" font-size="11" fill="currentColor">Jeffreys prior</text>
</svg>
<figcaption>The subjective prior in source #1 concentrates mass where the analyst expects the coin
to be; the Jeffreys prior does the opposite, concentrating mass where the data would be most
informative about small changes in θ. Neither is more "correct" — they answer different questions.</figcaption>
</figure>

## When the data does the work: intersubjective agreement

There is a partial rescue that does not require agreeing on any one source: when the data are
informative enough, essentially every reasonable prior gives nearly the same posterior, because the
likelihood swamps whatever differences the priors had.

**Example.** Let $X\sim\mathrm{Binom}(10^4,\theta)$ and observe $X=3000$. The sampling standard
deviation of $X/n$ is at most $\mathrm{SD}_\theta(X/n) = \sqrt{\theta(1-\theta)/n} \le 0.005$, so the
likelihood is effectively zero outside a narrow interval $C = [0.29, 0.31]$. If every "reasonable" prior
is roughly flat across an interval this narrow, then
$$
\begin{aligned}
\lambda(\theta\mid X) &\propto_\theta \mathrm{Lik}(\theta;X) \\
&\propto_\theta \exp\!\left\{-\tfrac{J(0.3)}{2}(\theta-0.3)^2\right\} \\
&\propto_\theta N\!\left(0.3,\, J(0.3)^{-1}\right),
\end{aligned}
$$
regardless of which reasonable prior you actually started with. The data has "swamped" everyone's
prior, and the posterior becomes an intersubjectively agreed-upon object even though no two people's
priors agreed to begin with — a direct echo of interpretation 3 of probability, above.

## A prior that goes wrong: the Gaussian sequence model

Intersubjective agreement is comforting, but "objective" priors are not safe in general — the flat
prior can produce badly biased answers to a question adjacent to the one it looks fine for.

Let $X\mid\mu \sim N_d(\mu, I_d)$, $\mu\in\mathbb R^d$. The Fisher information of this location family
does not depend on $\mu$, so the Jeffreys prior is again flat: $\lambda(\mu)\propto_\mu 1$. The
posterior is then $\mu\mid X \sim N_d(X, I_d)$, so the posterior mean is $\mathbb E[\mu\mid X] = X$ —
exactly the MLE and the UMVU estimator of $\mu$. So far, no trouble.

Now estimate $\rho^2 = \|\mu\|^2$ instead. Since $\mu\mid X \sim N_d(X, I_d)$,
$$
\mathbb E\!\left[\|\mu\|^2 \mid X\right] = \|X\|^2 + d.
$$
Compare this posterior-mean estimator, $\delta_\lambda(X) = \|X\|^2 + d$, with the UMVU estimator of
$\|\mu\|^2$, which is $\delta_{\mathrm{umvu}}(X) = \|X\|^2 - d$ (unbiased because
$\mathbb E_\mu\|X\|^2 = \|\mu\|^2 + d$). The two differ by a fixed amount:
$$
\delta_\lambda(X) = \delta_{\mathrm{umvu}}(X) + 2d,
$$
and since a constant shift changes only the bias, not the variance,
$$
\begin{aligned}
\mathrm{MSE}(\mu;\delta_\lambda) &= \mathrm{Var}_\mu(\delta_\lambda) + \mathrm{Bias}_\mu(\delta_\lambda)^2 \\
&= \mathrm{Var}_\mu(\delta_{\mathrm{umvu}}) + 4d^2.
\end{aligned}
$$
The Bayes estimator from the "uninformative" flat prior has error growing like $d^2$ worse than the
UMVU estimator — ruinous once $d$ is more than a handful.

**What went wrong** is visible by asking what the flat prior on $\mu$ implies for $\rho^2$. Prior mass
assigned to $\{\rho^2 \le t\}$ scales like the volume of a ball of radius $\sqrt t$ in $\mathbb R^d$:
$$
\mathbb P(\rho^2\le t) = \mathrm{Vol}\!\left(\text{ball of radius }\sqrt t\right) = \mathrm{const}(d)\cdot t^{d/2}
\quad\Longrightarrow\quad
\lambda(\rho^2) \propto_{\rho^2} (\rho^2)^{d/2-1} = \rho^{d-2},
$$
a density that grows rapidly as $\rho^2\to\infty$ once $d>2$. "Flat" in $\mu$-coordinates is very far
from flat, or even sane, once viewed through the coordinate $\rho^2$ you actually care about: it encodes
the strong (and absurd) prior expectation that $\|\mu\|^2$ is huge. This is the sharpest lesson of the
"objective prior" strategy — flatness is a choice tied to a parameterization, not the absence of a
choice, and it can silently smuggle in exactly the kind of unexamined assumption the whole strategy was
meant to avoid.

## Source #3: prior or concurrent experience

A third source treats the current problem as one of many *structurally identical* copies, and lets a
prior emerge from the population of copies rather than from anyone's belief or a mechanical default.
This is **hierarchical** or **empirical Bayes** — the catch being that choosing the right reference
class of "copies" can itself be a hard and consequential modeling decision.

**Example.** Estimate the same-side bias of $m=48$ coin-flippers, where flipper $i$ contributes $n_i$
trials and has their own true bias $\theta_i$. Model:
$$
\alpha,\beta \sim \lambda \;(\text{a "hyperprior"}), \qquad
\theta_i \mid \alpha,\beta \overset{\text{iid}}{\sim} \mathrm{Beta}(\alpha,\beta), \qquad
X_i \mid \alpha,\beta,\theta \overset{\text{ind}}{\sim} \mathrm{Binom}(n_i,\theta_i).
$$
Conditional on the hyperparameters, Beta–Binomial conjugacy gives
$$
\mathbb E[\theta_i \mid X,\alpha,\beta] = \frac{X_i+\alpha}{n_i+\alpha+\beta}.
$$
Since $(\alpha,\beta)$ are not actually known, the full posterior mean averages this over the posterior
of the hyperparameters given *all* the flippers' data:
$$
\mathbb E[\theta_i\mid X] = \mathbb E\!\left[\mathbb E[\theta_i\mid X,\alpha,\beta]\mid X\right]
= \iint \frac{X_i+\alpha}{n_i+\alpha+\beta}\,\lambda(\alpha,\beta\mid X)\, d\alpha\, d\beta.
$$
When $m$ is large, the pooled data across all 48 flippers pin $(\alpha,\beta)$ down almost exactly, so
$\lambda(\alpha,\beta\mid X)$ concentrates and the choice of hyperprior $\lambda$ stops mattering much —
intersubjective agreement recurring one level up the hierarchy.

### Worked example: the Gaussian hierarchical model

The same mechanism, worked by hand in a Gaussian setting where the algebra stays closed-form. Model:
$$
\tau^2\sim \lambda_0, \qquad \theta_i \mid \tau^2 \overset{\text{iid}}{\sim} N(0,\tau^2)\ (i\le d), \qquad X_i\mid\tau^2,\theta \overset{\text{ind}}{\sim} N(\theta_i, 1).
$$
Given $\tau^2$, Normal–Normal conjugacy gives $\mathbb E[\theta_i\mid X,\tau^2] = \frac{\tau^2}{1+\tau^2}X_i$. Averaging over the unknown $\tau^2$,
$$
\delta(X_i) = \mathbb E[\theta_i\mid X] = \mathbb E\!\left[\mathbb E[\theta_i\mid X,\tau^2]\mid X\right]
= \mathbb E\!\left[\frac{\tau^2}{1+\tau^2}\,\middle|\, X\right]\cdot X_i,
$$
a **linear shrinkage estimator**: every coordinate is shrunk toward $0$ by a common factor, and that
factor is itself estimated from the data rather than fixed in advance.

To estimate the shrinkage factor, write $\zeta = \frac{1}{1+\tau^2}$ (so the factor is $1-\zeta$) and
marginalize $\theta$ out of the model: $X_i\mid\tau^2 \sim N(0,1+\tau^2)$ independently across $i$, so
$$
\|X\|^2 \mid \tau^2 \sim (1+\tau^2)\,\chi^2_d,
$$
i.e. $\|X\|^2/d$ has mean $1+\tau^2$ and variance $2(1+\tau^2)^2/d$. Putting a conjugate
(scaled-inverse-$\chi^2$) prior on $\zeta$,
$$
\zeta \sim \tfrac1s\chi^2_k \quad\Longleftrightarrow\quad \text{density} \propto \zeta^{k/2-1}e^{-s\zeta},
$$
and combining with the sampling density of $v=\|X\|^2$ given $\zeta$ (density $\propto \zeta^{d/2}v^{d/2-1}e^{-\zeta v}$) gives, by the usual conjugate-family argument,
$$
\zeta \mid \|X\|^2 \;\propto_\zeta\; \zeta^{\frac{k+d}{2}-1} e^{-(s+\|X\|^2)\zeta}
\quad\Longrightarrow\quad
\zeta\mid\|X\|^2 \sim \frac{1}{s+\|X\|^2}\chi^2_{k+d},
$$
with posterior mean $\mathbb E[\zeta\mid\|X\|^2] = \dfrac{k+d}{s+\|X\|^2}$ — the same conjugate-family
pattern as the coin-flipper example, now continuous. Since $\|X\|^2$ concentrates near its mean
$d(1+\tau^2)$ once $d$ is not small, this posterior mean settles near $1/(1+\tau^2) = \zeta$ regardless
of the fixed hyperparameters $(k,s)$ inherited from $\lambda_0$: the hyperprior's influence washes out
as the number of coordinates grows, exactly as in the coin-flipper case. (The source flags one piece of
bookkeeping: because $\zeta = 1/(1+\tau^2)$ must lie in $(0,1]$, the conjugate family may need
truncating to that range when $d$ is small.)

## What Bayes buys you, and what it costs

Whatever the source of $\Lambda$, once you have a posterior, *any* decision problem is answered the same
way: for any prior $\Lambda$, any model $\mathcal P$, any loss $L$, and any target $g(\theta)$,
$$
\delta_\Lambda(x) = \operatorname*{arg\,min}_d \int L(\theta,d)\,\lambda(\theta\mid x)\, d\theta.
$$
This needs none of the special structure frequentist theory usually relies on — no exponential family
or complete sufficient statistic, no requirement that the estimand be $U$-estimable, no convexity or
niceness of $L$. The posterior is a "one-stop shop": every question about $\theta$ reduces to an
integral against it, and the whole problem is pushed into (possibly hard) computation. That buys highly
expressive modeling and estimation — but the price is real: you are now limited by your ability to
actually carry out the computation (the subject of the following lecture).

### Source #4: convenience priors

The fourth source of a prior is pure computational convenience: pick a conjugate or otherwise tractable
prior specifically because it makes the posterior computable, especially in high dimensions. This
reopens the objection from source #2 in a sharper form — the prior was not chosen to represent anyone's
belief or any principled default, only to make the arithmetic close, so it is even less clear what the
resulting posterior means.

**A cautionary example.** Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} p$ for an unknown density $p$ on
$\mathbb R$, with estimand $m = \mathrm{median}(p)$. The natural estimator $\delta(X) = \mathrm{median}(X)$
is good — robust and fully nonparametric — and for large $n$,
$\delta(X) \approx N\!\left(m, (4np(m))^{-1}\right)$. It is not, however, the Bayes rule for any
realistic prior. Doing this properly the Bayesian way means:

1. put a prior on the space of all densities $p$ — infinite-dimensional;
2. compute the posterior — intractable unless a special, convenience prior is chosen;
3. return, say, $\mathbb E[m\mid X]$.

If that Bayes answer disagrees substantially with the plain sample median, there is a genuine question
of whether to trust it — the convenience prior baked into step 2 to make the computation tractable, not
evidence or considered belief, may be exactly what is driving the disagreement.

## Sources

- Fall 2024, `handwritten/lecture10-bayesinterp`, files 01–04 (`01-where-does-come-from.md`,
  `02-gaussian-sequence-model.md`, `03-flexibility-of-bayes.md`, `04-gaussian-hierarchical-model.md`):
  the interpretations of probability, the four sources of a prior, the flat/Jeffreys examples, the
  intersubjective-agreement example, the Gaussian sequence model, the coin-flipper hierarchical
  example, the flexibility-of-Bayes statement, the median example, and the Gaussian hierarchical model
  worked example — this run has the most complete equation formatting and is the basis for most of the
  chapter's mathematics.
- Fall 2025 and fall 2026, `handwritten/lecture10-bayesinterp`, files `01-outline.md` and
  `02-source-2-objective-or-vague-prior.md`: the same lecture given in two later years, confirming the
  same four-source structure and worked examples, and additionally framing the median example as "Why
  not always be Bayesian?" ahead of the four-sources discussion rather than after it; these runs do not
  include the Gaussian hierarchical model section that fall 2024 has.
- All eight source files are model reconstructions of a handwritten PDF with no text layer and are
  marked **unverified** at the equation level; where an equation looked internally inconsistent (the
  final asymptotic line for $\mathbb E[\zeta\mid\|X\|^2]$ in the Gaussian hierarchical model), this
  chapter presents the conjugate-family derivation that is unambiguous and states only the
  concentration behavior implied by the model's own stated moments, rather than repeating the
  questionable line verbatim.
- Referred to but not contained in the supplied material: a homework exercise (cited as "Hw 5" in the
  2025/2026 notes) asking for the local Kullback–Leibler approximation to the Jeffreys prior; and "the
  topic of next lecture," on the computational limits of Bayesian inference, which this chapter does
  not cover.

---

[← 39. Bayes Estimation for Frequentists](39-bayes-estimation-for-frequentists.md) · [Contents](index.md) · [41. Hierarchical Bayes Models →](41-hierarchical-bayes-models.md)
