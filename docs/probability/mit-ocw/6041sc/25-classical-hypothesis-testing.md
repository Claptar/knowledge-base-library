---
title: "25. Classical Hypothesis Testing"
course: "MIT 6.041SC"
chapter: 25
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 25. Classical Hypothesis Testing

## What this covers

This chapter covers the foundations of classical hypothesis testing, moving from simple binary tests to composite hypotheses and goodness-of-fit procedures. It addresses how to partition data spaces into acceptance and rejection regions, how to balance the two types of decision errors, and how to verify whether observed data conform to an assumed probability model. We assume familiarity with basic continuous and discrete probability distributions, the Central Limit Theorem, and derived distributions.

## Classical Binary Hypothesis Testing

In the classical hypothesis testing framework, we do not assign prior probabilities to the possible states of the world. Instead, we formulate two competing hypotheses:

- The **null hypothesis**, denoted $H_0$, represents the default, baseline, or "status quo" model:
  $$X \sim p_X(x; H_0) \quad \text{or} \quad X \sim f_X(x; H_0)$$
- The **alternative hypothesis**, denoted $H_1$, represents a deviation from the baseline:
  $$X \sim p_X(x; H_1) \quad \text{or} \quad X \sim f_X(x; H_1)$$

When an experiment is performed, we observe a vector of data points $X = (X_1, X_2, \dots, X_n)$ residing in a data space $\mathcal{X}$. A hypothesis test partitions this space into two complementary sets:
1. An **acceptance region**, where we decide not to reject $H_0$.
2. A **rejection region** $R \subset \mathcal{X}$ (also known as the critical region), where we reject $H_0$ in favor of $H_1$.

Designing a statistical test requires two steps: choosing the geometric form or shape of the boundary that separates the acceptance region from the rejection region, and choosing the exact location of that boundary.

### The Likelihood Ratio Test

When both $H_0$ and $H_1$ are simple hypotheses (completely specifying the distribution), the canonical choice of decision structure is the **likelihood ratio test** (LRT). Given the observed data vector $x$, the likelihood ratio $L(x)$ is defined as:

$$L(x) = \frac{p_X(x; H_1)}{p_X(x; H_0)} \quad \text{(discrete case)}$$

or

$$L(x) = \frac{f_X(x; H_1)}{f_X(x; H_0)} \quad \text{(continuous case)}$$

A large value of $L(x)$ indicates that the observed sample is substantially more plausible under $H_1$ than under $H_0$. Thus, the test takes the structural form:

$$\text{Reject } H_0 \iff L(x) > \xi$$

where $\xi > 0$ is a scalar threshold called the **critical value**.

By evaluating the likelihood ratio, we map the multidimensional data vector $x$ to a single one-dimensional summary: a **statistic** $T = L(X)$. The complex geometric problem of selecting an $n$-dimensional decision boundary simplifies to placing a single cutoff point $\xi$ on the real line.

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Likelihood ratio scalar line partitioned at threshold xi into acceptance and rejection regions">
  <!-- Real line axis -->
  <line x1="30" y1="90" x2="390" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="390,87 400,90 390,93" fill="currentColor"/>
  
  <!-- Threshold tick -->
  <line x1="220" y1="75" x2="220" y2="105" stroke="currentColor" stroke-width="2"/>
  <text x="220" y="125" text-anchor="middle" font-size="12" fill="currentColor">Threshold ξ</text>
  
  <!-- Rejection Region shading on axis line -->
  <rect x="220" y="85" width="170" height="10" fill="currentColor" fill-opacity="0.15"/>
  
  <!-- Labels for regions -->
  <text x="125" y="65" text-anchor="middle" font-size="12" fill="currentColor">Accept H₀ (L(x) ≤ ξ)</text>
  <text x="310" y="65" text-anchor="middle" font-size="12" fill="currentColor">Reject H₀ (L(x) > ξ)</text>
  <text x="395" y="110" text-anchor="end" font-size="12" fill="currentColor">L(x)</text>
