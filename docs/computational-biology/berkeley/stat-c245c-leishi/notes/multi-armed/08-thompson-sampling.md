---
title: THOMPSON SAMPLING
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# THOMPSON SAMPLING

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

horizon <- 1000L
simulations <- 1000L
conversionProbabilities <- c(0.05, 0.10, 0.15, 0.20, 0.25)
bandit <- BasicBernoulliBandit$new(weights = conversionProbabilities)
policy <- ThompsonSamplingPolicy$new(alpha = 1, beta = 1)
agent <- Agent$new(policy, bandit)
historyThompson <- Simulator$new(agent, horizon, simulations)$run()
plot(historyThompson, type = "arms",  legend_labels = c('Ad 1', 'Ad 2', 'Ad 3', 'Ad 4', 'Ad 5'), legend_title = 'Thompson Sampling', legend_position = "topright", smooth = TRUE)
summary(historyThompson)

```


## Drawback of bandit problem & algorithms

The Multi-armed bandit is a simple model for many real-world systems.

Practical issue:

1. Not personalized

Theoretical issue:

1. Highly non-smooth struture
2. Highly probabilistic dependence

---

[← EPSILON GREEDY](07-epsilon-greedy.md) · [Up: contents](index.md)
