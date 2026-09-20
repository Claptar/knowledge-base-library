---
title: A Bayesian Networks Approach for Predicting Protein-Protein Interactions from
  Genomic Data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# A Bayesian Networks Approach for Predicting Protein-Protein Interactions from Genomic Data

Ronald Jansen,$^{1*}$ Haiyuan Yu,$^1$ Dov Greenbaum,$^1$ Yuval Kluger,$^1$ Nevan J. Krogan,$^4$ Sambath Chung,$^{1,2}$ Andrew Emili,$^4$ Michael Snyder,$^2$ Jack F. Greenblatt,$^4$ Mark Gerstein$^{1,3\dagger}$

B
In vivo pull-down: Gavin, Ho $\longrightarrow$ Fully connected Bayes $\longrightarrow$ PIE
Y2H: Uetz, Ito $\longrightarrow$ Fully connected Bayes $\longrightarrow$ PIE

mRNA co-expr.: Rosetta, Cell cycle $\longrightarrow$ Naïve Bayes $\longrightarrow$ PIP
GO process $\longrightarrow$ Naïve Bayes $\longrightarrow$ PIP
MIPS function $\longrightarrow$ Naïve Bayes $\longrightarrow$ PIP
Essentiality $\longrightarrow$ Naïve Bayes $\longrightarrow$ PIP

PIE, PIP $\longrightarrow$ Naïve Bayes $\longrightarrow$ PIT

Probabilistic interactome (PI)
Integration process
Data source

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-Protein Interactions from Genomic Data." Science 302, no. 5644 (2003): 449-53.
http://www.sciencemag.org/content/302/5644/449.abstract
SCIENCE VOL 302 17 OCTOBER 2003

---

## PSICQUIC and PSISCORE: accessing and scoring molecular interactions

Nature Methods 8, 528–529 (2011)
doi:10.1038/nmeth.1637

Human Proteome Organization Proteomics Standards Initiative (HUPO-PSI) released the PSI molecular interaction (MI) XML format

PSI common query interface (PSICQUIC), a community standard for computational access to molecular-interaction data resources.

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Aranda, Bruno, Hagen Blankenburg, et al. "PSICQUIC and PSISCORE: Accessing and Scoring Molecular Interactions." Nature Methods 8, no. 7 (2011): 528-9.

http://www.nature.com/nmeth/journal/v8/n7/full/nmeth.1637.html

---

Input $\longrightarrow$ PSISCORE Client $\longrightarrow$ Output

PSISCORE Server A: Coexpression of interactors
PSISCORE Server B: Functional similarity of protein annotation
PSISCORE Server C: Interactions that can be explained by domain-domain interactions

© Thomas Lengauer. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

http://www.nature.com/nmeth/journal/v8/n7/full/nmeth.1637.html

---

## MIscore algorithm

Minimum INformation about a Molecular Interaction eXperiment
Manuscript, Experiment, Interaction
$\downarrow$
Number of publications, Detection methods, Interaction types
$\downarrow$
MIscore [0-1]

Courtesy of Miscore. Used with permission.

MIscore is a normalized score between 0 and 1 that takes into account several variables:
• Number of publications
• Experimental detection methods found for the interaction
• Interaction types found for the interaction
Each of these variables is also represented by a score between 0 and 1. The importance of each variable in the main equation can be adjusted using a weight factor.

---

## MIscore algorithm

$$S_{MI} = \frac{K_p \times S_p(n) + K_m \times S_m(cv) + K_t \times S_t(cv)}{K_p + K_m + K_t}$$

Depends on
• Number of publications $\longleftarrow K_p \times S_p(n)$
• Experimental method (biophys.; imaging; genetic) $\longleftarrow K_m \times S_m(cv)$
• Annotation of interaction type (physical, genetic) $\longleftarrow K_t \times S_t(cv)$

---

## Weighted Interactome

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Finding Modules

### a Topological module
• **Topological module:**
– locally dense
– more connections among nodes in module than with nodes outside module

### b Functional module
• **Functional module:**
– high density of functionally related nodes

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Barabási, Albert-László, Natali Gulbahce, et al. "Network Medicine: A Network-based Approach to Human Disease." Nature Reviews Genetics 12, no. 1 (2011): 56-68.

## Can we use networks to predict function

known
unknown

| | *S. cerevisiae* | *C. elegans* | *D. melanogaster* | *A. thaliana* | *M. musculus* | *H. sapiens* |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Biological process** | 1.540 / 4.322 | 2.096 / 17.086 | 6.004 / 7.480 | 6.863 / 19.464 | 11.698 / 25.751 | 12.221 / 13.180 |
| **Molecular function** | 2.130 / 3.732 | 10.836 / 8.348 | 6.073 / 7.411 |

## Prize Collecting Steiner Tree

- Collect a **prize** for each data point included

No prize

No prize

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

---

## Don't Include All Data

- Pay a **penalty** for excluding nodes

No penalty

proportional to absolute value of log fold change

$$\sum_{v \text{ not in } T} \beta \text{ penalty}(v) + \sum_{e \text{ in } T} \text{cost}(e)$$

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

---

## Avoid Unlikely Interactions

- Pay a **cost** for **including** edges based on probability

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

$$\sum_{v \text{ not in } T} \beta \text{ penalty}(v) + \sum_{e \text{ in } T} \text{cost}(e)$$

---

## Balanced Objective Function

Does the **node penalty** justify the **edge costs**?

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

$$\sum_{v \text{ not in } T} \beta \text{ penalty}(v) + \sum_{e \text{ in } T} \text{cost}(e)$$

---

## Optimization methods:

- Biazzo I, Braunstein A, Zecchina R.
  *Phys Rev E Stat Nonlin Soft Matter Phys.* 2012 Aug;86(2 Pt 2):026706.
- I. Ljubic, R. Weiskircher, U. Pferschy, G. Klau, P. Mutzel, and M. Fischetti:
  *Mathematical Programming, Series B*, 105(2-3):427-449, 2006.

Does the **node penalty** justify the **edge costs**?

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

$$\sum_{v \text{ not in } T} \beta \text{ penalty}(v) + \sum_{e \text{ in } T} \text{cost}(e)$$

---

## Naïve Methods

- >2,500 nearest neighbors of phosphoproteins
- >4,500 nearest neighbors of phosphoproteins +transcription factors

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling
*PLoS Comput Biol* 9(2): e1002887. doi:10.1371/journal.pcbi.1002887

---

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling
*PLoS Comput Biol* 9(2): e1002887. doi:10.1371/journal.pcbi.1002887

---

## Can we find drug targets?

Rank every node by weighted distance to all prize-collecting Steiner tree nodes

**High rank targets**

**Control targets**

Steiner Tree

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

---

### Rank <27 out of 11,637

Cell Type
Control
vIII

### Lower Rank Targets 193 to 3,582 out of 11,637

Cell Type
Control
vIII

Source: Huang, Shao-shan Carol, David C. Clarke, et al. "Linking Proteomic and Transcriptional Data through the Interactome and Epigenome Reveals a Map of Oncogene-induced Signaling." *PLoS Computational Biology* 9, no. 2 (2013): e1002887.

---

## Data Integration

---

---

← B · [Up: contents](index.md) · [Approach →](06-approach.md)
