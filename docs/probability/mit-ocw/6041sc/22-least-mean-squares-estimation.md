---
title: "22. Least Mean Squares Estimation"
course: "MIT 6.041SC"
chapter: 22
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Least Mean Squares Estimation

## What this covers

This chapter covers Bayesian point estimation under the mean squared error criterion, leading to the conditional expectation as the optimal estimator, its theoretical properties, and its linear counterpart. We assume familiarity with joint and conditional probability densities, conditioning on continuous random variables, and the law of iterated expectations.

## The Bayesian Estimation Framework

In the Bayesian formulation of estimation, an unknown quantity is treated as a random variable $\Theta$ rather than a fixed unknown constant. Before taking any measurements, our beliefs about $\Theta$ are captured by a prior distribution, given by a probability density function $f_\Theta(\theta)$ (or a PMF $p_\Theta(\theta)$ in the discrete case). 

We then acquire an observation, modeled as a random variable $X$ (or a random vector $X = (X_1, \dots, X_n)$). The observation is statistically related to $\Theta$ through an observation model, specified by the conditional density $f_{X|\Theta}(x \mid \theta)$. Together, these define the joint density:
$$f_{X, \Theta}(x, \theta) = f_\Theta(\theta) f_{X|\Theta}(x \mid \theta)$$

Once a concrete measurement $X = x$ is observed, Bayes' rule yields the posterior distribution:
$$f_{\Theta|X}(\theta \mid x) = \frac{f_{X, \Theta}(x, \theta)}{f_X(x)} = \frac{f_\Theta(\theta) f_{X|\Theta}(x \mid \theta)}{\int f_\Theta(\theta') f_{X|\Theta}(x \mid \theta') \, d\theta'}$$

The posterior distribution captures everything there is to know about $\Theta$ given the data. However, in most engineering and scientific settings, we need to report a single numerical value—a point estimate $\hat{\theta}$. An estimator is a rule (a function) $g(X)$ that maps the observed data to an estimate $\hat{\Theta} = g(X)$.

One common choice is the Maximum A Posteriori (MAP) estimator, which selects the value of $\theta$ that maximizes the posterior density:
$$\hat{\theta}_{\text{MAP}} = \arg\max_\theta f_{\Theta|X}(\theta \mid x)$$

While intuitive, MAP ignores how probability mass is distributed around the peak. An alternative, deeply connected to signal processing, control, and communications, is to design an estimator that minimizes the average squared error.

## Least Mean Squares (LMS) Estimation

Let $g(X)$ be an estimator of $\Theta$. The estimation error is $\Theta - g(X)$, and the mean squared error (MSE) is defined as:
$$\mathbf{E}\left[(\Theta - g(X))^2\right]$$

We wish to find a function $g^*(\cdot)$ that minimizes this quantity over all possible estimators $g(\cdot)$.

### The Optimal Estimator

By the law of iterated expectations, we can decompose the unconditional mean squared error by conditioning on $X$:
$$\mathbf{E}\left[(\Theta - g(X))^2\right] = \mathbf{E}\left[ \mathbf{E}\left[(\Theta - g(X))^2 \mid X\right] \right] = \int \mathbf{E}\left[(\Theta - g(x))^2 \mid X = x\right] f_X(x) \, dx$$

Because the outer expectation averages over $X$ with non-negative weights $f_X(x)$, we can minimize the overall expectation by minimizing the inner conditional expectation separately for each possible value $x$:
$$\min_{g(\cdot)} \mathbf{E}\left[(\Theta - g(X))^2\right] \iff \min_{\hat{\theta}} \mathbf{E}\left[(\Theta - \hat{\theta})^2 \mid X = x\right] \quad \text{for every } x$$

Fix a value $x$, and consider minimizing $\mathbf{E}\left[(\Theta - c)^2 \mid X = x\right]$ over all real numbers $c$. In general, for any random variable $Y$, the constant $c$ that minimizes $\mathbf{E}[(Y - c)^2]$ is the mean $\mathbf{E}[Y]$. Therefore, within the conditional universe given $X = x$, the optimal estimate is:
$$\hat{\theta}^* = \mathbf{E}[\Theta \mid X = x]$$

When viewed as a function of the random variable $X$, the optimal estimator under the mean squared error criterion—the least mean squares (LMS) estimator—is the conditional expectation:
$$\hat{\Theta}_{\text{LMS}} = \mathbf{E}[\Theta \mid X]$$

This establishes two properties:
1. **Conditional optimality:** For any specific observation $X = x$, $\hat{\theta} = \mathbf{E}[\Theta \mid X = x]$ minimizes the conditional MSE $\mathbf{E}[(\Theta - \hat{\theta})^2 \mid X = x]$.
2. **Overall optimality:** Averaged over all possible observations, $\hat{\Theta} = \mathbf{E}[\Theta \mid X]$ minimizes the unconditional MSE $\mathbf{E}[(\Theta - g(X))^2]$ over all functions $g(\cdot)$.

### Conditional Mean Squared Error

When we report the estimate $\hat{\theta} = \mathbf{E}[\Theta \mid X = x]$, what is our expected squared error? Within the conditional universe given $X = x$, the estimate $\hat{\theta}$ is precisely the conditional mean of $\Theta$. The conditional MSE is therefore:
$$\mathbf{E}\left[(\Theta - \mathbf{E}[\Theta \mid X = x])^2 \mid X = x\right] = \text{Var}(\Theta \mid X = x)$$

The conditional MSE is simply the variance of the posterior distribution of $\Theta$ given $X = x$. 

Crucially, $\text{Var}(\Theta \mid X = x)$ is generally a function of $x$. Some observations provide substantial information and leave little residual uncertainty (small conditional variance), while other observations leave wide uncertainty (large conditional variance).

---

### Example: Uniform Parameter with Bounded Noise

Suppose the parameter $\Theta$ has a uniform prior over $[4, 10]$:
$$f_\Theta(\theta) = \frac{1}{6}, \quad 4 \le \theta \le 10$$
Given $\Theta = \theta$, the observation $X$ is uniformly distributed over the interval $[\theta - 1, \theta + 1]$. Equivalently, $X = \Theta + U$, where $U$ is independent uniform noise on $[-1, 1]$.

The joint density $f_{X, \Theta}(x, \theta)$ is nonzero on the parallelogram defined by $4 \le \theta \le 10$ and $\theta - 1 \le x \le \theta + 1$:
$$f_{X, \Theta}(x, \theta) = f_\Theta(\theta) f_{X|\Theta}(x \mid \theta) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}$$

