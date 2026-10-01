---
title: "2. Population, Sample, and Random Variables"
course: "GTPB Psls20"
chapter: 2
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Population, Sample, and Random Variables

## What this covers

Every later chapter talks about "the population" and "the sample" and switches between capital
and lowercase letters without comment. This chapter answers the question that makes those habits
make sense: what is a population, what is a random variable, and how does a probability
distribution let us describe a population and then, from a sample, estimate it. It assumes only
basic algebra — probability is built here from the ground up, using one running dataset (NHANES,
a survey of the American population) and three running examples: gender, IQ, and direct
cholesterol.

## The cycle a study goes through

A study is never really about the handful of subjects enrolled in it. The researcher wants to say
something about a **population**: the set of subjects — usually infinite, always a theoretical
construct — that the conclusion is meant to generalize to. Because a population can essentially
never be observed in full, a study runs through three stages:

1. **Experimental design.** Decide on the population, then draw a **representative sample** from
   it: financial and logistic limits force this, but the sample has to be drawn so that every
   subject in the population has an equal chance of ending up in it.
2. **Data exploration and descriptive statistics.** Explore, visualize and summarize the sample —
   gain insight, check assumptions.
3. **Estimation and inference.** Generalize what is observed in the sample back to the population,
   using a statistical model, and report the uncertainty in doing so.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Population and sample linked by sampling and by inference, with exploration happening inside the sample">
  <rect x="30" y="20" width="260" height="70" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="47" text-anchor="middle" font-size="13" fill="currentColor">population</text>
  <text x="160" y="66" text-anchor="middle" font-size="11" fill="currentColor">theoretical, usually infinite</text>

  <rect x="30" y="150" width="260" height="70" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="177" text-anchor="middle" font-size="13" fill="currentColor">sample</text>
  <text x="160" y="196" text-anchor="middle" font-size="11" fill="currentColor">n subjects, observed</text>

  <defs>
    <marker id="arrow2c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>

  <line x1="110" y1="92" x2="110" y2="148" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2c)"/>
  <text x="15" y="122" font-size="11" fill="currentColor">(1) design &#38; sample</text>

  <line x1="230" y1="148" x2="230" y2="92" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2c)"/>
  <text x="185" y="122" font-size="11" fill="currentColor">(3) infer back</text>

  <text x="160" y="232" text-anchor="middle" font-size="11" fill="currentColor">(2) explore &#38; describe, inside the sample</text>
</svg>
<figcaption>The three stages of a study: draw a representative sample from the population,
explore and summarize it, then use a model to generalize the result back to the population, with
a stated uncertainty.</figcaption>
</figure>

The rest of this chapter is vocabulary for stage 1 (population, random variable) and machinery for
stages 2 and 3 (distributions, mean, variance, estimates). The running dataset throughout is
NHANES — the National Health and Nutrition Examination Survey, an American demographic study
recording a large number of physical, demographic, nutritional, lifestyle and health
characteristics on a sample of subjects.

## Variables

A **variable** is a characteristic measured on the subjects in the sample — direct cholesterol,
age, gender. It varies from subject to subject in the population, and so also within the sample
and from sample to sample. Variables come in two families:

- **Qualitative variables**: a limited number of non-numeric categories.
  - *Nominal*: no natural ordering — gender, blood group, eye colour.
  - *Ordinal*: a natural ordering — BMI class, smoking status (1: never smoked, 2: stopped
    smoking, 3: smoker).
- **Numeric variables**:
  - *Discrete*: counts — number of partners over a lifetime, and so on.
  - *Continuous*: can in principle take any value between two limits — age, weight, BMI, a
    fluorescence measurement in an ELISA assay.

A continuous variable is often dichotomized into a qualitative one for convenience. That always
throws information away.

## The population, defined

