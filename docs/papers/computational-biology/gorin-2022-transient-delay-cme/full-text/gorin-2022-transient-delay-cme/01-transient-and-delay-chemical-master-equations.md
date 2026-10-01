---
title: Transient and delay chemical master equations
source: https://doi.org/10.1101/2022.10.17.512599/
source_file: sources/papers/gorin-2022-transient-delay-cme/gorin-2022-transient-delay-cme.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-2022-transient-delay-cme.pdf` from [papers/gorin-2022-transient-delay-cme](https://doi.org/10.1101/2022.10.17.512599/) — papers · gorin-2022-transient-delay-cme, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Transient and delay chemical master equations

Gennady Gorin$^1$, Shawn Yoshida$^{1,2}$, and Lior Pachter$^{2,3,*}$

$^1$Division of Chemistry and Chemical Engineering, California Institute of Technology, Pasadena, CA, 91125
$^2$Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA, 91125
$^3$Department of Computing and Mathematical Sciences, California Institute of Technology, Pasadena, CA, 91125
*Correspondence: lpachter@caltech.edu

**Abstract** The serial nature of reactions involved in the RNA life-cycle motivates the incorporation of delays in models of transcriptional dynamics. The models couple a bursty or switching promoter to a fairly general set of Markovian or deterministically delayed monomolecular RNA interconversion reactions with no feedback. We provide numerical solutions for the RNA copy number distributions the models induce, and solve several systems with splicing and degradation. An analysis of single-cell and single-nucleus RNA sequencing data using these models reveals that the kinetics of nuclear export do not appear to require invocation of a non-Markovian waiting time.

**Keywords** Chemical master equations, delay processes, single-cell RNA sequencing, model identification, stochastic simulation

**Acknowledgments** G.G. thanks Dr. John J. Vastola and Catherine Felce for valuable discussions. G.G. and L.P. were partially funded by the National Institutes of Health grant U19MH114830. A part of the reported results were obtained during a Data Sciences Co-op with Celsius Therapeutics, Inc. The DNA and RNA illustrations are derived from the DNA Twemoji by Twitter, Inc., used under CC-BY 4.0.

**Code availability** All scripts used to process data and generate the figures are located at https://github.com/pachterlab/GYP_2022. The raw count matrices, as well as the outputs of the *Monod* pipeline, are available on Zenodo (Gorin, 2022).

**Statements and Declarations** The authors declare no competing interests.

---

[Up: contents](index.md) · [1 INTRODUCTION →](02-1-introduction.md)
