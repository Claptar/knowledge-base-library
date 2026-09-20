---
title: "6. The Logic of Statistical Inference"
course: "GTPB Psls20"
chapter: 6
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. The Logic of Statistical Inference

## What this covers

This chapter follows one small drug trial through the entire arc of statistical inference:
designing the study, exploring the data it produced, estimating a population effect from a
sample, and testing whether that effect is real. It assumes familiarity with random variables,
expectation and variance, and the normal distribution, but not with sampling distributions,
confidence intervals or hypothesis tests — those are built up from scratch around a single
running example: whether the drug captopril lowers blood pressure in patients with hypertension.

## Design: population, sample, and the cycle between them

Every study starts by mapping a scientific question onto a *parameter* of a distribution. "Does
captopril lower blood pressure" is not itself a statistical statement; the statistical version is
"is the population mean $\mu = E(X)$ of some blood-pressure-related random variable $X$ different
from what it would be without treatment?" Design, exploration, estimation and testing are all
about that one number, $\mu$, which is never observed directly — only estimated from a sample.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="Cycle showing a study moving from population to sample by design, and back by estimation and inference">
  <defs>
    <marker id="arrow-cycle" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="70" y="15" width="220" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="38" text-anchor="middle" font-size="12" fill="currentColor">Population</text>
  <text x="180" y="55" text-anchor="middle" font-size="11" fill="currentColor">parameter &#956; (unknown)</text>

  <rect x="70" y="165" width="220" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="188" text-anchor="middle" font-size="12" fill="currentColor">Sample</text>
  <text x="180" y="205" text-anchor="middle" font-size="11" fill="currentColor">statistic mean, s.d. (observed)</text>

  <line x1="105" y1="70" x2="105" y2="165" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-cycle)"/>
  <text x="55" y="112" text-anchor="middle" font-size="11" fill="currentColor">random</text>
  <text x="55" y="125" text-anchor="middle" font-size="11" fill="currentColor">sampling</text>
  <text x="55" y="138" text-anchor="middle" font-size="11" fill="currentColor">(design)</text>

  <line x1="255" y1="165" x2="255" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-cycle)"/>
  <text x="317" y="106" text-anchor="middle" font-size="11" fill="currentColor">estimation</text>
  <text x="317" y="119" text-anchor="middle" font-size="11" fill="currentColor">&#38; inference</text>

  <text x="180" y="232" text-anchor="middle" font-size="11" fill="currentColor">data exploration &#38; descriptive statistics act only inside the sample box</text>
</svg>
<figcaption>Design governs the trip down, from population to sample; estimation and inference make
the trip back up. Exploring and describing the data never leaves the sample box — it comes before
any claim about the population.</figcaption>
</figure>

- **Design** decides how subjects get from the population into the sample. Representative,
  randomised sampling is what licenses generalising *back* from a sample statistic to the
  population parameter — nothing done later in the analysis can repair a biased sample.
- **Estimation and inference** is the return trip: using a sample statistic to say something,
  with a stated uncertainty, about $\mu$.
- **Data exploration and descriptive statistics** happens entirely inside the sample: describing
  what was actually measured, before any claim about the population is made.

### The running example: captopril and blood pressure

Fifteen patients with hypertension were drawn at random from the population of hypertensive
patients. Each patient's systolic and diastolic blood pressure was measured before and after
receiving captopril — a *pre-test/post-test design*.

- **Advantage**: because the same patient is measured twice, the design controls for
  between-patient variability directly — the effect of the drug can be assessed patient by
  patient rather than by comparing different people to each other.
- **Disadvantage**: there is no control group. Anything else that changes blood pressure between
  the two measurements — a placebo effect, regression toward the mean, simply resting — is
  confounded with the treatment effect. This limitation resurfaces at the end of the chapter,
  once the statistical result is in hand.

## Data exploration: turning paired measurements into one random variable

The instinct is to summarise the before/after measurements by their means and plot a bar chart
with error bars. This is a poor plot for two reasons: it hides the raw data entirely, and — more
importantly — it treats "before" and "after" as if they were two independent samples, when in
fact the same 15 people were measured both times.

