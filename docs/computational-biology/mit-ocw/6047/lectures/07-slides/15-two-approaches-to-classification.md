---
title: Two Approaches to Classification
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Two Approaches to Classification

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### • Generative

   - Bayesian Classification (e.g. Naïve Bayes)

   - Pose classification problem in prob terms

   - Model feature distribution in different classes

   - Use probability calculus for making decisions

- Discriminative

   - E.g. Support Vector Machines

   - No modeling of underlying distributions

   - Make decisions using distance from boundary

- Example: Gene finding: HMMs vs. CRFs

39

###### **Bayesian classification with a single feature**

P( _Feature | Class_ )

**<u>Ex 1:</u>** DNA repair genes show higher expression during stress **<u>Ex 2:</u>** Protein-coding regions show higher conservation levels

**<u>Ex 3:</u>** Regulatory regions show higher GC-content **<u>In general:</u>** foreground signal vs. background

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

1. If you know both distributions, how to classify a new example

– Picking a cutoff. Minimizing classification error. Maximizing posterior prob. 2. If you have many classified examples, how to estimate model params. – Parametric vs. non-parametric models. Class-conditional distributions. Priors **Likelihood Prior** 3. Bayes’ Rule: _P_ <u>(</u> _Feature_ <u>|</u> _Class_ <u>)</u> _P_ <u>(</u> _Class_ <u>)</u>  – P(C|F) from P(F|C) _P_ ( _Class_ | _Feature_ ) **Posterior** _P_ ( _Feature_ ) – Take probability ratios **Evidence** 40

40

###### **Classification problem: Max Probability Class**


Select the class that maximizes posterior:

**Likelihood Prior** _P_ <u>(</u> _Feature_ <u>|</u> _Class_ <u>)</u> _P_ <u>(</u> _Class_ <u>)</u>  _P_ ( _Class_ | _Feature_ ) **Posterior** _P_ ( _Feature_ ) **Evidence**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Maximum-A-Posteriori (MAP) estimates _BestClass = argmaxC P(Class|Feature)_

_= argmaxC P(Feature|Class) P(Class)_ Scaling the above distribution based on class priors

41

_<mark>P</mark>_ <u><mark>(</mark></u> _<mark>Feature</mark>_ <u><mark>|</mark></u> _<mark>Class</mark>_ <u><mark>)</mark></u> _<mark>P</mark>_ <u>(</u> _Class_ <u>)</u>  _P_ ( _Class_ | _Feature_ ) Likelihood: _P_ ( _Feature_ )

**Features for each class drawn from conditional probability distributions (conditional on the class)**

**P(X|Class1) P(X|Class2)**


<!-- Start of picture text -->
X<br><!-- End of picture text -->

**Our first goal will be to** **_model_ these class-conditional probability distributions (CCPD)**

42

_P_ <u>(</u> _Feature_ <u>|</u> _Class_ <u>)</u> _<mark>P</mark>_ <u><mark>(</mark></u> _<mark>Class</mark>_ <u><mark>)</mark></u>  _P_ ( _Class_ | _Feature_ ) Class Priors: _P_ ( _Feature_ )

**We model prior probabilities to quantify the expected** **_a priori_ chance of seeing a class P(Class2)   &   P(Class1)**

P(mito) = how likely is the next protein to be a mitochondrial protein _before I see any features to help me decide_

We expect ~1500 mitochondrial genes out of ~21000 total, so P(mito)=1500/21000 P(~mito)=19500/21000

43

_P_ <u>(</u> _Feature_ <u>|</u> _Class_ <u>)</u> _P_ <u>(</u> _Class_ <u>)</u>  _P_ ( _Class_ | _Feature_ ) Evidence _<mark>P</mark>_ <mark>(</mark> _<mark>Feature</mark>_ <mark>)</mark>

**Total evidence is P(Feature)=Σi P(Feature|Classi)P(Classi) But it does not need to be known for classification** If we observe an object with feature X, how do decide if the object is from Class 1?

The Bayes Decision Rule is simply choose Class1 if: _P_ ( _Class_ 1| _X_ )  _P_ ( _Class_ 2 | _X_ ) _P_ <u>(</u> _X_ <u>|</u> _Class_ 1) _P_ <u>(</u> _L_ 1) _P_ <u>(</u> _X_ <u>|</u> _Class_ 2) _P_ <u>(</u> _L_ 2)  _P_ ( _X_ ) _P_ ( _X_ ) same _P_ ( _X_ | _Class_ 1) _P_ ( _Class_ 1)  _P_ ( _X_ | _Class_ 2) _P_ ( _Class_ 2)

 **P(Feature) does not need to be computed for classification** 44

### Discriminant Function for selecting Class1

We can create a convenient representation of the Bayes Decision Rule

_P_ ( _X_ | _Class_ 1) _P_ ( _Class_ 1)  _P_ ( _X_ | _Class_ 2) _P_ ( _Class_ 2)

_P_ <u>(</u> _X_ <u>|</u> _Class_ 1) _P_ <u>(</u> _Class_ 1)  1 _P_ ( _X_ | _Class_ 2) _P_ ( _Class_ 2)

_P_ <u>(</u> _X_ <u>|</u> _Class_ 1) _P_ <u>(</u> _Class_ 1)  _G_ ( _X_ ) log  0 _P_ ( _X_ | _Class_ 2) _P_ ( _Class_ 2)

###### _If G(X) > 0, we classify as Class 1_

45

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

46

---

[← Hierarchical clustering](14-hierarchical-clustering.md) · [Up: contents](index.md) · [Training and Testing Datasets →](16-training-and-testing-datasets.md)
