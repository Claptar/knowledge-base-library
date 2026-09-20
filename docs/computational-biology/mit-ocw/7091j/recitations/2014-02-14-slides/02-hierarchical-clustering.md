---
title: Hierarchical clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Hierarchical clustering

- What dissimilarity measure should be used?
  - To compare individual points
- What type of linkage should be used?
  - To compare clusters with each other
- Where do we cut dendrogram to obtain clusters?

---

### Algorithm 10.2 *Hierarchical Clustering*

1. Begin with $n$ observations and a measure (such as Euclidean distance) of all the $\binom{n}{2} = n(n - 1)/2$ pairwise dissimilarities. Treat each observation as its own cluster.
2. For $i = n, n - 1, \dots, 2$:
   (a) Examine all pairwise inter-cluster dissimilarities among the $i$ clusters and identify the pair of clusters that are least dissimilar (that is, most similar). Fuse these two clusters. The dissimilarity between these two clusters indicates the height in the dendrogram at which the fusion should be placed.
   (b) Compute the new pairwise inter-cluster dissimilarities among the $i - 1$ remaining clusters.

© Springer-Verlag. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Hastie, Trevor, Robert Tibshirani, et al. *The Elements of Statistical Learning*. Springer-Verlag 2, no. 1, 2009.

---

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

| Linkage | Formula | Description |
| :--- | :--- | :--- |
| Complete | $d(A, B) = \max_{x \in A, y \in B} d(x, y)$ | Maximal intercluster dissimilarity |
| Single | $d(A, B) = \min_{x \in A, y \in B} d(x, y)$ | Minimal intercluster dissimilarity |
| Average | $d(A, B) = \sum_{x \in A, y \in B} \frac{d(x, y)}{\|A\|\|B\|}$ | Average intercluster dissimilarity (UPGMA) |
| Centroid | $d(A, B) = d\left(\sum_{x \in A} \frac{x}{\|A\|}, \sum_{y \in B} \frac{y}{\|B\|}\right)$ | Dissimilarity between centroids of each cluster |

---

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Model selection

- Hierarchical clustering – cutoff tree at certain point
- K-means – how to choose K?
  - Balance number of clusters (# of parameters – K=n is uninformative) and the variance of the clusters
- BIC Score – general model selection criterion
- $\text{BIC} = -2 \times \text{loglikelihood} + d \times \log(N)$
- Can use to decide whether to split a cluster
- Compute BIC score of cluster and two potential child clusters – if BIC score is lower after split, do not accept split

---

---

[← Clustering – K-means](01-clustering-k-means.md) · [Up: contents](index.md) · [Biclustering →](03-biclustering.md)
