---
title: Random Walk
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Random Walk

**Source:** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Another simple but important / helpful extension to the idea of white noise is the random walk. The simple random walk is defined as:

$x_t = x_{t-1} + w_t$ with initial condition $x_0 = 0$.

Equivalently, $x_t = \displaystyle\sum_{j=1}^t w_j$

The expected value of any time point $\mathbb{E}[x_t] = \mathbb{E}[x_0] = 0$, so the mean does not vary over time.

The variance of a random walk, on the other hand, is additive and grows linearly with time:

$\operatorname{Var}(x_t) = \operatorname{Var}(\displaystyle\sum_{j=1}^t w_j) = t \sigma^2$

Are random walks iid? No! Each time point is not independent, but depends on the past time point. They're also not identically distributed, since variance is changing with time.

**What are some real examples?**

* Stock prices (over short time scales - days, not months/years)
* Brownian motion (continous time) - diffusion of molecules
* Null models for decision making (no evidence accumulation)

## Random Walk with Drift

More frequently, we see the concept of the random walk with drift ($\delta$). This extends the idea of the random walk.

$x_t = \delta + x_{t-1} + w_t$ with initial condition $x_0 = 0$.

Equivalently, $x_t = \delta t + \displaystyle\sum_{j=1}^t w_j$

![Random walk with and without drift](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec2_random_walk.png)

Here, the expected value is related directly to the drift term: $\mathbb{E}[x_t] = \delta t + x_0$. However, if we know the drift and we can condition on a prior observations ($x_s$, we can get a conditional expectation: $\mathbb{E}[x_t | x_s] = x_s + \delta (t-s)$

Again, the variance scales with the number of time points as noise is accumulating step by step.

**What are some real examples?**

* Stock prices over longer time scales
* Decision making (drift diffusion models)
* Atmospheric concentrations of CO2 (drift represents human influences, stochastic noise reflects natural variability)

## Drift diffusion models

Drift diffusion models are a cognitive model explaining how people accumulate evidence to make decisions. In these models, $x_t$ is a decision variable, and the drift $\delta$ represents the mean evidence gained per unit time. Usually we also set boundaries for a binary choice: $-1$ for an incorrect choice or $1$ for a correct choice. We can then calculate the reaction time for the decision, which is the first time at which $x_t$ hits either of the choice values, at which point the random walk stops. For no drift, we expect a long reaction time and a 50/50 probability of the correct or incorrect choice. High confidence / high information can be represented by a high value of $\delta$. For example, your $\delta$ values may be lower if you are doing a visual discrimination task under a lot of noise (uncertainty). $\delta$ values could also be increased by motivation or by higher certainty information.

An example of neurons performing something that looks like evidence accumulation is shown from [Gold \& Shadlen (2007)](https://pubmed.ncbi.nlm.nih.gov/17600525/). This is from a decision making task in which a monkey watches movies of moving dots, where a certain percentage of the dots move coherently, making the task either very easy (all the dots moving the same way) or not (very few coherent dots).

![neurons during a dot motion task show drift diffusion like characteristics](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec2_dot_motion.png)

---

[← Autoregression](05-autoregression.md) · [Up: contents](index.md) · [Signal in noise →](07-signal-in-noise.md)
