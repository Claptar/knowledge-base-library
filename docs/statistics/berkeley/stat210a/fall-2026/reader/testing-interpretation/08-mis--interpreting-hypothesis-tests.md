---
title: (Mis-)Interpreting Hypothesis Tests
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# (Mis-)Interpreting Hypothesis Tests

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

ypothesis tests, and their manifestations as $p$-values and confidence intervals, are ubiquitous in science and social science because drawing reliable conclusions from data is a ubiquitous goal. They are tremendously useful tools, but they unfortunately lend themselves to a variety of misinterpretations. For example, it is distressingly common to observe the following reasoning errors implicit in published scientific work:

1. $p < 0.05$, therefore there is an effect (which is equal to the point estimate).

2. $p > 0.05$, therefore there is no effect

3. $p < 10^{-6}$, therefore the effect is huge

4. $p < 10^{-6}$, therefore "the data are highly significant" and all point estimates of model parameters can be taken at face value

5. The CI for the effect size on men is $[0.2, 3.2]$, but for women it is $[-0.2, 2.8]$, therefore there is an effect for men but not for women.

As a broad generalization, confidence intervals tend not to mislead novices as frequently as $p$-values or dichotomous accept/reject decisions do. For example, "the effect size was $1.4$ ($p = 0.03$)" gives an impression of greater precision than "the effect size was $1.4$ (CI $[0.14, 2.7]$).

More subtly, statistical models are almost always abstractions that fail to capture every detail of a real-world scientific setting. It is always important to keep these limitations in mind, but especially so when we are looking to draw some conclusive inference from our data. Many errors arise from the desire of scientists, who may feel shaky in their understanding of statistics, to compartmentalize the statistical analysis from the scientific reasoning it supports.

Unfortunately, interpreting tests can never be made easy or automatic, for the same reason that science can never be made easy or automatic. Hypothesis tests are a tool for critical thinking, not a substitute for it: they let us ask specific questions, in specific ways, under specific modeling assumptions, and all of the choices we make along the way must be justified as a part of any argument that we ultimately want to make for a scientific conclusion. When scientists report some scientific claim supported by a $p$-value, but omit any description of what analysis was performed or what assumptions were made in order to produce the $p$-value, their arguments are inherently incomplete.

---

[← Confidence Regions](07-confidence-regions.md) · [Up: contents](index.md) · [Conceptual objections to hypothesis testing →](09-conceptual-objections-to-hypothesis-testing.md)
