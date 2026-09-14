---
title: 3 Training with backpropagation
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_08_Neural_Networks.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Training with backpropagation

**Source:** [`notes/Lecture_08_Neural_Networks.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Training a feedforward neural network is not much different from training any other machine leanring model with gradient descent. Suppose _θ_ contains all unknown parameters including _β_ , _W_ and _b_ , we typically need the gradient information for any parameters as required in the update equation:


Backpropagation is technique that allows us to efficiently use the chain rule of differentiation to calculate loss gradients for any parameter used in the feed-forward computation on the model. To

3


Figure 2: Illustration of a multilayer neural network.

understand this further, let us understand a toy network with two neurons for which we perform backpropagation. Note that the term “backpropagation” strictly refers only to the algorithm for computing the gradient, not how the gradient is used.

Suppose we have one input vector _x_ . When it passes the first neuron, the input is weighted by w1 and produce some product function _P_ 1 = _x_<sup>_′_</sup> _w_ 1. The performance function then goes through some activation function, say sigmoid activation function _σ_ ( _P_ 1), resulting in an outcome _y_ . The outcome _y_ then goes through another neuron, weighted by _w_ 2, resulting in a product function _P_ 2 = _y_<sup>_′_</sup> w2. In the last step, we go though another sigmoid function _σ_ ( _P_ 2), which is the final outcome, denoted as _z_ . Therefore the loss function is of the form:


where _d_ is the desired outcome. The unknown parameters are thus _θ_ = (w1 _,_ w2).

Now we want to evaluate the change of the loss function with respect to w2 (gradient),


where the second term can be again replaced through chain rule:


This means:


4

Note that for a given smooth sigmoid function, all above derivatives can be calculated. Benefiting from the sigmoid activation function we have adopted _σ_ ( _x_ ) = 1+1 _e_<sup>_<u>−x</u>_,wethushave</sup>


Similarly for the partial derivative with respect to w1, we have


Now the gradients are computed, and we can continue to train the neural networks with gradientbased algorithms.

An algorithm usually contains two interactive passes: (1) forward pass that gives some input values and learns the final outcome, and (2) backward pass that learns the gradient of the objective function.

5

---

[← 2 Feed-forward Computation](03-2-feed-forward-computation.md) · [Up: contents](index.md) · [References →](05-references.md)
