---
title: INTRODUCTION
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INTRODUCTION

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_It requires indeed some courage to undertake a labor of such_

_far-reaching extent; this appears, however, to be the only right way by which we can finally reach the solution of a question the importance of which cannot be overestimated in connection with the history of the evolution of organic forms._

#### GREGOR MENDEL

One of the most fundamental questions in biology is how chemical information stored in a sequence of DNA molecules encapsulated in tiny cell-chambers of living organisms gives rise to a plethoric plentitude of biological behaviors and characteristics, differing across tissues within the same organism, organisms of the same species, and species ranging the tree of life. While today, unprecedentedly large-scale analyses associate variants in DNA sequences to phenotypic differences using tens of thousands of samples, it is valuable to remember how we arrived in the age of big data genomics as a way of guiding how to advance.

That discrete traits can be passed down from organism to organism, Mendel first observed in the 1860s by performing crosses of the unassuming garden pea, _Pisum sativum_ [1]. Without knowledge of DNA, he described the laws governing “ _elementen_ ,” or hereditary factors, that hybrid crosses inherited from each parent: functional units that later came to be described as _alleles_ of _genes_ . A few years later, in 1869, Miescher discovered a phosphorus-rich compound in the nuclei of cells that he called “ _nuclein_ ,” composed mostly of what we now call deoxyribose nucleic acid (DNA) [2]. However, it was not until the work of Oswald Avery in the mid-1940s, building on Frederick Griffith’s earlier experiments, that the nucleic acid DNA was shown to “transform” bacteria from non-virulent to virulent and was thus discovered to be the substance carrying Mendel’s proposed genetic unit [3].

2

The 1950s saw the structure of DNA resolved, and the famous (and infamously misunderstood) proposition by Crick of directional information flow from DNA to RNA to protein, but not from protein to either protein or nucleic acid [4]. In the 1970s and 80s, nucleic acid sequencing technologies emerged, with the first RNA genome, bacteriophage MS2, sequenced in 1976 [5] and the first DNA genome, bacteriophage _𝜙_ X174, in 1977 [6], both only several thousand nucleotides long. The first multicellular organism to have its 97 megabase (Mb) genome sequenced was _Caenorhabditis elegans_ , published in1998 [7], followed by the 2001 publication of the 30-times larger human genome as the culmination of the 3-billion-dollar<sup>1</sup> Human Genome Project (HGP) [8]. The initial publication, however, was incomplete, and only as recently as 2022 did the follow-up Telomere-to-Telomere consortium publish an end-to-end reference sequence that includes highly repetitive regions near centromeres and telomere ends [9]<sup>2</sup> .

The creation of a human reference sequence was a foundational event in the ongoing history of characterizing the function of sequences of DNA. With it, genome-wide association studies (GWAS) began to link _variation_ from that reference in the form of single-nucleotide polymorphisms (SNPs) to sample phenotypes like disease and other traits [11, 12, 13]. Today, as the cost of sequencing a genome has dropped from three billion to several hundred dollars, GWAS are performed with ever larger sample sizes [14], increasing the number of variants implicated in an extensive set of diseases and traits, including heart disease [15], psychiatric disorders [16, 17], multiple forms of cancer [18], height [19], and behavioral habits like tobacco use [20].

However, most of the SNPs identified as significant in GWAS are located in noncoding regions of the genome, making their functional mechanism hard to interpret. This is unsurprising, as only about 1.5% of the 3 billion haploid base pairs in the human genome codes for proteins. The remaining 98.5%, though, is far from inert: aiming to catalogue non-coding genomic regions and create an Encyclopedia of DNA Elements, the ENCODE project identified over 80% of the genome as biochemically active [21]. Many of these are important regulatory regions, such as promoters, enhancers, or regions of structured chromatin and histone modifications.

> 1About one dollar per base pair!

> 2Arguably, there is no “human genome,” as every genome contains variation in the form of singlenucleotide differences, copy-number differences in repetitive regions, small inserts and deletions (indels), and larger scale structural variation. Now, there is a push towards the use of “pangenome graphs” rather than a single, linear reference genome to better capture a range of genetic diversity [10].

3

This showed that the vast majority of our DNA contains _regulatory information_ that carefully controls the directed flow of information from DNA to “transcribed functional units” of RNA. The regulatory information governs the production (transcription) of nascent RNA molecules, as well as how they are altered (e.g., removing introns by splicing to leave exons comprising mature RNA molecules) before being exported from the nucleus and translated into protein. This process, how genes are turned on and off or modulated to produce dynamic distributions of RNA in different contexts and in response to stimuli, is called **gene expression regulation** .

