---
title: Assessing bias in high-throughput protein-protein interaction networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/05-questions-pset5-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Assessing bias in high-throughput protein-protein interaction networks

**Source:** `psets/05-questions-pset5-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Protein-protein interactions are often stored in databases that cover thousands of proteins and interactions between them. However, there are biases present in these data.

- Poorly studied proteins may be under-represented in these databases because few people have taken the time to identify interacting partners, thus the databases are over-represented among highly studied proteins.

- Evidence of protein-protein interaction is highly variable, as there exist diverse biochemical assays to identify protein-protein interaction and these assays in themselves are biased towards specific types of proteins.

In this problem, we will study these biases and the relationship between them.

You will be completing the script citationNetwork.py, using the networkX module which allows us to manipulate and study networks in python. NetworkX has been installed on Athena so we will follow a similar procedure as other problems.

Log on to Athena's Dialup Service:

ssh <your Kerberos username>@athena.dialup.mit.edu

Before running any python scripts, use the following command to add the networkX module we installed to your PYTHONPATH:

export

PYTHONPATH=/afs/athena/course/20/20.320/pythonlib/lib/python2.7/site­ packages/

otherwise, you will get an ImportError.

You will also need to get the .zip containing the files for this problem in the course folder.

cp /afs/athena/course/7/7.91/sp_2014/citationNetwork.zip ~

- cd ~

unzip citationNetwork.zip

- cd citationNetwork

Please submit the citationNetwork.py script online.

It should take a uniprot file and a network and print some scaffold text. The networks that the script expects as input are given in the .pkl files that will be used in part (b). Each of the .pkl files corresponds to a different network. Of course, feel free to modify the script in any way that is helpful to you to answer the questions, but have it conform to the above standard when you submit it.

2

- **(a) (2 points) Bias in protein studies:** In the zip file, we have provided protein citation data from UniProt in uniprot.txt.

In citationNetwork.py, for each unique entry name in this file, collect the unique number of mapped PubMed ID (correlating to the number of times the protein has been cited).

- a. Plot a histogram of the number of citations per protein. Attach the PDF to this write-up.

- b. What are the median citation rate and maximum citation rate?

   - **Median: Maximum:**

- c. Which protein has been cited the most?

**(b) (4 points) Bias in source of interaction evidence:** STRING is a database of protein-protein interactions with confidence scores ascribed to each interaction based on distinct sources of evidence (http://www.string-db.org). There are seven sources of evidence, each with its own scoring contribution:

|**Evidence**|**Description**|
|---|---|
|Neighborhood score|Computed from the inter-gene nucleotide count|
|Fusion score|Derived from fusedproteins in other species|
|Co-occurrence score|Score of thephyleticprofile(derived from similar absence/presence ofgenes)|
|Co-expression score|Derived from similar pattern of mRNA expression measured by DNA arrays<br>and similar technologies|
|Experimental score|Derived from experimental data,such as,affinitychromatography|
|Database score|Derived from curated data of various databases|
|Text-miningscore|Derived from the co-occurrence ofgene/protein names in abstracts|


For each source of evidence, we've provided you with a .pkl file containing a distinct NetworkX graph with the proteins (nodes) and interactions (edges) between them. The weight of the edge is the normalized score for that particular source of evidence (if it was greater than 0.25). You will find a function to load these, and directions for interacting with them, in the script.

- a. How many edges (interactions) and nodes (proteins) are in each protein interaction network?

|**Network**|**Edges**|**Nodes**|
|---|---|---|
|Neighborhood score|||
|Fusion score|||
|Co-occurrence score|||
|Co-expression score|||
|Experimental score|||
|Database score|||
|Text-miningscore|||


- b. How many edges have a normalized score above 0.4? 0.8? What is the number of nodes in interaction networks with these score cutoffs?

3

Cutoff = 0.4:

|**Network**|**Edges**|**Nodes**|
|---|---|---|
|Neighborhood score|||
|Fusion score|||
|Co-occurrence score|||
|Co-expression score|||
|Experimental score|||
|Database score|||
|Text-miningscore|||


Cutoff = 0.8:

|**Network**|**Edges**|**Nodes**|
|---|---|---|
|Neighborhood score|||
|Fusion score|||
|Co-occurrence score|||
|Co-expression score|||
|Experimental score|||
|Database score|||
|Text-miningscore|||


c. Comment on what these results say about the different types of evidence.

4

- **(c) (4 points) Relationship between number of citations and node degree?** The size and distribution of an interaction network measured by distinct types of evidence varies greatly. For each interaction network collect the node degree of each protein. Then, after removing proteins without interactions and interacting nodes without data in UniProt, calculate the Spearman rank correlation to determine if the node degree is correlated with the number of citations of that protein collected in the first section.

   - a. What is the node citation/interaction correlation for each of the sources of evidence? b. What are the correlation values when you restrict the interactions to those with at least a score of 0.4? 0.8?

|**Network**|**No cutoff**|**0.4**|**0.8**|
|---|---|---|---|
|**Neighborhood score**||||
|**Fusion score**||||
|**Co-occurrence score**||||
|**Co-expression score**||||
|**Experimental score**||||
|**Database score**||||
|**Text-mining score**||||


- c. Is there a relationship between the number of citations and degree? If so, what is the relationship and why do you think this is?

- d. Does this relationship vary between sources of evidence? If so, why?

To copy your script and histogram from Athena onto your own computer, use SCP:

```
<in a new Terminal on your computer, cd into your local computer’s
directory where you want to download the PDF>
```

```
scp –r <your Kerberos
```

```
username>@athena.dialup.mit.edu:~/citationNetwork/citationNetwork.py .
```

```
scp –r <your Kerberos
```

```
username>@athena.dialup.mit.edu:~/citationNetwork/histogram.pdf .
```

5

## **<mark>P2 – Analysis of Chromatin Structure (5 points)</mark>**

- **(A)** <mark>Suppose we reduced the number of Segway states to be fewer than the true number of distinct patterns of chromatin marks. How might the resulting labels under this model be different?</mark>

- **(B)** <mark>The</mark> _<mark>C, M</mark>_ <mark>,</mark> _<mark>t,</mark>_ <mark>and</mark> _<mark>J</mark>_ <mark>variables in the Segway model implement a ‘countdown’ function, one of the core features of Segway. How might these countdown variables improve on a simple HMM model in modeling the underlying genomic states?</mark>

<mark>Suppose we remove the</mark> _<mark>C</mark>_ <mark>,</mark> _<mark>M</mark>_ <mark>,</mark> _<mark>t</mark>_ <mark>, and</mark> _<mark>J</mark>_ <mark>countdown variables from the Segway model for the remainder of this problem.</mark>

- **(C)** <mark>Draw the resulting graphical model.</mark>

- **(D)** <mark>Assuming that</mark> _<mark>J</mark>_ <mark>is a binary variable and we allow for 50 segment labels, describe how the conditional probability table for the segment label variables has changed between the old model and this new model in terms of the number of parameters.</mark>

- **(E)** <mark>Which other core feature of the Segway model does this new model retain that is not present in a simple HMM model?</mark>

6

## **P3 – Heritability (5 points)**

## **(A)** **<mark>(3 points)</mark>**

- (i) Suppose there is a single locus in a haploid organism controlling a trait with a positive allele for which the phenotype is 1 and a neutral allele for which the phenotype is 0. Calculate VG for this trait in an infinite population of F1 children from these two parents.

- 1

- (ii) Now, suppose there are three unlinked loci each with a positive allele contributing 3 to the phenotype and neutral allele contributing 0 to the phenotype. Calculate VG.

1

- (iii) Generalize the previous results to calculate VG for _N_ unlinked loci contributing 0 or N to the phenotype.

How many possible values are there for the phenotype?

- **(B)** **<mark>(1 point)</mark>** <mark>You perform linear regression to predict a phenotypic trait (y) on a set of binary genotypic variables (x</mark> 1 <mark>, x</mark> 2 <mark>, … , x</mark> N <mark>) for a model system. Show how the R</mark><sup>2</sup> <mark>that results relates to the narrow sense heritability of the trait.</mark>

- **(C)** **<mark>(1 point)</mark>** <mark>Assume that all of the genetic components from part (a) are additive.   Give the environmental contribution to the observed phenotype variance assuming that the covariance between the genetic and environmental components is zero.</mark>

7

## **<mark>P4 – Association Studies (5 points)</mark>**

- **(A)** **<mark>(3 points)</mark>** <mark>Consider the following data case-control data. We will perform a chi-square test for association with a SNP.</mark>

||**A**|**T**|
|---|---|---|
|**Case**|90|110|
|**Control**|50|250|


- (i) Fill in the following table with the counts you would expect if you assumed independence. Show your work.


<!-- Start of picture text -->
A  T<br>Case<br>Control<br><!-- End of picture text -->

   - (ii) Now, compute the Chi-Square statistic and state the conclusion for the p-value cutoff of 0.05.

- **(B)** **<mark>(1 point)</mark>** You perform a large scale analysis and generate a list of significant SNPs and would now like to prioritize SNPs for further study. How might you use what you have learned from using the Segway model to do so?

- **(C)** **<mark>(1 point)</mark>** <mark>Describe why it is better to do association tests using a likelihood test based on reads instead of first calling variants and then using a statistical test on the binary variant calls.</mark>

8

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Python Scripts](01-python-scripts.md) · [Up: contents](index.md)
