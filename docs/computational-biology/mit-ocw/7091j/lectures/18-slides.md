---
title: Analysis of Chromatin Structure
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/18-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Analysis of Chromatin Structure

### Lecture 18

David K. Gifford

Massachusetts Institute of Technology

---

## Today’s Narrative Arc

1. Using computational methods we can break the epigenetic “code” that describes the function and state of genome elements. Epigenetic state regulates gene function without changing primary DNA sequence. Epigenetic state includes histone marks, DNA methylation, and chromatin openness.
2. We can estimate the protein occupancy of the genome and discover pioneer factors with DNase-seq via computational methods.
3. We can map enhancers to their regulatory targets with the computational analysis of ChIA-PET data (and similar technologies)

---

## Today’s Computational Methods

1. Dynamic Bayesian Networks
2. Factor binding classification using a log likelihood ratio
3. Hypergeometric distribution

---

Chromatin organization has multiple structural layers and organizes chromatin into “domains”

Both DNA methylation and chromatin marks contain important functional information

OFF | ON
--- | ---
DNA sequence, DNA methylation: Me, Me, Me |
Nucleosomes |
Histone modifications,

## Dominant negative pioneers reduce proximal DNase HS

We created dominant negative versions of the NFYA and Nrf1 pioneers and measured DNase accessibility at native NFYA and Nrf1 sites after induction of dominant negatives.

Highly HS 2.5
1.5
Non-HS 1

\* $p < 0.01$
wt mES
DN NFYA
DN Nrf1

NFYA sites
Nrf1 sites

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Sherwood, Richard I., Tatsunori Hashimoto, et al. "Discovery of Directional and Nondirectional Pioneer Transcription Factors by Modeling DNase Profile Magnitude and Shape." *Nature Biotechnology* 32, no. 2 (2014): 171-8.

---

## Dominant negative NFYA reduces binding of downstream c-Myc

- Relative c-Myc ChIP-qPCR over genomic binding regions with either **NFYA** / **c-Myc** or **c-Myc** / **NFYA** to test asymmetry

Strong ChIP 2.5
1.5
No ChIP 1

\* $p < 0.01$
wt mES
DN NFYA

Predicted pioneering sites
Predicted non-pioneering sites

---

## Pioneers appear to be conserved between human/mouse

$r^2 = 0.84$

Chromatin Opening Index (mESC lineage) $\rightarrow$
Chromatin Opening Index (K562) $\rightarrow$

---

## Overview of Results

- PIQ is highly accurate at predicting transcription factor (TF) binding from DNase-seq data
- PIQ can identify pioneer factors regulate proximal chromatin opening and TF binding
- Certain pioneer TFs are directional
- Settlers factors follow pioneer factor binding and loss of pioneer binding causes chromatin to return to a closed state

---

## Today’s Narrative Arc

1. We can break the epigenetic "code" that describes the function and state of genome elements using computational methods. Epigenetic state regulates gene function without changing primary DNA sequence. Epigenetic state includes histone marks, DNA methylation, and chromatin openness.
2. We can estimate the protein occupancy of the genome and discover pioneer factors with DNase-seq via computational methods.
3. **We can map enhancers to their regulatory targets with the computational analysis of ChIA-PET data (and similar technologies)**

---

## Enhancers regulate distal target genes by genome looping

Enhancer
Cohesin
Mediator
Master Regulators
Pol II
Gene

---

## ChIA-PET protocol - After IP of RNA Pol II, sonnication, and ligation, ligation products are sequenced

self-ligation
inter-ligation

The ChIA-PET Protocol

---

## ChIA-PET discovered enhancer linkages

iMN: Lhx3 ChIP-seq
iMN: Pol II ChIA-PET

pMN: Olig2 ChIP-seq
pMN: Pol II ChIA-PET

mES: Sox2 ChIP-seq
mES: Pol II ChIA-PET

Sox2

---

## The significance of observing $I$ inter-ligation events between two binding events $A$ and $B$ can be calculated using a hypergeometric test

Let $I_{A,B}$ be the number of inter-ligation events between binding events $A$ and $B$. Let $c_A$ and $c_B$ be the number of ligation event ends associated with $A$ and $B$, respectively. Let $N$ be the total number of ligation events ends. The null hypothesis assumes that each ligation event end has an equal probability of ligating with any other end. Then, under the null hypothesis:

$$P(I_{A,B} \mid N, c_A, c_B) = \frac{\binom{c_A}{I_{A,B}}\binom{N - c_A}{c_B - I_{A,B}}}{\binom{N}{c_B}}$$

$$p = \sum_{i=I_{A,B}}^{\min\{c_A, c_B\}} P(i \mid N, c_A, c_B)$$

---

## Issues with ChIA-PET

1. High false negative rate. Libraries produced are not complex enough to permit further discovery by additional sequencing.
2. Specific to a protein (RNA Polymerase II in our example)
3. Hi-C and derivatives may solve these problems eventually

---

## Estimating total events from overlap

Imagine we perform two biological replicates of an experiment and obtain 1000 events in each, of which 900 are identical

We can use a hypergeometric model to infer how many possible events exist ($N$) given two sample sizes ($m$ and $n$) and an overlap ($k$):

$$\hat{N} = \operatorname{argmax}_N [P(X = k; N, m, n)]$$

Using this model, we predict ~1100 total events

---

## Approximate closed form solution for total number of events

- The ML estimate of $N$ is approximately:

$$\hat{N}(m, n, k) = \frac{mn}{k}$$

- One way to see this is by using the normal approximation of the binomial approximation to the hypergeometric distribution:

$$P(X = k; N, m, n) \approx \text{Binomial}\left(X = k; n = n, p = \frac{m}{N}\right)$$

