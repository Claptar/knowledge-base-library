---
title: 1 Hierarchical Bayes
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Hierarchical Bayes

Published

September 28, 2023

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{minimize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
$$

## 1 Hierarchical Bayes {.anchored number="1" anchor-id="hierarchical-bayes"}

The full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.

### 1.1 Example: Predicting Batting Averages {.anchored number="1.1" anchor-id="example-predicting-batting-averages"}

Predict a batter’s true batting average from $n_i$ at-bats, $X_i$ hits: $X_i|\theta_i \sim \text{Binom}(n_i, \theta_i)$

Pool info across players $i=1,\ldots,m$ via hierarchical model:

$$
\begin{aligned}
\alpha, \beta &\sim \pi_0(\alpha, \beta) \quad \text{(hyperprior)} \\
\theta_i|\alpha, \beta &\sim \text{Beta}(\alpha, \beta), \quad i=1,\ldots,m \\
X_i|\theta_i, n_i &\sim \text{Binom}(n_i, \theta_i), \quad i=1,\ldots,m
\end{aligned}
$$

$$
\mathbb{E}[\theta_i|X] = \mathbb{E}[\mathbb{E}[\theta_i|X, \alpha, \beta]|X] = \mathbb{E}\left[\frac{\alpha + X_i}{\alpha + \beta + n_i}|X\right]
$$

Use all $X_1,\ldots,X_m$ to learn a good prior on $\theta_i$.

Note: There is always an equivalent model where we marginalize over $\alpha, \beta$ and just write a more complicated prior on $\theta$. The hierarchical version may give better intuition or computational strategies.

### 1.2 Gaussian Hierarchical Model {.anchored number="1.2" anchor-id="gaussian-hierarchical-model"}

$$
\begin{aligned}
\theta_i &\sim N(\mu, \tau^2), \quad i=1,\ldots,d \\
X_i|\theta_i &\sim N(\theta_i, \sigma^2), \quad i=1,\ldots,d
\end{aligned}
$$

Posterior mean:

$$
\mathbb{E}[\theta_i|X] = \mathbb{E}[\mathbb{E}[\theta_i|X, \mu, \tau^2]|X] = \mathbb{E}\left[\frac{\tau^2}{\tau^2 + \sigma^2}X_i + \frac{\sigma^2}{\tau^2 + \sigma^2}\mu|X\right]
$$

Linear shrinkage estimator: Bayes optimal shrinkage estimated from data.

Likelihood for $\mu, \tau^2$ (marginalizing over $\theta_i$):

$$
\begin{aligned}
X_i|\mu, \tau^2 &\sim N(\mu, \tau^2 + \sigma^2) \\
\bar{X} &\sim N(\mu, \frac{\tau^2 + \sigma^2}{n}) \\
S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 &\sim \frac{\tau^2 + \sigma^2}{n-1}\chi^2_{n-1}
\end{aligned}
$$

Define $B = \tau^2 + \sigma^2$ (amount of shrinkage):

$$
\delta(x) = \mathbb{E}[\mathbb{E}[\theta_i|X, B]|X] = \mathbb{E}\left[\frac{B - \sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar{X}|X\right]
$$

Estimated from entire data set:

$$
\begin{aligned}
\bar{X} &\sim N(\mu, \frac{B}{n}) \\
(n-1)S^2 &\sim B\chi^2_{n-1}
\end{aligned}
$$

Conjugate prior (scale mixture):

$$
\pi(B|\lambda, \nu) \propto B^{-\nu/2-2}\exp(-\frac{\lambda}{2B})
$$

$$
B|X \sim \text{InvGamma}\left(\frac{n+\nu}{2}, \frac{\lambda + (n-1)S^2}{2}\right)
$$

$$
\mathbb{E}\left[\frac{1}{B}|X\right] = \frac{n+\nu}{\lambda + (n-1)S^2}
$$

$$
\delta_i(x) = \frac{(n-3)S^2}{(n-1)S^2 + \lambda}X_i + \frac{\lambda + 2S^2}{(n-1)S^2 + \lambda}\bar{X}
$$

Pseudo-data: $\nu, \lambda$ with $\nu \approx 2, \lambda \approx \nu\sigma^2$

Might want to truncate prior to $[\sigma^2, \infty)$ if $\lambda$ small.

### 1.3 Graphical Form {.anchored number="1.3" anchor-id="graphical-form"}

For hyperparameters $\alpha, \beta$:

```
     α, β
    /  |  \
   θ₁  θ₂  θ₃
   |   |   |
   X₁  X₂  X₃
```

These are the distributions associated with a factor for each vertex in a DAG $(V,E)$:

$$
p(z) = \prod_{i=1}^{|V|} p(z_i|z_{\text{pa}(i)})
$$

For this model:

$$
p(\alpha, \beta, \theta_1,\ldots,\theta_m, X_1,\ldots,X_m) = p(\alpha, \beta)\prod_{i=1}^m p(\theta_i|\alpha, \beta)p(X_i|\theta_i)
$$

---

[Up: contents](index.md) · [2 Markov Chain Monte Carlo (MCMC) →](02-2-markov-chain-monte-carlo-mcmc.md)
