---
title: Review / basic concepts
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Review / basic concepts

* **Reading**: Chapter 1.2 – Shumway and Stoffer

* Most time series are not iid
* Instead, most have dependence on time
	* Sometimes called "autocorrelation" - the $x_t$ is correlated with $x_{t-1}, ..., x_{t-p}$
* Some have _drift_
* The purpose of time series analysis is to develop mathematical models to provide plausible explanations for sample data

## Stochastic process

* Systems or phenomena that evolve randomly over time
* Many time series are modeled as realizations of stochastic processes, even though they contain components that are deterministic / predictable.
* These are addressed in more detail in Stat150!

## White noise

Many real-world time series are a combination of underlying signal $s_t$ plus noise $w_t$. In some (nice) cases, $w_t$ is _white noise_.

White noise is a special case of uncorrelated variables in sequence, e.g. $x_t$ where $t=1,2,3,...$. White noise, unlike most real time series, *is* iid, with mean $0$ and variance $\sigma^2_w$.  One very useful case is white noise from a Gaussian distribution, where we can write: $w_t \sim \mbox{iid } \mathcal{N}(0,\sigma^2_w)$.

If all time series could be described in this way, classical statistics would suffice.

What does white noise look like?

![White noise time series](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec2_white_noise.png)

## Moving average

One way of smoothing a time series (including white noise) is to average the value at a time point $t$ with its neighbors $t-1$ and $t+1$ (or an even larger window from $t-p$ to $t+p$). For example:

$v_t = \frac{1}{3}(w_{t-1}+w_t+w_{t+1})$

or more generally

$v_t = \frac{1}{n} \displaystyle\sum_{k=-\frac{n-1}{2}}^{\frac{n-1}{2}} w_{t+k}$ for odd $n$

This is inherently a low-pass filter (lets low frequency signals pass, gets rid of high frequency). It preserves trends slower than $\sim n$ samples, and suppresses oscillations with period $\lesssim n$ samples.

**When do we use this?**

We might use this to reveal trends in noisy time series data, remove fluctuations we consider "noise", or do simple online smoothing (especially if we choose the window to include only data in the past). However, this is the most basic form of smoothing and is typically replaced by more complex methods such as exponential moving averages, Kalman filters, median filter, etc.

## Autoregression

Another flavor of dataset we might see is data that comes from an autoregressive process. Autoregression = regression or prediction based on past values of the same time series ("auto").

This might look something like:

$x_t = 1.5 x_{t-1} - 0.75 x_{t-2} + w_t$

You will see what this looks like in Lab 1. Because the data at $t$ relies on $t-1$ and $t-2$ (the prior two data points), this is an AR(2) process. Generating data in this way can result in oscillatory behavior.

---

[Up: contents](index.md) · [Random Walk →](02-random-walk.md)