A boxplot of the raw points side by side is more honest about the spread, but is still the wrong
picture for paired data: it throws away *which* before-point belongs with *which* after-point.
Plotting each patient's two points joined by a line makes the pairing visible, and shows a
consistent downward pull for almost every patient.

Because the data are paired, the natural object to analyse is not two blood pressures per patient
but their **difference**:
$$X = \Delta_{\text{after}-\text{before}} = \text{SBP}_\text{after} - \text{SBP}_\text{before}.$$
Taking the difference converts 15 dependent pairs of measurements into 15 values that can be
treated as independent draws from a single distribution — the distribution of "the effect of
captopril on this patient." A normal quantile-quantile plot of the 15 differences shows no serious
departure from normality, which licenses the model used for the rest of the chapter:
$$X \sim N(\mu, \sigma^2).$$

## Point estimation: the sample mean and how far it can be trusted

$\mu$ is the average blood-pressure change captopril produces *in the population*; it is estimated
from the sample by the sample mean
$$\bar X = \frac{X_1 + X_2 + \cdots + X_n}{n}.$$
$\bar X$ is itself a random variable — a different sample of 15 patients would give a different
$\bar X$. Two questions need answers before a single number from a single sample can be trusted:
is $\bar X$ *right on average* (unbiased), and how far can it typically stray from $\mu$ (its
precision)?

### Unbiasedness

If the sample is a genuine simple random sample — every subject drawn from the population with
the same probability, no systematic favouring of any subgroup — then $X_1,\dots,X_n$ all share the
population's mean and variance: $E(X_i)=\mu$, $\mathrm{Var}(X_i)=\sigma^2$ for every $i$. Linearity
of expectation then gives
$$E(\bar X) = \frac{E(X_1)+\cdots+E(X_n)}{n} = \frac{n\mu}{n} = \mu,$$
so $\bar X$ is an **unbiased estimator** of $\mu$: averaged over repeated samples, it hits the
right value. This is exactly why representative, randomised sampling matters — bias in *how the
sample was drawn* shows up as bias in $\bar X$, and no amount of clever estimation afterwards can
undo it.

### Standard error

Being unbiased says nothing about how far a *single* $\bar X$ can be from $\mu$. Under the
additional assumption that the observations are drawn **independently**,
$$\mathrm{Var}(\bar X) = \mathrm{Var}\left(\frac{X_1+\cdots+X_n}{n}\right)
= \frac{\mathrm{Var}(X_1)+\cdots+\mathrm{Var}(X_n)}{n^2} = \frac{\sigma^2}{n},$$
using $\mathrm{Var}(X_i+X_j) = \mathrm{Var}(X_i)+\mathrm{Var}(X_j)+2\,\mathrm{Cov}(X_i,X_j)$ and
$\mathrm{Cov}(X_i,X_j)=0$ for independent $X_i,X_j$. So the standard deviation of $\bar X$ is
$$\sigma_{\bar X} = \frac{\sigma}{\sqrt n},$$
called the **standard error** (SE) of the mean — a factor of $\sqrt n$ smaller than the standard
deviation of a single observation, and shrinking as $n$ grows. This is exactly the independence
that pairing bought earlier: the raw before/after measurements on the same patient are dependent,
but the 15 *differences* are independent across patients, which is what lets this formula apply to
the captopril study at all.

In practice $\sigma$ is unknown and is itself estimated by the sample standard deviation $S$,
giving $SE = S/\sqrt n$. For captopril, if the population standard deviation of the blood-pressure
differences were $\sigma = 9.0$ mmHg, the standard error on the mean of $n=15$ differences would be
$$SE = \frac{9.0}{\sqrt{15}} \approx 2.32 \text{ mmHg.}$$

A repeated-sampling simulation (drawing many samples from a large reference population's
cholesterol measurements) makes the distinction between the two kinds of spread concrete: the
*sample standard deviation* stays centred on the same value — the population's — regardless of
sample size, because it estimates a fixed population quantity; the *standard error of the mean*
shrinks as sample size grows, because it measures how precisely that fixed quantity can be pinned
down. For normally distributed data, the sample mean is also the unbiased estimator with the
smallest standard error — smaller than the sample median's, for instance — which is part of why it
is the default choice of estimator.

