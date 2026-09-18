---
title: 'Lecture 23: Convolutional neural networks'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/23_CNNs_Part1.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/lectures/23_CNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 23: Convolutional neural networks

Liberty Hamilton
April 21, 2026

h/t to NeuroMatch academy (Alona Fyshe)

---

## Announcements

• HW4 due this Thursday!

• HW5 will be released later this week and will cover some DNN applications from these last modules (mostly not covered yet, so watch for the material as it comes)

• Course evaluations open - please give your feedback, it's helpful!

---

## What is a convolutional neural network?

• CNN, ConvNet

• Deep learning model designed to process structured grid-like data by learning spatial hierarchies of features

Convolution Neural Network (CNN)

image credit: https://developersbreach.com/convolution-neural-network-deep-learning/

---

## Why should we care about them in time series analysis?

• Can capture regular patterns over space (or time!)

• e.g. object detection

• Scale well to long sequences

• Frontend for modern sequence models (WavLM, wav2vec 2.0, HuBERT)

---

## Where's Waldo?

---

## Outline

• Motivation for CNNs from neuroscience

• Definitions, how it works

• Parts of a CNN
  • convolutional layers
  • pooling layers
  • putting everything together

---

## Visual Processing in the Brain

Hubel & Wiesel 1968

---

## Hierarchy of visual processing

Rolls 2021

---

## Invariance

Lipman et al. 2005

source: https://www.reddit.com/r/berkeleyca/comments/1kwdsgy/berkeley_rose_garden_astonishingly_full_of_bloom/

Matt Krause
mattkrause

---

## Early History of CNNs

---

## Automatic handwriting recognition

---

## LeNet (1998) Architecture

• Developed by Yann LeCun at Bell Labs

• Update of original version (1989)

Fig. 2. Architecture of LeNet-5, a Convolutional Neural Network, here for digits recognition. Each plane is a feature map, i.e. a set of units whose weights are constrained to be identical.

---

## LeNet (1998) Results

• Successfully trained a 60,000 parameter neural network with no GPU acceleration

• Used for automatically reading zip codes on mail

• 0.8% error on MNIST (near state of the art for the time!)

---

## What are natural images made out of?

• ImageNet ILSVRC (~1000 images in 1000 categories)

• 1.2 million images in the training set

• 50k validation, 100k test

• Variable resolution images

• CNN to classify images into categories

---

## Learned filters from CNNs

Krizhevsky et al., 2012

Hubel & Wiesel 1968

---

## Using CNNs to decode imagined images from the brain

Horikawa and Kamitani (2017)

---

## Example learned filters

Horikawa and Kamitani (2017)

---

## Representation Learning

• Deep learning is fundamentally about representation learning

• A representation is a symbol that approximates the entities and/or relations in the real world

• Your brain has representations of the real world because it cannot actually contain the real world

---

## How do CNNs work?

---

## Important properties

• Images, sound clips, other types of data have structure

• They can be stored as multi-dimensional arrays

• They feature axes for which ordering matters (e.g. width vs. height, time)

• One axis (the channel axis) can be used to access different views of the data (e.g. R/G/B color channels in an image, L/R of a stereo audio track)

---

## Discrete convolution

kernel

input feature map

output

Dumouilin and Visin 2018

Figure 1.1: Computing the output values of a discrete convolution.

---

## Discrete convolution

For input $X$ and kernel $K$

