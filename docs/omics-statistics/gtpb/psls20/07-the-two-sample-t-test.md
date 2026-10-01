---
title: "7. The Two-Sample T-Test"
course: "GTPB Psls20"
chapter: 7
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. The Two-Sample T-Test

## What this covers

How to test whether two independent groups have the same mean, using a worked microbiome
experiment throughout. It assumes the reader already has the machinery of hypothesis testing from
a single sample — null and alternative hypotheses, test statistics, p-values, confidence intervals,
and the one-sample and paired t-tests — and asks what changes when the two numbers being compared
come from two *different* sets of subjects rather than one set measured twice.

## The armpit experiment

Smelly armpits are not caused by sweat itself but by the group of bacteria *Corynebacterium spp.*,
which metabolise sweat into odorous compounds. A second, abundant group, *Staphylococcus spp.*,
does not. A research group proposed a therapy: strip the armpit microbiome with antibiotics, then
reseed it with a microbial transplant.

Twenty subjects with smelly armpits were split into two treatment groups:

- **placebo** — antibiotics only,
- **transplant** — antibiotics followed by a microbial transplant,

and six weeks later the microbiome was sampled and the relative abundance of *Staphylococcus spp.*
against the combined *Staphylococcus* + *Corynebacterium* pool was measured by gel electrophoresis
(DGGE). The question the whole chapter answers is whether the transplant shifted this relative
abundance compared with placebo — and the two groups are two disjoint sets of subjects, not the
same subjects before and after, so this is not a job for the paired t-test.

Data exploration compares the two groups directly: a boxplot of relative abundance against
treatment group, with the individual points jittered on top, and a normal QQ-plot of the
abundances faceted by group, to get an early look at whether each group's data look plausibly
Gaussian and whether the spread looks similar in the two groups. Both questions turn out to matter
for which test is valid, below.

## Setting up the comparison

Write $Y_{ij}$ for the response of subject $i = 1, \ldots, n_j$ in population (here: treatment
group) $j = 1, 2$ — treatment $j=1$ is the microbial transplant, $j=2$ is the placebo. The model is

$$Y_{ij} \text{ i.i.d. } N(\mu_j, \sigma^2), \quad i = 1,\ldots,n_j,\; j = 1,2.$$

Note the single $\sigma^2$: this model assumes the two groups share one variance, called
**homoscedasticity**. (Unequal variances are **heteroscedasticity**, treated separately below.)

The hypotheses are stated on the two means, or equivalently on their difference — the **effect
size** $\mu_1 - \mu_2$:

$$H_0: \mu_1 = \mu_2 \qquad\text{vs.}\qquad H_1: \mu_1 \neq \mu_2,$$
$$H_0: \mu_1 - \mu_2 = 0 \qquad\text{vs.}\qquad H_1: \mu_1 - \mu_2 \neq 0.$$

$H_1$ is the research hypothesis: that the average relative abundance of *Staphylococcus spp.*
differs between transplant and placebo. The effect size is estimated by the difference of sample
means,

$$\hat\mu_1 - \hat\mu_2 = \bar Y_1 - \bar Y_2.$$

## The variance of the difference, and the pooled estimator

The two groups consist of different subjects, so the sample means $\bar Y_1$ and $\bar Y_2$ are
independent, and variances of independent quantities add:

$$\operatorname{Var}(\bar Y_1 - \bar Y_2) = \frac{\sigma^2}{n_1} + \frac{\sigma^2}{n_2}
 = \sigma^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right),$$

so the standard error of the difference is

$$\sigma_{\bar Y_1 - \bar Y_2} = \sigma\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}.$$

$\sigma^2$ itself is unknown, and each group supplies its own estimate of it, the usual sample
variance

$$S_1^2 = \frac{1}{n_1 - 1}\sum_{i=1}^{n_1} (Y_{i1} - \bar Y_1)^2, \qquad
  S_2^2 = \frac{1}{n_2 - 1}\sum_{i=1}^{n_2} (Y_{i2} - \bar Y_2)^2.$$

Because the model assumes $\sigma_1^2 = \sigma_2^2 = \sigma^2$, $S_1^2$ and $S_2^2$ are two separate
estimators of the *same* parameter, and it is wasteful to use only one of them. Combining every
observation from both groups gives a single, more precise estimator, the **pooled variance**:

