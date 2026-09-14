---
title: 1 Metric Learning
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_04_Metric_Learning.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_04_Metric_Learning.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Metric Learning

**Source:** [`notes/Lecture_04_Metric_Learning.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_04_Metric_Learning.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Although the origin of metric learning can be traced back to some earlier work, it really emerged in 2002 with the pioneering work of Xing et al. (2002) which formulates metric learning as a convex optimization problem. Before we (in)formally introduce metric learning, we first look in to two examples.

**Example 1** (Predicting CAD) **.** _Suppose we want to use the synthetic data presented in Table 1 for heart attack prediction. We can clearly see that attributes are scaled differently, and maybe correlated. This raises two questions:_

_1. If we go for the traditional approaches (well integrated in_ _`R` packages), predictors like income might get down-weighted as it has with high variances. But income might be, in fact, a very important predictor for predicting hearth disease._

_2. Say if we use SVM dual problem to do classification with a quadratic kernel function K_ ( _x, z_ ) = _||x−z||_ 2<sup>2</sup><sup>_,_</sup> _it ignores the correlation between variables and the genuinely significant variable might not play an important role._

In practice, we might apply some preprocessing of the data (say, normalization or standardization) to resolve these issues:


Rather than working with some arbitrary transformation of the data, the intuition of metric learning is to learn a better distance metric that is more relevant for the prediction problem at hand.

|Patient ID|Gender|Age|Weight (kg)|Income ($)|Heart Attack|
|---|---|---|---|---|---|
|1|1|63|82|56,000|1|
|2|0|43|67|105,000|0|
|3|0|55|70|75,000|0|
|4|1|76|68|60,000|1|
|new|0|50|78|90,000|?|


Table 1: (Synthetic) Data similar to Homework 1. How can we predict whether the new patient will get a heart attack?

1


Figure 1: A illustrative example for Metric learning. Think about metric as a “ruler.”

More rigorously, the goal of metric learning is to adapt some metric function to our data so that our supervised learning problem can provide more accurate prediction. For example, we want to find a metric _G ∈_ R<sup>_d×d_</sup> that transform the original data as the following:


Then, given _G_ is unknown, we must define certain criteria for an “ideal” _G_ for prediction purposes. The criteria of metric learning starts by defining two sets:


and it aims to find a matrix _G such that_ the sum of distances between similar individuals are minimized, and the sum of the distances between dissimilar individuals are maximized. Concretely, metric learning aims to find _G_ such that


See Figure 1 for a general illustration. We want to find a metric space to measure the distance between observations so that the similar objects move closer, and dissimilar objects can be separated. In other words, the distance metric provides a new data representation in the transformed space which is easily able to distinguish the items of different classes.

**What is a metric? A simple example** To better understand the role of _G_ in metric learning, let’s look at an example in Figure 2. If we set _G_ = _I_ , the identity matrix, separating low risk and high risk patients is not straightforward. Because the distances between similar/dissimilar objectives are very close. We would measure the distance between, for example, _X_ 1 and _X_ 3 via the simple Euclidean distance:


But if we do not stick to Euclidean distance, instead switch to a different distance measure:


2

where


Such a distance measure can more effectively put similar/dissimilar individuals into two groups, as we can calculate


By doing this exercise, we have changed the “ruler” that measures the distance between data points from _d_ ( _·, ·_ ) to _d_<sup>_∗_</sup> ( _·, ·_ ), metric learning can then very efficiently separate the data into different groups.

**Metric learning with Mahalanobis distance** To introduce some statistical terms (jargon), the distance measure used in the seminal work Xing et al. (2002) is based on the Mahalanobis distance, which measures the distance between two data points via


And they aim to find a matrix _M_ so that:

Figure 2: An example for Metric learning.


The optimization problem in (1) is a convex optimization problem and can be solved efficiently via projected gradient descent algorithm as discussed in Xing et al. (2002). Furthermore, the distance measure we adopt in (1) is a non-isotropic distance that reflects some intrinsic structure of the data.

After solving for _M_ , for a new patient with attribute x, we can calculate the average distances from x to the data labelled as 1, that is <u>�</u> _i_<sup>**1**(</sup> <u>1</u><sup>_Yi_=1)</sup> � _i_ : _Yi_ =1<sup>_dM_(</sup><sup>_Xi,_x),andtothedatalabelledas0,thatis</sup> <u>�</u> _i_<sup>**1**(</sup> <u>1</u><sup>_Yi_=0)</sup> � _i_ : _Yi_ =0<sup>_dM_(</sup><sup>_Xi,_x).Wepredicty = 1whenever</sup>


and vice versa.

Can you think about a different formulation of the optimization problem?

**Difference with Kernel methods?** Metric learning is natural to adapt for semi-supervised learning. Think about the example in Figure 3, where in total we have _n_ = 23 pictures of 4 bald Hollywood action

3


Figure 3: Who’s who? Illustration of metric learning applied to a face recognition task.

heroes. The goal is to use metric learning to identify how many different people there are and which faces belong to each person. Because metric learning needs us to specify a set that contains similar individuals _S_ , and a set that contains dissimilar individuals _D_ . Pairwise similarities are measured based on whether two images representing the same person (similar-link, shown in green) or different persons (dissimilar-link, shown in red). Based on measured similarities (note that we do not need to go for all pairs), we wish to adapt the metric so that we can separate these persons. The (deep) metric learning algorithms can automatically identified face into fours clusters. You can read more about this example in this post.

While metric learning is parametric (one learns the parameters of a given form of metric, such as a Mahalanobis distance), kernel learning is usually nonparametric: one learns the kernel matrix without any assumption on the form of the kernel that implicitly generated it. These approaches are thus very powerful but limited to the transductive setting and can hardly be applied to new data.

4

---

[Up: contents](index.md) · [2 Brainstorm time for the final project →](02-2-brainstorm-time-for-the-final-project.md)
