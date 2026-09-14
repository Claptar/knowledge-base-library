---
title: Preprocessing of raw sequencing data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.Rmd
source_file: sources/statomics-sga21/sequencing_intro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing of raw sequencing data

**Source:** [`sequencing_intro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

After sequencing, we typically do a quality control (QC) check to verify the quality of the samples. During QC check, aberrant samples due to e.g. degraded mRNA can be detected.

The sequencing reads on their own contain a lot of information, but are most useful if we would be able to assign sequencing reads to genomic features (genes, exons, transcripts, etc.), i.e., for each sequencing read we will try to derive the (set of) feature(s) that could have plausibly produced the fragment through the process of gene expression. This process is called **mapping**. Most often we map reads to genes.

```r
include_graphics("./images_sequencing/seqWorkflow2.png")
```

## Quality control

During quality control, diagnostic plots are created for each sample in order to determine its quality. The most popular QC tool for bulk RNA-seq data is [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/). If many samples are sequenced, then [MultiQC](https://multiqc.info/) can be used to aggregate the QC checks across samples in a conveniently organized overview.

The FastQC website provides interesting example reports for us to look at and compare against. Here are example reports of [high-quality Illumina data](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/good_sequence_short_fastqc.html) and [low-quality Illumina data](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/bad_sequence_fastqc.html).

## Mapping

 - Mapping is a critical step in the interpretation of RNA-seq data, where we are attributing reads to genomic features.
 - Allows us to measure how strong a feature such as a gene is expressed: the number of reads mapping to a gene serve as a proxy for how high that gene has been expressed in the sample.
 - While this opens the door to many opportunities, mapping is hard.
 - We are **typically unable to assign each individual read uniquely** to one specific gene; some reads cannot be unambiguously mapped and are compatible with multiple genes. These reads are said to be 'multi-mapping'.

Finally, a note on terminology. In this text we will use the words 'read' or 'fragment' (referring to the fragmented mRNA molecule being sequenced) to designate a datum, note that this could be either a single read (in single-end sequencing) or a read pair (in paired-end sequencing). The literature may also use these words interchangeably, although 'fragment' seems better at avoiding ambiguity between single-end reads and paired-end read pairs.

### Reference files

 - The alignment most often relies on a **reference genome** of the species, which can be considered a 'representative example' of the genome sequence of that species. Reference genomes are contiuously updated and released periodically.
 - Reference genomes can be freely downloaded from several providers, for example [Ensembl](http://www.ensembl.org/info/data/ftp/index.html) or [Gencode](https://www.gencodegenes.org/human/).
 - Along with a reference genome, an annotation GFF or GTF file defines the coordinates of specific genomic features.
 - While here we will focus on reference-based alignment, i.e., alignment where a reference genome or transcriptome is available, note that a *de novo* construction of a reference transcriptome is also possible, where the reference may be constructed from the observed sequencing reads.

```r
include_graphics("./images_sequencing/referenceGenome.png")
```

```r
include_graphics("./images_sequencing/gtfFile.png")
```

 - More recently, mapping of RNA-seq data occurs more often against a **reference transcriptome**, which is a reference file containing the sequences all known isoforms of a particular species, e.g., using [kallisto](https://www.nature.com/articles/nbt.3519) or [Salmon](https://www.nature.com/articles/nmeth.4197).
 - The set of spliced transcripts is much smaller than the entire genome, and therefore mapping against a reference transcriptome is typically **fast and memory efficient**.
 - However, [it has been noted](https://www.biorxiv.org/content/10.1101/2021.05.05.442755v1) that mapping against a reference transcriptome may also introduce spurious expression for genes that are not expressed. These observations can be explained by **intronic reads** that share some sequence similarity with transcripts, and could map to spliced transcript sequences. Recent methods, such as [alevin-fry](https://www.biorxiv.org/content/10.1101/2021.06.29.450377v1), avoid this by expanding the reference transcriptome to also include intronic sequences.

### Alignment-based workflows

 - Traditionally, alignment-based workflows have been used to map reads, where one tries to **find the exact coordinates a read maps to** on the reference genome or the reference transcriptome.
 - Note that due to alternative splicing, reads do not necessarily map contiguously on a reference genome, as a read can overlap with a splicing junction, where an intron has been excised. When mapping against a transcriptome, however, reads should be mapping contiguously.
  - A main challenge in spliced alignment against a reference genome is the proper alignment of reads that span a splice junction, especially when these junctions are not annotated a priori. Indeed, in spliced alignment reads can be split at any nucleotide, and the corresponding subsequences can map several thousands of basepairs apart. Meanwhile, the main challenge in unspliced alignment to a transcriptome is the redundant sequence among related transcripts in the transcriptome, which often leads to a high multi-mapping rate (i.e., reads that cannot be unambiguously assigned to a single transcript).
 - Spliced alignment against a genome is therefore computationally a much harder task. Since the transcript sequences are already spliced when aligning to a reference transcriptome, reads should align contiguously, and many of the computationally expensive steps and heuristics can be avoided, there.

```r
include_graphics("./images_sequencing/splicedAlignment.png")
```

### Alignment-free workflows

 - Modern approaches **avoid mapping each fragment individually** (i.e., do not attempt to find the exact coordinates of a read's origin), and instead posit a probabilistic model where **transcript abundances are typically defined using its constituent $k$-mers**. These methods are sometimes referred to as *lightweight*.
 - A $k$-mer is a short sequence of nucleotides of length $k$. The space of possible $k$-mers and the corresponding transcripts can be precomputed in advance using the reference transcriptome, providing a computational advantage as it only needs to be computed once.
 - For each fragment, the transcripts its $k$-mers are compatible with is searched for using an indexed (efficiently searchable) transcriptome. The set of compatible transcripts is called the '$k$-compatibility class', 'equivalence class' or 'transcript compatibility class' of the fragment.

```r
include_graphics("./images_sequencing/kallisto_equivalenceClasses.png")
include_graphics("./images_sequencing/kallisto_equivalenceClasses_caption.png")
```

## Abundance quantification

Given a set of mappings, using either alignment-based or alignment-free workflows, the estimation of expression of a gene/transcript/exon may occur in several ways.

**Counting**:

 - In alignment-based workflows, one could do a direct counting of fragments at, for instance, the gene level, counting the number fragments mapping to each gene. This has been the dominant approach for the first decade of RNA-seq data, often obtained using reference genome alignments.
 - Many heuristic choices need to be made: Do we count a fragment as soon as it intersects with the gene's coordinates, or do we require the full fragment to map to the gene? Do we count intronic reads? Do we count multi-mapping reads?

```r
include_graphics("./images_sequencing/readCounting.png")
```

**Estimation**:

 - Abundance quantification is more recently starting to shift from counting towards using statistical models to estimate the expression counts for a feature, which in this case is typically a transcript.
 - This approach is amenable to alignment-free workflows, since the number of fragments in each equivalence class are sufficient statistics for the abundance quantification, meaning that they contain all information needed to estimate the parameters of the statistical model, and hence the feature-level abundances. Since the expression counts in this case are estimated, they are not necessarily integer counts, and will be referred to as 'estimated counts'.
 - In order to derive these, the EM-algorithm ([Dempster *et al.* (1977)](https://www.jstor.org/stable/2984875)) is often used, although other approaches have been used by tools like Salmon. A big advantage of the estimation approach is that it **probabilistically assigns fragments to transcripts, thereby automatically dealing with multi-mapping reads**. The total number of fragments mapping to each transcript is then the sum of all fragment-level probabilities to be assigned to that respective transcript.

```r
include_graphics("./images_sequencing/abundanceEMAlgorithm.png")
```

### Abundance metrics

 - For simplicity, we have mainly been talking about feature-level counts as in sums of fragments. However, this is merely one metric that can be used as a proxy for expression, and several others exist.
 - Most of these were introduced to attempt to make the abundances more comparable across samples or features, as compared to the simple counts. These mainly serve to correct for technical biases such as transcript length and sequencing depth, both of which have significant impact on the observed counts.
  - Indeed, for a gene with the same mRNA concentration in two samples, sequencing one sample deeper, will on average result in a higher count.
  - Likewise, for two transcripts with the same mRNA concentration but different transcript lengths, one will tend to observe more fragments from the longer transcript due to the fragmentation step in the RNA-seq protocol, where longer transcripts can be split into more fragments of appropriate length.


Below we introduce several relevant abundance metrics, but note that most data analysis methods we will discuss in this course will work with (estimated) counts. In what follows, let $Y_{fi}$ denote the random variable representing the expression counts of feature $f$ in sample $i$ (obtained either as a simple sum of fragments or estimated using lightweight approaches), and let $N_i = \sum_f Y_{fi}$ denote the sequencing depth ('library size') of sample $i$.

 * **Counts per million (CPM)** are the counts one could expect to observe if the sample was sequenced to a depth of one million.

$$ CPM_{fi} = \frac{Y_{fi}}{N_i} 10^6 $$

 * **Transcripts per million (TPM)** refers to the concentration or proportion of your feature in the sample. TPMs take into account the length of the feature, which is often reformulated into an *effective length* $l_{fi}^{(eff)}$, relating to the number of possible start sites that a feature may have in order to generate fragments of a typical length observed in your dataset. This typical length is often calculated using the observed fragment length distribution from the data and defined as $$ l_{fi}^{(eff)} = l_{f} - \hat{\bar{F}}_i + 1,$$ where $l_{f}$ is the total length of a feature in terms of number of nucleotides, and $\hat{\bar{F}}_i$ is the estimated average fragment length in sample $i$. We can use this to define $$ TPM_{fi} = \frac{Y_{fi}}{l_{fi}^{(eff)}} \left( \frac{1}{\sum_f \frac{Y_{fi}}{l_{fi}^{(eff)}}} \right) 10^6.$$ Note that the first part of the right-hand-side (RHS), $\frac{Y_{fi}}{l_{fi}^{(eff)}}$ is the expression counts normalized for the length of the feature. This measure, however, is still affected by the sequencing depth, which is then alleviated by dividing by the sum of the length-normalized counts across all features, i.e., $\sum_f \frac{Y_{fi}}{l_{fi}^{(eff)}}$. TPMs hence normalize for the feature length as well as sequencing depth.

### The final countdown

Once abundances have been quantified, the (estimated) counts are typically stored in a count matrix, with genes spanning the rows and samples spanning the columns. This count matrix forms the basis of most downstream analyses to interpret RNA-seq data, and it will be the main object we will be working with in the following lectures.


```r
include_graphics("./images_sequencing/seqWorkflow3.png")
```

---

[← All defaults](04-all-defaults.md) · [Up: contents](index.md) · [A preprocessing tutorial →](06-a-preprocessing-tutorial.md)
