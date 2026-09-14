---
title: TABLE OF CONTENTS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# TABLE OF CONTENTS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>iii|
|---|
|Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>v|
|Published Content and Contributions . . . . . . . . . . . . . . . . . . . . . .<br>vi|
|Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii|
|List of Illustrations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>xi|
|List of Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xxv|
|Chapter I: Introduction and outline . . . . . . . . . . . . . . . . . . . . . . .<br>1|
|Chapter II: Technologies, desiderata, and axioms<br>. . . . . . . . . . . . . . .<br>3|
|2.1 The two perspectives on the negative binomial distribution . . . . . .<br>3|
|2.2 Motivations for mechanistic models . . . . . . . . . . . . . . . . . .<br>8|
|2.3 Technologies and axioms<br>. . . . . . . . . . . . . . . . . . . . . . .<br>11|
|Chapter III: Mathematical tools and preliminaries . . . . . . . . . . . . . . .<br>14|
|3.1 Common mathematical objects, distributions, and identities . . . . .<br>14|
|3.2 Model selection criteria . . . . . . . . . . . . . . . . . . . . . . . .<br>23|
|3.3 Distance measures . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>24|
|Chapter IV: Stochastic models and solutions . . . . . . . . . . . . . . . . . .<br>25|
|4.1 Motivations for model classes . . . . . . . . . . . . . . . . . . . . .<br>25|
|4.2 Models of RNA processing and transcriptional noise . . . . . . . . .<br>26|
|<br>4.3 Challenges of broader model classes<br>. . . . . . . . . . . . . . . . .<br>36|
|4.4 Models of the experimental process . . . . . . . . . . . . . . . . . .<br>38|
|4.5 A unified framework for scRNA-seq stochasticity . . . . . . . . . . .<br>44|
|4.6 Commonly encountered processes . . . . . . . . . . . . . . . . . . .<br>44|
|Chapter V: Computational considerations<br>. . . . . . . . . . . . . . . . . . .<br>48|
|5.1 Key challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>48|
|5.2 Special function approximations . . . . . . . . . . . . . . . . . . . .<br>49|
|5.3 Neural approximations . . . . . . . . . . . . . . . . . . . . . . . . .<br>53|
|5.4 _Monod_ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>58|
|5.5 Simulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>63|
|Chapter VI: Snapshot inference . . . . . . . . . . . . . . . . . . . . . . . . .<br>69|
|6.1 Critical analysis of RNA velocity . . . . . . . . . . . . . . . . . . .<br>69|
|6.2 Self-consistent snapshot inference . . . . . . . . . . . . . . . . . . .<br>77|
|Chapter VII: Model identification and selection . . . . . . . . . . . . . . . .<br>82|
|7.1 The role of multimodal data in inference<br>. . . . . . . . . . . . . . .<br>82|
|7.2 The identification of transcriptional driving processes<br>. . . . . . . .<br>88|
|7.3 RNA processing . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>91|
|Chapter VIII: Sequencing model specification . . . . . . . . . . . . . . . . .<br>95|
|8.1 Empty droplets . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>95|
|8.2 Length biases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>98|
|8.3 Technology differences . . . . . . . . . . . . . . . . . . . . . . . . . 100|


|8.4|x<br> Limitations of normalization procedures<br>. . . . . . . . . . . . . . . 104|
|---|---|
|Chapter     f|IX: Determination of biological differences . . . . . . . . . . . . . . 110|
|9.1|The role of multimodal data in differential expression<br>. . . . . . . . 110|
|9.2|Mechanistic differential expression<br>. . . . . . . . . . . . . . . . . . 111|
|9.3|Genome-wide noise modulation . . . . . . . . . . . . . . . . . . . . 115|
|Chapter|X: Modeling multi-gene systems . . . . . . . . . . . . . . . . . . . . 117|
|10.1|Key goals and context . . . . . . . . . . . . . . . . . . . . . . . . . 117|
|10.2|Biophysical constraints on “fast” transcript–transcript covariation . . 120|
|10.3|Multimodal variational autoencoder models for “slow” covariation<br>. 124|
|Chapter|XI: Modeling further classes of multiomic data . . . . . . . . . . . . 133|
|11.1|Protein velocity and acceleration<br>. . . . . . . . . . . . . . . . . . . 133|
|11.2|Chromatin accessibility<br>. . . . . . . . . . . . . . . . . . . . . . . . 135|
|11.3|Spatial transcriptomics . . . . . . . . . . . . . . . . . . . . . . . . . 137|
|Chapter|XII: Discussion and conclusion . . . . . . . . . . . . . . . . . . . . 139|
|12.1|Future challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139|
|12.2|Concluding notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140|
|Bibliogr|aphy<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|
|Append|ix A: Supplementary generating function derivations . . . . . . . . . 186|
|A.1|The full master equation . . . . . . . . . . . . . . . . . . . . . . . . 187|
|A.2|Fully discrete master equation terms . . . . . . . . . . . . . . . . . . 188|
|A.3|Fully continuous master equation terms . . . . . . . . . . . . . . . . 190|
|A.4|Mixed master equation terms<br>. . . . . . . . . . . . . . . . . . . . . 191|
|A.5|Converting the master equation to a partial differential equation . . . 192|
|A.6|Representing the PDE in matrix form . . . . . . . . . . . . . . . . . 195|
|A.7|Regulation extensions . . . . . . . . . . . . . . . . . . . . . . . . . 200|
|A.8|Stochastic process identities . . . . . . . . . . . . . . . . . . . . . . 203|
|Append|ix B: Qualitative discussion of sequencing procedures and their caveats212|
|B.1|Notes on nomenclature and binary assignment . . . . . . . . . . . . 212|
|B.2|Notes on ambiguity<br>. . . . . . . . . . . . . . . . . . . . . . . . . . 215|
|B.3|Notes on imputation and reconstruction . . . . . . . . . . . . . . . . 218|
|B.4|Notes on graph methods . . . . . . . . . . . . . . . . . . . . . . . . 219|


xi

---

[← PUBLISHED CONTENT AND CONTRIBUTIONS](04-published-content-and-contributions.md) · [Up: contents](index.md) · [LIST OF ILLUSTRATIONS →](06-list-of-illustrations.md)
