---
title: calculate ATE-hat for every partition
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html
source_file: sources/berkeley-stat158/spring-2026/05-testing/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# calculate ATE-hat for every partition

**Source:** [`05-testing/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

all_partitions_ATEs <- all_partitions_df |>
  group_by(partition, d_i) |>
  summarize(ybar = mean(y_i)) |>       # average within each group within each partition
  summarize(ATE_hat = diff(ybar)) |>   # take the difference between the two groups mean each partition
  arrange(partition)
```

    `summarise()` has grouped output by 'partition'. You can override using the
    `.groups` argument.

``` {.sourceCode .r .code-with-copy}
all_partitions_ATEs
```

    # A tibble: 20 × 2
       partition ATE_hat
       <ord>       <dbl>
     1 1            2
     2 2            1.33
     3 3            1.33
     4 4            4.67
     5 5           -1.33
     6 6           -1.33
     7 7            2
     8 8           -2
     9 9            1.33
    10 10           1.33
    11 11          -1.33
    12 12          -1.33
    13 13           2
    14 14          -2
    15 15           1.33
    16 16           1.33
    17 17          -4.67
    18 18          -1.33
    19 19          -1.33
    20 20          -2

## Visualize the Sampling Distribution under the null {.anchored anchor-id="visualize-the-sampling-distribution-under-the-null"}

``` {.sourceCode .r .code-with-copy}
ggplot(all_partitions_ATEs, aes(x = ATE_hat)) +
  geom_dotplot() +
  geom_vline(xintercept = ATE_obs, color = "tomato")
```

    Bin width defaults to 1/30 of the range of the data. Pick better value with
    `binwidth`.

<figure class="figure">
<p><img src="code_files/figure-html/unnamed-chunk-16-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

## Calculate p-value {.anchored anchor-id="calculate-p-value"}

``` {.sourceCode .r .code-with-copy}
mean(abs(all_partitions_ATEs$ATE_hat) > ATE_obs)
```

    [1] 0.1

## A function for a Randomization Test {.anchored anchor-id="a-function-for-a-randomization-test"}

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

Here’s a demonstation of how this version works. The order of the elements in `d_i` do not matter but the total number and type do: they illustrate the size of the different groups.

``` {.sourceCode .r .code-with-copy}
stats <- rand_stats(schedule = my_null_sched, d_i = c(0, 0, 0, 1, 1, 1))
```

Compare p-values.

``` {.sourceCode .r .code-with-copy}
mean(abs(stats) > ATE_obs)
```

    [1] 0.081

---

[← add the unique permutations as a new column and find yi, the observed responses](06-add-the-unique-permutations-as-a-new-column-and-find-yi-the.md) · [Up: contents](index.md)
