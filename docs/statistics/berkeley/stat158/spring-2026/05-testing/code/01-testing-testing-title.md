---
title: Testing {#testing .title}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html
source_file: sources/berkeley-stat158/spring-2026/05-testing/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Testing {#testing .title}

**Source:** [`05-testing/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Code

Let’s pick up where we left off in calculating our sampling distribution of <span class="math inline">\$\\widehat{ATE}\$</span>.

``` {.sourceCode .r .code-with-copy}
library(tidyverse)
anchor_mini_sched <- tibble(Y_0 = c(15, 15, 19, 2, 10, 8),
                            Y_1 = c(31, 22, 45, 20, 20, 15))

anchor_mini_sched <- anchor_mini_sched |>
    mutate(tau = Y_1 - Y_0)

parameters <- anchor_mini_sched |>
    summarize(Ybar_1 = mean(Y_1),
              Ybar_0 = mean(Y_0),
              ATE = mean(tau))
```

### Calculating the sampling distribution {.anchored anchor-id="calculating-the-sampling-distribution"}

To learn the sampling distribution of <span class="math inline">\$\\widehat{ATE}\$</span>, we need to:

1.  Articulate every possible way to split the six students into two groups of size three.
2.  For each unique partition, calculate <span class="math inline">\$\\widehat{ATE}\$</span>
3.  Calculate the probability of observing each of those values.

To aid in step 1, we can use the `permutations()` function to show every permutation of the a vector containing size elements, three of which indicate the treatment (`1`) and three of which indicate the control (`0`). We can imagine that the indices of this vector correspond to the indices of the students.

``` {.sourceCode .r .code-with-copy}
library(arrangements)
d_x <- c(0, 0, 0, 1, 1, 1)
permmat <- permutations(d_x) |>
  unique()
```

There are many ways to use R to calculate all corresponding <span class="math inline">\$\\widehat{ATE}\$</span>s. I’ll use a method that makes a dataframe for every permutation, stacks them on top of one another, then uses grouped aggregation to calculate the estimates. This method is conceptually clean, however if the number of permutations was in the hundreds or thousands, it would be too RAM-intensive an an interative approach using the `apply()` family would be better.

``` {.sourceCode .r .code-with-copy}

---

[Up: contents](index.md) · [replicate the anchor sched 20 times and stack them on top of one another →](02-replicate-the-anchor-sched-20-times-and-stack-them-on-top-of.md)
