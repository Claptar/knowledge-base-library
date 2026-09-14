---
title: Part c.
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md
source_file: sources/berkeley-stat158/spring-2026/problem-sets/ps5.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Part c.

**Source:** [`problem-sets/ps5.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

$$
\frac{\text{Var}(\hat{\tau}_{CRD})}{\text{Var}(\hat{\tau}_{CO})} = \frac{2(\sigma_s^2 + \sigma_\varepsilon^2)/n}{\sigma_\varepsilon^2/n} = \frac{2(\sigma_s^2 + \sigma_\varepsilon^2)}{\sigma_\varepsilon^2} = 2\left(1 + \frac{\sigma_s^2}{\sigma_\varepsilon^2}\right)
$$

The crossover design is most advantageous when $\sigma_s^2 / \sigma_\varepsilon^2$ is large — that is, when between-subject variability dominates within-subject variability. This is common in biomedical studies: for instance, when measuring blood pressure response to a drug, baseline blood pressure varies enormously between people but the same person's response to a drug across two occasions (the within-subject error) is relatively stable. In such settings, the crossover can be dramatically more efficient than a CRD.

::: -->



4.  **Sequential Probability Ratio Test: Tinkering with Parameters**.
    The SPRT is a powerful tool, but its performance depends on the
    choice of parameters. In this exercise, we will explore how changing
    the parameters $p_0$, $p_1$, $\alpha$, and $\beta$ affects the
    behavior of the test that was shown in class[^1].

    a.  Using the same simulation of a single run that was shown in
        class, lower both the error rates ($\alpha$ and $\beta$) to
        represent a more stringent test. Plot the same simulated run
        with the new thresholds. How does the decision process change
        with the new thresholds? Does it take more or fewer samples to
        reach a decision?

    b.  Choose a fixed value for $p_0$ (e.g., 0.5) and vary $p_1$ (e.g.,
        0.6, 0.7, 0.8). For each value of $p_1$, use a full simulation
        to calculate the expected number of samples needed to reach a
        decision under both hypotheses.

    c.  Now, fix $p_1$ (e.g., 0.7) and vary $p_0$ (e.g., 0.5, 0.4, 0.3).
        Again, calculate the expected number of samples needed for each
        scenario.

    d.  Summarize your findings. How do the choices of $p_0$ and $p_1$
        affect the efficiency of the SPRT? What trade-offs do you
        observe when adjusting the error rates $\alpha$ and $\beta$?



5.  **Adaptive Assignment: Implementing UCB**. A pharmaceutical company
    is running a clinical trial comparing two pain relief drugs. Each
    patient reports a pain relief score on a continuous scale from 0 to
    1 (higher is better). The company wants to use an adaptive
    assignment strategy that balances learning which drug is better with
    assigning more patients to the better-performing drug.

    The following code generates potential outcomes for $N = 30$
    subjects under both treatments.

    ::: cell
    ``` {.r .cell-code}
    library(tidyverse)
    set.seed(42)
    N <- 30
    po <- tibble(
      subject = 1:N,
      Y_A = rbeta(N, 4, 6),
      Y_B = rbeta(N, 5, 5)
    )
    ```
    :::

    Recall the UCB algorithm with Hoeffding's Inequality. The upper
    confidence bound for arm $j$ at time $t$ is:

    $$U_j = \hat{\mu}_j + \sqrt{\frac{\ln(t)}{2\, n_j}}$$

    where $\hat{\mu}_j$ is the sample mean of responses observed so far
    for arm $j$, $n_j$ is the number of subjects assigned to arm $j$ so
    far, and $t$ is the index of the current subject. At each step, the
    algorithm assigns the next subject to the arm with the highest
    $U_j$.

    a.  Write code to implement the UCB algorithm on these potential
        outcomes. Initialize by assigning the first subject to arm A and
        the second to arm B, then use the UCB rule for subjects 3
        through 30[^2]. Store the results in a data frame with columns
        for the subject index, assignment, and observed response.

    <!-- -->

    b.  Create a plot of the cumulative fraction of subjects assigned to
        arm B ($n_B / t$) as a function of the subject index $t$.
        Describe what you see: when is the algorithm exploring
        (assigning roughly evenly) and when is it exploiting (favoring
        one arm)?

    c.  For a single time step of your choosing between $t = 5$ and
        $t = 10$, report the values of $\hat{\mu}_A$, $\hat{\mu}_B$, the
        addition to the mean (aka the Hoeffding bonus), and the
        resulting $U_j$. Verify that the algorithm's assignment matches
        the arm with the higher $U_j$. What role does the bonus term
        play when one arm has been sampled much less than the other?

    d.  Compute the *total regret* of the UCB algorithm on these 30
        subjects and compare it with the expected total regret of a
        balanced completely randomized design that assigns 15 subjects
        to each arm[^3]. The per-subject regret is
        $\max(Y_i(A), Y_i(B)) - Y_i(d_i)$, where $d_i$ is the arm
        actually assigned. Does the UCB algorithm achieve lower total
        regret than what we would expect had we used a balanced CR
        design?

[^1]: See the slides for Sequential Analysis I for code to simulate the
    performance of the SPRT.

[^2]: Start off by simply writing the code to calculate $U_j$ after
    observing the first two subjects, and then assign the third subject
    accordingly. Next, wrap that logic in a loop to handle all subjects
    up to 30.

[^3]: To compute the expected total regret of a balanced CR design, you
    can simulate many random assignments of 15 subjects to each arm,
    compute the total regret for each simulation, and then take the
    average.

---

[← Part b.](03-part-b.md) · [Up: contents](index.md)
