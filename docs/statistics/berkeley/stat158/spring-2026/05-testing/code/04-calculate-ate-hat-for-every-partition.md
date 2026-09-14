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
     2 2           16
     3 3           13.3
     4 4           15.7
     5 5            7
     6 6            4.33
     7 7            6.67
     8 8           18.3
     9 9           20.7
    10 10          18
    11 11          10
    12 12           7.33
    13 13           9.67
    14 14          21.3
    15 15          23.7
    16 16          21
    17 17          12.3
    18 18          14.7
    19 19          12
    20 20          26

### Visualize the distribution of estimates {.anchored anchor-id="visualize-the-distribution-of-estimates"}

``` {.sourceCode .r .code-with-copy}
ggplot(all_partitions_ATEs, aes(x = ATE_hat)) +
  geom_dotplot()
```

    Bin width defaults to 1/30 of the range of the data. Pick better value with
    `binwidth`.

<figure class="figure">
<p><img src="code_files/figure-html/unnamed-chunk-5-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Note that the stacking of the dots doesn’t mean they take the same value. Indeed, each of the 20 possible partitions has a different <span class="math inline">\$\\widehat{ATE}\$</span>.

``` {.sourceCode .r .code-with-copy}
all_partitions_ATEs |>
  distinct(ATE_hat) |>
  nrow()
```

    [1] 20

### Calculate E and V {.anchored anchor-id="calculate-e-and-v"}

First add probabilities (each partition is equally likely):

``` {.sourceCode .r .code-with-copy}
all_partitions_ATEs <- all_partitions_ATEs |>
  mutate(prob = 1 / n())
all_partitions_ATEs
```

    # A tibble: 20 × 3
       partition ATE_hat  prob
       <ord>       <dbl> <dbl>
     1 1            2     0.05
     2 2           16     0.05
     3 3           13.3   0.05
     4 4           15.7   0.05
     5 5            7     0.05
     6 6            4.33  0.05
     7 7            6.67  0.05
     8 8           18.3   0.05
     9 9           20.7   0.05
    10 10          18     0.05
    11 11          10     0.05
    12 12           7.33  0.05
    13 13           9.67  0.05
    14 14          21.3   0.05
    15 15          23.7   0.05
    16 16          21     0.05
    17 17          12.3   0.05
    18 18          14.7   0.05
    19 19          12     0.05
    20 20          26     0.05

Then calculate Expected Value.

``` {.sourceCode .r .code-with-copy}
expected_value <- sum(all_partitions_ATEs$ATE_hat * all_partitions_ATEs$prob)
expected_value
```

    [1] 14

Note that this is the same as the value of the parameter, <span class="math inline">\$ATE\$</span>, demonstrated the unbiasedness of this estimator.

Next calculate Variance.

``` {.sourceCode .r .code-with-copy}
var <- sum((all_partitions_ATEs$ATE_hat - expected_value)^2 * all_partitions_ATEs$prob)
var
```

    [1] 42.66667

## Testing {#testing-1 .anchored anchor-id="testing"}

``` {.sourceCode .r .code-with-copy}
my_experiment <- all_partitions_df |>
  filter(partition == "1")
my_experiment
```

    # A tibble: 6 × 6
      partition   Y_0   Y_1   tau   d_i   y_i
      <ord>     <dbl> <dbl> <dbl> <dbl> <dbl>
    1 1            15    31    16     0    15
    2 1            15    22     7     0    15
    3 1            19    45    26     0    19
    4 1             2    20    18     1    20
    5 1            10    20    10     1    20
    6 1             8    15     7     1    15

``` {.sourceCode .r .code-with-copy}
my_experiment <- my_experiment |>
  select(d_i, y_i)
my_experiment
```

    # A tibble: 6 × 2
        d_i   y_i
      <dbl> <dbl>
    1     0    15
    2     0    15
    3     0    19
    4     1    20
    5     1    20
    6     1    15

Calculate observed test statistic:

``` {.sourceCode .r .code-with-copy}
ATE_obs <- my_experiment |>
  group_by(d_i) |>
  summarize(Ybar = mean(y_i)) |>
  summarize(ATEhat = diff(Ybar)) |>
  pull()
ATE_obs
```

    [1] 2

## Make schedule under sharp null {.anchored anchor-id="make-schedule-under-sharp-null"}

``` {.sourceCode .r .code-with-copy}
my_null_sched <- my_experiment |>
  mutate(Y_0 = y_i,
         Y_1 = y_i) |>
  select(Y_0, Y_1)
my_null_sched
```

    # A tibble: 6 × 2
        Y_0   Y_1
      <dbl> <dbl>
    1    15    15
    2    15    15
    3    19    19
    4    20    20
    5    20    20
    6    15    15

## Turn the Sampling Crank… {.anchored anchor-id="turn-the-sampling-crank"}

``` {.sourceCode .r .code-with-copy}

---

[← add the unique permutations as a new column and find yi, the observed responses](03-add-the-unique-permutations-as-a-new-column-and-find-yi-the.md) · [Up: contents](index.md) · [replicate the anchor sched 20 times and stack them on top of one another →](05-replicate-the-anchor-sched-20-times-and-stack-them-on-top-of.md)
