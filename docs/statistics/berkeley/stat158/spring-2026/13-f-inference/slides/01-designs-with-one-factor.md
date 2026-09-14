---
title: Designs with One Factor
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/13-f-inference/slides.html
source_file: sources/berkeley-stat158/spring-2026/13-f-inference/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Designs with One Factor

**Source:** [`13-f-inference/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/13-f-inference/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Babies Walking

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
babies
```

       walk       program
    1     9       Special
    2     9       Special
    3    10       Special
    4    10       Special
    5    13       Special
    6    11       Regular
    7    10       Regular
    8    10       Regular
    9    12       Regular
    10   10       Regular
    11   11 Weekly report
    12   12 Weekly report
    13    9 Weekly report
    14   12 Weekly report
    15   13 Weekly report
    16   13 Single report
    17   11 Single report
    18   12 Single report
    19   13 Single report
    20   11 Single report

## EDA

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(ggplot2)
library(ggbeeswarm)
babies |>
  ggplot(aes(x = program, y = walk)) +
  geom_beeswarm(cex = 3, size = 3)
```

<figure>

</figure>

## EDA

## Estimates: contrasts

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(dplyr)
group_means <- babies |>
  group_by(program) |>
  summarize(avg = mean(walk))
group_means
```

    # A tibble: 4 × 2
      program         avg
      <fct>         <dbl>
    1 Special        10.2
    2 Regular        10.6
    3 Weekly report  11.4
    4 Single report  12

## Estimates: contrasts

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[1] - group_means$avg[2]
```

    [1] -0.4

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[1] - group_means$avg[3]
```

    [1] -1.2

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[1] - group_means$avg[4]
```

    [1] -1.8

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[2] - group_means$avg[3]
```

    [1] -0.8

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[2] - group_means$avg[4]
```

    [1] -1.4

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
group_means$avg[3] - group_means$avg[4]
```

    [1] -0.6

## Estimates: Effects relative to benchmark

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
overall_mean <- mean(babies$walk)
a_hat1 <- group_means$avg[1] - overall_mean
a_hat2 <- group_means$avg[2] - overall_mean
a_hat3 <- group_means$avg[3] - overall_mean
a_hat4 <- group_means$avg[4] - overall_mean
c(a_hat1, a_hat2, a_hat3, a_hat4)
```

    [1] -0.85 -0.45  0.35  0.95

## Randomization-based Inference

The base R engine for randomization: `sample()`.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
a <- c(3, 5, 7, 9)
sample(x = a, size = 2, replace = FALSE)
```

    [1] 3 9

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sample(a, 4)
```

    [1] 5 3 9 7

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sample(a)
```

    [1] 5 9 3 7

## Simulating five draws under Null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
shuffle4 <- function(y, z) {
  Z <- sample(z) # source of randomness

  babies_sim <- data.frame(walk = y,
                           program = Z)
  group_means <- babies_sim |>
    group_by(program) |>
    summarize(avg = mean(walk))
  overall_mean <- mean(babies_sim$walk)
  stats <- c(group_means$avg[1] - overall_mean,
             group_means$avg[2] - overall_mean,
             group_means$avg[3] - overall_mean,
             group_means$avg[4] - overall_mean)
  stats
}
```

## Simulating five draws under Null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(5, shuffle4(y = babies$walk, z = babies$program))
null_stats
```

          [,1]  [,2]  [,3]  [,4]  [,5]
    [1,]  0.15 -0.05  0.35  0.15  0.35
    [2,] -0.85  0.15 -0.45  0.15 -0.45
    [3,]  0.75 -0.05  0.75 -0.25 -0.05
    [4,] -0.05 -0.05 -0.65 -0.05  0.15

To access simulations from <span class="math inline">\$\\hat{\\alpha}\_1\$</span>:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats[1, ] # extract first row as a vector.
```

    [1]  0.15 -0.05  0.35  0.15  0.35

## Simulating 500 draws under null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(500, shuffle4(y = babies$walk, z = babies$program))
null_1 <- null_stats[1, ]
null_2 <- null_stats[2, ]
null_3 <- null_stats[3, ]
null_4 <- null_stats[4, ]
```

## Null dist of <span class="math inline">\$\\hat{\\alpha}\_1\$</span> {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
null1 <- data.frame(stat = null_1)
ggplot(null1, aes(x = stat)) +
  geom_histogram()
```

<figure>

</figure>

## Null dist of <span class="math inline">\$\\hat{\\alpha}\_1\$</span> {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
null1 <- data.frame(stat = null_1)
ggplot(null1, aes(x = stat)) +
  geom_histogram() +
  geom_vline(xintercept = a_hat1, color = "tomato", lwd = 2)
```

<figure>

</figure>

## p-value for <span class="math inline">\$\\hat{\\alpha}\_1\$</span>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null1 |>
  summarize(pval = mean(stat < a_hat1) * 2)
```

       pval
    1 0.088

> What is our decision regarding <span class="math inline">\$H\_0\$</span>? . . .

At threshold of .05, we fail to reject the null.

## What about, say, <span class="math inline">\$\\hat{\\alpha}\_3\$</span>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null3 <- data.frame(stat = null_3)
ggplot(null3, aes(x = stat)) +
  geom_histogram() +
  geom_vline(xintercept = a_hat3, color = "tomato", lwd = 2)
```

<figure>

</figure>

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
babies |>
  group_by(program) |>
  summarize(var = var(walk))
```

    # A tibble: 4 × 2
      program         var
      <fct>         <dbl>
    1 Special         2.7
    2 Regular         0.8
    3 Weekly report   2.3
    4 Single report   1

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
babies |>
  group_by(program) |>
  summarize(var = var(walk)) |>
  summarize(avg_var = mean(var))
```

    # A tibble: 1 × 1
      avg_var
        <dbl>
    1     1.7

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
avg_var <- babies |>
  group_by(program) |>
  summarize(var = var(walk)) |>
  summarize(avg_var = mean(var)) |>
  pull(avg_var)
avg_var
```

    [1] 1.7

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
babies |>
  group_by(program) |>
  summarize(avg = mean(walk))
```

    # A tibble: 4 × 2
      program         avg
      <fct>         <dbl>
    1 Special        10.2
    2 Regular        10.6
    3 Weekly report  11.4
    4 Single report  12

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
babies |>
  group_by(program) |>
  summarize(avg = mean(walk)) |>
  summarize(var_avg = var(avg))
```

    # A tibble: 1 × 1
      var_avg
        <dbl>
    1   0.650

## Creating a single statistic {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
var_avg <- babies |>
  group_by(program) |>
  summarize(avg = mean(walk)) |>
  summarize(var_avg = var(avg)) |>
  pull(var_avg)
var_avg
```

    [1] 0.65

## Bringing them together

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
f_stat <- var_avg / avg_var
```

## Randomization-based Inference

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
shuffle4_f <- function(y, z) {
  Z <- sample(z) # source of randomness

  babies_sim <- data.frame(walk = y,
                           program = Z)

  avg_var <- babies_sim |>
    group_by(program) |>
    summarize(var = var(walk)) |>
    summarize(avg_var = mean(var)) |>
    pull(avg_var)
  var_avg <- babies_sim |>
    group_by(program) |>
    summarize(avg = mean(walk)) |>
    summarize(var_avg = var(avg)) |>
    pull(var_avg)

  var_avg / avg_var
}
```

## 5 draws from the null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(5, shuffle4_f(y = babies$walk, z = babies$program))
null_stats
```

    [1] 0.12048193 0.06590038 0.34095238 0.22982456 0.44923077

## 500 draws from the null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(500, shuffle4_f(y = babies$walk, z = babies$program))
null <- data.frame(stats = null_stats)

ggplot(null, aes(x = stats)) +
  geom_histogram() +
  geom_vline(xintercept = f_stat, color = "tomato", lwd = 2)
```

<figure>

</figure>

## p-value for F

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null |>
  summarize(pval = mean(stats > f_stat))
```

       pval
    1 0.154

---

[Up: contents](index.md) · [Model-Based Inference →](02-model-based-inference.md)