<figure>
<svg viewBox="0 0 380 240" role="img" aria-label="Support of joint density and conditional LMS estimator">
  <!-- Axes -->
  <line x1="40" y1="200" x2="360" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <!-- Axis labels -->
  <text x="355" y="218" font-size="12" fill="currentColor">x</text>
  <text x="25" y="30" font-size="12" fill="currentColor">θ</text>
  <!-- Parallelogram corners: 
       (x=3, theta=4) -> (75, 152)
       (x=5, theta=4) -> (125, 152)
       (x=11, theta=10) -> (275, 48)
       (x=9, theta=10) -> (225, 48) -->
  <polygon points="75,152 125,152 275,48 225,48" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <!-- Ticks on x-axis -->
  <line x1="75" y1="200" x2="75" y2="205" stroke="currentColor"/>
  <text x="75" y="218" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <line x1="125" y1="200" x2="125" y2="205" stroke="currentColor"/>
  <text x="125" y="218" text-anchor="middle" font-size="11" fill="currentColor">5</text>
  <line x1="225" y1="200" x2="225" y2="205" stroke="currentColor"/>
  <text x="225" y="218" text-anchor="middle" font-size="11" fill="currentColor">9</text>
  <line x1="275" y1="200" x2="275" y2="205" stroke="currentColor"/>
  <text x="275" y="218" text-anchor="middle" font-size="11" fill="currentColor">11</text>
  <!-- Ticks on theta-axis -->
  <line x1="35" y1="152" x2="40" y2="152" stroke="currentColor"/>
  <text x="25" y="156" text-anchor="end" font-size="11" fill="currentColor">4</text>
  <line x1="35" y1="48" x2="40" y2="48" stroke="currentColor"/>
  <text x="25" y="52" text-anchor="end" font-size="11" fill="currentColor">10</text>
  <!-- Estimator g(x):
       x in [3,5]: midpoint between 4 and x+1 -> (x+5)/2
       x=3 -> theta=4 (75, 152); x=5 -> theta=5 (125, 134.7)
       x in [5,9]: midpoint between x-1 and x+1 -> x
       x=5 -> theta=5 (125, 134.7); x=9 -> theta=9 (225, 65.3)
       x in [9,11]: midpoint between x-1 and 10 -> (x+9)/2
       x=9 -> theta=9 (225, 65.3); x=11 -> theta=10 (275, 48) -->
  <polyline points="75,152 125,135 225,65 275,48" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="180" y="85" font-size="12" fill="#2563eb">g(x) = E[Θ|X=x]</text>
