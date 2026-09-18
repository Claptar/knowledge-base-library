---
title: 'Lecture 24: Convolutional neural networks part 2'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/24_CNNs_Part2.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/lectures/24_CNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 24: Convolutional neural networks part 2

Liberty Hamilton
April 23, 2026

*h/t to NeuroMatch academy (Alona Fyshe)*

---

## What do you think would happen?

Given an image $A$ and the kernel $K$ below

$$K$$

$$\mathbf{G}_x = \begin{bmatrix} -1 & 0 & +1 \\ -2 & 0 & +2 \\ -1 & 0 & +1 \end{bmatrix} * \mathbf{A} \qquad \mathbf{G}_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ +1 & +2 & +1 \end{bmatrix} * \mathbf{A}$$

Image $A$

---

## But how do we get all the edges?

nonlinear combination of Gx and Gy

- We need a nonlinearity!
- In CNNs, this is typically done using a ReLU (rectified linear unit)
  - $\text{ReLU}(x) = \max(0, x)$

---

## STRF and time lagged regression as convolution

- Here we are convolving our 2D STRF filter (the beta weights from time lagged regression) with our feature matrix to produce the predicted neural data (red trace on top)

---

## What are the building blocks of CNNs?

---

## Elements of a CNN

Convolution Neural Network (CNN)

1. Input layer
2. Convolutional layer
3. Activation layer (introduces nonlinearity)
4. Pooling layer
5. Flattening
6. Fully connected (dense) layer
7. Output layer

---

## Example convolution operations (from last time)

Output
$Y \in \mathbb{R}^{3 \times 3}$

Kernel
$K \in \mathbb{R}^{3 \times 3}$

Input $X \in \mathbb{R}^{5 \times 5}$

padding, stride=2

Output
$Y \in \mathbb{R}^{5 \times 5}$

Kernel
$K \in \mathbb{R}^{3 \times 3}$

Input $X \in \mathbb{R}^{5 \times 5}$

"same" padding, stride=1

---

## Combining multiple filters

---

[Up: contents](../../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 2 of the original](24_CNNs_Part2/figures/p002-1.png)

![Figure from page 2 of the original](24_CNNs_Part2/figures/p002-2.png)

![Figure from page 2 of the original](24_CNNs_Part2/figures/p002-3.png)

![Figure from page 2 of the original](24_CNNs_Part2/figures/p002-4.png)

![Figure from page 3 of the original](24_CNNs_Part2/figures/p003-1.png)

![Figure from page 4 of the original](24_CNNs_Part2/figures/p004-1.png)

![Figure from page 6 of the original](24_CNNs_Part2/figures/p006-1.png)

![Figure from page 7 of the original](24_CNNs_Part2/figures/p007-1.png)

![Figure from page 7 of the original](24_CNNs_Part2/figures/p007-2.png)

![Figure from page 8 of the original](24_CNNs_Part2/figures/p008-1.png)

![Figure from page 8 of the original](24_CNNs_Part2/figures/p008-2.png)

![Figure from page 9 of the original](24_CNNs_Part2/figures/p009-1.png)

![Figure from page 10 of the original](24_CNNs_Part2/figures/p010-1.png)

![Figure from page 11 of the original](24_CNNs_Part2/figures/p011-1.png)

![Figure from page 11 of the original](24_CNNs_Part2/figures/p011-2.png)

![Figure from page 12 of the original](24_CNNs_Part2/figures/p012-1.png)

![Figure from page 13 of the original](24_CNNs_Part2/figures/p013-1.png)

![Figure from page 13 of the original](24_CNNs_Part2/figures/p013-2.png)

![Figure from page 14 of the original](24_CNNs_Part2/figures/p014-1.png)

![Figure from page 15 of the original](24_CNNs_Part2/figures/p015-3.png)

![Figure from page 16 of the original](24_CNNs_Part2/figures/p016-1.png)

![Figure from page 17 of the original](24_CNNs_Part2/figures/p017-1.png)

![Figure from page 18 of the original](24_CNNs_Part2/figures/p018-1.png)

![Figure from page 19 of the original](24_CNNs_Part2/figures/p019-1.png)

![Figure from page 20 of the original](24_CNNs_Part2/figures/p020-3.png)

![Figure from page 21 of the original](24_CNNs_Part2/figures/p021-3.png)

![Figure from page 24 of the original](24_CNNs_Part2/figures/p024-2.png)

![Figure from page 25 of the original](24_CNNs_Part2/figures/p025-2.png)

![Figure from page 27 of the original](24_CNNs_Part2/figures/p027-2.png)

![Figure from page 28 of the original](24_CNNs_Part2/figures/p028-1.png)

![Figure from page 33 of the original](24_CNNs_Part2/figures/p033-1.png)

