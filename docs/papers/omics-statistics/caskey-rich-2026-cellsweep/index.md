---
title: "Caskey & Rich et al. 2026 — Single-Cell Genomics Decontamination with CellSweep"
paper: "summary"
source: "https://doi.org/10.64898/2026.03.04.709349"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Caskey, M., Rich, J., Weber, R., Mortazavi, A., Pachter, L., & Hallgrimsdottir, I. (2026). Single-Cell Genomics Decontamination with CellSweep. bioRxiv preprint, posted March 6, 2026. https://doi.org/10.64898/2026.03.04.709349. ([original](https://doi.org/10.64898/2026.03.04.709349)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Single-Cell Genomics Decontamination with CellSweep

**[Read the full text](full-text/index.md)**

## What this covers

A computational-biology paper on cleaning up single-cell genomics data: separating a cell's true
molecular signal from contaminating RNA that was never really inside it, without the neural-network
and variational-inference machinery current decontamination tools rely on.

## The question

Every single-cell assay — droplet-based (10x, Drop-seq), well-based (Smart-seq2), combinatorial
barcoding (SPLiT-seq), and spatial platforms — captures more than the intended cell. Free RNA from
lysed or damaged cells enters droplets or wells alongside intact cells ("ambient" contamination),
and pooling, PCR and sequencing add a further layer of near-uniform background across all barcodes
("bulk" contamination). Left uncorrected this blurs cell identities, inflates apparent similarity
between cell types, produces spurious marker expression, and distorts clustering and
differential-expression results downstream. Existing tools either use deep generative models fit by
variational inference (CellBender, scAR) — accurate but slow and GPU-hungry — or faster, simpler
approaches (DecontX, SoupX) whose performance is reported to vary unpredictably across benchmarks.
The authors set out to keep the explicit, interpretable probabilistic structure of the first group
at the speed of the second.

## The approach

CellSweep models each barcode's observed counts as a mixture of three interpretable sources: the
expression profile of its assigned cell type, a shared ambient-RNA profile, and a shared "bulk"
background profile for the whole experiment, combined via a barcode-specific ambient fraction and
one global bulk fraction, then drawn as a multinomial sample. Cell types are fixed in advance by an
external clustering step (CellTypist, here). The ambient profile is normally estimated directly from
barcodes identified as non-cellular (empty droplets or wells, found via EmptyDrops or a knee-point in
the UMI-count curve), since their counts should be pure background; the bulk profile is approximated
as the mean expression across all barcodes. Where a technology yields few or no non-cellular
barcodes, such as Smart-seq2, an alternative formulation instead represents the ambient pool as a
weighted mixture of the inferred cell-type profiles themselves, reasoning that ambient RNA comes from
lysed cells of those same types.

The central technical choice is fitting this with classical expectation-maximization rather than
variational inference or amortized neural inference. Because the mixture likelihood is tractable,
the E-step (assigning each count fractionally to its source) and M-step (closed-form updates to the
ambient fraction, bulk fraction, and cell-type profiles) decompose cleanly and parallelize across
barcodes. A two-stage optimization with a "repulsion" term during burn-in keeps fitted cell-type
profiles from drifting toward the ambient profile and stops a few poorly-explained barcodes pulling
the fit toward degenerate, fully-ambient solutions. After convergence, denoised counts come from
subtracting the inferred ambient and bulk contributions from each barcode's raw counts.

## What it found

Across technologies — droplet, well-based, ATAC-seq, spatial, combinatorial barcoding, and a
simulation with known ground truth — CellSweep
removed more cross-contamination while retaining more true signal than CellBender, scAR, SoupX and
DecontX in head-to-head comparisons. On a human-mouse 10x mixture it cut cross-species gene
contamination by roughly 98-99% while keeping nearly all same-species counts, outperforming all four
comparators; the same pattern held on a Smart-seq2 mixture and a mixed-species ATAC-seq dataset. On
a PBMC dataset it removed background counts from marker genes spuriously expressed across unrelated
clusters while leaving a genuinely pan-leukocyte marker intact, and on a multi-tissue plate-based
experiment it removed cross-tissue contamination with little loss of tissue-specific signal.
Reapplying it to already-denoised data changed the output only slightly (near-idempotent), unlike
some neural-network tools that kept eroding counts on repeated passes. On simulated data its
positive predictive value for distinguishing signal from noise matched the strongest competitors and
exceeded scAR's by a wide margin. The headline practical claim is speed: CellSweep runs on CPU in
about five minutes on an 8,000-cell dataset (25 seconds with 16 threads), against tens of minutes to hours for some comparators, several needing a GPU to be practical at all.

## Limits and context

The authors present this as an early-stage report with named open problems, not a finished method.
Doublet/multiplet detection is not modeled jointly with contamination, which they note would help in
dense droplet experiments. The model treats ambient RNA as a simple mixture of cell-type profiles
and ignores molecules disproportionately represented in that pool, such as mitochondrial transcripts
released by lysis. The variant used when non-cellular barcodes are scarce loses the idempotency the
default model shows, flagged as needing further work. They also describe studying how contamination and its removal affect downstream machine-learning
models — embeddings, classifiers, foundation models trained on large atlases — as an open, and in
their view important, direction this paper does not itself settle. The paper argues against the
premise that accurate decontamination requires deep generative or variational modeling, offering
CellSweep's closed-form EM approach as evidence that a simpler likelihood-based model can match or
exceed that accuracy at much lower cost. It is explicit that this is a preprint, not yet
peer-reviewed.

## Citation

Caskey, M., Rich, J., Weber, R., Mortazavi, A., Pachter, L., & Hallgrimsdottir, I. (2026).
Single-Cell Genomics Decontamination with CellSweep. *bioRxiv* preprint, posted March 6, 2026.
https://doi.org/10.64898/2026.03.04.709349. Licensed CC BY 4.0; available via bioRxiv at that DOI.
