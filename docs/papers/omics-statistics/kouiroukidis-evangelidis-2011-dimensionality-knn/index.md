---
title: "Kouiroukidis & Evangelidis 2011 — The Effects of Dimensionality Curse in High Dimensional kNN Search"
paper: "summary"
source: "https://doi.org/10.1109/PCI.2011.45"
licence: "© IEEE — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Nikolaos Kouiroukidis and Georgios Evangelidis, "The Effects of Dimensionality Curse in High Dimensional kNN Search," in 2011 Panhellenic Conference on Informatics (PCI), Thessaloniki, Greece, 2011, pp. 41-45. ([original](https://doi.org/10.1109/PCI.2011.45)). Rights: © IEEE — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# The Effects of Dimensionality Curse in High Dimensional kNN Search

## What this covers
This paper is an experimental database-systems study of how the "curse of dimensionality"
degrades k-nearest-neighbour (kNN) search using tree-based multidimensional indexes, speaking to
the similarity-search and multimedia-indexing literature.

## The question
Multidimensional indexes such as R-trees and related structures are built to answer kNN queries
faster than scanning an entire dataset, but it has long been observed that beyond some
dimensionality they stop helping and end up costing about as much as a sequential scan. The
literature commonly states that indexes "suffer above 10 dimensions," yet papers that introduce new
indexing methods rarely test this directly. The authors set out to measure, for several
established indexes, at what dimensionality (and for which $k$) a kNN query degrades to visiting
essentially the whole dataset, rather than relying on that received rule of thumb.

## The approach
They compare three indexing methods representative of different design families: the Hybrid Tree
(space-partitioning, with kd-tree-style node splits), the R*-tree (the established data-partitioning,
minimum-bounding-rectangle structure), and iDistance (which maps each high-dimensional point to a
single value based on its distance to a nearest reference point, then indexes that value with a
B+-tree). Using existing public implementations, they inserted 100,000 uniformly distributed points
into each index, varied dimensionality from 2 to 24, fixed a 4KB page size, and measured the
fraction of data pages visited when answering kNN queries for $k=1$, $k=5$ and $k=10$. The ratio of
visited pages to total pages is their single cost measure: as it approaches 1, the index offers no
advantage over a full scan.

## What it found
All three indexes show a sharply increasing visited-page ratio as dimensionality rises, consistent
with the dimensionality curse. For $k=1$, the Hybrid Tree stays efficient far longer than the other
two, because its design minimises node overlap. For $k=5$ and $k=10$ that advantage largely
disappears, with the R*-tree slightly outperforming the Hybrid Tree at higher dimensions. iDistance
is consistently worse than the other two at low-to-medium dimensionality but closes the gap above
roughly 20 dimensions, matching its stated design goal of favouring high-dimensional performance;
even there it beats sequential scan by only about 5-10%. Across all three methods and all tested
$k$, performance deteriorates rapidly above about eight dimensions, and by 24 dimensions a kNN query
visits almost all data pages regardless of the indexing method used. The authors attribute this to
the loss of discrimination between near and far points at high dimensionality — the concentration of
distances.

## Limits and context
This is an empirical comparison, not a proposal of a new method: no new index or distance function
is introduced. The results are limited to the three structures tested, to uniformly distributed
synthetic data, to a single dataset size (100K points) and page size (4KB), and to dimensionalities
up to 24, so the paper does not establish behaviour under other data distributions, other scales, or
higher dimensions. The authors also qualify the usual story that "distance functions lose meaning"
above some dimension: citing other work, they note the degradation is driven specifically by
irrelevant ("noise") dimensions rather than by dimensionality as such, since relevant additional
dimensions can increase rather than reduce discriminative contrast, and that fractional ($L_p$ with
$p<1$) and Manhattan ($L_1$) distance metrics have been shown to behave better than Euclidean
distance in high dimensions. They conclude that a real remedy needs new distance functions suited to
high-dimensional data together with indexes built around them, rather than further tuning of
page-access tree structures — the three indexes tested are presented as close to a ceiling on what
that approach can achieve, not as an unfinished design.

## Citation
Nikolaos Kouiroukidis and Georgios Evangelidis, "The Effects of Dimensionality Curse in High
Dimensional kNN Search," in *2011 Panhellenic Conference on Informatics (PCI)*, Thessaloniki,
Greece, 2011, pp. 41-45. DOI: [10.1109/PCI.2011.45](https://doi.org/10.1109/PCI.2011.45). Available
via IEEE Xplore at the DOI link above.
