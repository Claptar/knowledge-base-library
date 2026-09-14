---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework6.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework6.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework6.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework6.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

SURE gives us a reasonable way of selecting a tuning parameter for estimation problems, and can help us choose a tuning parameter that achieves the near optimal performance. Also, regularization methods that set a lot of parameters to zero can substantially reduce the MSE in sparse problems, by eliminating all the variance for most of the coordinates.

**Problem 4** (Shrinking toward the average).

Assume we observe data from a Gaussian sequence model $X \sim N_d(\theta, I_d)$ with $d \geq 4$, and we want to estimate $\theta\in \mathbb{R}^d$ with low mean-squared error loss. Instead of shrinking toward zero, however, we want to shrink toward $\overline{X}$. This implements an inductive bias that the $\theta_i$ values should be close to each other, as opposed to assuming they should be close to zero.

We can use the estimator whose $i$th coordinate is $$\delta_{gamma,i}(X) = \gamma \overline{X} + (1-\gamma) X_i = \overline{X} + (1-\gamma)(X_i - \overline{X}),$$ leading to $$\delta_{\gamma}(X) = \overline{X} 1_d + (1-\gamma)(X - \overline{X}1_d),$$ where $1_d = (1,1,\ldots,1) \in \mathbb{R}^d$. The course reader calculated the SURE for this model when we have a fixed $\gamma$.

We will instead consider a popular version of the James–Stein estimator, which uses an adaptive choice $$\hat\gamma(X) = \frac{d-3}{\|X - \overline{X} 1_d\|^2} = \frac{d-3}{\sum_i (X_i - \overline{X})^2},$$ leading to $$\delta_{\text{JS}_2}(X) = \overline{X} 1_d + \left(1 - \frac{d-3}{\|X - \overline{X} 1_d\|^2}\right) (X - \overline{X} 1_d)$$

1.  As with the previous James–Stein estimator, we can motivate this estimator in a similar way by empirical Bayes in a model with $\theta_i \overset{\text{i.i.d.}}{\sim}N(\mu, \tau^2)$. If we want we can write $\zeta = (1+\tau^2)^{-1}$ as before. Show that $\delta_{\text{JS}_2}$ is the empirical Bayes estimator for this prior, where we estimate the hyperparameters $(\mu,\zeta)$ by UMVU.

2.  Derive an unbiased estimator for the risk $\text{MSE}(\theta; \delta_{\text{JS}_2})$. Your estimator should be a function of the data $X$, and should not involve any unknown parameters like $\mu$, $\zeta$, or $\theta$.

3.  Find an expression for the MSE of $\delta_{\text{JS}_2}$ as a function of $\theta$, and show that it dominates the MSE of $\delta_0(X) = X$ for all $\theta \in \mathbb{R}^d$. Evaluate your expression in the case where $\theta_1 = \theta_2 = \cdots = \theta_d$.

4.  Now make a change of variables to $Z = Q'X$, where $q_1 = d^{-1/2}1_d$ and $q_2,\ldots,q_d$ are any completion of an orthonormal basis for $\mathbb{R}^d$, and $Q= [q_1 \cdots q_d] \in \mathbb{R}^{d\times d}$. Show that $$Z \sim  N_d(\mu, I_d), \quad \text{ where } \mu_1 = d^{-1/2}\sum_i\theta_i.% \quad \text{ and } \|\theta\|^2 = \left(\begin{pmatrix}d^{-1/2}\sum_i\theta_i\\ \nu\end{pmatrix}$$ Show that $Q'\delta_{\text{JS}_2}(X)$, as an estimator of $\mu$, could be characterized as estimating $\mu_1$ as $Z_1$ (without any shrinkage), and estimating $\mu_{-1}=(\mu_2,\ldots,\mu_d)$ via the original James–Stein estimator on the $(d-1)$-variate normal $Z_{-1} \sim N_{d-1}(\mu_{-1},I_{d-1})$. Use this construction to re-derive the results in part (c).

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
