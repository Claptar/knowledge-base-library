---
title: 6 Experimental opportunities and limitations
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 6 Experimental opportunities and limitations

Multiple experimental approaches are available for the collection of nascent and mature mRNA
data. We focus on the most prevalent technologies and their relevance to the modeling question at
hand.

Fluorescence microscopy methods are broadly divided between spatial transcriptomics and intron
counting. Spatial transcriptomics leverages relative positions of fluorescently-labeled mRNA and
DNA to identify DNA-localized nascent mRNA [22, 29]. Intron counting directly detects
intron-targeted fluorescent probes [23]. These methods are rather complex and impractical to
perform on a genome-wide scale. Furthermore, we are unaware of any studies combining them with
dual-reporter assays to directly estimate intrinsic and extrinsic noise. Finally, the
discrimination of nascent and mature mRNA aside, dual-reporter assays are in general impractical to
scale to large numbers of genes.

Sequencing methods are broadly divided between labeling and bioinformatics. Labeling refers to
spiking the live media with a nucleoside analogue and distinguishing older and newer mRNA
molecules based on characteristic mutations [30–33]. Purely computational methods do not require
labeling, but identify nascent mRNA based on intron-aligned reads [24, 34]. These methods yield
genome-wide information; however, they are not amenable to reporter duplication on the same scale.
Commercially-available short-read methods present the problem of isoform indistinguishability if
introns interest are outside the read region [24]. Finally, both short- and long-read methods tend
to rely on the capture of polyadenylated tails [7, 35, 36], which are not present in nascent
mRNA, introducing the potential of technical bias against the nascent molecules of interest.
Off-target priming at intronic polyadenine sites [24, 37] and experimental methods including
poly(A) ligation [31] facilitate the capture and identification of nascent transcripts, but the
magnitude of technical biases is as of yet uncharacterized.

Parenthetically, we note that the motivating study by Ham et al. [13] describes a purely
data-based approach to the identification of extrinsic effects, based upon the identification of
heavy distribution tails. This approach appears to be quite powerful based on the provided
demonstration. However, certain aspects are potentially problematic. The validation compares the
tail behavior of the telegraph model to the compound telegraph model. However, even relatively
simple telegraph models suffer from parameter non-identifiability issues [38, 39], so the
robustness of the method is unclear. The specific fit method and metric are not reported; it is not
clear that the conventional choices are appropriate when tail behavior is significant. Recent work
in extreme value theory proposes several Rényi divergence alternatives [40]. Finally, we note that
the underlying data is from Zheng et al. [7], which is the earliest version of the 10X Genomics
single-cell RNA sequencing platform. Since the underlying mammalian physiology has export and
splicing processes [41], but 10X sequencing explicitly focuses on exonic reads [7], it is unclear
that the choice of a one-stage model is justified. More problematically, raw count data are rarely
used in scRNA-seq analyses [42], with substantial debate and disagreement regarding the
appropriate approach to normalization [43, 46]. Therefore, it is conceivable that technical biases
may, in part, explain the 15-25 cells with extremely high expression that control the kernel
density in the tail region, used to support the hypothesis of extrinsic noise.

---

[← 5 Discriminating between intrinsic and extrinsic noise models](05-5-discriminating-between-intrinsic-and-extrinsic-noise-model.md) · [Up: contents](index.md) · [7 Discussion →](07-7-discussion.md)
