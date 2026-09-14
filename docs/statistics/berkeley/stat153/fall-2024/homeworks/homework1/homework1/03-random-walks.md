---
title: Random walks
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework1/homework1.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Random walks

**Source:** [`homeworks/homework1/homework1.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

4. (2 pts)
Let $x_t$, $t = 1,2,3,\dots$ be a random walk with drift:
$$
x_t = \delta + x_{t-1} + w_t,
$$
where (say) $w_t \sim N(0,\sigma^2)$ for $t = 1,2,3,\dots$. Recall from lecture
that this is not stationary. Prove that $\rho(t-1,t) = \sqrt{\frac{t-1}{t}}$.
What does this approach as $t \to \infty$ and what is the interpretation of this
result?

5. (3 pts)
Suppose that both $\delta$ and $\sigma^2$ are unknown. Devise a test statistic
for the null hypothesis that $\delta = 0$ in the random walk model from Q4. This
should be based on a standard test that you know (have learned in a past course)
for testing whether the mean of Gaussian is zero, with unknown variance, based
on i.i.d.\ samples from this Gaussian.

    State what the null distribution is for this test statistic, and how you
would compute it in R (a function name is sufficient if the test statistic is
implemented as a function in base R). Hint: consider taking differences along
the sequence ... after that, what you want sounds like "c-test", or "p-test",
or "$\phi$-test", or ...

6. (2 pts)
Simulate a random walk of length 200 *without* drift, i.e., $\delta = 0$, and
compute the test statistic you devised in Q5 and report its value. Then repeat,
but using a large nonzero value $\delta$.

7. (4 pts)
Simulate 50 random walks each of length 200, with nonzero drift, and plot them
on the same plot using transparent coloring, following the code used in the
lecture notes from week 2 ("Measures of dependence and stationarity"). Calculate
the sample mean $\hat\mu_t$ at each time $t$, across the repetitions, and plot
as a dark line on the same plot. Then, calculate the sample standard deviation
$\hat\sigma_t$ at each time $t$, and plot the mean plus or minus one standard
deviation: $\hat\mu_t \pm \hat\sigma_t$, as dark dotted lines on the same plot.
Describe what you see (you should see that both the mean and variance increase
over time).

---

[← Correlation and independence](02-correlation-and-independence.md) · [Up: contents](index.md) · [Stationarity →](04-stationarity.md)
