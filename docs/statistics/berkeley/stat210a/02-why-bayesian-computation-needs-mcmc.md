---
title: "2. Why Bayesian Computation Needs MCMC"
course: "Berkeley Stat 210A"
chapter: 2
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Why Bayesian Computation Needs MCMC

## What this covers

Bayesian inference asks for a posterior distribution $\lambda(\theta \mid x)$, and this chapter
answers a narrower question: why is that distribution generically hard to *compute*, and what is
the standard remedy? It introduces Markov chain Monte Carlo (MCMC) — running a Markov chain whose
stationary distribution is the posterior — states and motivates the theorem that guarantees such a
chain converges, and then looks at what makes MCMC hard to trust in practice, once it has to be run
for a finite number of steps. It assumes familiarity with Bayes' rule for a posterior density and
with simple conjugate examples where that posterior is available in closed form.

## Why the posterior is hard to compute

Recall the Bayesian posterior density,
$$
\lambda(\theta \mid x) = \frac{\lambda(\theta)\, p_\theta(x)}{\int_\Theta \lambda(\zeta)\, p_\zeta(x)\, d\zeta},
$$
where $\lambda(\theta)$ is the prior and $p_\theta(x)$ the likelihood. The numerator — prior times
likelihood, evaluated at one value of $\theta$ — is easy to compute even in complicated models: it
is just a product of densities. All of the difficulty is in the denominator, the integral of that
same product over the whole parameter space $\Theta$. That integral does not depend on $\theta$; it
exists only to make $\lambda(\theta \mid x)$ integrate to one. With a conjugate prior, or with only
one or two parameters, it is usually available in closed form, which is exactly the setting behind
most posterior calculations seen so far. But a hierarchical model with many linked quantities makes
$\Theta$ high-dimensional, and there is no reason to expect the normalizing integral to have a nice
closed form there. In that generic case it must be approximated numerically.

The strategy this chapter builds does not try to compute that integral at all. Instead it *samples*
from $\lambda(\theta \mid x)$ directly, by a method that only ever touches the cheap numerator and
never the intractable denominator. That method is Markov chain Monte Carlo: construct a sequence of
random variables $\theta^{(0)}, \theta^{(1)}, \theta^{(2)}, \ldots$ whose distribution converges to
the posterior, then treat a well-chosen subset of the later $\theta^{(t)}$ as a sample from
$\lambda(\theta \mid x)$.

## Markov chains and stationary distributions

A **Markov chain** is a sequence of random variables $X^{(0)}, X^{(1)}, X^{(2)}, \ldots$ such that
the distribution of $X^{(t+1)}$ given the entire history $X^{(0)}, \ldots, X^{(t)}$ depends only on
$X^{(t)}$. Informally, the chain is *memoryless*: at time $t$, everything relevant about the past is
already summarized by the current state.

Formally, fix a state space $\mathcal{X}$ with base measure $\mu$, a **transition kernel**
$Q(y \mid x)$ — a probability density in $y$ for each fixed $x$ — and an initial distribution
$\pi_0$. The chain is $X^{(0)} \sim \pi_0$ with $X^{(t+1)} \mid X^{(0)}, \ldots, X^{(t)} \sim
Q(\cdot \mid X^{(t)})$. Its joint density up to time $T$ factors as
$$
\pi_0\bigl(x^{(0)}\bigr) \prod_{t=0}^{T-1} Q\bigl(x^{(t+1)} \mid x^{(t)}\bigr),
$$
which exhibits a Markov chain as a graphical model with an arrow from each variable only to the
next one, and no others.

Iterating the kernel gives the $n$-step transition density,
$$
Q^n(y \mid x) = \int_{\mathcal{X}} Q(y \mid z)\, Q^{n-1}(z \mid x)\, d\mu(z),
$$
and the marginal distribution of $X^{(t)}$ is
$\pi_t(y) = \int_{\mathcal{X}} Q^t(y \mid x)\, \pi_0(x)\, d\mu(x)$.

A distribution $\pi$ is **stationary** for $Q$ if one step of the chain leaves it unchanged:
$$
\pi(y) = \int_{\mathcal{X}} Q(y \mid x)\, \pi(x)\, d\mu(x).
$$

A convenient sufficient — though not necessary — condition for stationarity is **detailed
balance**:
$$
\pi(x)\, Q(y \mid x) = \pi(y)\, Q(x \mid y) \qquad \text{for all } x, y \in \mathcal{X}.
$$
The check is one line: integrating both sides over $x$,
$$
\int Q(y \mid x)\, \pi(x)\, d\mu(x) = \pi(y) \int Q(x \mid y)\, d\mu(x) = \pi(y),
$$
using that $Q(\cdot \mid y)$ is a probability density in its first argument.

