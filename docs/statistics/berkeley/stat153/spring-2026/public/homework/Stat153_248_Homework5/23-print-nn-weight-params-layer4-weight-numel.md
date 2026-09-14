---
title: print("\nn weight params:", layer4.weight.numel())
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# print("\nn weight params:", layer4.weight.numel())

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

**Expected answers** (check after you run the code):

1. Output shape $(2, 4, 6)$ — length drops by $k - 1 = 4$.
2. Output shape $(2, 4, 10)$ — "same" padding preserves length.
3. Output shape $(2, 4, 8)$. The layer has $4 \times 3 \times 3 = 36$ weights: each filter now looks across all 3 input channels, so the per-filter weight count is $\text{in\_channels} \times \text{kernel\_size}$.

In the third case, note that `in_channels` multiplies into the per-filter weight count, even though the kernel only slides along the length axis. This will matter for Question 2, which uses 3 RGB input channels.

---

Now let's start the questions.

## Part 1: Convolution mechanics

The first four questions ask you to compute output shapes and parameter counts by hand, then verify your answers in code.

### Question 1 (4 points)

A 1D convolutional layer has:

- input shape `(batch, 1, 100)` or `(batch, channels, length)`. Batch is how many independent samples we process at once, channels is how many parallel signals at each point, and length is the temporal axis that the kernel slides along.
- 8 filters
- kernel size 7
- no padding
- stride 1

Compute:

**(a)** The output shape.

**(b)** The total number of *weights* in this layer (ignoring biases - which can be used if the input data and features are not centered).

**(c)** The total number of weights if this layer were fully connected instead (i.e., every input element connected to every hidden unit, where the number of hidden units equals the flattened output size from part (a)).

**(d)** The ratio of fully-connected to convolutional weights. Briefly explain in one sentence what property of convolutional layers is responsible for this ratio.

**Your answer:**

(a)

(b)

(c)

(d)

### Question 2 (2 points)

A 2D convolutional layer takes an RGB image of shape `(batch, 3, 64, 64)` and applies 16 filters of size 5×5 with `padding=2` (same padding) and `stride=1`.

**(a)** What is the output shape?

**(b)** How many weights does this layer have (ignore biases)? Be explicit about where each factor comes from.

**Your answer:**

(a)

(b)

### Question 3 (2 points)

Consider three padding strategies for a 1D convolution with kernel size 5 applied to an input of length 20:

- **Valid padding** ($p=0$)
- **Same padding** ($p=2$)
- **Full padding** ($p=4$)

**(a)** Compute the output length for each (stride 1).

**(b)** In lecture 23 there was a brief discussion about padding choices in a *time series* context (forward vs. backward in time). Briefly describe what "causal padding" would mean and why it matters for a model that should not peek into the future.

**Your answer:**

(a)

(b)

## Part 2: Architecture

For these questions, we will talk about the architecture of CNNs and how to calculate the number of weights in different networks.

### Question 4 (5 points)

Lecture 24 argued that a fully-connected network for a 256×256 RGB image (3 color channels) with 1000 hidden units and 1000 output classes has a very large number of weights. Compute this number and show your work. Then compute the weight count if each of the 1000 hidden units has its receptive field restricted to 11×11 pixels (still using all 3 color channels). What is the reduction factor?

**Your answer**:

### Question 5 (3 points)

State whether each of the following is true or false, and give a one-sentence justification.

**(a)** Max pooling over a filter's response map makes the network's decision approximately invariant to *where* in the input the feature appears.

**(b)** A ReLU nonlinearity can be replaced by a linear function without loss of expressiveness, as long as enough layers are stacked.

**(c)** Two stacked 3×3 convolutional layers have the same effective receptive field as one 5×5 convolutional layer. (Hint: compute the

**Your answer:**

(a)

(b)

(c)

## Part 3: Code exercises

Use the code cells below. Answers should be kept short.

### Question 6 (3 points): verify your shape calculations

Construct an `nn.Conv2d` layer matching the specification in Question 2 (input `(1, 3, 64, 64)`, 16 filters of size 5×5, same padding). Apply it to a random input tensor using `torch.randn` for an input of shape `(1, 3, 64, 64)`. Print both the output shape and the total number of weights in the layer's `.weight` parameter. Confirm that they match your hand calculations from Question 2.

```python

---

[← print(layer4(torch.randn(2, 3, 10)).shape)](22-print-layer4-torch-randn-2-3-10-shape.md) · [Up: contents](index.md) · [Solution for Q6 →](24-solution-for-q6.md)