$$S_p^2 = \frac{n_1 - 1}{n_1 + n_2 - 2} S_1^2 + \frac{n_2 - 1}{n_1 + n_2 - 2} S_2^2
 = \frac{1}{n_1 + n_2 - 2} \sum_{j=1}^{2} \sum_{i=1}^{n_j} (Y_{ij} - \bar Y_{j})^2.$$

$S_p^2$ is a weighted average of the two group variances, weighted by each group's degrees of
freedom, and it uses the squared deviations of every observation from its own group mean. Pooling
both groups' data costs two degrees of freedom overall — one per group mean estimated — leaving
$n_1 + n_2 - 2$ degrees of freedom for $S_p^2$, against $n_j - 1$ for a single group's $S_j^2$.

## The two-sample t-statistic

Plugging the pooled variance into the standard error of $\bar Y_1 - \bar Y_2$ gives the two-sample
t-test statistic:

$$T = \frac{\bar Y_1 - \bar Y_2}{\sqrt{\dfrac{S_p^2}{n_1} + \dfrac{S_p^2}{n_2}}}
   = \frac{\bar Y_1 - \bar Y_2}{S_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}.$$

Under $H_0$, provided the data in both groups are independent, normally distributed, and share a
common variance, $T$ follows a $t$-distribution with $n_1 + n_2 - 2$ degrees of freedom — the
degrees of freedom of the pooled variance estimator that sits in its denominator.

**Armpit example.** Running the test (`t.test(rel~trt, data=ap, var.equal=TRUE)` in R) rejects
$H_0$ at the $5\%$ level. If the transplant truly had no effect, the chance of seeing a test
statistic at least as extreme as the one observed is under $9$ in $100{,}000$ — extremely rare
under $H_0$, and exactly the kind of outcome $H_1$ predicts: a large test statistic and a small
p-value. The conclusion is that the relative abundance of *Staphylococcus spp.* is extremely
significantly larger, on average, in the transplant group than in the placebo group ($p \ll 0.001$).

**Good statistical practice** is to report not just the p-value but the effect size together with
its confidence interval, so that a reader can separately judge *statistical* significance and
*biological* (or scientific) relevance — a theme returned to below.

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="Two overlapping normal curves for the placebo and transplant groups, shifted apart by the effect size mu1 minus mu2">
  <line x1="20" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 40 170 C 70 170, 90 40, 120 40 C 150 40, 170 170, 200 170" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 40 170 C 70 170, 90 40, 120 40 C 150 40, 170 170, 200 170" fill="currentColor" fill-opacity="0.1" stroke="none"/>
  <path d="M 130 170 C 160 170, 180 40, 210 40 C 240 40, 260 170, 290 170" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="120" y="188" text-anchor="middle" font-size="12" fill="currentColor">mu_2 (placebo)</text>
  <text x="210" y="188" text-anchor="middle" font-size="12" fill="currentColor">mu_1 (transplant)</text>
  <line x1="120" y1="40" x2="120" y2="25" stroke="currentColor" stroke-width="1"/>
  <line x1="210" y1="40" x2="210" y2="25" stroke="currentColor" stroke-width="1"/>
  <line x1="120" y1="25" x2="210" y2="25" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" marker-start="url(#arrow)"/>
  <text x="165" y="18" text-anchor="middle" font-size="12" fill="currentColor">mu_1 - mu_2</text>
  <defs>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <polygon points="0,0 6,3 0,6" fill="currentColor"/>
    </marker>
  </defs>
</svg>
<figcaption>The two-sample t-test asks whether the gap between the two group means is larger than
sampling variation, from two independent samples, would explain.</figcaption>
</figure>

## Assumptions, and what to do when they fail

The validity of the two-sample t-test rests on the same kind of distributional assumptions as the
one-sample and paired versions, now doubled up:

- **independence** — a matter of experimental design, not something checked in the data;
- **normality of the observations in *both* groups**;
- **equal variances** across the two groups.

If these do not hold, the null distribution of $T$ is not really a $t$-distribution, so the
p-values and critical values computed from it — and the coverage of any confidence interval built
from the same quantiles — are wrong.

### Checking normality

- **Boxplots and histograms** show the shape of each group's distribution and flag outliers;
  **QQ-plots** (as used in the armpit exploration above) compare the sample quantiles against
  those of a normal distribution.
- Formal goodness-of-fit tests exist (Kolmogorov–Smirnov, Shapiro–Wilk, Anderson–Darling), but their
  null hypothesis is *that the data are normal* — so failing to reject is a weak conclusion, not
  evidence of normality. They also behave badly at the extremes: low power in small samples, and in
  large samples they flag deviations too small to matter.
- **Recommendation**: start with graphical exploration, bearing the sample size in mind so as not
  to over-interpret noise in a small plot. If in doubt, simulate data of the same sample size from
  a normal distribution with the observed mean and variance, and compare by eye. If normality
  looks doubtful, check the literature for how sensitive the intended method is to that kind of
  deviation — the t-test, for instance, is fairly insensitive to non-normality as long as the
  distribution stays symmetric. In large samples the central limit theorem covers for
  non-normality of the raw data. Transforming the response is another option.

### Checking homoscedasticity

- On a boxplot, the box height (the interquartile range) is a robust stand-in for the variance in
  each group; if the two boxes are not very different in size, homoscedasticity is plausible.
- Simulation, as above, can again build intuition for how much difference in spread is expected
  under equal variances.
- A formal F-test for comparing variances exists, but its null hypothesis is again *equal
  variances*, so the same criticism that applies to normality tests applies here too.

### The Welch modified t-test

If the variances genuinely differ, the fix is to drop the pooled estimator and use each group's
own sample variance directly:

$$T = \frac{\bar Y_1 - \bar Y_2}{\sqrt{\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}}}.$$