$$\approx \text{Normal}\left(X = k; \mu = \frac{mn}{N}, \sigma^2 = \frac{mn}{N}\left(1 - \frac{m}{N}\right)\right)$$

---

## Allowing for false positive events

- What if some events in each replicate are false positives? Then we will overestimate the total event count
- We can assume that overlapping (shared) events are true positives and that $(1 - f)$ of the remaining events are false negatives, where $f$ is the true positive rate (TPR)
- This approximation lets us update $m$ and $n$ and apply the same model:

$$m' = (1 - f)(m - k) + k$$
$$n' = (1 - f)(n - k) + k$$

---

## A higher true positive rate estimates more total events with a fixed overlap

- Replicate A had 3811 events, replicate B had 1384 events
- The overlap was 533 events
- Likelihood plots versus $N$ for several true positive rates (TPR):

Total events calculated from biological replicates

- $\text{TPR} = 0.80, \hat{N} = 7180$
- $\text{TPR} = 0.90, \hat{N} = 8482$
- $\text{TPR} = 1.00, \hat{N} = 9896$

Probability vs Events ($N$)

---

## Today’s Narrative Arc

1. Using computational methods we can break the epigenetic "code" that describes the function and state of genome elements. Epigenetic state regulates gene function without changing primary DNA sequence. Epigenetic state includes histone marks, DNA methylation, and chromatin openness.
2. We can estimate the protein occupancy of the genome and discover pioneer factors with DNase-seq via computational methods.
3. We can map enhancers to their regulatory targets with the computational analysis of ChIA-PET data (and similar technologies)

---

## Today’s Computational Methods

1. Dynamic Bayesian Networks
2. Factor binding classification using a log likelihood ratio
3. Hypergeometric distribution

---

## FIN

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 1 of the original](18-slides/figures/p001-1.png)

![Figure from page 1 of the original](18-slides/figures/p001-2.png)

![Figure from page 4 of the original](18-slides/figures/p004-1.jpeg)

![Figure from page 5 of the original](18-slides/figures/p005-1.jpeg)

![Figure from page 6 of the original](18-slides/figures/p006-1.jpeg)

![Figure from page 7 of the original](18-slides/figures/p007-1.jpeg)

![Figure from page 9 of the original](18-slides/figures/p009-2.jpeg)

![Figure from page 11 of the original](18-slides/figures/p011-1.png)

![Figure from page 12 of the original](18-slides/figures/p012-1.jpeg)

![Figure from page 14 of the original](18-slides/figures/p014-1.png)

![Figure from page 14 of the original](18-slides/figures/p014-2.png)

![Figure from page 15 of the original](18-slides/figures/p015-1.jpeg)

![Figure from page 17 of the original](18-slides/figures/p017-1.png)

![Figure from page 18 of the original](18-slides/figures/p018-1.jpeg)

![Figure from page 19 of the original](18-slides/figures/p019-1.jpeg)

![Figure from page 20 of the original](18-slides/figures/p020-1.jpeg)

![Figure from page 21 of the original](18-slides/figures/p021-1.png)

![Figure from page 21 of the original](18-slides/figures/p021-2.png)

![Figure from page 22 of the original](18-slides/figures/p022-1.png)

![Figure from page 22 of the original](18-slides/figures/p022-2.png)

![Figure from page 24 of the original](18-slides/figures/p024-1.png)

![Figure from page 26 of the original](18-slides/figures/p026-1.png)

![Figure from page 28 of the original](18-slides/figures/p028-1.png)

![Figure from page 31 of the original](18-slides/figures/p031-1.png)

![Figure from page 32 of the original](18-slides/figures/p032-1.png)

![Figure from page 33 of the original](18-slides/figures/p033-1.png)

![Figure from page 34 of the original](18-slides/figures/p034-1.png)

![Figure from page 35 of the original](18-slides/figures/p035-1.png)

![Figure from page 36 of the original](18-slides/figures/p036-1.png)

![Figure from page 37 of the original](18-slides/figures/p037-1.png)

![Figure from page 37 of the original](18-slides/figures/p037-9.png)

![Figure from page 38 of the original](18-slides/figures/p038-1.png)

![Figure from page 39 of the original](18-slides/figures/p039-1.png)

![Figure from page 40 of the original](18-slides/figures/p040-20.jpeg)

![Figure from page 40 of the original](18-slides/figures/p040-26.jpeg)

![Figure from page 40 of the original](18-slides/figures/p040-34.png)

![Figure from page 41 of the original](18-slides/figures/p041-1.png)

![Figure from page 42 of the original](18-slides/figures/p042-1.png)

![Figure from page 42 of the original](18-slides/figures/p042-2.png)

![Figure from page 43 of the original](18-slides/figures/p043-1.png)

![Figure from page 46 of the original](18-slides/figures/p046-6.png)

![Figure from page 46 of the original](18-slides/figures/p046-9.png)

![Figure from page 47 of the original](18-slides/figures/p047-1.png)

![Figure from page 47 of the original](18-slides/figures/p047-33.png)

![Figure from page 47 of the original](18-slides/figures/p047-39.png)

![Figure from page 47 of the original](18-slides/figures/p047-61.png)

![Figure from page 47 of the original](18-slides/figures/p047-83.png)

![Figure from page 47 of the original](18-slides/figures/p047-103.png)

![Figure from page 47 of the original](18-slides/figures/p047-108.png)

![Figure from page 48 of the original](18-slides/figures/p048-1.png)

![Figure from page 52 of the original](18-slides/figures/p052-2.png)

![Figure from page 54 of the original](18-slides/figures/p054-1.png)

