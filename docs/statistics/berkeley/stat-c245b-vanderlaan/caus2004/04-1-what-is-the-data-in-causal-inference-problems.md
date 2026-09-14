---
title: 1. What is the data in causal inference problems?
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. What is the data in causal inference problems?

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will be interested in longitudinal data, where each subject is followed over time, and we define the following variables.

A(t). This denotes the treatment given to a subject at time t.

- Y(t). This denotes some outcome of interest, measured at time t.

X(t). This include Y (t), as well as time-dependent (and baseline) covariates measured on the subject.

Note that A(t), Y (t), X(t) can be <u>possibly</u> multivariate. Define A as (A(t) : t ≥ 0), the process giving the value of A(t) for each t, and define Y and X similarly. The observed data in causal inference problems is then n i.i.d. copies of (A, X) ∼ P0. If the reader is unfamiliar with the notation i.i.d., feel free to consult any introductory statistics text. Here P0 is the (unknown) data generating distribution, which assigns probabilities to members of the population of interest.

As an example, consider an AIDS study. Suppose n patients are selected at random from an AIDS registry, and each is followed up for a period of time. Here P0 is the probability distribution putting equal mass on each sample of n distinct subjects from the registry (this approximates i.i.d. sampling if the registry size is very large compared to n), and the population of interest consists of all members of the registry. We might have A(t) represent the collection of medications being prescribed to the patient at time t, and the outcome Y (t) might represent the viral load at time t or an indicator of whether the patient is still alive at time t. Here X(t) could include baseline measurements such as the patient’s sex, age, and income, as well as time-dependent covariates such as the patient’s CD4 count at time t.

---

[← The three big questions](03-the-three-big-questions.md) · [Up: contents](index.md) · [2. What is the model in causal inference problems? →](05-2-what-is-the-model-in-causal-inference-problems.md)
