---
title: "24. Linear Regression and Hypothesis Testing"
course: "MIT 6.041SC"
chapter: 24
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Linear Regression and Hypothesis Testing

## What this covers

This chapter covers two core methodologies of classical statistics: linear regression for modeling relationships between variables and binary hypothesis testing for choosing between two competing models. We assume familiarity with maximum likelihood estimation, confidence intervals, and the central limit theorem.

## Review: Maximum Likelihood and Confidence Intervals

In classical statistics, the underlying parameter $\theta$ is an unknown, fixed constant rather than a random variable. We observe data $X$ drawn from a distribution governed by a candidate model:

$$X \sim p_X(x; \theta) \quad \text{or} \quad X \sim f_X(x; \theta)$$

The principle of **maximum likelihood estimation** (MLE) is to select the parameter value that makes the observed data most plausible:

$$\hat{\theta}_{\text{ML}} = \arg\max_\theta p_X(x; \theta)$$

In contrast, Bayesian Maximum A Posteriori (MAP) estimation treats $\Theta$ as a random variable with a prior distribution $p_\Theta(\theta)$ and maximizes the posterior:

$$\max_\theta p_{\Theta \mid X}(\theta \mid x) = \max_\theta \frac{p_{X \mid \Theta}(x \mid \theta)p_\Theta(\theta)}{p_X(x)}$$

Formally, when the prior $p_\Theta(\theta)$ is flat (constant over all $\theta$), MAP estimation yields the same mathematical expression as MLE. Conceptually, however, they differ: MAP finds the parameter value that is most probable given the data, whereas MLE finds the parameter value under which the observed data had the highest likelihood of occurring.

When estimating the expectation $\theta = \mathbf{E}[X]$ from $n$ independent and identically distributed (i.i.d.) observations $X_1, \dots, X_n$, the natural point estimator is the sample mean:

$$\hat{\Theta}_n = \frac{1}{n}\sum_{i=1}^n X_i$$

By the weak law of large numbers, $\hat{\Theta}_n$ converges in probability to $\theta$. 

To quantify uncertainty, we construct a $1 - \alpha$ **confidence interval** $[\hat{\Theta}_n^-, \hat{\Theta}_n^+]$ satisfying:

$$\mathbf{P}(\hat{\Theta}_n^- \le \theta \le \hat{\Theta}_n^+) \ge 1 - \alpha \quad \text{for all } \theta$$

Because $\theta$ is a deterministic constant, the endpoints $\hat{\Theta}_n^-$ and $\hat{\Theta}_n^+$ are random variables. The correct interpretation is that the interval generation procedure has at least a $1 - \alpha$ probability of covering the true parameter $\theta$. Using the Central Limit Theorem (CLT), the sample mean is approximately normal for large $n$. For a standard normal critical value $z$ satisfying $\Phi(z) = 1 - \alpha/2$, the approximate $1 - \alpha$ confidence interval is:

$$\mathbf{P}\left(\hat{\Theta}_n - \frac{z\sigma}{\sqrt{n}} \le \theta \le \hat{\Theta}_n + \frac{z\sigma}{\sqrt{n}}\right) \approx 1 - \alpha$$

When the true variance $\sigma^2$ is unknown, it is either replaced by an empirical estimate from the data or by an upper bound.

## Simple Linear Regression

Consider paired observations $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$, such as high school SAT scores ($x_i$) and college GPAs ($y_i$). We hypothesize an approximate affine relationship between the explanatory variable $x$ and the response variable $y$:

$$y \approx \theta_0 + \theta_1 x$$

Because data points do not fall precisely on a straight line, any chosen line produces prediction residuals $y_i - (\theta_0 + \theta_1 x_i)$. The standard least squares criterion chooses the parameters $\theta_0$ (intercept) and $\theta_1$ (slope) that minimize the sum of squared errors:

