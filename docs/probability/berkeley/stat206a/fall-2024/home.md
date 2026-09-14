---
title: 'Statistics 206a: Advanced Topics in Probability and Stochastic Process'
source: https://github.com/berkeley-stat206a/fall-2024/blob/67b33919409b2507b48465b8d9e92b11fb41a983/index.qmd
source_file: sources/berkeley-stat206a/fall-2024/index.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistics 206a: Advanced Topics in Probability and Stochastic Process

**Source:** [`index.qmd`](https://github.com/berkeley-stat206a/fall-2024/blob/67b33919409b2507b48465b8d9e92b11fb41a983/index.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Geometric aspects of high dimensional Gibbs measures

High dimensional Gibbs measures are ubiquitous in probability theory, statistical mechanics and theoretical computer science. A generic example, say on the hypercube $Q=\{-1,1\}^n$, is given by a Hamiltonian $H: Q\to \mathbb{R}$, with the measure $\mu$ at $\sigma \in Q$ being proportional to $\exp\left(-\beta H(\sigma)\right)$ where $\beta>0$ is the inverse temperature parameter. $Z$, the normalizing constant, is known as the partition function. Central examples include  the Ising model, spin glass models, exponential random graphs, the hardcore model and so on. Such Gibbs measures also admit natural Glauber dynamics which keep $\mu$ stationary.

The energy landscape induced by the Hamiltonian can often be quite complicated admitting exponentially many near ground states (the ground state is the state with the minimal energy).

In this course we will learn various techniques to estimate the partition function as well as establish structure theorems for a variety of Gibbs measures and the behavior of the associated Glauber dynamics. Phenomena such as super-concentration, chaos, multiple valleys and peaks, replica symmetry/breaking and metastability will be explored.

We will assume familiarity with the basics of graduate probability equivalent to Stat 205 A.

---

[Up: contents](index.md)
