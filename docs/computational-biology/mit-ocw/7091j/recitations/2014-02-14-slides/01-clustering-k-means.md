---
title: Clustering – K-means
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Clustering – K-means

Courtesy of an MIT Teaching Assistant.

---

## Reminders

- Pset 1 posted – due Feb $20^{\text{th}}$ (no extra problem)
- Pset 2 posted – due Mar $13^{\text{th}}$
- Project teams due – Feb $25^{\text{th}}$
  - Interests and background directory has been posted
- Lecture videos will be posted on MITx soon – next week?

---

## Today

- Clustering (6.874 topic)
- Biology review
- Alignment

---

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Gkountela, Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." *Nature Cell Biology* 15, no. 1 (2013): 113-22.

---

- Group points together based on how 'close' they are to each other
- Dataset of unlabelled points: $X = \{x_1, x_2, \dots, x_N\}$, $x_n \in \mathbb{R}^d$
- Assume K clusters – each is defined by a centroid $\mu_k$
- $r_{nk} = 1$ if $x_n$ belongs to cluster k
- Find unknowns $\mu_k$ and $r_{nk}$

$$J = \sum_{n=1}^N \sum_{k=1}^K r_{nk} \|x_n - \mu_k\|^2$$

---

### Algorithm 10.1 *K-Means Clustering*

1. Randomly assign a number, from 1 to $K$, to each of the observations. These serve as initial cluster assignments for the observations.
2. Iterate until the cluster assignments stop changing:
   (a) For each of the $K$ clusters, compute the cluster *centroid*. The $k$th cluster centroid is the vector of the $p$ feature means for the observations in the $k$th cluster.
   (b) Assign each observation to the cluster whose centroid is closest (where *closest* is defined using Euclidean distance).

© Springer-Verlag. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Hastie, Trevor, Robert Tibshirani, et al. *The Elements of Statistical Learning*. Springer-Verlag 2, no. 1, 2009.

---

(a)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(b)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(c)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(d)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(e)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(f)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(g)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(h)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

(i)

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

### Table 1 Gene expression similarity measures

| | |
| :--- | :--- |
| Manhattan distance
(city-block distance, L1 norm) | $d_{fg} = \sum_c |e_{fc} - e_{gc}|$ |
| Euclidean distance
(L2 norm) | $d_{fg} = \sqrt{\sum_c (e_{fc} - e_{gc})^2}$ |
| Mahalanobis distance | $d_{fg} = (\mathbf{e}_f - \mathbf{e}_g)' \mathbf{\Sigma}^{-1} (\mathbf{e}_f - \mathbf{e}_g)$, where $\mathbf{\Sigma}$ is the (full or within-cluster) covariance matrix of the data |
| Pearson correlation
(centered correlation) | $d_{fg} = 1 - r_{fg}$, with $r_{fg} = \frac{\sum_c (e_{fc} - \bar{e}_f)(e_{gc} - \bar{e}_g)}{\sqrt{\sum_c (e_{fc} - \bar{e}_f)^2 \sum_c (e_{gc} - \bar{e}_g)^2}}$ |
| Uncentered correlation
(angular separation, cosine angle) | $d_{fg} = 1 - r_{fg}$, with $r_{fg} = \frac{\sum_c e_{fc} e_{gc}}{\sqrt{\sum_c e_{fc}^2 \sum_c e_{gc}^2}}$ |
| Spearman rank correlation | As Pearson correlation, but replace $e_{gc}$ with the rank of $e_{gc}$ within the expression values of gene $g$ across all conditions $c = 1 \dots C$ |
| Absolute or squared correlation | $d_{fg} = 1 - |r_{fg}|$ or $d_{fg} = 1 - r_{fg}^2$ |

$d_{fg}$, distance between expression patterns for genes $f$ and $g$; $e_{gc}$, expression level of gene $g$ under condition $c$.

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: D'haeseleer, Patrik. "How Does Gene Expression Clustering Work?." *Nature Biotechnology* 23, no. 12 (2005): 1499-1502.
doi:10.1038/nbt1205-1499

---

## Hierarchical clustering

- Organize data in a tree
  - Leaves are individual genes/species
  - Path lengths between leaves are distances
  - Similar points should lie in same lower subtrees
- Used to reveal evolutionary history of sequences

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

---

---

[Up: contents](index.md) · [Hierarchical clustering →](02-hierarchical-clustering.md)
