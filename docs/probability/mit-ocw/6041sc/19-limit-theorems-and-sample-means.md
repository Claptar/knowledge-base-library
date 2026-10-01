---
title: "19. Limit Theorems and Sample Means"
course: "MIT 6.041SC"
chapter: 19
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Limit Theorems and Sample Means

## What this covers

This chapter addresses how averages and sums of independent, identically distributed random variables behave as the sample size grows without bound. We establish Markov's and Chebyshev's inequalities, define the notion of convergence in probability, and use them to prove the Weak Law of Large Numbers. Finally, we analyze sample size requirements in polling and preview the Central Limit Theorem.

## The Motivation for Limit Theorems

Suppose you wish to determine the average height of a penguin population at the South Pole. If you pick a penguin uniformly at random from the population, its height is a random variable $X$ whose expected value $\mathbf{E}[X] = \mu$ equals the true population average. Measuring every single penguin is practically impossible. Instead, you collect a sample of $n$ penguins, measure their heights $X_1, X_2, \dots, X_n$, and form the **sample mean**:

$$M_n = \frac{X_1 + X_2 + \dots + X_n}{n}$$

It is essential to distinguish between the two kinds of means appearing here:
* The **expected value** $\mu$ is a deterministic number—the average over the entire population (or an idealized infinite sequence of identical expeditions).
* The **sample mean** $M_n$ is a random variable—its value fluctuates depending on which specific sample of $n$ penguins was gathered during a single expedition.

Intuitively, as the sample size $n$ tends to infinity, the random estimate $M_n$ should settle down close to the true numerical parameter $\mu$. Limit theorems make this intuition mathematically rigorous. Beyond reassuring practitioners who perform statistical sampling, limit theorems provide powerful approximations: while computing exact distributions of sums of tens or hundreds of random variables via convolutions is computationally intractable, asymptotic limits yield simple, universal approximations.

## Markov and Chebyshev Inequalities

To establish limit theorems, we require tools that relate the tail probabilities of a random variable to its expectations.

### Markov's Inequality

Let $X$ be a non-negative random variable ($X \ge 0$). For any positive constant $a > 0$, the probability that $X$ exceeds $a$ is constrained by its expected value. For a discrete random variable with PMF $p_X(x)$:

$$\mathbf{E}[X] = \sum_x x \, p_X(x) \ge \sum_{x \ge a} x \, p_X(x)$$

The inequality holds because every term in the omitted sum ($x < a$) is non-negative. For all values retained in the second summation, $x \ge a$. Replacing $x$ with $a$ gives:

$$\mathbf{E}[X] \ge \sum_{x \ge a} a \, p_X(x) = a \sum_{x \ge a} p_X(x) = a \, \mathbf{P}(X \ge a)$$

Dividing both sides by $a$ yields **Markov's inequality**:

$$\mathbf{P}(X \ge a) \le \frac{\mathbf{E}[X]}{a}, \quad \text{for all } a > 0$$

If the expected value of a non-negative random variable is small, the probability that it takes a large value must also be small.

### Chebyshev's Inequality

Chebyshev's inequality bounds how far a random variable $X$ (with finite mean $\mu$ and variance $\sigma^2$) can deviate from its mean. Consider the non-negative random variable $(X - \mu)^2$. Applying Markov's inequality to $(X - \mu)^2$ with threshold $c^2 > 0$:

$$\mathbf{P}\big((X - \mu)^2 \ge c^2\big) \le \frac{\mathbf{E}[(X - \mu)^2]}{c^2} = \frac{\sigma^2}{c^2}$$

Because $(X - \mu)^2 \ge c^2$ is equivalent to $|X - \mu| \ge c$, we obtain **Chebyshev's inequality**:

$$\mathbf{P}(|X - \mu| \ge c) \le \frac{\sigma^2}{c^2}$$

Alternatively, we can derive this directly from the definition of variance for a continuous random variable:

