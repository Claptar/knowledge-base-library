---
title: "21. Introduction to Bayesian Inference"
course: "MIT 6.041SC"
chapter: 21
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Introduction to Bayesian Inference

## What this covers

This chapter introduces statistical inference, contrasting the classical approach with the Bayesian framework. It shows how unknown quantities are modeled as random variables, how Bayes' rule is applied to compute posterior distributions from data, and why the conditional expectation acts as the optimal estimator under a squared-error criterion.

## From Probability to Statistical Inference

In forward probability models, we assume a known probabilistic structure—such as an arrival process governed by a Poisson law with rate $\lambda$—and calculate the probability of observing specific events. In statistical inference, the arrow is reversed. Reality produces observable data $X$, and from this data we seek to deduce the underlying model or its unknown parameters:

$$\text{Reality} \longrightarrow \text{Data } X \longrightarrow \text{Model / Inference}$$

Applications of this reverse reasoning are ubiquitous:
- **Design of experiments and polling:** Inferring population preferences from a sampled subset, or evaluating whether a medical treatment is effective based on clinical trial outcomes.
- **Recommendation systems:** Estimating missing user preferences from sparse rating data (as in the Netflix Prize competition).
- **Signal processing and tracking:** Estimating an underlying signal $S$ or physical parameter $a$ from a noisy measurement $X = aS + W$.
- **Model fitting:** Determining the trajectory parameters of a celestial body or projectile given noisy position coordinates over time.

While probability theory yields unique, mathematically deductive solutions from fixed axioms and distributions, statistics offers no single universally valid method. Different estimators possess different desirable properties, making it essential to analyze the exact criteria under which an estimator performs well.

## Taxonomy of Inference Problems

Inference tasks can be grouped across several dimensions:

1. **System Identification vs. Signal Estimation:**
   In a linear model such as $X = aS + W$ with noise $W$:
   - *System identification (model building):* We transmit a known test signal $S$, observe $X$, and estimate the channel parameter $a$.
   - *Signal estimation:* We know the transmission parameter $a$, observe $X$, and attempt to recover the transmitted message $S$.
   Mathematically, both problems treat an unobserved multiplier as the quantity to estimate from a noisy sum.

2. **Hypothesis Testing vs. Estimation:**
   - *Hypothesis testing:* The unknown quantity takes one of a small, discrete set of values (e.g., an airplane is either present or absent on radar). The goal is to minimize the probability of making an incorrect decision.
   - *Estimation:* The unknown quantity is continuous (e.g., an unknown fraction $f$ of voters, or the physical coordinates of an object). The objective is to make the numerical error as small as possible.

3. **Classical vs. Bayesian Philosophies:**
   - *Classical statistics:* The unknown parameter $\theta$ is an unknown, fixed constant (a deterministic number, denoted in lowercase $\theta$). It has no probability distribution. For instance, the physical mass of an electron is a fixed constant of nature.
     $$\theta \longrightarrow \fbox{$p_X(x; \theta)$} \stackrel{X}{\longrightarrow} \fbox{Estimator} \longrightarrow \hat{\Theta}$$
   - *Bayesian statistics:* Any unobserved quantity is modeled as a random variable, denoted by an uppercase $\Theta$. Even if the physical quantity is fixed, the prior distribution $p_\Theta(\theta)$ or $f_\Theta(\theta)$ models our subjective state of belief or uncertainty before observing the data.
     $$\Theta \sim p_\Theta(\theta) \longrightarrow \fbox{$p_{X|\Theta}(x \mid \theta)$} \stackrel{X}{\longrightarrow} \fbox{Estimator} \longrightarrow \hat{\Theta}$$

In both formulations, because the observed data $X$ is subject to random measurement noise or sampling variability, the resulting estimator $\hat{\Theta} = g(X)$ is a function of a random variable, and hence is itself a random variable.

## The Bayesian Framework and Bayes' Rule

The Bayesian method treats inference as a direct application of conditional probability. We begin with:
- A **prior distribution** ($p_\Theta$ or $f_\Theta$) summarizing initial beliefs.
- A **data model / observation likelihood** ($p_{X|\Theta}$ or $f_{X|\Theta}$) representing the measuring apparatus and noise.

Once data $X = x$ is observed, Bayes' rule yields the **posterior distribution**:

