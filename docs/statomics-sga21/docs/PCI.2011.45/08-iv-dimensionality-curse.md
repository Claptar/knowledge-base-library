---
title: IV. DIMENSIONALITY CURSE
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# IV. DIMENSIONALITY CURSE

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The dimensionality curse in applied mathematics refers to the problem caused by the exponential increase in volume associated with adding extra dimensions to a mathematical space ([3], [4], [16]). For example, consider a unit 1-dimensional interval with 100 evenly-spaced sample points, i.e., each point is 0.01 distance units away from its neighbors. An equivalent sampling of a 10-dimensional unit hypercube with a lattice with a spacing of 0.01 between adjacent points would require 10<sup>20</sup> sample points: thus, in some sense, the 10-dimensional unit hypercube can be said to be a factor of 10<sup>18</sup> “larger” than the unit 1-dimensional interval. Another way to illustrate the “vastness” of highdimensional Euclidean space is to compare the proportion of a hypersphere with radius _𝑟_ and dimension _𝑑_ , to that of a hypercube with sides of length 2 _𝑟_ , and equivalent dimension. The volume of such a sphere is:


The volume of the cube would be: (2 _𝑟_ )<sup>_𝑑_</sup> .

42

As the dimensionality _𝑑_ increases, the hypersphere’s volume becomes insignificant relative to that of the hypercube. This can clearly be seen by computing their ratio as the dimension _𝑑_ goes to infinity:


where Γ is the Gamma function: Γ( _𝑛_ ) = ( _𝑛−_ 1)!, _𝑑 →∞_ . Thus, in some sense, nearly all of the high-dimensional space is “far away” from the centre, or, to put it another way, the high-dimensional unit space can be said to consist almost entirely of the “corners” of the hypercube, with almost no “middle”.

The curse of dimensionality can also be considered from another perspective [17]. In high dimensional space, most of the volume is close to the surface of the data space, as shown in the following example. Let us have the _𝑑_ -dimensional unit hypercube. In order to consider the region close to the surface, let us assume we only consider the locus of points with distance _≤_ 0 _._ 05 from the surface. This defines a hollow cube with a volume _𝑉_ = 1 _−_ (1 _−_ 2 _×_ 0 _._ 05)<sup>_𝑑_</sup> . For _𝑑_ = 3, _𝑉_ = 1 _−_ 0 _._ 9<sup>3</sup> = 0 _._ 27, for _𝑑_ = 10, _𝑉_ = 1 _−_ 0 _._ 9<sup>10</sup> = 0 _._ 65, and, for _𝑑_ = 15, _𝑉_ = 1 _−_ 0 _._ 9<sup>15</sup> = 0 _._ 79. Actually, in any size and any shape of data space, the above property is satisfied. Because of this property, if data objects are uniformly distributed in space, progressively more of them will be close to the surfaces of the data spaces when the number of dimensions increases. Let the center of the cube be the query object. We can see that the above property causes two effects on the nearest neighbor search. First, if the number of objects is fixed, the average distance of the nearest neighbor will be increased as the dimension increases. Second, the distances of all objects from the center are becoming more and more similar when the number of dimensions increases.

In the multidimensional indexing data literature, dimensionality curse also appears as “the concentration of measure” or “the effect on distance functions” ([18], [19]).

Given a single distribution, the minimum and the maximum occurring distances have been shown to become indiscernible, since the ratio of the difference of the minimum and maximum values and the minimum value converges to 0:


This is often cited as “distance functions losing their usefulness in high dimensionality”. However, recent research indicates that the mere number of dimensions is not the problem, since relevant additional dimensions can also increase the contrast. In addition, the resulting ranking remains useful in discerning close and far neighbors. However, irrelevant (“noise”) dimensions reduce the contrast, as expected.

The dimensionality curse in high dimensional indexing methods is related to what we call _𝐿𝑝_ norm. The definition of _𝐿𝑝_ norm is:


The _𝐿_ 2 norm, or Euclidean distance metric, is the most commonly used metric, while the _𝐿_ 1 norm is the Manhattan distance metric. Distance functions that rely on these norms in metric spaces have the following three common properties. The distance functions are defined as _𝑑_ : _𝑈 × 𝑈 → 𝑅_<sup>+</sup> , where _𝑈_ is the universe of the objects.


These three properties are valid for many reasonable similarity functions. Recent research shows that, in high dimensional spaces, the validity of the _𝐿𝑝_ norm in measuring the similarity between data points is sensitive to the value of _𝑝_ . For example, the Manhattan distance metric ( _𝐿_ 1 norm) is consistently more preferable than the Euclidean distance metric ( _𝐿_ 2 norm) for high dimensional data mining applications ([16], [20]). Furthermore, a natural extension of the _𝐿𝑝_ norm to fractional distance metrics is introduced and examined from both the theoretical and empirical perspectives. The fractional distance metric is defined in the same manner with the exception that _𝑝_ belongs to (0 _,_ 1).

From the theoretical perspective, fractional distance metrics provide better divergence between the maximum and minimum distances to a given query point than integral distance metrics. This feature makes a proximity query more meaningful and stable. Empirical studies also demonstrate that fractional distance metrics can significantly improve the effectiveness of some standard classification and clustering algorithms such as kNN and k-means on high dimensional datasets. In the meantime, fractional distance measures have been applied to content-based image retrieval and the experiments also show that retrieval performances of these measures consistently outperform the Manhattan and Euclidean distance metrics when used with a wide range of high-dimensional visual features.

In the following section, we demonstrate how some of the most promising multidimensional indexing structures behave in high dimensionality, and, especially, in what dimension given a specific dataset size, kNN searches access as many data pages as a plain sequential scan.

---

[← III. K-NEAREST NEIGHBOR QUERIES](07-iii-k-nearest-neighbor-queries.md) · [Up: contents](index.md) · [V. EXPERIMENTAL EVALUATION →](09-v-experimental-evaluation.md)
