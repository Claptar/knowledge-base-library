---
title: From Beaker to (Peta)Byte
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# From Beaker to (Peta)Byte

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Over the past decade, the ‘omics’ era of the life sciences has led to a significant increase in the volume and complexity of biological data. The Sequence Read Archive, which stores raw sequencing data and alignment information, has grown to >30 petabases since its establishment in 2012<sup>1</sup> . In 1996, the NCBI GenBank, which stores annotated DNA sequences, was sent to subscriber’s homes in the format of 7 CDs (Figure 1.1). Today, GenBank contains 2.5 billion sequences, and one would require 5,703 CDs (assuming a capacity of 700 MB per CD) to follow GenBank’s original distribution model (the GenBank Release 258.0 (https://www.ncbi.nlm.nih.gov/genbank/release/258) requires roughly 3,992 GB of disk space). To store the Sequence Read Archive on CDs, one would require upwards of 42,857,143 CDs. To tackle the increasing size, as well as the heterogenicity and noisiness of omics data, a myriad of software programs continues to be released daily.

As a wet-lab geneticist who learned how to code and switched to the field of computational biology during her Ph.D., I noticed that there were often overlooked yet crucial factors beyond how well a software program performs its designated function that contribute heavily to whether a program will be widely implemented. I incorporated these into the software programs described in this thesis, which were instantly adopted and became a worldwide standard in the analysis of transcriptomic and proteomic data analysis (Figure 1.2). Here, I will describe and quantify some of these factors.

I will use the software tools documented in the scRNA-tools database<sup>2</sup> <u>(https://www.scrnatools.org/) to model the current state of software</u> released to support omics research. Single-cell RNA sequencing (scRNA-seq) is a method to measure all RNA molecules in thousands of individual cells in parallel while retaining single-cell resolution, and it is one of the most widely used omics technologies that emerged over the past decade. According to the scRNA-tools database, 1,706 software programs were released between September 2016 and January 2024 for the analysis of scRNA-seq data – approximately one tool every second day. 107 of these tools were not published. To get an estimate of the extent to which the tools were used in practice, Figure 1.3 shows the number of citations of tools that


**Figure 1.1** Photograph of the CDs containing release 97.0 of the NCBI GenBank database as distributed to subscribers in 1996. Courtesy of Prof. Lior Pachter.


<!-- Start of picture text -->
2<br><!-- End of picture text -->


**Figure 1.2** The number of active users of the _gget_ website (https://pachterlab.github.io/gget/) by country between November 2023 and February 2024. The code to reproduce this figure can be found here: <u>https://github.com/lauraluebbert/lauraluebbert.</u>

were published between September 2016 and December 2022 (to allow at least one year to gather citations). I note that this method will be biased towards tools that have had more time to accumulate citations. Only 35 (3 %) of published tools received over 1,000 citations, suggesting extensive use, with the most highly cited tools STAR<sup>3</sup> , Seurat<sup>4</sup> , Monocle<sup>5</sup> , Salmon<sup>6</sup> , and kallisto<sup>7</sup> having been cited 32,005, 29,316, 7,912, 7,030, and 7,011 times, respectively. 490 (46 %) of published tools received less than 20 citations. This indicates that almost half of peer-reviewed software programs published for analyzing scRNA-seq data are barely used in practice. To understand the difference between tools that end up being widely used and those that don’t, we first need to understand the user base.

Omics data is highly complex, both in terms of the computational requirements of its analysis and the underlying biological implications. To rigorously analyze and interpret highdimensional omics data, extensive knowledge in both computer science and biology is required. However, only recently have undergraduate and graduate biology programs begun to include advanced programming classes in their curriculums, and many biology students still begin their Ph.D. and PostDoc positions with no to minimal coding skills<sup>8,9</sup> . Hence, widely used omics tools need to accommodate novice programmers. From my experience as I evolved from novice programmer to writing software for novice and advanced bioinformaticians, there are three major obstacles an omics software’s user interface needs to overcome for successful, widespread, and long-lived implementation: installation, documentation, and updates.

#### _Installation_

The first hurdle when using a new software program is the installation. There are several program repositories and associated package managers that greatly simplify the installation of software programs. For Python programs, the most widely used program repositories for omics software are _PyPI_ and _Bioconda_ . Both allow the installation of software in a single line of code, greatly simplifying the process compared to requiring users to run a container

3


**Figure 1.3** The number of citations for software tools used in the analysis of scRNA-seq data published between September 2016 and December 2022 according to the scRNA-tools database (https://www.scrna- <u>tools.org/). The top plot shows the histogram for all published tools. The first bin in the top plot consists of</u> tools with 0-100 citations and is broken down further in the bottom plot. The code to reproduce this figure can be found here: https://github.com/lauraluebbert/PhD_thesis/blob/main/Chapter1_Introduction.ipynb.

application, e.g., through Docker, or compile the software from source code. Even without testing whether the installation is functional, highly cited Python tools are more likely to have available PyPI and/or Bioconda installations (Figure 1.4A).

#### _Documentation_

Next, the user needs to learn how to use the newly installed software program. Ideally, software documentation is provided in the form of Python/R function descriptions, shell script help arguments, a GitHub README and/or wiki, and/or a separate documentation website. All 35 published tools with over 1,000 citations in the scRNA-tools database provide an extensive, publicly available manual containing software documentation, installation guidelines, quick start guides, and tutorials (Table 1.1). Except for the programs BackSPIN, CellChat, DoubletFinder, Scrublet, and MAGIC, for which documentation and tutorials are included in the GitHub README, these manuals are hosted on a website separate from the GitHub code repository. The Bioconductor project has set a commendable example by requiring contributors to adhere to a minimum standard of guidelines outlining, amongst others, package documentation <u>(contributions.bioconductor.org). The accessibility of the documentation can be further</u> increased by following Americans with Disabilities Act (ADA) guidelines for web content, as well as providing translations to different languages. Based on Google Analytics tracking of the documentation website for the software tool _gget_<sup>_10_</sup> <u>(https://pachterlab.github.io/gget/),</u> further described in Chapter 2, the number of Spanish-speaking users increased by 35 %

4


<!-- Start of picture text -->
A  B<br><!-- End of picture text -->

**Figure 1.4 A** Fraction of published Python software tools in the scRNA-tools database (https://www.scrna- <u>tools.org/) with available installations from PyPI or Bioconda binned by number of citations.</u> **B** Fraction of software tools in the scRNA-tools database (https://www.scrna-tools.org/) released between September 2016 and December 2022 for which the last GitHub commit was at least 6 months after the initial software release binned by number of citations. The code to reproduce these figures can be found here: <u>https://github.com/lauraluebbert/PhD_thesis/blob/main/Chapter1_Introduction.ipynb.</u>

(from an average 3.1 to 4.2 new users per month) after the _gget_ documentation was also made available in Spanish.

#### _Updates_

With the pressure to produce and publish in academic research, it may be tempting to move on to the next project after the release of a software program and forget all about the latter. However, as omics methods evolve, data structures and package dependencies are likely to be updated or changed, and programs must also evolve with these updates to provide continued usability. Figure 1.4B shows the fraction of tools in the scRNA-tools database released between September 2016 and December 2022, for which the latest GitHub commit was at least six months after the initial release of the software tool. Using the latest GitHub commit as an indicator for a software update, 91.4 % of highly cited (>500 citations) software programs were updated after the initial release compared to 47.4 % of less cited (0-10 citations) programs (Figure 1.4B).

The following subchapter lists specific guidelines for user-friendly omics technologies based on the factors discussed here. User-friendliness is especially important when catering to novice programmers, including a large fraction of the biologists generating the omics data these software tools are designed to analyze. However, making it easier for beginners makes it easier for everyone, which increases the chances of the software being implemented.

5

The guidelines described in the following subchapter are intended to complement widely accepted best practices in software engineering, such as code quality control, testing, debugging, version control, formatting, and documentation, including comments and meaningful commit messages.

All software described in this thesis, though varying in purpose, followed these guidelines and was rapidly adopted by the bioinformatics community. Where applicable, I also adhered to these guidelines when releasing auxiliary code and workflows used for downstream analyses (Chapters 3-5), which resulted in the added benefit of maximizing reproducibility.

#### **References**

1. Katz, K. _et al._ The Sequence Read Archive: A decade more of explosive growth. _Nucleic Acids Res._ **50** , D387–D390 (2022).

2. Zappia, L., Phipson, B. & Oshlack, A. Exploring the single-cell RNA-seq analysis landscape with the scRNA-tools database. _PLoS Comput. Biol._ **14** , (2018).

3. Dobin, A. _et al._ STAR: Ultrafast universal RNA-seq aligner. _Bioinformatics_ **29** , 15– 21 (2013).

4. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. Spatial reconstruction of single-cell gene expression data. _Nat. Biotechnol._ **33** , 495–502 (2015).

5. Trapnell, C. _et al._ The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells. _Nat. Biotechnol._ **32** , 381–386 (2014).

6. Patro, R., Duggal, G., Love, M. I., Irizarry, R. A. & Kingsford, C. Salmon provides fast and bias-aware quantification of transcript expression. _Nat. Methods_ **14** , 417–419 (2017).

7. Bray, N. L., Pimentel, H., Melsted, P. & Pachter, L. Near-optimal probabilistic RNAseq quantification. _Nat. Biotechnol._ **34** , 525–527 (2016).

8. Dreyfuss, E. Want to Make It as a Biologist? Better Learn to Code. _WIRED_ (2017). 9. Gammie, A., Lorsch, J. & Singh, S. Catalyzing the Modernization of Graduate Education. _NIGMS Feedback Loop Blog – National Institute of General Medical Sciences_ (2015).

10.  Luebbert, L. & Pachter, L. Efficient querying of genomic reference databases with gget. _Bioinformatics_ **39** , 4–6 (2023).

6

|**Name**|**Platform**|**Citations**|**Website/**<br>**Manual**|**Manual type**|**Tutorials/**<br>**Vignettes**|
|---|---|---|---|---|---|
|STAR|C/C++|32,005|Link|Separate website|Yes|
|Seurat|R|29,316|Link|Separate website|Yes|
|Monocle|R|7,912|Link|Bioconductor standard|Yes|
|salmon|C++|7,030|Link|Separate website|Yes|
|kallisto|C/C++|7,011|Link|Separate website|Yes|
|Scanpy|Python|4,481|Link|Separate website|Yes|
|CellRanger|Python/R|4,084|Link|Separate website|Yes|
|inferCNV|R|3,329|Link|GitHub Wiki|Yes|
|SCENIC|R/Python|3,328|Link|Separate website|Yes|
|Harmony|R/C++|3,241|Link|Separate website|Yes|
|CellPhoneDB|Python|3,103|Link|Separate website|Yes|
|AUCell|R|2,878|Link|Separate website|Yes|
|BackSPIN|Python|2,501|Link|GitHub README|Yes|
|velocyto|Python/R|2,497|Link|Separate website|Yes|
|scran|R|2,329|Link|Bioconductor standard|Yes|
|SingleR|R|2,129|Link|Bioconductor standard|Yes|
|scvi-tools|Python|2,086|Link|Separate website|Yes|
|CellChat|R/C++|1,948|Link|GitHub README|Yes|
|MAST|R|1,918|Link|Bioconductor standard|Yes|
|Rsubread|R|1,616|Link|Bioconductor standard|Yes|
|DoubletFinder|R|1,533|Link|GitHub README|Yes|
|batchelor|R|1,513|Link|Bioconductor standard|Yes|
|slingshot|R|1,470|Link|Bioconductor standard|Yes|
|scVelo|Python|1,454|Link|Separate website|Yes|
|SCDE|R|1,412|Link|Separate website|Yes|
|MiXCR|Java/Kotlin|1,371|Link|Separate website|Yes|
|UMI-tools|Python|1,253|Link|Separate website|Yes|
|Scrublet|Python|1,214|Link|GitHub README|Yes|
|Scater|R|1,212|Link|Bioconductor standard|Yes|
|scuttle|R/C++|1,212|Link|Bioconductor standard|Yes|
|MAGIC|Python/R/MATLAB|1,147|Link|GitHub README|Yes|
|SC3|R|1,128|Link|Bioconductor standard|Yes|
|MIMOSCA|Python|1,090|Link|GitHub README|Yes|
|dynverse|R|1,036|Link<br>|Separate website|Yes|
|bseqsc|R|1,007|Link<br>(broken)|Separate website|Yes|


**Table 1.1** The 35 most highly cited (>1000 citations) software tools for the analysis of scRNA-seq data published between September 2016 and December 2022 according to the scRNA-tools database (https://www.scrna-tools.org/).

7

---

[← INTRODUCTION – PART I](05-introduction-part-i.md) · [Up: contents](index.md) · [INTRODUCTION – PART II →](07-introduction-part-ii.md)
