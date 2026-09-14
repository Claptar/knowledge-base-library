---
title: Challenges and Solutions
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Challenges and Solutions

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The first step in the analysis of single-cell RNA sequencing data following standard analysis workflows is the alignment of the data to a reference genome. This assumes that a reference genome for the species of interest is available. As discussed in Chapter 2, the number of viruses with the potential to cause human infectious disease is eclipsed by the comparatively few viruses with complete reference genomes. In the workflows described in Chapter 2, this challenge is overcome by identifying protein domains that were highly conserved across species. Assuming that a genome is available, the alignment quality will depend on the quality of the genome assembly, including the percentage of gaps in the assembly, annotation of protein-encoding and non-coding genes, including isoforms and gene candidates, and haplotype completeness. While there are high-quality genome assemblies for widely studied organisms such as human, mouse, and rhesus macaque, the quality of genome assemblies for other species quickly decreases (Figure 4.1).


**Figure 4.1** Number of gaps and contig N50 lengths for different mammalian genomes, including human (GRCh38.p13), mouse (GRCm38.p6), and rhesus macaque (Mmul_10). Reproduced from Warren _et al_ .<sup>1</sup>

The following subchapter presents the results obtained through single-cell RNA sequencing of the non-model organism _Taeniopygia guttata_ (zebra finch). This dataset was the first single-cell RNA sequencing dataset generated from zebra finch tissue. While the zebra finch was the second avian species, after chicken, to have its genome sequenced, at the time the analysis discussed below was performed, the zebra finch genome coverage was only 88.2x with a contig N50 of 12 Mb (compared to 67.8 Mb for the human genome assembly GRCh38). Moreover, depending on which assembly and version are used, different results may be obtained. This problem is further complicated when the difference between reference genomes is not documented comprehensively.

79


**Figure 4.2** Example commands and results obtained using the _gget search_ module for the search term ‘HLADRA,’ showing how the annotation for this gene changed between two different Ensembl releases (109 and 110).

For example, between the zebra finch reference genomes GCA_003957565.2 (available on Ensembl) and GCA_003957565.4 (available on NCBI), the haplotypes were switched, with bTaeGut1_v1 containing the first haplotype (GCA_003957565.2) and bTaeGut1.4.pri the alternative haplotype (GCA_003957565.4). Both genomes should be derived from the male zebra finch ‘Black17’. However, according to the fna files of bTaeGut1.4.pri (GCA_003957565.4) provided by RefSeq (GCF_003957565.2 as listed on <u>https://www.ncbi.nlm.nih.gov/assembly/GCA_003957565.4), all chromosomes originated</u> from the female zebra finch ‘Blue55’. Moreover, only bTaeGut1.4.pri includes information from mitochondrial (MT) chromosomes, which is crucial for the assessment of cell health. The bTaeGut1.4.pri fna file provided by GenBank (GCA_003957565.4) is annotated as Black17, as expected (GCA_003957565.4_bTaeGut1.4.pri_genomic.fna). However, MT chromosomes are not immediately included, but available in a separate fna file. Additionally, chromosome W from the female bird Blue 55 is also not included in the general fna file, but is available when each chromosome is downloaded separately. This is not a problem for the analysis below, since all of those animals were male.

To make sense of the different assemblies and allow reproducible retrieval over time as assemblies get updated, I developed the _gget ref_ module<sup>3</sup> , which allows version-controlled retrieval of genome assemblies from Ensembl<sup>2</sup> (further described in Chapter 2).

Beyond incomplete genome sequence coverage, lower-quality reference genome assemblies tend to lack transcriptome annotations. In Ensembl genome assemblies, genes and transcripts are annotated with Ensembl IDs. For example, gene ENSG00000167360 encodes transcript ENST00000300778. Since these IDs do not contain any biological information, ideally, each ID has metadata associated with it, including the gene name and a description. However, in the zebra finch assembly GCA_003957565.2 (May 2019), 23.8 % of Ensembl IDs had no associated metadata. This often led to unannotated genes of interest obtained through clustering and differential gene expression analyses (described in the following subchapter). As a result, the Ensembl ID was the only information obtained about the gene of interest, which does not allow any further biological interpretation. This problem was the initial motivation behind writing the first _gget_<sup>_3_</sup> module, _gget info_ (also see Chapter 2), which facilitates the retrieval of metadata about a gene from its Ensembl ID by combining information from several databases, including Ensembl<sup>2</sup> , NCBI<sup>4</sup> , and UniProt<sup>5</sup> .

80

Combining information from different databases increases the chance of finding information for genes with little to no annotation on Ensembl and allows the comparison of information stored in each database. Moreover, _gget_ ’s database version arguments allow continued reproducibility over time as databases get updated (Figure 4.2 shows an example of a gene name change between Ensembl releases). The _gget search_ module allows conversion in the other direction, from search terms or gene names to Ensembl IDs. Later modules, such as _gget blast_ and _gget seq,_ enable the retrieval of information about homologous genes in other species, which potentially have more extensively annotated reference genomes. Overall, the _gget_ suite of tools allows leveraging reference genome annotation across databases and species, allowing the analysis and interpretation of sequencing data from species with sparsely annotated reference genomes.

Augmenting transcriptome metadata using _gget_ does not solve the second problem of lowquality reference genomes: low coverage. Efforts such as the international Genome 10K (G10K) consortium<sup>6</sup> are working to develop cost-effective methods for producing highquality, comprehensive reference genome assemblies. Moreover, the translated alignment algorithm described in Chapter 3 may be co-opted to align bulk and single-cell RNA sequencing data to reference proteomes from homologous species. Alignment in the amino acid space will make the alignment more robust to silent nucleotide substitutions between homologs and potentially allow the analysis of sequencing data from species with a missing or low-quality reference genome.

81

#### **References**

1. Warren, W. C. _et al._ Sequence diversity analyses of an improved rhesus macaque genome enhance its biomedical utility. _Science (80-. )._ **370** , (2020).

2. Martin, F. J. _et al._ Ensembl 2023. _Nucleic Acids Res._ **51** , D933–D941 (2023). 3. Luebbert, L. & Pachter, L. Efficient querying of genomic reference databases with gget. _Bioinformatics_ **39** , 4–6 (2023).

4. Sayers, E. W. _et al._ Database resources of the national center for biotechnology information. _Nucleic Acids Res._ **50** , D20–D26 (2022).

5. Consortium, T. U. UniProt: the Universal Protein Knowledgebase in 2023 - Google Scholar. **51** , 523–531 (2023).

6. Rhie, A. _et al._ Towards complete and error-free genome assemblies of all vertebrate species. _Nature_ **592** , 737–746 (2021).

82

TRANSCRIPTOMICS IN NON-MODEL ORGANISMS – PART II

---

[← TRANSCRIPTOMICS IN NON-MODEL ORGANISMS – PART I](14-transcriptomics-in-non-model-organisms-part-i.md) · [Up: contents](index.md) · [Neuronal Dynamics of Behavior Recovery in Zebra Finches →](16-neuronal-dynamics-of-behavior-recovery-in-zebra-finches.md)
