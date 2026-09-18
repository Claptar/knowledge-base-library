---
title: 6 Random Walk
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 6 Random Walk

Another simple but important / helpful extension to the idea of white noise is the random walk. The simple random walk is defined as:

$$x_t = x_{t-1} + w_t \text{ with initial condition } x_0 = 0.$$

Equivalently, $x_t = \sum_{j=1}^t w_j$

The expected value of any time point $\text{E}[x_t] = \text{E}[x_0] = 0$, so the mean does not vary over time.

The variance of a random walk, on the other hand, is additive and grows linearly with time:

$$\text{Var}(x_t) = \text{Var}(\sum_{j=1}^t w_j) = t\sigma^2$$

Are random walks iid? No! Each time point is not independent, but depends on the past time point. They're also not identically distributed, since variance is changing with time.

**What are some real examples?**

• Stock prices (over short time scales - days, not months/years)

• Brownian motion (continous time) - diffusion of molecules

• Null models for decision making (no evidence accumulation)

### 6.1 Random Walk with Drift

More frequently, we see the concept of the random walk with drift ($\delta$). This extends the idea of the random walk.

$$x_t = \delta + x_{t-1} + w_t \text{ with initial condition } x_0 = 0.$$

Equivalently, $x_t = \delta t + \sum_{j=1}^t w_j$

Fig. 1.11. Random walk, $\sigma_w = 1$, with drift $\delta = .2$ (upper jagged line), without drift, $\delta = 0$ (lower jagged line), and straight (dashed) lines with slope $\delta$

Here, the expected value is related directly to the drift term: $\text{E}[x_t] = \delta t + x_0$. However, if we know the drift and we can condition on a prior observations ($x_s$, we can get a conditional expectation: $\text{E}[x_t | x_s] = x_s + \delta(t - s)$

Again, the variance scales with the number of time points as noise is accumulating step by step.

**What are some real examples?**

• Stock prices over longer time scales

• Decision making (drift diffusion models)

• Atmospheric concentrations of $\text{CO}_2$ (drift represents human influences, stochastic noise reflects natural variability)

### 6.2 Drift diffusion models

Drift diffusion models are a cognitive model explaining how people accumulate evidence to make decisions. In these models, $x_t$ is a decision variable, and the drift $\delta$ represents the mean evidence gained per unit time. Usually we also set boundaries for a binary choice: -1 for an incorrect choice or 1 for a correct choice. We can then calculate the reaction time for the decision, which is the first time at which $x_t$ hits either of the choice values, at which point the random walk stops. For no drift, we expect a long reaction time and a 50/50 probability of the correct or incorrect choice. High confidence / high information can be represented by a high value of $\delta$. For example, your $\delta$ values may be lower if you are doing a visual discrimination task under a lot of noise (uncertainty). $\delta$ values could also be increased by motivation or by higher certainty information.

An example of neurons performing something that looks like evidence accumulation is shown from Gold & Shadlen (2007). This is from a decision making task in which a monkey watches movies of moving dots, where a certain percentage of the dots move coherently, making the task either very easy (all the dots moving the same way) or not (very few coherent dots).

## 7 Signal in noise

More generally, we can see other examples of periodic signals contaminated by white noise. For example:

$$x_t = A * \cos(2\pi\omega t + \phi) + w_t$$

Where $A$ is the amplitude of the signal, $\omega$ is the frequency of the oscillation, and $\phi$ is a phase shift.

The ratio of the amplitude of the signal to the standard deviation of the noise determines the SNR - signal to noise ratio. The larger the SNR, the easier it is to recover our signal.

Later, we will use various forms of regression to try to recover these signals!

## 8 Next week:

• Measures of dependence! Read SS Chapter 1, sections 1.3-1.7.

---

[← Lecture 2 Notes - Characteristics of Time Series](01-lecture-2-notes---characteristics-of-time-series.md) · [Up: contents](index.md)
