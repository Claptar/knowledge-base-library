---
title: Genomic Analysis Module
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/01-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Genomic Analysis Module

### Next Generation Sequencing

* L5 – How to index and process millions of DNA sequence reads using the Burrows-Wheeler Transform (BWT) to build genome indexes
* L6 – How to assemble a reference genome sequence from $10^8$ short sequence reads
* L7 – How to discovery where regulatory proteins occupy the genome (ChIP-seq analysis)
* L8 – How to measure RNA expression and isoforms using high-throughput DNA sequencing (RNA-seq analysis)

---

## Reads aligned to a reference genome for interpretation (L5)

Reference Genome Sequence

35 bp identified

330 - 430 bp unknown sequence

35 bp identified

Courtesy of Suspencewl on wikipedia. Image is in the public domain.
http://en.wikipedia.org/wiki/Genomics

---

## Reference genomes are assembled from millions of short reads (L6)

a) Multiple copies of genome
b) Sheared random fragments
c) Size fractionated fragments
d) Reads
e) Contigs
f) Scaffolds (Super contigs)

Courtesy of Shinichi Morishita. Used with permission.
http://www.k.u-tokyo.ac.jp/pros-e/person/shinichi morishita/shinichi morishita.htm

---

## ChIP-seq reveals where key genomic regulators bind to the genome (L7)

$\text{chr3} \times 1,000$
34837 | 34838 | 34839 | 34840 | 34841 | 34842 | 34843 | 34844 | 34845 | 34846

Oct4 IP

Whole-Cell Extract

Sox2

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## RNA-seq reveals both RNA expression levels and isoforms (L8)

Reads over exons

Smug1

Junction reads (split between exons)

Smug1, NM_027885

---

---

[Up: contents](index.md) · [Computational Genetics Module →](02-computational-genetics-module.md)
