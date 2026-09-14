---
title: In a world where… {.anchored anchor-id="in-a-world-where"}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# In a world where… {.anchored anchor-id="in-a-world-where"}

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

To toy around with the notion of statistical power, let’s start by creating a toy schedule of potential outcomes for 10 units. I’ll start with only the potential outcomes under the control.

``` {.sourceCode .r .code-with-copy}
my_true_sched <- tibble(Y_0 = c(-.1, -.5, 1.2, -1.4, .1, -1, 1.1, 0, .02, .5))
```

To populate the second potential outcome, let’s work with a very particular assumption about the causal mechanism: that the ITE (and thus the ATE) is 1 for all units.

``` {.sourceCode .r .code-with-copy}
tau <- 1
my_true_sched <- my_true_sched |>
  mutate(Y_1 = Y_0 + tau)
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [“Conduct the experiment” {.anchored anchor-id="conduct-the-experiment"} →](03-conduct-the-experiment-anchored-anchor-id-conduct-the-experi.md)
