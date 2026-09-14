---
title: I. INTRODUCTION
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# I. INTRODUCTION

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In many modern applications, like image and video content indexing and retrieval or time series data mining, similarity search plays an important role. Images, for example, are transformed into high dimensional feature vectors (points) that describe their most interesting features. Then, multi-dimensional indexes can be used to index these vectors and answer similarity queries ([1], [2]). A similarity query, or kNN query, searches for all the points that are “close” to a given query point. kNN queries are a special case of range queries, where, given a query region the index locates all points contained in it. Since those indexes are external memory structures, there have been developed sophisticated and efficient searching algorithms in terms of both time and accessed pages to answer such queries. But, unfortunately, all these indexes are affected by the dimensionality curse problem. According to this problem, above a certain dimensionality, searching for the answer points becomes inefficient because it costs the same as a plain sequential scan of the entire dataset ([3], [4]).

In this paper, we explore the degree that the dimensionality curse problem affects various well known and established indexes. We are interested in determining which indexes are better suited for kNN queries when k varies. Also, we are interested in testing the resistance of the indexes as the dimensionality increases. According to the literature, all indexes suffer above 10 dimensions [5], but unfortunately,

This multidimensional indexing structure combines the advantages of space-based and data-based partitioning methods. It is very similar to space partitioning methods (like the kDB-tree [6] and the hB-tree [7]) in that its index nodes use kd-trees, instead of arrays of bounding rectangles, to compactly and efficiently represent space partitioning. It always splits nodes using a single attribute (1-d splitting), but contrary to space partitioning methods, it allows overlapping subspaces (bounding rectangles) the way data partitioning methods do (like the R*-tree) and it avoids cascading node splits (like the KDB-tree).

In addition to the usual metric distance functions like the _𝐿𝑝_ Norms, one can employ different distance functions when range and kNN queries must be implemented [8].

---

[← A. Hybrid Tree](02-a-hybrid-tree.md) · [Up: contents](index.md) · [B. R-tree →](04-b-r-tree.md)
