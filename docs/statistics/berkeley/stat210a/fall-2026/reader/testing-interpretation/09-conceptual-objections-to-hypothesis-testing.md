---
title: Conceptual objections to hypothesis testing
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conceptual objections to hypothesis testing

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

It is an uncontroversial view among statisticians that hypothesis tests are often used carelessly, leading to unsound conclusions.  More controversially, some statisticians are skeptical that hypothesis tests can ever be a conceptually sound tool for statistical analysis even when they are interpreted correctly. The following objections are commonly heard:

## Objection 1: Point nulls are unrealistic

Some critics ask why we should ever bother to test $\theta = 0$. In practice, they say, no effect size is ever equal to zero, so we learn nothing by using the data to establish that $\theta \neq 0$.

There are at least two good answers to this objection. The most direct answer, at least in parametric problems, is that if we don't want to test the point null we have plenty of other options, for example:

1. We can always test a different null, such as $H_0:\;|\theta|\leq \delta$, for some value $\delta>0$.

2. We can interpret the two-sided test of $H_0:\;\theta=0$ as two one-sided tests of $H_0^1:\;\theta\geq 0$ and $H_0^2:\;\theta\leq 0$, with Type I errors of $\alpha_1$ and $\alpha_2$, respectively. That is, if $T(X)>c_2$ we can reject $H_0^2$ and conclude $\theta>0$, and if $T(X)<c_1$ we can reject $H_0^1$ and conclude $\theta<0$. Because $\alpha_1+\alpha_2=\alpha$, the likelihood that either test makes a Type I error -- and thus the probability that we make a false claim about the sign of $\theta$ -- is below $\alpha$. On this interpretation, we never reject the point null $H_0$ without learning the sign of $\theta$.

3. We can usually *invert* a test of the point null to obtain a CI for $\theta$

The objection to exact nulls can be harder to answer in non-parametric problems, such as in nonparametric two-sample tests that formally test the hypothesis that two distributions $P$ and $Q$ are identical to each other. Depending on what test we use, we may be able to justify drawing a more specific conclusion from a rejection (e.g., that the median of $P$ is greater or less than the median of $Q$). On the other hand, there may not be other good options for nonparametric analysis of the data; in particular, using Bayesian nonparametric models requires making much stronger assumptions.

## Objection 2: Frequentist methods answer the wrong question

A second objection is that frequentist methods like hypothesis tests are at best a clever evasion of the questions scientists really want to answer, and at worst a deceptive bait and switch. For example, instead of telling scientists what they really want to know, the likelihood that $H_0$ is true in light of the data, frequentists instead calculate a $p$-value, which is the probability the data would be as extreme as observed given that the null is true. They implicitly hope scientists don't dwell too much on the difference between these two probabilities --- and then blame the scientists when they can't keep it straight!

Many practitioners are chronically confused about what confidence intervals mean and don't mean: any good lesson about CIs (including this one) must include copious warnings about what we *can't* say about them. Again, this is because what scientists really want to be able to do is calculate a confidence interval and say that the estimand is probably in the interval; but we can only make such a probability statement about a CI *before* we have calculated it (or, having calculated it, we can only make probability statements about the CI in a new experiment)

These objections cannot be dismissed as easily as the first objection; these really are drawbacks of frequentist methods. But Bayesian alternatives have drawbacks of their own, especially that they require the analyst to supply his or her own opinions about every aspect of the problem, including:

1. The probability that the null is true (which is the very question that we are trying to answer), and

2. The probability distribution over alternative values (which the frequentist very often does not need to worry about, because they can use a UMP or other canonical choice of test).

One major advantage of hypothesis tests and other frequentist methods that has led to their abiding popularity in scientific data analysis is their versatility and applicability in settings where we wish to be parsimonious with our assumptions.

---

[← (Mis-)Interpreting Hypothesis Tests](08-mis--interpreting-hypothesis-tests.md) · [Up: contents](index.md)
