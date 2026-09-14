---
title: Find Sampling Distribution under \$H\0\$
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Find Sampling Distribution under \$H\0\$

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

First let’s load our workhorse function for doing randomization based inference.

``` {.sourceCode .r .code-with-copy}
rand_stats <- function(schedule, d_i, stat = "diff in means", reps = 1000) {

  # store treatment vector separately
  d_i_vec <- d_i

  # replicate the schedule reps times and stack them on top of one another
  randomized_exp_df <- map_dfr(1:reps, ~ schedule, .id = "experiment") |>
    mutate(experiment = factor(experiment, levels = as.character(1:reps), ordered = TRUE),
           d_i = c(replicate(n = reps, sample(d_i_vec))),  # create random assignments
           y_i = Y_1 * d_i +  Y_0 * (1 - d_i)) |>    # find observed responses
    arrange(experiment)

  # calculate test statistic for every random assignment
  if (stat == "diff in means") {
    stats <- randomized_exp_df |>
      group_by(experiment, d_i) |>
      summarize(ybar = mean(y_i),     # average within each group within each experiment
                .groups = "drop_last") |>
      summarize(ATE_hat = diff(ybar),
                .groups = "drop") |>   # take the difference between the two groups mean
      pull()
  } else {
    stop("Statistic not implemented")
  }

  return(stats)
}
```

``` {.sourceCode .r .code-with-copy}
H_0 <- rand_stats(schedule = my_null_sched, d_i = d_i, reps = 5000)
p_val <- mean(abs(H_0) > ATE_obs)

p_val
```

    [1] 0.0222

---

[← “Conduct the experiment”](03-conduct-the-experiment.md) · [Up: contents](index.md) · [Visualizing the threshold →](05-visualizing-the-threshold.md)
