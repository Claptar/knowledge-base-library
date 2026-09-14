---
title: 1 Naive Bayes Classification
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Naive Bayes Classification

**Source:** `psets/02-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will use a Naive Bayes classifier to label fragments of the genome based on sequence properties.

- (a) Suppose we want to classify sequence fragments into categories (represented by random variable Y): genes, regulatory motifs, or repetitive elements. We want to use the following features: length X1, GC content (proportion of bases which are G or C) X2, and _complexity_ X3 (intuitively, what fraction of possible k-mers are observed).

Does the naive Bayes assumption hold in this setting? Explain why or why not.

- (b) Regardless of whether the naive Bayes assumption holds, we can still build a classifier. (Surprisingly, naive Bayes classifiers perform well in many applications where this assumption does not hold.) To simplify, we will discretize each of the features.

Given the training set below, write down the maximum likelihood estimates (recall these are relative fre­ quencies) of each of the conditional probability distributions P(Xi | Y) and the prior probability distribution P(Y).

|**GC** **Content**|**Length**|**Complexity**|**Class**|
|---|---|---|---|
|Low|Long|High|Gene|
|Low|Long|Low|Gene|
|High|Long|High|Repeat|
|Medium|Short|High|Motif|
|Medium|Short|Low|Motif|
|High|Long|Low|Repeat|
|High|Short|High|Motif|
|Medium|Long|High|Gene|
|High|Long|Low|Repeat|
|High|Short|High|Motif|


(c) Given the model, compute the maximum a posteriori estimate of the class of the new observation below.


1

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Classification of conserved regions →](03-2-classification-of-conserved-regions.md)