- **Discrete unknown $\Theta$ (Hypothesis testing):**
  - Discrete observations $X$:
    $$p_{\Theta|X}(\theta \mid x) = \frac{p_\Theta(\theta) \, p_{X|\Theta}(x \mid \theta)}{p_X(x)} = \frac{p_\Theta(\theta) \, p_{X|\Theta}(x \mid \theta)}{\sum_{\theta'} p_\Theta(\theta') \, p_{X|\Theta}(x \mid \theta')}$$
  - Continuous observations $X$:
    $$p_{\Theta|X}(\theta \mid x) = \frac{p_\Theta(\theta) \, f_{X|\Theta}(x \mid \theta)}{f_X(x)} = \frac{p_\Theta(\theta) \, f_{X|\Theta}(x \mid \theta)}{\sum_{\theta'} p_\Theta(\theta') \, f_{X|\Theta}(x \mid \theta')}$$

- **Continuous unknown $\Theta$ (Continuous estimation):**
  - Continuous observations $X$:
    $$f_{\Theta|X}(\theta \mid x) = \frac{f_\Theta(\theta) \, f_{X|\Theta}(x \mid \theta)}{f_X(x)} = \frac{f_\Theta(\theta) \, f_{X|\Theta}(x \mid \theta)}{\int f_\Theta(\theta') \, f_{X|\Theta}(x \mid \theta') \, d\theta'}$$
  - Discrete observations $X$:
    $$f_{\Theta|X}(\theta \mid x) = \frac{f_\Theta(\theta) \, p_{X|\Theta}(x \mid \theta)}{p_X(x)} = \frac{f_\Theta(\theta) \, p_{X|\Theta}(x \mid \theta)}{\int f_\Theta(\theta') \, p_{X|\Theta}(x \mid \theta') \, d\theta'}$$

### Example: Estimating Coin Bias with Discrete Data
Consider a coin whose probability of heads is an unknown continuous parameter $\Theta \in [0, 1]$. In $n$ independent tosses, we observe $X = k$ heads. 

A classical statistician calculates the sample proportion $\hat{\theta} = k/n$ and proves via the weak law of large numbers that $\hat{\theta}$ converges in probability to $\theta$ as $n \to \infty$. 

A Bayesian specifies a prior $f_\Theta(\theta)$ reflecting prior knowledge:
- A uniform prior $f_\Theta(\theta) = 1$ for $\theta \in [0, 1]$ models complete initial ignorance.
- A prior tightly concentrated around $1/2$ models belief that the manufacturing process produces nearly fair coins.

Using Bayes' rule with the binomial likelihood $p_{X|\Theta}(k \mid \theta) = \binom{n}{k}\theta^k(1-\theta)^{n-k}$, the posterior density is:
$$f_{\Theta|X}(\theta \mid k) = \frac{f_\Theta(\theta) \binom{n}{k} \theta^k (1-\theta)^{n-k}}{\int_0^1 f_\Theta(\theta') \binom{n}{k} (\theta')^k (1-\theta')^{n-k} \, d\theta'}$$

### Vector Unknowns and Vector Observations
When estimating trajectories, the unknown is typically a vector of parameters. If an object follows a parabolic flight path:
$$Z_t = \Theta_0 + t\Theta_1 + t^2\Theta_2$$
and we record noisy measurements at several points in time:
$$X_t = Z_t + W_t, \quad t = 1, 2, \dots, n$$
the Bayesian procedure operates identically on vectors:
$$f_{\boldsymbol{\Theta}|\mathbf{X}}(\theta_0, \theta_1, \theta_2 \mid x_1, \dots, x_n) = \frac{f_{\boldsymbol{\Theta}}(\theta_0, \theta_1, \theta_2) \, f_{\mathbf{X}|\boldsymbol{\Theta}}(x_1, \dots, x_n \mid \theta_0, \theta_1, \theta_2)}{f_{\mathbf{X}}(x_1, \dots, x_n)}$$

## Point Estimators: MAP and Conditional Expectation

The complete output of Bayesian inference is the posterior distribution $p_{\Theta|X}(\cdot \mid x)$ or $f_{\Theta|X}(\cdot \mid x)$. When practical constraints require reporting a single numerical estimate $\hat{\theta}$, two principal estimators are used.

### Maximum A Posteriori (MAP) Probability
The MAP estimate selects the value of $\theta$ that maximizes the posterior:
- Discrete unknown:
  $$\theta^*_{\text{MAP}} = \arg\max_\theta p_{\Theta|X}(\theta \mid x)$$
- Continuous unknown:
  $$\theta^*_{\text{MAP}} = \arg\max_\theta f_{\Theta|X}(\theta \mid x)$$

In hypothesis testing (discrete $\Theta$), if we guess $\hat{\theta}$, the probability of being correct is $p_{\Theta|X}(\hat{\theta} \mid x)$, and the probability of error is $1 - p_{\Theta|X}(\hat{\theta} \mid x)$. Choosing $\theta^*_{\text{MAP}}$ minimizes the probability of error.

For continuous parameters, the probability of any exact value is zero ($P(\Theta = \theta) = 0$). The MAP point identifies the peak of the probability density, meaning small intervals centered at this point have the highest probability mass, but it no longer has the same direct interpretation of maximizing $P(\Theta = \hat{\theta})$.

### Conditional Expectation
The conditional expectation is the center of mass of the posterior distribution:
$$\mathbf{E}[\Theta \mid X = x] = \int \theta \, f_{\Theta|X}(\theta \mid x) \, d\theta$$
For an asymmetric or multimodal posterior distribution, the MAP peak and the conditional expectation can differ significantly:

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Posterior probability density function showing the MAP estimate at the peak and the conditional expectation shifted rightward toward the tail.">
  <defs>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="40" y1="180" x2="390" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="50" y1="190" x2="50" y2="20" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="395" y="184" font-size="12" fill="currentColor">θ</text>
  <text x="35" y="18" font-size="12" fill="currentColor">f(θ|x)</text>

  <!-- Density Curve -->
  <path d="M 50,180 C 80,180 100,165 115,100 C 125,50 135,40 145,40 C 155,40 165,80 180,130 C 200,170 230,150 260,150 C 310,150 350,180 380,180" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="2"/>

  <!-- MAP line -->
  <line x1="140" y1="40" x2="140" y2="180" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="140" y="198" text-anchor="middle" font-size="11" fill="currentColor">θ_MAP</text>

  <!-- Conditional Expectation line -->
  <line x1="195" y1="137" x2="195" y2="180" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="195" y="198" text-anchor="middle" font-size="11" fill="currentColor">E[Θ|X=x]</text>
</svg>
<figcaption>Posterior density $f_{\Theta|X}(\theta \mid x)$ where the peak ($\theta_{\text{MAP}}$) and the balance point ($\mathbf{E}[\Theta \mid X = x]$) take different values due to asymmetry.</figcaption>
</figure>

## Least Mean Squares (LMS) Estimation

When estimation errors are continuous, reporting a single point estimate requires specifying an error metric. A standard metric is the squared error $(\Theta - \hat{\theta})^2$, which penalizes larger errors disproportionately.

### LMS Without Observations
Consider finding a single constant $c$ to estimate $\Theta$ in the absence of any data, so as to minimize the Mean Squared Error (MSE):
$$\min_c \mathbf{E}\left[(\Theta - c)^2\right]$$

Expanding the quadratic expression:
$$\mathbf{E}\left[(\Theta - c)^2\right] = \mathbf{E}\left[\Theta^2 - 2c\Theta + c^2\right] = \mathbf{E}[\Theta^2] - 2c\,\mathbf{E}[\Theta] + c^2$$
Differentiating with respect to $c$ and setting the derivative to zero:
$$\frac{d}{dc} \mathbf{E}\left[(\Theta - c)^2\right] = -2\mathbf{E}[\Theta] + 2c = 0 \implies c^* = \mathbf{E}[\Theta]$$
The second derivative is $2 > 0$, confirming this is a minimum. 

The resulting minimum mean squared error is:
$$\mathbf{E}\left[(\Theta - \mathbf{E}[\Theta])^2\right] = \text{Var}(\Theta)$$

### LMS With Observations
Now suppose we observe data $X = x$. Conditioning on this observation defines a new universe governed by the conditional distribution $f_{\Theta|X}(\theta \mid x)$.

To minimize the conditional mean squared error:
$$\min_c \mathbf{E}\left[(\Theta - c)^2 \mid X = x\right]$$
the exact same minimization argument applies within this conditional universe. Thus, the optimal constant is the conditional expectation:
$$c^* = \mathbf{E}[\Theta \mid X = x]$$
Therefore, for any alternative estimate $g(x)$:
$$\mathbf{E}\left[(\Theta - \mathbf{E}[\Theta \mid X = x])^2 \mid X = x\right] \le \mathbf{E}\left[(\Theta - g(x))^2 \mid X = x\right]$$

### Optimality Over All Estimators
Because this inequality holds for every possible realized value $x$, it holds when evaluated as a function of the random variable $X$:
$$\mathbf{E}\left[(\Theta - \mathbf{E}[\Theta \mid X])^2 \mid X\right] \le \mathbf{E}\left[(\Theta - g(X))^2 \mid X\right]$$
Taking expectations of both sides with respect to $X$ (using the law of iterated expectations):
$$\mathbf{E}\left[(\Theta - \mathbf{E}[\Theta \mid X])^2\right] \le \mathbf{E}\left[(\Theta - g(X))^2\right]$$

This establishes that across the entire class of conceivable estimators $g(X)$—linear or non-linear—the conditional expectation $g^*(X) = \mathbf{E}[\Theta \mid X]$ minimizes the overall mean squared error.

### Practical Considerations
While $\mathbf{E}[\Theta \mid X_1, \dots, X_n]$ is mathematically the optimal LMS estimator, practical implementation involves two challenges:
1. **Prior Selection:** The estimator depends directly on the chosen prior $f_\Theta$, requiring informed domain judgment.
2. **Computational Complexity:** When the observation vector $\mathbf{X}$ has high dimension, evaluating the denominator $f_{\mathbf{X}}(\mathbf{x}) = \int f_{\boldsymbol{\Theta}}(\boldsymbol{\theta}) f_{\mathbf{X}|\boldsymbol{\Theta}}(\mathbf{x} \mid \boldsymbol{\theta}) \, d\boldsymbol{\theta}$ and computing the expectation requires high-dimensional integration, which can be analytically intractable and computationally expensive.

---

## Exercises

1. Let $X_1, \ldots, X_{10}$ be independent random variables, uniformly distributed over the unit interval $[0,1]$.
   (a) Estimate $\mathbf{P}(X_1 + \cdots + X_{10} \ge 7)$ using the Markov inequality.
   (b) Repeat part (a) using the Chebyshev inequality.
   (c) Repeat part (a) using the central limit theorem.

2. A factory produces $X_n$ gadgets on day $n$, where the $X_n$ are independent and identically distributed random variables, with mean 5 and variance 9.
   (a) Find an approximation to the probability that the total number of gadgets produced in 100 days is less than 440.
   (b) Find (approximately) the largest value of $n$ such that
   $$\mathbf{P}\left(X_1 + \cdots + X_n \ge 200 + 5n\right) \le 0.05$$
   (c) Let $N$ be the first day on which the total number of gadgets produced exceeds 1000. Calculate an approximation to the probability that $N \ge 220$.

3. Let $X_1, X_2, \ldots$ be independent Poisson random variables with mean and variance equal to 1. For any $n > 0$, let $S_n = \sum_{i=1}^n X_i$.
   (a) Show that $S_n$ is Poisson with mean and variance equal to $n$.
   (b) Show how the central limit theorem suggests the approximation
   $$n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$
   for large values of the positive integer $n$.

---

## Sources

- **Lecture 21 Slides:** Overview of statistical models, taxonomy of inference problems (system identification, hypothesis testing, classical vs. Bayesian), Bayes' rule formulas across discrete/continuous combinations, coin bias example, MAP decision rules, and derivation of LMS estimators without and with observations.
- **Lecture 21 Transcript:** Motivation using arrival modeling, Netflix recommendations, orbit fitting, electron mass example, philosophical differences between classical parameters and Bayesian priors, contrast between MAP and conditional expectation, and the proof of LMS optimality over all functions $g(X)$.
- **Recitation 21 Slides and Transcript:** Formulation of the bounding and limit theorem problems for the Exercises section. Note: The lecture referred to specific historical misuses of statistics and promised simpler alternatives to multi-dimensional Bayesian integration (linear least squares), which were deferred to subsequent lectures.

---

[← 20. The Central Limit Theorem](20-the-central-limit-theorem.md) · [Contents](index.md) · [22. Least Mean Squares Estimation →](22-least-mean-squares-estimation.md)
