---
title: Continuation of State Space Models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Continuation of State Space Models

* **Reading**: Ch 6.2 - Shumway and Stoffer

## Examples

To remind you, we talked a bit about some examples last time of where state space models might be useful:

* Estimating global warming/global temperatures $x_t$ from land and sea temperature measurements $y_t$
* Brain computer interfaces (BCI) - we want to infer intended cursor velocity ($x_t$) from brain measurements from 100 electrodes in motor cortex $y_t$
* Health - we want to estimate true blood glucose level $x_t$ from $y_t$ intermittent measurements from a continuous glucose monitor with some sensor drift.
* Finance - we want to measure volatility $x_t$ of the S&P500 on day $t$, we observe $y_t$ daily log returns

## Advantages of state space models

What are the advantages of state space models as opposed to other models we've discussed in this class?

1. They deal well with missing data and don't require every time point to be observed. You can still get estimates of the latent state for those missing time points.
2. We can separate process noise from measurement noise. In ARIMA models, we have just one noise term (innovations/shocks). For real scientific applications, we may have noisy sensors where the measurement reading's error is distinct from underlying noise in the true signal.
3. We can have time-varying parameters (unlike fixed $\beta$ in a regression model).

---

[Up: contents](index.md) · [Filtering, smoothing, and forecasting →](02-filtering-smoothing-and-forecasting.md)
