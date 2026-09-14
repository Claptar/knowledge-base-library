---
title: Estimation in statistical models
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Estimation in statistical models

**Source:** [`reader/estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Having observed <span class="math inline">\$X \\sim P\_\\theta\$</span>, an unknown distribution in the model <span class="math inline">\$\\cP = \\{P\_\\theta:\\; \\theta \\in \\Theta\\}\$</span>, we will be interested in learning something about <span class="math inline">\$\\theta\$</span>. In *estimation*, we guess the value of some quantity of interest <span class="math inline">\$g(\\theta)\$</span>, called the *estimand*. Our guess is called the *estimate* <span class="math inline">\$\\delta(X)\$</span>, calculated based on the data. The method <span class="math inline">\$\\delta(\\cdot)\$</span> that we use to calculate the estimate is called the *estimator*.

**Example (Binomial, continued):** We return to our binomial example from above, substituting the more prosaic outcomes “heads” and “tails” for the “same-side up” and “different-side up” outcomes we were discussing before, We may want to estimate <span class="math inline">\$g(\\theta) = \\theta\$</span>, the probability of the coin landing heads. A natural estimator is <span class="math inline">\$\\delta\_0(X) = X/n\$</span>, the fraction of coins landing heads in any given trial. One favorable property of this estimator is that it is *unbiased*, meaning that <span class="math inline">\$\\EE\_\\theta \\delta\_0(X) = g(\\theta)\$</span>, for all <span class="math inline">\$\\theta \\in \\Theta\$</span>.

There are many potential estimators for any given problem, so our goal will generally be to find a good estimator. To evaluate and compare estimators, we must have a way of evaluating how successful an estimator is in any given realization of the data. To this end we introduce the *loss function* <span class="math inline">\$L(\\theta, d)\$</span>, which measures *how bad* it is to guess that <span class="math inline">\$g(\\theta) = d\$</span> when <span class="math inline">\$\\theta\$</span> is the true parameter value. Typically loss functions are non-negative, with <span class="math inline">\$L(\\theta, d) = 0\$</span> if and only if <span class="math inline">\$g(\\theta) = d\$</span> (no loss from a perfect guess) but this is not required.

In any given problem, we should ideally choose the loss that best measures our own true (dis)utility function, but in practice people fall back on simple defaults. One loss function that is especially popular for its mathematical convenience is the *squared-error loss*, defined by <span class="math inline">\$L(\\theta, d) = (d-g(\\theta))^2\$</span>.

Whereas the loss function measures how (un)successful an estimator is in one realization of the data, we would really like to evaluate an estimator’s performance over the whole range of possible data sets <span class="math inline">\$X\$</span> that we might observe. This is measured by the *risk function*, defined as

<span class="math display">\\$$ R(\\theta; \\delta(\\cdot)) = \\EE\_\\theta \[\\, L(\\theta, \\delta(X)) \\,$$ = \\int L(\\theta, \\delta(x)) \\td P\_\\theta(x) \\\]</span>

**Remark on notation:** The subscript in the previous expression tells us *which* of our candidate probability distributions to use in evaluating the expectation. In some other fields, people may use the subscript to indicate “what randomness to integrate over,” with the implication that any random variable that does not appear in the subscript should be held fixed. In our course, it should generally be assumed that any expectation or probability is integrating over the joint distribution of the entire data set; if we want to hold something fixed we will condition on it. Recall that, for now, the parameter <span class="math inline">\$\\theta\$</span> is fixed unless otherwise specified.

The semicolon in the risk function is meant to indicate we are viewing it primarily as a function of <span class="math inline">\$\\theta\$</span>. That is, we should think of and estimator <span class="math inline">\$\\delta\$</span> as having a risk function <span class="math inline">\$R(\\theta)\$</span>, and the second input in <span class="math inline">\$R(\\theta; \\delta)\$</span> is telling us which estimator’s risk function to evaluate at <span class="math inline">\$\\theta\$</span>.

The risk for the squared-error loss is called the *mean squared error* (MSE):

<span class="math display">\\$$ \\textrm{MSE}(\\theta; \\delta) = \\EE\_\\theta\\left\[\\,(\\delta(X) - g(\\theta))^2\\,\\right$$ \\\]</span>

**Example (Binomial, continued):** To calculate the MSE of our estimator <span class="math inline">\$\\delta\_0 = X/n\$</span>, note that <span class="math inline">\$\\EE\_\\theta$$X/n$$ = \\theta\$</span> (the estimator is *unbiased*). As a result, we have

<span class="math display">\\$$ \\begin{aligned} \\textrm{MSE}(\\theta; \\delta\_0) &= \\EE\_\\theta\\left\[ \\left(\\frac{X}{n} - \\theta\\right)^2\\right$$ \\\\$$7pt$$ &= \\text{Var}\_\\theta(X/n)\\\\$$3pt$$ &= \\frac{1}{n}\\theta(1-\\theta) \\end{aligned} \\\]</span>

One reason why we might consider estimators other than <span class="math inline">\$\\delta\_0\$</span> is that, if <span class="math inline">\$n\$</span> is small, our estimate could be quite noisy. As an extreme example, if <span class="math inline">\$n=1\$</span> we will always estimate either <span class="math inline">\$\\theta = 0\$</span> or <span class="math inline">\$\\theta = 1\$</span>, both of which would be extreme conclusions to draw after a single trial. One simple way of reducing the variance is to pretend that we flipped the coin an additional <span class="math inline">\$m\$</span> times resulting in <span class="math inline">\$a\$</span> heads and <span class="math inline">\$m-a\$</span> tails. This will tend to shade our estimate toward <span class="math inline">\$a/m\$</span>, reducing the risk if <span class="math inline">\$\\theta = a/m\$</span> but possibly increasing the risk for other values of <span class="math inline">\$\\theta\$</span>.

We show the risk function for several alternative estimators of this form below:

<span class="math display">\\$$ \\delta\_1(X) = \\frac{X + 1}{n + 2}, \\quad \\delta\_2(X) = \\frac{X + 2}{n + 4}, \\quad \\delta\_3(X) = \\frac{X + 1}{n} \\$$</span>

The last estimator, <span class="math inline">\$\\delta\_3\$</span>, is another example where we add something to <span class="math inline">\$X\$</span> in the numerator but nothing <span class="math inline">\$n\$</span> in the denominator.

``` {.sourceCode .r .code-with-copy}
library(RColorBrewer)

n = 16

---

[← Statistical models](02-statistical-models.md) · [Up: contents](index.md) · [risk function of estimator (X + synth.heads) / (n + synth.flips) →](04-risk-function-of-estimator-x-synth-heads-n-synth-flips.md)
