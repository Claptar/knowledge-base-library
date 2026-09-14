---
title: 1 Hypothesis Testing {.anchored number="1" anchor-id="hypothesis-testing"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hypothesis-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Hypothesis Testing {.anchored number="1" anchor-id="hypothesis-testing"}

**Source:** [`units/reader/hypothesis-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assume we have a larger model <span class="math inline">\$\\cP = \\{P\_\\theta: \\theta \\in \\Theta\\}\$</span> (which, as usual, may be “nonparametric” if <span class="math inline">\$\\theta\$</span> is an infinite-dimensional object like a density), and two competing hypotheses about where <span class="math inline">\$\\theta\$</span> lies:

- Null hypothesis: <span class="math inline">\$H\_0: \\theta \\in \\Theta\_0\$</span>

- Alternative hypothesis: <span class="math inline">\$H\_1: \\theta \\in \\Theta\_1\$</span>

These hypotheses should be *disjoint*, meaning <span class="math inline">\$\\Theta\_0 \\cap \\Theta\_1 = \\emptyset\$</span>, and *exhaustive*, meaning <span class="math inline">\$\\Theta\_0 \\cup \\Theta\_1 = \\Theta\$</span>. Sometimes <span class="math inline">\$\\Theta\_0\$</span> is specified and <span class="math inline">\$\\Theta\_1\$</span> is left unspecified; in that case you can assume <span class="math inline">\$\\Theta\_1 = \\Theta \\setminus \\Theta\_0\$</span>.

A few examples to have in mind:

**Example 1 (Gaussian summary statistic, a.k.a. <span class="math inline">\$Z\$</span>-test):** We observe <span class="math inline">\$Z \\sim N(\\theta,1)\$</span> (which is commonly a summary statistic <span class="math inline">\$Z(X)\$</span> from a large data set) and we want to draw an inference about <span class="math inline">\$\\theta\$</span>. Two common hypothesis testing settings are the *one-sided* hypotheses <span class="math inline">\$H\_0:\\; \\theta \\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta &gt; \\theta\_0\$</span> and the *two-sided* hypotheses <span class="math inline">\$H\_0:\\; \\theta = \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta \\neq \\theta\_0\$</span>.

**Example 2 (Two-sample nonparametric testing):** We observe two samples, <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid P\$</span> and <span class="math inline">\$Y\_1,\\ldots,Y\_m \\simiid Q\$</span>, independently of each other. Without making any further assumptions about <span class="math inline">\$P\$</span> and <span class="math inline">\$Q\$</span>, we want to test the *nonparametric* hypotheses <span class="math inline">\$H\_0:\\; P = Q\$</span> vs <span class="math inline">\$H\_1:\\; P \\neq Q\$</span>.

A hypothesis is called *simple* if it fully specifies the data distribution, and *composite* otherwise. In the examples above, the point null hypothesis <span class="math inline">\$H\_0:\\; \\theta = \\theta\_0\$</span> is a simple hypothesis, and the other five are composite.

We’d like to use the data <span class="math inline">\$X\\sim P\_\\theta\$</span> to determine which of <span class="math inline">\$H\_0\$</span> or <span class="math inline">\$H\_1\$</span> is true, but if a statistician has been called in then this is usually not possible through pure deductive reasoning. For example, if the distributions <span class="math inline">\$P\_\\theta\$</span> all have the same support, then any data set <span class="math inline">\$X\$</span> we see is logically consistent with any value of <span class="math inline">\$\\theta\$</span> in the parameter space.

As usual, we have two options to get around this problem: we can beg the question (the Bayesian approach) or change the subject (the frequentist approach). The Bayesian answer to this problem is clean and simple: just calculate the posterior probabilities <span class="math inline">\$\\Lambda(\\Theta\_0 \\mid X) = \\PP(\\theta \\in \\Theta\_0 \\mid X)\$</span> and <span class="math inline">\$\\Lambda(\\Theta\_1 \\mid X) = \\PP(\\theta \\in \\Theta\_1 \\mid X)\$</span>.

But there are a variety of settings where this is regarded as unappealing: scientists, drug companies, and others often work very hard to design carefully controlled experiments where the only stochastic assumptions made are ones that very few people would disagree with, and we’d like to be able to analyze the data from those experiments without having to layer on any further assumptions.

The frequentist approach to this conundrum is to replace *inductive reasoning* with *inductive behavior*: we will come up with a decision rule to decide between the two hypotheses based on the data. Formally, we can say we will either

1.  Reject <span class="math inline">\$H\_0\$</span> (conclude that <span class="math inline">\$H\_0\$</span> is implausible and <span class="math inline">\$H\_1\$</span> must be true), or

2.  Accept <span class="math inline">\$H\_0\$</span> (go on believing <span class="math inline">\$H\_0\$</span>).

There is a basic asymmetry here in that <span class="math inline">\$H\_0\$</span> is privileged as the default choice to be disconfirmed, or else corroborated. An analogy is often drawn to a criminal trial where the defendant is innocent until proven guilty.

In reality, of course, our credence in the null (or alternative) hypothesis should be continuous in the evidence that we observe; it would be ridiculous to flip from 100% belief in the null to 100% belief in the alternative just at the point where a normal random variable crosses some threshold. But there are real-world situations in which a dichotomous decision must be made. For example, should the FDA approve a drug, or not? Or, do we need to control for some variable in our experimental setup, or not? Still, it is helpful to retain some critical distance from the conceit that we are ever really dichotomously “rejecting” or “accepting” either hypothesis in an epistemic sense.

In many settings where hypothesis testing is applied, including the examples of two-sided <span class="math inline">\$Z\$</span>-testing and two-sample nonparametric testing above, there will always be points in the alternative hypothesis that explain the data even better than the null hypothesis does. As a result, even if we accept the conceit of making a dichotomous decision about what to “conclude,” it is implausible that we would ever “accept” <span class="math inline">\$H\_0\$</span> in the sense of regarding <span class="math inline">\$H\_1\$</span> as disconfirmed, even in an approximate sense. As a result, it is usually preferable to say that we “fail to reject <span class="math inline">\$H\_0\$</span>” rather than saying we accept it. Though we will continue to use “accept” as a technical term in what follows, “fail to reject” has less risk of inadvertently misleading non-statisticians.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 The critical function {.anchored number="2" anchor-id="the-critical-function"} →](03-2-the-critical-function-anchored-number-2-anchor-id-the-crit.md)
