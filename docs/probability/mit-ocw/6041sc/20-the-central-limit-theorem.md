---
title: "20. The Central Limit Theorem"
course: "MIT 6.041SC"
chapter: 20
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. The Central Limit Theorem

## What this covers

This chapter covers the Central Limit Theorem (CLT), which establishes that the standardized sum of independent and identically distributed random variables converges in distribution to a standard normal random variable. We examine what the theorem states, how to use it as an accurate computational shortcut, the continuity correction for discrete distributions, and the difference between normal and Poisson approximations. It assumes familiarity with the Law of Large Numbers, expectation, variance, and the standard normal distribution.

## The Central Limit Theorem

Let $X_1, X_2, \dots, X_n$ be independent, identically distributed (i.i.d.) random variables, each with finite mean $\mu = \text{E}[X_i]$ and finite variance $\sigma^2 = \text{var}(X_i)$. Consider their sum:
$$S_n = X_1 + X_2 + \dots + X_n$$

By linearity of expectation and independence, the sum has:
$$\text{E}[S_n] = n\mu, \qquad \text{var}(S_n) = n\sigma^2, \qquad \sigma_{S_n} = \sqrt{n}\sigma$$

As $n \to \infty$, the variance of $S_n$ grows without bound, meaning the distribution spreads out across the entire real line and does not settle into a limiting distribution. To observe a meaningful limit, we must standardize $S_n$ by subtracting its mean and dividing by its standard deviation:
$$Z_n = \frac{S_n - \text{E}[S_n]}{\sigma_{S_n}} = \frac{S_n - n\mu}{\sqrt{n}\sigma}$$

By construction, $Z_n$ is centered and scaled:
$$\text{E}[Z_n] = 0, \qquad \text{var}(Z_n) = 1$$

No matter how large $n$ becomes, the mean remains at $0$ and the width of the distribution remains stable. The Central Limit Theorem asserts that the shape of this distribution settles into the standard normal distribution.

**Theorem (Central Limit Theorem):** For every real number $c$,
$$\lim_{n \to \infty} \text{P}(Z_n \le c) = \text{P}(Z \le c) = \Phi(c)$$
where $Z \sim \mathcal{N}(0, 1)$ is a standard normal random variable, and $\Phi(c)$ is its cumulative distribution function (CDF), tabulated in standard normal tables.

### Understanding the Theorem's Scope

Several aspects of the theorem warrant careful attention:

1. **Universality:** The theorem requires only that the underlying $X_i$ be independent, identically distributed, and possess a finite mean and variance. The specific form of their common distribution does not matter; only $\mu$ and $\sigma$ are needed.
2. **Convergence of CDFs, Not PMFs or PDFs:** The CLT guarantees convergence of the cumulative distribution function $\text{P}(Z_n \le c)$. It does *not* assert that the probability mass function (PMF) or probability density function (PDF) of $Z_n$ converges to the normal bell curve. For discrete random variables, the sum $S_n$ remains discrete for all $n$, having isolated spikes rather than a smooth density, yet its step-like CDF approaches the smooth curve $\Phi(c)$.
3. **The Practical Approximation:** In practice, we treat $Z_n$ as standard normal. Because $S_n = \sqrt{n}\sigma Z_n + n\mu$ is an affine function of $Z_n$, we equivalently treat the unstandardized sum $S_n$ as approximately normal:
   $$S_n \approx \mathcal{N}(n\mu, n\sigma^2)$$

### Applicability for Moderate $n$

Although the theorem is asymptotic, it serves as an accurate approximation even for moderate values of $n$, often as small as $20$ to $30$. 

The speed of convergence depends heavily on the symmetry of the underlying distribution:
- If the distribution of $X_i$ is symmetric around its mean (such as a discrete uniform distribution), the sum becomes bell-shaped very rapidly (e.g., $n = 4$ or $n = 8$).
- If the distribution of $X_i$ is heavily skewed (such as a geometric distribution), the sum exhibits asymmetry in the tails for small $n$, requiring larger sample sizes ($n \ge 30$) before the normal approximation becomes accurate.

Historically and philosophically, the CLT provides the foundational justification for normal models in science and engineering. When an observed physical phenomenon (such as Brownian motion, where a suspended particle experiences billions of independent collisions from surrounding molecules) is the aggregate of many small, independent random shocks, the resulting displacement is approximately normal.

## Application: The Pollster's Problem

