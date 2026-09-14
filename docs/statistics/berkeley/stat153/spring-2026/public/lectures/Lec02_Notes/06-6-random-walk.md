---
title: 6 Random Walk
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Random Walk

**Source:** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Another simple but important / helpful extension to the idea of white noise is the random walk. The simple random walk is defined as:

_xt_ = _xt−_ 1 + _wt_ with initial condition _x_ 0 = 0.

2

_t_ Equivalently, _xt_ = ∑ _wj j_ =1

The expected value of any time point E[ _xt_ ] = E[ _x_ 0] = 0, so the mean does not vary over time.

The variance of a random walk, on the other hand, is additive and grows linearly with time:


Are random walks iid? No! Each time point is not independent, but depends on the past time point. They’re also not identically distributed, since variance is changing with time.

**What are some real examples?**

- Stock prices (over short time scales - days, not months/years)

- Brownian motion (continous time) - diffusion of molecules

- Null models for decision making (no evidence accumulation)

## **6.1 Random Walk with Drift**

More frequently, we see the concept of the random walk with drift ( _δ_ ). This extends the idea of the random walk.

_xt_ = _δ_ + _xt−_ 1 + _wt_ with initial condition _x_ 0 = 0.


<!-- Start of picture text -->
t<br>Equivalently, xt =  δt  + ∑ wj<br>j =1<br><!-- End of picture text -->


Here, the expected value is related directly to the drift term: E[ _xt_ ] = _δt_ + _x_ 0. However, if we know the drift and we can condition on a prior observations ( _xs_ , we can get a conditional expectation: E[ _xt|xs_ ] = _xs_ + _δ_ ( _t − s_ )

Again, the variance scales with the number of time points as noise is accumulating step by step.

**What are some real examples?**

- Stock prices over longer time scales

3

- Decision making (drift diffusion models)

- Atmospheric concentrations of CO2 (drift represents human influences, stochastic noise reflects natural variability)

## **6.2 Drift diffusion models**

Drift diffusion models are a cognitive model explaining how people accumulate evidence to make decisions. In these models, _xt_ is a decision variable, and the drift _δ_ represents the mean evidence gained per unit time. Usually we also set boundaries for a binary choice: -1 for an incorrect choice or 1 for a correct choice. We can then calculate the reaction time for the decision, which is the first time at which _xt_ hits either of the choice values, at which point the random walk stops. For no drift, we expect a long reaction time and a 50/50 probability of the correct or incorrect choice. High confidence / high information can be represented by a high value of _δ_ . For example, your _δ_ values may be lower if you are doing a visual discrimination task under a lot of noise (uncertainty). _δ_ values could also be increased by motivation or by higher certainty information.

An example of neurons performing something that looks like evidence accumulation is shown from Gold & Shadlen (2007). This is from a decision making task in which a monkey watches movies of moving dots, where a certain percentage of the dots move coherently, making the task either very easy (all the dots moving the same way) or not (very few coherent dots).


4

---

[← 5 Autoregression](05-5-autoregression.md) · [Up: contents](index.md) · [7 Signal in noise →](07-7-signal-in-noise.md)
