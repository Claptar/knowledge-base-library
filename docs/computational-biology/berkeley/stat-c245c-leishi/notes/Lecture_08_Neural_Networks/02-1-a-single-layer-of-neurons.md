---
title: 1 A single-layer of neurons
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_08_Neural_Networks.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 A single-layer of neurons

**Source:** [`notes/Lecture_08_Neural_Networks.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_08_Neural_Networks.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The simplest kind of neural network is a single-layer perceptron network, which consists of a single layer of output nodes; the inputs (recorded in _x ∈_ R<sup>_d_</sup> ) are fed directly to the outputs via a series of weights:


The sum of the products of the weights w and the inputs _x_ is calculated in each node, and if the value is above some threshold _t_ (typically 0) the neuron fires and takes the activated value (equals 1 in the above activation function); otherwise it takes the deactivated value (equals 0 in our activation function). Neurons with this kind of activation function are also called **artificial neurons** or linear threshold units. In the literature the term perceptron often refers to networks consisting of just one of these units.

Note that what differentiates the outputs of different artificial neurons are their parameters (also referred to as their weights). Say we have access to _m_ neurons in total, and each neuron has weight w _j_ and bias _bj_ . The output of the neuron _j_ with an indicator activation function is thus


We can also instead use other form of the activation function instead of the step function. For example, sigmoid activation function is also frequently used due to its clear benefit in optimization (we will see this in a minute)


1


Figure 1: Illustration of how one neuron _k_ stimulated by the synaptic changes _Xi_ = ( _Xi_ 1 _, . . . , Xid_ )<sup>_′_</sup> and then produces an output _hi_ .

So what do these activations really tell us? Well, one can think of these activations as indicators of the presence of some weighted combination of features. We can then use a combination of these activations to perform classification tasks.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Feed-forward Computation →](03-2-feed-forward-computation.md)
