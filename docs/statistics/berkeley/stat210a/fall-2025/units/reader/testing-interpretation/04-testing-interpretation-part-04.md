---
title: Testing interpretation Part 04 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Testing interpretation Part 04 —

**Source:** [`units/reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Hypothesis tests ubiquitous in science Common misinterpretations:

1.  p &lt; 0.05, therefore there is an effect (or the effect size = the estimate)
2.  p &gt; 0.05, therefore there is no effect
3.  p = 10^-6, therefore the effect is huge
4.  p &lt; 10^-6, therefore the data are significant and everything about our model is correct (in most naive interpretation)
5.  Effect CI for men is $$0.2, 3.2$$, for women is $$-0.2, 2.8$$, therefore there is an effect for men and not for women

Dichotomous test doesn’t eliminate uncertainty CIs usually less misleading to novices

Interpreting tests is not easy or automatic Hypothesis tests let us ask specific questions under specific modeling assumptions Interpreting them requires care and experience

Top-tier medical journals let people publish claims reporting p-values without saying what model was used or what test was employed Pretty bad when you think about it

Hyp. tests can be a good companion to critical thinking, never a substitute All models are wrong, some are useful, but need experience and theory to understand when assumptions do or don’t cause real trouble

### <span class="header-section-number">3.1</span> Common Objections to Hypothesis Testing {.anchored number="3.1" anchor-id="common-objections-to-hypothesis-testing"}

1.  Why should I test <span class="math inline">\$\\theta = 0\$</span>? Is <span class="math inline">\$\\theta\$</span> ever exactly 0?

    A: a. Test <span class="math inline">\$H\_0: \|\\theta\| &lt; \\epsilon\$</span> if you want If <span class="math inline">\$\\sigma\_{\\hat{\\theta}} \\ll \\epsilon\$</span>, not much difference

    1.  Most two-sided tests justify directional interest: If <span class="math inline">\$T &gt; c\$</span>, declare <span class="math inline">\$\\theta &gt; 0\$</span>, if <span class="math inline">\$T &lt; -c\$</span>, declare <span class="math inline">\$\\theta &lt; 0\$</span> with <span class="math inline">\$\\mathbb{P}(\\text{false claim}) &lt; \\alpha\$</span>

    2.  Harder to answer in non-parametric problems e.g. <span class="math inline">\$H\_0: P = Q\$</span> vs <span class="math inline">\$H\_1: P \\neq Q\$</span> for perm test, but alternative frameworks like Bayes force very strong assumptions on us

2.  People only like frequentist results like p-values, CIs because they mistake them for Bayesian results “95% chance <span class="math inline">\$\\theta &gt; 0\$</span>” is misinterpreted as a claim about <span class="math inline">\$\\mathbb{P}(\\theta &gt; 0 \| X)\$</span>

    A: True, but subjective Bayesian results often misinterpreted as the posterior dist. of <span class="math inline">\$\\theta\$</span> when really should be “posterior opinion about <span class="math inline">\$\\theta\$</span>”

---

[← 2 Confidence Regions {.anchored number="2" anchor-id="confidence-regions"}](03-2-confidence-regions-anchored-number-2-anchor-id-confidence.md) · [Up: contents](index.md)
