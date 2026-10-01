---
title: Introduction
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Introduction

Singe-cell genomics provides a fundamental framework for classifying cell types based on their
molecular profile (Flynn et al., 2023). In order to achieve single-cell resolution, single-cell
assays rely on the assignment of molecules to barcoded containers based on the physical or
logical encapsulation of cells. Following library preparation, libraries are amplified and
sequenced and individual transcripts are identified by their unique molecular identifiers (UMIs)
and cell barcodes. Ideally, the contents of each barcoded container consist of molecules from a
single cell. However, in practice, these assays are subject to several sources of error: ambient
contamination from lysed or damaged cells introduces a background signal; containers may
capture no or multiple cells (multiplets); and bulk contamination adds additional noise during
amplification and sequencing (Luecken and Theis, 2019; Kavaliauskaite and Madsen, 2023;
Griffiths et al., 2018; Farouni et al., 2020; Potapov and Ong, 2017). Notably, containers that
capture no cell can still generate sequenced libraries composed entirely of background RNA.
Although the physical mechanisms of cell partitioning differ between technologies, the resulting
contamination can be described within a common statistical framework.

Sequencing technologies can be classified into three types according to the type of container:
"shell", "cell", or "well" (Booeshaghi et al., 2023) (Fig. 1A). All three of these approaches suffer
from ambient contamination, multiplets, and non-cellular barcodes, albeit to different degrees.

We use the term "shells" to refer to the droplets used in droplet-based technologies such as 10x
Genomics (Zheng et al., 2017), inDrops (Klein et al., 2015) and Drop-seq (Macosko et al., 2015).
In these assays, a suspension of cells is partitioned into thousands of nanoliter droplets, each of
which ideally contains both a single cell and a barcoded capture bead. After cell lysis, the bead
binds and labels the RNA molecules. Ambient contamination arises from encapsulation of ambient
RNA from the cell suspension along with a cell and a bead. To limit multiplets, these assays are
intentionally underloaded, and a substantial portion of the recovered barcodes represent empty
droplets that must be removed in downstream processing (Pan et al., 2022; Lun et al., 2019). This
is similar for combinatorial barcoding technologies (Vitak et al., 2017).

Cells are the reaction chamber for combinatorial barcoding-based technologies such as SPLiT-seq
(Rosenberg et al., 2018). In these assays, cells are labeled through successive rounds of
combinatorial barcoding, in which cells are repeatedly partitioned into wells, assigned barcodes,
and pooled. After multiple rounds, a RNA from a single cell can be identified by a unique
permutation of barcodes. Although ambient RNA is not physically associated with an intact cell,
it can still be captured and barcoded, producing ambient-only barcodes (equivalent to empty
droplets) and contaminated cellular barcodes.

Technologies such as Smart-seq use wells to isolate single cells for amplification and sequencing
(Ramsköld et al., 2012; Picelli et al., 2013). Ambient RNA molecules are introduced from the
cell suspension prior to well partitioning. However, physical partitioning of cells into wells with
fluorescent activated cell sorting significantly reduces instances of ambient contamination,
non-cellular barcodes, and multiplets (Ding et al., 2020).

In addition to cell-level ambient contamination, bulk contamination can arise from molecular
exchange during PCR amplification or sequencing (e.g. index hopping, barcode swapping, PCR
chimeras) (Griffiths et al., 2018; Farouni et al., 2020; Potapov and Ong, 2017). This form of
background noise affects all cells approximately uniformly and can be interpreted as a "global
noise" profile superimposed on the true signal. Together, these contamination channels can
substantially distort downstream analyses across single-cell technologies, leading to incorrect
cell-type assignments, inflated cell–cell similarities, spurious marker expression, and
compromised differential expression results.

Numerous computational methods have been developed to mitigate the effects background noise,
particularly that introduced by ambient contamination, yet each comes with limitations. Methods
relying on deep-generative models such as CellBender (Fleming et al., 2023) and scAR (Sheng et
al., 2022) explicitly model contamination using variational inference and neural networks have a
high computational cost: they often require GPUs and can take hours to run on medium-sized
datasets. Other widely used tools—including DecontX (Yang et al., 2020) and SoupX (Young and
Behjati, 2020)—are considerably faster, completing analyses in minutes on a CPU, but rely on
simple generative models or heuristic corrections. The benchmarking that has been performed of
these tools reveals divergent and variable performance, making it difficult to select tools in
practice (Cargnelli et al., 2026).

To address these shortcomings, we have developed CellSweep, focusing on efficiency, accuracy and
interpretability. The CellSweep model incorporates explicit mixture components for cell-type
expression, ambient contamination, and global bulk contamination, and uses an efficient
expectation—maximization (EM) algorithm for inference.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Results →](03-results.md)
