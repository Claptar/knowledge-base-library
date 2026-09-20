---
title: "8. Statistical Models and Estimation"
course: "Berkeley Stat 210A Fall 2024"
chapter: 8
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Statistical Models and Estimation

## What this covers

This chapter answers two questions in sequence: what is a *statistical model* — the object that
turns a data set into a question with a definite (if uncertain) answer — and, once a model is
fixed, what does it mean to *estimate* a quantity within it well? It assumes familiarity with basic
probability: distributions, expectation and variance, the binomial and Bernoulli distributions, and
independent and i.i.d. sampling. It does not assume any prior exposure to estimation theory —
loss, risk, bias, admissibility and the Bayes/minimax split are all introduced from scratch.

## From probability to statistics

Probability and statistics ask opposite questions of the same mathematical objects. In probability,
the distribution of a random variable is given in full, and the exercise is deductive: given a
complete description of a random walk, for instance, how long does it take in expectation to cross
a threshold? The mathematics can be hard, but the question has an unambiguous answer.

Statistics runs the argument backwards. *Data* — from the Latin for "given" — is what we start
with, and the point is to work back to the distribution that generated it. This is an *inductive*
exercise, and its answers are inevitably more ambiguous than a probability calculation's.

The data set is denoted $X$, drawn from some unknown distribution $P$ on a *sample space*
$\mathcal{X}$. We do not know $P$ outright, but we are willing to assume it belongs to some family
of candidate distributions $\mathcal{P}$, called the **statistical model**. The working assumption
of the whole subject is that *some* $P \in \mathcal{P}$ is the truth — we just don't know which one.

## A worked example: three models for coin flipping

A large study had 48 participants flip coins a total of $n = 350{,}757$ times, recording $X =
178{,}079$ outcomes where the coin landed on the same side it started — about $50.8\%$. The same
data admit several statistical models, in increasing order of complexity.

**Model 1 (binomial).** Assume all $n$ flips are independent and land same-side up with a common
probability $\theta \in [0,1]$. Then

$$
X \sim \text{Binom}(n,\theta), \quad \mathcal{P} = \{\text{Binom}(n,\theta) : \theta \in [0,1]\},
$$

a family indexed by a single real parameter. Here $n$ is *known* — the same for every $P \in
\mathcal{P}$ — while $\theta$ is *unknown* in the sense that it is what varies across the family.
This known/unknown distinction is what makes $\theta$ "the parameter" and not $n$: it is not about
which quantity is more fundamental, but about which one indexes the family we're choosing among.
The model has pmf

$$
p_\theta(x) = \binom{n}{x}\theta^x (1-\theta)^{n-x}, \quad x = 0, 1, \ldots, n,
$$

with respect to counting measure on $\mathcal{X} = \{0,1,\ldots,n\}$.

**Model 2 (independent binomials).** A more general model keeps independence but lets each of the
48 flippers have their own same-side bias. Writing $n_i$ for the $i$th flipper's number of flips,
$\theta_i \in (0,1)$ for their bias, and $X_i$ for their same-side count,

$$
X_i \stackrel{\text{ind}}{\sim} \text{Binom}(n_i, \theta_i), \quad i = 1,\ldots,48.
$$

This model *contains* Model 1 as the special case where all $\theta_i$ coincide, but is indexed by
a $48$-dimensional parameter vector $\theta = (\theta_1,\ldots,\theta_{48}) \in (0,1)^{48}$ instead
of a single number. Multiparameter models are harder to work with than single-parameter ones
precisely because there is no longer an obviously right thing to do: data on flippers $1$ through
$47$ plausibly carries information about what values of $\theta_{48}$ are more or less likely, even
though the flippers are modeled as independent. Exploiting that kind of cross-parameter information
is a theme taken up later in the course.

**Model 3 (bias decaying over time).** A still more general model lets each flipper's bias drift as
they gain practice — the study in fact found that each flipper's same-side probability started
above $50\%$ and decayed toward it over the course of the experiment. Writing $\theta_{i,j}$ for the
probability that flipper $i$'s $j$th flip lands same-side up, and $X_{i,j} \in \{0,1\}$ for the
indicator that it did,

$$
X_{i,j} \stackrel{\text{ind}}{\sim} \text{Bernoulli}(\theta_{i,j}), \quad i=1,\ldots,48,\ \ j = 1,\ldots,n_i.
$$