</svg>
<figcaption>Support of $(X, \Theta)$ and the LMS estimator $g(x) = \mathbf{E}[\Theta \mid X=x]$ tracing the midpoints of the vertical slices.</figcaption>
</figure>

To determine the conditional expectation $\mathbf{E}[\Theta \mid X = x]$, consider a vertical slice at a fixed $x$:
- Since the joint density is constant over the region, the conditional density $f_{\Theta|X}(\theta \mid x)$ is uniform over the vertical cross-section.
- The conditional expectation is simply the midpoint of this vertical interval.

Depending on $x$, there are three distinct regions:
1. **$3 \le x < 5$:** $\Theta$ ranges from $4$ to $x + 1$. The midpoint is:
   $$g(x) = \frac{4 + (x + 1)}{2} = \frac{x + 5}{2}$$
2. **$5 \le x \le 9$:** $\Theta$ ranges from $x - 1$ to $x + 1$. The midpoint is:
   $$g(x) = \frac{(x - 1) + (x + 1)}{2} = x$$
3. **$9 < x \le 11$:** $\Theta$ ranges from $x - 1$ to $10$. The midpoint is:
   $$g(x) = \frac{(x - 1) + 10}{2} = \frac{x + 9}{2}$$

The optimal estimator $g(x)$ is piecewise linear, but globally **nonlinear**.

Now consider the conditional error variance $\text{Var}(\Theta \mid X = x)$:
- Recall that for a uniform distribution over an interval of length $L$, the variance is $L^2 / 12$.
- For $5 \le x \le 9$, the vertical slice has constant length $L = (x + 1) - (x - 1) = 2$. Thus:
  $$\text{Var}(\Theta \mid X = x) = \frac{2^2}{12} = \frac{1}{3}$$
- For $3 \le x < 5$, the length is $L = (x + 1) - 4 = x - 3$. The variance is:
  $$\text{Var}(\Theta \mid X = x) = \frac{(x - 3)^2}{12}$$
  At $x = 3$, $L = 0$ and the variance is $0$: observing $X = 3$ reveals with certainty that $\Theta = 4$.
- For $9 < x \le 11$, the length is $L = 10 - (x - 1) = 11 - x$, yielding:
  $$\text{Var}(\Theta \mid X = x) = \frac{(11 - x)^2}{12}$$
  At $x = 11$, the variance drops to $0$, since $\Theta$ must be $10$.

The conditional MSE is plotted below. It illustrates that some observations are much more informative than others.