### Distribution of the sample mean, and the Central Limit Theorem

Knowing $\bar X$'s mean and standard error is not yet enough to build an interval around it; its
*shape* is needed too. If the individual observations are normally distributed, the sample mean is
exactly normal as well:
$$X_i \sim N(\mu,\sigma^2) \implies \bar X \sim N\!\left(\mu, \frac{\sigma^2}{n}\right).$$
When the individual observations are *not* normal — cholesterol levels in a reference population
are visibly right-skewed — the sample mean is still only approximately normal, and how large $n$
needs to be for that approximation to be good depends on how skewed the underlying distribution is.
This is the **Central Limit Theorem**: for i.i.d. observations $X_1,\dots,X_n$ from *any*
distribution with finite variance, the sample mean becomes approximately normal as $n$ grows,
irrespective of the shape of the individual observations. It is why a normal-based analysis of
$\bar X$ is defensible even when the raw data plainly are not normal, provided the sample is large
enough.

## Interval estimators: confidence intervals

A single number like $\bar x \approx -18.9$ mmHg invites over-interpretation unless it comes with a
statement of how much it could plausibly differ from $\mu$. A **confidence interval** is built to
contain $\mu$ with a stated probability across repeated samples.

### Known variance

If $\sigma$ is known, $\bar X \sim N(\mu,\sigma^2/n)$ gives a reference range for $\bar X$ around
$\mu$:
$$\left[\mu - 1.96\frac{\sigma}{\sqrt n},\ \mu + 1.96\frac{\sigma}{\sqrt n}\right]$$
holds $\bar X$ with probability 95%. This cannot be *used* as it stands, because $\mu$ is unknown —
but the inequality inside it can be turned around: the statement "$\bar X$ is within
$1.96\,\sigma/\sqrt n$ of $\mu$" is exactly the statement "$\mu$ is within $1.96\,\sigma/\sqrt n$ of
$\bar X$." That gives the usable, mirror-image interval
$$\left[\bar X - 1.96\frac{\sigma}{\sqrt n},\ \bar X + 1.96\frac{\sigma}{\sqrt n}\right],$$
reported as the **95% confidence interval** for $\mu$.

The 95% is a property of the *procedure*, not of any one realised interval: the endpoints
$\bar X \pm 1.96\,\sigma/\sqrt n$ are themselves random, varying from sample to sample, so the
interval is a *stochastic interval*. Over many repeated samples, 95% of the intervals produced this
way contain the true $\mu$ and 5% do not — but for any one interval already computed, $\mu$ either
is or is not inside it, and there is no way to tell which from the data alone. "95% confidence"
describes the long-run behaviour of the method, not a probability statement about a fixed interval.

### Unknown variance and the t-distribution

$\sigma$ is essentially never known in practice; it is replaced by the sample standard deviation
$S$. When $n$ is large, $S$ is close enough to $\sigma$ that the same interval (with $S$ in place
of $\sigma$) still works well. For small $n$, estimating $S$ from the same data adds extra
uncertainty that the normal-based interval does not account for, and the naive interval turns out
too narrow — a repeated-sampling check confirms this directly: the coverage of the $z$-based
interval falls noticeably short of 95% at $n=10$, but is fine at $n=50$ and $n=100$.

The fix is to track the extra variability introduced by estimating $S$. The standardised quantity
$(\bar X-\mu)/(S/\sqrt n)$ is no longer exactly standard normal; it follows a **Student
$t$-distribution with $n-1$ degrees of freedom** — symmetric like the normal, but with heavier
tails, the excess thickness set by $n$. As $n\to\infty$, $S\to\sigma$ and the $t$-distribution
converges to $N(0,1)$. The correct confidence interval for the mean of a normal population with
unknown variance is therefore
$$\left[\bar X - t_{n-1,\alpha/2}\frac{S}{\sqrt n},\ \bar X + t_{n-1,\alpha/2}\frac{S}{\sqrt n}\right],$$
the normal quantile $z_{\alpha/2}=1.96$ replaced by the larger $t$-quantile $t_{n-1,\alpha/2}$ (for
14 degrees of freedom the 97.5% quantile is about 2.14, versus 1.96 for the normal — the price paid
for not knowing $\sigma$). Redoing the repeated-sampling coverage check with the $t$-quantile
instead of $z=1.96$ restores the coverage to the nominal 95% at every sample size, including
$n=10$.