This has one parameter *per flip*, which is too many: sending $\theta_{i,j} \to X_{i,j}$ for every
$i,j$ reproduces the data exactly, so the model is vacuous as stated. The fix is to impose a
constraint that rules out this pathology while still capturing the qualitative pattern observed —
for instance, that each flipper's bias is non-negative and monotonically decaying toward one half:

$$
\theta_{i,1} \geq \theta_{i,2} \geq \cdots \geq \theta_{i,n_i} \geq 0.5, \quad i = 1,\ldots,48.
$$

This is an example of a *shape constraint*, and the resulting model is essentially nonparametric.

A detail worth noticing: the sample space itself changed across the three models, even though the
experimenters recorded the same underlying sequence of flips in every case. That is not because the
data collected changed, but because the model determines how much of that data must be *retained*
to summarize it without losing information — a question the notion of *sufficiency*, covered later,
makes precise.

## Parametric and nonparametric models

A model is **parametric** if it can be indexed by finitely many real numbers: $\mathcal{P} =
\{P_\theta : \theta \in \Theta\}$ for some *parameter space* $\Theta \subseteq \mathbb{R}^d$, in
which case $\theta$ is the *parameter (vector)* and $d$ is the *model dimension*.

A model is **nonparametric** if there is no such finite-dimensional indexing. Despite the name,
essentially no nonparametric model is assumption-free — an i.i.d. assumption or a shape constraint
still narrows the family considerably, even without pinning it down to a finite list of numbers.
For example, an i.i.d. sample of size $n$ from a completely unspecified distribution $P$ on
$\mathbb{R}$,

$$
X_1,\ldots,X_n \stackrel{\text{i.i.d.}}{\sim} P, \quad \text{for some distribution } P \text{ on } \mathbb{R},
$$

is nonparametric — the family is $\mathcal{P} = \{P^n : P \text{ a distribution on } \mathbb{R}\}$,
where $P^n$ is the $n$-fold product measure — yet the independence assumption alone does real work.

There is no crisp line between the two cases in practice, and much of what follows applies to both.
It is often convenient to write $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ without committing
to what kind of object $\Theta$ is — nothing stops $\theta$ from being infinite-dimensional, such as
a whole density function. This loses no generality: one can always take $\theta = P$ and $\Theta =
\mathcal{P}$ itself.

## What is $\theta$? Three stances

Return to the simplest model, $X \sim \text{Binom}(n,\theta)$, and ask what $\theta$ actually is.
There are three standard ways to approach the question.

**The skeptic's answer.** A skeptic in Hume's mold will say we cannot know: any $X$ is logically
consistent with any $\theta \in (0,1)$. If $\theta = 0.1$, seeing $X = 178{,}079$ successes is
astronomically unlikely — but not impossible, and logic alone cannot rule it out.

**The Bayesian's answer.** A Bayesian resolves this by adding an assumption: that $\theta$ itself
has a distribution over $(0,1)$ before the data is seen (a *prior*), so that all that remains is
to compute the conditional distribution of $\theta$ given $X$ via Bayes' rule. The Bayesian still
won't tell you exactly what $\theta$ is, but can make exact probability statements — for instance,
about the (posterior) probability that $\theta \leq 0.1$. This turns inference into a calculation,
though the calculation can be hard if the prior is meant to reflect genuine subjective belief.
Different priors give different posteriors — a Bayesian convinced in advance that $\theta < 0.1$
can see this data and remain unimpressed — but in a case like this one, most "reasonable" priors
will land in roughly the same place after seeing so much data.

**The frequentist's answer.** A frequentist changes the subject entirely: rather than saying what
$\theta$ is, they propose a *method* for guessing it from $X$ — for instance, the estimator
$\delta_0(X) = X/n$ — and characterize how well that method performs. For $n = 350{,}757$, a
frequentist can say, without knowing $\theta$, that $\delta_0(X)$ is unbiased and has standard
deviation at most $1/(2\sqrt{n}) \approx 8.4\times 10^{-4}$, so it is very unlikely to miss $\theta$
by more than a percentage point. This works well right up until the data is realized: $\delta_0(X)
= 50.8\%$, and it is tempting to say $\theta$ is *probably* within a point of that number. Here the
frequentist demurs — the standard-deviation calculation was a statement about the randomness in the
data, made without assuming $\theta$ is random; once $X$ is observed there is no randomness left to
attach a probability to, so there is no license to say anything about *this* $\theta$. This is not
pedantry: a Bayesian could hold a prior that puts most of its mass below $10\%$, and nothing in the
frequentist's calculation would be contradicted, because the two are answering different questions.