$$\begin{aligned}
\sigma^2 &= \int_{-\infty}^\infty (x - \mu)^2 f_X(x) \, dx \\
&\ge \int_{-\infty}^{\mu - c} (x - \mu)^2 f_X(x) \, dx + \int_{\mu + c}^\infty (x - \mu)^2 f_X(x) \, dx \\
&\ge c^2 \left[ \int_{-\infty}^{\mu - c} f_X(x) \, dx + \int_{\mu + c}^\infty f_X(x) \, dx \right] \\
&= c^2 \cdot \mathbf{P}(|X - \mu| \ge c)
\end{aligned}$$

Dividing by $c^2$ produces the same bound. 

A particularly illuminating substitution is to set $c = k\sigma$, measuring deviation in units of the standard deviation $\sigma$:

$$\mathbf{P}(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

For instance, the probability that an observation lies 3 or more standard deviations away from the mean is at most $1/3^2 = 1/9$, regardless of the underlying distribution.

## Convergence in Probability

### Deterministic Limits

Recall that a deterministic sequence of real numbers $a_n$ converges to a limit $a$, written $\lim_{n \to \infty} a_n = a$, if the sequence eventually enters and permanently remains within an arbitrarily narrow band around $a$:

$$\text{For every } \epsilon > 0, \text{ there exists } n_0 \text{ such that for all } n \ge n_0, \ |a_n - a| \le \epsilon$$

### Random Variables and Convergence in Probability

For a sequence of random variables $Y_n$, each realization is governed by a probability distribution. We cannot demand that every realization falls within a deterministic band, because probability distributions often have unbounded tails. Instead, we require that the *probability mass* or *density* gets concentrated inside an arbitrarily narrow band around $a$.

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Probability distribution concentrating around a limit value inside an epsilon band">
  <defs>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="30" y1="150" x2="390" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="210" y1="160" x2="210" y2="25" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- Band boundaries -->
  <line x1="140" y1="155" x2="140" y2="35" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="280" y1="155" x2="280" y2="35" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <!-- Tail shading -->
  <path d="M 40 150 Q 80 150 110 142 Q 130 132 140 118 L 140 150 Z" fill="currentColor" fill-opacity="0.15"/>
  <path d="M 280 118 Q 290 132 310 142 Q 340 150 380 150 L 280 150 Z" fill="currentColor" fill-opacity="0.15"/>
  <!-- Density curve -->
  <path d="M 40 150 Q 110 146 140 118 Q 175 70 210 35 Q 245 70 280 118 Q 310 146 380 150" fill="none" stroke="currentColor" stroke-width="2"/>
  <!-- Labels -->
  <text x="210" y="170" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <text x="140" y="170" text-anchor="middle" font-size="12" fill="currentColor">a - ε</text>
  <text x="280" y="170" text-anchor="middle" font-size="12" fill="currentColor">a + ε</text>
  <text x="90" y="130" text-anchor="middle" font-size="11" fill="currentColor">Tail area</text>
  <text x="330" y="130" text-anchor="middle" font-size="11" fill="currentColor">Tail area</text>
</svg>
<figcaption>Convergence in probability: as $n$ increases, the probability assigned to outcomes outside $[a - \epsilon, a + \epsilon]$ vanishes.</figcaption>
</figure>

A sequence of random variables $Y_n$ **converges in probability** to a number $a$ if for every $\epsilon > 0$:

$$\lim_{n \to \infty} \mathbf{P}(|Y_n - a| \ge \epsilon) = 0$$

Because $\mathbf{P}(|Y_n - a| \ge \epsilon)$ is a regular sequence of real numbers, this condition means: for every $\epsilon > 0$ and every $\epsilon' > 0$, there exists an integer $n_0$ such that for all $n \ge n_0$, $\mathbf{P}(|Y_n - a| \ge \epsilon) \le \epsilon'$.

### An Instructive Counterexample: Moments Need Not Converge

Convergence in probability implies that tail probabilities vanish, but it does not constrain how far into the extremes those tails reach. Consequently, convergence in probability does not imply convergence of expected values or higher moments.

Consider a discrete random variable $Y_n$ with PMF:

$$p_{Y_n}(y) = \begin{cases} 1 - \dfrac{1}{n}, & y = 0, \\ \dfrac{1}{n}, & y = n, \\ 0, & \text{otherwise.} \end{cases}$$

For any $\epsilon \in (0, 1)$, the probability of falling outside $[-\epsilon, \epsilon]$ is simply the probability that $Y_n = n$:

$$\mathbf{P}(|Y_n - 0| \ge \epsilon) = \mathbf{P}(Y_n = n) = \frac{1}{n}$$

As $n \to \infty$, this probability tends to 0. Thus, $Y_n$ converges in probability to 0. However:
* The expectation is $\mathbf{E}[Y_n] = 0 \cdot \left(1 - \frac{1}{n}\right) + n \cdot \frac{1}{n} = 1$ for all $n$, so $\lim_{n \to \infty} \mathbf{E}[Y_n] = 1 \neq 0$.
* The second moment is $\mathbf{E}[Y_n^2] = 0^2 \cdot \left(1 - \frac{1}{n}\right) + n^2 \cdot \frac{1}{n} = n \to \infty$.

The infinitesimal probability $1/n$ is multiplied by an increasingly extreme value $n$, giving a persistent contribution to expectations and an exploding contribution to variance.

## The Weak Law of Large Numbers

Let $X_1, X_2, \dots, X_n$ be independent and identically distributed (i.i.d.) random variables with finite mean $\mu = \mathbf{E}[X_i]$ and finite variance $\sigma^2 = \text{Var}(X_i)$. 

Let $M_n = \frac{1}{n} \sum_{i=1}^n X_i$ denote the sample mean. We determine the moments of $M_n$:
1. **Expected Value:** By linearity of expectation,
   $$\mathbf{E}[M_n] = \frac{1}{n} \sum_{i=1}^n \mathbf{E}[X_i] = \frac{1}{n} \cdot n\mu = \mu$$
2. **Variance:** Because the $X_i$ are independent, the variance of the sum is the sum of the variances. Factoring out $1/n$ squares the denominator:
   $$\text{Var}(M_n) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$$

As the sample size $n$ grows, the variance $\text{Var}(M_n)$ shrinks to 0. Applying Chebyshev's inequality to $M_n$ for any fixed $\epsilon > 0$:

$$\mathbf{P}(|M_n - \mu| \ge \epsilon) \le \frac{\text{Var}(M_n)}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2}$$

