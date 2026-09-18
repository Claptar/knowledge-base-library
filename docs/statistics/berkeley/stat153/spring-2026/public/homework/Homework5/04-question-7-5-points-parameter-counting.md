---
title: 'Question 7 (5 points): parameter counting'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Question 7 (5 points): parameter counting

Define a small 1D CNN for waveform classification with the architecture below. Then write code that prints the number of trainable parameters in each layer and the total.

```
Conv1d(1 -> 16, kernel_size=32, stride=4, padding=16) ->
ReLU -> MaxPool1d(4)
Conv1d(16 -> 32, kernel_size=3, padding=1) ->
ReLU -> MaxPool1d(4)
Conv1d(32 -> 64, kernel_size=3, padding=1) ->
ReLU -> AdaptiveAvgPool1d(1)
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
# conv1 weight: 1*16*32 = 512, bias: 16 -> 528
# conv2 weight: 16*32*3 = 1536, bias: 32 -> 1568
# conv3 weight: 32*64*3 = 6144, bias: 64 -> 6208
# fc weight: 64*10 = 640, bias: 10 -> 650
# total = 8954
```

## Question 8 (2 points)

You are designing a classifier for two different tasks. For each, state whether you would use a **1D CNN on the raw waveform**, a **2D CNN on a spectrogram**, or a **non-convolutional model** (e.g., logistic regression on hand-engineered features). Justify your choice in one or two sentences referencing specific properties of convolutional models.

**(a)** Detecting a single, fixed, known template (e.g., a specific epileptic spike waveform) in continuous time series brain data (EEG).

**(b)** Classifying spoken words from raw audio, where pronunciation varies across speakers and time.

### Your answer:

(a)

(b)

## Question 9 (2 points)

A student trains two models on the same audio dataset with the same architecture and hyperparameters. The only difference is the train/test split:

* **Model A:** random 80/20 split of all recordings.
* **Model B:** held-out speaker where all recordings from one speaker are in the test set, none in the training set.

Model A achieves 95% test accuracy; Model B achieves 45% test accuracy.

**(a)** Explain the gap. What has Model A likely learned that Model B is failing to exploit?

**(b)** Which number better reflects how well the model will perform on a *new user* of the system, and why?

### Your answer:

(a)

(b)

---

[← Part 0: Warm-up](03-part-0-warm-up.md) · [Up: contents](index.md) · [Part 4: Recurrent neural networks →](05-part-4-recurrent-neural-networks.md)
