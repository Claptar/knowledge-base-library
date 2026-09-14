---
title: Stein's Unbiased Risk Estimator
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/jamesstein.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/jamesstein.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Stein's Unbiased Risk Estimator

**Source:** [`reader/jamesstein.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/jamesstein.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Stein's Lemma

The first ingredient in finding the MSE of $\delta_\text{JS}$ is a lemma called *Stein's Lemma*:

**Theorem (Stein's lemma, univariate):** Suppose $X \sim N(\theta, \sigma^2)$, and that $h:\; \RR \to \RR$ is differentiable, with $\EE|\dot{h}(X)| < \infty$. Then we have
$$\Cov(X, h(X)) = \EE[(X-\theta)h(X)] = \sigma^2\EE[\dot{h}(X)].$$

*Proof*:


Next, we will do the calculation for $\theta = 0$ and $\sigma^2 = 1$. Then
$$\EE[Xh(X)] = \int_{-\infty}^\infty xh(x)\phi(x)\,dx = \int_{-\infty}^\infty \dot{h}(x)\phi(x)\,dx,$$
where we've used integration by parts:
$$\dot{\phi}(x) = \frac{d}{dx} \frac{1}{\sqrt{2\pi}}e^{-x^2/2} = -x \frac{1}{\sqrt{2\pi}}e^{-x^2/2} = -x\phi(x).$$
(A slightly more rigorous version is in the handwritten notes: we can assume wlog $h(0) = 0$ because otherwise we could center it by using $k(X) = h(X) - h(0)$, which has the same covariance with $X$. Then we can break up the integral into an integral from $0$ to $\infty$ and another from $-\infty$ to $0$, and do integration by parts a bit more carefully for each.)

For more general $\theta$, we can write $X = \theta + \sigma Z$, where $Z \sim N(0,1)$. Then applying the result for $k(z) = h(\theta + \sigma z)$, we have

$$\EE[(X-\theta) h(X)] = \sigma\EE[Zh(\theta + \sigma Z)] = \sigma^2\EE[\dot{h}(\theta + \sigma Z)] = \sigma^2\EE[\dot{h}(X)],$$
giving the general result.

We will need the multivariate version of Stein's lemma. For a function $h:\; \RR^d \to \RR^d$, define the Jacobian matrix $Dh \in \RR^{d\times d}$ by
$$(Dh(x))_{ij} = \frac{\partial h_i}{\partial x_j}(x).$$

Define the **Frobenius norm** $A \in \RR^{d\times d}$ as
$$\|A\|_F = \left(\sum_{ij} A_{ij}^2\right)^{1/2}.$$

Now we can state our theorem:

**Theorem (Stein's lemma, multivariate):** Assume $X \sim N_d(\theta; \sigma^2 I_d)$, and $h:\;\RR^d \to \RR^d$ is differentiable with $\EE\|Dh(X)\|_F < \infty$. Then
$$ \EE[(X-\theta)'h(X)] = \sigma^2 \EE \text{tr}(Dh(X)) = \sigma^2 \sum_i \EE \frac{\partial h_i}{\partial x_i} (X).$$

*Proof:* The proof follows from the proof of the univariate version if we observe that the distribution of $X_i$ conditional on the other coordinates $X_{-i}$ is $N(\theta, \sigma^2)$. Then we have
$$ \EE\left[(X_i - \theta_i)h_i(X) \mid X_{-i}\right]
= \sigma^2 \EE\left[\frac{\partial h_i}{\partial x_i}(X_i) \mid X_{-i} \right].$$
Taking expectations gives
$$ \EE\left[(X_i - \theta_i)h_i(X)\right]
= \sigma^2 \EE\left[\frac{\partial h_i}{\partial x_i}(X_i) \right],$$
and summing over $i$ gives the result.

### Stein's unbaised risk estimator (SURE)

We can obtain an unbiased estimator of the MSE for almost any differentiable estimator $\delta(X)$ in the Gaussian sequence model, if we apply Stein's lemma to the function $h(x) = x - \delta(x)$. We only need the derivative of $h$ to satisfy the condition of Stein's lemma, which it does for most differentiable estimators.

Using the identity $\|a - b\|^2 = \|a\|^2 + \|b\|^2 - 2a'b$, we have for $h(x) = x - \delta(x)$,
$$
\begin{aligned}
\text{MSE}(\theta; \delta)
&= \EE_\theta\|\delta(X) - \theta\|^2\\
&= \EE_\theta\|X - h(X) - \theta\|^2\\
&= \EE_\theta\|X - \theta\|^2 + \EE_\theta\|h(X)\|^2 - 2\EE_\theta \left[(X - \theta)'h(X)\right]\\
&= \sigma^2 d + \EE_\theta\|h(X)\|^2 - 2\sigma^2 \EE_\theta \text{tr}(Dh(X)).
\end{aligned}
$$
Thus, if $\sigma^2$ is known, we obtain the unbiased estimator
$$ \widehat{\text{MSE}}(X) = \sigma^2 d +  \|h(X)\|^2 - 2 \sigma^2 \text{tr}(Dh(X)).$$

### Example: shrinking toward $\overline{X}$

As an example, we can estimate the MSE of an estimator that shrinks $X_i$ partway toward the average estimate across the $d$ coordinates, $\overline{X} = \frac{1}{d}\sum_i X_i$:
$$
\delta_i^\gamma(X) = (1-\gamma) X_i  + \gamma \overline{X}.
$$
We can think of this as making a bet that most of the $\theta_i$ values are close to $\bar{\theta} = \frac{1}{d}\sum_i \theta_i$. Then
$$
h(X) = X - \delta^\gamma(X) = \gamma(X - \overline{X} 1_d),
$$
and
$$
Dh(X)_{ii} = \frac{\partial}{\partial X_i} \gamma(X_i - \overline{X}) = \gamma (1-1/d) \Rightarrow \text{tr}(Dh(X)) = (d-1)\gamma
$$
An unbiased estimator for the MSE of $\delta^\gamma$ is then
$$
\widehat{\text{MSE}}^\gamma(X) = \sigma^2 d +  \gamma^2(d-1)V^2 - 2(d-1) \gamma \sigma^2,
$$
where $V^2 = \frac{1}{d-1}\sum_i (X_i-\overline{X})^2$ is the sample variance. Take note that the $X_i$ values are not assumed to be i.i.d. here, since their means are generically different.

We can use this estimator in two different ways. The simplest way would be to calculate the actual MSE by taking the estimator's expectation, which we know is the actual MSE of $\delta^\gamma$. The only random variable is $V^2$. Write $X_i = \theta_i + Z_i$ where $Z_i \sim N(0,\sigma^2)$. Then we have
$$
\frac{1}{d-1}\sum_i\EE_\theta(X_i-\overline{X})^2 = \frac{1}{d-1}\sum_i (\theta_i - \bar{\theta})^2 + \frac{1}{d-1}\sum_i \EE(Z_i - \overline{Z})^2 = \beta^2 + \sigma^2,
$$
where $\beta^2 = \frac{1}{d-1}\sum_i(\theta_i - \bar{\theta})^2$ is the sample variance of the $\theta_i$ values. Plugging in this expectation and collecting terms, we obtain the MSE
$$
\text{MSE}^\gamma(\theta) = \EE_\theta\left[\widehat{\text{MSE}}^\gamma(X)\right] = \sigma^2 + (d-1)(1-\gamma)^2\sigma^2 + (d-1)\gamma^2\beta^2.
$$
We can solve for the optimal value $\gamma^*(\beta) = \frac{\sigma^2}{\beta^2+\sigma^2}$, which unsurprisingly depends on $\beta^2$. If $\beta^2 = 0$ then all $\theta_i$ values are equal so we should set $\gamma = 1$ (shrink fully to the sample mean), but if $\beta^2 \gg \sigma^2$ we should take $\gamma \to 0$ (shrink very little).

We could also choose $\gamma$ adaptively to minimize this estimator. That is, we could take
$$
\hat\gamma(X) = \argmin_\gamma \widehat{\text{MSE}}^\gamma(X) = \sigma^2/V^2,
$$
which we could think of as an estimator of $\gamma^*(X)$ since $V^2$ is unbiased for $\beta^2+\sigma^2$. If we plug in $\hat\gamma(X)$ we get a new adaptive shrinkage estimator which is not the same as $\delta^\gamma$ for any fixed $\gamma$, and we could use the same idea to calculate its MSE, if we wanted to.

---

[← Gaussian sequence model](01-gaussian-sequence-model.md) · [Up: contents](index.md) · [Risk of the James-Stein estimator →](03-risk-of-the-james-stein-estimator.md)