The aim of a scientific study is a general statement about a population — for instance, whether
average cholesterol differs between males and females above age 25. That last clause matters: a
population in statistics has to be **clearly defined**, and it is a theoretical object precisely
because it is in continuous change and because conclusions are usually meant to generalize to
future subjects as well as present ones. It can typically be treated as infinite.

A population is pinned down by two kinds of criteria:

- **Inclusion criteria** — characteristics a subject must have to belong to the population, e.g.
  age above 25, normal BMI.
- **Exclusion criteria** — characteristics that rule a subject out, e.g. pregnancy in a study of a
  new drug, or diabetes, a history of hard drugs, or generally low health status when the aim is
  to establish a range of normal values in a population of healthy individuals.

## Random variables

Because a variable's value changes across the population, it is *random*: before a subject is
drawn, its value for that subject is unknown. This is more than a formality — the crucial question
of the whole course is *how precise are conclusions drawn from a sample about the population*, and
that question only makes sense once "the value we would get from a random subject" is itself
treated as an object that varies from sample to sample.

**Convention.** A capital letter (e.g. $X$) denotes a study characteristic without reference to any
particular subject's value — a **random variable**, the result of randomly sampling the
characteristic from the population. $X$ is the not-yet-collected measurement on a random subject.
A study typically produces a whole sequence $X_1, \ldots, X_n$, one per subject. Random variables
can be qualitative or quantitative, discrete or continuous, exactly like the variables they
represent — the only new thing is the acknowledgment that their value is not yet known.

## Probability: the discrete case

To reason about how precise a conclusion is, we need probability. Start with a discrete random
variable $X$.

- The set of all possible values of $X$ is the **sample space** $\Omega$. For gender,
  $\Omega = \{0,1\}$ (0: male, 1: female); for a die roll, $\Omega = \{1,2,3,4,5,6\}$.
- An **event** $A$ is a subset of $\Omega$ — e.g. "an even number" on a die, $A = \{2,4,6\}$, or a
  single outcome, $A = \{1\}$. The **event space** $\mathcal{A}$ is the class of all events
  associated with the experiment.
- Two events are **mutually exclusive** if they cannot occur together: the odd numbers
  $A_1 = \{1,3,5\}$ and the single outcome $A_2 = \{6\}$ satisfy $A_1 \cap A_2 = \emptyset$.
- A **probability** is a function $P: \mathcal{A} \to [0,1]$ satisfying
  1. $0 \le P(A) \le 1$ for every $A \in \mathcal{A}$,
  2. $P(\Omega) = 1$,
  3. for mutually exclusive events $A_1, \ldots, A_k$,
     $P(A_1 \cup \cdots \cup A_k) = P(A_1) + \cdots + P(A_k)$.

For the die, "odd number" is the union of the three mutually exclusive single-outcome events
$\{1\}, \{3\}, \{5\}$, so $P(\text{odd}) = \tfrac16+\tfrac16+\tfrac16 = 0.5$, and
$P(\Omega) = 1$ as it must. If two subjects $j$ and $k$ are drawn independently from the
population, the joint probability factors: $P(X_j, X_k) = P(X_j)\,P(X_k)$.

### Probability mass function, mean, variance

The **probability mass function (pmf)** gives the probability of each value in $\Omega$. Gender is
binary, and binary variables are **Bernoulli distributed**: in the American population 50.8% of
subjects are female, so with $\pi = 0.508$ the probability of being female,
$$X \sim \begin{cases} P(X=0) = 1-\pi \\ P(X=1) = \pi \end{cases},
\qquad P(X=x) = \pi^{x}(1-\pi)^{1-x}.$$
This is written in shorthand as $X \sim B(\pi)$.

The **cumulative distribution function** $F(x) = \sum_{X \le x} P(X)$ gives the probability of
observing a value at most $x$. For gender, $F(0) = 1-\pi$ and $F(1) = 1$.

The **mean**, or expected value,
$$E[X] = \sum_{x \in \Omega} x\, P(X=x)$$
is $E[X] = 0\cdot(1-\pi) + 1\cdot\pi = \pi = 0.508$ for gender, and for a fair die
$E[X] = \tfrac16(1+2+\cdots+6) = 3.5$.

