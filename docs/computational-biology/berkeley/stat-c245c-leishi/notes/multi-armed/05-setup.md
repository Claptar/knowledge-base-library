---
title: setup
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# setup

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

set.seed(240)
horizon <- 1000L
simulations <- 1000L
conversionProbabilities <- c(0.05, 0.10, 0.15, 0.20, 0.25)
nTestSample <- 0.5 * horizon
clickProb <- rep(NA, simulations)
adDistMatrix <- matrix(NA, nrow = simulations, ncol = length(conversionProbabilities))
adDistMatrixAB <- matrix(NA, nrow = simulations, ncol = length(conversionProbabilities)) # simulation
for(i in 1:simulations){
  testSample <- sapply(conversionProbabilities,  function(x) sample(0:1, nTestSample, replace = TRUE, prob = c(1 - x, x)))

  testColumns <- (1:length(conversionProbabilities))[-which.max(colSums(testSample))]

  p.values <- sapply(testColumns, function(x) prop.test(x = colSums(testSample[, c(x, which.max(colSums(testSample)))]), n = rep(nTestSample, 2))$p.value)

  adsAfterABTest <- (1:length(conversionProbabilities))[- testColumns[which(p.values < 0.05)]]

  # now just with the best performing ad(s)
  ABSample <- sapply(conversionProbabilities[adsAfterABTest],
                     function(x) sample(0:1, round((horizon - nTestSample)*length(conversionProbabilities) /length(adsAfterABTest), 0), replace = TRUE, prob = c(1 - x, x)))

  clickProbTest <- sum(as.vector(testSample)) / length(unlist(testSample))

  clickProbAB <- sum(as.vector(ABSample)) / length(unlist(ABSample))

  clickProb[i] <- clickProbTest * (nTestSample / horizon) + clickProbAB * (1 - nTestSample / horizon)

  # distribution of which ads were seen over the course of all trials
  adDistMatrix[i,] <- rep(1 / length(conversionProbabilities), length(conversionProbabilities))

  adDistributionAB <- rep(0, length(conversionProbabilities))

  adDistributionAB[adsAfterABTest] <- rep(1 / length(adsAfterABTest), length(adsAfterABTest))

  adDistMatrixAB[i,] <- adDistributionAB
  }

---

[← A/B TEST](04-a-b-test.md) · [Up: contents](index.md) · [Multi armed Part 06 — →](06-multi-armed-part-06.md)
