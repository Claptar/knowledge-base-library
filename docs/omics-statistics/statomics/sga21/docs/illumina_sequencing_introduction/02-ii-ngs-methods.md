---
title: II. NGS Methods
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf
source_file: sources/statomics-sga21/docs/illumina_sequencing_introduction.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/illumina_sequencing_introduction.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# II. NGS Methods

NGS platforms enable a wide variety of methods, allowing researchers to ask virtually any question related to the genome, transcriptome, or epigenome of any organism. Sequencing methods differ primarily by how the DNA or RNA samples are obtained (eg, organism, tissue type, normal vs. affected, experimental conditions, etc) and by the data analysis options used. After the sequencing libraries are prepared, the actual sequencing stage remains fundamentally the same, regardless of the method. There are various standard library preparation kits that offer protocols for whole-genome sequencing (WGS), RNA sequencing (RNA-Seq), targeted sequencing (such as exome sequencing or 16S sequencing), custom-selected regions, protein-binding regions, and more. Although the number of NGS methods is constantly growing, a brief overview of the most common methods is presented here.

## a. Genomics

### Whole-Genome Sequencing

Microarray-based, genome-wide association studies (GWAS) have been a common approach for identifying disease associations across the whole genome. While GWAS microarrays can interrogate over four million markers per sample, the most comprehensive method of interrogating the 3.2 billion bases of the human genome is WGS. The rapid drop in sequencing cost and the ability of WGS to produce large volumes of data rapidly make it a powerful tool for genomics research. While WGS is commonly associated with sequencing human genomes, the scalable, flexible nature of the method makes it equally useful for sequencing any species, such as agriculturally important livestock, plant genomes, or disease-related microbial genomes. This broad utility was demonstrated during the recent *E. coli* outbreak in Europe in 2011, which prompted a rapid scientific response. Using the latest NGS systems, researchers quickly sequenced the bacterial strain, enabling them to track the origins and transmission of the outbreak as well as identify genetic mutations conferring the increased virulence.$^{13}$

### Exome Sequencing

Exome sequencing is a widely-used targeted sequencing method. The exome represents less than 2% of the human genome, but contains most of the known disease-causing variants, making whole-exome sequencing (WES) a cost-effective alternative to WGS.$^{14}$ With WES, the protein-coding portion of the genome is selectively captured and sequenced. It can efficiently identify variants across a wide range of applications, including population genetics, genetic disease, and cancer studies.

$^\dagger$With dual flow cell mode enabled.

### De novo Sequencing

*De novo* sequencing refers to sequencing a novel genome where there is no reference sequence available for alignment. Sequence reads are assembled as contigs and the coverage quality of *de novo* sequence data depends on the size and continuity of the contigs (ie, the number of gaps in the data). Another important factor in generating high-quality *de novo* sequences is the diversity of insert sizes included in the library. Combining short-insert paired-end and long-insert mate pair sequences is the most powerful approach for maximal coverage across the genome (Figure 7). The combination of insert sizes enables detection of the widest range of structural variant types and is essential for accurately identifying more complex rearrangements. The short-insert reads, sequenced at higher depths, can fill in gaps not covered by the long inserts, which are often sequenced at lower read depths. Therefore, using a combined approach results in higher quality assemblies. In parallel with NGS technology improvements, many algorithmic advances have emerged in sequence assemblers for short-read data. Researchers can perform high-quality *de novo* assembly using NGS reads and publicly available short-read assembly tools with existing computer resources in the laboratory.

**Figure 7: Mate Pairs and De novo Assembly**—Using a combination of short and long insert sizes with paired-end sequencing results in maximal coverage of the genome for *de novo* assembly.

### Targeted Sequencing

With targeted sequencing, a subset of genes or regions of the genome are isolated and sequenced. Targeted sequencing allows researchers to focus time, expenses, and data analysis on specific areas of interest and enables sequencing at much higher coverage levels. For example, a typical WGS study achieves coverage levels of 30–$50\times$ per genome, while a targeted resequencing project can easily cover the target region at 500–$1000\times$ or higher. This higher coverage allows researchers to identify rare variants, variants that would be too rare and too expensive to identify with WGS or CE-based sequencing.

Targeted sequencing panels can be purchased with fixed, preselected content or can be custom designed. A wide variety of targeted sequencing library prep kits are available, including kits with probe sets focused on specific areas of interest such as cancer, cardiomyopathy, or autism. Custom probe sets are available through DesignStudio™ Software enabling researchers to target regions of the genome relevant to specific research interests. Custom targeted sequencing is ideal for examining genes in specific pathways, or for follow-up studies from GWAS or WGS. Illumina currently supports two methods for targeted sequencing, target enrichment and amplicon generation (Figure 8).

Target enrichment captures between 10 kb–62 Mb regions, depending on the library prep kit parameters. Amplicon sequencing allows researchers to sequence 16–1536 targets at a time, spanning 2.4–652.8 kb of total content, depending on the library prep kit used. This highly multiplexed approach enables a wide range of applications for discovery, validation, or screening of genetic variants. Amplicon sequencing is useful for discovery of rare somatic mutations in complex samples (eg, cancerous tumors mixed with germline DNA).$^{15,16}$ Another common amplicon application is sequencing the bacterial 16S rRNA gene across multiple species, a widely used method for phylogeny and taxonomy studies, particularly in diverse metagenomic samples.$^{17}$

For more information on Illumina targeted, WGS, exome, or *de novo* sequencing solutions, visit www.illumina.com/applications/sequencing/dna_sequencing.html.