Taking the limit as $n \to \infty$:

$$\lim_{n \to \infty} \mathbf{P}(|M_n - \mu| \ge \epsilon) \le \lim_{n \to \infty} \frac{\sigma^2}{n\epsilon^2} = 0$$

Because probabilities are non-negative, this limit must be identically 0. This establishes the **Weak Law of Large Numbers (WLLN)**: the sample mean $M_n$ converges in probability to the true expectation $\mu$.

## Application: The Pollster's Problem

A pollster wishes to estimate the unknown fraction $f \in [0, 1]$ of a population that prefers brand A over brand B. 

We interview $n$ randomly selected individuals. Let:
$$X_i = \begin{cases} 1, & \text{if person } i \text{ prefers brand A}, \\ 0, & \text{otherwise.} \end{cases}$$

The random variables $X_i$ are modeled as i.i.d. Bernoulli trials with parameter $p = f$. The mean is $\mathbf{E}[X_i] = f$, and the sample mean $M_n = \frac{1}{n}\sum_{i=1}^n X_i$ represents the sample fraction $\hat{f}$.

Suppose the specifications require that the pollster be at least $95\%$ confident that the estimate $\hat{f}$ lies within $1$ percentage point ($0.01$) of the true fraction $f$:

$$\mathbf{P}(|M_n - f| \ge 0.01) \le 0.05$$

