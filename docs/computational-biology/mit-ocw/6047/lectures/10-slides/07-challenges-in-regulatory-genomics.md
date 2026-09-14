---
title: Challenges in regulatory genomics
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Challenges in regulatory genomics

**Source:** `lectures/10-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

TFs: Homology to TFs/domains TFs: Selex, DIP-Chip, Protein-Binding-Microarrays miRNAs: Evolutionary signatures miRNAs: Evolutionary/structural signatures miRNAs: Experimental cloning miRNAs: Experimental cloning of 5’-ends

TFs/miRNAs: _De novo_ comparative discovery** Motif Sequence specificity TFs: Enrichment in co-regulated genes/ bound regions ** TFs/miRNAs: Evolutionary signatures** miRNAs: Composition/folding

TFs: Mass Spec (difficult)

Regulator TF/miRNA

Network analysis (next lecture) Targets TFs: ChIP-Chip/ChIP-Seq Functional instances

TFs: ChIP-Chip/ChIP-Seq TFs/miRs: Perturbation response

* = Covered in today’s lecture

81

###### **Recitation tomorrow:** **_in vitro_ motif identification**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Courtesy of the authors. Used with permission. Source: Ray, Partha, and Rebekah R. White. "Aptamers for targeted drug delivery.“ Pharmaceuticals 3, no. 6 (2010): 1761-1778.

**SELEX (Systematic Evolution of Ligands by Exponential Enrichment; Klug & Famulok, 1994)**

**PBMs (Protein binding microarrays; Mukherjee, 2004) Double stranded DNA arrays**

- **PBMs: Protein binding microarrays**

- • **SELEX: Selectionbased motif identiifcation**

- **De Bruijn graphs to generate PBM probes**

- • **From k-mers to motifs**

- • **Gapped motifs**

- **Degenerate motifs and DNA bending (DNA shape)**

- **Relaxing independence assumptions in PWMs**

82

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix

– M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

- – Validation of discovered motifs: functional datasets

- 5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

- – Foreground vs. background. Real vs. control motifs.

83

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Test 3: Upstream vs. Downstream](06-test-3-upstream-vs-downstream.md) · [Up: contents](index.md)
