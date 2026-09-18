---
title: 'Part 0: Warm-up'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Part 0: Warm-up

Before we start on the main problems, we'll work through this short warm-up to make sure you are comfortable with PyTorch's shape conventions. This helps to set you up for Question 1.

## Shape conventions for Conv1d

A 1D convolutional layer in PyTorch expects input tensors of shape

$$(\text{batch},\ \text{channels},\ \text{length}).$$

- **batch**: how many independent signals you are processing in parallel (e.g., 32 EEG trials).
- **channels**: how many parallel values exist at each timepoint (e.g., 1 for a univariate signal, 64 for 64 electrodes, 40 for 40 frequency bins). Channels are *not* a spatial axis. Rather, the kernel looks across all of them simultaneously at each position.
- **length**: the temporal axis. This is what the kernel slides along, and this is the $L$ in the output-length formula.

The "1D" in "1D convolution" means the kernel slides along **one axis** (length). We never slide over batch or channels.

## Worked example

Suppose the input has shape $(\text{batch}=2,\ \text{channels}=1,\ \text{length}=10)$ and we apply a `Conv1d` with 4 filters, kernel size 3, no padding, stride 1. We can use the formula at the top of this notebook:

- Output length: $L_{\text{out}} = \lfloor (10 + 0 - 3)/1 \rfloor + 1 = 8$.
- Output channels: equal to the number of filters = 4.
- Output shape: $(2, 4, 8)$.

Each of the 4 filters has shape $(\text{in_channels}=1) \times (\text{kernel_size}=3) = 3$ weights, so the layer has $4 \times 3 = 12$ weight parameters (plus 4 biases if biases are enabled).

## Verify in code

Run the cell below to confirm the shape calculation, then modify it and predict before running.

```python
# Build the layer from the worked example
layer = nn.Conv1d(in_channels=1, out_channels=4, kernel_size=3)

# Apply it to a batch of 2 univariate signals of length 10
x = torch.randn(2, 1, 10) # initialize some random data
out = layer(x) # apply convolutional layer

print("input shape: ", tuple(x.shape))        # expect (2, 1, 10)
print("output shape:", tuple(out.shape))      # expect (2, 4, 8)
print("weight shape:", tuple(layer.weight.shape))  # expect (4, 1, 3)
print("n weight params:", layer.weight.numel())    # expect 12
```

```python
# ---- Predict-then-verify ----
# Before running the lines below, predict:
#   1. What output shape do you expect if kernel_size is 5 instead of 3?
#   2. What if you add padding=2 (with kernel_size=5)?
#   3. What if the input has 3 channels instead of 1 (so x.shape = (2, 3, 10)),
#      with kernel_size=3 and out_channels=4? How many weights does the layer have now?

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

**Expected answers** (check after you run the code):

1. Output shape $(2, 4, 6)$ — length drops by $k - 1 = 4$.
2. Output shape $(2, 4, 10)$ — "same" padding preserves length.
3. Output shape $(2, 4, 8)$. The layer has $4 \times 3 \times 3 = 36$ weights: each filter now looks across all 3 input channels, so the per-filter weight count is $\text{in_channels} \times \text{kernel_size}$.

In the third case, note that `in_channels` multiplies into the per-filter weight count, even though the kernel only slides along the length axis. This will matter for Question 2, which uses 3 RGB input channels.

---

Now let's start the questions.

---

[← Stat153 248 Homework5 Part 02 —](02-stat153-248-homework5-part-02.md) · [Up: contents](index.md) · [Part 1: Convolution mechanics →](04-part-1-convolution-mechanics.md)