Recall the polling problem: a pollster wishes to estimate the unknown fraction $f \in (0, 1)$ of a population that holds a particular opinion. We draw $n$ individuals uniformly and independently at random, defining:
$$X_i = \begin{cases} 1, & \text{if person } i \text{ responds yes,} \\ 0, & \text{if person } i \text{ responds no.} \end{cases}$$

Here, $\text{E}[X_i] = f$ and $\sigma^2 = \text{var}(X_i) = f(1-f)$. The sample mean is:
$$M_n = \frac{S_n}{n} = \frac{X_1 + \dots + X_n}{n}$$

Suppose the polling specifications require that the estimate falls within $0.01$ of the true fraction with at least $95\%$ confidence:
$$\text{P}(|M_n - f| \ge 0.01) \le 0.05$$

### Transforming to Standard Form

We express the event of interest in terms of the standardized variable $Z_n$:
$$|M_n - f| \ge 0.01 \iff \left| \frac{S_n - nf}{n} \right| \ge 0.01 \iff \left| \frac{S_n - nf}{\sqrt{n}\sigma} \right| \ge \frac{0.01\sqrt{n}}{\sigma}$$

The quantity on the left is $|Z_n|$. Using the normal approximation:
$$\text{P}(|M_n - f| \ge 0.01) \approx \text{P}\left(|Z| \ge \frac{0.01\sqrt{n}}{\sigma}\right)$$

Because $f$ is unknown, the exact variance $\sigma^2 = f(1-f)$ is also unknown. However, the product $f(1-f)$ attains its maximum value at $f = 1/2$:
$$\sigma = \sqrt{f(1-f)} \le \sqrt{\frac{1}{2}\cdot\frac{1}{2}} = \frac{1}{2}$$

Since $\sigma \le 1/2$, we have:
$$\frac{0.01\sqrt{n}}{\sigma} \ge \frac{0.01\sqrt{n}}{0.5} = 0.02\sqrt{n}$$

A larger threshold corresponds to a smaller tail probability:
$$\text{P}\left(|Z| \ge \frac{0.01\sqrt{n}}{\sigma}\right) \le \text{P}(|Z| \ge 0.02\sqrt{n})$$

To guarantee our error requirement, it suffices to choose $n$ such that:
$$\text{P}(|Z| \ge 0.02\sqrt{n}) \le 0.05$$

### Evaluating Sample Sizes

By symmetry of the standard normal distribution:
$$\text{P}(|Z| \ge c) = 2\text{P}(Z \ge c) = 2(1 - \Phi(c))$$

If we test $n = 10{,}000$:
$$0.02\sqrt{10{,}000} = 0.02 \times 100 = 2$$
$$\text{P}(|Z| \ge 2) = 2(1 - \Phi(2)) = 2(1 - 0.9772) = 0.0456$$
This yields an error rate of $4.56\%$, which satisfies the $\le 0.05$ requirement.

To determine the minimal sample size necessary to achieve an error rate of exactly $0.05$, we solve backward:
$$\text{P}(|Z| \ge c) = 0.05 \implies 1 - \Phi(c) = 0.025 \implies \Phi(c) = 0.975$$

Looking up $0.975$ in the standard normal table yields $c = 1.96$. Setting $0.02\sqrt{n} = 1.96$:
$$\sqrt{n} = \frac{1.96}{0.02} = 98 \implies n = (98)^2 = 9{,}604$$
Thus, a sample size of $n = 9{,}604$ satisfies the polling specification under the Central Limit Theorem.

## Normal Approximation to the Binomial and the Continuity Correction

Let $S_n \sim \text{Binomial}(n, p)$, representing the sum of $n$ independent $\text{Bernoulli}(p)$ trials. Here, $\text{E}[S_n] = np$ and $\sigma = \sqrt{np(1-p)}$. According to the CLT:
$$\frac{S_n - np}{\sqrt{np(1-p)}} \xrightarrow{d} \mathcal{N}(0, 1)$$

Consider $n = 36$ and $p = 0.5$. The mean and standard deviation are:
$$\mu = 36(0.5) = 18, \qquad \sigma = \sqrt{36(0.5)(0.5)} = \sqrt{9} = 3$$

Suppose we wish to find $\text{P}(S_n \le 21)$. The exact binomial probability is:
$$\sum_{k=0}^{21} \binom{36}{k} \left(\frac{1}{2}\right)^{36} \approx 0.8785$$

### Standard Application

Applying the normal approximation directly:
$$\text{P}(S_n \le 21) = \text{P}\left(\frac{S_n - 18}{3} \le \frac{21 - 18}{3}\right) \approx \text{P}(Z \le 1) = \Phi(1) \approx 0.8413$$
While close, this misses the exact probability by more than $0.03$.