For the captopril differences, with $\bar x \approx -18.9$ mmHg and $n=15$ (14 degrees of freedom),
this gives a 95% confidence interval whose upper limit is about $-14.8$ mmHg — one-sided, because
the question of interest is only whether blood pressure *drops* (see below). Reporting the interval
alongside the point estimate is standard practice: a point estimate alone invites the misleading
impression of exactness, whereas the interval shows how precisely the effect has actually been
pinned down, and is what allows a reader to weigh statistical significance against whether the
effect is large enough to matter biologically or clinically.

## Hypothesis tests: is the effect real, or noise?

A negative sample mean is not by itself evidence that captopril lowers blood pressure at the
population level — a genuinely ineffective drug could easily produce a negative $\bar x$ in one
particular sample of 15 patients just by chance. The question is: how large would $\bar x$ have to
be before "chance" stops being a credible explanation?

### Null and alternative hypotheses

Karl Popper's **falsification principle** says data can never *prove* a hypothesis, only fail to
refute it. Hypothesis testing is built around this asymmetry: state a **null hypothesis** $H_0$
(the "nothing interesting is happening" case — captopril has no effect, $\mu=0$) and an
**alternative hypothesis** $H_1$ (what the researchers actually want to show — $\mu<0$, a genuine
drop). The strategy is not to prove $H_1$ directly but to try to falsify $H_0$: if the observed
data would be extremely unlikely under $H_0$, that counts as evidence against it.

### Building the test by permutation

Under $H_0$, the "before" and "after" measurement on a given patient are two interchangeable
baseline readings — there is no reason, if the drug does nothing, that one should systematically
be lower than the other. That means the labels can be shuffled: for each patient, independently
flip a coin and decide whether to swap "before" and "after". Repeating this shuffle thousands of
times and recomputing the mean difference each time builds up, from the data itself, the
distribution of what $\bar X$ *would* look like if $H_0$ were true. Doing this 10,000 times for the
captopril data, **not one** of the 10,000 shuffled means was as extreme as the mean actually
observed — meaning the probability of seeing a drop this large under $H_0$ is well below
$1/10{,}000$. That is strong evidence against $H_0$.

### The pivot statistic and the p-value

Rather than reporting the raw mean difference, it is standardised against its own standard error —
this balances the *size* of the effect against the *noise* in the estimate, and is what makes the
statistic comparable across different studies and sample sizes:
$$T = \frac{\bar X - \mu_0}{SE_{\bar X}}, \qquad \mu_0 = 0 \text{ under } H_0.$$
For the captopril data, $T = (-18.93-0)/2.33 \approx -8.12$. Repeating the permutation argument on
$T$ instead of the raw mean gives, once again, a null distribution with essentially no mass
anywhere near $-8.12$ — and that permutation null distribution turns out to trace out exactly the
$t$-distribution with 14 degrees of freedom introduced above. That coincidence is why this whole
procedure is called a **t-test**: the same $t$-distribution that describes the extra uncertainty of
estimating $\sigma$ from a small sample also describes, under $H_0$, how the standardised mean
behaves — so the test statistic can be evaluated directly from the $t$-distribution, without
running 10,000 permutations by hand.

The **p-value** is the probability, computed under $H_0$, of a test statistic at least as extreme
(in the direction of $H_1$) as the one actually observed:
$$p = P_0[T \le t] = F_t(t;\,n-1)$$
for a one-sided test with $H_1:\mu<0$. For captopril, $p = F_t(-8.12;14) \approx 0.6\times10^{-6}$:
essentially no chance of seeing a drop this large if the drug did nothing. The p-value measures the
strength of evidence against $H_0$ — it is emphatically **not** the probability that $H_0$ is true.