This is the **Welch two-sample t-test**. Its statistic follows only *approximately* a
t-distribution, with degrees of freedom somewhere between $\min(n_1 - 1, n_2 - 1)$ and
$n_1 + n_2 - 2$; R estimates the exact value by the Welch–Satterthwaite approximation, used
automatically by `t.test(rel~trt, data=ap, var.equal=FALSE)`. In the armpit data this gives
$df = 17.876$ — close to the pooled test's degrees of freedom, because the two groups' variances
turn out to be approximately equal, and correspondingly the two versions of the test agree closely
here.

## How to report a result

The chapter's running theme resolves into a single rule of thumb: **report the effect size together
with its confidence interval, and its p-value** — not the p-value alone. The two are not
independent pieces of information to choose between:

1. The outcome of an $\alpha$-level hypothesis test is exactly equivalent to checking whether the
   null value of the effect ($0$, here) lies inside the corresponding $1-\alpha$ confidence
   interval — so the test result can always be read off the interval.
2. The confidence interval additionally lets the reader judge **scientific relevance**, which a
   p-value alone cannot do: an effect can be extremely statistically significant and still be too
   small, biologically, to matter. Looking only at significance hides this; the interval reveals it
   directly, since a significant but tiny effect shows up as an interval that excludes zero but sits
   entirely close to it.

## Exercises

No problem set accompanied this material.

## Sources

- `docs/omics-statistics/gtpb/psls20/theory/05-statisticalInference-twosampleT/01-introduction.md`
  — the armpit-microbiome experiment, its design and data exploration.
- `docs/omics-statistics/gtpb/psls20/theory/05-statisticalInference-twosampleT/02-two-sample-t-test.md`
  — notation, hypotheses, the pooled variance estimator, the test statistic, and the worked
  armpit-data conclusion.
- `docs/omics-statistics/gtpb/psls20/theory/05-statisticalInference-twosampleT/03-assumptions.md`
  — the assumptions behind the test, how to check them, the Welch modification, and how to report
  results.

All three are converted from `theory/05-statisticalInference-twosampleT.Rmd` in the GTPB PSLS20
course (CC BY 4.0). No slide deck or lecture transcript accompanied this material — only the
course's own written notes, which is why this chapter follows them directly. The R code that
produces the boxplots, QQ-plots and `t.test` calls is referenced but its output (the actual armpit
dataset, plots and printed test results) was not included in the supplied material and is not
reproduced here.

---

[← 6. The Logic of Statistical Inference](06-the-logic-of-statistical-inference.md) · [Contents](index.md) · [8. Hypothesis-Testing Case Studies →](08-hypothesis-testing-case-studies.md)
