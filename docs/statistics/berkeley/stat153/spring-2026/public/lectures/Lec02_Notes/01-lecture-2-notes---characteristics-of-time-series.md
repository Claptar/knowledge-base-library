---
title: Lecture 2 Notes - Characteristics of Time Series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 2 Notes - Characteristics of Time Series

Liberty Hamilton

Thursday $22^{\text{nd}}$ January, 2026

• Reading: Chapter 1.2 – Shumway and Stoffer

## 1 Review / basic concepts

• Most time series are not iid

• Instead, most have dependence on time

– Sometimes called "autocorrelation" - the $x_t$ is correlated with $x_{t-1}, ..., x_{t-p}$

• Some have drift

• The purpose of time series analysis is to develop mathematical models to provide plausible explanations for sample data

## 2 Stochastic process

• Systems or phenomena that evolve randomly over time

• Many time series are modeled as realizations of stochastic processes, even though they contain components that are deterministic / predictable.

• These are addressed in more detail in Stat150!

## 3 White noise

Many real-world time series are a combination of underlying signal $s_t$ plus noise $w_t$. In some (nice) cases, $w_t$ is *white noise*.

White noise is a special case of uncorrelated variables in sequence, e.g. $x_t$ where $t = 1, 2, 3, ....$ White noise, unlike most real time series, is iid, with mean 0 and variance $\sigma^2_w$. One very useful case is white noise from a Gaussian distribution, where we can write: $w_t \sim \text{iid } \mathcal{N}(0, \sigma_w^2)$.

If all time series could be described in this way, classical statistics would suffice.

What does white noise look like?

## 4 Moving average

One way of smoothing a time series (including white noise) is to average the value at a time point $t$ with its neighbors $t - 1$ and $t + 1$ (or an even larger window from $t - p$ to $t + p$). For example:

$$v_t = \frac{1}{3}(w_{t-1} + w_t + w_{t+1})$$

or more generally

$$v_t = \frac{1}{n} \sum_{k=-\frac{n-1}{2}}^{\frac{n-1}{2}} w_{t+k} \text{ for odd } n$$

This is inherently a low-pass filter (lets low frequency signals pass, gets rid of high frequency). It preserves trends slower than $\sim n$ samples, and suppresses oscillations with period $\lesssim n$ samples.

**When do we use this?**

We might use this to reveal trends in noisy time series data, remove fluctuations we consider "noise", or do simple online smoothing (especially if we choose the window to include only data in the past). However, this is the most basic form of smoothing and is typically replaced by more complex methods such as exponential moving averages, Kalman filters, median filter, etc.

## 5 Autoregression

Another flavor of dataset we might see is data that comes from an autoregressive process. Autoregression = regression or prediction based on past values of the same time series ("auto").

This might look something like:

$$x_t = 1.5x_{t-1} - 0.75x_{t-2} + w_t$$

You will see what this looks like in Lab 1. Because the data at $t$ relies on $t-1$ and $t-2$ (the prior two data points), this is an AR(2) process. Generating data in this way can result in oscillatory behavior.

---

[Up: contents](index.md) · [6 Random Walk →](02-6-random-walk.md)