<figure>
<svg viewBox="0 0 360 180" role="img" aria-label="Conditional mean squared error as a function of the observation x">
  <!-- Axes -->
  <line x1="40" y1="140" x2="340" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="140" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="335" y="158" font-size="12" fill="currentColor">x</text>
  <text x="25" y="25" font-size="12" fill="currentColor">Var(Θ|X=x)</text>
  <!-- Ticks -->
  <line x1="60" y1="140" x2="60" y2="145" stroke="currentColor"/>
  <text x="60" y="158" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <line x1="120" y1="140" x2="120" y2="145" stroke="currentColor"/>
  <text x="120" y="158" text-anchor="middle" font-size="11" fill="currentColor">5</text>
  <line x1="240" y1="140" x2="240" y2="145" stroke="currentColor"/>
  <text x="240" y="158" text-anchor="middle" font-size="11" fill="currentColor">9</text>
  <line x1="300" y1="140" x2="300" y2="145" stroke="currentColor"/>
  <text x="300" y="158" text-anchor="middle" font-size="11" fill="currentColor">11</text>
  <!-- Variance level 1/3 at y=60 (scale: 0 is y=140, 1/3 is y=60) -->
  <line x1="35" y1="60" x2="40" y2="60" stroke="currentColor"/>
  <text x="30" y="64" text-anchor="end" font-size="11" fill="currentColor">1/3</text>
  <!-- Curve: quadratic from (60,140) to (120,60), flat to (240,60), quadratic to (300,140) -->
  <path d="M 60,140 Q 100,130 120,60 L 240,60 Q 260,130 300,140" fill="none" stroke="#2563eb" stroke-width="2"/>
</svg>
<figcaption>Conditional mean squared error $\text{Var}(\Theta \mid X=x)$ as a function of the observation $x$.</figcaption>
</figure>

---

## Theoretical Properties of LMS Estimation

Define the estimation error random variable as:
$$\tilde{\Theta} = \hat{\Theta} - \Theta = \mathbf{E}[\Theta \mid X] - \Theta$$

The estimator $\hat{\Theta}$ possesses several fundamental orthogonality and variance-decomposition properties.

### 1. Unbiasedness

Conditioning on $X$, we evaluate the conditional expected error:
$$\mathbf{E}[\tilde{\Theta} \mid X] = \mathbf{E}[\hat{\Theta} - \Theta \mid X] = \mathbf{E}[\hat{\Theta} \mid X] - \mathbf{E}[\Theta \mid X]$$
Because $\hat{\Theta} = \mathbf{E}[\Theta \mid X]$ is completely determined once $X$ is known, it acts as a constant in the conditional universe: $\mathbf{E}[\hat{\Theta} \mid X] = \hat{\Theta}$. By definition, $\mathbf{E}[\Theta \mid X] = \hat{\Theta}$. Thus:
$$\mathbf{E}[\tilde{\Theta} \mid X] = 0$$
This is an equality of random variables. It states that for any specific observed value $x$:
$$\mathbf{E}[\tilde{\Theta} \mid X = x] = 0$$
Taking unconditional expectations on both sides and applying the law of iterated expectations:
$$\mathbf{E}[\tilde{\Theta}] = \mathbf{E}\left[\mathbf{E}[\tilde{\Theta} \mid X]\right] = 0$$
On average, the estimation error is zero: $\hat{\Theta}$ is an **unbiased** estimator.

### 2. Orthogonality to Functions of the Data

Let $h(X)$ be any arbitrary function of $X$. In the conditional expectation $\mathbf{E}[\tilde{\Theta} h(X) \mid X]$, the term $h(X)$ is a constant given $X$ and can be factored out:
$$\mathbf{E}[\tilde{\Theta} h(X) \mid X] = h(X) \mathbf{E}[\tilde{\Theta} \mid X] = h(X) \cdot 0 = 0$$
Taking unconditional expectations via iterated expectations yields:
$$\mathbf{E}[\tilde{\Theta} h(X)] = \mathbf{E}\left[\mathbf{E}[\tilde{\Theta} h(X) \mid X]\right] = 0$$

### 3. Uncorrelatedness with the Estimator

Because the estimator $\hat{\Theta} = \mathbf{E}[\Theta \mid X]$ is itself a function of $X$, setting $h(X) = \hat{\Theta}$ gives:
$$\mathbf{E}[\tilde{\Theta}\hat{\Theta}] = 0$$
Since $\mathbf{E}[\tilde{\Theta}] = 0$, the covariance between the error and the estimate is:
$$\text{Cov}(\tilde{\Theta}, \hat{\Theta}) = \mathbf{E}[\tilde{\Theta}\hat{\Theta}] - \mathbf{E}[\tilde{\Theta}]\mathbf{E}[\hat{\Theta}] = 0 - 0 = 0$$
The estimation error $\tilde{\Theta}$ and the estimate $\hat{\Theta}$ are uncorrelated.

