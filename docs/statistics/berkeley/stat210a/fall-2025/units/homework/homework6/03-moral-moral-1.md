---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework6.tex
source_file: sources/berkeley-stat210a/fall-2025/units/homework/homework6.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`units/homework/homework6.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework6.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

SURE gives us a reasonable way of selecting a tuning parameter for estimation problems, and can help us choose a tuning parameter that achieves the near optimal performance. Also, regularization methods that set a lot of parameters to zero can substantially reduce the MSE in sparse problems, by eliminating all the variance for most of the coordinates.

**Problem 3** (Shrinking toward the average). Assume we observe data from a Gaussian sequence model $X \sim N_d(\theta, I_d)$ with $d \geq 4$, and we want to estimate $\theta\in \mathbb{R}^d$ with low mean-squared error loss. Instead of shrinking toward zero, however, we want to shrink toward $\overline{X}$. This implements an inductive bias that the $\theta_i$ values should be close to each other, as opposed to assuming they should be close to zero.

We can use the estimator whose $i$th coordinate is $$\delta_{gamma,i}(X) = \gamma \overline{X} + (1-\gamma) X_i = \overline{X} + (1-\gamma)(X_i - \overline{X}),$$ leading to $$\delta_{\gamma}(X) = \overline{X} 1_d + (1-\gamma)(X - \overline{X}1_d),$$ where $1_d = (1,1,\ldots,1) \in \mathbb{R}^d$. The course reader calculated the SURE for this model when we have a fixed $\gamma$.

We will instead consider a popular version of the James–Stein estimator, which uses an adaptive choice $$\hat\gamma(X) = \frac{d-3}{\|X - \overline{X} 1_d\|^2} = \frac{d-3}{\sum_i (X_i - \overline{X})^2},$$ leading to $$\delta_{\text{JS}_2}(X) = \overline{X} 1_d + \left(1 - \frac{d-3}{\|X - \overline{X} 1_d\|^2}\right) (X - \overline{X} 1_d)$$

1.  As with the previous James–Stein estimator, we can motivate this estimator in a similar way by empirical Bayes in a model with $\theta_i \overset{\text{i.i.d.}}{\sim}N(\mu, \tau^2)$. If we want we can write $\zeta = (1+\tau^2)^{-1}$ as before. Show that $\delta_{\text{JS}_2}$ is the empirical Bayes estimator for this prior, where we estimate the hyperparameters $(\mu,\zeta)$ by UMVU.

2.  Derive an unbiased estimator for the risk $\text{MSE}(\theta; \delta_{\text{JS}_2})$. Your estimator should be a function of the data $X$, and should not involve any unknown parameters like $\mu$, $\zeta$, or $\theta$.

3.  Find an expression for the MSE of $\delta_{\text{JS}_2}$ as a function of $\theta$, and show that it dominates the MSE of $\delta_0(X) = X$ for all $\theta \in \mathbb{R}^d$. Evaluate your expression in the case where $\theta_1 = \theta_2 = \cdots = \theta_d$.

4.  **Optional:** (Not graded, no extra points) If we make a change of variables to a certain $Z = f(X)$ with $Z \sim N_d(\mu, I_d)$, then $\delta_{\text{JS}_2}$ could be characterized as estimating $\mu_1$ as $Z_1$ (without any shrinkage), and estimating $\mu_{-1}=(\mu_2,\ldots,\mu_d)$ via the original James–Stein estimator on the $(d-1)$-variate normal $Z_{-1} \sim N_{d-1}(\mu_{-1},I_{d-1})$. Find such a transformation $f$ and use this construction to repeat part (c).

**Problem 4** (Tweedie’s formula). Besides James–Stein, another well-known empirical Bayes method is *Tweedie’s formula* for doing Bayes estimation of natural parameters in exponential family models.

Assume that the data come from a common $1$-parameter exponential family with a different parameter for each observation: $$X_i \overset{\text{ind.}}{\sim}p_{\eta_i}(x) = e^{\eta_i x - A(\eta)}h(x),$$

Additionally, assume $\eta_i \overset{\text{i.i.d.}}{\sim}\lambda(\eta)$ where $\lambda$ is an unknown density on $\mathbb{R}$ (so this is a non-parametric model for the prior). Define the marginal $$q(x) = \int p_\eta(x) \lambda_0(\eta),$$

1.  Show that the posterior distribution $\lambda(\eta_i \mid x_i)$ follows a one-parameter exponential family model with sufficient statistic $\eta_i$ and normalizing constant $B(x_i) = \log(q(x_i)/h(x_i))$.

2.  Use part (a) to find the Bayes posterior mean of $\eta_i$ given $X_i$.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
