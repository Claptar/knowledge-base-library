---
title: "16. Hierarchical Bayes"
course: "Berkeley Stat 210A Fall 2024"
chapter: 16
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Hierarchical Bayes

## What this covers

How should you build a Bayesian model for many similar units — many baseball players' batting
averages, many groups' means — so that data from one unit helps estimate the others? This chapter
develops hierarchical Bayesian models and the shrinkage estimators they produce, then turns to the
computational problem a hierarchical prior creates: the posterior's normalizing constant is rarely
available in closed form. It covers Markov chain Monte Carlo, the Gibbs sampler in particular, and
closes with the empirical Bayes shortcut that sometimes lets you skip building a sampler at all. It
assumes Bayesian updating, the standard conjugate families (Beta–Binomial, Normal–Normal), and the
definition of a Markov chain.

## Hierarchical models: pooling information across units

A hierarchical, or multilevel, model handles many units that share structure by inserting a layer of
shared hyperparameters between the prior and each unit's parameter. Rather than fixing one prior for
every unit, each unit's parameter $\theta_i$ is itself drawn from a distribution governed by a
hyperparameter, and a hyperprior is placed on that hyperparameter. Data from every unit then updates
the hyperparameter, and through it every other unit's estimate. That flow of information between
units — "the full power of Bayes ... realized in large, complex problems with repeat structure" — is
what a hierarchical model is for.

It is worth being clear from the start that this is not a different kind of inference from ordinary
Bayes. Marginalizing the hyperparameters out of the joint distribution always produces an ordinary,
if more complicated, prior directly on the $\theta_i$'s. Nothing about *what the posterior is* forces
you to write the model hierarchically — writing it that way is a choice, made because it is often
easier to reason about (a Beta–Binomial prior on each $\theta_i$ is more legible than the marginal
prior it induces) and, as this chapter shows, because it can make the computation tractable in a way
the marginal form would not.

### Example: predicting batting averages

Suppose you want to predict a batter's true batting average from $n_i$ at-bats and $X_i$ observed
hits, with
$$
X_i \mid \theta_i \sim \text{Binom}(n_i, \theta_i).
$$
Estimating each $\theta_i$ from $X_i/n_i$ alone ignores everything you know from every *other*
player. A hierarchical model pools across players $i=1,\dots,m$:
$$
\begin{aligned}
\alpha,\beta &\sim \pi_0(\alpha,\beta) &&\text{(hyperprior)}\\
\theta_i \mid \alpha,\beta &\sim \text{Beta}(\alpha,\beta), & i&=1,\dots,m\\
X_i \mid \theta_i, n_i &\sim \text{Binom}(n_i,\theta_i), & i&=1,\dots,m.
\end{aligned}
$$
Beta–Binomial conjugacy gives $\mathbb E[\theta_i \mid X, \alpha,\beta] = \dfrac{\alpha+X_i}{\alpha+
\beta+n_i}$: the usual conjugate shrinkage of the raw rate $X_i/n_i$ toward $\alpha/(\alpha+\beta)$,
with $\alpha,\beta$ acting as pseudo-counts. What makes this *hierarchical*, rather than just a
conjugate prior, is that $\alpha,\beta$ are not chosen in advance — they have their own posterior,
and the tower property gives the estimator that is actually used:
$$
\mathbb E[\theta_i \mid X] = \mathbb E\big[\mathbb E[\theta_i \mid X,\alpha,\beta] \mid X\big]
= \mathbb E\!\left[\frac{\alpha+X_i}{\alpha+\beta+n_i} \,\middle|\, X\right].
$$
All $m$ players' data, $X_1,\dots,X_m$, are used to learn a good prior on each individual $\theta_i$
— that is the pooling.

### Example: a Gaussian hierarchical model and shrinkage