For the rest of the chapter, we adopt the frequentist's stance: approach the problem before seeing
the data, and design a method that performs well with high probability, whatever $\theta$ turns out
to be. Most of the work is in *evaluating* and *comparing* candidate methods.

## The building blocks of estimation

Having observed $X \sim P_\theta$ in a model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$, the
goal of **estimation** is to guess some quantity of interest $g(\theta)$, called the **estimand**.
The guess itself, computed from the data, is the **estimate** $\delta(X)$; the rule $\delta(\cdot)$
used to compute it is the **estimator**.

**Example.** For $X \sim \text{Binom}(n,\theta)$ and estimand $g(\theta) = \theta$, the natural
estimator is $\delta_0(X) = X/n$, the sample proportion of heads. It is **unbiased**: $\mathbb{E}_\theta[\delta_0(X)] = g(\theta)$ for every $\theta$.

Since many estimators are available for any given problem, we need a way to grade them. A **loss
function** $L(\theta,d)$ measures how bad it is to guess $g(\theta) = d$ when the truth is $\theta$;
typically $L \geq 0$ with equality exactly at a perfect guess, though this isn't required. The
choice of loss should reflect the real cost of being wrong, but the default used almost everywhere
for its convenience is **squared-error loss**, $L(\theta,d) = (d - g(\theta))^2$.

Loss grades a single realization of the data. To grade an estimator overall, average the loss over
every data set it might see: the **risk function**

$$
R(\theta;\delta(\cdot)) = \mathbb{E}_\theta[L(\theta,\delta(X))] = \int L(\theta,\delta(x))\, dP_\theta(x).
$$

Two notational conventions are worth fixing early. The subscript $\theta$ on $\mathbb{E}_\theta$
says *which* candidate distribution the expectation integrates over — in this course, an
expectation or probability always integrates over the *entire* joint distribution of the data
unless something is explicitly conditioned on. And the semicolon in $R(\theta;\delta)$ signals that
the risk is being viewed primarily as a function of $\theta$, for a fixed choice of estimator
$\delta$.

The risk under squared-error loss is the **mean squared error**,

$$
\text{MSE}(\theta;\delta) = \mathbb{E}_\theta\big[(\delta(X) - g(\theta))^2\big].
$$

**Example, continued.** Since $\delta_0(X) = X/n$ is unbiased, its MSE is just its variance:

$$
\text{MSE}(\theta;\delta_0) = \text{Var}_\theta(X/n) = \frac{\theta(1-\theta)}{n}.
$$

## A family of shrinkage estimators, and their risk

$\delta_0$ can be noisy when $n$ is small — with $n=1$ it can only ever output $0$ or $1$, both
extreme conclusions from a single flip. One way to tame this is to pretend the data included $m$
extra "pseudo-flips," with $a$ pseudo-heads and $m-a$ pseudo-tails, which shrinks the estimate
toward $a/m$. Three instances of this idea, alongside a deliberately bad fourth one, are

$$
\delta_1(X) = \frac{X+1}{n+2}, \qquad \delta_2(X) = \frac{X+2}{n+4}, \qquad \delta_3(X) = \frac{X+1}{n}.
$$

$\delta_3$ adds a pseudo-head to the numerator without adding anything to the denominator, so it
is not of the shrinkage form at all — it is included as a foil.

