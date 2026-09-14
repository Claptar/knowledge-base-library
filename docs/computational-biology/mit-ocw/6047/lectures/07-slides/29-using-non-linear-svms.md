---
title: Using (Non-Linear) SVMs
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using (Non-Linear) SVMs

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **Step 1 – Transform data to Kernel Matrix K**


<!-- Start of picture text -->
1  2  N<br>1<br>2<br>N<br>K(Xi,Xj)<br><!-- End of picture text -->

###### **Step 2 – Train SVM on transformed data – get support vectors**

1 1 Minimize LD   _i_   _i j y yi j_ **xi**  **xj**   _i_   _i j y yi j_ K  **xi** , **xj**  2 2 _i i_ , _j i i_ , _j_

###### **Step 2 – Test/Classify on new samples**


73

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

   - Non-linear discrimination, Kernel functions <mark>, SVMs in practice</mark>

74

### Classifying Tumors with Array Data

- Primary samples:

   - 38 bone marrow samples

   - 27 ALL, 11 AML

   - obtained from acute leukemia patients at the time of diagnosis;

Excerpt of article removed due to copyright restrictions. Source: Golub, Todd R. et al. "Molecular classification of cancer: Class discovery and class prediction by gene expression monitoring." Science 286, no. 5439 (1999): 531-537.

- Independent samples:

   - 34 leukemia samples

   - 24 bone marrow

   - 10 peripheral blood samples

- Assay ~6800 Genes

75

---

[← Example Kernels](28-example-kernels.md) · [Up: contents](index.md) · [Weighted Voting Classfication →](30-weighted-voting-classfication.md)