</svg>
<figcaption>The likelihood ratio $L(x)$ condenses multidimensional data onto the real line, dividing decisions into acceptance and rejection regions at threshold $\xi$.</figcaption>
</figure>

### Error Probabilities and the Fundamental Trade-off

Because the data vector $X$ is random, any decision rule can make mistakes. There are two distinct types of errors:

1. **Type I error (False rejection):** Rejecting $H_0$ when $H_0$ is actually true. Its probability is denoted $\alpha$:
   $$\alpha = \mathbf{P}(\text{reject } H_0; H_0) = \mathbf{P}(L(X) > \xi; H_0)$$
   In statistical testing, $\alpha$ is called the **significance level** or false alarm rate (commonly set to $\alpha = 0.05$).

2. **Type II error (False acceptance):** Accepting $H_0$ when $H_1$ is actually true. Its probability is denoted $\beta$:
   $$\beta = \mathbf{P}(\text{accept } H_0; H_1) = \mathbf{P}(L(X) \le \xi; H_1)$$

<figure>
<svg viewBox="0 0 460 220" role="img" aria-label="Distributions of the test statistic under H0 and H1 showing Type I error alpha and Type II error beta">
  <!-- Horizontal axis -->
  <line x1="30" y1="180" x2="430" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="430,177 440,180 430,183" fill="currentColor"/>
  
  <!-- Distribution under H0: center ~ 150 -->
  <path d="M 60 180 C 110 180, 120 40, 150 40 C 180 40, 190 180, 240 180" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="130" y="30" font-size="12" fill="currentColor">f(l; H₀)</text>
  
  <!-- Distribution under H1: center ~ 290 -->
  <path d="M 200 180 C 250 180, 260 40, 290 40 C 320 40, 330 180, 380 180" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="310" y="30" font-size="12" fill="currentColor">f(l; H₁)</text>
  
  <!-- Threshold line xi at x = 215 -->
  <line x1="215" y1="20" x2="215" y2="180" stroke="currentColor" stroke-dasharray="4" stroke-width="1.5"/>
  <text x="215" y="195" text-anchor="middle" font-size="12" fill="currentColor">ξ</text>
  
  <!-- Shaded tail under H0 to the right of xi (alpha) -->
  <path d="M 215 146 C 223 162, 230 174, 240 180 L 215 180 Z" fill="currentColor" fill-opacity="0.15"/>
  <text x="245" y="165" font-size="11" fill="currentColor">α</text>
  
  <!-- Shaded tail under H1 to the left of xi (beta) -->
  <path d="M 200 180 C 205 180, 210 170, 215 152 L 215 180 Z" fill="currentColor" fill-opacity="0.15"/>
  <text x="185" y="165" font-size="11" fill="currentColor">β</text>
</svg>
<figcaption>Distributions of the test statistic under $H_0$ and $H_1$. The threshold $\xi$ trades off false rejection probability $\alpha$ against false acceptance probability $\beta$.</figcaption>
</figure>

A fundamental trade-off governs $\alpha$ and $\beta$:
- Shifting $\xi$ to the right decreases $\alpha$ (fewer false rejections), but increases $\beta$. At the extreme $\xi \to \infty$, $\alpha = 0$ and $\beta = 1$.
- Shifting $\xi$ to the left decreases $\beta$, but increases $\alpha$. At the extreme $\xi \to -\infty$, $\alpha = 1$ and $\beta = 0$.

Simultaneous minimization of both error probabilities is impossible for a fixed sample size. The standard approach fixes $\alpha$ at a prescribed tolerance (e.g., $0.05$) and places $\xi$ such that $\mathbf{P}(L(X) > \xi; H_0) = \alpha$. 

A central theoretical result of classical hypothesis testing states that the likelihood ratio test achieves the optimal trade-off curve between $\alpha$ and $\beta$: for any prescribed false rejection probability $\alpha$, no other decision rule yields a smaller false acceptance probability $\beta$.

---

## Examples: Normal Mean and Variance Tests

### Test on a Normal Mean