<figure>
<svg viewBox="0 0 360 230" role="img" aria-label="Mean squared error curves for four binomial estimators, showing delta 3 dominated everywhere by delta 0, and delta 1, delta 2 crossing it">
  <polygon points="50,200 78,149.4 106,110 134,81.9 162,65 190,59.4 218,65 246,81.9 274,110 302,149.4 330,200 330,164.9 302,114.3 274,74.9 246,46.8 218,29.9 190,24.3 162,29.9 134,46.8 106,74.9 78,114.3 50,164.9" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="50" y1="200" x2="330" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="200" x2="50" y2="15" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="50,200 78,149.4 106,110 134,81.9 162,65 190,59.4 218,65 246,81.9 274,110 302,149.4 330,200" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="50,164.9 78,114.3 106,74.9 134,46.8 162,29.9 190,24.3 218,29.9 246,46.8 274,74.9 302,114.3 330,164.9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 3"/>
  <polyline points="50,172.2 78,142.2 106,118.9 134,102.2 162,92.2 190,88.9 218,92.2 246,102.2 274,118.9 302,142.2 330,172.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 3"/>
  <line x1="50" y1="110" x2="330" y2="110" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1 4"/>
  <text x="336" y="204" font-size="12" fill="currentColor">δ₀</text>
  <text x="336" y="182" font-size="12" fill="currentColor">δ₁</text>
  <text x="336" y="165" font-size="12" fill="currentColor">δ₃</text>
  <text x="336" y="114" font-size="12" fill="currentColor">δ₂</text>
  <text x="47" y="214" font-size="12" text-anchor="middle" fill="currentColor">0</text>
  <text x="190" y="214" font-size="12" text-anchor="middle" fill="currentColor">0.5</text>
  <text x="330" y="214" font-size="12" text-anchor="middle" fill="currentColor">1</text>
  <text x="190" y="227" font-size="12" text-anchor="middle" fill="currentColor">θ</text>
  <text x="12" y="20" font-size="12" fill="currentColor">MSE</text>
</svg>
<figcaption>Mean squared error against θ for n = 16, computed directly from the formulas above.
δ₃ lies strictly above δ₀ everywhere (shaded gap), so δ₀ dominates it. δ₁ and δ₂ cross δ₀: lower
risk near θ = 1/2, higher risk near the extremes. δ₂'s risk is exactly flat, at 0.01 for every θ.</figcaption>
</figure>

An MSE of $0.01$ sounds small, but for a parameter confined to $[0,1]$ it corresponds to a typical
error of about $0.1$ — worth keeping in mind when reading the vertical scale.

## Comparing estimators: admissibility

The picture shows a general phenomenon. $\delta_1$ and $\delta_2$ beat $\delta_0$ near $\theta =
1/2$ but lose to it near the extremes, so neither dominates the other. $\delta_3$, on the other
hand, is worse than $\delta_0$ *everywhere* — it added bias without buying back any variance. This
distinction is worth making formal.

An estimator $\delta$ is **inadmissible** if some other estimator $\delta^*$ satisfies

1. $R(\theta;\delta^*) \leq R(\theta;\delta)$ for every $\theta \in \Theta$, and
2. $R(\theta;\delta^*) < R(\theta;\delta)$ for some $\theta \in \Theta$.

In that case $\delta^*$ **dominates** $\delta$ (**strictly**, if both conditions hold). An estimator
that is not inadmissible is **admissible**. Here $\delta_0$ strictly dominates $\delta_3$, so
$\delta_3$ is inadmissible; there is never a reason to prefer it.

Comparing $\delta_0$, $\delta_1$, and $\delta_2$ is harder, because none dominates the others. This
is typical, not an artifact of this example: no estimator can have uniformly minimal risk over all
of $\Theta$, because the constant estimator $\delta(X) \equiv 1/2$ — which ignores the data
entirely — has exactly zero risk at $\theta = 1/2$, beating every other estimator there. Since we
cannot minimize risk pointwise for every $\theta$ at once, the ambiguity must be resolved some other
way. Two general strategies follow.

## Strategy 1: summarizing the risk by a single number

If the whole risk function can be reduced to one real number to be minimized, the ambiguity in
comparing estimators disappears. There are two standard ways to do this.

**Average-case risk (Bayes estimation).** Minimize a weighted average of the risk over $\Theta$,

$$
\operatorname*{minimize}_{\delta(\cdot)} \int_\Theta R(\theta;\delta)\, d\Lambda(\theta),
$$

for some measure $\Lambda$ of our choosing. If $\Lambda(\Theta) < \infty$ it can be normalized to a
probability measure without changing the minimizer, in which case this average is exactly the
estimator's expected risk under a prior $\Lambda$ on $\theta$ — the **Bayes risk** — and a minimizer
is a **Bayes estimator**. In the running example, $\delta_1(X) = (X+1)/(n+2)$ is Bayes for the
uniform (Lebesgue) prior on $[0,1]$, and $\delta_2(X) = (X+2)/(n+4)$ is Bayes for a
$\text{Beta}(2,2)$ prior. Minimizing average-case risk is a reasonable thing to do whether or not
one actually believes $\theta \sim \Lambda$ — Bayes estimators are useful tools for a frequentist
too, independent of any philosophical commitment about the nature of $\theta$. When $\Lambda(\Theta)
= \infty$, $\Lambda$ is an **improper prior**: the Bayes risk is no longer literally an expectation,
but working with improper priors is often convenient and can still produce good estimators.

