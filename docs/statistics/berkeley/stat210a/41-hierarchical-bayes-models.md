---
title: "41. Hierarchical Bayes Models"
course: "Berkeley Stat 210A"
chapter: 41
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 41. Hierarchical Bayes Models

## What this covers

How do you use a Bayesian model to let many similar units — many baseball players, many
experimental subjects, many groups in a study — share statistical strength with one another,
instead of being estimated in isolation? This chapter sets up the **hierarchical Bayes** model
that answers that question, works through the standard batting-average example, and derives the
form of the pooled posterior estimate. It assumes familiarity with Bayes' rule, the Beta–Binomial
conjugate pair, and the tower property (iterated expectation) $\mathbb{E}[Z] = \mathbb{E}[\mathbb{E}[Z \mid Y]]$.

The lecture's own outline promises two further topics — Markov chain Monte Carlo and the Gibbs
sampler — as the computational tools that make hierarchical models tractable. The surviving
material breaks off before reaching either, so this chapter covers only the hierarchical-model
setup itself; see **Sources** below.

## Why hierarchical models: pooling repeated structure

The full power of a Bayesian analysis shows up in large, complex problems that have **repeat
structure**: many units of the same kind, each with its own unknown parameter, all measured
through the same kind of noisy observation. A single unit's data is often too sparse to pin down
its own parameter well, but if the units are related — drawn from a common population — then the
data from all of them together can be used to learn about that population, and that population-level
information can, in turn, sharpen the estimate for each individual unit. This is **pooling**.

A hierarchical Bayes model builds this into the model itself, as a chain of conditional
distributions: a *hyperprior* on population-level hyperparameters, then unit-level parameters
drawn i.i.d. given the hyperparameters, then observations drawn independently given the unit-level
parameters.

## Worked example: batting averages

Take $m$ baseball players. Player $i$ has $n_i$ at-bats, of which $X_i$ are hits, so

$$
X_i = \#\{\text{hits}\} \sim \text{Binom}(n_i, \theta_i),
$$

where $\theta_i$ is player $i$'s (unobserved) true batting average. The goal is to estimate every
$\theta_i$.

Estimating each $\theta_i$ from $X_i$ and $n_i$ alone throws away information: a player with few
at-bats has a very noisy estimate, even though the population of players is not arbitrary — batting
averages cluster in a fairly narrow, known range. A hierarchical model captures that population
structure explicitly, by putting a common prior on all the $\theta_i$ and letting the shape of that
prior itself be uncertain and estimated from the pooled data:

$$
\begin{aligned}
\alpha, \beta &\sim \lambda_0(\alpha, \beta) \\
\theta_i \mid \alpha, \beta &\overset{\text{iid}}{\sim} \text{Beta}(\alpha, \beta), \qquad i \le m \\
X_i \mid \theta_i &\overset{\text{indep}}{\sim} \text{Binom}(n_i, \theta_i), \qquad i \le m.
\end{aligned}
$$

Here $\lambda_0$ is a hyperprior on the Beta shape parameters $(\alpha, \beta)$, which set the
population-level distribution of true batting averages. Conditional on $(\alpha,\beta)$, the
$\theta_i$ are i.i.d. draws from that population, and conditional on $\theta_i$, the data $X_i$ are
independent across players.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Three-level hierarchy: hyperparameters generate player abilities, which generate observed hit counts">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="170" cy="30" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="35" text-anchor="middle" font-size="13" fill="currentColor">&#945;, &#946;</text>

  <circle cx="70" cy="115" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="70" y="120" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8321;</text>
  <circle cx="170" cy="115" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="120" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8305;</text>
  <circle cx="270" cy="115" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="120" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8350;</text>

  <circle cx="70" cy="195" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="70" y="200" text-anchor="middle" font-size="11" fill="currentColor">X&#8321;</text>
  <circle cx="170" cy="195" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="200" text-anchor="middle" font-size="11" fill="currentColor">X&#8305;</text>
  <circle cx="270" cy="195" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="200" text-anchor="middle" font-size="11" fill="currentColor">X&#8350;</text>

  <line x1="158" y1="48" x2="82" y2="97" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="170" y1="52" x2="170" y2="93" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="182" y1="48" x2="258" y2="97" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>

  <line x1="70" y1="137" x2="70" y2="177" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="170" y1="137" x2="170" y2="177" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="270" y1="137" x2="270" y2="177" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
