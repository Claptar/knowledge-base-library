---
title: Ps
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/ps.html
source_file: sources/berkeley-stat158/spring-2026/04-sampling-distributions/ps.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Ps

**Source:** [`04-sampling-distributions/ps.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/ps.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

------------------------------------------------------------------------

**Sampling Distributions**. Consider the following schedule of potential outcomes corresponding to six students in the anchoring experiment.

``` {.sourceCode .r .code-with-copy}
library(tidyverse)
anchor_mini_sched <- tibble(Y_0 = c(15, 15, 19, 2, 10, 8),
                            Y_1 = c(31, 22, 45, 20, 20, 15))
anchor_mini_sched
```

    # A tibble: 6 × 2
        Y_0   Y_1
      <dbl> <dbl>
    1    15    31
    2    15    22
    3    19    45
    4     2    20
    5    10    20
    6     8    15

1.  If the random assignment in the experiment involved assigning indices to the students, randomly permuting a vector of three 1s and three 0s, then assigning the units to either treatment (1) or control (0) based on whether the index in the vector was a 1 or a 0, what is the sampling distribution of <span class="math inline">\$\\widehat{ATE}\$</span>? Display the distribution as a table with two columns (one for the value of the RV, the other for the probability) and as a plot.

<!-- -->

1.  Using this sampling distribution, calculate the expected value and variance of <span class="math inline">\$\\widehat{ATE}\$</span>.

<!-- -->

1.  What is the smallest number of permutations / partitions that you need to consider in order to know the sampling distribution?

------------------------------------------------------------------------

---

[Up: contents](../index.md)
