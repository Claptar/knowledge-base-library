---
title: Biclustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Biclustering

- Simultaneous clustering of rows and columns of a matrix
- Bicluster – subset of rows which exhibit similar behavior across a subset of columns, or vice versa

---

Fig. 4. Bicluster structure. (a) Single bicluster, (b) exclusive row and column biclusters, (c) checkerboard structure, (d) exclusive rows biclusters, (e) exclusive columns biclusters, (f) nonoverlapping biclusters with tree structure, (g) nonoverlapping nonexclusive biclusters, (h) overlapping biclusters with hierarchical structure, and (i) arbitrarily positioned overlapping biclusters.

© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Madeira, Sara C., and Arlindo L. Oliveira. "Biclustering Algorithms for Biological Data Analysis: A Survey." *Computational Biology and Bioinformatics, IEEE/ACM Transactions on* 1, no. 1 (2004): 24-45.

---

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Gkountela, Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." *Nature Cell Biology* 15, no. 1 (2013): 113-22.

---

## Biology Review

---

## Selection

- Negative selection (purifying/natural selection) – removal of deleterious traits
- Positive selection – increases prevalence of adaptive traits
- Thinking about selection happening at different levels
  - *Protein level*: Sequence -> Structure -> Function
  - *RNA level*: splicing, degradation/processing (NMD)
  - *DNA level*: DNA-protein binding sites

---

## Synonymous/Non-synonymous mutations

- Redundancy built into the genetic code
- Synonymous – one base changes for another in an exon, but the resulting amino acid sequence is unchanged
- Non-synonymous – new AA
- Can affect splicing, mRNA processing - so may not be silent

Image by MIT OpenCourseWare.

---

## Side-chain biochemistry

- Amino acids classified by properties of side chains
  - Grouped by general properties
- Substitutions of amino acid with another of similar chemical properties may conserve protein function

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Side chain size (Trp – W)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Disulfide bond

- Important in protein folding – holds two distant portions of protein together
- Occurs between Cys residues

---

## Next-generation sequencing

- Sequencing is always of DNA
  - Need to convert RNA to DNA by *reverse transcription* (RT)
- Illumina is current leader in the field
  - 8 lanes on a flow cell
  - Each lane can sequence 200 million 100bp reads – 20 Gbps!
  - Can sequence multiple samples per lane by barcoding
  - Requires (heterogeneous) population of cells to get enough DNA for sample
- Single cell sequencing applications are becoming more common (RNAseq)
- Single molecule technologies are still being developed – PacBio

---

## Alignment

---

## Alignment

$$F(i, j) = \max \begin{cases} F(i-1, j-1) + s(x_i, y_j), \\ F(i-1, j) - d, \\ F(i, j-1) - d. \end{cases}$$

$$F(i, j) = \max \begin{cases} 0, \\ F(i-1, j-1) + s(x_i, y_j), \\ F(i-1, j) - d, \\ F(i, j-1) - d. \end{cases}$$

Biological Sequence Analysis - Durbin

---

## Local alignment example

Do a local alignment between these using PAM250 and gap penalty -2:

AWEK
FWEF

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Local alignment solution

| | Gap | A | W | E | K |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Gap** | 0 | 0 | 0 | 0 | -8 |
| **F** | 0 | 0 | 0 | 0 | 0 |
| **W** | 0 | 0 | 17 | 15 | 13 |
| **E** | 0 | 0 | 15 | 21 | 19 |
| **F** | 0 | 0 | 13 | 19 | 17 |

alignment:
W E
W E

---

## Global alignment solution

| | Gap | A | W | E | K |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Gap** | 0 | -2 | -4 | -6 | -8 |
| **F** | -2 | -4 | -2 | -4 | -6 |
| **W** | -4 | -6 | 13 | 11 | 9 |
| **E** | -6 | -4 | -6 | 17 | 11 |
| **F** | -8 | -6 | -4 | 15 | 12 |

alignment:
A W E K
F W E F

| | Global | Semiglobal | Local (gapped) |
| :--- | :---: | :---: | :---: |
| **Penalties at edges?** | Yes | No | No |
| **Reset to 0 instead of including negative entries?** | No | No | Yes |
| **End of alignment** | Bottom right entry | Highest score entry in bottom row or rightmost column | Highest score entry in matrix |

## Reminders

- Pset 1 posted – due Feb 20^th (no extra problem)
- Pset 2 posted – Due Mar 13^th
- Project teams due – Feb 25^th
  - Interests and background directory has been posted
- Lecture videos will be posted on MITx soon – next week?

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802 / 6.874 / HST.506 Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Hierarchical clustering](02-hierarchical-clustering.md) · [Up: contents](index.md)
