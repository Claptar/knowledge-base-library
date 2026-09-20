---
title: GWAS analysis can identify human variants associated with disease (L20)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/01-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# GWAS analysis can identify human variants associated with disease (L20)

Figure 4 | Genome-wide scan for seven diseases. For each of seven diseases $-\log_{10}$ of the trend test $P$ value for quality-control-positive SNPs, excluding those in each disease that were excluded for having poor clustering after visual inspection, are plotted against position on each chromosome. Chromosomes are shown in alternating colours for clarity, with $P$ values $< 1 \times 10^{-5}$ highlighted in green. All panels are truncated at $-\log_{10}(P\,\text{value}) = 15$, although some markers (for example, in the MHC in T1D and RA) exceed this significance threshold.

Courtesy of Macmillan Publishers Limited. Used with permission.
Burton, Paul R., David G. Clayton, et al. "Genome-wide Association Study of 14,000 Cases of Seven Common Diseases and 3,000 Shared Controls." *Nature* 447, no. 7145 (2007): 661-78.
Nature Vol 447 | 7 June 2007 | doi:10.1038/nature05911

---

* L12 - Introduction to Protein Structure; Structure Comparison & Classification
* L13 - Predicting protein structure
* L14 - Predicting protein interactions
* L15 - Gene Regulatory Networks
* L16 - Protein Interaction Networks
* L17 - Computable Network Models

---

## Modeling Scales

$$U_{bond} = \sum_{bonds} K_b (b - b^0)^2$$

### Atom
### Protein
### Network

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Barabasi, Albert-László, Natali Gulbahce, et al. "Network Medicine: A Network-based Approach to Human Disease." *Nature Reviews Genetics* 12, no. 1 (2011): 56-68.

---

## Predicting Protein Structure (L13)

| Chignolin | Trp-cage | BBA | Villin |
| :---: | :---: | :---: | :---: |
| 106 $\mu$s | 208 $\mu$s | 325 $\mu$s | 125 $\mu$s |
| cln025 1.0 Å 0.6 $\mu$s | 2JOF 1.4 Å 14 $\mu$s | 1FME 1.6 Å 18 $\mu$s | 2F4K 1.3 Å 2.8 $\mu$s |

| WW domain | NTL9 | BBL | Protein B |
| :---: | :---: | :---: | :---: |
| 1137 $\mu$s | 2936 $\mu$s | 429 $\mu$s | 104 $\mu$s |
| 2F21 1.2 Å 21 $\mu$s | 2HBA 0.5 Å 29 $\mu$s | 2WXC 4.8 Å 29 $\mu$s | 1PRB 3.3 Å 3.9 $\mu$s |

| Homeodomain | Protein G | $\alpha$3D | $\lambda$-repressor |
| :---: | :---: | :---: | :---: |
| 327 $\mu$s | 1154 $\mu$s | 707 $\mu$s | 643 $\mu$s |
| 2P6J 3.6 Å 3.1 $\mu$s | 1MI0 1.2 Å 65 $\mu$s | 2A3D 3.1 Å 27 $\mu$s | 1LMB 1.8 Å 49 $\mu$s |

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Lindorff-Larsen, Kresten, Stefano Piana, et al. "How Fast-folding Proteins Fold." *Science* 334, no. 6055 (2011): 517-20.

---

## Predicting Protein Structure

## Man vs. Machine (L13)

### The New York Times

#### In a Video Game, Tackling the Complexities of Protein Folding
By JOHN MARKOFF
Published: August 9, 2010

Gamers 1, computer 0.

In a match that pitted video game players against the best known computer program designed for the task, the gamers outperformed the software in figuring out how 10 proteins fold into their three-dimensional configurations.

ANTON

© The ACM. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Shaw, David E., Martin M. Deneroff, et al. "Anton, A Special-purpose Machine for Molecular Dynamics Simulation." *Communications of the ACM* 51, no. 7 (2008): 91-7.

© The New York Times Company. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Markoff, John. "In a Video Game, Tackling the Complexities of Protein Folding." *The New York Times*, 2010.

---

## Predicting Interactions (L14)

Rad52
Cdk2
Cks1
CycA
From PDB
ERCC1
From PDB
p27
TFIIH (p62 subunit)
Mdm2

N. Tuncbag Courtesy of Nurcan Tuncbag, Ozlem Keskin and Attila Gursoy. Used with permission.

---

## Gene Regulatory Networks (L15)

Courtesy of Elsevier B.V. Used with permission.
Source: Sumazin, Pavel, Xuerui Yang, et al. "An Extensive MicroRNA-mediated Network of RNA-RNA Interactions Regulates Established Oncogenic Pathways in Glioblastoma." *Cell* 147, no. 2 (2011): 370-81.

---

## Interaction Networks (L16)

* Cell polarity
* Cell structure
* Cell wall maintenance
* Mitosis
* DNA synthesis
* Chromosome structure
* DNA repair
* Unknown
* Others

© Annual Reviews. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Dixon, Scott J., Michael Costanzo, et al. "Systematic Mapping of Genetic Interaction Networks." *Annual Review of Genetics* 43 (2009): 601-25.

Dixon et al. (2009) Annual Review of Genetics Vol. 43: 601-625
(doi:10.1146/annurev.genet.39.073003.114751)

---

## Computable Models (L17)

Courtesy of the authors. License: CC-BY.
Source: Guziolowski, Carito, Santiago Videla, et al. "Exhaustively Characterizing Feasible Logic Models of a Signaling Network using Answer Set Programming." *Bioinformatics* 30, no. 13 (2014): 1942-2.

Guziolowski C et al. *Bioinformatics* 2013;29:2320-2326

---

| Course | Project | AI problems |
| :---: | :---: | :---: |
| 7.36/20.390/6.802 | NO | NO |
| 7.91/20.490/HST.506 | YES | NO |
| 6.874 | YES | YES |

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Computational Genetics Module](02-computational-genetics-module.md) · [Up: contents](index.md)
