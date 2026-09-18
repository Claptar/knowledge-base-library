---
title: 'Part 3: Code exercises'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Part 3: Code exercises

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

## Question 7 (5 points): parameter counting

Define a small 1D CNN for waveform classification with the architecture below. Then write code that prints the number of *trainable* parameters in each layer and the total.

```
Conv1d(1   -> 16, kernel_size=32, stride=4, padding=16)  -> ReLU -> MaxPool1d(4)
Conv1d(16  -> 32, kernel_size=3,  padding=1)             -> ReLU -> MaxPool1d(4)
Conv1d(32  -> 64, kernel_size=3,  padding=1)             -> ReLU -> AdaptiveAvgPool1d(1)
Linear(64 -> 10)
```

Hint: biases count as parameters. A `Conv1d(in, out, k)` layer has `in*out*k + out` parameters total; `Linear(a, b)` has `a*b + b`.

```python
# Solution for Q7
model = nn.Sequential(
    nn.Conv1d(##FILLIN),
    nn.ReLU(##FILLIN),
    nn.MaxPool1d(##FILLIN),
    ## ADD The OTHER LAYERS HERE
)

total = 0
for name, p in model.named_parameters():
    if p.requires_grad:
        print(f"{name:20s} {tuple(p.shape)!s:20s} {p.numel():>6d}")
        total += p.numel()
print(f"{'total':20s} {'':20s} {total:>6d}")

# Expected (by hand):
# conv1 weight: 1*16*32 = 512, bias: 16   -> 528
# conv2 weight: 16*32*3 = 1536, bias: 32  -> 1568
# conv3 weight: 32*64*3 = 6144, bias: 64  -> 6208
# fc weight: 64*10 = 640, bias: 10        -> 650
# total = 8954
```

## Question 8 (2 points)

You are designing a classifier for two different tasks. For each, state whether you would use a **1D CNN on the raw waveform**, a **2D CNN on a spectrogram**, or a **non-convolutional model** (e.g., logistic regression on hand-engineered features). Justify your choice in one or two sentences referencing specific properties of convolutional models.

**(a)** Detecting a single, fixed, known template (e.g., a specific epileptic spike waveform) in continuous time series brain data (EEG).

**(b)** Classifying spoken words from raw audio, where pronunciation varies across speakers and time.

**Your answer:**

(a)

(b)

## Question 9 (2 points)

A student trains two models on the same audio dataset with the same architecture and hyperparameters. The only difference is the train/test split:

- **Model A:** random 80/20 split of all recordings.
- **Model B:** held-out speaker where all recordings from one speaker are in the test set, none in the training set.

Model A achieves 95% test accuracy; Model B achieves 45% test accuracy.

**(a)** Explain the gap. What has Model A likely learned that Model B is failing to exploit?

**(b)** Which number better reflects how well the model will perform on a *new user* of the system, and why?

**Your answer:**

(a)

(b)

---

[← Part 1: Convolution mechanics](04-part-1-convolution-mechanics.md) · [Up: contents](index.md) · [Part 4: Recurrent neural networks →](06-part-4-recurrent-neural-networks.md)
