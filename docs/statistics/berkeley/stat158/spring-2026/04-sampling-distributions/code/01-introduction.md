---
title: Introduction
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/code.html
source_file: sources/berkeley-stat158/spring-2026/04-sampling-distributions/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Introduction

**Source:** [`04-sampling-distributions/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# Sampling Distributions {#sampling-distributions .title}

Code

To understand the behavior of estimators under a random process, we start by assuming the impossible: that we know the full schedule of potential outcomes. Here it is, for six students who went through the anchoring experiment.

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

Let’s compute the individual treatment effect (ITE) for each of the size students.

``` {.sourceCode .r .code-with-copy}
anchor_mini_sched <- anchor_mini_sched |>
    mutate(tau = Y_1 - Y_0)
anchor_mini_sched
```

    # A tibble: 6 × 3
        Y_0   Y_1   tau
      <dbl> <dbl> <dbl>
    1    15    31    16
    2    15    22     7
    3    19    45    26
    4     2    20    18
    5    10    20    10
    6     8    15     7

Now we can calculate summary statistics on the schedule, which are better thought of as parameters.

``` {.sourceCode .r .code-with-copy}
parameters <- anchor_mini_sched |>
    summarize(Ybar_1 = mean(Y_1),
              Ybar_0 = mean(Y_0),
              ATE = mean(tau))
parameters
```

    # A tibble: 1 × 3
      Ybar_1 Ybar_0   ATE
       <dbl>  <dbl> <dbl>
    1   25.5   11.5    14

Note that the Average Treatment Effect (ATE), 14, our estimand, can either be expressed as the difference between the means of the potential outcomes, <span class="math inline">\$\\bar{Y}\_1 - \\bar{Y}\_0\$</span>, or as the average of the <span class="math inline">\$\\tau\_i\$</span>.

---

[Up: contents](index.md) · [A single experiment →](02-a-single-experiment.md)
