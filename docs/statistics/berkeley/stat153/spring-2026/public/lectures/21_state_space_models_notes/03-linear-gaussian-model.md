---
title: Linear Gaussian Model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/21_state_space_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Linear Gaussian Model

**Source:** [`public/lectures/21_state_space_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We can write the basic form of a linear Gaussian state-space model, also called the dynamic linear model (DLM) with the following *state equation*:

$$x_t = \Phi x_{t-1} + \Upsilon u_t + w_t$$

This is an order one, $p$-dimensional vector autoregression where $w_t$ are $p \times 1$ white Gaussian noise, $w_t \overset{iid}\sim N_p(0,Q)$. At $t=0$, we start with a normal vector $x_0 \sim N_p(\mu_0, \sigma_0)$.

* $\Phi$ is the state transition parameter and is a $p \times p$ matrix. This describes the internal dynamics, i.e., how the state at $t-1$ produces the state at $t$
* $u_t$ is an $r \times 1$ fixed input series. This includes any covariates, experimental conditions, interventions, or other aspects you might supply rather than learning from the data. $\Upsilon$ is $p \times r$ and controls how those inputs influence the state.
* $w_t$ is the state noise and is Gaussian with covariance $Q$.

We do not observe this state vector $x_t$ directly, instead we see a linearly transformed version of it with noise added:

*Observation equation:*
$$y_t = A_t x_t+\Gamma u_t + v_t$$

* The data vector $y_t$ is $q$-dimensional, which can be $>p$ or $<p$, the state dimension.
* $A_t$ is a $q \times p$ measurement or observation matrix. This specifies which linear combinations of the state we measure. By allowing $A_t$ to depend on $t$, we can handle things like missing data by dropping rows for time points where measurements are missing.
* $v_t$ is measurement noise with covariance $R$
* $\Gamma$ is $q \times r$ and lets the inputs $u_t$ affect the observation directly.

So external inputs can influence $y_t$ through either $\Upsilon u_t$ (through the state equation) or $\Gamma u_t$ (through the observation equation). As a concrete example, say $x_t$ is a person's true blood pressure, and $y_t$ is the blood pressure measured by a blood pressure cuff. Say a drug was administered at time $t$ - this would then change the state equation, because it will modify the actual blood pressure. On the other hand, an input like "which nurse took the reading" or "which blood pressure cuff was used" would belong in the observation equation, since it will affect what the meter reports, but not the underlying physiological cause. $\Gamma=0$ is commonly used, so inputs only drive the state. On the other hand $\Upsilon=0$ might show up when you're trying to model known measurement artifacts.

---

[← Extension of AR model to VAR](02-extension-of-ar-model-to-var.md) · [Up: contents](index.md) · [Bone marrow transplant example →](04-bone-marrow-transplant-example.md)
