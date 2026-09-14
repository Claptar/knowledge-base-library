---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

As we have previously defined hypothesis tests, they are characterized by dichotomous accept/reject decisions after choosing a null hypothesis, a test statistic, and a critical threshold. Sometimes we really do need to make a dichotomous decision (for example, the FDA really has to decide whether to approve a drug or not), but this is rare in practice. If our test statistic is large enough to reject $H_0:\;\theta=0$ at the $\alpha = 0.05$ level, we would usually still be interested in questions like:

- Would we have rejected $H_0$ at a stricter $\alpha$ level, like $\alpha = 0.01$ or $\alpha = 0.005$?

- Have we established that $\theta$ is far from zero, or only that it isn't exactly zero?

These questions can be answered by $p$-values and confidence regions, which enrich our dichotomous decision by respectively telling us about the outcome for other $\alpha$ values we could have used, and for other null hypotheses we could have tested.

---

[Up: contents](index.md) · [p-Values →](02-p-values.md)
