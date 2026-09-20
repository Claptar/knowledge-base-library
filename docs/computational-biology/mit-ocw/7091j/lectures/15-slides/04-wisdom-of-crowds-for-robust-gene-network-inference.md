---
title: Wisdom of crowds for robust gene network inference
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Wisdom of crowds for robust gene network inference

Daniel Marbach, James C Costello, Robert Küffner, Nicole M Vega, Robert J Prill, Diogo M
Camacho, Kyle R Allison, The DREAM5 Consortium, Manolis Kellis, James J Collins &
Gustavo Stolovitzky

Affiliations | Contributions | Corresponding author

Nature Methods 9, 796–804 (2012) | doi:10.1038/nmeth.2016
Received 31 October 2011 | Accepted 22 May 2012 | Published online 15 July 2012

---

Wisdom of crowds for robust gene network inference
Nature Methods 9, 796–804 (2012) doi:10.1038/nmeth.2016

(1) Target networks
Simulation
In silico
195 regulators
1,643 genes

Experiments
E. coli
296 regulators
4,297 genes

S. cerevisae
183 regulators
5,667 genes

S. aureus
90 regulators
2,677 genes

(2) Microarray data sets
805 arrays
487 conditions

805 arrays
487 conditions

Knockouts
Antibiotics
Toxins
...
536 arrays
321 conditions

160 arrays
53 conditions

Inference methods
Anonymize data

(3) Inferred networks

Integrate

(4) Consensus

Validate

(5) Evaluation
True in silico network
Experimentally determined interactions
ChIP motifs
...
S. aureus not used for evaluation

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Marbach, Daniel, James C. Costello, et al. "Wisdom of Crowds for
Robust Gene Network Inference." Nature Methods 9, no. 8 (2012): 796-804.

---

b
Inference methods
Regression
Mutual information (MI)
Correlation (corr.)
Bayesian networks
Other
Meta

C1. Regression
C2. Bayesian
C3. MI & corr.
C4. Other

Second principal component
Third principal component

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Marbach, Daniel, James C. Costello, et al. "Wisdom of Crowds for
Robust Gene Network Inference." Nature Methods 9, no. 8 (2012): 796-804.

Wisdom of crowds for robust gene network inference
Nature Methods 9, 796–804 (2012) doi:10.1038/nmeth.2016

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

## Bayesian Networks

Predict unknown variables from observations

mRNA co-expr.
- Rosetta
- Cell cycle
GO process
MIPS function
Essentiality

Naïve Bayes $\rightarrow$ PIP

A “natural” way to think about biological networks.

TF A1
TF B1
TF A2
TF B2

---

## Is the p53 pathway activated?

P53 SIGNALING PATHWAY

Response
Cell cycle arrest
Apoptosis
Inhibition of angiogenesis and metastasis
DNA repair and damage prevention
Inhibition of IGF-1/mTOR pathway
Exosome mediated secretion
p53 negative feedback
Cellular senescence

Courtesy of Looso et al. License: CC-BY.
Source: Looso, Mario, Jens Preussner, et al. "A De Novo Assembly of the Newt Transcriptome Combined with Proteomic
Validation Identifies New Protein Families Expressed During Tissue Regeneration." Genome Biology 14, no. 2 (2013): R16.

---

## Is the p53 pathway activated?

### Possible Evidence

- **Known p53 targets are up-regulated**
  - Could another pathway also cause this?
- **Genes for members of signaling pathway are expressed (ATM, ATR, CHK1, …)**
  - Might be true under many conditions where pathway has not yet been activated
- **Genes for members of signaling pathway are differentially expressed**
  - Still does not prove change in activity

Courtesy of Looso et al. License: CC-BY.
Source: Looso, Mario, Jens Preussner, et al. "A De Novo Assembly of the Newt Transcriptome Combined with Proteomic
Validation Identifies New Protein Families Expressed During Tissue Regeneration." Genome Biology 14, no. 2 (2013): R16.

---

## Is the p53 pathway activated?

- Formulate problem probabilistically
- Compute
  - $\text{P}(\text{p53 pathway activated} \mid \text{data})$
- How?
  - Relatively easy to compute $\text{p}(\text{X up} \mid \text{TF up})$
  - How?

TF
X1 X2 X3

---

## Is the p53 pathway activated?

- Formulate problem probabilistically
- Compute
  - $\text{P}(\text{p53 pathway activated} \mid \text{data})$