This is the hook MCMC hangs on: if a transition kernel $Q$ can be engineered so that the posterior
$\lambda(\theta \mid x)$ is stationary for it — detailed balance being the standard way to arrange
this — then running the chain and reading off later states is a candidate for sampling the
posterior. What is still needed is a guarantee that the chain actually gets close to $\pi$, from
any starting point.

## Convergence to the stationary distribution

Having a stationary distribution is not by itself enough: a chain can have $\pi$ stationary and
still fail to approach it, for instance by refusing to leave a region of the space it starts in, or
by cycling deterministically through a partition of it. Two extra conditions rule this out.

**Theorem (Markov chain convergence).** Let $X^{(0)}, X^{(1)}, \ldots$ be a Markov chain with
transition kernel $Q$ and stationary distribution $\pi$. Suppose further that

1. **Irreducible**: for every $x, y \in \mathcal{X}$ there is some $n$ with $Q^n(y \mid x) > 0$;
2. **Aperiodic**: for every $x \in \mathcal{X}$, $\gcd\{n : Q^n(x \mid x) > 0\} = 1$.

Then, regardless of the initial distribution $\pi_0$, $\pi_t \to \pi$ in total variation distance:
$$
\|\pi_t - \pi\|_{\mathrm{TV}} = \sup_{A \subseteq \mathcal{X}} \bigl|\pi_t(A) - \pi(A)\bigr| \to 0
\qquad \text{as } t \to \infty.
$$

Irreducibility rules out the state space splitting into pieces that never communicate — "parallel
universes" the chain could get permanently stuck in depending on where it starts. Aperiodicity
rules out the chain cycling deterministically through a partition of the space instead of mixing
across it; it is also the easy condition to repair when it fails, by building a *lazy* kernel that
at each step flips a coin and either applies $Q$ or stays put — stationarity is unaffected by this.
The theorem as stated is for discrete state spaces; on a continuous space the two conditions need
more care to state, though they go through unchanged when $Q$ itself is a continuous density —
otherwise there can be measure-zero pathologies to worry about, of the kind set aside all semester.

### Why it's true: coupling

The proof, sketched here for the discrete case, uses a **coupling** argument — worth following
because it is also the intuition for why real chains can take a long time to mix.

Run a second, independent chain $Y^{(0)}, Y^{(1)}, \ldots$ with the same kernel $Q$, but started
already at stationarity, $Y^{(0)} \sim \pi$. Let $\tau = \min\{t : X^{(t)} = Y^{(t)}\}$ be the first
time the two chains meet, and build a spliced chain that follows $X$ until they meet and $Y$
afterward:
$$
Z^{(t)} = \begin{cases} X^{(t)} & t \le \tau \\ Y^{(t)} & t > \tau. \end{cases}
$$
One can check $Z$ is itself a Markov chain with kernel $Q$ and the same initial distribution as
$X$, so $Z^{(t)} \sim \pi_t$. Since $Z^{(t)} = Y^{(t)}$ whenever $\tau \le t$,
$$
\|\pi_t - \pi\|_{\mathrm{TV}} = \sup_{A} \bigl|\mathbb{P}(Z^{(t)} \in A) - \mathbb{P}(Y^{(t)} \in A)\bigr|
\le \mathbb{P}(\tau > t).
$$
The remaining step — omitted here — is that irreducibility, aperiodicity, and the existence of a
stationary distribution together force $\tau < \infty$ almost surely, so $\mathbb{P}(\tau > t) \to
0$ and the bound goes to zero. $\blacksquare$

The payoff: to sample from a posterior $\lambda(\theta \mid x)$, it suffices to find *any*
irreducible, aperiodic transition kernel $Q$ for which $\lambda(\theta \mid x)$ is stationary.
Running that chain from any starting point $\theta^{(0)}$ then produces, for large $t$, a state
whose distribution is close to the posterior — with no normalizing integral ever computed.

## MCMC in practice: how slow can convergence be?

The theorem guarantees convergence "for long enough," but says nothing about how long that is —
and in practice it can be very long indeed.

One illustration makes this concrete: a target distribution that mixes two bivariate Gaussians, one
centered at $(\mu,\mu)$ and the other at $(-\mu,-\mu)$,
$$
\theta \sim \tfrac12\, p\!\left(\theta - \binom{\mu}{\mu}\right) + \tfrac12\, p\!\left(\theta -
\binom{-\mu}{-\mu}\right), \qquad p(z) = \frac{1}{2\pi\sqrt{1-\rho^2}} \exp\left\{-\tfrac12\, z'
\Sigma^{-1} z\right\},
$$
each component having covariance $\Sigma = \begin{pmatrix}1 & \rho \\ \rho & 1\end{pmatrix}$. A
chain that updates one coordinate at a time on this density — draw $\theta_1$ given the current
$\theta_2$, then $\theta_2$ given the new $\theta_1$, the coordinate-by-coordinate mechanism behind
the Gibbs sampler — shows two distinct ways to mix slowly:

- **Between modes**: the farther apart the two components are (larger $\mu$), the longer the chain
  tends to linger near one mode before a step happens to carry it across to the other.
- **Within a mode**: the more correlated the coordinates are (larger $|\rho|$), the smaller the
  effective step size of a one-coordinate-at-a-time update, so even exploring a single mode
  thoroughly takes longer.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A Markov chain path that jitters for a long time inside one mode of a two-mode density before rarely crossing to the other mode">
  <defs>
    <marker id="arrow-c902" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <ellipse cx="85" cy="165" rx="55" ry="42" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <ellipse cx="255" cy="55" rx="55" ry="42" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="85" y="204" text-anchor="middle" font-size="11" fill="currentColor">mode at (-mu,-mu)</text>
  <text x="255" y="16" text-anchor="middle" font-size="11" fill="currentColor">mode at (mu,mu)</text>
  <polyline points="65,150 95,175 70,145 105,160 85,180 68,152 100,140 90,168"
            fill="none" stroke="currentColor" stroke-width="1.3" stroke-opacity="0.55"/>
  <polyline points="90,168 140,130 190,95 225,70"
            fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#arrow-c902)"/>
  <polyline points="225,70 245,55 265,40 235,60 258,75 240,45 260,65"
            fill="none" stroke="currentColor" stroke-width="1.3" stroke-opacity="0.55"/>
  <text x="150" y="118" text-anchor="middle" font-size="11" fill="currentColor">rare crossing</text>
</svg>
<figcaption>A chain on a two-mode density spends long stretches jittering inside one mode
(faint path) before an infrequent step carries it to the other mode (bold arrow) — the mechanism
behind slow mixing, made worse the farther apart or more correlated the modes are.</figcaption>
</figure>

The **trace plot** — the sequence $\theta_1^{(0)}, \theta_1^{(1)}, \ldots$ plotted against
iteration — is the standard diagnostic for this. It is good at revealing exactly the two symptoms
above: switching back and forth between modes, or crawling very slowly through the space. It is not
good at revealing the more dangerous failure of simply never visiting a high-probability region of
the posterior at all — a chain that has never seen a mode leaves no trace of having missed it.

Two devices are standard in implementations. **Burn-in** discards the first $B$ steps of the chain,
on the grounds that the distribution of $\theta^{(t)}$ for small $t$ is still far from $\pi$.
**Thinning** then keeps only every $s$-th draw after that, $\theta^{(B)}, \theta^{(B+s)},
\theta^{(B+2s)}, \ldots$, to reduce the correlation between the retained samples. Given this final
set of draws as a proxy for a sample from the posterior, any of the usual questions — posterior
means, credible intervals, or the minimizer of any expected loss — can be answered from it just as
if the posterior itself were in hand.

## Sources

- Berkeley STAT 210A course reader, the chapter titled "Why Bayesian computation is difficult" in
  one offering and "Markov Chain Monte Carlo" in the other, sections 1 ("Why Bayesian computation
  is difficult"), 2 ("Markov chains," both the "stationarity" and "convergence" subsections), and 4
  ("MCMC in practice"). Two near-identical offerings were supplied and merged into one treatment:
    - fall-2025, `reader/bayes-computation.html` —
      https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
    - fall-2026, `reader/bayes-computation.qmd` —
      https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd
- Not included in either supplied file: section 3, "The Gibbs sampler," which both offerings link
  to and which section 4 leans on by name ("the Gibbs sampler (for instance)"). The
  coordinate-by-coordinate updating rule used in the mixture example is the mechanism, reconstructed
  from the example itself, but the Gibbs sampler's general definition and derivation were not part
  of the supplied material.
- The interactive figure described in section 4 — an animated trace plot and contour plot of the
  two-mode mixture, with sliders for $\mu$, $\rho$, and the starting point — exists in the source as
  executable JavaScript/Observable code rather than a static image; the SVG above redraws what it
  shows, not the applet itself.
- No slides, transcript, or problem set were supplied for this chapter.

---

[← 1. Introduction to Asymptotic Theory](01-introduction-to-asymptotic-theory.md) · [Contents](index.md) · [3. Bayes Risk and Bayes Estimator →](03-bayes-risk-and-bayes-estimator.md)