Let $X_1, X_2, \dots, X_n$ be independent and identically distributed (i.i.d.) observations drawn from a normal distribution with variance $\sigma^2 = 1$. We wish to test:
$$H_0: X_i \sim \mathcal{N}(0, 1) \quad \text{versus} \quad H_1: X_i \sim \mathcal{N}(1, 1)$$

The joint probability density functions under $H_0$ and $H_1$ are:
$$f_X(x; H_0) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}} \exp\left\{ -\frac{x_i^2}{2} \right\} = \left(\frac{1}{\sqrt{2\pi}}\right)^n \exp\left\{ -\frac{1}{2} \sum_{i=1}^n x_i^2 \right\}$$
$$f_X(x; H_1) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}} \exp\left\{ -\frac{(x_i - 1)^2}{2} \right\} = \left(\frac{1}{\sqrt{2\pi}}\right)^n \exp\left\{ -\frac{1}{2} \sum_{i=1}^n (x_i - 1)^2 \right\}$$

The likelihood ratio test rejects $H_0$ if:
$$\frac{f_X(x; H_1)}{f_X(x; H_0)} = \frac{\exp\left\{ -\frac{1}{2}\sum_{i=1}^n (x_i - 1)^2 \right\}}{\exp\left\{ -\frac{1}{2}\sum_{i=1}^n x_i^2 \right\}} > \xi$$

Expanding $(x_i - 1)^2 = x_i^2 - 2x_i + 1$ inside the exponent:
$$\exp\left\{ -\frac{1}{2} \sum_{i=1}^n \left( (x_i - 1)^2 - x_i^2 \right) \right\} = \exp\left\{ \sum_{i=1}^n x_i - \frac{n}{2} \right\} > \xi$$

Taking the natural logarithm of both sides:
$$\sum_{i=1}^n x_i - \frac{n}{2} > \ln \xi \implies \sum_{i=1}^n x_i > \ln \xi + \frac{n}{2} \equiv \xi'$$

The optimal test reduces to computing the sample sum $\sum_{i=1}^n X_i$ and rejecting $H_0$ if this statistic exceeds a new threshold $\xi'$. 