$$X = \begin{bmatrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \\ x_{41} & x_{42} & x_{43} & x_{44} \end{bmatrix}, \quad K = \begin{bmatrix} k_{11} & k_{12} & k_{13} \\ k_{21} & k_{22} & k_{23} \\ k_{31} & k_{32} & k_{33} \end{bmatrix}.$$

our output size with no padding and stride 1 will be:

$$(4 - 3 + 1) \times (4 - 3 + 1) = 2 \times 2$$

the general formula for the convolution is:

$$Y_{ij} = \sum_{m=1}^{3} \sum_{n=1}^{3} X_{i+m-1,\, j+n-1} \cdot K_{mn}.$$

---

## Step by step

• Position (1,1), kernel aligned with top-left 3x3 patch of input

$$Y_{11} = x_{11}k_{11} + x_{12}k_{12} + x_{13}k_{13} + x_{21}k_{21} + x_{22}k_{22} + x_{23}k_{23} + x_{31}k_{31} + x_{32}k_{32} + x_{33}k_{33}$$

• Position (1,2), slide one column right

$$Y_{12} = x_{12}k_{11} + x_{13}k_{12} + x_{14}k_{13} + x_{22}k_{21} + x_{23}k_{22} + x_{24}k_{23} + x_{32}k_{31} + x_{33}k_{32} + x_{34}k_{33}$$

• Position (2,1), left edge, one row down

\$\$Y_{21} = x_{21}k_{11} + x_{22}k_{12} + x_{23}k_{13}

---

[Up: contents](../../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 3 of the original](23_CNNs_Part1/figures/p003-1.png)

![Figure from page 5 of the original](23_CNNs_Part1/figures/p005-2.png)

![Figure from page 8 of the original](23_CNNs_Part1/figures/p008-1.png)

![Figure from page 8 of the original](23_CNNs_Part1/figures/p008-2.png)

![Figure from page 9 of the original](23_CNNs_Part1/figures/p009-1.png)

![Figure from page 10 of the original](23_CNNs_Part1/figures/p010-1.png)

![Figure from page 10 of the original](23_CNNs_Part1/figures/p010-2.png)

![Figure from page 12 of the original](23_CNNs_Part1/figures/p012-1.png)

![Figure from page 12 of the original](23_CNNs_Part1/figures/p012-2.png)

![Figure from page 13 of the original](23_CNNs_Part1/figures/p013-1.png)

![Figure from page 13 of the original](23_CNNs_Part1/figures/p013-2.png)

![Figure from page 14 of the original](23_CNNs_Part1/figures/p014-1.png)

![Figure from page 16 of the original](23_CNNs_Part1/figures/p016-1.png)

![Figure from page 16 of the original](23_CNNs_Part1/figures/p016-2.png)

![Figure from page 17 of the original](23_CNNs_Part1/figures/p017-1.png)

![Figure from page 18 of the original](23_CNNs_Part1/figures/p018-2.png)

![Figure from page 22 of the original](23_CNNs_Part1/figures/p022-1.png)

![Figure from page 22 of the original](23_CNNs_Part1/figures/p022-2.png)

![Figure from page 23 of the original](23_CNNs_Part1/figures/p023-1.png)

![Figure from page 23 of the original](23_CNNs_Part1/figures/p023-2.png)

![Figure from page 24 of the original](23_CNNs_Part1/figures/p024-1.png)

![Figure from page 24 of the original](23_CNNs_Part1/figures/p024-2.png)

![Figure from page 24 of the original](23_CNNs_Part1/figures/p024-3.png)

![Figure from page 24 of the original](23_CNNs_Part1/figures/p024-4.png)

![Figure from page 25 of the original](23_CNNs_Part1/figures/p025-1.png)

![Figure from page 25 of the original](23_CNNs_Part1/figures/p025-2.png)

![Figure from page 26 of the original](23_CNNs_Part1/figures/p026-1.png)

![Figure from page 26 of the original](23_CNNs_Part1/figures/p026-2.png)

![Figure from page 27 of the original](23_CNNs_Part1/figures/p027-1.png)

![Figure from page 27 of the original](23_CNNs_Part1/figures/p027-2.png)

![Figure from page 28 of the original](23_CNNs_Part1/figures/p028-1.png)

![Figure from page 28 of the original](23_CNNs_Part1/figures/p028-2.png)

![Figure from page 29 of the original](23_CNNs_Part1/figures/p029-1.png)

![Figure from page 29 of the original](23_CNNs_Part1/figures/p029-2.png)

![Figure from page 29 of the original](23_CNNs_Part1/figures/p029-3.png)

![Figure from page 31 of the original](23_CNNs_Part1/figures/p031-1.png)

![Figure from page 31 of the original](23_CNNs_Part1/figures/p031-2.png)

![Figure from page 32 of the original](23_CNNs_Part1/figures/p032-1.png)

![Figure from page 32 of the original](23_CNNs_Part1/figures/p032-2.png)

![Figure from page 32 of the original](23_CNNs_Part1/figures/p032-3.png)

![Figure from page 32 of the original](23_CNNs_Part1/figures/p032-4.png)

