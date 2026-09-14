---
title: Using an SVM
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using an SVM

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Labels<br>   Y=+1<br> Y=-1<br>w<br>b/|w|<br>xnew<br><!-- End of picture text -->


<!-- Start of picture text -->
Given a new data<br>point we simply<br>assign it the label:<br>yi  sign  w  x new  b <br> <br> sign  i yi xi  x new  b <br> i <br>Again, only dot product<br>of input data!<br><!-- End of picture text -->

66

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

   - Non-linear discrimination, <mark>Kernel functions,</mark> SVMs in practice

67

---

[← SVM Formulation](22-svm-formulation.md) · [Up: contents](index.md) · [Non-linear Classifier →](24-non-linear-classifier.md)
