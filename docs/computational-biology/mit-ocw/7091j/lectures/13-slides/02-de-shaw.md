---
title: DE Shaw
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# DE Shaw

- Lindorff-Larsen et al. (2011) *Science*
- Simulate protein folding.
- Built a specialized supercomputer
  - Hundreds of application specific integrated circuits

© The ACM. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Shaw, David E., Martin M. Deneroff, et al. "Anton, A Special-purpose Machine for Molecular Dynamics Simulation." *Communications of the ACM* 51, no. 7 (2008): 91-7.

---

| | | | |
|---|---|---|---|
| Chignolin $106\ \mu\text{s}$
cln025 $1.0\ \text{Å}\quad 0.6\ \mu\text{s}$ | Trp-cage $208\ \mu\text{s}$
2JOF $1.4\ \text{Å}\quad 14\ \mu\text{s}$ | BBA $325\ \mu\text{s}$
1FME $1.6\ \text{Å}\quad 18\ \mu\text{s}$ | Villin $125\ \mu\text{s}$
2F4K $1.3\ \text{Å}\quad 2.8\ \mu\text{s}$ |
| WW domain $1137\ \mu\text{s}$
2F21 $1.2\ \text{Å}\quad 21\ \mu\text{s}$ | NTL9 $2936\ \mu\text{s}$
2HBA $0.5\ \text{Å}\quad 29\ \mu\text{s}$ | BBL $429\ \mu\text{s}$
2WXC $4.8\ \text{Å}\quad 29\ \mu\text{s}$ | Protein B $104\ \mu\text{s}$
1PRB $3.3\ \text{Å}\quad 3.9\ \mu\text{s}$ |
| Homeodomain $327\ \mu\text{s}$
2P6J $3.6\ \text{Å}\quad 3.1\ \mu\text{s}$ | Protein G $1154\ \mu\text{s}$
1MIO $1.2\ \text{Å}\quad 65\ \mu\text{s}$ | $\alpha\text{3D}$ $707\ \mu\text{s}$
2A3D $3.1\ \text{Å}\quad 27\ \mu\text{s}$ | $\lambda$-repressor $643\ \mu\text{s}$
1LMB $1.8\ \text{Å}\quad 49\ \mu\text{s}$ |

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Lindorff-Larsen, Kresten, Stefano Piana, et al. "How Fast-folding Proteins Fold." *Science* 334, no. 6055 (2011): 517-20.

---

## FoldIT Game

### The New York Times

#### In a Video Game, Tackling the Complexities of Protein Folding

By JOHN MARKOFF
Published: August 9, 2010

Gamers 1, computer 0.

PUZZLE University of Washington scientists developed Foldit, a free online game that drew thousands of players. "It's like trying to solve a million-sided Rubik's Cube while it also spins at 10,000 r.p.m.," a player wrote in a Web forum.

In a match that pitted video game players against the best known computer program designed for the task, the gamers outperformed the software in figuring out how 10 proteins fold into their three-dimensional configurations.

Proteins are essentially biological nanomachines that carry out myriad functions in the body, and biologists have long sought to understand how the long chains of

© The New York Times Company. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Markoff, John. "In a Video Game, Tackling the Complexities of Protein Folding." *The New York Times.* August 4, 2010.

---

## Predictions

### So far: protein structure

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Lindorff-Larsen, Kresten, Stefano Piana, et al. "How Fast-folding Proteins Fold." *Science* 334, no. 6055 (2011): 517-20.

### Next: protein interactions

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Prediction Challenges

- Predict effect of point mutations
- Predict structure of complexes
- Predict all interacting proteins

---

## Community-wide evaluation of methods for predicting the effect of mutations on protein–protein interactions

DOI: 10.1002/prot.24356

"Simple" challenge:
Starting with known structure of a complex: predict how much a mutation changes binding affinity.

**Figure 1**
The structures of (A) HB36 (B) HB80 in complex with HA (blue) which were provided to participants. Residues probed in the deep sequencing enrichment experiment are in orange; the remainder are in grey. Residues at the interface are represented as sticks.

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community-wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." *Proteins: Structure, Function, and Bioinformatics* 81, no. 11 (2013): 1980-7.

---

## Community-wide evaluation of methods for predicting the effect of mutations on protein–protein interactions

DOI: 10.1002/prot.24356

- All possible single-point mutations at each of 53 and 45 positions for two proteins.
- Expressed on yeast
- High-throughput assay based on sequencing used to estimate changes in binding affinity

**Figure 1**
The structures of (A) HB36 (B) HB80 in complex with HA (blue) which were provided to participants. Residues probed in the deep sequencing enrichment experiment are in orange; the remainder are in grey. Residues at the interface are represented as sticks.

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community-wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." *Proteins: Structure, Function, and Bioinformatics* 81, no. 11 (2013): 1980-7.

---

---

[← Predicting Protein Structure](01-predicting-protein-structure.md) · [Up: contents](index.md) · [13 slides Part 03 — →](03-13-slides-part-03.md)
