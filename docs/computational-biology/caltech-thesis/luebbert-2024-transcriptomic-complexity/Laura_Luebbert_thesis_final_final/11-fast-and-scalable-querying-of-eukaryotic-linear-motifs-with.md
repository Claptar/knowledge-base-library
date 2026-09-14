---
title: Fast and Scalable Querying of Eukaryotic Linear Motifs with gget elm
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fast and Scalable Querying of Eukaryotic Linear Motifs with gget elm

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Preamble**

This subchapter describes the development of _gget elm_ , a recently published tool for highthroughput identification of protein-protein interaction motifs in amino acid sequences. The _gget elm_ module exemplifies how the _gget_ project provides a platform and backbone for the rapid development of novel modules that solve widely faced challenges in computational biology spanning various fields, in this case interactomics, proteomics, and molecular cell biology.

**Laura Luebbert,** Chi Hoang, Manjeet Kumar, Lior Pachter (2023). Fast and scalable querying of eukaryotic linear motifs with _gget elm_ . _Bioinformatics_ . <u>https://doi.org/10.1093/bioinformatics/btae095</u>

#### **Summary**

Eukaryotic linear motifs (ELMs), or Short Linear Motifs (SLiMs), are protein interaction modules that play an essential role in cellular processes and signaling networks and are often involved in diseases like cancer. The ELM database is a collection of manually curated motif knowledge from scientific papers. It has become a crucial resource for investigating motif biology and recognizing candidate ELMs in novel amino acid sequences. Users can search amino acid sequences or UniProt Accessions on the ELM resource web interface. However, as with many web services, there are limitations in the swift processing of large-scale queries through the ELM web interface or API calls, and, therefore, integration into protein function analysis pipelines is limited.

To allow swift, large-scale motif analyses on protein sequences using ELMs curated in the ELM database, we have extended the _gget_ suite of Python and command line tools with a new module, _gget elm_ , which does not rely on the ELM server for efficiently finding candidate ELMs in user-submitted amino acid sequences and UniProt Accessions. _gget elm_ increases accessibility to the information stored in the ELM database and allows scalable searches for motif-mediated interaction sites in the amino acid sequences.

The manual and source code are available at https://github.com/pachterlab/gget.

#### **Introduction**

Eukaryotic linear motifs (ELMs), also known as Short Linear Motifs (SLiMs), are short stretches of contiguous amino acids, typically 3 to 15 residues in length, encoding proteinprotein interaction sites. They are mainly located in the intrinsically disordered regions (IDRs) of proteins and are typically found to be highly conserved in orthologous proteins. These modules can encode multiple functionalities, which include modification, degradation, docking, targeting, and binding sites for protein domains. As such, ELMmediated interactions play an essential role in cellular processes and signaling networks, including the regulation of homeostasis, apoptosis, and differentiation (Van Roey _et al._ ,

17

2014; Davey _et al._ , 2012). Pathogens like SARS-CoV-2 mimic ELMs to gain entry into the cell (Kruse _et al._ , 2021; Mészáros _et al._ , 2021), and mutations in sequences containing ELMs contribute to diseases like cancer (Uyar _et al._ , 2014; Mészáros _et al._ , 2017). As a result, ELM-mediated protein interactions are potential targets for therapeutic intervention (Mészáros _et al._ , 2021; Simonetti _et al._ , 2023; Fasano _et al._ , 2022).

The ELM resource has two main components: an exploratory candidate motif search web interface and a database with manually curated linear motif knowledge, including information on binding partners and recognition features along with associated biological context. The database information is derived from the scientific literature by expert ELM curators who analyze motif-containing sequences to capture key insights, such as the residues involved in the interaction, their evolutionary conservation, local sequence context in flanking regions, features of the binding site on the interacting partner, and


**Figure 2.2** Runtime comparison for 50 amino acid sequences and 50 UniProt Accessions submitted to _gget elm_ and the ELM server API. For the ELM server API, a 3-minute wait time was observed between each request to comply with the server rules. These wait times were not taken into account when measuring the runtimes. The black dot denotes the mean. The code used to generate this figure can be found here: http://tinyurl.com/bdc6mhm3.