**Figure 8: Target Enrichment and Amplicon Generation Workflows**—With target enrichment, specific regions of interest are captured by hybridization to biotinylated probes, then isolated by magnetic pulldown. Amplicon sequencing involves the amplification and purification of regions of interest using highly multiplexed PCR oligos sets.

## b. Transcriptomics

Library preparation methods for RNA-Seq typically begin with total RNA sample preparation followed by a ribosome removal step. The total RNA sample is then converted to cDNA before standard NGS library preparation. RNA-Seq focused on mRNA, small RNA, noncoding RNA, or microRNAs can be achieved by including additional isolation or enrichment steps before cDNA synthesis (Figure 9).

**Figure 9: A Complete View of Transcriptomics with NGS**—A broad range of methods for transcriptomics with NGS have emerged over the past 10 years including total RNA-Seq, mRNA-Seq, small RNA-Seq, and targeted RNA-Seq.

### Total RNA and mRNA Sequencing

Transcriptome sequencing is a major advance in the study of gene expression because it allows a snapshot of the whole transcriptome rather than a predetermined subset of genes. Whole-transcriptome sequencing provides a comprehensive view of a cellular transcriptional profile at a given biological moment and greatly enhances the power of RNA discovery methods. As with any sequencing method, an almost unlimited dynamic range allows identification and quantification of both common and rare transcripts. Additional capabilities include aligning sequencing reads across splice junctions, and detection of isoforms, novel transcripts, and gene fusions. Library preparation kits that support precise detection of strand orientation are available for both total RNA-Seq and mRNA-Seq methods.

### Targeted RNA Sequencing

Targeted RNA sequencing is a method for measuring transcripts of interest for detecting differential expression, allele-specific expression, detection of gene-fusions, isoforms, cSNPs, and splice junctions. Illumina TruSeq$^\circledR$ Targeted RNA Sequencing Kits include preconfigured, experimentally validated panels focused on specific cellular pathways or disease states such as apoptosis, cardiotoxicity, NF$\kappa$B pathway, and more. Custom content can be designed and ordered for analysis of specific genes of interest. Targeted RNA sequencing is a powerful method for the investigation of specific pathways of interest or for the validation of gene expression microarray or whole-transcriptome sequencing results.

### Small RNA and Noncoding RNA Sequencing

Small, noncoding RNA, or microRNAs are short, 18–22 bp nucleotides that play a role in the regulation of gene expression often as gene repressors or silencers. The study of microRNAs has grown as their role in transcriptional and translational regulation has become more evident.$^{18,19}$

For more information regarding Illumina solutions for small RNA (noncoding RNA), targeted RNA, total RNA, and mRNA sequencing, visit www.illumina.com/applications/sequencing/rna.html.

## c. Epigenomics

While genomics involves the study of heritable or acquired alterations in the DNA sequence, epigenetics is the study of heritable changes in gene activity caused by mechanisms other than DNA sequence changes. Mechanisms of epigenetic activity include DNA methylation, small RNA–mediated regulation, DNA–protein interactions, histone modification, and more.

### Methylation Sequencing

A critical focus in epigenetics is the study of cytosine methylation (5mC) states across specific areas of regulation, such as promotors or heterochromatin. Cytosine methylation can significantly modify temporal and spatial gene expression and chromatin remodeling.$^{20}$ While there are many methods for the study of genetic methylation, methylation sequencing leverages the advantages of NGS technology and genome-wide analysis while assessing methylation states at the single-nucleotide level. Two methylation sequencing methods are widely used: whole-genome bisulfite sequencing (WGBS) and reduced representation bisulfite sequencing (RRBS). With WGBS, sodium bisulfite chemistry converts nonmethylated cytosines to uracils, which are then converted to thymines in the sequence reads or data output. In RRBS, DNA is digested with MspI, a restriction enzyme unaffected by methylation status. Fragments in the 100–150 bp size range are isolated to enrich for CpG and promotor containing DNA regions. Sequencing libraries are then constructed using the standard NGS protocols.

For more information on methylation sequencing solutions, visit www.illumina.com/techniques/sequencing/methylation-sequencing.html

### ChIP Sequencing

Protein–DNA or protein–RNA interactions have a significant impact on many biological processes and disease states. These interactions can be surveyed with NGS by combining chromatin immunoprecipitation (ChIP) assays and NGS methods. ChIP-Seq protocols begin with the chromatin immunoprecipitation step (ChIP protocols vary widely as they must be specific to the species, tissue type, and experimental conditions).

For more information on ChIP-Seq, visit www.illumina.com/techniques/sequencing/dna-sequencing/chip-seq.html.

### Ribosome Profiling

Ribosome profiling is a method based on deep sequencing of ribosome protected–mRNA fragments. Purification and sequencing of these fragments provides a "snapshot" of all the ribosomes active in a cell at a specific time point. This information can determine what proteins are being actively translated in a cell, and can be useful for investigating translational control, measuring gene expression, determining the rate of protein synthesis, or predicting protein abundance. Ribosome profiling enables systematic monitoring of cellular translation processes and prediction of protein abundance. Determining what regions of a transcript are being translated can help define the proteome of complex organisms. With NGS, ribosome profiling allows detailed and accurate *in vivo* analysis of protein production.

To learn more about Illumina ribosome profiling, visit www.illumina.com/applications/sequencing/rna.html.

---

[← I. Welcome to Next-Generation Sequencing](01-i-welcome-to-next-generation-sequencing.md) · [Up: contents](index.md) · [III. Illumina DNA-to-Data NGS Solutions →](03-iii-illumina-dna-to-data-ngs-solutions.md)