To calibrate $\xi'$ for a specified significance level $\alpha$ (e.g., $\alpha = 0.05$):
$$\mathbf{P}\left(\sum_{i=1}^n X_i > \xi'; H_0\right) = \alpha$$

Under $H_0$, each $X_i \sim \mathcal{N}(0, 1)$, so the sum $S = \sum_{i=1}^n X_i$ is distributed as $\mathcal{N}(0, n)$. Standardizing $S$:
$$\mathbf{P}\left(\frac{S}{\sqrt{n}} > \frac{\xi'}{\sqrt{n}}\right) = \alpha$$
The critical value $\xi'$ is determined directly from standard normal tables.

### Test on a Normal Variance

Consider next the case where the mean is known to be zero, but the variance is uncertain:
$$H_0: X_i \sim \mathcal{N}(0, 1) \quad \text{versus} \quad H_1: X_i \sim \mathcal{N}(0, 4)$$
given $n$ i.i.d. observations. The likelihood ratio is:
$$\frac{f_X(x; H_1)}{f_X(x; H_0)} = \frac{\left( \frac{1}{\sqrt{2\pi \cdot 4}} \right)^n \exp\left\{ -\frac{1}{2 \cdot 4}\sum_{i=1}^n x_i^2 \right\}}{\left( \frac{1}{\sqrt{2\pi}} \right)^n \exp\left\{ -\frac{1}{2}\sum_{i=1}^n x_i^2 \right\}} > \xi$$

Simplifying:
$$\left(\frac{1}{2}\right)^n \exp\left\{ \left(-\frac{1}{8} + \frac{1}{2}\right) \sum_{i=1}^n x_i^2 \right\} = \left(\frac{1}{2}\right)^n \exp\left\{ \frac{3}{8}\sum_{i=1}^n x_i^2 \right\} > \xi$$

Taking logarithms:
$$\frac{3}{8}\sum_{i=1}^n x_i^2 > \ln \xi + n\ln 2 \implies \sum_{i=1}^n x_i^2 > \xi'$$

The likelihood ratio test prescribes using the sum of squares, $\sum_{i=1}^n X_i^2$, as the test statistic. To determine $\xi'$ such that:
$$\mathbf{P}\left(\sum_{i=1}^n X_i^2 > \xi'; H_0\right) = \alpha$$
we solve a derived distribution problem. Under $H_0$, the $X_i$ are independent standard normal variables $\mathcal{N}(0,1)$. The sum of the squares of $n$ independent standard normal variables follows a **chi-square distribution** with $n$ degrees of freedom ($\chi^2_n$). Because this distribution is thoroughly tabulated, the threshold $\xi'$ is selected as the $(1 - \alpha)$-quantile of the $\chi^2_n$ distribution.

---

## Testing Composite Hypotheses

In many practical applications, the alternative hypothesis cannot be described by a single parameter value. When testing whether a coin is fair, the alternative is not simply that $p = 0.6$; it is the entire continuum $p \neq 0.5$. A hypothesis that encompasses more than one parameter state is called a **composite hypothesis**.

Because we cannot construct a simple likelihood ratio $f(x; H_1)/f(x; H_0)$ against an entire family of alternatives, testing proceeds as follows:
1. Select an intuitive scalar summary statistic $T(X)$ reflecting departures from $H_0$.
2. Choose the shape of the rejection region (e.g., extreme deviations $|T - \mathbf{E}[T]| > \xi$).
3. Fix a significance level $\alpha$ (typically $\alpha = 0.05$).
4. Compute the distribution of $T$ under $H_0$ and set $\xi$ so that $\mathbf{P}(\text{reject } H_0; H_0) = \alpha$.

### Example: Testing Whether a Coin is Fair

Suppose a coin is tossed $n = 1000$ times, yielding $S = 472$ heads. Is the coin fair?
- $H_0: p = 1/2$
- $H_1: p \neq 1/2$

Under $H_0$, the expected number of heads is $n/2 = 500$. If the coin is fair, large deviations $|S - n/2|$ are rare. We define the rejection region:
$$\text{Reject } H_0 \iff \left|S - \frac{n}{2}\right| > \xi$$

By the Central Limit Theorem, under $H_0$, the total number of heads $S = \sum_{i=1}^n X_i$ is approximately normal with:
$$\mathbf{E}[S; H_0] = 1000 \times 0.5 = 500, \quad \operatorname{Var}(S; H_0) = 1000 \times 0.5 \times 0.5 = 250$$
The standard deviation is $\sigma = \sqrt{250} \approx 15.81$.

We require a significance level $\alpha = 0.05$, meaning:
$$\mathbf{P}(|S - 500| \le \xi; H_0) \approx 0.95$$
For a normal distribution, $95\%$ of the probability mass lies within approximately $1.96$ standard deviations of the mean:
$$\xi \approx 1.96 \times 15.81 \approx 31$$

Evaluating our observed data:
$$|S - 500| = |472 - 500| = 28$$
Since $28 \le 31$, the observed outcome falls inside the acceptance region. We conclude: **$H_0$ is not rejected at the 5% level**.

### "Not Rejected" versus "Accepted"

In scientific inference, observing data consistent with $H_0$ does not prove that $H_0$ is true. A coin with true bias $p = 0.50001$ or a sequence of dependent tosses could readily yield $472$ heads in $1000$ tosses. 

No finite amount of data can establish that $p$ is strictly $1/2$; data can only falsify hypotheses whose predictions are severely incompatible with observation. Therefore, statisticians state that the null hypothesis is **not rejected** rather than "accepted." The default model remains a working description of reality until evidence contradicts it.

---

## Goodness-of-Fit Tests

Goodness-of-fit tests evaluate whether an entire probability distribution or probability mass function fits an observed sample.

### Discrete Goodness-of-Fit: Testing a Die

Suppose we roll a six-sided die $n$ times and wish to test:
$$H_0: p_i = \mathbf{P}(X = i) = \frac{1}{6}, \quad i = 1, \dots, 6$$
assuming independent rolls.

Let $N_i$ denote the number of times face $i$ appears across the $n$ rolls, such that $\sum_{i=1}^6 N_i = n$. Under $H_0$, the expected count for face $i$ is $n p_i = n/6$. Large discrepancies between observed counts $N_i$ and expected counts $n p_i$ provide evidence against $H_0$.

The standard discrepancy measure is the **chi-square statistic**:
$$T = \sum_{i=1}^6 \frac{(N_i - n p_i)^2}{n p_i}$$

The test rule is:
$$\text{Reject } H_0 \iff T > \xi$$
where $\xi$ is chosen such that $\mathbf{P}(T > \xi; H_0) = 0.05$.

Under $H_0$, each count $N_i$ is a binomial random variable. By the Central Limit Theorem, for large $n$, each $N_i - np_i$ is approximately normal. Squaring, normalizing, and summing these variables produces a statistic $T$ whose large-$n$ limiting distribution under $H_0$ is a chi-square distribution with $m - 1 = 5$ degrees of freedom (one degree of freedom is lost because $\sum_{i=1}^6 N_i = n$). The critical value $\xi$ is obtained from standard chi-square tables.

### Continuous Goodness-of-Fit

When observations are continuous, testing whether data originate from a hypothesized probability density function $f_X(x)$ can be handled in two ways.

#### 1. Binning and the Chi-Square Test
One can partition the range of the random variable into $k$ disjoint intervals (bins) $[a_{i-1}, a_i)$. For each bin, compute the theoretical probability under $H_0$:
$$p_i = \int_{a_{i-1}}^{a_i} f_X(x; H_0)\,dx$$
With $N_i$ representing the observed count in bin $i$, the test statistic:
$$T = \sum_{i=1}^k \frac{(N_i - n p_i)^2}{n p_i}$$
approximately follows a $\chi^2_{k-1}$ distribution under $H_0$ for large $n$. However, binning requires an ad hoc choice of bin boundaries: bins that are too narrow leave many counts at zero, while bins that are too wide discard distributional information.

#### 2. The Kolmogorov-Smirnov Test
The Kolmogorov-Smirnov test avoids arbitrary binning by comparing the hypothesized continuous cumulative distribution function (CDF), $F_X(x)$, directly to the **empirical CDF** $\hat{F}_X(x)$ constructed from the sample $X_1, \dots, X_n$:
$$\hat{F}_X(x) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{\{X_i \le x\}} = \frac{\text{number of observations } \le x}{n}$$

Under $H_0$, the Law of Large Numbers implies that $\hat{F}_X(x) \to F_X(x)$ as $n \to \infty$ for every $x$. The Kolmogorov-Smirnov test statistic measures the maximum vertical discrepancy between the two functions:
$$D_n = \max_x |F_X(x) - \hat{F}_X(x)|$$

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Comparison between hypothesized smooth CDF and staircase empirical CDF showing maximum discrepancy Dn">
  <!-- Axes -->
  <line x1="40" y1="190" x2="390" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="390" y="205" text-anchor="end" font-size="12" fill="currentColor">x</text>
  <text x="30" y="25" text-anchor="end" font-size="12" fill="currentColor">F(x)</text>
  
  <!-- Smooth theoretical CDF -->
  <path d="M 40 185 C 140 185, 180 110, 220 100 C 260 90, 300 25, 380 25" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="330" y="45" font-size="12" fill="currentColor">F_X(x)</text>
  
  <!-- Empirical staircase CDF -->
  <path d="M 40 190 L 100 190 L 100 170 L 150 170 L 150 135 L 195 135 L 195 90 L 250 90 L 250 50 L 310 50 L 310 25 L 380 25" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3"/>
  <text x="130" y="155" font-size="12" fill="currentColor">F̂_X(x)</text>
  
  <!-- Max distance indicator Dn at x = 195 -->
  <line x1="195" y1="90" x2="195" y2="118" stroke="currentColor" stroke-width="2"/>
  <text x="205" y="110" font-size="12" fill="currentColor">D_n</text>
</svg>
<figcaption>The Kolmogorov-Smirnov test statistic $D_n$ is the maximum vertical discrepancy between the theoretical CDF $F_X(x)$ and the empirical staircase CDF $\hat{F}_X(x)$.</figcaption>
</figure>

Remarkably, when $F_X$ is continuous, the distribution of $D_n$ under $H_0$ does not depend on the specific underlying distribution $F_X$. For large $n$, its distribution is tabulated, with the asymptotic critical threshold for a $5\%$ significance level given by:
$$\mathbf{P}\left(\sqrt{n} D_n \ge 1.36; H_0\right) \approx 0.05 \implies \text{Reject } H_0 \text{ if } D_n > \frac{1.36}{\sqrt{n}}$$

---

## Methodological Cautions in Statistical Testing

While probability theory is a deductive, mathematical discipline founded on axioms, applied statistics demands sound experimental hygiene. Several widespread practices undermine statistical inference:

1. **Publication Bias:** Researchers testing drugs or interventions under the null hypothesis $H_0$ (that the treatment has no effect) typically submit papers only when $H_0$ is rejected. If hundreds of researchers evaluate ineffective treatments using a $5\%$ significance level, $5\%$ of these studies will reject $H_0$ purely by chance, flooding the literature with false discoveries.
2. **Multiple Testing:** Conducting $k$ independent tests each at level $\alpha = 0.05$ creates a probability of at least one false rejection of:
   $$1 - (1 - 0.05)^k$$
   For large $k$, this probability approaches $1$. Finding a "statistically significant" outlier among thousands of evaluated features is almost guaranteed by chance alone.
3. **Hypothesis Formulation After Seeing Data:** Statistical tests require specifying the hypothesis and the test statistic *before* collecting or examining data. Finding an unusual anomaly in a dataset and subsequently testing whether that specific anomaly is statistically significant invalidates standard error bounds.

Beyond binary and goodness-of-fit testing, the broader landscape of statistical inference includes:
- Nonparametric density estimation (histogram construction and smoothing kernels).
- Recursive, real-time signal estimation.
- Model selection (choosing optimal subsets of explanatory variables in linear regression).
- High-dimensional inference designed for vast parameter spaces and massive datasets.

---

## Exercises

### Exercise 1: Ambulance Response Time Distribution

An ambulance travels back and forth along a road segment of length $l$, represented by the interval $[0, l]$. 

1. An accident occurs at location $X$, where $X$ is uniformly distributed on $[0, l]$.
2. At the moment the accident occurs, the ambulance is at location $Y$, where $Y$ is uniformly distributed on $[0, l]$, independently of $X$.
3. The ambulance travels at a constant velocity $v > 0$. The travel time required to reach the scene of the accident is:
   $$T = \frac{|Y - X|}{v}$$

Determine the cumulative distribution function $F_T(t)$ and the probability density function $f_T(t)$ of the travel response time $T$ for all $t \in \mathbb{R}$.

---

## Sources

- **Lecture 25 Slides and Transcript:** Simple binary hypothesis testing; likelihood ratio formulation; tests on normal mean and variance; composite hypothesis testing (fair coin); chi-square goodness-of-fit for dice and continuous distributions; Kolmogorov-Smirnov test; broader topics in statistics; methodology critique ("Why Most Published Research Findings Are False", publication bias, post-hoc hypothesis testing).
- **Recitation/Problem Set Video (No 25 ch4 ambulance):** Derived distribution problem for ambulance travel time $T = |Y - X|/v$ on an interval of length $l$.
- *Omitted/Non-contained mentions:* General proofs of the Neyman-Pearson lemma (optimality of the LRT) and analytical derivations of the Kolmogorov-Smirnov limiting distribution, which were cited in lecture but deliberately not derived.

---

[← 24. Linear Regression and Hypothesis Testing](24-linear-regression-and-hypothesis-testing.md) · [Contents](index.md) · [26. Hypergeometric Probabilities →](26-hypergeometric-probabilities.md)