To fully understand how the genome’s information content produces biological function, then, it is necessary to ascertain not only the precise sequence of DNA but the levels of intermediates between genome and protein: RNA transcripts. Genomewide measurements of RNA expression were first made using microarrays, which contained thousands of probes pre-designed to hybridize to known transcript sequences [22]. In the 2000s, the development of high-throughput, massively parallel sequencing methods gave rise to a more unbiased quantification of gene products, RNA-seq [23]. Most RNA-seq technologies use poly(T) probes to capture polyadenylated tails of messenger RNA (mRNA), with initial applications to bulk tissue samples (bulk RNA-seq). The probes also contain priming sites for reverse transcriptase and DNA polymerase, which convert RNA to cDNA libraries via reverse transcription and subsequent amplification, and indices that bind to sequencing machine flow cells. Sequencing machines then perform many rounds of complementary strand synthesis with fluorescently labeled nucleotides to “read” cDNA sequences corresponding to the original RNA. These reads are then aligned to a reference genome, and the number that overlap with annotated genes are used to quantify the gene expression profile of input samples. With the proper annotation, reads can also be assigned at the sub-gene level: for example, as spliced/mature or unspliced/nascent if aligning to exonic or intronic regions of a gene, respectively [24, 25].

In the 2010s, these RNA capture technologies were combined with microfluidic and well-based approaches that separate individual cells [26, 27], and sequencing probes were designed with cell-specific barcodes and unique molecular identifiers (UMIs), to allow the quantification of unique RNA molecules across the full spectrum of protein coding genes in _individual cells_ . This technology, single-cell RNA-seq (scRNA-seq), unlocked extensive observations of the wide diversity of gene expression profiles across cells: these differences are used to distinguish and classify cell

4

types (more on this in Chapter II). It also paved the way for the creation of comprehensive _cell atlases_ : from identifying all the genes and functional elements in the human genome came the effort to classify all cell types and states in the human body [28].

Returning to the goal of GWAS to determine the association between SNPs and high-level phenotypes like disease, there was introduced the intermediate step of linking SNPs to gene expression (RNA levels) in particular biological settings, and then determining post hoc if the gene’s protein product had any role related to the SNP-linked disease or trait. These variant to expression associations (expression Quantitative Trait Loci, or eQTL, studies) have been performed across tissues in the human body [29, 16], and, after the rise of scRNA-seq, even specific cell types [30]. These studies provide maps between genetic variants, the gene encoding the functional protein, the biological context, and particular diseases or traits. However, several issues remain.

Firstly, there is a combinatorics problem for identifying significant variant-gene associations. Testing for significant associations between hundreds of millions of SNPs in the human genome ( _𝑓_ × 10<sup>8</sup> ) [31] and tens of thousands of genes ( _𝑓_ × 10<sup>3</sup> ) in hundreds of cell types and contexts ( _𝑓_ × 10<sup>2</sup> ) is computationally and statistically burdensome ( _𝑓_ × 10<sup>14</sup> tests!). To reduce the number of tests, variant testing is split into two digestible conceptual categories: _cis_ , or variants that are restricted to be within some distance (usually ±1 Mb) of the gene; and _trans_ , or any variants outside of this window. This reduces the number of _cis_ tests from tens to thousands per gene, as opposed to tens of millions. _Trans_ variant identification has not escaped the combinatoric encumbrance. To give a sense of the difficulty in identifying _trans_ eQTLs, in a final release of the Gene-Expression-Tissue (GTEx) project that tested variant-gene associations across 54 human tissues, only 143 genes with _trans_ regulation were identified, as opposed to 23,268 _genes_ with _cis_ eQTLs [29].

Another missing piece is mechanism: eQTL studies associate variants with a change in average gene expression, revealing nothing of the cellular _processes_ that the variant could be affecting. While adaptations of eQTL studies for testing links between SNPs and ratios of spliced to unspliced RNA counts for a gene (splicing QTL, or sQTL, studies) give oblique insight into mechanism [32], the ratio of spliced to unspliced counts is a mere proxy for the actual process of splicing.

ScRNA-seq data could hold the key to linking SNP to disrupted cellular process, as they give access to mechanistic information. In parallel to the genomic revolution,

5