### Deciding: significance level and the rejection region

A p-value is compared to a pre-chosen threshold, the **significance level** $\alpha$ —
conventionally $0.05$ — and the test is *significant* if $p<\alpha$. Rough conventional bands for
how the evidence is usually described:

| p-value | verdict |
|---|---|
| $>0.10$ | not significant — no evidence against $H_0$ |
| $0.05$–$0.10$ | marginal, weak evidence |
| $0.01$–$0.05$ | significant |
| $0.001$–$0.01$ | strongly significant |
| $<0.001$ | extremely significant |

Equivalently, $\alpha$ carves the distribution of $T$ under $H_0$ into a rejection region (in the
tail, beyond a **critical value** $t_\text{crit}$) and an acceptance region. Observing $T$ in the
rejection region and rejecting $H_0$ are the same decision stated two ways — once as a probability,
once as where the statistic landed.

<figure>
<svg viewBox="0 0 330 210" role="img" aria-label="Density of the test statistic under the null hypothesis, with the rejection region shaded in the left tail">
  <line x1="20" y1="170" x2="312" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="316" y="174" font-size="11" fill="currentColor">t</text>

  <path d="M 30.0,170.0 L 32.2,169.9 L 34.5,169.9 L 36.8,169.9 L 39.0,169.9 L 41.2,169.8 L 43.5,169.8 L 45.8,169.7 L 48.0,169.7 L 50.2,169.6 L 52.5,169.5 L 54.8,169.4 L 57.0,169.2 L 59.2,169.0 L 61.5,168.8 L 63.8,168.6 L 66.0,168.2 L 68.2,167.9 L 70.5,167.4 L 72.8,166.9 L 75.0,166.3 L 77.2,165.6 L 79.5,164.7 L 81.8,163.8 L 84.0,162.7 L 86.2,161.5 L 88.5,160.0 L 90.8,158.4 L 93.0,156.6 L 95.2,154.6 L 97.5,152.4 L 99.8,149.9 L 102.0,147.2 L 104.2,144.3 L 106.5,141.1 L 108.8,137.6 L 111.0,133.9 L 113.2,129.9 L 115.5,125.7 L 117.8,121.2 L 120.0,116.6 L 122.2,111.7 L 124.5,106.7 L 126.8,101.6 L 129.0,96.4 L 131.2,91.2 L 133.5,85.9 L 135.8,80.7 L 138.0,75.6 L 140.2,70.7 L 142.5,65.9 L 144.8,61.4 L 147.0,57.2 L 149.2,53.4 L 151.5,50.0 L 153.8,47.0 L 156.0,44.5 L 158.2,42.6 L 160.5,41.2 L 162.8,40.3 L 165.0,40.0 L 167.2,40.3 L 169.5,41.2 L 171.8,42.6 L 174.0,44.5 L 176.2,47.0 L 178.5,50.0 L 180.8,53.4 L 183.0,57.2 L 185.2,61.4 L 187.5,65.9 L 189.8,70.7 L 192.0,75.6 L 194.2,80.7 L 196.5,85.9 L 198.8,91.2 L 201.0,96.4 L 203.2,101.6 L 205.5,106.7 L 207.8,111.7 L 210.0,116.6 L 212.2,121.2 L 214.5,125.7 L 216.8,129.9 L 219.0,133.9 L 221.2,137.6 L 223.5,141.1 L 225.8,144.3 L 228.0,147.2 L 230.2,149.9 L 232.5,152.4 L 234.8,154.6 L 237.0,156.6 L 239.2,158.4 L 241.5,160.0 L 243.8,161.5 L 246.0,162.7 L 248.2,163.8 L 250.5,164.7 L 252.8,165.6 L 255.0,166.3 L 257.2,166.9 L 259.5,167.4 L 261.8,167.9 L 264.0,168.2 L 266.2,168.6 L 268.5,168.8 L 270.8,169.0 L 273.0,169.2 L 275.2,169.4 L 277.5,169.5 L 279.8,169.6 L 282.0,169.7 L 284.2,169.7 L 286.5,169.8 L 288.8,169.8 L 291.0,169.9 L 293.2,169.9 L 295.5,169.9 L 297.8,169.9 L 300.0,170.0"
        fill="none" stroke="currentColor" stroke-width="1.5"/>

  <path d="M 30.0,170.0 L 32.2,169.9 L 34.5,169.9 L 36.8,169.9 L 39.0,169.9 L 41.2,169.8 L 43.5,169.8 L 45.8,169.7 L 48.0,169.7 L 50.2,169.6 L 52.5,169.5 L 54.8,169.4 L 57.0,169.2 L 59.2,169.0 L 61.5,168.8 L 63.8,168.6 L 66.0,168.2 L 68.2,167.9 L 70.5,167.4 L 72.8,166.9 L 75.0,166.3 L 77.2,165.6 L 79.5,164.7 L 81.8,163.8 L 84.0,162.7 L 86.2,161.5 L 88.5,160.0 L 90.8,158.4 L 93.0,156.6 L 95.2,154.6 L 97.5,152.4 L 99.8,149.9 L 102.0,147.2 L 104.2,144.3 L 104.2,170 L 30,170 Z"
        fill="currentColor" fill-opacity="0.15" stroke="none"/>

  <line x1="104.2" y1="144.3" x2="104.2" y2="185" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="104.2" y="198" text-anchor="middle" font-size="11" fill="currentColor">t_crit &#8776; -1.76</text>
  <text x="165.0" y="185" text-anchor="middle" font-size="11" fill="currentColor">0</text>

  <text x="62" y="150" text-anchor="middle" font-size="11" fill="currentColor">rejection</text>
  <text x="62" y="163" text-anchor="middle" font-size="11" fill="currentColor">region (&#945;=0.05)</text>
  <text x="205" y="150" text-anchor="middle" font-size="12" fill="currentColor">acceptance region</text>

  <text x="60" y="45" text-anchor="middle" font-size="11" fill="currentColor">observed t &#8776; -8.12</text>
  <text x="60" y="58" text-anchor="middle" font-size="11" fill="currentColor">(far outside this range)</text>
  <line x1="90" y1="65" x2="45" y2="65" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-cycle)"/>
