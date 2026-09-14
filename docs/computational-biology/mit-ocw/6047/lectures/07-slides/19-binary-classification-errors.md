---
title: Binary Classification Errors
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Binary Classification Errors

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

True (Mito) False (~Mito) Predicted True TP FP Predicted False FN TN

**Sensitivity = TP/(TP+FN) Specificity = TN/(TN+FP)**

- Sensitivity

   - Fraction of all Class1 (True) that we correctly predicted at Class 1

   - _How good are we at finding what we are looking for_

- Specificity

   - Fraction of all Class 2 (False) called Class 2

   - _How many of the Class 2 do we filter out of our Class 1 predictions_

55

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

56

## Classifying Mitochondrial Proteins

**Derive 7 features for all human proteins**


<!-- Start of picture text -->
Targeting signal<br>Protein domains<br>Co-expression<br>Mass Spec<br>Homology<br>Induction<br>Motifs<br><!-- End of picture text -->

First page of article removed due to copyright restrictions. Source: Calvo, Sarah et al. "Systematic identification of human mitochondrial disease genes through integrative genomics." Nature Genetics 38, no. 5 (2006): 576-582.

###### **Predict nuclear encoded mitochondrial genes Maestro**

57

---

[← Naïve Bayes Classifier](18-naïve-bayes-classifier.md) · [Up: contents](index.md) · [Individual Feature Distributions →](20-individual-feature-distributions.md)