The **variance** measures the variability of $X$ around its mean,
$$\mathrm{Var}(X) = E[(X-E[X])^2] = \sum_{x\in\Omega}(x-E[X])^2 P(X=x).$$
For the Bernoulli case this simplifies to a clean closed form, worth seeing worked through once:
$$
\begin{aligned}
E[(X-\pi)^2] &= (0-\pi)^2(1-\pi) + (1-\pi)^2\pi \\
&= \pi^2(1-\pi) + (1-\pi)^2\pi \\
&= \pi(1-\pi)\big(\pi + (1-\pi)\big) \\
&= \pi(1-\pi).
\end{aligned}
$$
So a Bernoulli random variable has mean $\pi$ and variance $\pi(1-\pi)$ — largest at $\pi=0.5$,
zero at $\pi=0$ or $1$, exactly as it should be: the more lopsided the split, the less a random
draw actually varies.

## Probability: the continuous case

A continuous variable's sample space $\Omega$ is infinitely large — it is impossible to predict
the exact value $X$ will take, but it *is* possible to reason about probabilities using a
**density function** $f(x)$, which describes how likely it is to observe a value near $x$ when
sampling a random subject. Many biological characteristics are, after transformation if necessary,
approximately **normally distributed**:
$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad
\text{shorthand: } f(x) = N(\mu,\sigma^2).$$
IQ in the population is known to follow $N(100, 15^2)$: mean 100, standard deviation 15.

The **cumulative distribution function** is again $F(x) = P(X \le x)$, but for a continuous
variable this is an integral rather than a sum:
$$F(x) = \int_{-\infty}^{x} f(t)\,dt,$$
with $f(x)=0$ outside the sample space. Over the whole sample space the area under the density is
exactly 1, $\int_{\Omega} f(x)\,dx = 1$ — probability 1 that $X$ takes *some* value. Concretely, for
$X \sim N(100,15^2)$, the probability that a random subject's IQ is below 80 is
$F(80) = \int_{-\infty}^{80} f(x)\,dx \approx 0.09$ — the two standard deviations below the mean
put 80 well into the lower tail.

### Mean, variance, and the empirical rule

For a continuous variable the mean and variance are again integrals rather than sums:
$$E[X] = \int_\Omega x f(x)\,dx, \qquad \mathrm{Var}(X) = \int_\Omega (x-E[X])^2 f(x)\,dx,$$
which for the normal distribution evaluate to exactly $\mu$ and $\sigma^2$ — the two parameters
that name the distribution are its mean and variance. Because the variance is not in the same
units as $X$, it is usually reported as the **standard deviation** $SD = \sqrt{\mathrm{Var}(X)}$,
which is.

The standard deviation of a normal distribution has a direct reading: about 68% of the population
lies within one standard deviation of the mean, and about 95% lies within two —
$$P(\mu-\sigma < X < \mu+\sigma) \approx 0.68, \qquad P(\mu-2\sigma < X < \mu+2\sigma) \approx 0.95.$$

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Normal density curve with the region within two standard deviations of the mean shaded">
  <path d="M20,170 C60,170 90,40 160,30 C230,40 260,170 300,170" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M100,170 C115,170 125,70 160,60 C195,70 205,170 220,170 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="160" y1="30" x2="160" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="100" y1="170" x2="100" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="220" y1="170" x2="220" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="20" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="100" y="188" text-anchor="middle" font-size="12" fill="currentColor">&#956; − 2&#963;</text>
  <text x="160" y="188" text-anchor="middle" font-size="12" fill="currentColor">&#956;</text>
  <text x="220" y="188" text-anchor="middle" font-size="12" fill="currentColor">&#956; + 2&#963;</text>
  <text x="160" y="100" text-anchor="middle" font-size="12" fill="currentColor">≈ 95%</text>
