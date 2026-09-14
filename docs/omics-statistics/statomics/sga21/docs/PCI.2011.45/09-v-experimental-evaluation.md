---
title: V. EXPERIMENTAL EVALUATION
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# V. EXPERIMENTAL EVALUATION

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The implementations of the three indexes we tested are available on the web. Since we were interested in testing kNN performance only, we fixed certain parameters in our experiments. We chose to insert 100K uniformly distributed points and we varied the dimensionality from 2 to 24. We also chose a fixed page size of 4KB for all indexes. In some cases we had to modify the original code in order to collect the required statistics. For example, in the case of iDistance,

43


Figure 1. 1NN performance

we chose 64 reference points and we also added counters to compute the size of the B+-tree and the number of retrieved nodes during the queries. The experiments were conducted on a plain Pentium IV computer with 512MB of RAM and a 120GB hard disk running Debian GNU/Linux.

We present the results of our experiments for _𝑘_ = 1, _𝑘_ = 5 and _𝑘_ = 10. In all cases, we plot the ratio of visited data nodes over the total number of data nodes versus the dimensionality when answering the respective kNN queries. For _𝑘_ = 1, the Hybrid Tree outperforms all indexes since by design it minimizes node overlapping (Figure 1). For _𝑘_ = 5 and _𝑘_ = 10 we obtain similar results, with the R*-tree slightly outperforming the Hybrid tree in higher dimensions. The iDistance is always worse that the other two indexes in low to medium dimenions, but it achieves similar performance above 20 dimensions. This is attributed to the fact that the iDistance was designed to perform well in high dimensions. The iDistance is always better than sequential scan albeit by only 5%–10% in high dimensions [10] (Figures 2 and 3).

Finally, we confirm the findings of previous researchers and we observe that the “dimensionality curse” phenomenon renders all indexes unusable in medium dimensionality. The performance of all indexes deteriorates rapidly above eight dimensions. More specifically, all indexes have to visit almost all data pages in order to answer a 24NN query.

Figure 2. 5NN performance


Figure 3. 10NN performance

chosen indexing method. This is attributed to the fact that in high dimensions there is little discrimination between the nearest and the farthest points from a given query point. A solution to this problem is the design of new distance functions that fit the needs of modern applications ([21], [20]) and the development of new indexes that exploit the new distance functions.

---

[← IV. DIMENSIONALITY CURSE](08-iv-dimensionality-curse.md) · [Up: contents](index.md) · [VI. CONCLUSIONS →](10-vi-conclusions.md)
