---
title: Estimation in statistical models
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Estimation in statistical models

**Source:** [`reader/estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Having observed $X \sim P_\theta$, an unknown distribution in the model $\cP = \{P_\theta:\; \theta \in \Theta\}$, we will be interested in learning something about $\theta$. In *estimation*, we guess the value of some quantity of interest $g(\theta)$, called the *estimand*. Our guess is called the *estimate* $\delta(X)$, calculated based on the data. The method $\delta(\cdot)$ that we use to calculate the estimate is called the *estimator*.

**Example (Binomial, continued):** Returning to our binomial example from above, we may want to estimate $g(\theta) = \theta$, the probability of the coin landing heads. A natural estimator is $\delta_0(X) = X/n$, the fraction of coins landing heads in any given trial. One favorable property of this estimator is that it is *unbiased*, meaning that $\EE_\theta \delta_0(X) = g(\theta)$, for all $\theta \in \Theta$.

There are many potential estimators for any given problem, so our goal will generally be to find a good estimator. To evaluate and compare estimators, we must have a way of evaluating how successful an estimator is in any given realization of the data. To this end we introduce the *loss function* $L(\theta, d)$, which measures *how bad* it is to guess that $g(\theta) = d$ when $\theta$ is the true parameter value. Typically loss functions are non-negative, with $L(\theta, d) = 0$ if and only if $g(\theta) = d$ (no loss from a perfect guess) but this is not required.

In any given problem, we should ideally choose the loss that best measures our own true (dis)utility function, but in practice people fall back on simple defaults. One loss function that is especially popular for its mathematical convenience is the *squared-error loss*, defined by $L(\theta, d) = (d-g(\theta))^2$.

Whereas the loss function measures how (un)successful an estimator is in one realization of the data, we would really like to evaluate an estimator's performance over the whole range of possible data sets $X$ that we might observe. This is measured by the *risk function*, defined as

$$
R(\theta; \delta(\cdot)) = \EE_\theta [\, L(\theta, \delta(X)) \,] = \int L(\theta, \delta(x)) \td P_\theta(x)
$$

**Remark on notation:** The subscript in the previous expression tells us *which* of our candidate probability distributions to use in evaluating the expectation. In some other fields, people may use the subscript to indicate "what randomness to integrate over," with the implication that any random variable that does not appear in the subscript should be held fixed. In our course, it should generally be assumed that any expectation or probability is integrating over the joint distribution of the entire data set; if we want to hold something fixed we will condition on it. Recall that, for now, the parameter $\theta$ is fixed unless otherwise specified.

The semicolon in the risk function is meant to indicate we are viewing it primarily as a function of $\theta$. That is, we should think of and estimator $\delta$ as having a risk function $R(\theta)$, and the second input in $R(\theta; \delta)$ is telling us which estimator's risk function to evaluate at $\theta$.

The risk for the squared-error loss is called the *mean squared error* (MSE):

$$
\textrm{MSE}(\theta; \delta) = \EE_\theta\left[\,(\delta(X) - g(\theta))^2\,\right]
$$

**Example (Binomial, continued):** To calculate the MSE of our estimator $\delta_0 = X/n$, note that $\EE_\theta[X/n] = \theta$ (the estimator is *unbiased*). As a result, we have

$$
\begin{aligned}
\textrm{MSE}(\theta; \delta_0) &= \EE_\theta\left[ \left(\frac{X}{n} - \theta\right)^2\right] \\[7pt]
&= \text{Var}_\theta(X/n)\\[3pt]
&= \frac{1}{n}\theta(1-\theta)
\end{aligned}
$$

One reason why we might consider estimators other than $\delta_0$ is that, if $n$ is small, our estimate could be quite noisy. As an extreme example, if $n=1$ we will always estimate either $\theta = 0$ or $\theta = 1$, both of which would be extreme conclusions to draw after a single trial. One simple way of reducing the variance is to pretend that we flipped the coin an additional $m$ times resulting in $a$ heads and $m-a$ tails. This will tend to shade our estimate toward $a/m$, reducing the risk if $\theta = a/m$ but possibly increasing the risk for other values of $\theta$.

<!--# Add widget to show the distribution of estimates for a variety of theta, n, a, m values -->

We show the risk function for several alternative estimators of this form below:

$$
\delta_1(X) = \frac{X + 1}{n + 2}, \quad \delta_2(X) = \frac{X + 2}{n + 4}, \quad \delta_3(X) = \frac{X + 1}{n}
$$

The last estimator, $\delta_3$, is another example where we add something to $X$ in the numerator but nothing $n$ in the denominator.

```r
library(RColorBrewer)

n = 16

---

[← Statistical models](01-statistical-models.md) · [Up: contents](index.md) · [risk function of estimator (X + synth.heads) / (n + synth.flips) →](03-risk-function-of-estimator-x-synth-heads-n-synth-flips.md)