</svg>
<figcaption>For a normal density, the shaded region within two standard deviations of the mean
holds about 95% of the population; one standard deviation (unshaded here) holds about 68%.</figcaption>
</figure>

### Standardization

Normal data are often **standardized**,
$$z = \frac{x-\mu}{\sigma},$$
so that $z \sim N(0,1)$, the *standard* normal distribution. The quantiles
$z_{2.5\%}$ and $z_{97.5\%}$ satisfying $F(z_{2.5\%}) = 0.025$ and $F(z_{97.5\%}) = 0.975$ are
$-1.96$ and $1.96$: about $97.5\% - 2.5\% = 95\%$ of a standard normal variable falls in
$[-1.96, 1.96]$ — the interval of two standard deviations either side of the mean, in different
notation for the same fact stated above.

## From population to sample

In real studies the population's distribution is unknown, and its parameters — mean IQ, variance
of IQ — cannot be pinned down without error, because only a small subset of the population, the
**sample**, is ever actually studied. Sampling completely at random gives every subject an equal
chance of inclusion, which is what makes a sample *representative*.

The sample $x_1, x_2, \ldots, x_n$ is treated as $n$ realizations of the same random variable $X$,
one per subject $i = 1, \ldots, n$. If the family of the population distribution can be assumed
(e.g. normal), only its parameters need to be estimated from the sample — $\mu$ and $\sigma^2$,
written as estimates $\hat\mu$ and $\hat\sigma^2$ once estimated.

**In summary**: the unknown values of the characteristic for subjects $1$ to $n$ in a sample not
yet drawn are random variables $X_1, \ldots, X_n$ — that is the object we reason about in order to
understand how observations, estimates and conclusions would change from sample to sample. Once
the sample is drawn, we observe the *realized* outcomes $x_1, \ldots, x_n$ — the actual genders or
cholesterol levels measured. Capital letters for the not-yet-observed, lowercase for the observed,
throughout.

## Worked example: gender as a Bernoulli variable

Gender in NHANES is binary, hence Bernoulli, with parameter $\pi$ — its mean. The natural estimate
of $\pi$ from the sample is the **sample mean** $\bar x = \frac1n\sum_{i=1}^n x_i$. Note already
that the sample mean is itself a random variable: computed from a random sample, it too varies
from sample to sample, and is denoted $\bar X$ before the sample is fixed.

A practical trap sits inside this example. NHANES stores Gender as a categorical factor, and R's
default is to take the alphabetically first level — "female" — as the reference class. Recoding it
to a 0/1 numeric variable via `as.numeric(Gender) - 1` gives 1 to the *second* alphabetical level,
i.e. male, and 0 to female. The sample mean of that recoded variable therefore estimates the
fraction of *males*, not females, in the population — the opposite of what the raw factor levels
might suggest. The general lesson: always be deliberate about which category a 0/1 encoding
actually points at, because the estimator's meaning flips with it.

## Worked example: direct cholesterol, empirical vs. normal

### Empirical distribution

