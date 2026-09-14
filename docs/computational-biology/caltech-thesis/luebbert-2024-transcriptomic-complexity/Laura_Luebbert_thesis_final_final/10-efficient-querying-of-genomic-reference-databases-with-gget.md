---
title: Efficient Querying of Genomic Reference Databases with gget
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Efficient Querying of Genomic Reference Databases with gget

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Preamble**

This chapter describes the development of the software program _gget_ , which, since its release in May 2022, has been downloaded 97,000 times. _gget_ is a collection of separate, but interoperable modules and has grown to 16 modules to date, including several modules contributed by the _gget_ community. Beyond tackling endemic problems faced by the bioinformatics community accurately and efficiently, the success of _gget_ can be attributed to the factors and guidelines described in the introduction. The rationale behind _gget_ as described in the summary and introduction below is magnified when working with data from non-model organisms, as further described in Chapter 4 Part I.

**Laura Luebbert,** Lior Pachter (2023). Efficient querying of genomic reference databases with _gget_ . _Bioinformatics_ . https://doi.org/10.1093/bioinformatics/btac836

#### **Summary**

A recurring challenge in interpreting single-cell RNA-seq data is the assessment of results in the context of existing genomic databases. Currently, there is no tool implementing <mark>automated, easy programmatic access to information stored in a diverse collection of large, public genomic databases.</mark> _<mark>g</mark> get_ is a <mark>free and open-source command-line tool and Python package that enables efficient querying of genomic databases.</mark> _<mark>gget</mark>_ <mark>consists of a collection of separate but interoperable modules, each designed to facilitate one type of database querying required for single-cell RNA-seq data analysis in a single line of code.</mark> The manual and source code are available at <u>https://github.com/pachterlab/gget.</u>

#### **Introduction**

<mark>The increasingly common use of single-cell RNA-seq to provide transcriptomic characterization of cells is dependent on quick and easy access to reference information stored in large genomic databases such as Ensembl, NCBI, and UniProt (Cunningham</mark> _<mark>et al.</mark>_ <mark>, 2022; NCBI Resource Coordinators, 2013; UniProt Consortium, 2021). A majority of researchers currently access genomic databases to annotate and functionally characterize putative marker genes through web access (Stalker</mark> _<mark>et al.</mark>_ <mark>, 2004; Birney</mark> _<mark>et al.</mark>_ <mark>, 2004). This process is time-consuming and error-prone, as it requires manually copying and pasting data, such as gene IDs.</mark>

To facilitate and automate functional annotation for single-cell RNA-seq analyses, we developed _gget:_ a <mark>free and open-source software package that rapidly queries information stored in several large, public databases directly from a</mark> command line <mark>or Python environment.</mark> _<mark>gget</mark>_ <mark>consists of a collection of tools designed to perform the database querying required for single-cell RNA-seq data analysis in a single line of code. In addition</mark>

10


**Figure 2.1** Overview of the nine _gget_ tools and the public databases they access. One simple command line ($) example and its Python (>>>) equivalent are shown for each tool with the corresponding output.

<mark>to providing access to genomic databases,</mark> _<mark>gget</mark>_ <mark>can also leverage sequence analysis tools, such as BLAST (Altschul</mark> _<mark>et al.</mark>_ <mark>, 1990, 1997), thus simplifying complex annotation workflows.</mark>

While there are some web-based Application Programming Interface (API) data mining systems, such as BioMart (Durinck _et al._ , 2005; Kasprzyk _et al._ , 2004), we identified several limitations in such tools, including limits to query types and to utilizing databases in tandem. Moreover, large-scale single-cell RNA-seq analysis is better served by command line or packaged APIs that can fetch data directly into programming environments.

The _gget_ modules combine MySQL (Oracle Corporation, 1995), API, and web data extraction queries to rapidly and reliably request comprehensive information from different databases (Figure 2.1). This approach allows _gget_ to perform tasks unsupported by existing tools built around standard API queries (de Ruiter, 2016). For instance, searching for genes and transcripts using free-form search terms. Each _gget_ tool requires minimal arguments, provides clear output, and operates from both the command line and Python environments, such as JupyterLab, maximizing ease of use and accommodating novice programmers.

11

#### **Description**

_gget_ consists of nine tools:

- _<mark>gget ref:</mark>_ <mark>Fetch File Transfer Protocols (FTPs) and metadata for reference genomes or annotations from Ensembl by species.</mark>

- _<mark>gget search:</mark>_ <mark>Fetch genes or transcripts from Ensembl using free-form search terms.</mark>

- <mark>●</mark> _<mark>gget info</mark>_ <mark>: Fetch extensive gene or transcript metadata from Ensembl, UniProt, and NCBI by Ensembl ID.</mark>

- _<mark>gget seq:</mark>_ <mark>Fetch nucleotide or amino acid sequences of genes or transcripts from Ensembl or UniProt by Ensembl ID.</mark>

