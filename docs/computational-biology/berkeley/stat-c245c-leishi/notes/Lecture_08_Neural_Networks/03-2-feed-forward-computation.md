---
title: 2 Feed-forward Computation
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_08_Neural_Networks.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Feed-forward Computation

**Source:** [`notes/Lecture_08_Neural_Networks.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Similar to our problem setup in the supervised learning section, the learner receives a training sample _S_ = _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>ofsize</sup><sup>_n_i.i.dfrom</sup><sup>_X_accordingtosomeunknowndistribution</sup><sup>_F_(</sup><sup>_·_),with</sup> _Yi_ = _f_ ( _Xi_ ) and _Xi ∈_ R<sup>_d_</sup> , _Yi ∈{_ 0 _,_ 1 _}_ . Instead of building a linear classifier from the set:


we search a classifier from a class of non-linear functions:


The question is then how to choose the mapping _φ_ ( _·_ ):

1. One option is to use a very generic _φ_ , such as the infinite-dimensional _φ_ used by kernel machines based on the gaussian kernel. However, such a method often faces difficulties when generalizing the prediction model to test data.

2. Another option is to manually engineer _φ_ ( _·_ ). Until the advent of deep learning, this was the dominant approach. It requires a decade of human effort for each separate task, with practitioners specializing in different domains.

3. The strategy of deep learning is to learn _φ_ . In this approach, we essentially model the outcome

2

with


where the parameter _θ_ needed to learn from a broad class of functions, and _β_ maps from _φ_ ( _x_ ) to desired outputs. This is an example of a deep feedforward network with _φ_ defining a hidden layer. This approach is the only one of the three

Suppose for now we can stack these activation functions _g_ ( _·_ ) together as


and the activation function _g_ ( _·_ ) is applied component-wise. Then our complete network function is defined as


Our goal is to learn the relationship between an outcome _y_ and the input vector _x_ : _y_ = _f_ ( _x_ ) based on our training data. In other words, given a set of input vectors and the outcome, we aim to learn _f_ ( _·_ ) based on _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>.Like most machine learning models,neural networks also need</sup> an optimization objective, a measure of error or goodness which we want to minimize or maximize respectively. We may chose the mean squared error loss function to simplify the mathematical derivation as much as possible. The MSE loss function is


Training a Other loss function we have introduced in the empirical risk minimization section can be applied as well.

Multilayer neurons work in a similar fashion, see Figure 2 for illustration.

---

[← 1 A single-layer of neurons](02-1-a-single-layer-of-neurons.md) · [Up: contents](index.md) · [3 Training with backpropagation →](04-3-training-with-backpropagation.md)
