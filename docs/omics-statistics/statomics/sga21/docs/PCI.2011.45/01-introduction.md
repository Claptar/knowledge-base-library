---
title: Introduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

2011 Panhellenic Conference on Informatics

# **The Effects of Dimensionality Curse in High Dimensional kNN Search**

Nikolaos Kouiroukidis, Georgios Evangelidis _Department of Applied Informatics University of Macedonia Thessaloniki, Greece Email: {kouiruki, gevan}@uom.gr_

**_Abstract_ —The dimensionality curse phenomenon states that in high dimensional spaces distances between nearest and farthest points from query points become almost equal. Therefore, nearest neighbor calculations cannot discriminate candidate points. Many indexing methods that try to cope with the dimensionality curse in high dimensional spaces have been proposed, but, usually these methods end up behaving like the sequential scan over the database in terms of accessed pages when queries like k-Nearest Neighbors are examined. In this paper, we experiment with state of the art multi-attribute indexing methods and try to investigate when these methods reach their limits, namely, at what dimensionality a kNN query requires visiting all the data pages. In our experiments we compare the Hybrid Tree, the R*-tree, and, the iDistance Method.**

**_Keywords_ -high dimensional point indexing; index performance comparison; kNN search**

the papers that introduce new multi-attribute indexes do not present any experimental results in high dimensions.

The rest of this paper is organized as follows: Section II briefly describes some popular multidimensional indexes, and, Section III discusses the k-Nearest Neighbor problem in high dimensional spaces. Section IV illustrates the dimensionality curse phenomenon, whereas Section V contains experimental results on k-NN searching in high dimensions with various indexes. Finally, Section VI concludes the paper.

II. REVIEW OF POPULAR MULTIDIMENSIONAL INDEXES

We briefly introduce some of the most promising indexing methods that have been proposed in the literature.

---

[Up: contents](index.md) · [A. Hybrid Tree →](02-a-hybrid-tree.md)
