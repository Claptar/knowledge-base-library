---
title: For 156 perturbations
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# For 156 perturbations

Genetic Data Enriched for:
- **Transcriptional regulation**
- **Signal transduction**

Expression Data Enriched for:
- **Metabolic Processes**
  - **e.g., organic acid metabolic process, oxidoreducatse activities**

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

DNA Damage

Sliding clamp checkpoint

MEC3 DDC1 RAD17 RAD24
MEC1
RAD9
RAD53
DUN1
RFX1
Cell cycle arrest
RNR4g+
DNA repair

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

DNA Damage

MEC3 DDC1 RAD17 RAD24
MEC1 = ATM
RAD9
RAD53 = CHK2
DUN1
RFX1
Cell cycle arrest
RNR4g+
DNA repair

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

Interactome

TF

ChIP-chip & Sequence Analysis

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

## Test case: Perturbing pheromone response pathway

### Perturbing Ste5

20 genes rescue mating phenotype (SGD)

12 genes differentially expressed (Rosetta compendium)

Ste2
Gpa1
Ste18
Ste4
Ste5
Ste11
Ste7
Cdc42
Ste20
Ste50
Fus3
Dig1 Ste12

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

## $\Delta$ste5: Naïve approach
### Paths limited to length 3

Genetic Data

Expression Data

193 nodes, 778 edges

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

## Maximize the connectivity via reliable paths

$p=0.1$
$p=0.9$

Goal: find paths that maximize product of $P_{ij}$

Assign probabilities using a Bayesian approach based on reliability of underlying data type:

Myers, C.L. et al. *Genome Biology* (2005).

Jansen, R. et al. *Science* (2003).

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

## Maximize the connectivity via reliable paths

Source

Minimum cost flow problem

Flow

Low probability
High probability

FLOW

Sink

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

## Maximize the connectivity via reliable paths

Source

Minimum cost flow problem

Flow

$p=0.1$
$p=0.9$

Low probability
High probability

FLOW

Proteins ranked by their incoming flow:

Less important $\longrightarrow$ More important

Sink

---

## Maximize the connectivity via reliable paths

Source

$p=0.1$
$p=0.9$

FLOW

Sink

Minimum cost flow problem

Maximize flow: source to sink

$$\text{Minimize cost}(e_{ij}) = f_{ij} * (-\log P_{ij})$$

$$\min \left(\sum \text{cost}(e_{ij}) - \gamma * \sum f_{Sj}\right)$$

$f_{ij} =$ flow through $e_{ij}$

$c_{ij} =$ capacity of $e_{ij} = 1$ for all $e_{ij}$

Proteins ranked by their incoming flow:

Less important $\longrightarrow$ More important

---

## Test case: Perturbing pheromone response pathway

### Perturbing Ste5

20 genes rescue mating phenotype (SGD)

12 genes differentially expressed (Rosetta compendium)

Ste2
Gpa1
Ste18
Ste4
Ste5
Ste11
Ste7
Cdc42
Ste20
Ste50
Fus3
Dig1 Ste12

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

Enriched for pheromone response $p < 10^{-18}$

Genetic Data

Expression Data

49 nodes, 96 edges

Predicted genes
Importance

---

## Network Models

- Structure of network
  - Coexpression
  - Mutual information
  - Physical/genetic interactions
- Analysis of network
  - Ad hoc
  - Shortest path
  - Clustering
  - Optimization

---

| | Known Components | Unknown Components |
| :--- | :--- | :--- |
| **Physical Relationships** | Differential equations

Boolean logic, decision trees | Interactome Models |
| **Statistical Relationships** | Bayesian networks | mutual information

regression, clustering |

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Approach](06-approach.md) · [Up: contents](index.md)