small scale investigations of transcription in individual cells using fluorescently labeled RNA molecules reported key parameters governing the process, such rates of transcriptional initiation and RNA decay. These were inferred by fitting particular biophysical models to the observed distribution of RNA counts, grounded in the observation of the systems’ stochasticity [33, 34, 35]. Crucial to these discoveries was the insight that the variance in RNA counts over genetically identical cells in identical conditions was not merely technical noise but contained information about the underlying biological system: the _distribution_ is more informative than the mean. Count distributions from scRNA-seq can be similarly modeled; and, with the inclusion of spliced and unspliced information, used to learn about the lifecycle of RNA in different cell types and organisms [36, 37, 38].

Unfortunately, although common for decades in fluorescence studies, using a biophysical model to analyze scRNA-seq data has been slow to gain traction in the genomics field. It is by far outnumbered by heuristic choices and arbitrary data manipulations [39], with the final output being a list of “differentially expressed genes” (DEGs), or genes with different means in the different tested groups [40]. Rather than taking advantage of count variation across single cells, sc-eQTL pipelines attempt to remove it by porting over approaches from bulk eQTL pipelines. A recent review on best-practices for sc-eQTL pipelines tested whether median, mean, or sum of RNA counts over cells of a cell type would be “best,” as defined by finding the greatest number of significant variant-gene associations [41]. While this failure to account for the data generating process is a characteristic of the genomic data analysis philosophy belonging to the “algorithmic modeling” versus “stochastic data” modeling culture [42], it is also a problem of practicality. For all but the simplest biophysical models, there is no closed-form distribution solution [43], and tools to scale computationally costly inference procedures to the datasets required for genetic association studies have not been available.

So, in pursuit of understanding how DNA sequences lead to biological function, and how genetic variants alter this, we are left with challenges:

1. **Statistical and computational difficulties in identifying trans-acting variants:** Before we pinpoint exact _trans_ variants, can we determine _to what extent and which genes are regulated in trans_ ?

2. **Resolution and context dependence:** How does regulation act at the tissue and cell type level, and _how do we make full use of single-cell data to explore_

6

_this_ ?

3. **Mechanism:** By what mechanisms do genetic variants act, i.e. _what is their effect on biophysical processes of the cell_ ?

These are the overarching/motivating questions I consider in my thesis, asking what we can gain from coupling genetic analyses to single cell biophysics, and how to scale this to modern-day genomic datasets. We develop the theory and tools that are the necessary building blocks for answering these questions, and then apply them to infer biophysical mechanisms and its regulation for tens of thousands of genes across eight tissues in eight founder mouse strains: the largest analysis of single-cell biophysical mechanism of which we are aware.

Before fitting biophysical models to full RNA count distributions, we showcase the utility of moving beyond comparison of its first moment (mean) to its second (variance) [44, 45]. We start with one of the first steps in single-cell analyses pipelines: dimensionality reduction. While most scRNA-seq pipelines use principal component analysis (PCA) to group similar cells into “types,” we demonstrate in Chapter II how it can be adapted to move beyond comparing average expression to identify patterns of variation that are different in a target or case versus a background or control genomic dataset.

We then describe the biophysical modeling formulation we use for scRNA-seq distributions in Chapter III [37]. We provide examples of how this can be used for biological discovery and hypothesis generation by giving access to mechanistic interpretation of biological responses to intervention. In Chapter IV and V, we show how distributions for intractable biophysical models can be efficiently approximated and scaled for inference using machine learning, expanding the practical scope of their applicability [46, 47].

In Chapter VI, with a nod to Mendel and his peas, we present a new mathematical framework for determining the relative contributions of _cis_ and _trans_ regulation to differences in homozygous parental gene expression using their hybrid crosses [48]. This complements eQTL studies by providing a way to discover the presence and extent of _trans_ regulation by induction (while we cannot determine the _trans_ acting variant, we can say that it exists), restricting the search space for candidate genes.

Finally, in Chapter VII, we combine the threads of the thesis for an exciting demonstration of coupling genetics to single cell biophysics at scale. We fit biophysical

7

models for the largest analysis of biophysical parameters of which we know: 15 diverse genotypes, eight tissues, 92 unique cell types, and 30,763 genes. We next apply the framework developed in Chapter VI to determine gene regulatory strategies of biophysical mechanism between the diverse strains across genes, cell types, and tissues.

In Chapter VIII, we think ahead to the future of modeling approaches in light of ever expanding, dizzyingly large genomic datasets and computational revolutions: what kinds of questions may be possible to ask, and what are the role and capacity of the human computational biology researcher?

8

_C h a p t e r 2_

---

[← TABLE OF CONTENTS](05-table-of-contents.md) · [Up: contents](index.md) · [CONTRASTIVE DIMENSIONALITY REDUCTION FOR DIFFERENTIAL VARIANCE →](07-contrastive-dimensionality-reduction-for-differential-varian.md)