This has an intuitive interpretation: if $\hat{\Theta}$ and $\tilde{\Theta}$ were correlated, observing a large estimate $\hat{\Theta}$ would provide information about the sign of the error $\tilde{\Theta}$. If you suspected that a large $\hat{\Theta}$ meant the error was likely positive (meaning $\hat{\Theta} > \Theta$), you could improve the estimate by reducing it. But $\hat{\Theta}$ is already optimal; it leaves no systematic residual trend.

### 4. Variance Decomposition

Rewriting the parameter identity $\Theta = \hat{\Theta} - \tilde{\Theta}$, and using the fact that $\hat{\Theta}$ and $\tilde{\Theta}$ are uncorrelated:
$$\text{Var}(\Theta) = \text{Var}(\hat{\Theta} - \tilde{\Theta}) = \text{Var}(\hat{\Theta}) + \text{Var}(\tilde{\Theta})$$
- $\text{Var}(\Theta)$ represents the total prior uncertainty in the parameter.
- $\text{Var}(\hat{\Theta})$ represents the variability captured by the estimator.
- $\text{Var}(\tilde{\Theta}) = \mathbf{E}[\tilde{\Theta}^2]$ represents the remaining estimation error variance.

To minimize the error variance $\text{Var}(\tilde{\Theta})$, we want $\hat{\Theta}$ to capture as much of the parameter's variance as possible. In the ideal case where $\hat{\Theta} = \Theta$, $\text{Var}(\tilde{\Theta}) = 0$ and $\text{Var}(\hat{\Theta}) = \text{Var}(\Theta)$.

---

## Linear Least Mean Squares (LLMS) Estimation

While the conditional expectation $\mathbf{E}[\Theta \mid X]$ is optimal, it often results in a complicated nonlinear function (as seen in the uniform example). Furthermore, computing it requires knowledge of the complete joint distribution and potentially difficult multidimensional integrals.

A practical alternative is to restrict the estimator to be an affine function of the observation:
$$\hat{\Theta}_L = aX + b$$
We seek the coefficients $a$ and $b$ that minimize the mean squared error:
$$\min_{a, b} \mathbf{E}\left[(\Theta - aX - b)^2\right]$$

### Derivation for a Single Observation

Expanding the objective function $S(a, b) = \mathbf{E}[(\Theta - aX - b)^2]$:
$$S(a, b) = \mathbf{E}[\Theta^2] + a^2 \mathbf{E}[X^2] + b^2 - 2a\mathbf{E}[X\Theta] - 2b\mathbf{E}[\Theta] + 2ab\mathbf{E}[X]$$
This is a convex quadratic function in $a$ and $b$. Setting the partial derivatives to zero:
1. With respect to $b$:
   $$\frac{\partial S}{\partial b} = 2b - 2\mathbf{E}[\Theta] + 2a\mathbf{E}[X] = 0 \implies b = \mathbf{E}[\Theta] - a\mathbf{E}[X]$$
   Substituting $b$ back into the estimator form:
   $$\hat{\Theta}_L = \mathbf{E}[\Theta] + a(X - \mathbf{E}[X])$$

2. With respect to $a$, substituting $b$:
   $$S(a) = \mathbf{E}\left[\left( (\Theta - \mathbf{E}[\Theta]) - a(X - \mathbf{E}[X]) \right)^2\right] = \text{Var}(\Theta) - 2a \text{Cov}(X, \Theta) + a^2 \text{Var}(X)$$
   Differentiating with respect to $a$ and setting to zero:
   $$-2\text{Cov}(X, \Theta) + 2a\text{Var}(X) = 0 \implies a = \frac{\text{Cov}(X, \Theta)}{\text{Var}(X)}$$

