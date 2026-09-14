---
title: Extension of AR model to VAR
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/21_state_space_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Extension of AR model to VAR

**Source:** [`public/lectures/21_state_space_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Before we get into state space models, we should briefly mention an extension of the AR model to multiple dimensions, which is the VAR model (vector autoregressive model). Everything we've talked about so far with AR has been for a single series. Sometimes, however, we may have $k$ multiple series that influence each other. For the VAR model, we write:

$$x_t = \alpha + \Phi x_{t-1} + w_t$$,

Where $x_t$ is now a vector and $\Phi$ is a $(k\times k)$ *transition matrix* that expresses the dependence of $x_t$ on $x_{t-1}$. You can read more about this in Chapter 5.5 of Shumway and Stoffer. State space models are more general extension of this.

---

[← State Space Models](01-state-space-models.md) · [Up: contents](index.md) · [Linear Gaussian Model →](03-linear-gaussian-model.md)
