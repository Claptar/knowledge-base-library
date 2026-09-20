---
title: 15 slides Part 03 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 15 slides Part 03 —

David Venet$^{1}$, Jacques E. Dumont$^{2}$, Vincent Detours$^{2,3*}$

1 IRIDIA-CoDE, Université Libre de Bruxelles (U.L.B.), Brussels, Belgium, 2 IRIBHM, Université Libre de Bruxelles (U.L.B.), Campus Erasme, Brussels, Belgium, 3 WELBIO, Université Libre de Bruxelles (U.L.B.), Campus Erasme, Brussels, Belgium

PLoS Computational Biology | www.ploscompbiol.org
October 2011 | Volume 7 | Issue 10 | e1002240

---

A post-prandial laughter
HR=1.8 (CI, 1.2–2.9)
p=0.0072

B localization of skin fibroblasts
HR=1.9 (CI, 1.2–2.9)
p=0.0066

C social defeat in mice
HR=2.4 (CI, 1.5–3.9)
p=0.00014

D
mSigDB sig.
random sig.
77%
67%
$\log_{10}(0.05)$

Courtesy of Venet et al. License: CC-BY.
Source: Venet, David, Jacques E. Dumont, et al. "Most Random Gene Expression Signatures are Significantly
Associated with Breast Cancer Outcome." PLoS Computational Biology 7, no. 10 (2011): e1002240.

OS= the fraction of patients alive (overall survival)
Hazard Ratio= Death rate vs. control

---

$\log_{10}(0.05)$

Published Signature
Distribution for random signatures
Best 5% of random signatures

$p\text{-value } (\log_{10})$

Courtesy of Venet et al. License: CC-BY.
Source: Venet, David, Jacques E. Dumont, et al. "Most Random Gene
Expression Signatures are Significantly Associated with Breast Cancer
Outcome." PLoS Computational Biology 7, no. 10 (2011): e1002240.

---

Hazard Ratio=
Death rate vs. control

$$R^2 = 0.9$$

abs. PCNA metagene corr.

Courtesy of Venet et al. License: CC-BY.
Source: Venet, David, Jacques E. Dumont, et al. "Most Random Gene
Expression Signatures are Significantly Associated with Breast Cancer
Outcome." PLoS Computational Biology 7, no. 10 (2011): e1002240.

PCNA metagene = 1% genes the most positively correlated with expression of PCNA
(proliferating cell nuclear antigen, a known marker) across 36 tissues

---

## Outline

- Bayesian Networks for PPI prediction
- Gene expression
  - Distance metrics
  - Clustering
  - Signatures
  - **Modules**
    - **Bayesian networks**
    - Regression
    - Mutual Information
    - Evaluation on real and simulated data

---

## Reconstructing Regulatory Networks

TF A1
TF B1
TF A2
TF B2

Courtesy of Elsevier B.V. Used with permission.
Source: Sumazin, Pavel, Xuerui Yang, et al. "An Extensive
MicroRNA-mediated Network of RNA-RNA Interactions
Regulates Established Oncogenic Pathways in
Glioblastoma." Cell 147, no. 2 (2011): 370-81.

---

## Clustering vs. “modules”

- Clusters are purely phenomenological – no claim of causality
- The term “module” is used to imply a more mechanistic connection

Transcription factor A
Transcription factor B

Correlated expression

---

NATURE METHODS | ANALYSIS

---

[← Distinct types of diffuse large B-cell lymphoma identified by gene expression profiling](02-distinct-types-of-diffuse-large-b-cell-lymphoma-identified-b.md) · [Up: contents](index.md) · [Wisdom of crowds for robust gene network inference →](04-wisdom-of-crowds-for-robust-gene-network-inference.md)
