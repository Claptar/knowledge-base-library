---
title: "Marioni et al. 2008 — RNA-seq: An assessment of technical reproducibility and comparison with gene expression arrays"
paper: "summary"
source: "https://doi.org/10.1101/gr.079558.108"
licence: "© Cold Spring Harbor Laboratory Press — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Marioni, J. C., Mason, C. E., Mane, S. M., Stephens, M., & Gilad, Y. (2008). RNA-seq: An assessment of technical reproducibility and comparison with gene expression arrays. Genome Research, 18(9), 1509-1517. ([original](https://doi.org/10.1101/gr.079558.108)). Rights: © Cold Spring Harbor Laboratory Press — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# RNA-seq: An assessment of technical reproducibility and comparison with gene expression arrays

## What this covers

An early methods paper asking whether the then-new "ultra-high-throughput" sequencing of cDNA
(what would come to be called RNA-seq) can measure mRNA expression levels reliably enough to
replace, or complement, gene expression microarrays. It speaks to the statistics of genomics and
to the practice of measuring differential expression.

## The question

By the mid-2000s, microarrays were the default way to measure expression, but they have known
limits: background hybridization inflates signal for low-abundance transcripts, probes of
different sequence composition behave differently even for the same true expression level, and
each array can only query the transcripts it was designed with probes for. Massively parallel
sequencing was emerging as an alternative for genotyping and for mapping chromatin and
transcription-factor binding, but its use for quantifying mRNA abundance was still largely
unproven. The authors set out to establish two things before the method could be trusted for
expression work: how much of the variation between repeated sequencing runs of the *same* sample
is just technical noise, and how the resulting calls of differential expression compare with
those from a standard array platform on the same RNA.

## The approach

The authors sequenced total RNA from one human liver sample and one kidney sample on the Illumina
Genome Analyzer, each sample run seven times across two sequencing runs and, for most lanes, at
the same cDNA concentration, so that repeat lanes could be compared directly. For each gene, the
"expression level" is simply the count of reads whose unique best alignment falls in that gene's
exons. For comparison, the same RNA was hybridized, in triplicate, to Affymetrix microarrays, and
probe sets were mapped to Ensembl genes so that the two platforms could be compared gene-for-gene.
To ask whether repeat lanes agree with each other, the paper treats read counts for a gene across
lanes as independent Poisson-distributed counts whose rate is proportional to that gene's true
relative abundance, and checks, gene by gene, whether the observed counts are consistent with this
null model — first comparing lanes pairwise using a hypergeometric test, then comparing several
lanes at once with a $\chi^2$ goodness-of-fit statistic. The same Poisson framework, recast as a
generalized linear model, is then used to test for differential expression between the liver and
kidney samples, and its results are compared against a standard empirical-Bayes moderated-t
analysis of the array data at a matched false discovery rate. A subset of genes flagged as
differentially expressed by one platform but not the other was independently checked by
quantitative PCR, and a separate read-alignment procedure was used to look for reads spanning
exon-exon junctions, as a preliminary test of whether the sequencing data could also detect
alternative splicing.

## What it found

Repeat lanes of the same sample agreed closely: gene counts across lanes were highly correlated,
and the goodness-of-fit tests showed only a small proportion of genes (consistently well under 1%)
departing from the Poisson null in a way that indicated a systematic "lane effect," whether lanes
came from the same sequencing run or from different runs. Reads sequenced at a different cDNA
concentration than their comparison lane showed more departure from uniformity, but this is framed
as an effect of concentration rather than of the sequencing platform itself. Applying the Poisson
model to pairs of lanes known to be technical replicates of the identical sample produced only a
handful of false positive "differentially expressed" genes even at a lenient threshold, supporting
the model's adequacy for calling real differences. Comparing liver against kidney, the sequencing
data called roughly ten thousand genes differentially expressed at a strict false discovery rate,
about 30% more than the array analysis found at the same false discovery rate, and the large
majority of the array-based calls were recovered by the sequencing data. Fold-change estimates
from the two platforms correlated well, more closely for genes with many mapped reads than for
genes with few. Quantitative PCR on a set of genes called as differentially expressed by only one
platform tended to agree more often with the sequencing calls than with the array calls. Read
coverage over a single lane already identified a majority of the genes found with five lanes
combined, with diminishing additional genes detected as more lanes were added, and reads spanning
exon-exon junctions could recover known and apparently novel splice junctions for individual
genes, illustrated with one gene examined in detail.

## Limits and context

The authors are explicit that the Poisson model is only approximately right: formal tests detect
a small but real excess of variation beyond what Poisson sampling predicts for a minority of
genes, and they flag over-dispersion-aware alternatives — such as a quasi-Poisson or negative
binomial model, or a variance-stabilizing transformation feeding into an empirical-Bayes
procedure — as directions that might improve on the simple Poisson approach without yet showing
that any of them is needed for the conclusions drawn here. The study design did not replicate the
library-preparation step itself, so the paper cannot separate technical variance from sequencing
runs and flow-cells from variance introduced earlier, during library construction, and says the
latter may still contribute meaningfully to overall technical variance. The splicing analysis is
described as preliminary and of the order-of-magnitude kind, since a single lane's read depth and
read length may not be sufficient to resolve all exon-annotation conflicts or reconstruct full
transcript structures, and the authors call for more careful follow-up work. More broadly, the
comparison with arrays is limited to one liver and one kidney sample from a single individual, and
the paper frames its findings as establishing feasibility and a provisional statistical protocol
for a still-new technology rather than a definitive characterization of its error properties.

## Citation

Marioni, J. C., Mason, C. E., Mane, S. M., Stephens, M., & Gilad, Y. (2008). RNA-seq: An assessment
of technical reproducibility and comparison with gene expression arrays. *Genome Research*, 18(9),
1509-1517. https://doi.org/10.1101/gr.079558.108. Published by Cold Spring Harbor Laboratory Press;
available via the DOI link above (open access on genome.org).
