---
title: 'Part 0: Warm-up'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Part 0: Warm-up

Before we start on the main problems, we'll work through this short warm-up to make sure you are comfortable with PyTorch's shape conventions. This helps to set you up for Question 1.

### Shape conventions for Conv1d

A 1D convolutional layer in PyTorch expects input tensors of shape

$$(\text{batch}, \text{channels}, \text{length}).$$

* **batch**: how many independent signals you are processing in parallel (e.g., 32 EEG trials).
* **channels**: how many parallel values exist at each timepoint (e.g., 1 for a univariate signal, 64 for 64 electrodes, 40 for 40 frequency bins). Channels are *not* a spatial axis. Rather, the kernel looks across all of them simultaneously at each position.
* **length**: the temporal axis. This is what the kernel slides along, and this is the $L$ in the output-length formula.

The "1D" in "1D convolution" means the kernel slides along **one axis** (length). We never slide over batch or channels.

### Worked example

Suppose the input has shape $(\text{batch} = 2, \text{channels} = 1, \text{length} = 10)$ and we apply a `Conv1d` with 4 filters, kernel size 3, no padding, stride 1. We can use the formula at the top of this notebook:

* Output length: $L_{\text{out}} = \lfloor (10 + 0 - 3)/1 \rfloor + 1 = 8$.
* Output channels: equal to the number of filters = 4.
* Output shape: $(2, 4, 8)$.

Each of the 4 filters has shape $(\text{in_channels} = 1) \times (\text{kernel_size} = 3) = 3$ weights, so the layer has $4 \times 3 = 12$ weight parameters (plus 4 biases if biases are enabled).

### Verify in code

Run the cell below to confirm the shape calculation, then modify it and predict before running.

```python
# Build the layer from the worked example
layer = nn.Conv1d(in_channels=1, out_channels=4, kernel_size=3)

# Apply it to a batch of 2 univariate signals of length 10
x = torch.randn(2, 1, 10) # initialize some random data
out = layer(x) # apply convolutional layer

print("input shape: ", tuple(x.shape)) # expect (2, 1, 10)
print("output shape:", tuple(out.shape)) # expect (2, 4, 8)
print("weight shape:", tuple(layer.weight.shape)) # expect (4, 1, 3)
print("n weight params:", layer.weight.numel()) # expect 12
```

```python
# ---- Predict-then-verify ----
# Before running the lines below, predict:
# 1. What output shape do you expect if kernel_size is 5 instead of 3?
# 2. What if you add padding=2 (with kernel_size=5)?
# 3. What if the input has 3 channels instead of 1 (so x.shape = (2, 3, 10))
# with kernel_size=3 and out_channels=4? How many weights does the layer have?
# Uncomment one block at a time after making your prediction.

# (1) kernel_size=5
# print('\nkernel_size=5, padding=0, stride=1, length=10')
# layer2 = nn.Conv1d(1, 4, kernel_size=5)
# print(layer2(torch.randn(2, 1, 10)).shape)

# (2) kernel_size=5, padding=2
# print('\nkernel_size=5, padding=2, stride=1, length=10')
# layer3 = nn.Conv1d(1, 4, kernel_size=5, padding=2)
# print(layer3(torch.randn(2, 1, 10)).shape)

# (3) in_channels=3
# print('\ninput_channels=3, kernel_size=3, padding=0, stride=1, length=10')
# layer4 = nn.Conv1d(3, 4, kernel_size=3)
# print(layer4(torch.randn(2, 3, 10)).shape)
# print("\nn weight params:", layer4.weight.numel())
```

Expected answers (check after you run the code):

1. Output shape $(2, 4, 6)$ — length drops by $k - 1 = 4$.
2. Output shape $(2, 4, 10)$ — "same" padding preserves length.
3. Output shape $(2, 4, 8)$. The layer has $4 \times 3 \times 3 = 36$ weights: each filter now looks across all 3 input channels, so the per-filter weight count is $\text{in_channels} \times \text{kernel_size}$.

