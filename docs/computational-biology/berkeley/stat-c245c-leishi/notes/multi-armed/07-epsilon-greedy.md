---
title: EPSILON GREEDY
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# EPSILON GREEDY

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

horizon <- 1000L
simulations <- 1000L
conversionProbabilities <- c(0.05, 0.10, 0.15, 0.20, 0.25)
bandit <- BasicBernoulliBandit$new(weights = conversionProbabilities)
policy <- EpsilonGreedyPolicy$new(epsilon = 0.10)
agent <- Agent$new(policy, bandit)
historyEG <- Simulator$new(agent, horizon, simulations)$run()
plot(historyEG, type = "arms",legend_labels = c('Ad 1', 'Ad 2', 'Ad 3', 'Ad 4', 'Ad 5'), legend_title = 'Epsilon Greedy', legend_position = "topright", smooth = TRUE)
summary(historyEG)

```

```r

---

[← Multi armed Part 06 —](06-multi-armed-part-06.md) · [Up: contents](index.md) · [THOMPSON SAMPLING →](08-thompson-sampling.md)
