---
title: Statistical models {.anchored anchor-id="statistical-models"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Statistical models {.anchored anchor-id="statistical-models"}

**Source:** [`units/reader/estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Until now, we have been discussing the topic of *probability*. Roughly speaking, in probability we fully specify the distribution of some random variables, and then ask what we can say about the distribution. For example, given a complete description of the rules for generating a random walk, we might ask how long, in expectation, it will take to reach a certain threshold. This is an essentially *deductive* exercise: while the mathematics might be very hard, the questions we ask generally have unambiguous answers.

In statistics, we do essentially the opposite: beginning with the *data* — the Latin word for “given” — we work backwards to draw inferences about the data-generating distribution. This is an *inductive* exercise, for which the answers will inevitably be more ambiguous.

We will generally use the letter <span class="math inline">\$X\$</span> to denote the full data set, which we assume is drawn randomly from some unknown distribution <span class="math inline">\$P\$</span> over the *sample space* <span class="math inline">\$\\cX\$</span>. Let <span class="math inline">\$\\cP\$</span> denote a family of candidate probability distributions, called the *statistical model*. We assume the analyst knows that one of the elements of <span class="math inline">\$\\cP\$</span> is the true data-generating distribution <span class="math inline">\$P\$</span>, but does not know which one. The set <span class="math inline">\$\\cX\$</span> in which <span class="math inline">\$X\$</span> is

**Example (Binomial):** As a simple example, we can imagine an analyst who flips a biased coin <span class="math inline">\$n\$</span> times, getting <span class="math inline">\$X\$</span> heads and <span class="math inline">\$n-X\$</span> tails. If we assume the successive flips are independent, and each has a common probability <span class="math inline">\$\\theta\$</span> of landing heads, we can write the model as

<span class="math display">\\$$ X \\sim \\text{Binom}(n, \\theta), \\quad \\text{ for some } \\theta \\in \[0,1$$. \\\]</span>

Formally, we could say the family of distributions is <span class="math inline">\$\\cP = \\{\\text{Binom}(n, \\theta):\\; \\theta \\in $$0,1$$\\}\$</span>, a set of distributions indexed by the real parameter <span class="math inline">\$\\theta\$</span>.

Note that in the previous example, the integer <span class="math inline">\$n\$</span> is another important variable in the problem, but we implicitly assumed that it was “known” by the analyst, meaning that it is the same for all <span class="math inline">\$P \\in \\cP\$</span>. The parameter <span class="math inline">\$\\theta\$</span>, by contrast, is termed “unknown” in the sense that it varies over the family <span class="math inline">\$\\cP\$</span>.

### Parametric vs nonparametric models {.anchored anchor-id="parametric-vs-nonparametric-models"}

Many of the models we will consider in this class are *parametric*, typically meaning that they are indexed by finitely many real parameters. That is, we have <span class="math inline">\$\\cP = \\{P\_\\theta:\\; \\theta \\in \\Theta\\}\$</span>, typically for some *parameter space* <span class="math inline">\$\\Theta \\subseteq \\RR^d\$</span>. Then <span class="math inline">\$\\theta\$</span> is called the *parameter* or *parameter vector*.

In other models, there is no natural way to index <span class="math inline">\$\\cP\$</span> using <span class="math inline">\$d\$</span> real numbers. We call these *nonparametric* models. Sometimes excited authors referred to their methods as “assumption-free,” but essentially all nonparametric models still make some assumptions about the data distribution. For example, we might assume independence between multiple observations, or shape constraints such as unimodality.

**Example (Nonparameric model):** Suppose we observe an i.i.d. sample of size <span class="math inline">\$n\$</span> from a distribution <span class="math inline">\$P\$</span> on the real line. Even if we do not want to assume anything about <span class="math inline">\$P\$</span>, the i.i.d. assumption will play an important role in the analysis. We might write this model as

<span class="math display">\\$$ X\_1,\\ldots,X\_n \\simiid P, \\quad \\text{ for some distribution } P \\text{ on } \\RR. \\$$</span>

Formally, if <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span>, we can write the family as <span class="math inline">\$\\cP = \\{P^n:\\; P \\text{ is a distribution on } \\RR\\}\$</span>, where <span class="math inline">\$P^n\$</span> represents the <span class="math inline">\$n\$</span>-fold product of <span class="math inline">\$P\$</span> on <span class="math inline">\$\\RR^n\$</span>.

**Notation:** Much of what we will learn in this course applies to parametric and nonparametric models alike, and indeed there is no crisp demarcation between parametric and nonparametric models in practice. It will often be convenient to use notation <span class="math inline">\$\\cP = \\{P\_\\theta :\\; \\theta \\in \\Theta\\}\$</span>, without specifying what kind of set <span class="math inline">\$\\Theta\$</span> is; in particular there is nothing to stop <span class="math inline">\$\\theta\$</span> from being an infinite-dimensional object such as a density function. We can work in this notation without any loss of generality, since we could always take <span class="math inline">\$\\theta = P\$</span> and <span class="math inline">\$\\Theta = \\cP\$</span>.

### Bayesian vs Frequentist inference {.anchored anchor-id="bayesian-vs-frequentist-inference"}

Thus far we have assumed the data <span class="math inline">\$X\$</span> follows a distribution <span class="math inline">\$P\_\\theta\$</span>, for some unknown parameter <span class="math inline">\$\\theta\$</span> which can be any arbitrary member of the set <span class="math inline">\$\\Theta\$</span>. In some contexts we will introduce an additional assumption we can call the *Bayesian assumption*: that <span class="math inline">\$\\theta\$</span> is itself random, drawn from some known distribution <span class="math inline">\$\\Lambda\$</span> that we call the *prior*.

A major advantage of this assumption is that it reduces the problem of inference about <span class="math inline">\$\\theta\$</span> to simply calculating the conditional distribution of <span class="math inline">\$\\theta\$</span> given <span class="math inline">\$X\$</span>.

The philosophical ramifications of this assumption, as well as its practical advantages and disadvantages, will be a major theme later in the course, but for now we will simply say it is an assumption we are sometimes, but not always, willing to make. From a mathematical perspective, it makes no more or less sense to assume <span class="math inline">\$\\theta\$</span> is random than it does to assume <span class="math inline">\$\\theta\$</span> is fixed and unknown.

For the remainder of this lecture, and until our unit on Bayesian inference, we will refrain from making this assumption, instead regarding <span class="math inline">\$\\theta\$</span> as taking an arbitrary fixed value in <span class="math inline">\$\\Theta\$</span>.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Estimation in statistical models {.anchored anchor-id="estimation-in-statistical-models"} →](03-estimation-in-statistical-models-anchored-anchor-id-estimati.md)