</svg>
<figcaption>The hierarchical model as a chain of conditionals: hyperparameters $(\alpha,\beta)$ set
the population distribution of true abilities $\theta_i$, each of which independently generates an
observed hit count $X_i$. Pooling happens because every $X_i$ carries information about
$(\alpha,\beta)$, which feeds back into the estimate of every $\theta_i$.</figcaption>
</figure>

## The pooled posterior mean

Write $X = (X_1, \dots, X_m)$ for all the data. By the tower property, conditioning first on
$(\alpha,\beta)$ and then averaging over the posterior distribution of $(\alpha,\beta)$ given $X$:

$$
\mathbb{E}[\theta_i \mid X] = \mathbb{E}\Big[\, \mathbb{E}[\theta_i \mid X, \alpha, \beta] \,\Big|\, X \,\Big].
$$

Given $(\alpha,\beta)$, the model reduces to the ordinary Beta–Binomial conjugate pair for player
$i$ alone: $\theta_i \mid X_i, \alpha, \beta \sim \text{Beta}(X_i + \alpha,\, n_i - X_i + \beta)$, so

$$
\mathbb{E}[\theta_i \mid X, \alpha, \beta] = \frac{X_i + \alpha}{n_i + \alpha + \beta}.
$$

In this expression $X_i$ and $n_i$ are player $i$'s own fixed data, but $\alpha$ and $\beta$ are
**not fixed** — they are random, distributed according to their posterior $\lambda(\alpha,\beta \mid X)$
given *all* the players' data, not just player $i$'s. That posterior distribution is exactly where
the pooling happens: information from every other player's at-bats updates the plausible values of
$(\alpha,\beta)$, which in turn shifts the effective prior used for $\theta_i$.

**Intuition.** Use all of $X_1, \dots, X_m$ to learn a good prior for each individual $\theta_i$.
A player with only a handful of at-bats gets an estimate that leans heavily on the population-level
shape $(\alpha,\beta)$ learned from everyone else; a player with many at-bats gets an estimate that
is dominated by his own data, since $X_i$ and $n_i$ then swamp $\alpha,\beta$ in the ratio above.

## An equivalent, non-hierarchical model

There is always a model equivalent to the hierarchical one, obtained by marginalizing out the
hyperparameters $(\alpha,\beta)$: integrating them out of the joint distribution leaves a single,
more complicated prior directly on $\theta = (\theta_1,\dots,\theta_m)$ — one under which the
$\theta_i$ are no longer independent, since they all still depend on the same integrated-out
$(\alpha,\beta)$. Writing the model with an explicit hierarchy adds no modeling power beyond what
this general dependent prior could already express. What it adds is **intuition** — the pooling
mechanism above is transparent in the hierarchical form and opaque in the marginal one — and,
often, a **computational strategy**: conditioning on $(\alpha,\beta)$ restores independence and
conjugacy at the $\theta_i$ level, which is the kind of structure a Gibbs sampler is built to
exploit.

## A second sketch: the Gaussian hierarchical model

The lecture begins a second instance of the same idea, replacing the Beta–Binomial pair with the
Normal–Normal pair:

$$
\begin{aligned}
\tau^2 &\sim \lambda_0 \\
\theta_i \mid \tau^2 &\overset{\text{iid}}{\sim} N(0, \tau^2), \qquad i \le d.
\end{aligned}
$$

The source breaks off at this point, before the observation layer is written down or the posterior
mean is worked out, and before the lecture reaches its remaining announced topics (Markov chain
Monte Carlo and the Gibbs sampler). Those are not covered here.

## Sources

- Handwritten lecture notes, *Outline* (lecture 11, "Bayes compute"), Berkeley STAT 210A. The same
  lecture recurs, essentially verbatim, across three offerings of the course:
  `fall-2024/handwritten/lecture11-bayescompute.md`,
  `fall-2025/handwritten/lecture11-bayescompute.md`, and
  `fall-2026/handwritten/lecture11-bayescompute.md`. The fall-2024 version is the most complete of
  the three reconstructions and is the one this chapter follows; fall-2025 and fall-2026 break off
  earlier, at the same point, before the pooled-posterior-mean derivation.
- All three are model reconstructions of a handwritten PDF with no text layer (marked
  "reconstructed by a model" in the source files); the equations are unverified against the
  original scan.
- The lecture's outline names two further topics, Markov chain Monte Carlo and the Gibbs sampler,
  and the Gaussian hierarchical model is left mid-setup — none of that material is present in any
  of the three supplied files, so it is not covered in this chapter.

---

[← 40. Where does $\Lambda$ come from?](40-where-does-lambda-come-from.md) · [Contents](index.md) · [42. Empirical Bayes and James-Stein →](42-empirical-bayes-and-james-stein.md)
