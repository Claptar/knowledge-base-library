---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6.874/… Recitation 2

Courtesy of an MIT Teaching Assistant.

1

## Reminders

- Pset 1 posted – due Feb 20<sup>th</sup> (no extra problem)

- Pset 2 posted – due Mar 13<sup>th</sup>

- Project teams due – Feb 25<sup>th</sup>

   - Interests and background directory has been posted

- Lecture videos will be posted on MITx soon – next week?

2

## Today

- Clustering (6.874 topic)

- Biology review

- Alignment

3

4


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Gkountela, Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." _Nature Cell Biology_ 15, no. 1 (2013): 113-22.

## Clustering – K-means

- Group points together based on how ‘close’ they are to each other

- Dataset of unlabelled points: 𝑋= 𝑥1, 𝑥2, … , 𝑥𝑁 , 𝑥𝑛 ∈𝑅<sup>𝑑</sup>

- Assume K clusters – each is defined by a centroid 𝜇𝑘

- 𝑟𝑛𝑘 = 1 if 𝑥𝑛 belongs to cluster k

- Find unknowns 𝜇𝑘 and 𝑟𝑛𝑘


5

6


© Springer-Verlag. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Hastie, Trevor, Robert Tibshirani, et al. The Elements of Statistical Learning. _Springer-Verlag_ 2, no. 1, 2009.


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

7

8

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

9

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

10

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

11

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

12

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

13

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

14

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

15

© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

16


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


Courtesy of Macmillan Publishers Limited. Used with permission. Source: D'haeseleer, Patrik. "How Does Gene Expression Clustering Work?." _Nature Biotechnology_ 23, no. 12 (2005): 1499-1502.


17

## Hierarchical clustering

- Organize data in a tree

   - Leaves are individual genes/species

   - Path lengths between leaves are distances

   - Similar points should lie in same lower subtrees

- Used to reveal evolutionary history of sequences


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

18


19

## Hierarchical clustering

- What dissimilarity measure should be used?

   - To compare individual points

- What type of linkage should be used?

   - To compare clusters with each other

- Where do we cut dendrogram to obtain clusters?

20


© Springer-Verlag. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Hastie, Trevor, Robert Tibshirani, et al. The Elements of Statistical Learning. _Springer-Verlag_ 2, no. 1, 2009.

21

22


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


<!-- Start of picture text -->
𝑑 max Maximal intercluster<br>𝐴, 𝐵=<br>Complete<br>𝑥∈𝐴,𝑦∈𝐵 𝑑(𝑥, 𝑦)<br>dissimilarity<br>Minimal intercluster<br>𝑑 𝐴, 𝐵= min<br>Single<br>𝑥∈𝐴,𝑦∈𝐵 𝑑(𝑥, 𝑦)<br>dissimilarity<br>𝑑(𝑥, 𝑦) Average intercluster<br>Average 𝑑 𝐴, 𝐵= dissimilarity<br>𝐴 𝐵<br>(UPGMA)<br>𝑥∈𝐴,𝑦∈𝐵<br>𝑑 𝐴, 𝐵 Dissimilarity between<br>𝑥 𝑦 centroids of each<br>Centroid<br>𝑥∈𝐴<br>𝐵 cluster<br>𝐴 , 𝑦∈𝐵<br>= 𝑑<br><!-- End of picture text -->

23


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

24

## Model selection

- Hierarchical clustering – cutoff tree at certain point

- K-means – how to choose K?

   - Balance number of clusters (# of parameters – K=n is uninformative) and the variance of the clusters

   - BIC Score – general model selection criterion

   - BIC = −2 × loglikelihood + d × log(N)

   - Can use to decide whether to split a cluster

   - Computer BIC score of cluster and two potential child clusters – if BIC score is lower after split, do not accept split

25

## Biclustering

- Simultaneous clustering of rows and columns of a matrix

- Bicluster – subset of rows which exhibit similar behavior across a subset of columns, or vice versa

26


© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Madeira, Sara C., and Arlindo L. Oliveira. "Biclustering Algorithms for Biological Data Analysis: A Survey." _Computational Biology and Bioinformatics_ , IEEE/ACM Transactions on 1, no. 1 (2004): 24-45.

27

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Gkountela, Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." _Nature Cell Biology_ 15, no. 1 (2013): 113-22.

28

---

[Up: contents](index.md) · [Biology Review →](02-biology-review.md)