Here, $\epsilon = 0.01$ is the desired accuracy, and $0.05 = 1 - 0.95$ represents the allowed probability of error ($1 - \text{confidence}$).

Applying Chebyshev's inequality:

$$\mathbf{P}(|M_n - f| \ge 0.01) \le \frac{\sigma_{M_n}^2}{(0.01)^2} = \frac{\sigma_X^2}{n(0.01)^2}$$

The variance of a Bernoulli random variable is $\sigma_X^2 = f(1 - f)$. Because $f$ is the unknown parameter we are attempting to estimate, $\sigma_X^2$ is unknown. However, the quadratic function $f(1 - f)$ achieves its maximum at $f = 1/2$:

$$f(1 - f) \le \frac{1}{2}\left(1 - \frac{1}{2}\right) = \frac{1}{4}$$

We adopt the most conservative (worst-case) upper bound:

$$\mathbf{P}(|M_n - f| \ge 0.01) \le \frac{1}{4n(0.01)^2}$$

To guarantee that this tail probability is at most $0.05$, we set:

$$\frac{1}{4n(0.01)^2} \le 0.05 \implies n \ge \frac{1}{4(0.0001)(0.05)} = \frac{1}{0.00002} = 50{,}000$$

A sample size of $50{,}000$ guarantees the required specifications. In practice, public opinion polls rarely survey more than $1{,}000$ to $2{,}000$ respondents. Sample sizes of $50{,}000$ are unnecessarily large because:
1. Real polls often target an accuracy of $\pm 3\%$ rather than $\pm 1\%$. Since accuracy $\epsilon$ enters as $\epsilon^2$, widening the tolerance to $0.03$ reduces $n$ by a factor of 9.
2. Chebyshev's inequality is a universal, distribution-free bound, making it notoriously conservative. Tighter sample size bounds require the Central Limit Theorem.

## Different Scalings of the Sum and the Central Limit Theorem

To understand how sums of random variables behave, consider the sum $S_n = X_1 + \dots + X_n$ of i.i.d. random variables with mean $\mu$ and variance $\sigma^2$ under three different scalings:

1. **Unscaled Sum: $S_n$**
   $$\mathbf{E}[S_n] = n\mu, \quad \text{Var}(S_n) = n\sigma^2$$
   As $n \to \infty$, the mean shifts linearly and the distribution spreads out, flattening completely.
2. **Averaged Sum: $M_n = S_n / n$**
   $$\mathbf{E}[M_n] = \mu, \quad \text{Var}(M_n) = \frac{\sigma^2}{n}$$
   As $n \to \infty$, the variance vanishes, compressing the entire distribution into a single degenerate spike at $\mu$.
3. **Diffusive Scaling: $S_n / \sqrt{n}$**
   $$\text{Var}\left(\frac{S_n}{\sqrt{n}}\right) = \frac{\text{Var}(S_n)}{n} = \frac{n\sigma^2}{n} = \sigma^2$$
   Scaling by $\sqrt{n}$ preserves a constant, non-zero variance $\sigma^2$ for all $n$.

Subtracting the mean $n\mu$ prevents the distribution from drifting to $\pm \infty$. This leads to the **standardized sum**:

$$Z_n = \frac{S_n - \mathbf{E}[S_n]}{\sigma_{S_n}} = \frac{S_n - n\mu}{\sqrt{n}\sigma}$$

By construction, $Z_n$ has zero mean and unit variance:

$$\mathbf{E}[Z_n] = 0, \quad \text{Var}(Z_n) = 1$$

The standardized variable $Z_n$ measures how many standard deviations $S_n$ deviates from its mean.

### The Central Limit Theorem

Let $Z$ be a standard normal random variable with cumulative distribution function (CDF) $\Phi(c) = \mathbf{P}(Z \le c)$.

The **Central Limit Theorem (CLT)** states that for any constant $c$:

$$\lim_{n \to \infty} \mathbf{P}(Z_n \le c) = \mathbf{P}(Z \le c) = \Phi(c)$$