other motif-related insights. In addition, the curation process captures relevant information on the contextual knowledge, which includes cellular function, location, and taxonomic distribution of motif-containing proteins. Since the database was first created (Puntervoll _et al._ , 2003; Dinkel _et al._ , 2011), it has been continuously updated and has been widely used for both biomedical studies as well as interactomics, proteomics, and molecular research studies (Kumar _et al._ , 2020, 2022; Gouw _et al._ , 2018; Dinkel _et al._ , 2015; Carberry, 2008; Kumar _et al._ , 2023, Benz _et al_ ., 2022; Gogl _et al._ , 2022; Zhang _et al_ ., 2012; Reys and Labesse, 2022). Users can search amino acid sequences or UniProt Accessions on the ELM database web interface (http://elm.eu.org/) or by submitting an API request through the ELM server. However, these methods have processing limitations when performing large-scale queries, and many requests being submitted simultaneously can lead to server overload and extended wait times.

To expedite the investigation of ELMs, we have extended the _gget_ suite of Python and command line tools (Luebbert and Pachter, 2022) with a new module which efficiently finds ELMs in user-submitted amino acid sequences or UniProt Accessions: _gget elm_ . _gget elm_ increases accessibility to the information stored in the ELM database and allows scalable searches for ELMs in amino acid sequences. The command line interface and

18


**Figure 2.3** Schematic overview of the _gget elm_ back-end.

optional JSON formatted output allow swift integration into existing protein analysis workflows.

#### **Description**

Users can submit an amino acid sequence or a UniProt Accession to _gget elm_ . _gget elm_ captures both homology-based matches corresponding to curated motifs in orthologous proteins in the ELM database and POSIX regular expression (regex) matches corresponding to candidate motifs in the provided sequence. Hence, _gget elm_ returns two separate data frames (or JSON formatted dictionaries for use from the command line) containing the respective motif matches and extensive information about each motif. Figure 2.3 provides an overview of the _gget elm_ back-end.

19

After installing _gget_ <mark>($ pip install gget)</mark> , the user downloads the ELM database reference information using a specialized module, _gget setup_ , with the command <mark>$ gget setup elm.</mark> This command may be repeated at any time to update the local copy of the ELM database, which currently requires a total of 3 MB of disk space. The files are saved in the _gget_ installation directory. If the user submits a UniProt Accession to _gget elm_ and the protein is not present in the ELM database, its amino acid sequence is fetched from UniProt (UniProt Consortium, 2021). Using the DIAMOND alignment algorithm (Buchfink _et al._ , 2021), the sequence is compared to the motif-containing proteins in the ELM database. _gget elm_ returns all motifs associated with orthologous proteins, including information about each orthologous protein, and extensive details on each motif. _gget elm_ also returns alignment scores for each DIAMOND hit, including identity and coverage percentages and boolean output on whether the orthologous motif is contained within the overlapping region between the query and subject sequence. To compute the regex data frame, _gget elm_ considers all regex expressions from the ELM database and scans them against the provided amino acid sequence to report all matches. The data from the ELM database is combined to return relevant information about each matched interaction motif, including motif description, type, sequence, location in the ortholog and query sequence, and host taxonomy, for both data frames. How different types of user input traverse the _gget elm_ back-end is explored in this Google Colab notebook: <u>https://tinyurl.com/4bd5h8hr.</u>

_gget elm_ builds on existing _gget_ modules, such as _gget seq_ to fetch amino acid sequences from UniProt, and a new module developed in parallel with _gget elm_ : _gget diamond_ , which aligns sequences using the DIAMOND algorithm (Buchfink _et al._ , 2021) and can be used independently from _gget elm_ .

While _gget elm_ results are similar to results obtained through the ELM web interface, they may not be identical due to differences underlying the computations. For example, _gget elm_ uses DIAMOND for fast and sensitive local alignment of the amino acid sequences, whereas the ELM web interface has its own suite of back-end tools and deliberately limits the number of proteins in the output to be manageable for the web server (Chica _et al._ , 2008). In a comparison between the ‘regex’ data frame returned by _gget elm_ and the results obtained through the ELM server API for 50 amino acid sequences and 50 UniProt Accessions, _gget elm_ returned results 8x faster for amino acid sequences and 3.5x faster for UniProt Accessions on average (Figure 2.2). For the ELM server API, runtimes are further increased significantly by a mandatory 1-minute wait time between amino acid sequence requests, and a 3-minute wait time between UniProt Accession requests to comply with the server usage recommendations and avoid 429 errors. The results returned by both methods matched 100% across all tested amino acid sequences and UniProt Accessions. The code to reproduce this analysis can be found here: <u>http://tinyurl.com/bdc6mhm3.</u>

#### **Usage and Documentation**

Akin to all modules contained within _gget_ (Luebbert and Pachter, 2022) _, gget elm_ features an extensive manual available as function documentation in a Python environment or as standard output using the help flag [-h] in the command line. The accuracy of the returned

20 results is maintained through extensive unit tests, which automatically run on a biweekly basis. The complete manual with examples can be viewed on the _gget_ website in English <u>(https://pachterlab.github.io/gget/en/elm)</u> and in Spanish (https://pachterlab.github.io/gget/es/elm).

_gget_ can be installed from PyPI using the command line with the following command: <mark>$ pip install gget</mark> Alternatively, _gget_ can be installed using Anaconda: <mark>$ conda install -c bioconda gget</mark>

Example _gget elm_ commands to find ELMs in a protein from its amino acid sequence or UniProt Accession look as follows:

Command line (JSON formatted results are saved in a folder named ‘results’): <mark>$ gget setup elm                       # Downloads/updates local ELM database $ gget elm -o results LIAQSIGQASFV $ gget elm -o results --uniprot Q02410</mark>

Python (two data frames are returned): <mark>>>> gget.setup(“elm”)             # Downloads/updates local ELM database >>> ortholog_df, regex_df = gget.elm(“LIAQSIGQASFV”) >>> ortholog_df, regex_df = gget.elm(“Q02410”, uniprot=True)</mark>

The [--threads][-t] (Python: “threads”) argument can be used to multithread the sequence alignment for increased speed for large-scale computations. The following tutorial demonstrates how _gget elm_ can be combined with the IUPred3 API (Erdős _et al.,_ 2021) to filter putative ELMs located within intrinsically disordered regions and thereby limiting false positive matches: http://tinyurl.com/mw5s5yf3.

#### **Proof of concept:** **_gget elm_ reports the loss of a protein interaction motif involved in DNA repair in a carcinogenic BRCA2 mutation**

BRCA2 (BReast CAncer gene 2) plays an essential role in DNA repair through homologous recombination, and heterozygous germline defects in BRCA2 increase the risk of breast cancer. The promotion of homologous recombination by BRCA2 requires its association with the partner and localizer of BRCA2 (PALB2) (Hanenberg and Andreassen, 2018). This important protein-protein interaction occurs at the site of a linear motif (ELM: LIG_PALB2_WD40_1, regex: [....WF..L]), which can be recognized by _gget elm_ . We analyzed the wildtype BRCA2 sequence and a mutant BRCA2 sequence with a single amino acid substitution (W31C), previously described as carcinogenic due to a loss of interaction with PALB2 (Oliver _et al._ , 2009). _gget elm_ accurately reports the loss of the PALB2 interaction motif in the mutant sequence compared to the wildtype sequence: <u>https://tinyurl.com/yc5r2b5m.</u>

#### **Discussion**

We have shown that _gget elm_ facilitates scalable querying of the ELM database via local queries, and its use via the command line makes it easy to integrate into scripted workflows. While this feature should extend the usability of the ELM database, there are limitations

21

while performing motif searches using the ELM database web interface or _gget elm._ A common problem encountered is that short and degenerate ELMs inevitably lead to false positive matches. Accuracy can be improved by filtering the results using the additional contextual information, which is also returned by _gget elm_ , including description, structural features, and host taxonomy. Furthermore, combining motif results with structural and alignment information can provide information about the functional availability of the interaction site (Lee _et al._ , 2023). The 3D structure of a protein can be predicted from its amino acid sequence _de novo_ using algorithms like AlphaFold2 (Jumper _et al._ , 2021) and compared to experimentally derived crystal structures of orthologs deposited on the PDB (Berman _et al._ , 2000). The _gget_ suite of tools contains a workflow to perform both of these computations, which is demonstrated here: <u>https://tinyurl.com/yzc9ytvx.</u>

#### **Acknowledgments**

We thank the expert curators of the ELM database for providing an excellent resource. We thank Dr. Toby Gibson for the valuable feedback on the manuscript. We also thank Candace Rypisi and the rest of the Summer Undergraduate Research Fellowships (SURF) program staff for facilitating valuable research opportunities for undergraduate students and mentorship opportunities for graduate students at Caltech. Illustrations in Figure 2.3 were created with BioRender.com.

22

#### **References**

- Benz, C. _et al._ (2022) Proteome‐scale mapping of binding sites in the unstructured regions of the human proteome. _Mol. Syst. Biol.,_ **18** , e10584.

- Berman, H.M. _et al._ (2000) The Protein Data Bank. _Nucleic Acids Res._ , **28** , 235–242.

- Buchfink, B. _et al._ (2021) Sensitive protein alignments at tree-of-life scale using DIAMOND. _Nat. Methods_ , **18** , 366–368.

- Carberry, J.,Jr (2008) Toward a unified theory of high-energy metaphysics: Silly string theory. _Knit Forecast Int._ , **5** , 1–3.

- Chica, C. _et al._ (2008) A tree-based conservation scoring method for short linear motifs in multiple alignments of protein sequences. _BMC Bioinformatics_ , **9** , 229.

- Davey, N.E. _et al._ (2012) Attributes of short linear motifs. _Mol. Biosyst._ , **8** , 268–281.

- Dinkel, H. _et al._ (2015) ELM 2016—data update and new functionality of the eukaryotic linear motif resource. _Nucleic Acids Res._ , **44** , D294–D300.

- Dinkel, H. _et al._ (2011) ELM—the database of eukaryotic linear motifs. _Nucleic Acids Res._ , **40** , D242–D251.

- Erdős, G. _et al._ (2021) IUPred3: Prediction of protein disorder enhanced with unambiguous experimental annotation and visualization of evolutionary conservation. _Nucleic Acids Res._ , **49** , W297–W303.

- Fasano, C. _et al._ (2022) Short Linear Motifs in Colorectal Cancer Interactome and Tumorigenesis. _Cells_ , **11** .

- Gogl, G. _et al._ (2022) Quantitative fragmentomics allow affinity mapping of interactomes. _Nat. Commun._ , **13** , 5472.

- Gouw, M. _et al._ (2018) The eukaryotic linear motif resource - 2018 update. _Nucleic Acids Res._ , **46** , D428–D434.

- Hanenberg, H. and Andreassen,P.R. (2018) PALB2 (partner and localizer of BRCA2). _Atlas Genet. Cytogenet. Oncol. Haematol._ , **22** , 484–490.

- Jumper, J. _et al._ (2021) Highly accurate protein structure prediction with AlphaFold. _Nature_ , **596** , 583–589.

- Kruse, T. _et al._ (2021) Large scale discovery of coronavirus-host factor protein interaction motifs reveals SARS-CoV-2 specific mechanisms and vulnerabilities. _Nat. Commun._ , **12** , 6761.

- Kumar, M. _et al._ (2023) ELM-the Eukaryotic Linear Motif resource-2024 update. _Nucleic Acids Res._

- Kumar, M. _et al._ (2020) ELM-the Eukaryotic Linear Motif resource in 2020. _Nucleic Acids Res._ , **48** , D296–D306.

- Kumar, M. _et al._ (2022) The Eukaryotic Linear Motif resource: 2022 release. _Nucleic Acids Res._ , **50** , D497–D508.

- Lee, C.Y. _et al._ (2023) Systematic discovery of protein interaction interfaces using AlphaFold and experimental validation. _bioRxiv_ , 2023.08.07.552219.

- Luebbert, L. _et al._ (2023) Efficient querying of genomic reference databases with gget. _Bioinformatics_ , **39** , btac836.

- Mészáros, B. _et al._ (2017) Degrons in cancer. _Sci. Signal._ , **10** .

- Mészáros, B. _et al._ (2021) Short linear motif candidates in the cell entry system used by SARS-CoV-2 and their potential therapeutic implications. _Sci. Signal._ , **14** , eabd0334.

23

- Oliver, A.W. _et al._ (2009) Structural basis for recruitment of BRCA2 by PALB2. _EMBO Rep._ , **10** , 990–996.

- Puntervoll, P. _et al._ (2003) ELM server: A new resource for investigating short functional sites in modular eukaryotic proteins. _Nucleic Acids Res._ , **31** , 3625–3630.

- Reys, V. and Labesse, G. (2022) SLiMAn: An Integrative Web Server for Exploring Short Linear Motif-Mediated Interactions in Interactomes. _J. Proteome Res._ , **21** , 1654–1663.

- Simonetti, L. _et al._ (2023) SLiM-binding pockets: An attractive target for broad-spectrum antivirals. _Trends Biochem. Sci._ , **48** , 420–427.

- UniProt Consortium (2021) UniProt: The universal protein knowledgebase in 2021. _Nucleic Acids Res._ , **49** , D480–D489.

- Uyar, B. _et al._ (2014) Proteome-wide analysis of human disease mutations in short linear motifs: neglected players in cancer? _Mol. Biosyst._ , **10** , 2626–2642.

- Van Roey, K. _et al._ (2014) Short linear motifs: Ubiquitous and functionally diverse protein interaction modules directing cell regulation. _Chem. Rev._ , **114** , 6733–6778.

- Zhang, Q.C. _et al._ (2012) PrePPI: A structure-informed database of protein–protein interactions. _Nucleic Acids Res._ , **41** , D828–D833.

24

_C h a p t e r 3_

---

[← Efficient Querying of Genomic Reference Databases with gget](10-efficient-querying-of-genomic-reference-databases-with-gget.md) · [Up: contents](index.md) · [QUANTIFYING HIDDEN INFORMATION →](12-quantifying-hidden-information.md)
