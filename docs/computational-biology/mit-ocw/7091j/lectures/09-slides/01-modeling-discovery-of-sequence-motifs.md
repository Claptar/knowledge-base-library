---
title: Modeling & Discovery of Sequence Motifs
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Modeling & Discovery of Sequence Motifs

7.91 / 20.490 / 6.874 / HST.506
7.36 / 20.390 / 6.802

C. Burge Lecture #9
Mar. 6, 2014

---

- Motif Discovery with Gibbs Sampling Algorithm
- Information Content of a Motif
- Parameter Estimation for Motif Models (+ others)

### Background for today:
NBT Primers on Motifs, Motif Discovery. Z&B Ch. 6.

Optional: Lawrence Gibbs paper, Bailey & Elkan MEME paper

### For Tuesday:
NBT primer on HMMs, Z&B on HMMs (various pp.)

Rabiner tutorial on HMMs

---

## What is a (biomolecular) sequence motif?

A pattern common to a set of DNA, RNA or protein sequences that share a common biological property, such as functioning as binding sites for a particular protein

### Ways of representing motifs
- Consensus sequence
- Regular expression
- Weight matrix/PSPM/PSSM
- More complicated models

---

## Where do motifs come from?

- Sequences of known common function
- Cross-linking/pulldown experiments
- in vitro binding / SELEX experiments
- Multiple sequence alignments / comparative genomics

### Why are they important?

- Identify proteins, DNAs or RNAs that have a specific property
- Can be used to infer which factors regulate which genes
- Important for efforts to model gene expression

---

## Examples of Protein Sequence Motifs

$\text{CX}_2\text{CX}_4\text{HX}_4\text{C}$

Zinc finger (DNA binding)

Ericsson et al. Genet. Mol. Res. 2006

Phosphorylation sites
(*Arabidopsis* SRPK4)

de la Fuente van Bentem et al. NAR 2006

---

## Core Splicing Motifs (Human)

5' splice site

branch site

3' splice site

---

## Weight Matrix with Background Model

5' splice site
motif (+)

| Pos | -3 | -2 | -1 | ... | +5 | +6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Con: | C | A | G | ... | G | T |
| A | 0.3 | 0.6 | 0.1 | ... | 0.1 | 0.1 |
| C | 0.4 | 0.1 | 0.0 | ... | 0.1 | 0.2 |
| G | 0.2 | 0.2 | 0.8 | ... | 0.8 | 0.2 |
| T | 0.1 | 0.1 | 0.1 | ... | 0.0 | 0.5 |

Background (-)

| Pos | Generic |
| :--- | :--- |
| A | 0.25 |
| C | 0.25 |
| G | 0.25 |
| T | 0.25 |

$S = S_1 \, S_2 \, S_3 \, S_4 \, S_5 \, S_6 \, S_7 \, S_8 \, S_9$

$$\text{Odds Ratio: } R = \frac{P(S|+)}{P(S|-)} = \frac{P_{-3}(S_1) P_{-2}(S_2) P_{-1}(S_3) \cdots P_5(S_8) P_6(S_9)}{P_{\text{bg}}(S_1) P_{\text{bg}}(S_2) P_{\text{bg}}(S_3) \cdots P_{\text{bg}}(S_8) P_{\text{bg}}(S_9)}$$

Background model homogenous, assumes independence

---

## Ways to describe a motif

Common motif adjectives:

exact/precise *versus* degenerate

strong *versus* weak (good *versus* lousy)

high information content *versus* low information content

low entropy *versus* high entropy

---

## Statistical (Shannon) Entropy

Motif probabilities: $p_k \quad (k = \text{A, C, G, T})$

Background probabilities: $q_k = \frac{1}{4} \quad (k = \text{A, C, G, T})$

$$H(q) = -\sum_{k=1}^4 q_k \log_2 q_k = ? \quad 2 \text{ bits}$$

$$H(p) = -\sum_{k=1}^4 p_k \log_2 p_k \quad (> \text{ or } < H(q)?)$$

Log base 2 gives entropy/information in 'bits'

Relation to Boltzmann entropy: $S = k_B \ln(\Omega)$

---

## Information, uncertainty, entropy

Claude Shannon on what name to give to the "measure of uncertainty" or attenuation in phone-line signals (1949):

"My greatest concern was what to call it. I thought of calling it 'information', but the word was overly used, so I decided to call it 'uncertainty'. When I discussed it with John von Neumann, he had a better idea. Von Neumann told me, 'You should call it entropy, for two reasons. In the first place your uncertainty function has been used in statistical mechanics under that name, so it already has a name. In the second place, and more important, nobody knows what entropy really is, so in a debate you will always have the advantage.'"

source: Wikipedia

---

## Information Content of a DNA Motif

Information at position $j$: $I_j = H_{\text{before}} - H_{\text{after}}$

Motif probabilities: $p_k \quad (k = \text{A, C, G, T})$

Background probabilities: $q_k = \frac{1}{4} \quad (k = \text{A, C, G, T})$

$$I_j = -\sum_{k=1}^4 q_k \log_2 q_k - \left( -\sum_{k=1}^4 p_k \log_2 p_k \right) = 2 - H_j$$

**If positions in the motif are independent, then**

$$I_{\text{motif}} = \sum_{j=1}^w I_j = 2w - H_{\text{motif}} \quad (\text{for motif of width } w \text{ bases})$$

Otherwise, this relation does not hold in general.

Log base 2 gives entropy/information in 'bits'

---

---

[Up: contents](index.md) · [The Motif Finding Problem →](02-the-motif-finding-problem.md)
