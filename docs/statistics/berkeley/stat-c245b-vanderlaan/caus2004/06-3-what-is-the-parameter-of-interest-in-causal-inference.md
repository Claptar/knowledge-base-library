---
title: 3. What is the parameter of interest in causal inference?
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. What is the parameter of interest in causal inference?

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In causal inference problems, parameters of interest are called causal parameters. Typically they are functions of the data generating distribution of X ~~F~~ ULL, but in history adjusted marginal structural models they will be functions of conditional distributions of the counterfactual outcome Ya¯, given an observed past. Usually these parameters will be related to how the outcome process Y <u>a</u><sup>varies with</sup> ~~a,~~ and how this variation is modified by the covariates. For instance, in a marginal structural models our model might assume that E[Y ~~a~~<sup>~~(~~t)]=m(t,</sup> ~~a,~~ β) for some known function m(·) and unknown Euclidean parameter β. In this case, β would be the causal parameter, and we would have to find a way to estimate it from the observed data. Note that because the observed data (A, X) is a strict subset of the full data (A, X ~~F~~ ULL), causal inference can be treated as a missing data problem. This will be heavily exploited in the following lectures. The general estimating function approach for censored/missing data structures as described in van der Laan, Robins (2002), and presented in this course, corresponds with first finding procedures (i.e., full data estimating functions) that can estimate the causal parameter from the full data, and then map these to procedures (i.e., observed data estimating functions) that estimate the causal parameter from the observed data.

---

[← 2. What is the model in causal inference problems?](05-2-what-is-the-model-in-causal-inference-problems.md) · [Up: contents](index.md) · [Causal graphs, 9/1/2004 Notes. →](07-causal-graphs-9-1-2004-notes.md)