- _<mark>gget blast:</mark>_ <mark>BLAST (Altschul</mark> _<mark>et al.</mark>_ <mark>, 1990, 1997) a nucleotide or amino acid sequence to any BLAST database.</mark>

- _<mark>gget blat:</mark>_ <mark>Find the genomic location of a nucleotide or amino acid sequence using BLAT (James Kent, 2002).</mark>

- _<mark>gget muscle:</mark>_ <mark>Align multiple nucleotide or amino acid sequences to each other using the Muscle5 algorithm (Edgar, 2021).</mark>

- _<mark>gget enrichr:</mark>_ <mark>Perform an enrichment analysis on a list of genes using Enrichr (Chen</mark> _<mark>et al.</mark>_ <mark>, 2013; Xie</mark> _<mark>et al.</mark>_ <mark>, 2021; Kuleshov</mark> _<mark>et al.</mark>_ <mark>, 2016) and an extensive collection of gene set libraries, including KEGG (Kanehisa and Goto, 2000; Kanehisa, 2019; Kanehisa</mark> _<mark>et al.</mark>_ <mark>, 2021) and Gene Ontology (Ashburner</mark> _<mark>et al.</mark>_ <mark>, 2000; Gene Ontology Consortium, 2021).</mark>

- _<mark>gget archs4:</mark>_ <mark>Find the most correlated genes to a gene of interest or find the gene's tissue expression atlas using ARCHS4 (Lachmann</mark> _<mark>et al.</mark>_ <mark>, 2018).</mark>

<mark>Each</mark> _<mark>gget</mark>_ <mark>tool accesses data stored in one or several public databases, as depicted in Figure 2.1.</mark> _<mark>gget</mark>_ <mark>fetches the requested data in real-time, guaranteeing that each query will return the latest information. One exception is</mark> _<mark>gget muscle</mark>_ <mark>, which locally compiles the Muscle5 algorithm (Edgar, 2021) and therefore does not require an internet connection.</mark>

_gget info_ combines information from Ensembl, NCBI, and UniProt (Cunningham _et al._ , <mark>2022; NCBI Resource Coordinators, 2013; UniProt Consortium, 2021) to provide the user with a comprehensive executive summary of the available information about a gene or transcript. This also enables users to assert whether data from different sources are consistent.</mark>

By accessing the NCBI server (NCBI Resource Coordinators, 2013) through HTTP <mark>requests,</mark> _<mark>gget blast</mark>_ <mark>does not require the download of a reference BLAST database, as is the case with existing BLAST tools (Buchfink</mark> _<mark>et al.</mark>_ <mark>, 2021; Camacho</mark> _<mark>et al.</mark>_ <mark>, 2009). The whole self-contained</mark> _<mark>gget</mark>_ <mark>package is approximately 3 MB after installation.</mark>

The package dependencies were carefully chosen and kept to a minimum. _gget_ depends on <mark>the HTML parser</mark> _<mark>beautifulsoup4</mark>_ <mark>(Richardson, 2022), the Python MySQL-connector (Oracle, 2022), and the HTTP library</mark> _<mark>requests</mark>_ <mark>(Reitz, 2022). All of these are wellestablished packages for server interaction in Python.</mark> _<mark>gget</mark>_ <mark>has been tested on Linux/Unix, Mac OS (Darwin), and Windows.</mark>

12

#### **Usage and documentation**

_gget_ can be installed from the command line by running ‘pip install gget’. Figure 2.1 depicts one use case for each _gget_ tool with the corresponding output.

Each _gget_ tool features an extensive manual available as function documentation in a Python environment or as standard output using the help flag [-h] in the command line. The complete manual with examples can be viewed in the _gget_ repository, available at <u>https://github.com/pachterlab/gget. A separate</u> _gget examples_ repository is accessible at <u>https://github.com/pachterlab/gget_examples and includes exemplary workflows</u> immediately executable in Google Colaboratory (Bisong, 2019).

#### **Discussion**

Our open-source Python and command-line program _gget_ <mark>enables efficient and easy programmatic access to information stored in a diverse collection of large, public genomic databases.</mark> The _gget_ modules were motivated by experience with tedious single-cell RNAseq data analysis tasks (Supplementary Figure 2.1), however, we anticipate their utility for a wide range of bioinformatics tasks.

#### **Acknowledgments**

We thank Kyung Hoi (Joseph) Min for advice on the command-line interface, Matteo Guareschi for advice on Windows operability, and A. Sina Booeshaghi, Kristján Eldjárn Hjörleifsson, and Ángel Gálvez-Merchán for insightful discussions about _gget_ . Cartoons in Figure 2.1 and Supplementary Figure 2.1 were created with BioRender.com. Thanks to the wonderful staff at Dash Coffee Bar in Pasadena, who occasionally gave LL free banana bread to sustain this work.

