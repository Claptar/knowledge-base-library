---
title: Gaussian sequence model
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/empirical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Gaussian sequence model

**Source:** [`reader/empirical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Recall that we have discussed a variety of estimators for
$\theta \in \RR^d$ in the *Gaussian sequence model*

$$X \sim N_d(\theta, I_d)$$

Note that this model is somewhat more general than it appears. If
$X_1,\ldots,X_n \simiid N_d(\theta, \sigma^2 I_d)$ for known
$\sigma^2> 0$, we could make a sufficiency reduction to obtain

$$Z = \frac{1}{\sigma\sqrt{n}} \sum\_i X_i \sim N_d(\theta, I_d).$$ For
simplicity we will discuss the \`\`vanilla'' version here, but we can
always translate our results to the more general setting via this
transformation.

We'll generally assume in what follows that the loss we care about is
the squared error loss, summed over the coordinates:\
$$L(\theta, d) =
\|\delta(X) - \theta\|\^2 = \sum\_j (\delta\_j(X) - \theta\_j)\^2$$

The most obvious estimator is $\delta_0(X) = X$ itself, which we could justify in a variety of ways: we've shown that it is the UMVU estimator for $\theta$ and also the objective Bayes estimator, since the flat prior on $\theta$ coincides with the Jeffreys prior (as it does for any location model). It also happens to be the maximum likelihood estimator (MLE), which we'll discuss later in the course.

### Bayes estimators

If we introduce the Bayesian prior $\theta_i \simiid N(0,\tau^2)$ then we have seen that we arrive at the Bayes estimator $\frac{\tau^2}{1+\tau^2}X$.

We can think of this as a tuning parameter for a generic *linear shrinkage estimator*
$$\delta_\zeta(X) = (1-\zeta)X,$$
where $\zeta \in [0,1]$ is in effect a tuning parameter we will call the *shrinkage parameter*. Taking $\zeta = 0$ corresponds to using $X$ as our estimator for $\theta$, and taking $\zeta = 1/(1+\tau^2)$ corresponds to the Bayes estimator where $\tau^2$ is known.

If we aren't sure which $\zeta$ to use, for example because we have some *a priori* uncertainty about $\tau^2$, we can try to estimate it from the data using hierarchical Bayes, which we've seen would give the final estimator
$$\delta(X) = (1 - \EE[\zeta \mid X]) X = \delta_{\hat\zeta_{\text{Bayes}}(X)}(X),$$
so we are in effect estimating $\zeta$ from the whole data set and then plugging it in as a data-adaptive tuning parameter.

The hierarchical Bayes estimator uses a Bayes estimator for $\zeta$, but if we take an empirical Bayes approach we could try other estimators, such as the MLE or UMVU. If $d \geq 3$ then the UMVU estimator for $\zeta$ is
$$\hat{\zeta}_{\text{UMVU}}(X) = \frac{d-2}{\|X\|^2},$$
which we can verify using the identity
$$\EE[1/Y] = \frac{1}{d-2}, \quad \text{ if } Y \sim \chi_d^2 = \text{Gamma}(d/2, 2), \text{ for } d > 2,$$
which is proved in the handwritten notes. Plugging in $\hat\zeta_\text{UMVU}$ results in an estimator called the *James-Stein* estimator,
$$ \delta_{\text{JS}}(X)= \left(1 - \frac{d-2}{\|X\|^2}\right)X = \delta_{\hat\zeta_{\text{UMVU}}}(X) $$

### James-Stein Paradox

While the James-Stein estimator can be motivated as an empirical Bayes estimator, it is surprisingly good even without making any Bayesian assumptions at all.

For $d \geq 3$, the estimator $X$ is actually *inadmissible* as an estimator of $\theta$ under squared error loss:

$$\text{MSE}(\theta, \delta_{JS}) < \text{MSE}(\theta, X) \quad \text{ for all } \theta \in \mathbb{R}^d.$$

It is not surprising for a Bayes estimator to beat the UMVU estimator *an average* with respect to some prior, but this result holds for *every fixed value* of the parameter $\theta$.

In fact, since there is nothing special about shrinking towards $0$. We could use a version of the estimator that shrinks toward any other $\theta_0 \in \RR^d$, i.e.
$$ \tilde delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X - \theta_0\|^2}\right) (X - \theta_0)$$.
This also dominates $\delta_0$ because it is just the James-Stein estimator we'd get if we made the substitution
$$Y = X - \theta_0 \sim N_d(\mu, I_d), \quad \text{ for } \mu = \theta - \theta_0.$$
The translation-invariance of the Gaussian location model means that the James-Stein estimator for $\mu$ using $Y$ also dominates the estimator $\hat\mu_0(Y) = Y$, which corresponds to the estimator $\delta_0(X) = \hat\mu_0 + \theta_0 = X$ for $\theta$.

This result was received as a shock in the 1950s when it first came out. It was regarded for a long time as a curiosity, but it was eventually understood to carry the deep implication that shrinkage makes sense, especially in higher-dimensional problems, even when we don't have a Bayes justification for it.


### Linear shrinkage estimators

Even without introducing a Bayesian prior for $\theta$, we can motivate our linear shrinkage estimator purely from the perspective of trading a bit of bias for a reduction in variance.

We can start by calculating the MSE (considered as a purely frequentist risk function) for a single coordinate, using the bias-variance tradeoff:
$$
\begin{aligned}
\EE_\theta[(\theta - \delta_i(X))^2]
&= (\theta_i - \EE_\theta (1-\zeta)X_i)^2 + \text{Var}_\theta (1-\zeta)X_i\\
&= (\zeta\theta_i)^2 + (1-\zeta)^2
\end{aligned}
$$
Summing over the $d$ coordinates gives
$$\text{MSE}(\theta; \delta) = \zeta^2\|\theta\|^2 + d(1-\zeta)^2,$$
where the first term represents the squared bias and the second is the variance.

Note that the risk is a quadratic in $\zeta$ with positive second derivative, so we can minimize it by setting
$$0 = \frac{d}{d\zeta}\text{MSE}(\theta) = 2\zeta\|\theta\|^2 - 2(1-\zeta)d,$$
leading to
$$\zeta^*(\theta) = \frac{d}{d+\|\theta\|^2} = \frac{1}{1+\|\theta\|^2/d},$$
which looks remarkably similar to $\frac{1}{1+\tau^2}$, which is the Bayes-optimal $\zeta$ under the Gaussian prior from the last section.

One thing to notice is that $\zeta^*(\theta) > 0$, so a small amount of shrinkage helps. But the correct amount of shrinkage depends on $\|\theta\|^2$: if $\|\theta\|^2 \to \infty$, the correct amount of shrinkage goes to $0$, so any fixed $\zeta$ would overshoot for some $\theta$ parameters.

It turns out the James-Stein estimator manages to estimate the correct amount of shrinkage from the data, in such a way that we avoid overshooting most of the time, and thereby improve on the MSE for *any* $\theta$.

To understand why, we need a general way to calculate the MSE for an estimator with an adaptive $\hat\zeta(X)$. Stein's unbiased risk estimator will give us that.

---

[Up: contents](index.md) · [Stein's Unbiased Risk Estimator →](02-stein-s-unbiased-risk-estimator.md)
