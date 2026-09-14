---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6.047/6.878/HST.507 Computational Biology: Genomes, Networks, Evolution

#### **Lecture 7 Gene expression analysis: Clustering and Classification**

1

**Module II: Gene expression analysis and networks**

- Computational foundations:

   - Unsupervised Learning: Expectation Maximization

   - Supervised learning: generative/discriminative models

   - Read mapping, significance testing, splice graphs

   - Folding: DP self-alignment, Context Free grammars

- Biological frontiers:

   - L6: RNA-Seq analysis, quantifying transcripts, isoforms

   - – L7: Gene expression analysis: cluster genes/conditions – L8: Networks I: Bayesian Inference, deep learning – L9: Networks II: Network structure, spectral methods

2

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

**5. (optional) Support Vector Machines (discriminative approach)** – SVM formulation, Margin maximization, Finding the support vectors – Non-linear discrimination, Kernel functions, SVMs in practice

3

###### **RNA-Seq: De novo tx reconstruction / quantification**


<!-- Start of picture text -->
Count<br><!-- End of picture text -->

- © sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **<u>Microarray technology</u>**

- Synthesize DNA probe array, complementary hybridization

- Variations:

   - One long probe per gene

   - Many short probes per gene

   - Tiled k-mers across genome

- Advantage:

   - Can focus on small regions, even if few molecules / cell

###### **<u>RNA-Seq technology:</u>**

- Sequence short reads from mRNA, map to genome

- Variations:

   - Count reads mapping to each known gene

   - Reconstruct transcriptome _de novo_ in each experiment

- Advantage:

• Digital measurements, de novo 4

### **Expression Analysis Data Matrix**

• Measure 20,000 genes in 100s of conditions

**Condition 1 Condition 2 Condition 3 n experiments …**

**Each experiment measures expression of thousands of ‘spots’, typically genes**


<!-- Start of picture text -->
Expression profile of a gene<br>m genes<br><!-- End of picture text -->

- Study resulting matrix

**Experiment similarity questions**

5


<!-- Start of picture text -->
 Clustering  vs.  Classification<br>Independent validation<br>Conditions  of groups that emerge:  Known<br>Conditions  classes:<br>Chronic<br>lymphocytic<br>leukemia<br>B-cell genes in<br>blood cell lines<br>Proliferation genes<br>in transformed cell lines<br>Lymph node genes in<br>diffuse large B-cell<br>lymphoma (DLBCL)<br>Alizadeh, Nature 2000<br>Alizadeh, Nature 2000<br>Genes  <br>Genes  <br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Alizadeh, Ash A., Michael B. Eisen, R. Eric Davis, Chi Ma, Izidore S. Lossos, Andreas Rosenwald, Jennifer C. Boldrick et al. "Distinct types of diffuse large B-cell lymphoma identified by gene expression profiling." Nature 403, no. 6769 (2000): 503-511. **<u>Goal of Clustering</u>** : **<u>Group similar items Goal of Classification</u>** : Extract features that likely come from the same category, from the data that best **<u>assign new</u>** and in doing so **<u>reveal hidden structure elements</u>** to ≥1 of **<u>well-defined classes-defined classesdefined classes</u>**

**<u>Goal of Classification</u>** : Extract features from the data that best **<u>assign new elements</u>** to ≥1 of **<u>well-defined classes-defined classesdefined classes</u>**

• **Unsupervised learning**

• **Supervised learning**

6

---

[Up: contents](index.md) · [Clustering vs Classification →](02-clustering-vs-classification.md)