$$\min_{\theta_0, \theta_1} \sum_{i=1}^n (y_i - \theta_0 - \theta_1 x_i)^2$$

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Fitted regression line through scattered data points with vertical residual lines">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="295" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="25" y="30" text-anchor="middle" font-size="12" fill="currentColor">y</text>
  <!-- Fitted Line: y = 175 - 0.45*x approximately -->
  <line x1="50" y1="165" x2="280" y2="60" stroke="currentColor" stroke-width="2"/>
  <!-- Residual dashes -->
  <line x1="80" y1="151" x2="80" y2="170" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="120" y1="133" x2="120" y2="105" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="160" y1="115" x2="160" y2="135" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="210" y1="92" x2="210" y2="70" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="250" y1="74" x2="250" y2="90" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Data Points -->
  <circle cx="80" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="120" cy="105" r="3.5" fill="currentColor"/>
  <circle cx="160" cy="135" r="3.5" fill="currentColor"/>
  <circle cx="210" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="250" cy="90" r="3.5" fill="currentColor"/>
  <!-- Residual label -->
  <text x="127" y="122" font-size="11" fill="currentColor">residual</text>
</svg>
<figcaption>Linear regression fits a line to minimize the sum of squared vertical residuals between the data points and the fitted values.</figcaption>
</figure>

### Maximum Likelihood Justification

The least squares objective can be derived probabilistically. Suppose that each response $Y_i$ is generated by:

$$Y_i = \theta_0 + \theta_1 x_i + W_i$$

where the disturbances $W_i \sim \mathcal{N}(0, \sigma^2)$ are independent and identically distributed normal random variables. Under this model, $Y_i \sim \mathcal{N}(\theta_0 + \theta_1 x_i, \sigma^2)$, and by independence the joint likelihood is:

$$f_{Y_1, \dots, Y_n}(y_1, \dots, y_n; \theta_0, \theta_1) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left\{ -\frac{(y_i - \theta_0 - \theta_1 x_i)^2}{2\sigma^2} \right\}$$

$$= c \cdot \exp\left\{ -\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \theta_0 - \theta_1 x_i)^2 \right\}$$

Maximizing this likelihood with respect to $\theta_0$ and $\theta_1$ is equivalent to maximizing the log-likelihood:

$$\ln f = \ln c - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \theta_0 - \theta_1 x_i)^2$$

Because $\sigma^2 > 0$, maximizing this expression is identical to minimizing the sum of squared errors. Fitting a line via least squares corresponds to performing maximum likelihood estimation under an additive i.i.d. normal noise assumption.

### Derivation and Interpretation of Estimates

To find the minimizers $\hat{\theta}_0$ and $\hat{\theta}_1$, we set the partial derivatives of the objective function with respect to $\theta_0$ and $\theta_1$ to zero. Defining the sample means:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i, \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$$

Setting the partial derivative with respect to $\theta_0$ to zero yields:

$$\sum_{i=1}^n -2(y_i - \theta_0 - \theta_1 x_i) = 0 \implies \sum_{i=1}^n y_i - n\theta_0 - \theta_1 \sum_{i=1}^n x_i = 0$$

Dividing by $n$ gives:

$$\hat{\theta}_0 = \bar{y} - \hat{\theta}_1 \bar{x}$$

Setting the derivative with respect to $\theta_1$ to zero and substituting $\hat{\theta}_0$ produces the closed-form solution for the slope:

$$\hat{\theta}_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}$$

#### Probabilistic Interpretation

Consider a random variable formulation where $Y = \theta_0 + \theta_1 X + W$, with $W$ having zero mean and being independent of $X$. Taking expectations:

$$\mathbf{E}[Y] = \theta_0 + \theta_1 \mathbf{E}[X] \implies \theta_0 = \mathbf{E}[Y] - \theta_1 \mathbf{E}[X]$$

Replacing the theoretical expectations $\mathbf{E}[Y]$ and $\mathbf{E}[X]$ with their sample averages $\bar{y}$ and $\bar{x}$ yields $\hat{\theta}_0 = \bar{y} - \hat{\theta}_1 \bar{x}$.

Assuming without loss of generality that $\mathbf{E}[X] = \mathbf{E}[Y] = 0$, multiplying $Y$ by $X$ and taking expectations gives:

$$\mathbf{E}[XY] = \mathbf{E}[X(\theta_0 + \theta_1 X + W)] = \theta_0 \mathbf{E}[X] + \theta_1 \mathbf{E}[X^2] + \mathbf{E}[XW]$$

Since $\mathbf{E}[X] = 0$ and $\mathbf{E}[XW] = \mathbf{E}[X]\mathbf{E}[W] = 0$, this simplifies to:

$$\operatorname{cov}(X, Y) = \theta_1 \operatorname{var}(X) \implies \theta_1 = \frac{\operatorname{cov}(X, Y)}{\operatorname{var}(X)} = \frac{\mathbf{E}[(X - \mathbf{E}[X])(Y - \mathbf{E}[Y])]}{\mathbf{E}[(X - \mathbf{E}[X])^2]}$$

The estimator $\hat{\theta}_1$ is the empirical plug-in estimator of this ratio, replacing the true covariance and variance with their sample estimates:

$$\widehat{\operatorname{cov}}(X,Y) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}), \quad \widehat{\operatorname{var}}(X) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2$$

The factor of $1/n$ cancels in the numerator and denominator, producing the formula for $\hat{\theta}_1$.

## Multiple Regression and Model Selection

The linear regression framework extends directly to multiple explanatory variables. If a response variable $y_i$ depends on multiple factors $(x_i, x_i', x_i'')$, such as SAT score, family income, and parental education:

$$y_i \approx \theta_0 + \theta x_i + \theta' x_i' + \theta'' x_i''$$

The least squares estimation problem becomes:

$$\min_{\theta_0, \theta, \theta', \theta''} \sum_{i=1}^n (y_i - \theta_0 - \theta x_i - \theta' x_i' - \theta'' x_i'')^2$$

Setting the derivatives with respect to each parameter to zero yields a system of linear equations that can be solved numerically or expressed in closed form using matrix algebra.

### Nonlinear Transformations of Variables

Linear regression requires linearity in the unknown parameters $\theta$, but not in the raw input variables. If the relationship between $x$ and $y$ exhibits curvature, we can define transformed variables $h(x)$. For instance, a quadratic model:

$$y \approx \theta_0 + \theta_1 x^2$$

is handled by defining a transformed feature $\tilde{x}_i = h(x_i) = x_i^2$ and solving:

$$\min_{\theta_0, \theta_1} \sum_{i=1}^n (y_i - \theta_0 - \theta_1 h(x_i))^2$$

This remains a linear regression problem. 

Care must be exercised when choosing transformations. With $n$ data points, choosing a polynomial of degree $n - 1$ produces $n$ parameters, allowing the curve to interpolate the data points with zero residual error. However, such an overparameterized model captures noise rather than underlying structure, leading to poor predictive ability.

### Practical Metrics and Pitfalls

In applied regression analysis, standard statistical software reports several auxiliary measures:

1. **Standard Error:** An estimate of the residual standard deviation $\sigma$, indicating the inherent scale of noise in the predictions.
2. **Confidence Intervals for $\theta_i$:** Quantification of the sampling variability associated with each parameter estimate.
3. **Coefficient of Determination ($R^2$):** A measure of explanatory power reflecting the fraction of the total sample variance of $Y$ explained by the regression model:
   $$\frac{\operatorname{var}(Y) - \operatorname{var}(Y \mid X)}{\operatorname{var}(Y)}$$

Several structural pitfalls can invalidate regression analyses:

* **Heteroskedasticity:** When the noise variance is not constant across the range of the explanatory variable (i.e., $\operatorname{var}(W_i)$ depends on $x_i$). Least squares places equal weight on all squared errors, causing the fitted parameters to be excessively driven by high-variance regions rather than the cleaner, low-variance data.
* **Multicollinearity:** When two or more explanatory variables are highly correlated (e.g., test scores from a first and second sitting). The individual parameter estimates become unstable and sensitive to minor perturbations in the data.
* **Correlation vs. Causation:** Establishing an empirical linear association between $X$ and $Y$ does not imply that variations in $X$ cause changes in $Y$. The association could be due to reverse causality or unobserved confounding variables that influence both.

## Binary Hypothesis Testing

In hypothesis testing, instead of estimating a continuous parameter, we decide between two candidate models:
* The **null hypothesis**, denoted $H_0$: $X \sim p_X(x; H_0)$ (or $f_X(x; H_0)$)
* The **alternative hypothesis**, denoted $H_1$: $X \sim p_X(x; H_1)$ (or $f_X(x; H_1)$)

To make a decision, the observation space is partitioned into two regions:
* A **rejection region** $R$: reject $H_0$ (and decide $H_1$) if the observed data $x \in R$.
* The acceptance region $R^c$: accept $H_0$ if $x \notin R$.

### Types of Errors

Any decision rule can commit two distinct types of errors:

1. **Type I Error (False Rejection / False Alarm):** $H_0$ is true, but the decision rule rejects $H_0$. The probability of this error is denoted by $\alpha$:
   $$\alpha(R) = \mathbf{P}(X \in R; H_0)$$
2. **Type II Error (False Acceptance / Missed Detection):** $H_1$ is true, but the decision rule fails to reject $H_0$. The probability of this error is denoted by $\beta$:
   $$\beta(R) = \mathbf{P}(X \notin R; H_1)$$

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Two overlapping normal densities showing Type I error alpha and Type II error beta separated by a threshold">
  <!-- Baseline -->
  <line x1="20" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <!-- H0 PDF: Center x=100, scale=35 -->
  <path d="M 20 179 C 50 178 70 140 100 60 C 130 140 150 178 180 179 L 180 180 L 20 180 Z" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <!-- H1 PDF: Center x=200, scale=35 -->
  <path d="M 120 179 C 150 178 170 140 200 60 C 230 140 250 178 280 179 L 280 180 L 120 180 Z" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <!-- Threshold line at x=150 -->
  <line x1="150" y1="30" x2="150" y2="180" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Shaded Type I error: H0 tail right of 150 -->
  <path d="M 150 173 C 160 177 170 179 180 179 L 180 180 L 150 180 Z" fill="currentColor" fill-opacity="0.15"/>
  <!-- Shaded Type II error: H1 tail left of 150 -->
  <path d="M 120 179 C 130 179 140 177 150 173 L 150 180 L 120 180 Z" fill="currentColor" fill-opacity="0.15"/>
  <!-- Labels -->
  <text x="100" y="50" text-anchor="middle" font-size="12" fill="currentColor">f(x; H₀)</text>
  <text x="200" y="50" text-anchor="middle" font-size="12" fill="currentColor">f(x; H₁)</text>
  <text x="150" y="22" text-anchor="middle" font-size="12" fill="currentColor">threshold ξ</text>
  <text x="165" y="170" font-size="11" fill="currentColor">α</text>
  <text x="135" y="170" font-size="11" fill="currentColor">β</text>
  <text x="90" y="200" text-anchor="middle" font-size="12" fill="currentColor">Accept H₀</text>
  <text x="210" y="200" text-anchor="middle" font-size="12" fill="currentColor">Reject H₀ (R)</text>
</svg>
<figcaption>Overlapping densities under $H_0$ and $H_1$. The decision threshold partitions the domain, creating a trade-off between the Type I error probability $\alpha$ and the Type II error probability $\beta$.</figcaption>
</figure>

There is an inherent trade-off between $\alpha$ and $\beta$. Shifting the threshold to the right reduces the rejection region, lowering the probability of false rejection $\alpha$, but increasing the probability of missed detection $\beta$.

### The Likelihood Ratio Test (LRT)

To determine the structure of an optimal decision rule, we look first at the Bayesian formulation. If prior probabilities $\mathbf{P}(H_0)$ and $\mathbf{P}(H_1)$ exist, the MAP decision rule chooses $H_1$ if:

$$\mathbf{P}(H_1 \mid X = x) > \mathbf{P}(H_0 \mid X = x)$$

Applying Bayes' rule:

$$\frac{p_{X \mid H}(x \mid H_1)\mathbf{P}(H_1)}{p_X(x)} > \frac{p_{X \mid H}(x \mid H_0)\mathbf{P}(H_0)}{p_X(x)}$$

Canceling the common denominator $p_X(x)$ and rearranging yields:

$$\frac{p_{X \mid H}(x \mid H_1)}{p_{X \mid H}(x \mid H_0)} > \frac{\mathbf{P}(H_0)}{\mathbf{P}(H_1)}$$

In the classical, non-Bayesian framework, prior probabilities $\mathbf{P}(H_0)$ and $\mathbf{P}(H_1)$ are undefined. However, the ratio of likelihoods remains the principled quantity for discriminating between the models. The non-Bayesian **Likelihood Ratio Test (LRT)** rejects $H_0$ when:

$$L(x) = \frac{p_X(x; H_1)}{p_X(x; H_0)} > \xi \quad (\text{discrete case})$$

$$L(x) = \frac{f_X(x; H_1)}{f_X(x; H_0)} > \xi \quad (\text{continuous case})$$

Here, $L(x)$ measures how much more consistent the observation $x$ is with $H_1$ relative to $H_0$. 

The threshold $\xi > 0$ governs the trade-off between $\alpha$ and $\beta$. The standard statistical methodology fixes a tolerable upper bound for the Type I error probability, $\alpha$ (often set to a significance level such as $0.05$):

$$\mathbf{P}(L(X) > \xi; H_0) = \alpha$$

The threshold $\xi$ is chosen to satisfy this constraint under $H_0$. The resulting Type II error probability $\beta$ is then determined by evaluating the probability of falling below $\xi$ under the distribution $H_1$.

## Exercises

### Exercise 1: Photon Counting and Temperature Estimation
A blackbody at fixed but unknown temperature $\theta$ radiates photons of all wavelengths. The PMF for the number of photons $K$ observed in a given wavelength range over a very short time interval is:

$$p_K(k; \theta) = \frac{1}{Z(\theta)} e^{-k/\theta}, \quad k = 0, 1, 2, \dots$$

where $Z(\theta)$ is a normalization factor (the partition function). Photon emissions in non-overlapping time intervals are statistically independent.

1. Determine the normalization factor $Z(\theta)$.
2. Compute the expected value $\mu_K = \mathbf{E}_\theta[K]$ and variance $\sigma_K^2 = \operatorname{var}_\theta(K)$ of the photon count measured in a 1-second interval.
3. Given photon counts $k_1, \dots, k_n$ across $n$ non-overlapping 1-second intervals, find the maximum likelihood estimator $\hat{\theta}_n$ in terms of the sample average $s_n = \frac{1}{n} \sum_{i=1}^n k_i$, assuming the body is hot ($\theta \gg 1$) so that $\frac{1}{e^{1/\theta}-1} \approx \theta$.
4. For the sample mean estimator $\hat{K} = \frac{1}{n} \sum_{i=1}^n K_i$, find the sample size $n$ required so that the noise-to-signal ratio $\frac{\sigma_{\hat{K}}}{\mu_{\hat{K}}}$ is equal to $0.01$.
5. Using the Central Limit Theorem, specify a 95% confidence interval for the mean photon count under the conditions of part 4.

### Exercise 2: Linear vs. Quadratic Regression
Consider the five observed pairs $(x_i, y_i)$:

| $x_i$ | 0.8 | 2.5 | 5.0 | 7.3 | 9.1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y_i$ | -2.3 | 20.9 | 103.5 | 215.8 | 334.0 |

We evaluate two candidate models:
* A linear model: $Y_i = \theta_0 + \theta_1 x_i + W_i$, with $W_i \sim \mathcal{N}(0, \sigma_1^2)$ i.i.d.
* A quadratic model: $Y_i = \beta_0 + \beta_1 x_i^2 + V_i$, with $V_i \sim \mathcal{N}(0, \sigma_2^2)$ i.i.d.

1. Find the maximum likelihood estimates of the linear model parameters $(\theta_0, \theta_1)$.
2. Find the maximum likelihood estimates of the quadratic model parameters $(\beta_0, \beta_1)$.

## Sources

* Review of classical estimation, maximum likelihood, and confidence intervals: slides 2–3; transcript [01:11]–[09:02].
* Simple linear regression formulation, least squares derivation via normal MLE, and closed-form estimators: slides 4–5; transcript [09:02]–[24:14].
* Multiple regression, nonlinear features, $R^2$, and practical regression pitfalls (heteroskedasticity, multicollinearity, causality): slides 6–7; transcript [24:14]–[42:22].
* Binary hypothesis testing, Type I and II errors, and the Likelihood Ratio Test (Bayesian and non-Bayesian): slides 8–9; transcript [42:22]–[50:13].
* Exercises: adapted directly from Fall 2010 Recitation 24 problem set.
* Not covered in supplied material: specific derivations for parameter confidence intervals in regression; quantitative tests for multicollinearity.

---

[← 23. Classical Statistics and Parameter Estimation](23-classical-statistics-and-parameter-estimation.md) · [Contents](index.md) · [25. Classical Hypothesis Testing →](25-classical-hypothesis-testing.md)
