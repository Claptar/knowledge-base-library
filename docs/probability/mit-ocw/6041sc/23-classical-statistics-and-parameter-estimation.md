---
title: "23. Classical Statistics and Parameter Estimation"
course: "MIT 6.041SC"
chapter: 23
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Classical Statistics and Parameter Estimation

## What this covers

This chapter introduces the classical (frequentist) framework for statistical inference, in which model parameters are treated as unknown fixed constants rather than random variables. It develops the maximum likelihood (ML) method for point estimation, formalizes desirable properties of estimators such as unbiasedness, consistency, and mean squared error, and details the construction and proper interpretation of confidence intervals.

## The Classical Framework

In Bayesian inference, unknown parameters are modeled as random variables $\Theta$ endowed with a prior distribution $p_\Theta(\theta)$. In contrast, classical statistics treats the unknown parameter $\theta$ as a deterministic, fixed constant. It is simply an unknown number.

Consequently, the observation model is written as:

$$p_X(x; \theta) \quad \text{or, for multiple observations,} \quad p_{X_1, \dots, X_n}(x_1, \dots, x_n; \theta_1, \dots, \theta_m)$$

The semicolon emphasizes that $p_X(x; \theta)$ is **not** a conditional probability distribution in the mathematical sense. Conditional probabilities are defined only between random variables. Here, $\theta$ is not random. Mathematically, classical statistics considers a family of alternative candidate probabilistic models—one model for each possible value of $\theta$—and attempts to decide which model generated the observed data.

Classical statistical problems broadly fall into two categories:

1. **Hypothesis Testing:** Deciding among discrete models. This may involve simple hypotheses:
   $$H_0 : \theta = 1/2 \quad \text{versus} \quad H_1 : \theta = 3/4$$
   or composite hypotheses where one or both hypotheses contain a continuous range of candidate models:
   $$H_0 : \theta = 1/2 \quad \text{versus} \quad H_1 : \theta \neq 1/2$$
2. **Estimation:** Constructing an estimator $\hat{\Theta}$, which is a function of the random observations, designed to produce an estimate close to the true value $\theta$ while keeping estimation error $\hat{\Theta} - \theta$ small.

## Maximum Likelihood Estimation

The primary general-purpose method for parameter estimation in classical statistics is the **Maximum Likelihood (ML)** method. Given an observation $x$, we select the parameter value $\theta$ that makes the observed data most likely to have occurred:

$$\hat{\theta}_{\text{ML}} = \arg\max_\theta p_X(x; \theta)$$

When the observations are continuous random variables, the probability mass function $p_X(x; \theta)$ is replaced by the joint probability density function $f_X(x; \theta)$.

It is instructive to compare the ML estimator with the Bayesian Maximum A Posteriori (MAP) estimator:

$$\hat{\theta}_{\text{MAP}} = \arg\max_\theta p_{\Theta|X}(\theta \mid x) = \arg\max_\theta \frac{p_{X|\Theta}(x \mid \theta) p_\Theta(\theta)}{p_X(x)}$$

In the MAP formulation, the denominator $p_X(x)$ does not depend on $\theta$ and can be ignored during maximization. If the prior $p_\Theta(\theta)$ is uniform (a constant over all candidate values of $\theta$), the MAP criterion reduces entirely to maximizing $p_{X|\Theta}(x \mid \theta)$. Thus, maximum likelihood estimation is mathematically equivalent to Bayesian MAP estimation under a uniform, uninformative prior.

### Example: i.i.d. Exponential Observations

Let $X_1, \dots, X_n$ be independent and identically distributed (i.i.d.) random variables following an exponential distribution with unknown parameter $\theta > 0$:

$$f_X(x_i; \theta) = \theta e^{-\theta x_i}, \quad x_i \geq 0$$

Because the observations are independent, their joint density is the product of the marginal densities:

$$f_{X_1, \dots, X_n}(x_1, \dots, x_n; \theta) = \prod_{i=1}^n \theta e^{-\theta x_i} = \theta^n \exp\left(-\theta \sum_{i=1}^n x_i\right)$$

To find the maximizing $\theta$, take the natural logarithm (the log-likelihood function):

$$\ln f_{X_1, \dots, X_n}(x_1, \dots, x_n; \theta) = n \ln \theta - \theta \sum_{i=1}^n x_i$$

Differentiating with respect to $\theta$ and setting the derivative to zero:

$$\frac{d}{d\theta}\left( n \ln \theta - \theta \sum_{i=1}^n x_i \right) = \frac{n}{\theta} - \sum_{i=1}^n x_i = 0$$

Solving for $\theta$ yields the maximum likelihood estimate:

$$\hat{\theta}_{\text{ML}} = \frac{n}{\sum_{i=1}^n x_i}$$

