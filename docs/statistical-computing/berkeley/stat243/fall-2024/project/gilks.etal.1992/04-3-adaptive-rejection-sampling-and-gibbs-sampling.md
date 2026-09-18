---
title: 3. Adaptive Rejection Sampling and Gibbs Sampling
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. Adaptive Rejection Sampling and Gibbs Sampling

## 3.1. Gibbs Sampling

Complex data sets can often be modelled in the form of a number $n$ of submodels, each submodel $m = 1, \dots, n$ expressing the conditional distribution $[\beta_m \mid \{\beta_i; \, i \in S_m\}]$ of parameter $\beta_m$ conditional on a set of other parameters indexed by $S_m$. We shall refer to $[\beta_m \mid \{\beta_i; \, i \in S_m\}]$ as the model conditional for $\beta_m$. Usually model conditionals are defined hierarchically (Lindley and Smith, 1972). For notational convenience we shall regard data as fixed parameters. Gibbs sampling (Geman and Geman, 1984) is often a convenient method of obtaining the joint posterior distribution of the parameters of a hierarchical model, and of any marginal or conditional posteriors of interest (Gelfand and Smith, 1990; Gelfand *et al.*, 1990).

To perform Gibbs sampling, initial values are assigned to each free parameter. Then for each free parameter $\beta_m$ in turn the current parameter value is replaced by a value drawn from the full conditional distribution of that parameter $[\beta_m \mid \{\beta_i; \, i = 1, \dots, m - 1, m + 1, \dots, n\}]$, conditioning on all the remaining parameters (fixed or free). We shall denote this full conditional distribution by $[\beta_m \mid\ ]$. This resampling is repeated many times. Under fairly weak regularity conditions Geman and Geman (1984) show that this process generates samples from the joint posterior distribution of the free parameters, conditional on the fixed parameters (data). From these samples any posterior summaries of interest can be straightforwardly calculated (e.g. the mean, median, 5th and 95th centiles of the sampled values for each free parameter). For further details see Gelfand *et al.* (1990).

TABLE 1
*Evaluations of $h(x)$ required to sample one point from the standard normal density, using adaptive rejection sampling, for various starting abscissae*†

| Starting abscissae $x_1$ | Starting abscissae $x_2$ | Mean number‡ of evaluations of $h(x)$ | Maximum number‡ of evaluations of $h(x)$ |
| :--- | :--- | :--- | :--- |
| $-0.5$ | $0.5$ | $3.1$ | $7$ |
| $-1.0$ | $1.0$ | $2.8$ | $6$ |
| $-2.0$ | $2.0$ | $3.3$ | $6$ |
| $-5.0$ | $5.0$ | $4.4$ | $8$ |
| $-10.0$ | $10.0$ | $5.1$ | $8$ |
| $-9.0$ | $1.0$ | $4.3$ | $8$ |
| $-8.0$ | $2.0$ | $4.4$ | $7$ |
| $-7.0$ | $3.0$ | $4.5$ | $8$ |
| $-6.0$ | $4.0$ | $4.4$ | $8$ |

†1000 simulations.
‡Including evaluations at the starting abscissae $x_1$ and $x_2$.

Thus Gibbs sampling requires specification of the full conditional distribution $[\beta_m \mid\ ]$ for each parameter $\beta_m$. For a hierarchical model the full conditional for $\beta_m$ can be expressed in terms of the model conditionals:
$$[\beta_m \mid\ ] \propto [\beta_m \mid \{\beta_i; \, i \in S_m\}] \prod_{\{j: m \in S_j\}} [\beta_j \mid \{\beta_i; \, i \in S_j\}] \tag{5}$$
where the product is over all submodels which condition on $\beta_m$. Here proportionality implies that the full conditional distribution for $\beta_m$ differs from the right-hand side of expression (5) only by a multiplicative term which does not depend on $\beta_m$, but which will in general depend on other $\{\beta_i; \, i \ne m\}$. Unless there is conjugacy between each of the producted terms in expression (5), the full conditional will not correspond to a common distribution and it will not be possible to derive a closed form for the proportionality constant in expression (5). Moreover, since it is the product of possibly many terms, expression (5) will be computationally expensive to evaluate repeatedly. Section 4 provides an example in which over 150 terms form the product in expression (5); in other applications several thousand terms could be involved.

## 3.2. Log-concavity

Now, most commonly used densities are concave on the logarithmic scale, with respect to both random variable and distributional parameters (see Table 2). Moreover, when this is not so, the log-density may be concave with respect to a suitably transformed random variable or parameter (taking account of the Jacobian if transforming the random variable) (Table 2). In particular if $[x \mid \mu, \sigma]$ is any density parameterized in terms of a location parameter $\mu$ and scale parameter $\sigma$, such that
$$[x \mid \mu, \sigma] = \frac{1}{\sigma} f\left(\frac{x - \mu}{\sigma}\right)$$
for some function $f(z)$, and if $\ln f(z)$ is concave with respect to its argument $z$, then the logarithm of the density $[x \mid \mu, \sigma]$ is concave with respect to $x$, $\mu$ and $\tau = \sigma^{-1}$, but not necessarily with respect to $\sigma$ or other functions of $\sigma$.

