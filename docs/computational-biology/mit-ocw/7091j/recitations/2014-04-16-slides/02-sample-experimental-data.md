---
title: Sample Experimental Data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Sample Experimental Data

- Phosphoproteomic data (measuring the activity state of pathway molecules)
  - Multiple relevant signaling pathways
  - Introduce perturbations (e.g. inhibitor molecules) and measure outputs at various time points

### b. Primary human hepatocytes

| Signal | Control | IFN$\gamma$ | TNF$\alpha$ | IL1$\alpha$ | IL6 | IGF-I | TGF$\alpha$ | LPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| IRS1 | | | | | | | | |
| AKT | | | | | | | | |
| MEK1 | | | | | | | | |
| ERK1&2 | | | | | | | | |
| p90RSK | | | | | | | | |
| CREB | | | | | | | | |
| p70S6 | | | | | | | | |
| p38 | | | | | | | | |
| HSP27 | | | | | | | | |
| I$\kappa$b | | | | | | | | |
| JNK12 | | | | | | | | |
| cJUN | | | | | | | | |
| p53 | | | | | | | | |
| GSK3$\alpha$/$\beta$ | | | | | | | | |
| Hist. H3 | | | | | | | | |
| STAT3 | | | | | | | | |
| STAT6 | | | | | | | | |

Inhibitors: 1 2 3 4 5 6 7 8 (repeated across stimuli)

### c. Transformed cell line (HepG2 cells)

| Signal | Control | IFN$\gamma$ | TNF$\alpha$ | IL1$\alpha$ | IL6 | IGF-I | TGF$\alpha$ | LPS | Maximum Value (Fluorescent Units) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| IRS1 | | | | | | | | | 590 |
| AKT | | | | | | | | | 1800 |
| MEK1 | | | | | | | | | 3100 |
| ERK12 | | | | | | | | | 620 |
| p90RSK | | | | | | | | | 180 |
| CREB | | | | | | | | | 200 |
| p70S6 | | | | | | | | | 1500 |
| p38 | | | | | | | | | 110 |
| HSP27 | | | | | | | | | 3100 |
| Ikb | | | | | | | | | 1100 |
| JNK12 | | | | | | | | | 160 |
| cJUN | | | | | | | | | 2700 |
| p53 | | | | | | | | | 110 |
| GSK3 | | | | | | | | | 550 |
| Hist.H3 | | | | | | | | | 80 |
| STAT3 | | | | | | | | | 570 |
| STAT6 | | | | | | | | | 25 |

Inhibitors: 1 2 3 4 5 6 7 8 (repeated across stimuli)

**Inhibitor Key:**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Control
No inhibitor | MEK1/2
PD325901 | p38
PHA818637 | PI3K
ZSTK747 | IKK
BMS345541 | mTOR
Rapamycin | GSK3$\alpha$/$\beta$
InhXI | JNK1/2
SP600125 |

**Response Dynamics:**
- **TRANSIENT:** $\boldsymbol{\Lambda}$
- **NO RESPONSE:** **—**
- **LATE:** $\boldsymbol{/}$
- **SUSTAINED:** $\boldsymbol{\Gamma}$

**Time-points: 0, 30 min, 3 hrs**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

- Phosphoproteomic data (measuring the activity state of pathway molecules)
  - Multiple relevant signaling pathways
  - Introduce perturbations (e.g. inhibitor molecules) and measure outputs at various time points
- Try to model the experimental data using the multiple potential networks (graph structures and associated quantitative relationships) from the databases
  - We must define some way to evaluate the model's performance to decide which is the most likely network

$$\text{Objective Function} \quad \theta = \theta_f + \alpha \cdot \theta_S$$

- **Fit to data:**
$$\theta_f = \sum_{l=1}^S \sum_{k=1}^M \frac{(B_{l,k}^M - B_{l,k}^E)^2}{E \in \{0, 1\}} \Biggr\vert_{E \in \{0, 1\}}$$

- **Relative importance:**
$$\text{Fit vs. Size}$$

- **Size of model:**
$$\theta_S = \sum_{k=1}^R v_k P_k$$

- We want to consider not necessarily the single best model (because of experimental noise), but look at the full spectrum of top performing models to come up with a representative family of models

---

## Improving upon models

- From the top performing model(s), make some perturbations of the model (via genetic algorithms) to improve the fit (similar to what we saw for Bayesian networks, e.g. Pebl)
- How well does this work in practice?
  - If we simply take the best result from the database and fit the experimental data to the model, we get ~45% error (because not all interactions are real and some are missing, might be the wrong cell type or environmental condition, etc.)
  - After model improvement (e.g. adding and removing edges), we may be able to reduce the error to below 10%
  - Often the model is not as complex as we might expect! Introducing too many variables may lead to simply fitting to noise and increase false positives

---

## What are models used for?

- Can make predictions for new inhibitor combinations (therapeutic drug cocktails) that may be infeasible to exhaustively test experimentally
  - Comparing where our model predictions went wrong based on new experimental data informs us where our network model may be incorrect and how we might improve it
  - Edges that are included in the model and needed to explain the data can inform us about cellular processes (interactions that are missing in the databases or off-target effects of drugs)

---

## Extending Boolean Logic for analog data

- Boolean logic deals with qualitative YES/NO (ON/OFF) relationships, but quantitative data is continuous
  - Instead of a step function from OFF to ON at a particular value, use continuous functions that have a graded slope from OFF to ON over a range of values
    - More realistic, but this ~doubles the number of free parameters in the model, so we need much more experimental data

---

## Fin

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4-16 Recitation](01-4-16-recitation.md) · [Up: contents](index.md)
