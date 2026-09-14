---
title: III. K-NEAREST NEIGHBOR QUERIES
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# III. K-NEAREST NEIGHBOR QUERIES

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a set _𝑃_ of points in a high dimensional space and a query point _𝑞_ , find the _𝑘_ points in _𝑃_ closest to _𝑞_ . This is the k-nearest neighbor search problem. It has significant importance to several areas of computer science, like in searching in multimedia data, pattern recognition, and, data mining in general. These applications involve very large data sets and the dimensionality of the data set is usually high as well. Multidimensional point indexes can be used to speed up searching is such data sets. Thus, it is very important to design algorithms that scale well with the database size as well as with the dimensionality of the data.

The nearest neighbor problem ([11], [12], [5]) is an example of a large class of proximity problems whose definition involves the notion of distance between the input points like the closest pair problem. Many of these problems have been firstly investigated in the field of computational geometry, for example, when the points lie in a space of constant dimension. The nearest neighbor problem of this kind can be solved in _𝑂_ ( _𝑙𝑜𝑔𝑁_ ) time per query using _𝑂_ ( _𝑁_ ) storage. Unfortunately, as the dimensionality grows the complexity of any index converges to _𝑂_ ( _𝑁_ ), that is, all points must be accessed in order to evaluate a NN-query [5].

The exponential dependence of space or time on the dimensionality, called the “dimensionality curse”, has been observed in many application settings. The lack of success in removing the exponential dependence on the dimensionality

led many researchers to deduce that no efficient solution exists for these problems when the dimensionality is sufficiently large. But, as many researchers showed, in many cases this exponential dependence on the dimensionality can be reduced to polynomial if we allow the answers to be approximate.

This notion of approximation is best explained as follows: instead of reporting a point _𝑝_ closest to _𝑞_ , the algorithm is allowed to report any point within distance (1+ _𝜀_ ) times the distance from _𝑞_ to _𝑝_ . This is similar to designing efficient approximation algorithms for NP-hard problems.

There are two main algorithms that calculate the nearest neighbor points to a given point in multidimensional spaces using indexing structures like the R*-tree and its variants, the SR-tree [13], the Hybrid tree [8], and many more.

The first one is the Branch and Bound algorithm proposed by Rousopoulos et al [14] that uses the MINDIST and MINMAXDIST metrics to put points for visiting and examination in an order and to determine the nodes that will not be further considered for examination (pruning). Node pruning is accomplished through the use of heuristic methods. A depth first search is implemented so that when the current search path cannot obtain all the nearest neighbors, backtracking is used to examine a neighboring path.

Hjaltason and Samet [15] proposed the second major algorithm for nearest neighbor searching with its incremental form applied to R-trees. Candidate objects are found with an order that is determined from their distance to the query point, thus, they are ranked. This process is called distance browsing. Also, this incremental algorithm differs from the classic kNN in the sense that the number of k nearest neighbors is not known in advance.

---

[← PCI.2011.45 Part 06 —](06-pci-2011-45-part-06.md) · [Up: contents](index.md) · [IV. DIMENSIONALITY CURSE →](08-iv-dimensionality-curse.md)
