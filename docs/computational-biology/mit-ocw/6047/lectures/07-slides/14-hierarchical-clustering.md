---
title: Hierarchical clustering
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hierarchical clustering

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Most widely used algorithm for expression data

- Start with each point in a separate cluster

- At each step:

   - Choose the pair of **closest clusters**


<!-- Start of picture text -->
c<br>a  b<br>h<br>e<br>d<br>f<br>g<br><!-- End of picture text -->

- Merge

Phylogeny (UPGMA)

**U** nweighted **P** air **G** roup **M** ethod with **A** rithmetic-mean

Select a “cut level” to create disjoint clusters


<!-- Start of picture text -->
a  b  d  e  f  c  g  h<br><!-- End of picture text -->

30

###### **Distance between clusters**

- CD(X,Y)=minx X, y Y D(x,y)

- <sup>_Single-link method_</sup>

- CD(X,Y)=maxx X, y Y D(x,y)

- _Complete-link method_


<!-- Start of picture text -->
h<br>e<br>d<br>f<br>g<br>h<br>e<br>d<br>f<br>g<br><!-- End of picture text -->

- CD(X,Y)=avgx X, y Y D(x,y)

- _Average-link method_

- CD(X,Y)=D( avg(X) , avg(Y) )

- _Centroid method_


<!-- Start of picture text -->
h<br>e<br>d<br>f<br>g<br>h<br>e<br>d<br>f<br>g<br><!-- End of picture text -->

###### Cluster distance affects both results and runtime

31

### **Point-to-point (Dis)Similarity Measures**

**D’haeseleer (2005) Nat Biotech** Courtesy of Macmillan Publishers Limited. Used with permission. Source: D'haeseleer, Patrik. "How does gene expression clustering work?." Nature biotechnology 23, no. 12 (2005): 1499-1502.

###### **Cluster-to-cluster distance as a function of point-to-point**

32

###### **Today: Gene Expression Clustering & Classification**

###### **1. Introduction to gene expression analysis**

   - Technology: microarrays vs. RNAseq. Resulting data matrices

   - Supervised (Clustering) vs. unsupervised (classification) learning

**2. K-means clustering (clustering by partitioning)**

   - Algorithmic formulation: Update rule, optimality criterion. Fuzzy k-means.

   - Machine learning formulation: Generative models, Expectation Maximization.

**3. Hierarchical Clustering (clustering by agglomeration)**

   - Basic algorithm, Distance measures. <mark>Evaluating clustering results</mark>

**4. Naïve Bayes classification (generative approach to classification)** – Discriminant function: class priors, and class-conditional distributions

   - Training and testing, Combine mult features, Classification in practice

**5. (optional) Support Vector Machines (discriminative approach)** – SVM formulation, Margin maximization, Finding the support vectors

   - Non-linear discrimination, Kernel functions, SVMs in practice

33

## Evaluating Cluster Performance

**In general, it depends on your goals in clustering**

- Robustness

   - Select random samples from data set and cluster

   - Repeat

   - Robust clusters show up in all clusters

- Category Enrichment

   - Look for categories of genes “over-represented” in particular clusters

   - Also used in Motif Discovery

34

###### Evaluating clusters – Hypergeometric Distribution

**Select k elements (at random)**


**m happen to be + (out of p +’s) k-m happen to be - (out of N-p -’s)**


<!-- Start of picture text -->
<br>N<br> p  p <br>        <br>m k m<br>  <br><br>P ( pos  r )<br><br>N<br>m  r  <br>P-value of uniformity<br>   <br>in computed cluster  k<br> <br><!-- End of picture text -->

- N experiments, **p labeled +** , **(N-p) –**

- **Cluster: k elements** , **m labeled +, k-m labeled -**

- P-value of _single_ cluster containing k elements of which at least r are **+**

P-value of uniformity in computed cluster

Prob that a randomly chosen set of k experiments would result in m positive and k-m negative

35

## Evaluation using functional enrichment


**Clustered 8600 human genes using expression time course in fibroblasts**

- **(A) Cholesterol biosynthesis**

- **(B) Cell cycle**

- **(C) Immediate early response**

- **(D) Signalling and angiogenesis**

- **(E) Wound healing**

Eisen, Michael et al. "Cluster Analysis and Display of Genome-wide Expression Patterns." PNAS 95, no. 25 (1998): 14863-14868. Copyright (1998) National Academy of Sciences, U.S.A.

**(Eisen (1998) PNAS)**

36

## Evaluation based on motif content

Expression from 15 time points during yeast cell cycle


Courtesy of Nature Publishing Group. Used with permission. Source: Tavazoie, Saeed et al. "Systematic determination of genetic network architecture." Nature Genetics 22, no. 3 (1999): 281-285.

**Tavazoie & Church (1999)**

37

###### **Today: Gene Expression Clustering & Classification**

###### **1. Introduction to gene expression analysis**

   - Technology: microarrays vs. RNAseq. Resulting data matrices

   - Supervised (Clustering) vs. unsupervised (classification) learning

**2. K-means clustering (clustering by partitioning)**

   - Algorithmic formulation: Update rule, optimality criterion. Fuzzy k-means.

   - Machine learning formulation: Generative models, Expectation Maximization.

**3. Hierarchical Clustering (clustering by agglomeration)**

   - Basic algorithm, Distance measures. Evaluating clustering results

**4. Naïve Bayes classification (generative approach to classification)** – Discriminant function: class priors, and class-conditional distributions

   - Training and testing, Combine mult features, Classification in practice

**5. (optional) Support Vector Machines (discriminative approach)** – SVM formulation, Margin maximization, Finding the support vectors

   - Non-linear discrimination, Kernel functions, SVMs in practice

38

---

[← Fuzzy K-means update rule](13-fuzzy-k-means-update-rule.md) · [Up: contents](index.md) · [Two Approaches to Classification →](15-two-approaches-to-classification.md)