Before numerical values are substituted, the estimation rule is an **estimator**—a random variable denoted with an uppercase letter:

$$\hat{\Theta}_n = \frac{n}{X_1 + \dots + X_n}$$

Because $\mathbf{E}[X_i] = 1/\theta$ for an exponential distribution, the estimator $\hat{\Theta}_n$ is the reciprocal of the sample mean, which is an intuitively appealing choice.

## Desirable Properties of Estimators

An estimator $\hat{\Theta}_n = g(X_1, \dots, X_n)$ is a function of random data and is therefore itself a random variable. Its distribution depends on the true parameter $\theta$. A sound estimator should satisfy desirable statistical criteria **for all possible values of $\theta$**.

### 1. Unbiasedness

An estimator is **unbiased** if its expected value equals the true parameter value, regardless of what $\theta$ is:

$$\mathbf{E}_\theta[\hat{\Theta}_n] = \theta \quad \text{for all } \theta$$

The subscript $\theta$ serves as a reminder that the expectation is taken with respect to the probability distribution governed by the true parameter value $\theta$. 

ML estimators are not guaranteed to be unbiased. In the exponential example with a single observation ($n = 1$):

$$\hat{\Theta}_1 = \frac{1}{X_1}$$

The expectation is:

$$\mathbf{E}\left[\frac{1}{X_1}\right] = \int_0^\infty \frac{1}{x_1} \theta e^{-\theta x_1} \, dx_1 = \infty$$

Because $\infty \neq \theta$, the estimator is heavily biased upward.

### 2. Consistency

An estimator is **consistent** if it converges in probability to the true parameter as the sample size $n$ approaches infinity:

$$\hat{\Theta}_n \xrightarrow{p} \theta \quad \text{as } n \to \infty, \quad \text{for all } \theta$$

For the exponential estimator, the Weak Law of Large Numbers (WLLN) guarantees that the sample mean converges in probability to the true mean:

$$\frac{X_1 + \dots + X_n}{n} \xrightarrow{p} \mathbf{E}[X] = \frac{1}{\theta}$$

Continuous functions preserve convergence in probability. Taking the reciprocal gives:

$$\hat{\Theta}_n = \frac{n}{X_1 + \dots + X_n} \xrightarrow{p} \theta$$

Thus, although $\hat{\Theta}_n$ is biased for finite $n$, it is consistent.

### 3. Mean Squared Error (MSE)

A quantitative measure of estimator quality is the Mean Squared Error:

$$\text{MSE}(\hat{\Theta}) = \mathbf{E}\left[(\hat{\Theta} - \theta)^2\right]$$

Expanding this expectation shows that the MSE decomposes into variance and bias:

$$\begin{aligned}
\mathbf{E}\left[(\hat{\Theta} - \theta)^2\right] &= \mathbf{E}\left[\left( (\hat{\Theta} - \mathbf{E}[\hat{\Theta}]) + (\mathbf{E}[\hat{\Theta}] - \theta) \right)^2\right] \\
&= \mathbf{E}\left[(\hat{\Theta} - \mathbf{E}[\hat{\Theta}])^2\right] + 2(\mathbf{E}[\hat{\Theta}] - \theta)\mathbf{E}[\hat{\Theta} - \mathbf{E}[\hat{\Theta}]] + (\mathbf{E}[\hat{\Theta}] - \theta)^2 \\
&= \text{var}(\hat{\Theta}) + (\text{bias})^2
\end{aligned}$$

A trivial estimator that ignores the data entirely and always reports a constant, such as $\hat{\Theta} = 100$, has $\text{var}(\hat{\Theta}) = 0$. However, its bias squared $(100 - \theta)^2$ can be arbitrarily large. Good estimators balance this trade-off to keep both variance and bias small across all candidate values of $\theta$.

## Estimating a Population Mean

Consider i.i.d. observations $X_1, \dots, X_n$ with unknown mean $\mathbf{E}[X_i] = \theta$ and variance $\text{var}(X_i) = \sigma^2$. This observation model can be written as:

$$X_i = \theta + W_i$$

where $W_i$ are i.i.d. noise terms with $\mathbf{E}[W_i] = 0$ and $\text{var}(W_i) = \sigma^2$.

The standard estimator for $\theta$ is the sample mean:

$$\hat{\Theta}_n = M_n = \frac{X_1 + \dots + X_n}{n}$$

The sample mean exhibits ideal baseline properties:
- **Unbiased:** $\mathbf{E}[\hat{\Theta}_n] = \frac{1}{n}\sum_{i=1}^n \mathbf{E}[X_i] = \theta$.
- **Consistent:** By the Weak Law of Large Numbers, $\hat{\Theta}_n \xrightarrow{p} \theta$.
- **Mean Squared Error:** Since the estimator is unbiased, $\text{MSE} = \text{var}(\hat{\Theta}_n) = \frac{\sigma^2}{n} \to 0$.

