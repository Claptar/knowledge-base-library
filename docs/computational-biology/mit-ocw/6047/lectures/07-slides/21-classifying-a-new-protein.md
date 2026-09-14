---
title: Classifying A New Protein
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Classifying A New Protein

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Targeting signal<br>Protein domains<br>Co-expression  P(Xi|Mito)<br>Mass Spec<br>Xi<br>P(Xi|~Mito)<br>Homology<br>Induction<br>(for all 8 features)<br>Motifs<br>Courtesy of AzaToth; image in the public domain.AzaToth; image in the public domain.; image in the public domain.<br>Plug these and priors into the discriminant function<br> P ( X i | Mito ) P ( Mito )<br><br>G X X  0<br>( 1,..., 7 ) log<br>~ ~<br>P ( X i | Mito ) P ( Mito )<br><br><!-- End of picture text -->

Courtesy of AzaToth; image in the public domain.AzaToth; image in the public domain.; image in the public domain.

###### **_IF G>0, we predict that the protein is from class Mito_**

59

#### Apply to human proteome: 1,451 predictions (of which 490 are novel predictions)


<!-- Start of picture text -->
Naïve Bayes<br>(Maestro)<br>(99%, 71%)<br>* *<br><!-- End of picture text -->

Courtesy of Sarah Calvo. Used with permission.

**Problem in genomics: not everything novel is false**

**Slide Credit: S. Calvo** 60

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

61

## Support Vector Machines (SVMs)

Easy to select a line

But many lines will separate these training data

What line should we choose?


62

## Support Vector Machines (SVMs)

**A sensible choice is to select a line that maximizes the** **_margin_ between classes**


<!-- Start of picture text -->
Support<br>Vectors<br><!-- End of picture text -->

63

---

[← Individual Feature Distributions](20-individual-feature-distributions.md) · [Up: contents](index.md) · [SVM Formulation →](22-svm-formulation.md)
