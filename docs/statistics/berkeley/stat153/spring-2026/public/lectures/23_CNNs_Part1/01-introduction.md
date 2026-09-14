---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/23_CNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/lectures/23_CNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **Lecture 23: Convolutional neural networks**

**Liberty Hamilton April 21, 2026**

_h/t to NeuroMatch academy (Alona Fyshe)_

## **Announcements**

- HW4 due this Thursday!

- • HW5 will be released later this week and will cover some DNN applications from these last modules (mostly not covered yet, so watch for the material as it comes)

- • Course evaluations open - please give your feedback, it’s helpful!

## **What is a convolutional neural network?**

- CNN, ConvNet

- • Deep learning model designed to process structured grid-like data by learning spatial hierarchies of features


image credit: https://developersbreach.com/convolution-neural-network-deep-learning/

## **Why should we care about them in time series analysis?**

• Can capture regular patterns over space (or time!)

• e.g. object detection

- Scale well to long sequences

- Frontend for modern sequence models (WavLM, wav2vec 2.0, HuBERT)


**Where’s Waldo?**

## **Outline**

• Motivation for CNNs from neuroscience

- Definitions, how it works

- Parts of a CNN

   - convolutional layers

   - pooling layers

   - • putting everything together

## **Visual Processing in the Brain**


<u>Hubel & Wiesel 1968</u>

## **Hierarchy of visual processing**


<u>Rolls 2021</u>

## **Invariance**


source: https://www.reddit.com/r/berkeleyca/comments/1kwdsgy/berkeley_rose_garden_astonishingly_full_of_bloom/


<u>Lipman et al. 2005</u>

Early History of CNNs


**Automatic handwriting recognition**


## **<u>LeNet (1998) Architecture</u>**

- Developed by Yann LeCun at Bell Labs

- Update of original version (1989)


## **LeNet (1998) Results**

- Successfully trained a 60,000 parameter neural network with no GPU acceleration

- Used for automatically reading zip codes on mail

- • 0.8% error on MNIST (near state of the art for the time!)


## **What are natural images made out of?**

- ImageNet ILSVRC (~1000 images in 1000 categories)

   - 1.2 million images in the training set

   - 50k validation, 100k test

- Variable resolution images

- • CNN to classify images into categories


## **Learned filters from CNNs**

---

[Up: contents](index.md) · [Krizhevsky et al., 2012 →](02-krizhevsky-et-al-2012.md)