When the underlying observations are normally distributed, $X_i \sim N(\theta, \sigma^2)$, the sample mean is identical to the maximum likelihood estimator.

## Confidence Intervals

A point estimate $\hat{\theta}_n$ does not convey the degree of uncertainty in the measurement. To quantify reliability, classical statistics constructs an interval around the estimate.

A **$1 - \alpha$ confidence interval** is a random interval $[\hat{\Theta}_n^-, \hat{\Theta}_n^+]$ such that:

$$\mathbf{P}(\hat{\Theta}_n^- \leq \theta \leq \hat{\Theta}_n^+) \geq 1 - \alpha, \quad \text{for all } \theta$$

Common choices for $\alpha$ are $0.05$ (a $95\%$ confidence interval) and $0.01$ (a $99\%$ confidence interval).

### Interpretation of Confidence Intervals

The interpretation of a confidence interval requires precision. Suppose an experiment yields numerical endpoints $[1.97, 2.56]$. It is incorrect to state:

$$\text{"With probability } 0.95\text{, the parameter } \theta \text{ lies between } 1.97 \text{ and } 2.56\text{."}$$

In the classical view, $\theta$ is a deterministic constant. The numbers $1.97$ and $2.56$ are also fixed constants. There is no randomness remaining: $\theta$ either lies in $[1.97, 2.56]$ or it does not.

The probability statement applies to the **random interval** $[\hat{\Theta}_n^-, \hat{\Theta}_n^+]$ before data collection:

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Repeated realization of confidence intervals showing coverage of a fixed true parameter">
  <!-- Parameter line -->
  <line x1="210" y1="20" x2="210" y2="155" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="210" y="170" text-anchor="middle" font-size="12" fill="currentColor">&#952; (true parameter)</text>

  <!-- Realization 1 (covers) -->
  <line x1="160" y1="40" x2="250" y2="40" stroke="currentColor" stroke-width="2"/>
  <circle cx="205" cy="40" r="3" fill="currentColor"/>
  <text x="50" y="44" font-size="11" fill="currentColor">Trial 1</text>

  <!-- Realization 2 (covers) -->
  <line x1="180" y1="70" x2="270" y2="70" stroke="currentColor" stroke-width="2"/>
  <circle cx="225" cy="70" r="3" fill="currentColor"/>
  <text x="50" y="74" font-size="11" fill="currentColor">Trial 2</text>

  <!-- Realization 3 (misses) -->
  <line x1="225" y1="100" x2="315" y2="100" stroke="currentColor" stroke-width="2"/>
  <circle cx="270" cy="100" r="3" fill="currentColor"/>
  <text x="50" y="104" font-size="11" fill="currentColor">Trial 3</text>

  <!-- Realization 4 (covers) -->
  <line x1="150" y1="130" x2="235" y2="130" stroke="currentColor" stroke-width="2"/>
  <circle cx="192" cy="130" r="3" fill="currentColor"/>
  <text x="50" y="134" font-size="11" fill="currentColor">Trial 4</text>
</svg>
<figcaption>Confidence intervals vary randomly across repeated experiments. A 95% confidence interval procedure guarantees that 95% of realized intervals will cover the fixed parameter $\theta$.</figcaption>
</figure>

The proper interpretation is: if we repeat the experiment many times under identical conditions, generating a new interval each time, approximately $100(1 - \alpha)\%$ of those calculated intervals will contain the true parameter $\theta$.

### Constructing the Interval for the Mean

By the Central Limit Theorem (CLT), the standardized sample mean converges in distribution to a standard normal random variable:

$$\frac{\hat{\Theta}_n - \theta}{\sigma / \sqrt{n}} \approx N(0, 1)$$

Let $z$ be the standard normal cutoff value satisfying $\Phi(z) = 1 - \alpha/2$, where $\Phi$ is the standard normal cumulative distribution function. For $\alpha = 0.05$, $z = 1.96$:

$$\mathbf{P}\left(-z \leq \frac{\hat{\Theta}_n - \theta}{\sigma / \sqrt{n}} \leq z\right) \approx 1 - \alpha$$

Rearranging the inequalities:

$$\mathbf{P}\left(\hat{\Theta}_n - z\frac{\sigma}{\sqrt{n}} \leq \theta \leq \hat{\Theta}_n + z\frac{\sigma}{\sqrt{n}}\right) \approx 1 - \alpha$$

The resulting $1 - \alpha$ confidence interval has random endpoints:

$$\hat{\Theta}_n^- = \hat{\Theta}_n - z\frac{\sigma}{\sqrt{n}}, \quad \hat{\Theta}_n^+ = \hat{\Theta}_n + z\frac{\sigma}{\sqrt{n}}$$