Thus, the optimal linear LMS estimator is:
$$\hat{\Theta}_L = \mathbf{E}[\Theta] + \frac{\text{Cov}(X, \Theta)}{\text{Var}(X)}(X - \mathbf{E}[X])$$

### Interpretation of the Linear Estimator

This formula has a direct interpretation:
- $\mathbf{E}[\Theta]$ is the baseline estimate in the absence of any data.
- $(X - \mathbf{E}[X])$ represents the "surprise" or new information contained in the measurement.
- If $X$ and $\Theta$ are positively correlated ($\text{Cov}(X, \Theta) > 0$), observing an $X$ above its mean suggests that $\Theta$ is also likely above its mean, and we adjust our estimate upward.
- If $\text{Cov}(X, \Theta) = 0$, the observation provides no linear information about $\Theta$, and the best linear estimate simply remains $\mathbf{E}[\Theta]$.

### Resulting Mean Squared Error

Substituting $a = \frac{\text{Cov}(X, \Theta)}{\text{Var}(X)}$ into the MSE expression:
$$\mathbf{E}[(\hat{\Theta}_L - \Theta)^2] = \text{Var}(\Theta) - 2\frac{\text{Cov}(X, \Theta)^2}{\text{Var}(X)} + \frac{\text{Cov}(X, \Theta)^2}{\text{Var}(X)^2} \text{Var}(X) = \sigma_\Theta^2 - \frac{\text{Cov}(X, \Theta)^2}{\sigma_X^2}$$
Using the correlation coefficient $\rho = \frac{\text{Cov}(X, \Theta)}{\sigma_X \sigma_\Theta}$, we obtain:
$$\mathbf{E}[(\hat{\Theta}_L - \Theta)^2] = (1 - \rho^2)\sigma_\Theta^2$$

- If $|\rho| = 1$ ($X$ and $\Theta$ are perfectly correlated), the error variance is $0$.
- If $\rho = 0$ ($X$ and $\Theta$ are uncorrelated), the error variance remains $\sigma_\Theta^2$; the measurement is of no use.
- In all other cases, correlation strictly reduces the prior uncertainty.

---

## Linear LMS with Multiple Observations

When observing a vector of measurements $X = (X_1, \dots, X_n)$, we consider estimators of the form:
$$\hat{\Theta}_L = a_1 X_1 + \dots + a_n X_n + b$$
To minimize $\mathbf{E}\left[(\sum_{i=1}^n a_i X_i + b - \Theta)^2\right]$, we set the partial derivatives with respect to $b$ and each $a_i$ to zero. 

Setting the derivative with respect to $b$ to zero yields:
$$b = \mathbf{E}[\Theta] - \sum_{i=1}^n a_i \mathbf{E}[X_i]$$
Setting the derivatives with respect to $a_i$ to zero leads to a system of linear equations:
$$\sum_{j=1}^n a_j \text{Cov}(X_i, X_j) = \text{Cov}(X_i, \Theta), \quad i = 1, \dots, n$$

A critical property of LLMS is that **only means, variances, and covariances are needed**. We do not need the full joint probability distributions to construct the optimal linear estimator.

---

### Cleanest Example: Independent Noise Measurements

Consider measuring an unknown parameter $\Theta$ across $n$ independent experiments with additive noise:
$$X_i = \Theta + W_i, \quad i = 1, \dots, n$$
Assume:
- $\Theta$ has prior mean $\mu$ and variance $\sigma_0^2$.
- The noises $W_i$ have zero mean $\mathbf{E}[W_i] = 0$ and variances $\sigma_i^2$.
- $\Theta, W_1, \dots, W_n$ are mutually independent.

Solving the linear system for the optimal coefficients produces a weighted average:
$$\hat{\Theta}_L = \frac{\frac{\mu}{\sigma_0^2} + \sum_{i=1}^n \frac{X_i}{\sigma_i^2}}{\sum_{i=0}^n \frac{1}{\sigma_i^2}}$$