### The Half-Correction

The discrepancy arises because $S_n$ is discrete, while $Z$ is continuous. For an integer-valued random variable, the events:
$$\{S_n \le 21\}, \qquad \{S_n < 22\}, \qquad \{S_n \le 21.5\}$$
are identical. However, when integrated under a continuous Gaussian curve, these boundaries yield different areas:
- Integrating up to $21$ omits the upper half of the probability mass bar at $k = 21$.
- Integrating up to $22$ includes the entire mass bar at $k = 21$ plus the lower half of the bar at $k = 22$.

Splitting the difference by evaluating at $21.5$ assigns the probability mass of the integer $k$ to the interval $[k - 0.5, k + 0.5]$.

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Continuity correction assigning interval from 18.5 to 19.5 to integer 19">
  <line x1="30" y1="150" x2="390" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <rect x="185" y="60" width="50" height="90" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <line x1="210" y1="150" x2="210" y2="60" stroke="currentColor" stroke-width="2"/>
  <path d="M 50 148 C 120 145 160 110 210 50 C 260 110 300 145 370 148" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="185" y1="150" x2="185" y2="156" stroke="currentColor" stroke-width="1"/>
  <line x1="210" y1="150" x2="210" y2="156" stroke="currentColor" stroke-width="1"/>
  <line x1="235" y1="150" x2="235" y2="156" stroke="currentColor" stroke-width="1"/>
  <text x="185" y="170" text-anchor="middle" font-size="12" fill="currentColor">18.5</text>
  <text x="210" y="170" text-anchor="middle" font-size="12" fill="currentColor">19</text>
  <text x="235" y="170" text-anchor="middle" font-size="12" fill="currentColor">19.5</text>
</svg>
<figcaption>The continuity correction attributes the area under the normal density curve between 18.5 and 19.5 to the discrete probability mass at 19.</figcaption>
</figure>

Applying the $1/2$ continuity correction:
$$\text{P}(S_n \le 21.5) = \text{P}\left(\frac{S_n - 18}{3} \le \frac{21.5 - 18}{3}\right) = \text{P}(Z_n \le 1.17)$$
Looking up $\Phi(1.17)$ in the normal tables:
$$\Phi(1.17) \approx 0.8790$$
This matches the exact value ($0.8785$) to three decimal places.

## The De Moivre–Laplace CLT: Approximating the PMF

The continuity correction also enables the approximation of individual probabilities $\text{P}(S_n = k)$ for a binomial variable, a historical precursor to the modern CLT established by De Moivre and Laplace. 

Because the probability of a continuous variable taking any single point value is zero ($\text{P}(Z = c) = 0$), we associate the integer $k$ with the interval $[k - 0.5, k + 0.5]$:
$$\text{P}(S_n = k) = \text{P}(k - 0.5 \le S_n \le k + 0.5)$$

### Example

Let $n = 36$ and $p = 0.5$. To estimate $\text{P}(S_n = 19)$:
$$18.5 \le S_n \le 19.5 \iff \frac{18.5 - 18}{3} \le \frac{S_n - 18}{3} \le \frac{19.5 - 18}{3} \iff 0.17 \le Z_n \le 0.50$$

Using the normal distribution:
$$\begin{aligned}
\text{P}(S_n = 19) &\approx \text{P}(0.17 \le Z \le 0.50) \\
&= \Phi(0.50) - \Phi(0.17) \\
&= 0.6915 - 0.5675 \\
&= 0.1240
\end{aligned}$$

The exact value computed from the binomial PMF is:
$$\binom{36}{19} \left(\frac{1}{2}\right)^{36} \approx 0.1251$$
The approximation provides high precision with minimal computation.

## Asymptotic Regimes: Normal vs. Poisson Approximation

Consider the following puzzle: let $X$ be the number of arrivals in a Poisson process of rate $\lambda = 1$ over the unit interval $[0, 1]$. Partition $[0, 1]$ into $n$ subintervals of length $1/n$. The total number of arrivals is:
$$X = \sum_{i=1}^n X_i$$
where $X_i$ is the number of arrivals in subinterval $i$. The random variables $X_i$ are independent, identically distributed, and have finite mean and variance. As $n \to \infty$, does the Central Limit Theorem imply that $X$ is normally distributed?

The answer is no, because $X$ is Poisson with mean $1$. 

