---
title: (Mis-)Interpreting Hypothesis Tests
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# (Mis-)Interpreting Hypothesis Tests

**Source:** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

ypothesis tests, and their manifestations as <span class="math inline">\$p\$</span>-values and confidence intervals, are ubiquitous in science and social science because drawing reliable conclusions from data is a ubiquitous goal. They are tremendously useful tools, but they unfortunately lend themselves to a variety of misinterpretations. For example, it is distressingly common to observe the following reasoning errors implicit in published scientific work:

1.  <span class="math inline">\$p &lt; 0.05\$</span>, therefore there is an effect (which is equal to the point estimate).

2.  <span class="math inline">\$p &gt; 0.05\$</span>, therefore there is no effect

3.  <span class="math inline">\$p &lt; 10^{-6}\$</span>, therefore the effect is huge

4.  <span class="math inline">\$p &lt; 10^{-6}\$</span>, therefore “the data are highly significant” and all point estimates of model parameters can be taken at face value

5.  The CI for the effect size on men is <span class="math inline">\$$$0.2, 3.2$$\$</span>, but for women it is <span class="math inline">\$$$-0.2, 2.8$$\$</span>, therefore there is an effect for men but not for women.

As a broad generalization, confidence intervals tend not to mislead novices as frequently as <span class="math inline">\$p\$</span>-values or dichotomous accept/reject decisions do. For example, “the effect size was <span class="math inline">\$1.4\$</span> (<span class="math inline">\$p = 0.03\$</span>)” gives an impression of greater precision than “the effect size was <span class="math inline">\$1.4\$</span> (CI <span class="math inline">\$$$0.14, 2.7$$\$</span>).

More subtly, statistical models are almost always abstractions that fail to capture every detail of a real-world scientific setting. It is always important to keep these limitations in mind, but especially so when we are looking to draw some conclusive inference from our data. Many errors arise from the desire of scientists, who may feel shaky in their understanding of statistics, to compartmentalize the statistical analysis from the scientific reasoning it supports.

Unfortunately, interpreting tests can never be made easy or automatic, for the same reason that science can never be made easy or automatic. Hypothesis tests are a tool for critical thinking, not a substitute for it: they let us ask specific questions, in specific ways, under specific modeling assumptions, and all of the choices we make along the way must be justified as a part of any argument that we ultimately want to make for a scientific conclusion. When scientists report some scientific claim supported by a <span class="math inline">\$p\$</span>-value, but omit any description of what analysis was performed or what assumptions were made in order to produce the <span class="math inline">\$p\$</span>-value, their arguments are inherently incomplete.

---

[← Confidence Regions](03-confidence-regions.md) · [Up: contents](index.md) · [Conceptual objections to hypothesis testing →](05-conceptual-objections-to-hypothesis-testing.md)
