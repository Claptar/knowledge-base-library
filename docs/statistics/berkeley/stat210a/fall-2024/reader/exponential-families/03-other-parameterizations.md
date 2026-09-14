---
title: Other parameterizations
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Other parameterizations

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Sometimes instead of parameterizing $\cP$ by the natural parameter $\eta$, it is more convenient to parameterize the family by another parameter $\theta$. Then we can write the density in terms of this alternative parameterization as

$$
p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x), \quad \text{ where } B(\theta) = A(\eta(\theta)).
$$

The Poisson distribution, if indexed by the mean $\lambda$, is an example of such an alternative parameterization, with $\eta(\lambda) = \log\lambda$ and $B(\lambda) = \lambda$. Another example is the normal family:

**Example (Normal):** Consider the model $X\sim \cN(\mu, \sigma^2)$, for $\mu\in\RR$ and $\sigma^2>0$. The usual parameter vector for this problem is $\theta = (\mu, \sigma^2)$. The density in that parameterization is

$$
p_\theta(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{-(\mu-x)^2/2\sigma^2\right\}.
$$

Expanding the square and raising the $\sqrt{2\pi\sigma^2}$ into the exponent, we can massage the density into the exponential family structure we are looking for:

$$
p_\theta(x)
= \exp\left\{\frac{\mu}{\sigma^2} x - \frac{1}{2\sigma^2}x^2 - \frac{\mu}{2\sigma^2} - \frac{1}{2}\log\left(2\pi\sigma^2\right)\right\},
$$

which we can recognize as an exponential family with sufficient statistic $T(x) = (x,x^2)$, natural parameter $\eta(\theta) = (\mu/\sigma^2,-1/2\sigma^2)$, carrier density $h(x)=1$, and log-partition function

$$
B(\theta) = \frac{\mu^2}{2\sigma^2} + \frac{1}{2}\log\left(2\pi\sigma^2\right).
$$

We can rewrite the log-partition function in terms of $\eta_1 = \mu^2/2\sigma^2$ and $\eta_2=-1/2\sigma^2$ to complete the natural parameterization:

$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)}, \quad \text{ for } A(\eta) = \frac{-\eta_1^2}{4\eta_2} + \frac{1}{2}\log(-\pi/\eta_2)
$$

Hence, the Gaussian is the (only) exponential family with sufficient statistic $T(x) = (x,x^2)$, and carrier density $h(x)=1$, with respect to the Lebesgue measure on $\RR$.

**Example (Binomial):** Next, consider the model $X \sim \text{Binom}(n,\theta)$, which has pmf

$$
p_\theta(x) = \theta^x (1-\theta)^{n-x}\binom{n}{x}.
$$

We can again massage this into canonical form by raising the parameters into the exponent and collecting terms

$$
\begin{aligned}
p_\theta(x)
&= \exp\left\{x\log\theta + (n-x)\log(1-\theta)\right\}\binom{n}{x}\\
&= \exp\left\{x\log\left(\frac{\theta}{1-\theta}\right)-n\log(1-\theta)\right\}\binom{n}{x},
\end{aligned}
$$

which we recognize as an exponential family structure with $T(x)=x$, natural parameter $\eta=\log\left(\frac{\theta}{1-\theta}\right)$ The natural parameter $\eta$ is called the *log-odds* or *logit*, which is used in classification models such as logistic regression and the many extensions thereof.

**Example (Beta):** The Beta distribution is a common family of distributions on the unit interval. If $X \sim \text{Beta}(\alpha,\beta)$ then $X$ has pdf

$$
\begin{aligned}
p_{\alpha,\beta}(x)
&= \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}\\[5pt]
&= \exp\{\alpha \log x + \beta\log (1-x) - \log B(\alpha,\beta)\}\cdot \frac{1}{x(1-x)},
\end{aligned}
$$

where $B(\alpha,\beta) = \int_0^1 t^{\alpha-1}(1-t)^{\beta-1}\td t$ is called the *beta function*. We recognize this as an exponential family with $T(x) = (\log x, \log(1-x))$, $\eta = (\alpha,\beta)$, and $h(x) = \frac{1}{x(1-x)}$, though as always there are other ways to decompose the density.

In addition to these examples, we could add most of the distributional families detailed on Wikipedia: the Gamma, multinomial, Dirichlet, Pareto, Wishart, and many others. We will see more exponential family examples throughout the course.

---

[← Differential identities](02-differential-identities.md) · [Up: contents](index.md) · [Exponential tilting →](04-exponential-tilting.md)
