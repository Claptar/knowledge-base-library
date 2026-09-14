---
title: Stat 153/248 - Homework 5 - YOUR NAME HERE {-}
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat 153/248 - Homework 5 - YOUR NAME HERE {-}

**Source:** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## Student ID: {-}

## Collaborated with: {-}

Due May 7 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

Instructions: Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

## Instructions:

Below is some helpful information for you as you solve these homework problems. "Part 0" will also cover some important intro material to help supplement what you saw in Lecture.

These models don't work well in the datahub, so you'll want to install pytorch on your own computer.

### Convolution output shape formula

For a 1D convolution with input length L, kernel size k, padding p, and stride s, the output length is


You may apply this over multiple independent batches and using different numbers of filters (with some kernel size).

For 2D, the same formula applies independently to each spatial dimension.

### Receptive field

The receptive field of an output unit is the number of input positions that unit depends on. It is a property of the architecture and does not change with input length.

For a single conv layer with kernel size k, each output unit sees k consecutive input positions, so the receptive field is k.


When you stack conv layers, the receptive field grows. Let's consider two 1D conv layers, each with kernel size k = 3:

- One unit in layer 2 sees 3 consecutive units in layer 1.

- Each of those 3 layer-1 units sees 3 consecutive units in the input.

- The leftmost layer-1 unit covers input positions 0, 1, 2. The rightmost covers 2, 3, 4. So a single layer-2 unit depends on input positions 0 through 4 — a receptive field of 5.


In general, for n stacked conv layers with kernel size k (stride 1):

RFn = n(k −1) + 1.

Two 3×3 layers → RF = 5. Three 3×3 layers → RF = 7. This is why deep networks built from small kernels can still cover large input regions: receptive field grows linearly with depth. On the left, we have 3 1D conv layers with kernel size k = 3, on the right, 3 1D conv layers with kernel size k = 5:


Note that receptive field is different from output length. Output length tells you how many positions remain after the convolutions; receptive field tells you, for one of those output positions, how many input positions contributed to it. Both involve (k −1) terms but they answer different questions.

```
In [ ]:import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
```

```
torch.manual_seed(0)
np.random.seed(0)
```

## Part 0: Warm-up

Before we start on the main problems, we'll work through this short warm-up to make sure you are comfortable with PyTorch's shape conventions. This helps to set you up for Question 1.

### Shape conventions for Conv1d

A 1D convolutional layer in PyTorch expects input tensors of shape

(batch, channels, length).

- batch: how many independent signals you are processing in parallel (e.g., 32 EEG trials).

- channels: how many parallel values exist at each timepoint (e.g., 1 for a univariate signal, 64 for 64 electrodes, 40 for 40 frequency bins). Channels are not a spatial axis. Rather, the kernel looks across all of them simultaneously at each position.

- length: the temporal axis. This is what the kernel slides along, and this is the L in the output-length formula.

The "1D" in "1D convolution" means the kernel slides along one axis (length). We never slide over batch or channels.

### Worked example

Suppose the input has shape (batch = 2, channels = 1, length = 10) and we apply a <mark>`Conv1d`</mark> with 4 filters, kernel size 3, no padding, stride 1. We can use the formula at the top of this notebook:

- Output length: Lout = ⌊(10 + 0 −3)/1⌋ + 1 = 8.

- Output channels: equal to the number of filters = 4.

- Output shape: (2, 4, 8).

Each of the 4 filters has shape (in\_channels = 1) × (kernel\_size = 3) = 3 weights, so the layer has 4 × 3 = 12 weight parameters (plus 4 biases if biases are enabled).

### Verify in code

Run the cell below to confirm the shape calculation, then modify it and predict before running.

```
In [ ]:# Build the layer from the worked example
layer = nn.Conv1d(in_channels=1, out_channels=4, kernel_size=3)

---

[Up: contents](index.md) · [Apply it to a batch of 2 univariate signals of length 10 →](02-apply-it-to-a-batch-of-2-univariate-signals-of-length-10.md)
