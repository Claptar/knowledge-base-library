---
title: PAM vs. BLOSUM
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# PAM vs. BLOSUM

### PAM
- Evolutionary time measured in Percent Accepted Mutations (PAMs)
- One PAM: 1% of the residues have changed, averaged over all 20 amino acids.
- To get the relative frequency of each type of mutation, count the times it was observed in a database of multiple sequence *global* alignments
- The PAM1 is the matrix calculated from comparisons of sequences with no more than 1% divergence
- Mutation frequencies assume a Markov model of evolution. Other matrices derived from PAM1:
  PAM250 ~ (PAM1)$^{250}$

### BLOSUM
- BLOSUM matrices are based on *local* alignments
- BLOSUM 62 is a matrix calculated from alignment of sequences with ~62% identity.
- BLOSUM matrices are based on observed alignments; unlike PAM, they are not extrapolated from comparisons of closely related proteins
- BLOSUM 62 is the default matrix in BLAST. It's tailored for comparisons of moderately distant proteins.
- Alignment of more distant proteins may be more accurate with a different matrix based on substitutions observed in more distantly evolved proteins

-See Nat. Biotech. 2 page primer for more in-depth discussion of BLOSUM62: http://selab.janelia.org/publications/Eddy-ATG2/Eddy-ATG2-reprint.pdf

---

## Jukes-Cantor model

- the number of observed differences between two homologous sequences is smaller than the actual number of changes that have occurred, due to reversions (e.g. $A \to G \to A$)
  - can underestimate the genetic distance between the sequences
  - How to compensate? need some model of how mutations occur

- Jukes-Cantor model assumes that all mutations are equally likely and occur with rate $\alpha$; if this is true, then you can apply the following correction:

$$K = -\frac{3}{4} \ln \left[ 1 - \frac{4}{3} P \right]$$

$P$ = observed fraction sites that differ
$K$ = actual number of substitutions

- This is very simple; other models are much more complex (e.g. Kimura, which has transitions $C \leftrightarrow T$ and $A \leftrightarrow G$ occurring more frequently than transversions $R \leftrightarrow Y$ and $Y \leftrightarrow R$).

---

---

[← 7.36/7.91 recitation](01-7-36-7-91-recitation.md) · [Up: contents](index.md) · [Positive / Negative Selection →](03-positive-negative-selection.md)