13


**Supplementary Figure 2.1** _gget_ performs the database querying underlying a standard single-cell RNA-seq data analysis workflow. The workflow and all of the figures are reproducible starting with raw reads using immediately executable Google Colaboratory notebooks that can be run for free and are accessible at <u>https://github.com/pachterlab/gget_examples/tree/main/scRNAseq_workflow.</u>

14

#### **References**

- Altschul, S.F. _et al._ (1990) Basic local alignment search tool. _J. Mol. Biol._ , **215** , 403–410. Altschul, S.F. _et al._ (1997) Gapped BLAST and PSI-BLAST: A new generation of protein database search programs. _Nucleic Acids Res._ , **25** , 3389–3402.

- Ashburner, M. _et al._ (2000) Gene ontology: Tool for the unification of biology. The Gene Ontology Consortium. _Nat. Genet._ , **25** , 25–29.

- Birney, E. _et al._ (2004) An overview of Ensembl. _Genome Res._ , **14** , 925–928.

- Bisong, E. (2019) Google Colaboratory. _Building Machine Learning and Deep Learning Models on Google Cloud Platform_ , 59–64.

- Buchfink, B. _et al._ (2021) Sensitive protein alignments at tree-of-life scale using DIAMOND. _Nat. Methods_ , **18** , 366–368.

- Camacho, C. _et al._ (2009) BLAST+: Architecture and applications. _BMC Bioinformatics_ , **10** , 421.

- Chen, E.Y. _et al._ (2013) Enrichr: Interactive and collaborative HTML5 gene list enrichment analysis tool. _BMC Bioinformatics_ , **14** , 128.

- Cunningham, F. _et al._ (2022) Ensembl 2022. _Nucleic Acids Res._ , **50** , D988–D995.

- Durinck, S. _et al._ (2005) BioMart and Bioconductor: A powerful link between biological databases and microarray data analysis. _Bioinformatics_ , **21** , 3439–3440.

- Edgar, R.C. (2021) MUSCLE v5 enables improved estimates of phylogenetic tree confidence by ensemble bootstrapping. _bioRxiv_ .

- Gene Ontology Consortium (2021) The Gene Ontology resource: Enriching a GOld mine. _Nucleic Acids Res._ , **49** , D325–D334.

- James Kent, W. (2002) BLAT—The BLAST-Like Alignment Tool. _Genome Res._ , **12** , 656– 664.

- Kanehisa, M. _et al._ (2021) KEGG: Integrating viruses and cellular organisms. _Nucleic Acids Res._ , **49** , D545–D551.

- Kanehisa, M. (2019) Toward understanding the origin and evolution of cellular organisms. _Protein Sci._ , **28** , 1947–1951.

- Kanehisa, M. and Goto,S. (2000) KEGG: kyoto encyclopedia of genes and genomes. _Nucleic Acids Res._ , **28** , 27–30.

- Kasprzyk, A. _et al._ (2004) EnsMart: A generic system for fast and flexible access to biological data. _Genome Res._ , **14** , 160–169.

- Kuleshov, M.V. _et al._ (2016) Enrichr: A comprehensive gene set enrichment analysis web server 2016 update. _Nucleic Acids Res._ , **44** , W90–7.

- Lachmann, A. _et al._ (2018) Massive mining of publicly available RNA-seq data from human and mouse. _Nat. Commun._ , **9** , 1366.

- NCBI Resource Coordinators (2013) Database resources of the National Center for Biotechnology Information. _Nucleic Acids Res._ , **41** , D8–D20.

- Oracle (2022) mysql-connector-python 8.0.29. Oracle Corporation (1995) MySQL https://www.mysql.com/.

- Reitz, K. (2022) requests 2.27.1. Richardson, L. (2022) beautifulsoup4 4.11.1. de Ruiter, J. (2016) PyBiomart 0.2.0 https://jrderuiter.github.io/pybiomart/.

- Stalker, J. _et al._ (2004) The Ensembl Web site: Mechanics of a genome browser. _Genome Res._ , **14** , 951–955.

15

UniProt Consortium (2021) UniProt: The universal protein knowledgebase in 2021. _Nucleic Acids Res._ , **49** , D480–D489.

Xie, Z. _et al._ (2021) Gene Set Knowledge Discovery with Enrichr. _Curr. Protoc._ , **1** , e90.

16

<mark>SOFTWARE FOR BIOLOGISTS BY BIOLOGISTS - PART II</mark>

---

[← SOFTWARE FOR BIOLOGISTS BY BIOLOGISTS - PART I](09-software-for-biologists-by-biologists---part-i.md) · [Up: contents](index.md) · [Fast and Scalable Querying of Eukaryotic Linear Motifs with gget elm →](11-fast-and-scalable-querying-of-eukaryotic-linear-motifs-with.md)
