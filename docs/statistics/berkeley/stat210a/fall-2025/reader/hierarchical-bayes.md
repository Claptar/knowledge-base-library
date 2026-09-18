---
title: Bayesian computation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hierarchical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Bayesian computation

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
\newcommand{\ep}{\varepsilon}
$$

## 1 Directed Graphical Models {number="1"}

## 2 Markov Chains {number="2"}

## 3 Markov Chain Monte Carlo {number="3"}

### 3.1 Hierarchical Bayes {.anchored number="3.1" anchor-id="hierarchical-bayes"}

The full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.

#### 3.1.1 Example: Predicting Batting Averages {.anchored number="3.1.1" anchor-id="example-predicting-batting-averages"}

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

#### 3.1.2 Gaussian Hierarchical Model {.anchored number="3.1.2" anchor-id="gaussian-hierarchical-model"}

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

#### 3.1.3 Graphical Form {.anchored number="3.1.3" anchor-id="graphical-form"}

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

### 3.2 Markov Chain Monte Carlo (MCMC) {.anchored number="3.2" anchor-id="markov-chain-monte-carlo-mcmc"}

Hierarchical models are very flexible, but often create big computational headaches:

$$
\pi(\theta|x) = \frac{p(x|\theta)\pi(\theta)}{\int p(x|\theta)\pi(\theta)d\theta}
$$

Numerator is usually nice, denominator often intractable.

Computational strategy: Set up a Markov chain with stationary distribution $\pi(\theta|x)$, run it to get approximate samples from $\pi(\theta|x)$.

#### 3.2.1 Definition of Markov Chain {.anchored number="3.2.1" anchor-id="definition-of-markov-chain"}

A stationary Markov chain with transition kernel $Q(y|x)$ and initial distribution $\pi_0(x)$ is a sequence of r.v.’s $X_0, X_1, \ldots$ where $X_0 \sim \pi_0$ and:

$$
P(X_{t+1} \in A | X_t, \ldots, X_0) = P(X_{t+1} \in A | X_t) = \int_A Q(y|X_t) dy
$$

Marginal distribution of $X_t$:

$$
\pi_t(y) = P(X_t \in A) = \int Q(y|x)\pi_{t-1}(x) dx
$$

This is a directed graphical model: $X_0 \to X_1 \to X_2 \to \cdots$

If $\pi(y) = \int Q(y|x)\pi(x) dx$, we say $\pi$ is a stationary distribution for $Q$.

A sufficient condition is detailed balance:

$$
\pi(x)Q(y|x) = \pi(y)Q(x|y)
$$

$$
\int_y Q(y|x)\pi(x) dx = \int_y \pi(y)Q(x|y) dy = \pi(y)
$$

A Markov chain with detailed balance is called reversible: $X_{t-1} | X_t \sim X_{t+1} | X_t$ if $\pi_t = \pi$.

#### 3.2.2 Theory {.anchored number="3.2.2" anchor-id="theory"}

If a Markov chain with stationary distribution $\pi$ is:

1.  Irreducible: $\forall x,y, \exists n: P(X_n = y | X_0 = x) > 0$
2.  Aperiodic: $\forall x, \gcd\{n > 0: P(X_n = x | X_0 = x) > 0\} = 1$

Then $\pi_t \to \pi$ in TV distance, regardless of $\pi_0$ (chain “forgets” $\pi_0$).

Strategy: Find $Q$ with stationary distribution $\pi(\theta|x)$, start at any $X_0$, run chain for a long time, then $X_t$ is approximately a sample from posterior for large $t$.

### 3.3 Gibbs Sampler {.anchored number="3.3" anchor-id="gibbs-sampler"}

For parameter vector $\theta = (\theta_1, \ldots, \theta_d)$:

Algorithm: 1. Initialize $\theta^{(0)}$ 2. For $t = 1, \ldots, T$: For $j = 1, \ldots, d$: Sample $\theta_j^{(t)} \sim p(\theta_j | \theta_{-j}^{(t-1)}, X)$ Record $\theta^{(t)}$

