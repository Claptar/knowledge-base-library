---
title: "Gálvez Merchán 2023 — Studies of mRNA expression and degradation"
paper: "summary"
source: "https://doi.org/10.7907/esxk-ch24"
licence: "all rights reserved — not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Gálvez Merchán, Ángel (2023). Studies of mRNA expression and degradation. PhD thesis. California Institute of Technology. https://doi.org/10.7907/esxk-ch24 ([original](https://doi.org/10.7907/esxk-ch24)). Rights: all rights reserved — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Studies of mRNA expression and degradation

## What this covers

A Caltech PhD thesis in two unrelated parts: how a cell degrades the truncated protein made from
an mRNA flagged by nonsense-mediated decay, and how to build single-cell gene-expression "atlases"
that can be updated and reanalysed rather than published as a fixed snapshot.

## The question

Part I asks what happens to the protein, not just the mRNA, when a transcript carries a premature
stop codon. Nonsense-mediated decay (NMD) is well understood as an mRNA pathway, but the truncated
mRNA is translated before it is destroyed, producing a nascent protein that could misfold,
aggregate, or act as a dominant-negative or gain-of-function factor. Whether the cell runs a
dedicated pathway to also destroy that protein, or instead relies on the generic ribosome quality
control (RQC) machinery known from stalled-ribosome pathways like no-go and non-stop decay, had not
been settled, partly for want of a reporter able to separate mRNA decay from protein decay.

Part II addresses a bottleneck in single-cell genomics: atlas projects (Human Cell Atlas, Tabula
Muris, Tabula Sapiens) each duplicate effort retrieving metadata, normalising counts and assigning
cell types, and the resulting atlas is a static object that cannot easily absorb new data, new
markers, or isoform-level questions. The thesis asks whether these steps can be automated and the
atlas made reproducible and continually updatable, then uses the result to ask whether isoforms of
the antiviral gene OAS1 are expressed differently across human cell types.

## The approach

For Part I, the author built a reporter expressing GFP and RFP from one open reading frame
separated by a viral 2A "self-cleaving" peptide, with an NMD-triggering beta-globin intron placed
after the stop codon driving RFP. Because both proteins come from one mRNA but only RFP sits
downstream of the premature stop, the RFP:GFP ratio isolates protein-level degradation from
mRNA-level effects. The reporter drove genome-wide CRISPR interference and knockout screens in K562
cells for genes needed to degrade the nascent NMD protein, followed by arrayed validation and
ubiquitination assays.

For Part II, the author built command-line tools — `ffq` for metadata retrieval from sequence
databases (SRA, ENA, DDBJ, GEO, ENCODE), and `mx`/`ec` for matrix filtering, normalisation and
cell-type assignment around the `kallisto`\|`bustools` pipeline — then benchmarked eight common
normalisation methods against variance stabilisation, depth normalisation and monotonicity across
526 public datasets, and assembled the tools into a "Commons Cell Atlas" (CCA) workflow used to
build a Human atlas from raw reads, quantified at gene and isoform level.

## What it found

**Chapter 2** (Inglis et al. 2023) found that NMD triggers a ubiquitin-proteasome-dependent
degradation branch for the nascent protein, distinct from mRNA decay: proteasome and
ubiquitin-activating-enzyme inhibitors selectively stabilised the reporter's protein product, and
the nascent chain was directly ubiquitinated. Screens recovered core NMD factors (UPF1, UPF2,
UPF3B, SMG6, the EJC component CASC3) but not the canonical RQC factors (PELO, HBS1, the ligase
LTN1) that the same platform detected for a matched non-stop-decay reporter. A UPF1 RING-domain
mutant unable to recruit E2 enzymes still rescued the phenotype, so UPF1 was placed upstream of
ubiquitination rather than acting as the responsible E3 ligase, which was not identified. SMG6's
endonuclease activity was required for both branches, pointing to one shared recognition step that
only later diverges.