The same idea in the Gaussian case, with $\sigma^2$ known:
$$
\theta_i \sim N(\mu,\tau^2), \qquad X_i \mid \theta_i \sim N(\theta_i,\sigma^2), \qquad i=1,\dots,d.
$$
Normal–Normal conjugacy makes the posterior mean of $\theta_i$ given the hyperparameters a convex
combination of the data point and the hyperprior mean, weighted by their relative precisions, so
$$
\mathbb E[\theta_i \mid X] = \mathbb E\big[\mathbb E[\theta_i\mid X,\mu,\tau^2]\mid X\big]
= \mathbb E\!\left[\frac{\tau^2}{\tau^2+\sigma^2}X_i + \frac{\sigma^2}{\tau^2+\sigma^2}\mu \,\middle|\, X\right]:
$$
a **linear shrinkage estimator**, with the shrinkage weight itself estimated from the data rather
than fixed in advance.

To estimate the hyperparameters, marginalize $\theta_i$ out of the model: $\theta_i$ and the noise are
both Gaussian, so
$$
X_i \mid \mu,\tau^2 \sim N(\mu,\tau^2+\sigma^2),
\qquad
\bar X \sim N\!\left(\mu, \tfrac{\tau^2+\sigma^2}{n}\right),
\qquad
S^2 = \tfrac1{n-1}\sum_{i=1}^n (X_i-\bar X)^2 \sim \tfrac{\tau^2+\sigma^2}{n-1}\chi^2_{n-1}.
$$
Only the sum $B := \tau^2+\sigma^2$ — the total variance the $X_i$ display around $\mu$ — is
identifiable from the data, not $\tau^2$ and $\sigma^2$ separately. Rewriting the shrinkage estimator
in terms of $B$, with $\bar X$ standing in for the estimate of $\mu$:
$$
\delta(x) = \mathbb E\big[\mathbb E[\theta_i \mid X,B]\mid X\big]
= \mathbb E\!\left[\frac{B-\sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar X \,\middle|\, X\right],
$$
with $\bar X \sim N(\mu, B/n)$ and $(n-1)S^2 \sim B\chi^2_{n-1}$ as the relevant statistics for $B$.

Putting a conjugate scale-mixture prior directly on $B$,
$$
\pi(B\mid\lambda,\nu) \propto B^{-\nu/2-2}\exp\!\left(-\frac{\lambda}{2B}\right),
$$
gives the closed-form posterior
$$
B\mid X \sim \text{InvGamma}\!\left(\frac{n+\nu}{2}, \frac{\lambda+(n-1)S^2}{2}\right),
\qquad
\mathbb E\!\left[\frac1B \,\middle|\, X\right] = \frac{n+\nu}{\lambda+(n-1)S^2},
$$
and hence the explicit shrinkage rule
$$
\delta_i(x) = \frac{(n-3)S^2}{(n-1)S^2+\lambda}X_i + \frac{\lambda+2S^2}{(n-1)S^2+\lambda}\bar X.
$$
The hyperparameters $\nu,\lambda$ act as **pseudo-data**: a weak choice takes $\nu \approx 2$ and
$\lambda \approx \nu\sigma^2$, contributing only the equivalent of a couple of extra observations
worth of variance. Since $B=\tau^2+\sigma^2$ with $\tau^2\ge 0$, values of $B$ below $\sigma^2$ are not
meaningful; if $\lambda$ is small the prior can put non-trivial mass there anyway, and it is then
worth truncating $\pi(B\mid\lambda,\nu)$ to $[\sigma^2,\infty)$.

### The DAG picture

Both examples share the same structure: a hyperparameter generating each unit's parameter, which in
turn generates that unit's data.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Directed graph showing shared hyperparameters generating each unit's parameter, which generates that unit's data">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="160" y="26" text-anchor="middle" font-size="13" fill="currentColor">&#945;, &#946;</text>
  <line x1="150" y1="34" x2="80" y2="96" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="160" y1="34" x2="160" y2="96" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="170" y1="34" x2="240" y2="96" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="70" y="112" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8321;</text>
  <text x="160" y="112" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8322;</text>
  <text x="250" y="112" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8323;</text>
  <line x1="70" y1="120" x2="70" y2="176" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="160" y1="120" x2="160" y2="176" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="250" y1="120" x2="250" y2="176" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="70" y="192" text-anchor="middle" font-size="12" fill="currentColor">X&#8321;</text>
  <text x="160" y="192" text-anchor="middle" font-size="12" fill="currentColor">X&#8322;</text>
  <text x="250" y="192" text-anchor="middle" font-size="12" fill="currentColor">X&#8323;</text>
</svg>
<figcaption>The hierarchical model as a directed acyclic graph: shared hyperparameters generate each
unit's parameter, which generates that unit's data. The joint density factors as one term per node,
each conditioned on its parents.</figcaption>
</figure>

More generally, a Bayesian network associates one factor with each vertex of a directed acyclic graph
$(V,E)$, conditioned on its parents:
$$
p(z) = \prod_{i=1}^{|V|} p\big(z_i \mid z_{\text{pa}(i)}\big).
$$
For the hierarchical model above, this reads
$$
p(\alpha,\beta,\theta_1,\dots,\theta_m,X_1,\dots,X_m)
= p(\alpha,\beta)\prod_{i=1}^m p(\theta_i\mid\alpha,\beta)\,p(X_i\mid\theta_i).
$$

## Markov chain Monte Carlo

Bayes' rule itself is never the problem:
$$
\pi(\theta\mid x) = \frac{p(x\mid\theta)\pi(\theta)}{\int p(x\mid\theta)\pi(\theta)\,d\theta}.
$$
The numerator — likelihood times prior, evaluated at a point — is usually easy. The denominator, an
integral over every value $\theta$ could take, is often intractable the moment $\theta$ has more than
a couple of dimensions, which is exactly the regime a hierarchical model with hyperparameters *and*
$\theta_1,\dots,\theta_m$ lives in.

The computational fix is to give up on evaluating the posterior density directly and instead
**simulate** from it: set up a Markov chain whose stationary distribution is $\pi(\theta\mid x)$, run
it, and use the resulting draws as approximate samples from the posterior.

### Markov chains, stationarity, and reversibility

A stationary Markov chain with transition kernel $Q(y\mid x)$ and initial distribution $\pi_0$ is a
sequence $X_0,X_1,\dots$ with $X_0\sim\pi_0$ and
$$
P(X_{t+1}\in A \mid X_t,\dots,X_0) = P(X_{t+1}\in A\mid X_t) = \int_A Q(y\mid X_t)\,dy:
$$
the future depends on the past only through the present. This is itself a directed graphical model,
$X_0 \to X_1 \to X_2 \to \cdots$, and the marginal distribution updates by
$$
\pi_t(y) = \int Q(y\mid x)\,\pi_{t-1}(x)\,dx.
$$
A distribution $\pi$ is a **stationary distribution** for $Q$ if $\pi(y) = \int Q(y\mid x)\pi(x)\,dx$
— plugging $\pi$ in on the right reproduces $\pi$ on the left, so once the chain reaches $\pi$ it
stays there.

A convenient sufficient condition for stationarity is **detailed balance**:
$$
\pi(x)Q(y\mid x) = \pi(y)Q(x\mid y) \quad\text{for all } x,y.
$$
Integrating both sides over $x$ recovers exactly the stationarity condition:
$$
\int_x Q(y\mid x)\pi(x)\,dx = \int_x \pi(y)Q(x\mid y)\,dx = \pi(y)\int_x Q(x\mid y)\,dx = \pi(y).
$$
A chain satisfying detailed balance is called **reversible**: if $X_t\sim\pi$, the pair
$(X_{t-1},X_t)$ has the same joint distribution as $(X_t,X_{t+1})$ read backwards, i.e.
$X_{t-1}\mid X_t \sim X_{t+1}\mid X_t$.

### Convergence to the stationary distribution

The reason this is useful for sampling is a convergence theorem: if a Markov chain with stationary
distribution $\pi$ is

1. **Irreducible** — for all $x,y$ there is some $n$ with $P(X_n=y\mid X_0=x)>0$, and
2. **Aperiodic** — for all $x$, $\gcd\{n>0 : P(X_n=x\mid X_0=x)>0\} = 1$,

then $\pi_t \to \pi$ in total variation distance, regardless of the initial distribution $\pi_0$: the
chain "forgets" where it started. This licenses the strategy behind every MCMC algorithm: find a
kernel $Q$ whose stationary distribution is the posterior $\pi(\theta\mid x)$, start the chain
anywhere, run it a long time, and treat $X_t$, for large $t$, as an approximate draw from the
posterior.

## The Gibbs sampler

The Gibbs sampler is a specific, and specifically convenient, way to build such a $Q$ for a parameter
vector $\theta=(\theta_1,\dots,\theta_d)$: replace one coordinate at a time by a draw from its exact
conditional distribution given everything else.

**Algorithm.** Initialize $\theta^{(0)}$. For $t=1,\dots,T$: for $j=1,\dots,d$, sample
$\theta_j^{(t)} \sim p(\theta_j \mid \theta_{-j}^{(t-1)}, X)$, and record $\theta^{(t)}$. Variations
update a single randomly chosen coordinate $J\sim\text{Unif}(1,\dots,d)$ each step, or sweep through
the coordinates in a random order.

For a hierarchical model, this is more than a generic recipe — it is what makes the model
computationally attractive in the first place. Because the joint density factors along the DAG, the
full conditional of a single node depends only on its parents and children:
$$
p(\theta_i \mid \theta_{-i}, X, \alpha) \propto p(\theta_i\mid\theta_{\text{pa}(i)})
\prod_{j\,\in\,\text{ch}(i)} p(\theta_j\mid\theta_i),
$$
a low-dimensional distribution rather than one over the whole parameter vector. With conjugate priors
at every level, this conditional is typically a recognizable named distribution, and, since the
$\theta_i$'s are conditionally independent given the hyperparameters, their updates can often be run
in parallel.

### Why a Gibbs sweep preserves the posterior

**Claim.** If $\theta^{(t)}\sim \pi(\theta\mid X)$, then $\theta^{(t+1)}\sim\pi(\theta\mid X)$ too.

**Proof sketch.** Consider updating a single fixed coordinate $j$:
$\theta_j^{(t+1)} \sim p(\theta_j\mid \theta_{-j}^{(t)}, X)$, with $\theta_{-j}$ left unchanged. Since
$\theta_j^{(t+1)}$ is drawn from *exactly* the conditional distribution of $\theta_j$ given
$\theta_{-j}^{(t)}$, and the correct joint law factors as that conditional times the marginal of
$\theta_{-j}$, the new pair $\big(\theta_{-j}^{(t)},\theta_j^{(t+1)}\big)$ has the same joint law as
$\big(\theta_{-j}^{(t)},\theta_j^{(t)}\big)$ did. So updating any one coordinate from its exact
conditional preserves $\pi(\theta\mid X)$, and updating every coordinate — in any fixed or random
order — does too, since each step of the sweep individually preserves it.

### Diagnosing convergence

In theory, the recipe is simple: pick an initialization and a valid kernel $Q$, run it long enough
that $\theta^{(t)} \sim \pi(\theta\mid X)$, and repeat to get as many samples as wanted.

In practice, "long enough" cannot be checked directly, only its symptoms of not having been reached
yet: plotting $\theta_i^{(t)}$ against $t$ to see how fast the chain moves around, or running several
independently initialized chains and computing
$$
\hat R = \frac{\text{between-chain variance}}{\text{within-chain variance}},
$$
checking that it is close to $1$. These diagnostics are **good, not great** — they can be fooled,
especially by a multimodal posterior, where a chain gets stuck exploring one mode and every
diagnostic looks fine.

The standard compromise is **burn-in**: discard an initial stretch of $B$ iterations as not yet
converged, and estimate the posterior from only $\theta^{(B+1)}, \dots, \theta^{(B+N)}$. For a
function $f$ of interest,
$$
\hat\mu_f = \frac1N \sum_{t=B+1}^{B+N} f\big(\theta^{(t)}\big).
$$

### A cautionary example: parametrization and mixing speed

The reader gives a compressed but useful example of how much implementation choices matter, even in
a model simple enough to solve exactly. Take
$$
\theta \sim N(0,100), \qquad X_i\mid\theta \sim N(\theta, 0.1^2), \quad i=1,\dots,n,
$$
so that conjugacy gives
$$
\theta \mid X \sim N\!\left(\frac{\bar X/0.01^2}{n/0.01^2+1/100},\ \frac1{n/0.01^2+1/100}\right),
$$
which, for the data used in the example, works out numerically to $\theta\mid X \sim N(8.9, 0.1^2)$.
The notes record that a Gibbs sampler built directly on $\theta$ in this form "takes a long time to
mix," while re-parametrizing to the deviation from the sample mean,
$$
B = \theta - \bar X \qquad (\text{so } \theta = B + \bar X),
$$
gives $B\mid X \sim N(0, 0.1^2)$ and lets the sampler draw directly from the posterior. The mechanics
behind exactly why the first version mixes slowly are compressed out of the source, but the moral is
not: two mathematically equivalent ways of writing down the same unknown can be the difference between
a chain that explores the posterior in one step and one that does not. The theoretical guarantee from
the convergence theorem above — irreducible and aperiodic implies convergence — says nothing about
*how many steps* that takes, and the practical answer depends on how the state is parametrized.

## Empirical Bayes: when the hyperprior barely matters

Return to the Gaussian hierarchical model. Once $B=\tau^2+\sigma^2$ is fixed, the Bayes rule is the
linear shrinkage estimator
$$
\mathbb E[\theta_i\mid X, B] = \frac{B-\sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar X.
$$
The notes make an observation that undercuts some of the machinery built to get here: for essentially
any reasonable prior on $B$, once there is enough data, the posterior for $B$ concentrates near the
sample variance almost regardless of which prior $\pi(B\mid\lambda,\nu)$ was chosen,
$$
B\mid X \approx \frac1N\sum_{i=1}^N (X_i-\bar X)^2.
$$
If the prior barely matters, the natural question is why carry one at all — you could just plug in a
sensible estimate of $B$, estimated from the data however you like. A minimax choice given here is
$$
B = \sigma^2 + \frac1N\sum_{i=1}^N (X_i-\bar X)^2.
$$
This hybrid — treat the hyperparameters as fixed numbers to be estimated, and only the remaining
parameters as genuinely random — is called **empirical Bayes**. It is the shortcut that lets you use
the shrinkage estimator without a hyperprior or a sampler, at the cost of no longer propagating the
uncertainty in $B$ itself into the answer.

## Sources

- Hierarchical models, the batting-average and Gaussian hierarchical examples, the shrinkage
  estimator, and the DAG factorization: Berkeley STAT 210A reader, "Hierarchical Bayes" — fall 2024
  [`reader/hierarchical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd),
  as split into `hierarchical-bayes/01-hierarchical-bayes.md`, cross-checked against the fall 2025
  edition
  ([`reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hierarchical-bayes.html)
  §3.1, and the split `units/reader/hierarchical-bayes/01-1-hierarchical-bayes.md` §1), which is
  textually identical.
- The intractability of the posterior normalizing constant, the definition of a Markov chain,
  stationarity, detailed balance and reversibility, and the irreducibility/aperiodicity convergence
  theorem: fall 2024 `hierarchical-bayes/02-markov-chain-monte-carlo-mcmc.md`, cross-checked against
  fall 2025 §3.2 / `02-2-markov-chain-monte-carlo-mcmc.md`.
- The Gibbs sampler, its stationarity proof sketch, convergence diagnostics and burn-in, the
  parametrization example, and empirical Bayes: fall 2024 `hierarchical-bayes/03-gibbs-sampler.md`,
  cross-checked against fall 2025 §3.3–3.4 / `03-3-gibbs-sampler.md`.
- No slide deck or lecture transcript was supplied for this lecture, only the course reader, so
  nothing in this chapter draws on spoken commentary beyond what the reader itself records. No
  problem set was supplied either, so there is no Exercises section. The reader's own worked numbers
  behind the "Implementation Details Matter" example (the data giving $\theta\mid X\sim N(8.9,0.1^2)$,
  and the precise reason the naive parametrization mixes slowly) are not given beyond what is quoted
  above.

---

[← 14. Fall 2024 Final Examination](14-fall-2024-final-examination.md) · [Contents](index.md) · [17. Standing Homework Conventions →](17-standing-homework-conventions.md)
