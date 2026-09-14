---
title: Conceptual objections to hypothesis testing
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Conceptual objections to hypothesis testing

**Source:** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

It is an uncontroversial view among statisticians that hypothesis tests are often used carelessly, leading to unsound conclusions. More controversially, some statisticians are skeptical that hypothesis tests can ever be a conceptually sound tool for statistical analysis even when they are interpreted correctly. The following objections are commonly heard:

## Objection 1: Point nulls are unrealistic {.anchored anchor-id="objection-1-point-nulls-are-unrealistic"}

Some critics ask why we should ever bother to test <span class="math inline">\$\\theta = 0\$</span>. In practice, they say, no effect size is ever equal to zero, so we learn nothing by using the data to establish that <span class="math inline">\$\\theta \\neq 0\$</span>.

There are at least two good answers to this objection. The most direct answer, at least in parametric problems, is that if we don’t want to test the point null we have plenty of other options, for example:

1.  We can always test a different null, such as <span class="math inline">\$H\_0:\\;\|\\theta\|\\leq \\delta\$</span>, for some value <span class="math inline">\$\\delta&gt;0\$</span>.

2.  We can interpret the two-sided test of <span class="math inline">\$H\_0:\\;\\theta=0\$</span> as two one-sided tests of <span class="math inline">\$H\_0^1:\\;\\theta\\geq 0\$</span> and <span class="math inline">\$H\_0^2:\\;\\theta\\leq 0\$</span>, with Type I errors of <span class="math inline">\$\\alpha\_1\$</span> and <span class="math inline">\$\\alpha\_2\$</span>, respectively. That is, if <span class="math inline">\$T(X)&gt;c\_2\$</span> we can reject <span class="math inline">\$H\_0^2\$</span> and conclude <span class="math inline">\$\\theta&gt;0\$</span>, and if <span class="math inline">\$T(X)&lt;c\_1\$</span> we can reject <span class="math inline">\$H\_0^1\$</span> and conclude <span class="math inline">\$\\theta&lt;0\$</span>. Because <span class="math inline">\$\\alpha\_1+\\alpha\_2=\\alpha\$</span>, the likelihood that either test makes a Type I error – and thus the probability that we make a false claim about the sign of <span class="math inline">\$\\theta\$</span> – is below <span class="math inline">\$\\alpha\$</span>. On this interpretation, we never reject the point null <span class="math inline">\$H\_0\$</span> without learning the sign of <span class="math inline">\$\\theta\$</span>.

3.  We can usually *invert* a test of the point null to obtain a CI for <span class="math inline">\$\\theta\$</span>

The objection to exact nulls can be harder to answer in non-parametric problems, such as in nonparametric two-sample tests that formally test the hypothesis that two distributions <span class="math inline">\$P\$</span> and <span class="math inline">\$Q\$</span> are identical to each other. Depending on what test we use, we may be able to justify drawing a more specific conclusion from a rejection (e.g., that the median of <span class="math inline">\$P\$</span> is greater or less than the median of <span class="math inline">\$Q\$</span>). On the other hand, there may not be other good options for nonparametric analysis of the data; in particular, using Bayesian nonparametric models requires making much stronger assumptions.

## Objection 2: Frequentist methods answer the wrong question {.anchored anchor-id="objection-2-frequentist-methods-answer-the-wrong-question"}

A second objection is that frequentist methods like hypothesis tests are at best a clever evasion of the questions scientists really want to answer, and at worst a deceptive bait and switch. For example, instead of telling scientists what they really want to know, the likelihood that <span class="math inline">\$H\_0\$</span> is true in light of the data, frequentists instead calculate a <span class="math inline">\$p\$</span>-value, which is the probability the data would be as extreme as observed given that the null is true. They implicitly hope scientists don’t dwell too much on the difference between these two probabilities — and then blame the scientists when they can’t keep it straight!

Many practitioners are chronically confused about what confidence intervals mean and don’t mean: any good lesson about CIs (including this one) must include copious warnings about what we *can’t* say about them. Again, this is because what scientists really want to be able to do is calculate a confidence interval and say that the estimand is probably in the interval; but we can only make such a probability statement about a CI *before* we have calculated it (or, having calculated it, we can only make probability statements about the CI in a new experiment)

These objections cannot be dismissed as easily as the first objection; these really are drawbacks of frequentist methods. But Bayesian alternatives have drawbacks of their own, especially that they require the analyst to supply his or her own opinions about every aspect of the problem, including:

1.  The probability that the null is true (which is the very question that we are trying to answer), and

2.  The probability distribution over alternative values (which the frequentist very often does not need to worry about, because they can use a UMP or other canonical choice of test).

One major advantage of hypothesis tests and other frequentist methods that has led to their abiding popularity in scientific data analysis is their versatility and applicability in settings where we wish to be parsimonious with our assumptions.

---

[← (Mis-)Interpreting Hypothesis Tests](04-mis--interpreting-hypothesis-tests.md) · [Up: contents](index.md)
