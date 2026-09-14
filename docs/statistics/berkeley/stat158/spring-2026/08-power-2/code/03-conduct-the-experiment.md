---
title: “Conduct the experiment”
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# “Conduct the experiment”

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Let’s assume the experimental design involves randomly assigning 5 units each to the treatment and control group. Let’s simulate that what that process would be like; this is us conducting our single experiment.

``` {.sourceCode .r .code-with-copy}
set.seed(4613)

n_0 <- 5
n_1 <- 5
d_i <- c(rep(0, n_0), rep(1, n_1))

my_data <- my_true_sched |>
  mutate(d_i = sample(d_i),
         y_i = Y_1 * d_i + Y_0 * (1 - d_i)) |>
  select(d_i, y_i)

my_data
```

    # A tibble: 10 × 2
         d_i   y_i
       <dbl> <dbl>
     1     1  0.9
     2     0 -0.5
     3     1  2.2
     4     0 -1.4
     5     0  0.1
     6     0 -1
     7     0  1.1
     8     1  1
     9     1  1.02
    10     1  1.5

Let’s do a test of the Fisher sharp null hypothesis that the ITE is zero for all units, let’s use the difference in means as a test statistic, and let’s use an alpha-level of .05. For a first step, let’s calculate our test statistic.

``` {.sourceCode .r .code-with-copy}
ATE_obs <- my_data |>
  group_by(d_i) |>
  summarize(Ybar_hat = mean(y_i)) |>
  summarize(ATE_obs = diff(Ybar_hat)) |>
  pull(ATE_obs)

ATE_obs
```

    [1] 1.664

To get our p-value, we need a sampling distribution. For that, we need to build a null schedule of outcomes, one where the potential outcome is the same under both treatments.

``` {.sourceCode .r .code-with-copy}
my_null_sched <- my_data |>
  mutate(Y_0 = y_i,
         Y_1 = y_i) |>
  select(Y_0, Y_1)
```

Note that the schedule under the null is different than the true schedule!

``` {.sourceCode .r .code-with-copy}
my_true_sched
```

    # A tibble: 10 × 2
         Y_0   Y_1
       <dbl> <dbl>
     1 -0.1   0.9
     2 -0.5   0.5
     3  1.2   2.2
     4 -1.4  -0.4
     5  0.1   1.1
     6 -1     0
     7  1.1   2.1
     8  0     1
     9  0.02  1.02
    10  0.5   1.5

``` {.sourceCode .r .code-with-copy}
my_null_sched
```

    # A tibble: 10 × 2
         Y_0   Y_1
       <dbl> <dbl>
     1  0.9   0.9
     2 -0.5  -0.5
     3  2.2   2.2
     4 -1.4  -1.4
     5  0.1   0.1
     6 -1    -1
     7  1.1   1.1
     8  1     1
     9  1.02  1.02
    10  1.5   1.5

---

[← In a world where…](02-in-a-world-where.md) · [Up: contents](index.md) · [Find Sampling Distribution under \$H\0\$ →](04-find-sampling-distribution-under.md)
