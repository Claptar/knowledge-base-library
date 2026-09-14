---
title: 'Non-parametric Methods: Randomization Tests'
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md
source_file: sources/berkeley-stat158/spring-2026/labs/02-randomization-tests/lab.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Non-parametric Methods: Randomization Tests

**Source:** [`labs/02-randomization-tests/lab.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

6.  We shall first implement this for the larger ManyLabs dataset
    provided. In order to conduct a randomization test, we will be
    working under the Potential Outcomes framework.

**Q:** What assumptions are required by the permutation test? What is
random in this setup?

**A:**\
\
\
\

Modify the dataset to reflect two columns, `Y_1` and `Y_0`, representing
the potential outcomes. Note that this will have missing values.

::: cell
``` {.r .cell-code}
# convert data to potential outcomes
```
:::

As in class, we will be testing the null hypothesis that (some people
call it the **Fisher Sharp Null Hypothesis**)
$$Y_i(1) - Y_i(0) = 0 \text{ for any }i.$$

Under the **Fisher Sharp Null Hypothesis**, impute the missing potential
outcomes.

::: cell
``` {.r .cell-code}
# Fill in the missing values
```
:::

We now implement the randomization test from class. The following
function evaluates the distribution of the test statistic under the null
by repeatedly randomizing who receives treatment.

::: cell
``` {.r .cell-code}
# Randomization distribution

rand_stats <- function(schedule, d_i, stat = "diff in means", reps = 1000) {

  # replicate the schedule reps times and stack them on top of one another
  randomized_exp_df <- map_dfr(1:reps, ~ schedule, .id = "experiment") |>
    mutate(experiment = factor(experiment, levels = as.character(1:reps), ordered = TRUE),
           d_i = c(replicate(n = reps, sample(d_i))),  # create random assignments
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
:::

7.  Fill in your own version of `schedule` and `d_i` based on the
    dataset we are working with. Proceed to then calculate a p-value.
    See the [Stat 158 testing code
    page](https://stat158.berkeley.edu/spring-2026/05-testing/code.html).

::: cell
``` {.r .cell-code}
# Randomization Test

# Fill these in
# my_null_schedule <-

# my_d_i <-

# my_ATE_obs <-

# calculate the test statistic distribution
stats <- rand_stats(schedule = my_null_sched, d_i = my_d_i)

# calculate p-value
mean(abs(stats) > my_ATE_obs)
```
:::

8.  Repeat these steps for your own collected dataset. Convert it to a
    filled-in potential outcomes style table, generate the randomization
    distribution and calculate the p-value.

::: cell
``` {.r .cell-code}
# Repeat on your own data
```
:::

---

[← Statistical tests](05-statistical-tests.md) · [Up: contents](index.md) · [Model-based Inference: The Z-Test →](07-model-based-inference-the-z-test.md)
