---
title: Markov chains
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-computation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Markov chains

**Source:** [`reader/bayes-computation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Markov chains and stationarity

A Markov chain is a sequence of random variables $X^{(0)},X^{(1)},X^{(2)},\ldots$ the distribution of $X^{(t+1)}$ given $X^{(0)},\ldots,X^{(t)}$ depends on $X^{(t)}$ alone. A Markov chain is sometimes called *memoryless*: at "time" $t$, the only thing we need to know about the entire history of the chain up until $t$ is the present state $X^{(t)}$.

In particular, a **stationary Markov chain** with transition kernel $Q(y \mid x)$ and initial distribution $\pi_0(x)$ (on state space $\cX$ with base measure $\mu$) is a sequence of random variables  $X^{(0)},X^{(1)},X^{(2)},\ldots$ where $X^{(0)}\sim \pi_0$ and $X^{(t+1)}$ given $X^{(0)},\ldots,X^{(t)}$ is distributed as $Q(\cdot\mid X^{(t)})$.

Fixing $x$, we can think of the function $Q(\cdot \mid x)$ as the probability density of $X^{(t+1)}$ given $X^{(t)}=x$.

The joint density of the chain up to finite time $T$ can therefore be factored as $\pi_0(x^{(0)})\prod_{t=0}^{T-1} Q(x^{(t+1)}\mid x^{(t)})$, so a Markov chain is thus a special kind of graphical model wherein there is an arrow pointing from each variable to the next, but there are no other arrows.

We can calculate the transition probabilities after two steps integrating over the probability of all two step paths
$$
Q^2(y \mid x) = \int_{\cX} Q(y\mid z)Q(z \mid x)\,d\mu(z),
$$
and more generally the transition probabilities after $n$ steps as $Q^n(y \mid x) = \int_{\cX} Q(y\mid z)Q^{n-1}(z \mid x)\,d\mu(z)$. Then the distribution of $X^{(t)}$ is
$$
\pi_t(y) = \int_{\cX} Q^t(y\mid x)\pi_0(x)\,d\mu(x).
$$

We say a distribution $\pi$ is **stationary** for $Q$ if this operation leaves $\pi$ fixed:
$$
\pi(y) = \int_\cX Q(y\mid x)\pi(x)\,d\mu(x).
$$
A sufficient (but not necessary) condition for $\pi$ to be stationary for $Q$ is **detailed balance**:
$$
\pi(x)Q(y\mid x) = \pi(y)Q(x\mid y), \quad \text{ for all } x, y\in \cX.
$$
The proof is one line: if we have detailed balance, then
$$
\int Q(y\mid x)\pi(x)\,d\mu(x) = \pi(y)\int Q(x\mid y)\,d\mu(x) = \pi(y),
$$
since $Q(x \mid y)$ is a probability density.

## Convergence

The idea of Markov chain Monte Carlo methods is to devise a Markov chain transition kernel $Q$ whose stationary distribution $\pi$ is the posterior distribution that we want to sample from. One reason this works is that Markov chains tend to converge over time to their stationary distributions, under mild conditions. Denote the transition kernel for $2$ steps as $Q^2(y \mid x) = \int

**Theorem (Markov chain convergence):** Suppose $X^{(0)},X^{(1)},\ldots$ is a Markov chain with transition kernel $Q$ and stationary distribution $\pi$. If additionally the chain is:
1. Irreducible: for all $x,y\in\cX$, there is some $n$ for which $Q^n(y \mid x)>0$, and
2. Aperiodic: for all $x\in\cX$, the greatest common divisor of $\{n:\; Q^n(x \mid x)>0\}$ is $1$.
Then, regardless of the initial distribution $\pi_0$, $\pi_t \to \pi$ in total variation distance as $t\to\infty$, meaning
$$
\|\pi_t-\pi\|_{\text{TV}} = \sup_{A \in \cX} |\pi_t(A)-\pi(A)| \to 0
$$
Intuitively, the irreducibility condition ensures the sample space is not split into "parallel universes" that don't communicate with each other, and the aperiodic condition ensures we are not regularly cycling through subsets of the sample space. Aperiodicity is especially easy to fix, just by making a new transition kernel that flips a coin to choose randomly between transitioning according to $Q$ and staying in place (check for yourself that this does not change the stationary distribution).

!!! danger "Caution"
Note this theorem applies to discrete sample spaces; for continuous sample spaces it is a bit more complicated to state the two conditions. They go through without modification if we assume $Q$ is continuous, but more generally we might have to worry about measure-zero pathologies of the kind that we have been ignoring all semester.
:::

*Proof sketch (discrete case):* Let $Y^{(0)},Y^{(1)},\ldots$ be an independent Markov chains with initial distribution $\pi$ and transition kernel $Q$. We construct a probabilistic *coupling* between the two chains.

Let $\tau = \min\{t:\; X^{(t)}=Y^{(t)}\}$ and define the *coupled chain* that starts as $X^{(t)}$ but then switches to $Y^{(t)}$ after they meet.
$$
Z^{(t)} = \begin{cases} X^{(t)} & \text{ if } t\leq\tau\\ Y^{(t)} & \text{ if } t > \tau\end{cases}
$$
It can be shown that $Z$ is also a Markov chain with transition kernel $Q$ and transition kernel $\pi_0$, so $Z^{(t)} \sim \pi_t$. Moreover,
$$
\|\pi_t-\pi\|_{\text{TV}} = \sup_{A \subseteq \cX} |\PP(Z^{(t)}\in A) - \PP(Y^{(t)}\in A)| \leq \PP(\tau > t),
$$
since $Z^{(t)}=Y^{(t)}$ on the event $\{\tau \leq t\}$. The key step, which we omit here for brevity, is that the irreducibility and aperiodicity conditions, plus the existence of a stationary distribution $\pi$, guarantee that $\tau < \infty$ with probability $1$, so $\PP(\tau>t)\to 0$. $\blacksquare$


The important implication of this theorem from our perspective is that, if we can only find an irreducible and aperiodic transition kernel $Q$ on the state space $\Theta$, whose stationary distribution is the posterior $\lambda(\theta \mid x)$, we will be able to sample from the posterior by running the Markov chain $\theta^{(0)},\theta^{(1)},\ldots$ from any initialization $\theta^{(0)}$.

---

[← Why Bayesian computation is difficult](01-why-bayesian-computation-is-difficult.md) · [Up: contents](index.md) · [The Gibbs sampler →](03-the-gibbs-sampler.md)
