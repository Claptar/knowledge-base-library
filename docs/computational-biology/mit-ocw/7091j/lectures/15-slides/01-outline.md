---
title: Outline
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

• L12 - Introduction to Protein Structure; Structure Comparison & Classification
• L13 - Predicting protein structure
• L14 - Predicting protein interactions
• L15 - Gene Regulatory Networks
• L16 - Protein Interaction Networks
• L17 - Computable Network Models

---

• Bayesian Networks for PPI prediction
• Gene expression
  – Distance metrics
  – Clustering
  – Signatures
  – Modules

## K-medoids clustering

- Initialize: choose k points as cluster means
- Repeat until convergence:
  - Assignment: place each point $X_i$ in the cluster with the closest medoid.
  - Update: recalculate the medoid for each cluster

---

## Other approaches

- SOM (Text 16.3)
- Affinity Propagation
  - Frey and Dueck (2007) Science.

---

## So What?

- Clusters could reveal underlying biological processes not evident from complete list of differentially expressed genes
- Clusters could be co-regulated. How could we find upstream factors?

---

- Bayesian Networks for PPI prediction
- Gene expression
  - Distance metrics
  - Clustering
  - Signatures
  - Modules
    - Bayesian networks
    - Regression
    - Mutual Information
    - Evaluation on real and simulated data

---

## Personalized Medicine

- Can gene expression be used for diagnosis and to determine the best treatment?

---

---

[Up: contents](index.md) · [Distinct types of diffuse large B-cell lymphoma identified by gene expression profiling →](02-distinct-types-of-diffuse-large-b-cell-lymphoma-identified-b.md)
