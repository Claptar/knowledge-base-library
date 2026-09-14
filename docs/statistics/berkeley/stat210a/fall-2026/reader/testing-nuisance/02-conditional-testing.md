---
title: Conditional testing
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conditional testing

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Conditional testing offers very effective and fairly strategy for dealing with nuisance parameters. To introduce the idea, consider a simple problem where we observe a binomial random variable with a random sample size. This is a very common situation: for example, suppose that we conduct a survey asking people which of two candidates they favor, and the number of respondents is a random number.

Let $N$ represent the sample size and assume that, conditional on $N = n$, we will observe a binomial random variable $X \sim \text{Binom}(n,theta)$.

**Example (Random sample size with known distribution):**
First, consider a simple setting where we actually know the distribution of $N$, for example $N \sim \text{Pois}(10)$; then having observed $N$ and $X$, we want to test $H_0:\;\theta \leq \frac{1}{2}$ vs $H_1:\;\theta > \frac{1}{2}$. The full likelihood for the model is
$$
p_\theta(n,x) = \frac{10^n e^{-10}}{n!} \cdot \binom{n}{x}\theta^x(1-\theta)^{n-x}, \quad \text{ for } 0 \leq x \leq n.
$$
There is no UMP test[^1], but we have at least two natural options:

$\log \frac{p_{\theta_1}}{p_{1/2}}(n,x) = x \log \frac{\theta_1}{1-\theta_1} - n\log2(1-\theta_1)$

**Option 1: Marginal test** Marginally, we have $X \sim \text{Pois}(10\cdot \theta)$. If we ignore $N$, this distribution has monotone likelihood ratio in $X$, so we could reject if $X > c_\alpha^{(1)}$, the upper-$\alpha$ quantile of a $\text{Pois}(5)$ distribution. This marginal test, which we can call $\phi_1$, will certainly have $\EE_\theta \phi_1(X) \leq \alpha$ for any $\theta \leq \frac{1}{2}$.

**Option 2: Conditional test** Conditionally, we have $X \mid N=n \sim \text{Binom}(n,\theta)$, which also has monotone likelihood ratio in $n$. So we can reject if $X > c_\alpha^{(2)}(n)$, the upper-$\alpha$ quantile of a $\text{Binom}\left(n,\frac{1}{2}\right)$ distribution. This conditional test, which we can call $\phi_2$, will have
$$
\EE_\theta \left[\phi_2(X) \mid N=n\right] \leq \alpha, \quad \text{ for all } n\geq 0, \text{ and } \theta \leq \frac{1}{2},
$$
hence we also have $\EE_\theta \phi_2(X) \leq \alpha$ for $\theta \leq \frac{1}{2}$.

If we let $q_{\theta}(x \mid n)$ represent the pmf of $X$ given $N=n$, then the latter test $\phi_2$ is UMP in the **conditional model**
$$
\mathcal{Q}_n = \{q_\theta(x \mid n):\; \theta \in \Theta\},
$$
consisting of the candidate conditional distributions for $X$ given $N=n$ (i.e., $\text{Binom}(n,\theta)$).

In general, any level-$\alpha$ (unbiased) test in the conditional model is also level-$\alpha$ (unbiased) in the marginal model: the marginal power is the average conditional power, so any guarantee that the conditional power is below (or above) $\alpha$ also holds perforce for the marginal power. For the same reason, any valid (unbiased) confidence interval in the conditional model is also valid (resp. unbiased) marginally.

The **conditionality principle** holds that, since $N$ is ancillary in this case, we should condition on its value. Informally, the observed value of $N$ has nothing to do with the parameter $\theta$ that we care about, so we shouldn't really think of it as data informing our inference about $\theta$ even if it is random. Instead, we should just condition on its value and work in the conditional model, treating it as fixed.

Whether or not we accept the conditionality principle, conditioning on part of the data can be a very helpful way to deal with nuisance parameters, as we see next:

**Example (Random sample size with unknown distribution):**
Now, we can modify the previous example to assume that $N$ is drawn from an *unknown* distribution $P^N$ on $\{0,1,\ldots\}$, but continuing to assume that $X \mid N=n \sim \text{Binom}(n,\theta)$. Having introduced the infinite-dimensional nuisance parameter $P^N$, we no longer have the option of rejecting for (marginally) large values of $X$.

Now the marginal test is no longer even an option, but we can still use the conditional test just as before, since the conditional model $\mathcal{Q}_n$ is no different than it was when $N$ was ancillary. In other words, conditioning on $N$ completely removes the nuisance parameter $P^N$ from the problem. This might be a bad thing if $N$ were for some reason highly informative about $\theta$, but if we don't think it is then we lose little and gain much by conditioning on $N$.

**Example (Comparing two Poissons, continued):** We continue the previous example of comparing independent $X\sim\text{Pois}(\mu)$ and $Y\sim\text{Pois}(\nu)$. If we let $N = X + Y \sim \text{Pois}(\mu + \nu)$, then we have a submodel of the last example:[^2]
$$
X \mid N = n \sim \text{Binom}(n,\theta), \quad \text{ for } \theta = \frac{\mu}{\mu + \nu}.
$$

$$
\begin{aligned}
\PP_{\mu,\nu}(X=x \mid X+Y=n) &= \frac{\PP_\mu(X=x)\PP_\nu(Y=x-n)}{\PP_{\mu+\nu}(X+Y=n)}\\[5pt]
&= \frac{\mu^x\nu^{n-x}e^{-\mu-\nu}}{x!y!} \,\big/\, \frac{n!}{(\mu+\nu)^ne^{-(\mu+\nu)}}\\[5pt]
&= \binom{n}{x}\theta^x(1-\theta)^{n-x}.
\end{aligned}
$$


Since $Y = N-X$ is recoverable from $N$ and $X$, we can simply regard $(N,X)$ as our full data set. Conditioning on $N$ removes the nuisance parameter $\lambda = \mu + \nu$ from the problem, leaving $H_0:\;\mu \leq \nu \iff \theta \leq \frac{1}{2}$, and $H_1:\;\mu > \nu \iff \theta > \frac{1}{2}$.

As we will see next, this beautiful reduction was not a miraculous coincidence, but a direct consequence of the exponential family structure of the model.

[^1]: The likelihood ratio for each alternative $\theta_1 > \frac{1}{2}$ is a different linear combination of $x$ and $n$:

[^2]: To derive this, note that

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Multiparameter exponential families →](03-multiparameter-exponential-families.md)
