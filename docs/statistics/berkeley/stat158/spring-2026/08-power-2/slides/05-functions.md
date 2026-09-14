---
title: Functions
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Functions

**Source:** [`08-power-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
rejection_region <- function(df, alpha = .05, reps = 1000, seed = 4892) {
  # create observed schedule (with missing data)
  obs_sched <- df |>
    mutate(Y_0 = ifelse(d_i == 0, y_i, NA),
           Y_1 = ifelse(d_i == 1, y_i, NA))

  # impute the missing potential outcomes with fisher sharp null
  null_sched <- obs_sched |>
    mutate(Y_0 = ifelse(is.na(Y_0), Y_1, Y_0),
           Y_1 = ifelse(is.na(Y_1), Y_0, Y_1))

  # simulate from sampling distribution under null
  set.seed(seed)
  H_0 <- rand_stats(schedule = null_sched,
                    d_i = df$d_i,
                    stat = "diff in means",
                    reps = reps)

  # find rejection region
  left_threshold <- quantile(H_0, alpha/2)
  right_threshold <- quantile(H_0, 1 - alpha/2)

  return(list(LT = left_threshold, RT = right_threshold))
}
```

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
HA_tau <- function(df, tau, reps = 1000, seed = 4892) {
  # create observed schedule (with missing data)
  obs_sched <- df |>
    mutate(Y_0 = ifelse(d_i == 0, y_i, NA),
           Y_1 = ifelse(d_i == 1, y_i, NA))

  # impute the missing potential outcomes under particular HA
  alt_sched <- obs_sched |>
    mutate(Y_0 = ifelse(is.na(Y_0), Y_1 - tau, Y_0),
           Y_1 = ifelse(is.na(Y_1), Y_0 + tau, Y_1))

  H_A <- rand_stats(schedule = alt_sched,
                    d_i = df$d_i,
                    stat = "diff in means",
                    reps = reps)

  return(H_A)
}
```

---

[← Power](04-power.md) · [Up: contents](index.md)
