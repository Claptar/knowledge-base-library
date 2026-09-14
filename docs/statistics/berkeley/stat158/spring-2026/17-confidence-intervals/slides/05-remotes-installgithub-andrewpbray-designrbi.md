---
title: remotes::installgithub("andrewpbray/designrbi")
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/17-confidence-intervals/slides.html
source_file: sources/berkeley-stat158/spring-2026/17-confidence-intervals/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# remotes::installgithub("andrewpbray/designrbi")

**Source:** [`17-confidence-intervals/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/17-confidence-intervals/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

library(designrbi)
```

## Convert Data to Schedule

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
schedule <- anchor |>
  experiment_to_schedule(treatment = d, response = y)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anchor
```

    # A tibble: 74 × 2
       d         y
       <fct> <dbl>
     1 11     16
     2 11      5
     3 73     20
     4 73     40
     5 11     73
     6 73     70
     7 11      6.5
     8 73     12
     9 11     15
    10 11     70
    # ℹ 64 more rows

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
schedule
```

    # A tibble: 74 × 4
       d         y   Y11   Y73
       <fct> <dbl> <dbl> <dbl>
     1 11     16    16      NA
     2 11      5     5      NA
     3 73     20    NA      20
     4 73     40    NA      40
     5 11     73    73      NA
     6 73     70    NA      70
     7 11      6.5   6.5    NA
     8 73     12    NA      12
     9 11     15    15      NA
    10 11     70    70      NA
    # ℹ 64 more rows

## Impute Schedule using Constant Effect

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
imputed_schedule <- schedule |>
  impute_unobserved(tau = ate_hat)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
schedule
```

    # A tibble: 74 × 4
       d         y   Y11   Y73
       <fct> <dbl> <dbl> <dbl>
     1 11     16    16      NA
     2 11      5     5      NA
     3 73     20    NA      20
     4 73     40    NA      40
     5 11     73    73      NA
     6 73     70    NA      70
     7 11      6.5   6.5    NA
     8 73     12    NA      12
     9 11     15    15      NA
    10 11     70    70      NA
    # ℹ 64 more rows

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
imputed_schedule
```

    # A tibble: 74 × 4
       d         y   Y11   Y73
       <fct> <dbl> <dbl> <dbl>
     1 11     16   16     31.5
     2 11      5    5     20.5
     3 73     20    4.53  20
     4 73     40   24.5   40
     5 11     73   73     88.5
     6 73     70   54.5   70
     7 11      6.5  6.5   22.0
     8 73     12   -3.47  12
     9 11     15   15     30.5
    10 11     70   70     85.5
    # ℹ 64 more rows

## Simulate one experiment

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
set.seed(14363)
sim1 <- imputed_schedule |>
  sim_experiment(reps = 1)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
imputed_schedule
```

    # A tibble: 74 × 4
       d         y   Y11   Y73
       <fct> <dbl> <dbl> <dbl>
     1 11     16   16     31.5
     2 11      5    5     20.5
     3 73     20    4.53  20
     4 73     40   24.5   40
     5 11     73   73     88.5
     6 73     70   54.5   70
     7 11      6.5  6.5   22.0
     8 73     12   -3.47  12
     9 11     15   15     30.5
    10 11     70   70     85.5
    # ℹ 64 more rows

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sim1
```

    # A tibble: 74 × 3
       replicate d         y
           <int> <fct> <dbl>
     1         1 73     31.5
     2         1 11      5
     3         1 73     20
     4         1 11     24.5
     5         1 11     73
     6         1 11     54.5
     7         1 73     22.0
     8         1 73     12
     9         1 73     30.5
    10         1 73     85.5
    # ℹ 64 more rows

## Calculate one ATE estimate

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sim1 |>
  summarize(ate = diff_in_means(y, d))
```

    # A tibble: 1 × 1
        ate
      <dbl>
    1  16.2

Recall our actual ATE estimate:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ate_hat
```

    [1] 15.46992

## Simulate many ATE estimates {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
imputed_schedule |>
  sim_experiment(reps = 5)
```

    # A tibble: 370 × 3
       replicate d         y
           <int> <fct> <dbl>
     1         1 11    16
     2         1 11     5
     3         1 11     4.53
     4         1 73    40
     5         1 11    73
     6         1 11    54.5
     7         1 73    22.0
     8         1 73    12
     9         1 73    30.5
    10         1 11    70
    # ℹ 360 more rows

## Simulate many ATE estimates {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
sim5 <- imputed_schedule |>
  sim_experiment(reps = 5) |>
  group_by(replicate) |>
  summarize(ate = diff_in_means(y, d))
sim5
```

    # A tibble: 5 × 2
      replicate   ate
          <int> <dbl>
    1         1  16.1
    2         2  15.6
    3         3  20.6
    4         4  14.5
    5         5  17.0

## Simulate many ATE estimates {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
sim5 |>
  ggplot(aes(x = ate)) +
  geom_histogram(binwidth = 1) +
  theme_bw() +
  labs(x = "ATE Estimate", y = "Frequency")
```

<figure>

</figure>

## Simulate many more ATE estimates {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
sim5000 <- imputed_schedule |>
  sim_experiment(reps = 5000) |>
  group_by(replicate) |>
  summarize(ate = diff_in_means(y, d))
sim5000
```

    # A tibble: 5,000 × 2
       replicate   ate
           <int> <dbl>
     1         1  8.25
     2         2 10.9
     3         3 13.0
     4         4  9.84
     5         5 22.9
     6         6 11.6
     7         7 24.0
     8         8 14.2
     9         9 15.9
    10        10 10.8
    # ℹ 4,990 more rows

## Simulate many more ATE estimates {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
sim5000 |>
  ggplot(aes(x = ate)) +
  geom_histogram(binwidth = 1) +
  theme_bw() +
  labs(x = "ATE Estimate", y = "Frequency")
```

<figure>

</figure>

## Confidence Interval

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
alpha <- .05
ci <- quantile(sim5000$ate, probs = c(alpha/2, 1 - alpha/2))
ci
```

        2.5%    97.5%
     6.75478 24.21553

---

[← install.packages("remotes")](04-install-packages-remotes.md) · [Up: contents](index.md)
