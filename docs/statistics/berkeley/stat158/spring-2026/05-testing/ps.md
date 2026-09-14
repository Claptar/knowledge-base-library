---
title: Ps
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/ps.html
source_file: sources/berkeley-stat158/spring-2026/05-testing/ps.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Ps

**Source:** [`05-testing/ps.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/ps.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

1.  **Testing Anchoring**. Conduct a hypothesis test that the first question on the Anchoring Experiment had no effect on the guess for the percent of UN Nations that are in Africa. Use <span class="math inline">\$\\alpha = .05\$</span>, consider only the randomness induced by the random assignment to X = 11 or X = 73, use the sharp null hypothesis, use the difference in group means as your statistic, and use a two-tailed test. Approximate the sampling distribution of the test statistic by first creating the schedule of outcomes implied by the null hypothesis, then use the `rand_stats()` function in the code sample from lecture to calculate 1000 test statistics under the null.

    Provide the code that you used, a plot of the sampling distribution (a.k.a. the null distribution), the p-value, and a clearly written interpretation about what this analysis says about our original research question.

    Use the full anchoring data set collected on the first day of class:

    ``` {.sourceCode .r .code-with-copy}
    library(tidyverse)
    anchoring <- read.csv("https://stat158.berkeley.edu/spring-2026/data/anchoring/anchoring.csv")
    ```

---

[Up: contents](../index.md)
