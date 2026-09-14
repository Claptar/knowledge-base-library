---
title: Getting Priors
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Getting Priors

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **Three general approaches**

1. Estimate priors by counting fraction of classes in training set

**P(Class1)=13/23 P(Class2)=10/23 13 Class1 10 Class2**

_But sometimes fractions in training set are not representative of world_

2. Estimate from “expert” knowledge

Example P(mito)=1500/21000 P(~mito)=19500/21000

3. We have no idea – use equal (uninformative) priors

P(Class1)=P(Class2)

50

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

51

### Combining Multiple Features

- We have focused on a single feature for an object

- But mitochondrial protein prediction (for example) has 7 features

**Targeting signal Protein domains Co-expression Mass Spec Homology Induction Motifs**

**_So P(X|Class) become P(X1,X2,X3,…,X8|Class) and our discriminant function becomes_**

_P_ <u>(</u> _X_ <u>1,</u> _X_ <u>2,...,</u> _X_ <u>7 |</u> _Class_ 1) _P_ <u>(</u> _Class_ 1)  _G_ ( _X_ ) log  0 _P X X X Class_ 2 _P Class_ 2 ( 1, 2,..., 7 | ) ( )

52

---

[← Training and Testing Datasets](16-training-and-testing-datasets.md) · [Up: contents](index.md) · [Naïve Bayes Classifier →](18-naïve-bayes-classifier.md)