**Worst-case risk (minimax estimation).** If averaging over $\Theta$ feels unmotivated, minimize
the worst case instead:

$$
\operatorname*{minimize}_{\delta(\cdot)} \sup_{\theta \in \Theta} R(\theta;\delta).
$$

This has a game-theoretic flavor: having committed to an estimator, nature adversarially picks the
least favorable $\theta$. Minimax estimators tend to have *flat* risk functions — pushing down the
worst case tends to equalize risk across $\Theta$ — and, as the figure shows, $\delta_2$ is exactly
the minimax estimator at $n=16$: its risk is constant. Minimax and Bayes estimation turn out to be
closely related, and the minimax estimator is often itself a Bayes estimator for some prior.

## Strategy 2: restricting the class of estimators

The second strategy is to require an estimator to satisfy some additional constraint, and then
compare only within that restricted class.

The natural constraint to start with is **unbiasedness**: $\mathbb{E}_\theta[\delta(X)] = g(\theta)$
for every $\theta \in \Theta$. This alone rules out estimators like $\delta(X) \equiv 1/2$ that
ignore the data. Among the four estimators considered here, only $\delta_0(X) = X/n$ is unbiased.

Once unbiasedness is imposed, there is often a clear winner: the **uniformly minimum variance
unbiased** (UMVU) estimator, which among all unbiased estimators has the smallest risk at *every*
$\theta$ simultaneously, for any convex loss function. In the binomial problem, $\delta_0$ is not
just the only unbiased estimator among the four considered — it is in fact the UMVU estimator for
this problem.

## Sources

- Berkeley STAT 210A course reader, "Statistical models and estimation." Both sections of this
  chapter follow the fall-2026 conversion, which carries the fullest treatment: `docs/statistics/berkeley/stat210a/fall-2026/reader/estimation/01-statistical-models.md`
  and `.../02-estimation-in-statistical-models.md` (converted from `reader/estimation.qmd`,
  CC BY 4.0). This is the version with the Bartos et al. coin-flipping study, the three nested
  models, and the skeptic/Bayesian/frequentist discussion of what $\theta$ "is."
- The same reader text, essentially unchanged, also appears at `docs/statistics/berkeley/stat210a/fall-2025/reader/estimation/01-statistical-models.md` and `.../02-estimation-in-statistical-models.md`,
  and again under `fall-2025/units/reader/estimation/`. These were checked against the fall-2026
  version and found to agree; nothing distinct was drawn from them for section 1.
- The earlier `docs/statistics/berkeley/stat210a/fall-2024/reader/estimation/01-statistical-models.md`
  (mirrored in `fall-2025/units/reader/estimation/01-statistical-models.md`) presents a plainer,
  single-model version of this material — one binomial example and a short "Bayesian assumption"
  paragraph, without the three-model study or the skeptic/frequentist framing. It was superseded
  by the fuller treatment above rather than merged in, per the instruction to take the clearest
  version of repeated material; none of its distinct wording was needed.
- The risk-function figure was redrawn as a static diagram from the `binom.mse` R function
  embedded in `02-estimation-in-statistical-models.md` (evaluated at $n=16$, the value fixed in
  that code block); the source's live R plot and interactive Observable widget (for varying $n$,
  $\alpha$, $\beta$) are not reproducible here and are not needed to make the argument.
- Two forward references the reader itself makes but does not resolve within this material: the
  topic of *sufficiency*, said to explain why the sample space changes across the three coin-flip
  models ("next week" in the source), and the claim that $\delta_2$ is Bayes for a
  $\text{Beta}(2,2)$ prior, which the source says will be shown later. Neither is covered here.
- No slides, transcript, or problem set were supplied for this chapter; no exercises are included
  for that reason.

---

[← 7. Gaussian sequence model](07-gaussian-sequence-model.md) · [Contents](index.md) · [9. Exponential Family Structure →](09-exponential-family-structure.md)