</svg>
<figcaption>The t-distribution under the null hypothesis. The observed captopril statistic
(&#8776;-8.12) is so far into the tail that not one of 10,000 permuted samples matched it — far
past even the critical value that would already have triggered rejection at &#945;=0.05.</figcaption>
</figure>

### Two kinds of error

Any single-sample decision to reject or not reject $H_0$ can be wrong in one of two ways:

| decision | $H_0$ true | $H_0$ false |
|---|---|---|
| accept $H_0$ | correct | Type II error ($\beta$) |
| reject $H_0$ | Type I error ($\alpha$) | correct |

A **Type I error** is a false positive: concluding there is an effect when there is not. It is
*controlled by construction* — the test is built so that $P[\text{reject } H_0 \mid H_0] = \alpha$
exactly, whatever $\alpha$ was chosen to be. A **Type II error** is a false negative: failing to
detect a real effect. Its probability $\beta$ is *not* controlled by the test's construction at all
— it depends on how large the true effect is, how much noise there is, and how big the sample is.
$1-\beta$, the probability of correctly detecting a real effect of a given size, is the test's
**power**.

A simulation makes the trade-off concrete: for a smaller, more realistic effect than captopril's
dramatic one — a population mean drop of only 2 mmHg, with $\sigma=9$ — a sample of 15 patients has
low power to detect it; increasing the sample size to 30 improves the power but it remains low.
Detecting a small effect reliably needs either a much larger sample or a much larger effect — and a
2 mmHg drop, even if detected, may not be large enough to be clinically relevant to begin with,
exactly the distinction a confidence interval preserves and a bare significance verdict does not.

This asymmetry between the two error types is why "reject $H_0$" and "do not reject $H_0$" are not
mirror-image conclusions. Rejecting $H_0$ is a **strong conclusion**: the Type I error rate is
known and small, so $H_1$ is probably correct. Not rejecting $H_0$ is only a **weak conclusion**: it
means the data did not contain enough evidence against $H_0$, not that $H_0$ has been shown to be
true — $\beta$ could easily be large, especially in an underpowered study.

### One-sided or two-sided?

The captopril test used $H_1:\mu<0$ — a **one-sided** test, justified because the study only cared
about detecting a *drop*. Had the study instead been an early safety check on healthy subjects,
where a rise in blood pressure would be just as important to detect as a drop, the natural
alternative would be **two-sided**: $H_1:\mu\ne0$, splitting the significance level across both
tails and roughly doubling the p-value for the same observed statistic.

The direction of the test has to be committed to *before* the data are seen, as part of the design
— not chosen afterwards to match whichever direction the data happened to point. A simulation of
the alternative practice makes the failure concrete: simulate many samples under a *true* null
($\mu=0$), and for each sample pick the one-sided test whose direction matches the sign of that
particular sample's mean. The correctly-run two-sided test rejects a true $H_0$ close to the
nominal $\alpha=0.05$ of the time, as it should; the direction-chosen-after-the-fact procedure
rejects a true $H_0$ roughly twice as often — its actual Type I error rate is silently inflated to
about $2\alpha$, because it is effectively given two chances (either tail) to call a result
significant. For this reason a two-sided test is the safer default whenever there was not a
genuine, pre-registered reason to look in only one direction.

### Back to captopril

Putting the pieces together: the captopril data support an **extremely significant** one-sample
(equivalently, paired) t-test, one-sided because the pre-specified question was about a drop.
Systolic blood pressure fell on average by 18.9 mmHg (95% CI: at most $-14.8$ mmHg). But the design
flaw noted at the start now matters: a pre-test/post-test design with no control group cannot
separate a true drug effect from a placebo effect, or any other reason blood pressure might have
fallen between the two measurements regardless of the drug. The statistical result is unambiguous;
what it can be attributed to is not — a reminder that no amount of care in estimation and testing
can repair a design that never included a comparison group.

## Sources

- **Experimental design and the population/sample cycle** — `01-experimental-design.md`: the
  population/sample framing, the captopril pre-test/post-test design and its advantage and
  disadvantage.
- **Data exploration** — `02-data-exploration-and-descriptive-statistics.md`: the failed bar-chart
  and boxplot attempts, the paired line plot, taking the within-patient difference, and the
  normal QQ-plot check.
- **Point and interval estimation** — `03-estimation.md`: unbiasedness and standard-error proofs
  for the sample mean, the NHANES repeated-sampling simulations (mean vs. median, standard
  deviation vs. standard error, sample size 10/50/100), the Central Limit Theorem, the known- and
  unknown-variance confidence intervals, the $t$-distribution, and the coverage simulations.
- **Hypothesis testing** — `04-hypothesis-tests.md`: the permutation-test construction, the pivot
  statistic and $p$-value, the significance-level table, the Type I/II error table and power
  simulation, and the one-sided-vs-two-sided argument and its simulation.

All four files are converted, lossless splits of a single source lecture, **GTPB PSLS20**,
`theory/05-statisticalInference.Rmd` (licensed CC BY 4.0); no separate slide deck or transcript was
supplied for this lecture, only this already-prose set of notes. Three "Points of Significance"
Nature Methods columns and one further Nature Methods article were embedded in the original
lecture as linked PDFs (on the distribution of the mean, on confidence-interval interpretation, on
statistical power, and on hypothesis testing generally); the lecture pointed to them but their
content is not reproduced here, only referenced where the surrounding notes describe what point
each one was illustrating. Numeric results that depended on live computation in the original R
code (for example the exact simulated power for detecting a 2 mmHg effect) are described
qualitatively rather than with an invented number, since the source document did not carry an
evaluated value.

---

[← 5. Data Exploration Case Studies](05-data-exploration-case-studies.md) · [Contents](index.md) · [7. The Two-Sample T-Test →](07-the-two-sample-t-test.md)
