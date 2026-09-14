---
title: Confidence Intervals {#confidence-intervals-1}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/17-confidence-intervals/slides.html
source_file: sources/berkeley-stat158/spring-2026/17-confidence-intervals/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Confidence Intervals {#confidence-intervals-1}

**Source:** [`17-confidence-intervals/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/17-confidence-intervals/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Recall: The Anchoring Experiment

<figure>

</figure>

## Estimating ATE

<span class="math display">\\$$ \\widehat{ATE} = \\hat{\\bar{Y}}\_1 - \\hat{\\bar{Y}}\_0 \\$$</span>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
diff_in_means <- function(y, x) {
  groups <- split(y, x)
  ybar0 <- mean(groups[[1]])
  ybar1 <- mean(groups[[2]])
  ybar1 - ybar0
}

ate_hat <- diff_in_means(anchor$y, anchor$d)
ate_hat
```

    [1] 15.46992

---

[← Confidence Intervals {#confidence-intervals .title}](01-confidence-intervals-confidence-intervals-title.md) · [Up: contents](index.md) · [Randomization CI →](03-randomization-ci.md)