**Chapter 4** (Gálvez-Merchán et al. 2023, *Bioinformatics*) describes `ffq`, which fetches
metadata and data links from SRA, ENA, DDBJ and ENCODE given an accession or paper DOI, returning
JSON rather than downloading data itself, unified across databases that share a hierarchical
study/sample/experiment/run structure.

**Chapter 5** (Booeshaghi et al. 2022, *bioRxiv*) benchmarks single-cell normalisation methods
(log-CP10k, log-CPM, sqrt, sctransform, and a proposed PFlog1pPF) across 437 passing datasets. Every
method traded off variance stabilisation against depth normalisation; sctransform did not fully
remove depth effects despite its stated aim, and also scrambled gene rank order within a cell,
breaking the monotonicity that marker-gene heatmaps depend on. PFlog1pPF — proportional fitting,
log, then a second proportional-fitting step — achieved near-complete depth normalisation with only
a small cost to variance stabilisation, and far fewer false-positive differentially expressed genes
than the common CP10k default.

**Chapter 6** describes the algorithmic core of the Commons Cell Atlas: `mx filter`, replacing
by-eye "knee plot" judgement of barcode quality with an automatic Gaussian-mixture fit, and `mx
assign`, a rank-based cell-type assignment method. Benchmarked against the existing tool CellAssign
on simulated data, `mx assign` stayed accurate with as few as three marker genes per type, stayed
robust to mis-specified markers, and ran about 350 times faster (roughly 4 seconds versus 21
minutes assigning 8,000 cells).

**Chapter 7** applies this to build a Human Commons Cell Atlas of 2.9 million cells across 27
tissues from 525 public datasets, processed uniformly from raw reads in about two weeks.
Tissue-level markers recovered known genes (LPL in adipose tissue, SFTPC in lung), and OAS1 gene
expression was broad and non-tissue-specific, rising in COVID-19-infected lung as expected for an
interferon-induced gene. At isoform level, of four substantially expressed OAS1 isoforms, the
normally minor isoform p44-b was unexpectedly dominant in testis — about 60% of OAS1 expression
there, over 80% in cells undergoing spermatogenesis — a specificity invisible to any
gene-level-only atlas.

## Limits and context

The NMD-coupled degradation finding is reporter-based: effects were modest (roughly two-fold), and
because the reporter is over-expressed with an unusually stable RFP, the true effect on an
endogenous substrate could differ. No E3 ligase for the nascent chain was identified, and the
thesis could not establish whether ubiquitination happens simultaneously with translation
termination or immediately after, though it favours a model in which ubiquitination precedes
release from the ribosome without claiming to have shown this directly. It argues specifically
against the canonical RQC pathway (PELO/HBS1/LTN1) and against UPF1 itself being the responsible
ligase.

For the atlas work, the normalisation benchmark argues against taking sctransform's claims of
complete depth normalisation at face value, citing conflicting published false-positive-rate
benchmarks, but does not claim to have solved variance stabilisation in general — all current
transforms are described as heuristics that ignore the biophysical origin of count overdispersion.
The OAS1 isoform finding is called preliminary, with assessment of p44-b's function in testis
stated as beyond the thesis's scope, and the atlas itself is framed as deliberately never "final",
meant to be revised as new data and cell-type definitions arrive rather than treated as a fixed
reference.

## Citation

Gálvez Merchán, Ángel (2023). *Studies of mRNA expression and degradation*. PhD thesis. California
Institute of Technology. Defended June 5, 2023. https://doi.org/10.7907/esxk-ch24

Incorporates, by the author's own account: Inglis, Alison J. et al. (2023). "Coupled protein
quality control during nonsense-mediated mRNA decay". *Journal of Cell Science* 136.10, jcs261216
(Chapter 2); Gálvez-Merchán, Ángel et al. (2023). "Metadata retrieval from sequence databases with
ffq". *Bioinformatics* 39.1, btac667 (Chapter 4); Booeshaghi, A. Sina et al. (2022). "Depth
normalization for single-cell genomics count data". *bioRxiv* 2022-05 (Chapter 5).

Available via the Caltech Thesis Repository: https://doi.org/10.7907/esxk-ch24
