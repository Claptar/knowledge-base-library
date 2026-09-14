---
title: 2. What is the model in causal inference problems?
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. What is the model in causal inference problems?

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Causal inference is the study of counterfactuals, which are the outcomes that would have been observed had the treatment somehow been different. Specifically, let X <u>a</u><sup>beacounterfactual,andrepresentthe</sup> process X that would have been observed had the treatment been set at A = ~~a.~~ When A = ~~a,~~ we refer to the observed X <u>a</u><sup>=</sup> X A<sup>asthefactual.Wewillassumethat</sup> X A<sup>=</sup> X, and this is called the consistency assumption. It states that the observed data is equal to what we would have observed in the counterfactual world had the treatment been set to the observed treatment. In the AIDS example, suppose ~~a~~ represents

1

no treatment being given. Then for a given patient, X <u>a</u><sup>representsthecovariateprocessthatwouldhave</sup> occured if, contrary to fact, no treatment had been given to that patient. The idea of counterfactuals raises philosophical issues that have been discussed at least since the time of David Hume, because in the real world each subject is only assigned one treatment process. In causal inference problems, our model will assume the existence of counterfactuals. If Θ represents the support of A, then we refer to X F ULL = (X ~~a~~<sup>:</sup> ~~a~~ ∈ Θ) as the full data. For the estimation procedures discussed in this class to be effective, we must make additional assumptions on the distribution of X ~~F~~ ULL (the full data model), and the conditional distribution of A¯, given X ~~F~~ ULL, such as the sequential randomization or no unmeasured confounding assumptions, and these will be formally defined in subsequent lectures. The choice of models are typically heavily driven by the parameter of interest. Our general phylosophy is that one should make model assumptions on the parameter of interest, but try to minimize assumptions on the nuisance parameters.

Marginal structural models, models for direct and indirect effects, and history adjusted marginal structural models (three topics covered in this class) are just different models on (conditional) distributions of counterfactuals, describing how these conditional distributions change with a change in treatment regime a¯.

---

[← 1. What is the data in causal inference problems?](04-1-what-is-the-data-in-causal-inference-problems.md) · [Up: contents](index.md) · [3. What is the parameter of interest in causal inference? →](06-3-what-is-the-parameter-of-interest-in-causal-inference.md)