The interval width decreases as the sample size $n$ increases (more data reduces uncertainty) or as $\sigma$ decreases (higher measurement precision reduces uncertainty).

## Dealing with Unknown Variance

Computing the endpoints requires the standard deviation $\sigma$. In practice, $\sigma$ is rarely known. Three main approaches resolve this issue:

### Option 1: Upper Bound on Variance

If an analytical bound on $\sigma$ is known, we substitute this conservative bound into the interval formula. For example, if $X_i \sim \text{Bernoulli}(\theta)$, the variance is $\theta(1 - \theta)$. The maximum variance occurs at $\theta = 1/2$, yielding $\sigma^2 \leq 1/4$, or $\sigma \leq 1/2$. Using $\sigma = 1/2$ produces a wider interval whose coverage probability is guaranteed to be at least $1 - \alpha$.

### Option 2: Ad Hoc Variance Estimate

For distributions where the variance is an explicit function of the mean, we can plug in the estimated mean. For Bernoulli trials with unknown success parameter $\theta$:

$$\hat{\sigma} = \sqrt{\hat{\Theta}_n(1 - \hat{\Theta}_n)}$$

By the law of large numbers, $\hat{\Theta}_n \xrightarrow{p} \theta$, so $\hat{\sigma} \xrightarrow{p} \sigma$.

### Option 3: Sample Variance

When no specific distribution is assumed, the variance $\sigma^2 = \mathbf{E}[(X_i - \theta)^2]$ must be estimated directly from the data. If $\theta$ were known, the natural estimator would be:

$$\hat{\sigma}_n^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \theta)^2$$

Because $\theta$ is unknown, we substitute the sample mean $\hat{\Theta}_n$. To make the estimator unbiased, we normalize by $n - 1$ instead of $n$:

$$\hat{S}_n^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \hat{\Theta}_n)^2$$

This sample variance estimator is unbiased:

$$\mathbf{E}[\hat{S}_n^2] = \sigma^2$$

and consistent, $\hat{S}_n^2 \xrightarrow{p} \sigma^2$. The estimated standard deviation $\hat{S}_n = \sqrt{\hat{S}_n^2}$ is plugged directly into the confidence interval bounds:

$$\left[ \hat{\Theta}_n - z\frac{\hat{S}_n}{\sqrt{n}}, \; \hat{\Theta}_n + z\frac{\hat{S}_n}{\sqrt{n}} \right]$$

This confidence interval relies on two levels of approximation: approximating the distribution of the sample mean via the Central Limit Theorem, and approximating the true standard deviation $\sigma$ with an estimate.

## Exercises

1. Juliet will be late on any date with Romeo by a random amount of time $X$, uniformly distributed over the interval $[0, \theta]$, where $\theta$ is an unknown parameter. Assuming that Juliet was late by an amount $x$ on their first date, find the maximum likelihood estimate of $\theta$ based on the single observation $X = x$.

2. Consider $n$ independent observations $X_1, \dots, X_n$ drawn from a normal distribution with unknown mean $\mu$ and unknown variance $v = \sigma^2$. Derive the maximum likelihood estimates for both $\mu$ and $v$.

3. A survey is conducted to estimate the fraction $\theta$ of voters supporting a candidate. Out of $n = 1200$ independently sampled voters in North Carolina, $k = 684$ support the candidate. The responses are modeled as i.i.d. Bernoulli random variables $X_1, \dots, X_n$ with parameter $\theta$. 
   Construct an approximate $95\%$ confidence interval for $\theta$ using the standard normal approximation cutoff $z = 1.96$ under each of the following three methods for determining the unknown standard deviation $\sigma = \sqrt{\text{var}(X_i)}$:
   (a) Using the sample variance estimator:
   $$\hat{S}_n^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \hat{\Theta}_n)^2$$
   (b) Using the ad hoc estimate derived from the sample mean:
   $$\hat{\sigma}^2 = \hat{\Theta}_n(1 - \hat{\Theta}_n)$$
   (c) Using the most conservative upper bound for the variance of a Bernoulli random variable.

## Sources

- Slides and lecture transcript for Lecture 23 ("Classical statistics", "Maximum likelihood estimation", "Estimating a sample mean", "Confidence intervals").
- Problem set selections adapted from Recitation 23 (Fall 2010), covering textbook Examples 9.1, 9.4, and 9.8.
- $t$-based confidence intervals from the textbook readings were excluded per the lecture slide instructions.

---

[← 22. Least Mean Squares Estimation](22-least-mean-squares-estimation.md) · [Contents](index.md) · [24. Linear Regression and Hypothesis Testing →](24-linear-regression-and-hypothesis-testing.md)