- How?
  - Relatively easy to compute $\text{p}(\text{X up} \mid \text{TF up})$
  - Look over lots of experiments and tabulate:
    - X1 up & TF up
    - X1 up & TF not up
    - X1 not up & TF not up
    - X1 not up & TF up

TF
X1 X2 X3

---

## Is the p53 pathway activated?

- Formulate problem probabilistically
- Compute
  - $\text{P}(\text{p53 pathway activated} \mid \text{data})$
- How?
  - Relatively easy to compute $\text{p}(\text{X up} \mid \text{TF up})$
  - $\text{P}(\text{TF up} \mid \text{X up}) = \text{p}(\text{X up} \mid \text{TF up}) \, \text{p}(\text{TF up}) / \text{p}(\text{X up})$

TF
X1 X2 X3

---

## Is the p53 pathway activated?

- Formulate problem probabilistically
- Compute
  - $\text{P}(\text{p53 pathway activated} \mid \text{data})$
- How?
  - Even with $\text{p}(\text{TF up} \mid \text{X up})$ how do we compare this explanation of the data to

## Quick Review of Information Theory

Information content of an event E
$$I(E) = \log_2 \frac{1}{P(E)}$$

Entropy is evaluated over all possible outcomes
$$H(S) = \sum_i p_i I(s_i) = \sum_i p_i \log_2 \frac{1}{p_i}$$

$$H(f) = -\int f(x) \ln f(x) dx.$$

---

## Mutual Information

- Does knowing variable X reduce the uncertainty in variable Y?
- Example:
  - P(Rain) depends on P(Clouds)
  - P(target expressed) depends on P(TF expressed)

$$I(x,y) = H(x) + H(y) - H(x,y)$$

- $I(x,y) = 0$ means variables are independent
- Reveals non-linear relationships that are missed by correlation.

---

## Mutual information detects non-linear relationships

### Incoherent feed-forward loop (FFL)

Mutual information = 1.7343

Correlation coefficient = -0.0464

No correlation, but knowing A reduces the uncertainty in the distribution of B

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Mutual information detects non-linear relationships

- Complex regulatory network structure => complex relationships between protein levels
- Example: incoherent feed-forward loop (FFL)

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## ARACNe

### Reverse engineering of regulatory networks in human B cells

Katia Basso$^1$, Adam A Margolin$^2$, Gustavo Stolovitzky$^3$, Ulf Klein$^1$, Riccardo Dalla-Favera$^{1,4}$ & Andrea Califano$^2$

VOLUME 37 | NUMBER 4 | APRIL 2005 NATURE GENETICS

---

## ARACNe

- Find TF-target relationships using mutual information
$$H(f) = -\int f(x) \ln f(x) dx.$$
- How do you recognize a significant value of MI?
  - randomly shuffle expression data
  - compute distribution of Mutual information

---

## ARACNE

- Data processing inequality
  - Eliminate indirect interactions
  - If G2 regulates G1,G3
    $I(G1,G3) > 0$ but adds no insight
  - Remove edge with smallest mutual information in each triple

$$I(g_1, g_3) \le \min [I(g_1, g_2); I(g_2, g_3)]$$

---

## MINDy

- Identify proteins that modulate TF function
  - Other TFs

Genome-wide identification of post-translational modulators of transcription factor activity in human B cells

Kai Wang$^{1,2,5,6}$, Masumichi Saito$^{3,5,6}$, Brygida C Bisikirska$^2$, Mariano J Alvarez$^2$, Wei Keat Lim$^{1,2,5}$, Presha Rajbhandari$^2$, Qiong Shen$^3$, Ilya Nemenman$^{2,5}$, Katia Basso$^3$, Adam A Margolin$^{1,2,5}$, Ulf Klein$^3$, Riccardo Dalla-Favera$^{3,4}$ & Andrea Califano$^{1-3}$

NATURE BIOTECHNOLOGY VOLUME 27 NUMBER 9 SEPTEMBER 2009

---

## Model

- Assumes that expression of target T is determined by TF and modulator (M)

$$[T] = C \cdot [TF]^i \cdot [M]^j$$

Modulator present at highest levels
Modulator present at lowest levels
-> Suggests M is an activator

---

---

[← 15 slides Part 03 —](03-15-slides-part-03.md) · [Up: contents](index.md) · [Filters →](05-filters.md)