Therefore, taking logarithms in expression (5), often all the terms in
$$h(\beta_m) = \ln [\beta_m \mid \{\beta_i; \, i \in S_m\}] + \sum_{\{j: m \in S_j\}} \ln [\beta_j \mid \{\beta_i; \, i \in S_j\}] \tag{6}$$
will be concave with respect to $\beta_m$, and consequently also $h(\beta_m)$ will be concave with respect to $\beta_m$, being the sum of concave terms. In these circumstances adaptive rejection sampling can be used to sample efficiently from $h(\beta_m)$. For adaptive rejection sampling of $\beta_m$ we require of $[\beta_j \mid \{\beta_i; \, i \in S_j\}]$ in equation (6) only that it be continuous, differentiable and log-concave with respect to $\beta_m$. Thus $[\beta_j \mid \{\beta_i; \, i \in S_j\}]$ could be a discrete distribution of $\beta_j$. We have included some common discrete distributions in Table 2.

TABLE 2
*Log-concavity for common probability density functions $f(x)$*†

| $f(x)$ | Parameters | $\log f(x)$ concave with respect to | $\log f(x)$ not concave with respect to |
| :--- | :--- | :--- | :--- |
| Normal | Mean $\mu$, variance $\sigma^2$ | $x$, $\mu$, $1/\sigma$, $\log\sigma$ | $\sigma$ |
| Log-normal | Location $\mu$, scale $\sigma^2$ | $\log x$, $\mu$, $1/\sigma$, $\log\sigma$ | $x$, $\sigma$ |
| Exponential | Rate $\lambda$ | $x$, $\log x$, $\lambda$ | |
| Gamma | Index $r$, rate $\lambda$ | $\log x$, $x$ (if $r \geqslant 1$), $\lambda$, $r$ | $x$ (if $r < 1$) |
| Beta | Shape $a$, $b$ | $\text{logit}(x)$, $x$ (if $a, b \geqslant 1$), $a$, $b$ | |
| Double exponential | Location $\alpha$, scale $\beta$ | $x$, $\alpha$, $1/\beta$, $\log\beta$ | $\beta$ |
| Weibull | Shape $b$, scale $a$ | $\log x$, $x$ (if $b \geqslant 1$), $a$, $b$ | |
| Logistic | Location $\alpha$, scale $\beta$ | $x$, $\alpha$, $1/\beta$ | $\beta$ |
| Pareto | Shape $\theta$, bound $x_0$ | $\log x$, $1/x$ (if $\theta \geqslant 1$), $x_0$, $\log x_0$, $\theta$ | $x$ |
| Gumbel or extreme value | Location $\alpha$, scale $\beta$ | $x$, $\alpha$, $1/\beta$ | $\beta$ |
| $t$ | Degrees of freedom $k$ | | $x$ |
| $F$ | Degrees of freedom $m, n$ | $\log x$ | $x$ |
| $\chi^2$ | Degrees of freedom $k$ | $\log x$, $x$ (if $k \geqslant 2$), $k$ | $x$ (if $k < 2$) |
| Bernoulli | Proportion $p$ | $p$, $\text{logit}(p)$ | |
| Binomial | Proportion $p$, index $r$ | $p$, $\text{logit}(p)$ | |
| Poisson | Rate $\lambda$ | $\lambda$ | |
| Geometric | Proportion $p$ | $p$, $\text{logit}(p)$ | |
| Negative binomial | Proportion $p$, index $r$ | $p$, $\text{logit}(p)$ | |

†In considering concavity of $\log f(x)$ with respect to transformations of the random variable $x$, the Jacobian of the transformation was taken into account. The table also contains common discrete distributions with continuous parameters. The notation follows that of Mood *et al.* (1974).

## 3.3. Multivariate Full Conditionals

Adaptive rejection sampling, as we have described it, permits only univariate sampling. However, if $\beta_m$ in formulae (5) and (6) is multivariate, then (univariate) adaptive rejection sampling can still be used. To see this note that, for each element $\beta_{mk}$ of $\beta_m$, the univariate full conditional $[\beta_{mk} \mid\ ]$ is proportional to the multivariate full conditional $[\beta_m \mid\ ]$. Therefore, if $[\beta_m \mid\ ]$ is log-concave with respect to $\beta_m$ (which it may be, by invoking the argument of Section 3.2), then $[\beta_{mk} \mid\ ]$ will be log-concave with respect to $\beta_{mk}$. Thus the Gibbs sampler can be implemented to update each element $\beta_{mk}$ in turn, using adaptive rejection sampling with $h(\beta_{mk}) = \ln [\beta_m \mid\ ]$.

---

[← 2. Adaptive Rejection Sampling](03-2-adaptive-rejection-sampling.md) · [Up: contents](index.md) · [4. Application to Monoclonal Antibody Reactivity →](05-4-application-to-monoclonal-antibody-reactivity.md)
