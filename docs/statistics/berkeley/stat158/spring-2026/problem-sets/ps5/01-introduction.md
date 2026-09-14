---
title: Introduction
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md
source_file: sources/berkeley-stat158/spring-2026/problem-sets/ps5.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`problem-sets/ps5.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

1.  **Question Format and Score: Crossover Design**. Three weeks ago you
    took your midterm exam. Unbeknownst to you, the exam was also
    serving as a crossover experiment. There were four versions (A, B,
    C, D) where versions A/C shared one structure and versions B/D
    shared another. The treatment of interest was question *format*:
    whether a question was presented as a single compound sentence or as
    separate sentences/bullet points. Questions 21 and 23 each had a
    compound and a separated version; the two structures (A/C vs B/D)
    ensured that if Q21 was compound then Q23 was separated, and vice
    versa.

    Exam versions were randomly assigned to students in blocks by
    session (morning or afternoon).

    a.  What are the experimental units in this study? What are the
        measurement units?
    b.  What is the treatment? How many levels does it have?
    c.  Why is this a crossover design rather than a simple completely
        randomized design? What is the advantage of each student
        receiving both formats?
    d.  What is the blocking factor, and why was blocking used?

<!-- -->

2.  **Coffee and Reaction Time: Crossover Design**. A researcher wants
    to know whether drinking coffee before a cognitive test improves
    reaction time. She recruits 20 subjects and uses a crossover design:
    each subject takes the cognitive test twice, once after drinking
    coffee and once after drinking decaf (a placebo). The order
    (coffee-first vs decaf-first) is randomly assigned, with a one-week
    washout period between sessions.

    a.  What is the primary advantage of this crossover design compared
        to a completely randomized design that assigns 10 subjects to
        coffee and 10 to decaf?
    b.  The researcher is concerned about a *carryover effect*: caffeine
        from the first session might still affect performance in the
        second session even after a week. Explain why it is a threat to
        this crossover design.
    c.  If carryover effects are present and asymmetric (i.e., the
        carryover from coffee to decaf is different from the carryover
        from decaf to coffee), explain why the crossover estimator
        $\bar{Z}$ (the average of the observed differences) from the
        previous problem would be biased.
    d.  One way to test for carryover is to compare the *total* response
        (session 1 + session 2) between the two sequence groups. Explain
        the logic behind this test: under no carryover, why should the
        sequence groups have the same expected total?

<!-- -->

3.  **Coffee and Reaction Time: Analysis**. The researcher from the
    previous problem ran her crossover experiment and collected data.
    You can generate a synthetic version of her dataset with the
    following code.

    ::: cell
    ``` {.r .cell-code}
    library(tidyverse)
    set.seed(40)
    n <- 20
    coffee <- tibble(
        subject  = 1:n,
        sequence = rep(c("coffee_first", "decaf_first"), each = n / 2),
        subject_ability = rnorm(n, mean = 250, sd = 30)
    ) |>
        mutate(
            period1 = case_when(
                sequence == "coffee_first" ~ subject_ability - 8 + rnorm(n, 0, 10),
                sequence == "decaf_first"  ~ subject_ability + rnorm(n, 0, 10)
            ),
            period2 = case_when(
                sequence == "coffee_first" ~ subject_ability + 5 + rnorm(n, 0, 10),
                sequence == "decaf_first"  ~ subject_ability - 8 + 5 + rnorm(n, 0, 10)
            )
        ) |>
        select(subject, sequence, period1, period2)
    ```
    :::

    Here, `period1` and `period2` are reaction times (in milliseconds)
    on the cognitive test in session 1 and session 2 respectively. We'll
    denote these $Y_{i1}$ and $Y_{i2}$ for subject $i$. Lower is better.
    The data-generating process includes a true treatment effect of
    coffee (coffee lowers reaction time by 8 ms) and a period effect
    (reaction time increases by 5 ms in period 2, perhaps due to fatigue
    or reduced novelty). There is no carryover effect.

    a.  For each subject, compute $Z_i$, the within-subject difference
        in reaction time (decaf $-$ coffee). Be careful: which period
        corresponds to the coffee score depends on the subject's
        sequence. Add this column to the data frame and compute
        $\bar{Z}$.

    b.  Conduct a randomization test of the sharp null hypothesis that
        coffee has no effect on any subject's reaction time.

        i.  State the null hypothesis in terms of potential outcomes.
        ii. Simulate 1,000 test statistics under the null by
            re-randomizing the sequence assignment (a complete
            randomization of 10 to each sequence).
        iii. Plot the null distribution with the observed statistic and
             report the two-sided p-value.

    c.  Reshape the data into long format (one row per subject per
        period) and fit a linear model with fixed effects for subject:

        $$Y_{ij} = \beta_0 + \beta_1 \text{treatment}_{ij} + \beta_2 \text{period}_{ij} + \alpha_i + \varepsilon_{ij}$$

        where $\alpha_i$ is a fixed effect for subject $i$. Report and
        interpret $\hat{\beta}_1$. Compare this with the result from the
        randomization test.

    d.  Now fit a simpler model that omits the period effect:
        $Y_{ij} = \beta_0 + \beta_1 \text{treatment}_{ij} + \alpha_i + \varepsilon_{ij}$.
        How does the estimate of the treatment effect change? Explain
        why the crossover design protects the treatment effect estimate
        from period effects even when period is not included in the
        model.

<!--
@. **Why Cross Over?**. Consider an experiment with $N = 2n$ subjects and two treatments. Compare two designs:

    - **Design CRD**: A completely randomized design where $n$ subjects are assigned to treatment $A$ and $n$ to treatment $B$.
    - **Design CO**: A crossover design where each of the $2n$ subjects receives both treatments (in random order).

    Suppose the outcome for subject $i$ under treatment $t$ can be written as $Y_i(t) = \mu_t + s_i + \varepsilon_{it}$, where $s_i \sim N(0, \sigma_s^2)$ is a subject effect and $\varepsilon_{it} \sim N(0, \sigma_\varepsilon^2)$ is random error, with all terms independent.

    a. Under Design CRD, show that $\text{Var}(\hat{\tau}_{CRD}) = \frac{2(\sigma_s^2 + \sigma_\varepsilon^2)}{n}$.
    b. Under Design CO, each subject provides $Y_i(A) - Y_i(B) = \tau + (\varepsilon_{iA} - \varepsilon_{iB})$. Show that $\text{Var}(\hat{\tau}_{CO}) = \frac{2\sigma_\varepsilon^2}{2n} = \frac{\sigma_\varepsilon^2}{n}$.
    c. Compute the ratio $\text{Var}(\hat{\tau}_{CRD}) / \text{Var}(\hat{\tau}_{CO})$. Under what conditions on $\sigma_s^2$ and $\sigma_\varepsilon^2$ is the crossover design most advantageous? Give a real-world example where you'd expect this condition to hold strongly.

:::{.content-hidden unless-meta="solutions"}

---

[Up: contents](index.md) · [Part a. →](02-part-a.md)