A histogram of direct cholesterol for the female subjects in NHANES is visibly skewed, with a tail
to the right. Because every observation in a sample of size $n$ occurs exactly once, the sample
itself defines a discrete distribution with probability $1/n$ on each observed value. The resulting
**empirical cumulative distribution function** is
$$\mathrm{ECDF}(x) = \sum_{x_i \le x} \frac1n = \frac{\#\{x_i \le x\}}{n},$$
a step function that estimates $F(x)$ directly from the data, with no assumption about the
underlying shape. The same construction was compared for the full female subsample and for a small
subsample of just 10 women, to see what happens when data are scarce.

### Normal approximation

The raw cholesterol histogram is skewed, but its $\log_2$-transformed version has a "nice bell
shape" — close enough to normal that it can be approximated by $N(\hat\mu, \hat\sigma^2)$, with
$\hat\mu$ and $\hat\sigma^2$ estimated by the sample mean and sample variance of $\log_2(\text{DirectChol})$.
The same fit was done twice: once on the full sample of women, once on the 10-woman subsample.

### Reference intervals

A 95% **reference interval** is the range in which 95% of the population's values for a
characteristic are expected to fall — the applied version of the standard-deviation reading given
above. It can be estimated two ways:

- **Empirically**, from the sample's own 2.5% and 97.5% quantiles of the raw DirectChol values.
- **Via the normal approximation**, using the fact that a 95% interval sits roughly two standard
  deviations either side of the mean on the (log) scale, then transforming back with $2^{(\cdot)}$
  since the fit was done on $\log_2$ values.

For the large sample the two methods agree closely. For the 10-woman sample they do not: the
empirical quantile estimate is crude, because there simply are not enough observations to pin down
an *extreme* quantile — 2.5% of 10 observations is a fraction of one data point. The normal
approximation does better here precisely because it uses *all* the data to estimate just two
numbers, the mean and the variance, rather than trying to read the tails directly off ten points.
That advantage is conditional: it only holds if the normal assumption is actually a good one.

## Statistics and the notation convention

A formula used to estimate a population parameter from a sample is a **statistic**, or an
**estimator**; the number obtained by evaluating it on a particular sample is also called a
statistic, or an **estimate**. Because a statistic is computed from the (random) sample, it is
itself a random variable — hence the capital-letter notation $\bar X$ for the sample mean and $S^2$
for the sample variance, reserved for reasoning about how the statistic would vary from sample to
sample. When it refers to the one number realized in a particular, already-drawn sample, the
lowercase $\bar x$ and $s^2$ are used instead.

Pulling the whole notational scheme together:

| | Population | Sample |
|---|:---:|:---:|
| fixed, unknown, Greek | $\mu$ | — |
| estimate of it | — | $\bar X$ or $\hat\mu$ |
| fixed, unknown, Greek | $\sigma^2$ | — |
| estimate of it | — | $S^2$ or $\hat\sigma^2$ |

**Population parameters are fixed but unknown, and are always Greek.** **Statistics used to
estimate them are Roman letters, decorated with a bar or a hat.** Every later chapter's notation
follows from this one rule.

## Exercises

All three use the model introduced above for IQ in the population, $IQ \sim N(100, 15^2)$.

1. What is the probability that a randomly chosen subject in the population has an IQ below 90?
2. What is the probability that a randomly chosen subject has an IQ below 110?
3. What is the probability that a randomly chosen subject has an IQ between 90 and 110?

## Sources

- All content is from the GTPB PSLS20 course, "Concepts" (`theory/02-concepts.Rmd`), as split into
  six library pages: `01-introduction.md`, `02-random-variables.md`,
  `03-describing-the-population.md`, `04-sample.md`, `05-gender-example.md` and
  `06-direct-cholesterol-example.md` (licence CC BY 4.0). No separate slide deck, transcript or
  problem set was supplied for this task; these six pages — themselves a lossless conversion of
  the lecture's R Markdown slide source — are the only input.
- The two diagrams (the population/sample/inference cycle; the shaded normal density) are redrawn
  from the R plotting code embedded in `01-introduction.md` and `03-describing-the-population.md`
  respectively. The rendered NHANES plots referred to throughout — the gender bar chart, the
  cholesterol histograms, the ECDFs, the density overlays — were part of the original R Markdown
  output but were not available as images here; their qualitative descriptions (e.g. "skewed with
  a tail to the right") are taken directly from the source text rather than reconstructed.
- The three IQ-probability questions in the Exercises section are the course's own, taken from
  `03-describing-the-population.md`; only the first came with a stated method (R's `pnorm`) in the
  source, and none came with a computed numeric answer.

---

[← 1. Statistics in the Scientific Method](01-statistics-in-the-scientific-method.md) · [Contents](index.md) · [3. Experimental Design and Randomization →](03-experimental-design-and-randomization.md)