Key insights from this formula:
1. **Weighted average:** The denominator is the sum of the weights, ensuring the weights sum to $1$.
2. **Inverse-variance weighting:** Each measurement $X_i$ is weighted by $1/\sigma_i^2$. Highly noisy measurements (large $\sigma_i^2$) receive little weight, while precise measurements receive heavy weight.
3. **Prior as an extra measurement:** The prior mean $\mu$ enters the formula symmetrically, acting as if it were a pseudo-measurement with value $\mu$ and variance $\sigma_0^2$.
4. **The Normal Case:** If $\Theta$ and all $W_i$ are normally distributed, the conditional expectation $\mathbf{E}[\Theta \mid X_1, \dots, X_n]$ is linear. In that case, the linear estimator is the globally optimal LMS estimator:
   $$\hat{\Theta}_L = \mathbf{E}[\Theta \mid X_1, \dots, X_n]$$
   Linear LMS estimation can be viewed as equivalent to operating under normal distribution assumptions.

---

## Choosing the Regressors in Linear LMS

There is an important distinction between general LMS and linear LMS when transforming the data:
- In unconstrained LMS, one-to-one transformations preserve information. For example, knowing $X^3$ gives the exact same information as knowing $X$. Therefore:
  $$\mathbf{E}[\Theta \mid X] = \mathbf{E}[\Theta \mid X^3]$$
- In linear LMS, the choice of data representation matters completely:
  $$\hat{\Theta} = aX + b \quad \text{is not the same as} \quad \hat{\Theta} = aX^3 + b$$
- Furthermore, one can construct nonlinear functions of $X$ while retaining a linear estimation architecture by using multiple derived features:
  $$\hat{\Theta} = a_1 X + a_2 X^2 + a_3 X^3 + b$$
  This remains a linear LMS problem in terms of solving for the coefficients $a_1, a_2, a_3, b$, but it generates a polynomial estimator in $X$.

---

## Exercises

### Exercise 1: Single Date Delay Model
Romeo and Juliet start dating, but Juliet will be late on any date by a random amount $X$, uniformly distributed over the interval $[0, \theta]$. The parameter $\theta$ is unknown and is modeled as the value of a random variable $\Theta$, uniformly distributed between $0$ and $1$ hour. Juliet is late by an amount $x$ on their first date.
1. Determine the updated posterior distribution of $\Theta$ given $X = x$.
2. Find the MAP estimate of $\Theta$ based on the observation $X = x$.
3. Find the LMS estimate of $\Theta$ based on the observation $X = x$.
4. Calculate and compare the conditional mean squared errors for the MAP and LMS estimates.
5. Derive the linear LMS estimator of $\Theta$ based on $X$.
6. Calculate the conditional mean squared error for the linear LMS estimator and compare it to the LMS and MAP results.

### Exercise 2: Multiple Date Delay Model
Using the delay model from Exercise 1, suppose Romeo observes Juliet's delays $X_1 = x_1, \dots, X_n = x_n$ across the first $n$ dates. Assume that conditional on $\Theta = \theta$, the delays $X_1, \dots, X_n$ are conditionally independent and uniformly distributed on $[0, \theta]$.
1. Find the posterior distribution $f_{\Theta \mid X_1, \dots, X_n}(\theta \mid x_1, \dots, x_n)$.
2. Identify the corresponding MAP and LMS estimates of $\Theta$.

---

## Sources

- Lecture 22 slides and lecture transcript: Framework of Bayesian estimation, conditional expectation as the optimal LMS estimator, conditional variance as conditional MSE, properties of estimation error, derivation and interpretation of linear LMS, multiple observation LLMS, the additive independent noise example, and feature choice.
- Recitation 22 problem set: Uniform prior date-delay model (Exercises 1 and 2), corresponding to Examples 8.2, 8.7, 8.12, and 8.15 in the course textbook.

---

[← 21. Introduction to Bayesian Inference](21-introduction-to-bayesian-inference.md) · [Contents](index.md) · [23. Classical Statistics and Parameter Estimation →](23-classical-statistics-and-parameter-estimation.md)