In the third case, note that `in_channels` multiplies into the per-filter weight count, even though the kernel only slides along the length axis. This will matter for Question 2, which uses 3 RGB input channels.

Now let's start the questions.

## Part 1: Convolution mechanics

The first four questions ask you to compute output shapes and parameter counts by hand, then verify your answers in code.

## Question 1 (4 points)

A 1D convolutional layer has:

* input shape `(batch, 1, 100)` or `(batch, channels, length)`. Batch is how many independent samples we process at once, channels is how many parallel signals at each point, and length is the temporal axis that the kernel slides along.
* 8 filters
* kernel size 7
* no padding
* stride 1

Compute:

**(a)** The output shape.

**(b)** The total number of *weights* in this layer (ignoring biases - which can be used if the input data and features are not centered).

**(c)** The total number of weights if this layer were fully connected instead (i.e., every input element connected to every hidden unit, where the number of hidden units equals the flattened output size from part (a)).

**(d)** The ratio of fully-connected to convolutional weights. Briefly explain in one sentence what property of convolutional layers is responsible for this ratio.

### Your answer:

(a)

(b)

(c)

(d)

## Question 2 (2 points)

A 2D convolutional layer takes an RGB image of shape `(batch, 3, 64, 64)` and applies 16 filters of size 5×5 with `padding=2` (same padding) and `stride=1`.

**(a)** What is the output shape?

**(b)** How many weights does this layer have (ignore biases)? Be explicit about where each factor comes from.

### Your answer:

(a)

(b)

## Question 3 (2 points)

Consider three padding strategies for a 1D convolution with kernel size 5 applied to an input of length 20:

* **Valid padding** ($p = 0$)
* **Same padding** ($p = 2$)
* **Full padding** ($p = 4$)

**(a)** Compute the output length for each (stride 1).

**(b)** In lecture 23 there was a brief discussion about padding choices in a *time series* context (forward vs. backward in time). Briefly describe what "causal padding" would mean and why it matters for a model that should not peek into the future.

### Your answer:

(a)

(b)

## Part 2: Architecture

For these questions, we will talk about the architecture of CNNs and how to calculate the number of weights in different networks.

## Question 4 (5 points)

Lecture 24 argued that a fully-connected network for a 256×256 RGB image (3 color channels) with 1000 hidden units and 1000 output classes has a very large number of weights. Compute this number and show your work. Then compute the weight count if each of the 1000 hidden units has its receptive field restricted to 11×11 pixels (still using all 3 color channels). What is the reduction factor?

### Your answer:

## Question 5 (3 points)

State whether each of the following is true or false, and give a one-sentence justification.

**(a)** Max pooling over a filter's response map makes the network's decision approximately invariant to *where* in the input the feature appears.

**(b)** A ReLU nonlinearity can be replaced by a linear function without loss of expressiveness, as long as enough layers are stacked.

**(c)** Two stacked 3×3 convolutional layers have the same effective receptive field as one 5×5 convolutional layer. (Hint: compute the

### Your answer:

(a)

(b)

(c)

## Part 3: Code exercises

Use the code cells below. Answers should be kept short.

## Question 6 (3 points): verify your shape calculations

Construct an `nn.Conv2d` layer matching the specification in Question 2 (input `(1, 3, 64, 64)`, 16 filters of size 5×5, same padding). Apply it to a random input tensor using `torch.randn` for an input of shape `(1, 3, 64, 64)`. Print both the output shape and the total number of weights in the layer's `.weight` parameter. Confirm that they match your hand calculations from Question 2.

```python
# Solution for Q6
layer = nn.Conv2d(## FILL IN##)
x = torch.randn(##FILL IN##)
out = # Apply the conv layer

# Print output shape:

# Print weight tensor shape:

# Print total number of weights:
```

---

[← Receptive field](02-receptive-field.md) · [Up: contents](index.md) · [Question 7 (5 points): parameter counting →](04-question-7-5-points-parameter-counting.md)
