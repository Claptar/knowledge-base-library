---
title: Data Analysis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/03-power-and-extrapolation/lab.md
source_file: sources/berkeley-stat158/spring-2026/labs/03-power-and-extrapolation/lab.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`labs/03-power-and-extrapolation/lab.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/03-power-and-extrapolation/lab.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

We shall now proceed to analyze some of these questions on two simulated
datasets. The datasets are stored in a `.csv` file. As earlier, use the
`readr` package, which is included inside the `tidyverse`. If you
haven't installed the tidyverse before, you can do so by running
`install.packages("tidyverse")` once.

::: cell
``` {.r .cell-code}
# load tidyverse (includes readr for CSVs)
library(tidyverse)
```
:::

::: cell
``` {.r .cell-code}
# load the data into R

data_randomized <- read_csv("https://stat158.berkeley.edu/spring-2026/data/hormone-risk/hormone_risk_randomized.csv")

data_observations <- read_csv("https://stat158.berkeley.edu/spring-2026/data/hormone-risk/hormone_risk_observational.csv")
```
:::

The dataset contains three major columns: Age Group (50-59/ 60-69/
70-79), Treatment (1/0), and Response (Continuous). The Binary Treatment
here reflects a single form and dosage level of the hormonal supplement,
evaluated against a continuous health outcome indicating cardiovascular
risk. The observational dataset contains an additional baseline health
score variable.

### @. T-tests and Power calculations

First, proceed to conduct t-tests on the whole population and at the
age-group levels using the inbuilt `t.test()` function in `R`. Do this
for both the randomized and observational datasets.

::: cell
``` {.r .cell-code}
# Conduct t-tests
```
:::

Next, investigate what the required sample size for the power of a
t-test would be here for the overall population. Use the observed effect
in the whole population for your calculations. Fill in the rest of the
`power.t.test()` function from `R` below. The data was simulated using
Gaussian distributions, so a t-test is valid in this case.

::: cell
``` {.r .cell-code}
# Calculate Effect Size from Population. Fill in the following:

# overall_mean_diff <- with(# data,
#                           mean(response[treatment==# Fill In]) -
#                             mean(response[treatment==# Fill In]))

# overall_sd <- sd(data$response)

# Check Sample size for 80% Power
power.t.test(
  delta = overall_mean_diff,
  sd = overall_sd,
  sig.level = 0.05,
  power = 0.8,
  type = "two.sample"
)
```
:::

### @. Investigating the Bias

We first subsample randomly from the randomized study to reflect a
smaller RCT. We then perform the usual t-test to see if its significant.
Feel free to change the size of the smaller sample above and below your
previous threshold and see how that changes effects.

::: cell
``` {.r .cell-code}
# Subsampling

small_study_sim <- function(n_sample = 400) {

  sample_data <- data_randomized[sample(1:nrow(data_randomized), n_sample), ]

  # result <- t.test()

  return(result$p.value)
}
```
:::

Now, test how often this subsample turns out to be significant with
`alpha = 0.05`

::: cell
``` {.r .cell-code}
# Run multiple small studies
n_sim <- 1000
p_values <- replicate(n_sim, small_study_sim(400))

mean(p_values < 0.05)
```
:::

We next simulate a method of sampling with bias from the observational
dataset. This is outlined below.

::: cell
``` {.r .cell-code}
# Subsampling with bias

small_biased_sim <- function(n_sample = 400) {

  # Only allow treated women from the top 40% healthiest
  cutoff <- quantile(data_observational$health, 0.60)

  eligible <- with(data_observational,
                   (treatment == "Hormone" & health > cutoff) |
                     (treatment == "Control"))

  pool <- data_observational[eligible, ]

  sample_data <- pool[sample(1:nrow(pool), n_sample), ]

  # result <- t.test(data = sample_data)

  c(
    p = result$p.value,
    effect = as.numeric(result$estimate["mean in group Hormone"] -
                          result$estimate["mean in group Control"])
  )
}
```
:::

Again conduct the t-test with these new subsample. How often are they
significant? And what is the direction?

::: cell
``` {.r .cell-code}
# Run multiple small studies

n_sim <- 1000

results_biased <- replicate(n_sim, small_biased_sim(400))

# Proportion statistically significant
mean(results_biased["p", ] < 0.05)

# Average p-value
mean(results_biased["p", ])

# Proportion with protective effect (negative estimate)
mean(results_biased["effect", ] < 0)
```
:::

### @. Power Dilution with Subgroups

Now, calculate using `power.t.test()` the required sample size for each
age-group and the observed effect size in each group. Assume independent
two-sample t-tests in each age group.

::: cell
``` {.r .cell-code}
# Power calculations

---

[← A Third Study](03-a-third-study.md) · [Up: contents](index.md) · [Lab Part 05 — →](05-lab-part-05.md)
