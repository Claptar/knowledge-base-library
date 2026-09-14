---
title: A single experiment {.anchored anchor-id="a-single-experiment"}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/code.html
source_file: sources/berkeley-stat158/spring-2026/04-sampling-distributions/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# A single experiment {.anchored anchor-id="a-single-experiment"}

**Source:** [`04-sampling-distributions/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/04-sampling-distributions/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Let’s simulate a single randomized experiment conducted on these six students by randomly assigning them to get the treatment (`1`) or the control (`0`).

``` {.sourceCode .r .code-with-copy}
set.seed(4032) # fix the randomness so we draw the same random numbers
anchor_mini_sched <- anchor_mini_sched |>
    mutate(d_i = sample(c(0, 0, 0, 1, 1, 1)),
           y_i = Y_1 * d_i +  Y_0 * (1 - d_i))
anchor_mini_sched
```

    # A tibble: 6 × 5
        Y_0   Y_1   tau   d_i   y_i
      <dbl> <dbl> <dbl> <dbl> <dbl>
    1    15    31    16     1    31
    2    15    22     7     1    22
    3    19    45    26     0    19
    4     2    20    18     1    20
    5    10    20    10     0    10
    6     8    15     7     0     8

Our estimator for the ATE will be the difference in the average responses of the units in the treated group and the control group.

``` {.sourceCode .r .code-with-copy}
ATE_hat <- anchor_mini_sched |>
    group_by(d_i) |>
    summarize(Ybar_hat = mean(y_i)) |>
    summarize(ATE_hat = diff(Ybar_hat)) |>
    pull(ATE_hat)
ATE_hat
```

    [1] 12

In a normal data analysis, all we get to see is our estimate, 12. Since we know the full schedule, here we’re effectively playing this game in “God Mode” and can know that the value of the parameter was in fact 14. So this particular estimate was a bit off, but not by much.

To learn about how much variability we can expect in our estimator, we need to know it’s sampling distribution.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Code Part 03 — →](03-code-part-03.md)