The fallacy lies in an implicit assumption of the Central Limit Theorem: the underlying distribution of the terms being summed must remain **fixed** as $n$ increases. In the partition argument, each $X_i$ has mean $\text{E}[X_i] = 1/n$ and variance $\text{var}(X_i) = 1/n$. As $n$ changes, the distribution of each component $X_i$ changes simultaneously.

This distinction defines the boundary between the Poisson and normal approximations for a binomial distribution $\text{Binomial}(n, p)$:

1. **Normal Approximation Regime (CLT):**
   The success probability $p$ is fixed while $n \to \infty$. Here, $np \to \infty$ and $n(1-p) \to \infty$. The sum comprises many terms from a fixed Bernoulli distribution, and its CDF approaches a normal distribution.
2. **Poisson Approximation Regime:**
   The product $\lambda = np$ is kept fixed while $n \to \infty$ and $p \to 0$. Here, we sum an increasing number of exceedingly rare events. The distribution converges to a Poisson distribution with parameter $\lambda$.

### Practical Rule of Thumb
When given concrete numerical parameters $n$ and $p$:
- If $p$ is small and $n$ is large such that $np$ is moderate (e.g., $p = 0.01, n = 100 \implies np = 1$), use the **Poisson approximation**.
- If $n$ is large and $np$ is comfortably away from zero (e.g., $p = 0.1, n = 500 \implies np = 50$, or generally $np \ge 10$), use the **normal approximation**.

## Exercises

### Exercise 1: Quality Control of Lightbulbs
In a manufacturing plant, you are tasked with estimating the probability $p$ that a produced lightbulb is defectless. Assume all lightbulbs have the same probability of having a defect, and defects across different lightbulbs are independent.
1. Suppose you test $n$ randomly selected bulbs. Propose an estimator $Z_n$ for $p$ such that $Z_n$ converges to $p$ in probability.
2. If you test $n = 50$ lightbulbs, use the Central Limit Theorem to find the probability that your estimate falls in the range $p \pm 0.1$.
3. How many lightbulbs must you test to ensure that the estimate falls within $p \pm 0.1$ with probability at least $0.95$?

### Exercise 2: Modes of Convergence
Consider two sequences of discrete random variables, $X_n$ and $Y_n$, with probability mass functions:
$$p_{X_n}(x) = \begin{cases} 1 - \frac{1}{n}, & x = 0, \\ \frac{1}{n}, & x = 1, \end{cases} \qquad p_{Y_n}(y) = \begin{cases} 1 - \frac{1}{n}, & y = 0, \\ \frac{1}{n}, & y = n. \end{cases}$$

1. Find the expected value and variance of $X_n$ and $Y_n$ as functions of $n$.
2. What does Chebyshev's inequality imply about the convergence of $X_n$ and $Y_n$?
3. Does $Y_n$ converge in probability to any value?
4. If a sequence of random variables $W_n$ converges in probability to a constant $a$, does $\lim_{n \to \infty} \text{E}[W_n] = a$? Prove or provide a counterexample using the variables defined above.
5. A sequence $W_n$ converges in the mean square to a constant $c$ if $\lim_{n \to \infty} \text{E}[(W_n - c)^2] = 0$. Use Markov's inequality to show that convergence in the mean square implies convergence in probability.
6. Show that convergence in probability does not necessarily imply convergence in the mean square.

### Exercise 3: Convergence of Scaled Uniform Sequences
Let $X$ be uniformly distributed on the interval $[-1, 1]$, and let $X_1, X_2, \dots$ be a sequence of independent and identically distributed random variables with the same distribution as $X$. Determine whether each of the following sequences converges in probability as $i \to \infty$. State the limit when it exists:
1. $X_i$
2. $Y_i = \frac{X_i}{i}$
3. $Z_i = (X_i)^i$

## Sources

- Slides and lecture notes: Lecture 20, "The Central Limit Theorem," MIT 6.041SC Fall 2013.
- Lecture transcript: Lecture 20, covering standardization, interpretation of convergence of CDFs vs. PMFs, the pollster problem, continuity correction, De Moivre–Laplace theorem, and normal vs. Poisson limits.
- Problem material: Recitation 20 slides and video transcripts for problems on lightbulb polling estimation, modes of convergence ($X_n, Y_n$, mean square convergence), and convergence in probability of uniform random sequences.

Solutions: [chapter 20](solutions/20-the-central-limit-theorem.md)


---

[← 19. Limit Theorems and Sample Means](19-limit-theorems-and-sample-means.md) · [Contents](index.md) · [21. Introduction to Bayesian Inference →](21-introduction-to-bayesian-inference.md)