Regardless of the original distribution of the $X_i$ (discrete, continuous, skewed, or multimodal), the CDF of the standardized sum converges pointwise to the standard normal CDF. In practice, for sufficiently large $n$, we approximate $S_n$ as a normal random variable with mean $n\mu$ and variance $n\sigma^2$:

$$S_n \approx \mathcal{N}(n\mu, n\sigma^2)$$

## Exercises

### Exercise 1: Course Switching Dynamics
Josephina is currently a Course 6-1 student. On each day that she is a 6-1 student, she has probability $1/2$ of remaining a 6-1 student the next day. Otherwise, she is equally likely to become a 6-2 student, a 6-3 student, a Course 9 student, or a Course 15 student the following day. 

On any day she is a 6-3 student, she has probability $1/4$ of switching to Course 9, probability $3/8$ of switching to 6-1, and probability $3/8$ of switching to 6-2 the next day. 

On any day she is a 6-2 student, she has probability $1/2$ of switching to Course 15, probability $3/8$ of switching to 6-1, and probability $1/8$ of switching to 6-3 the next day.

Assume Josephina will be a student forever. For parts (a) through (f), assume that if Josephina switches to Course 9 or Course 15, she remains there permanently and will not switch majors again.

(a) What is the probability that she will eventually leave Course 6?  
(b) What is the probability that she will eventually end up in Course 15?  
(c) What is the expected number of days until she leaves Course 6?  
(d) Every time she switches into 6-1 from either 6-2 or 6-3, she buys herself an ice cream cone. After she has purchased 2 ice cream cones, she stops buying ice cream altogether. What is the expected number of ice cream cones she buys before leaving Course 6?  
(e) Her friend Oscar began under the exact same initial conditions as Josephina and is currently in Course 15. Given that he has reached Course 15, what is the expected number of days it took him to switch to Course 15?  
(f) Josephina decides Course 15 is not an option. Accordingly, when she is a 6-1 student, she remains in 6-1 with probability $1/2$, and otherwise is equally likely to choose any of the remaining alternatives (6-2, 6-3, Course 9). When she is in 6-2, her transition probabilities to 6-1 and 6-3 maintain their original proportions ($3:1$), with zero probability of transitioning to Course 15. What is the expected number of days until she enters Course 9?  
(g) For this part only, remove the absorbing nature of Course 9 and Course 15: assume that when Josephina is in Course 9, she is equally likely to stay in Course 9 or switch to Course 15 on the next day. Similarly, if she is in Course 15, she is equally likely to stay in Course 15 or switch to Course 9. Calculate the steady-state probability of Josephina being in each course on a day far into the future.  
(h) Suppose instead that from Course 9 or Course 15, she has a probability of $1/8$ of transitioning to 6-1 on any given day, and otherwise remains in her current course. Given that she is in 6-1 today, what is the expected number of days until she is in 6-1 again?

## Sources

* Lecture slides: Course 6.041SC, Lecture 19 (Chebyshev's inequality, deterministic limits, convergence in probability, sample mean, pollster's problem, sum scalings, Central Limit Theorem statement).
* Lecture transcript: Course 6.041SC, Lecture 19 (Penguin motivation, Markov inequality derivation, Chebyshev derivation from Markov and continuous integrals, $Y_n$ moment counterexample, polling sample size derivation, $\sqrt{n}$ scaling justification).
* Recitation slides: Course 6.041/6.431 Fall 2010, Recitation 19 (Josephina Markov chain problems). Note: The recitation exercises supplied covered discrete Markov chains, while the lecture covered limit theorems.

Solutions: [chapter 19](solutions/19-limit-theorems-and-sample-means.md)


---

[← 18. Markov Chain Dynamics and Absorption](18-markov-chain-dynamics-and-absorption.md) · [Contents](index.md) · [20. The Central Limit Theorem →](20-the-central-limit-theorem.md)
