---
title: P1 – Network Statistics (10 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/05-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P1 – Network Statistics (10 points)

PROBLEM SET 5. Network Statistics, Chromatin Structure, Heritability, Association Testing (24 Points)

Due: Thursday, May 1st at noon .

## Python Scripts
All Python scripts must work on athena using /usr/athena/bin/python. You may not assume availability of any third party modules unless you are explicitly instructed so. You are advised to test your code on Athena before submitting. Please only modify the code between the indicated bounds, with the exception of adding your name at the top, and remove any print statements that you added before submission.

Electronic submissions are subject to the same late homework policy as outlined in the syllabus and submission times are assessed according to the server clock. Any Python programs you add code to must be submitted electronically, as .py files on the course website using appropriate filename for the scripts as indicated in the problem set or in the skeleton scripts provided on course website.

## Assessing bias in high-throughput protein-protein interaction networks
Protein-protein interactions are often stored in databases that cover thousands of proteins and interactions between them. However, there are biases present in these data.

- Poorly studied proteins may be under-represented in these databases because few people have taken the time to identify interacting partners, thus the databases are over-represented among highly studied proteins.
- Evidence of protein-protein interaction is highly variable, as there exist diverse biochemical assays to identify protein-protein interaction and these assays in themselves are biased towards specific types of proteins.

In this problem, we will study these biases and the relationship between them.

You will be completing the script citationNetwork.py, using the networkX module which allows us to manipulate and study networks in python. NetworkX has been installed on Athena so we will follow a similar procedure as other problems.

Log on to Athena's Dialup Service:

```text
ssh <your Kerberos username>@athena.dialup.mit.edu
```

Before running any python scripts, use the following command to add the networkX module we installed to your PYTHONPATH:

```text
export PYTHONPATH=/afs/athena/course/20/20.320/pythonlib/lib/python2.7/site-packages/
```

otherwise, you will get an ImportError.

You will also need to get the .zip containing the files for this problem in the course folder.

```text
cp /afs/athena/course/7/7.91/sp_2014/citationNetwork.zip ~
cd ~
unzip citationNetwork.zip
cd citationNetwork
```

Please submit the citationNetwork.py script online.

It should take a uniprot file and a network and print some scaffold text. Of course, feel free to modify the script in any way that is helpful to you to answer the questions, but have it conform to the above standard when you submit it.

**(a) (2 points) Bias in protein studies:** In the zip file, we have provided protein citation data from UniProt. This file was generated using the following procedure (you do not have to generate the file):

> Download protein citation data from http://www.uniprot.org. Use the 'Advanced Search' to select only those proteins that are human and their status is 'reviewed'. Click on 'customize' to make sure the table has ONLY the 'Mapped Pubmed ID' field, and then download the tab-delimited file.

In citationNetwork.py, for each unique entry name in this file, collect the unique number of mapped PubMed ID (correlating to the number of times the protein has been cited).

a. Plot a histogram of the number of citations per protein. Attach the PDF to this write-up.
b. What are the median citation rate and maximum citation rate?
**Median:** 3
**Maximum:** 5256
c. Which protein has been cited the most? P04637 (p53)

**(b) (4 points) Bias in source of interaction evidence:** STRING is a database of protein-protein interactions with confidence scores ascribed to each interaction based on distinct sources of evidence (http://www.string-db.org). There are seven sources of evidence, each with its own scoring contribution:

| Evidence | Description |
| :--- | :--- |
| Neighborhood score | Computed from the inter-gene nucleotide count |
| Fusion score | Derived from fused proteins in other species |
| Co-occurrence score | Score of the phyletic profile (derived from similar absence/presence of genes) |
| Co-expression score | Derived from similar pattern of mRNA expression measured by DNA arrays and similar technologies |
| Experimental score | Derived from experimental data, such as, affinity chromatography |
| Database score | Derived from curated data of various databases |
| Text-mining score | Derived from the co-occurrence of gene/protein names in abstracts |

For each source of evidence, we've provided you with a .pkl file containing a distinct NetworkX graph with the proteins (nodes) and interactions (edges) between them. The weight of the edge is the normalized score for that particular source of evidence (if it was greater than 0.25). You will find a function to load these, and directions for interacting with them, in the script.

a. How many edges (interactions) and nodes (proteins) are in each protein interaction network?

| Network | Edges | Nodes |
| :--- | :--- | :--- |
| Neighborhood score | 19976 | 1207 |
| Fusion score | 296 | 240 |
| Co-occurrence score | 3944 | 1148 |
| Co-expression score | 149333 | 3967 |
| Experimental score | 112787 | 10487 |
| Database score | 233910 | 6422 |
| Text-mining score | 1251381 | 14765 |

b. How many edges have a normalized score above 0.4? 0.8? What is the number of nodes in interaction networks with these score cutoffs?

Cutoff = 0.4:

| Network | Edges | Nodes |
| :--- | :--- | :--- |
| Neighborhood score | 8354 | 866 |
| Fusion score | 144 | 118 |
| Co-occurrence score | 1110 | 550 |
| Co-expression score | 49874 | 2390 |
| Experimental score | 95245 | 9772 |
| Database score | 233910 | 6422 |
| Text-mining score | 620858 | 14481 |

Cutoff = 0.8:

| Network | Edges | Nodes |
| :--- | :--- | :--- |
| Neighborhood score | 412 | 154 |
| Fusion score | 18 | 16 |
| Co-occurrence score | 0 | 0 |
| Co-expression score | 5172 | 642 |
| Experimental score | 16523 | 4035 |
| Database score | 233910 | 6422 |
| Text-mining score | 89560 | 9416 |

c. Comment on what these results say about the different types of evidence.
Many of the data types have a low proportion of high confidence interactions, indicating that much of the data may be of low quality. As long as a comment on data quality or reliability was made, points were awarded. In many cases, students commented on specific types of evidence, which was also accepted.

**(c) (4 points) Relationship between number of citations and node degree?** The size and distribution of an interaction network measured by distinct types of evidence varies greatly. For each interaction network collect the node degree of each protein. Then, after removing proteins without interactions and interacting nodes without data in UniProt, calculate the Spearman rank correlation to determine if the node degree is correlated with the number of citations of that protein collected in the first section.

a. What is the node citation/interaction correlation for each of the sources of evidence?
b. What are the correlation values when you restrict the interactions to those with at least a score of 0.4? 0.8?

| Network | No cutoff | 0.4 | 0.8 |
| :--- | :--- | :--- | :--- |
| Neighborhood score | 0.058 | 0.075 | |
| Fusion score | 0.104 | 0.182 | 0.370 |
| Co-occurrence score | 0.017 | -0.002 | |
| Co-expression score | 0.008 | 0.012 | 0.051 |
| Experimental score | 0.416 | 0.429 | 0.247 |
| Database score | 0.104 | 0.104 | 0.034 |
| Text-mining score | 0.706 | 0.685 | 0.564 |

c. Is there a relationship between the number of citations and degree? If so, what is the relationship and why do you think this is?
For some forms of evidence, there is a correlation between number of citations and edge degree. This may be due to bias in how much certain proteins have been studied. The more a protein has been experimented on, the more true interactions (and false positive) are likely to be discovered. Also, if a protein has lots of connections, it is likely to be mentioned in the context of its partners. Many people said there was a positive correlation, despite the fact that in many cases it was very low. It was quite open to interpretation, depending on what people considered a strong correlation.

d. Does this relationship vary between sources of evidence? If so, why?
Yes, fusion, experimental, and text-mining score have higher correlations than the other data types. This is likely because the data for these experiments comes from a large pool of smaller studies, which have bias in choice of protein to study. Genome-wide assays that look at all proteins at once do not have this problem. Again, this was open to interpretation.

To copy your script and histogram from Athena onto your own computer, use SCP:

```text
<in a new Terminal on your computer, cd into your local computer’s
directory where you want to download the PDF>

scp -r <your Kerberos
username>@athena.dialup.mit.edu:~/citationNetwork/citationNetwork.py .

scp -r <your Kerberos
username>@athena.dialup.mit.edu:~/citationNetwork/histogram.pdf .
```

---

[Up: contents](index.md) · [P2 – Analysis of Chromatin Structure (5 points) →](02-p2-analysis-of-chromatin-structure-5-points.md)