Variations: - Update one random coordinate $J \sim \text{Unif}(1,\ldots,d)$ - Update coordinates in random order

Advantage for hierarchical priors: only need to sample low-dimensional conditional distributions:

$$
p(\theta_i | \theta_{-i}, X, \alpha) \propto p(\theta_i | \theta_{\text{pa}(i)}) \prod_{j \in \text{ch}(i)} p(\theta_j | \theta_i)
$$

Especially easy if using conjugate priors at all levels; often can be parallelized.

#### 3.3.1 Gibbs Stationarity {.anchored number="3.3.1" anchor-id="gibbs-stationarity"}

Claim: If $\pi_t = \pi(\theta|X)$, then $\pi_{t+1} = \pi(\theta|X)$.

Proof (sketch): Consider updating only one fixed coordinate $j$: $\theta_j^{(t+1)} \sim p(\theta_j | \theta_{-j}^{(t)}, X)$ If $\theta^{(t)} \sim \pi(\theta|X)$, then $\theta^{(t+1)} \sim \pi(\theta|X)$ Updating any coordinate preserves posterior distribution Updating coordinates in any order also does

In theory: Pick initialization and valid kernel $Q$, sample long enough, get $\theta^{(t)} \sim \pi(\theta|X)$ Do it again $N$ more times, get $N$ samples from $\pi(\theta|X)$

In practice: How do we know we’ve sampled long enough? - Plot $\theta_i^{(t)}$ vs $t$, show how fast the MC mixes - Look for $\hat{R} = \frac{\text{between-chain variance}}{\text{within-chain variance}} \approx 1$

These methods are GOOD, NOT GREAT. Can be deceived, especially for bimodal posteriors.

Better approach: Burn-in then convergence. Estimate posterior based on $\theta^{(B+1)}, \ldots, \theta^{(B+N)}$

For function $f(\theta)$: $\hat{\mu}_f = \frac{1}{N} \sum_{t=B+1}^{B+N} f(\theta^{(t)})$

#### 3.3.2 Implementation Details Matter {.anchored number="3.3.2" anchor-id="implementation-details-matter"}

Example:

$$
\begin{aligned}
\theta &\sim N(0, 100) \\
X_i | \theta &\sim N(\theta, 0.1^2), \quad i=1,\ldots,n
\end{aligned}
$$

Posterior: $\theta | X \sim N\left(\frac{\bar{X}/0.01^2}{n/0.01^2 + 1/100}, \frac{1}{n/0.01^2 + 1/100}\right)$

Gibbs sampler: 1. $\mathbb{E}[\theta|X] = 8.9, \text{SD}(\theta|X) = 0.1$ 2. $\theta^{(t+1)} | X, \theta^{(t)} \sim N(8.9, 0.1^2)$

Gibbs takes a long time to mix.

Better parameterization:

$$
\begin{aligned}
B &= \theta - \bar{X} \\
\theta &= B + \bar{X}
\end{aligned}
$$

$B|X \sim N(0, 0.1^2)$

Gibbs: Directly sampling from posterior

### 3.4 Empirical Bayes {.anchored number="3.4" anchor-id="empirical-bayes"}

Back to Gaussian hierarchical model:

$$
\begin{aligned}
\theta_i &\sim N(\mu, \tau^2) \\
X_i | \theta_i &\sim N(\theta_i, \sigma^2)
\end{aligned}
$$

$$
\mathbb{E}[\theta_i | X, B] = \frac{B - \sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar{X}, \quad B = \tau^2 + \sigma^2
$$

For any reasonable prior: $B | X \approx \frac{1}{N}\sum_{i=1}^N (X_i - \bar{X})^2$

If prior doesn’t matter much, why use one? Could just estimate $B$ from data, however we want.

A minimax estimator is $B = \sigma^2 + \frac{1}{N}\sum_{i=1}^N (X_i - \bar{X})^2$

Called Empirical Bayes: a hybrid approach in which hyperparameters are treated as fixed, others treated as random.

---

[Up: contents](../index.md)
