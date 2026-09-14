---
title: Hierarchcial clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hierarchcial clustering

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Two types of approaches:

•Agglomerative •Divisive

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

45

## Agglomerative Clustering Algorithm

- Initialize: Each data point is in its own cluster

- Repeat until there is only one cluster:

   - Merge the two most similar clusters.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

46

## Agglomerative Clustering Algorithm

• Initialize: Each data point is in its own cluster • Repeat until there is only one cluster:

– Merge the two most similar clusters.

If distance is defined for a vector, how do I compare clusters?


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

47

- Clusters Y, Z with A in Y and B in Z

- Single linkage = min{dA,B}

- Complete linkage = max{dA,B}

- UPGMC (Unweighted Pair Group Method using **Centroids**


<!-- Start of picture text -->
Z<br>B<br>Y<br>A<br><!-- End of picture text -->

- Define  distance as


- UPGMA (Unweighted Pair Group Method with Arithmetic **Mean** ) average of pairwise distances:


48

• Single linkage = min{dA,B} • Complete linkage = max{dA,B}


49

- If clusters exist and are compact, it should not matter.

- Single linkage will “chain” together groups with one intermediate point.

- Complete linkage will not combine two groups if even one point is distant.

50

### Interpreting the Dendogram

- This produces a binary tree or **_dendrogram_**

- The final cluster is the root and each data item is a leaf

- The heights of the bars indicate how close the items are

- Can ‘slice’ the tree at any distance cutoff to produce discrete clusters

- Dendogram represents the results of the **<u>clustering</u>** <u>; its</u> usefulness in representing the **<u>data</u>** is mixed.

Data items (genes, etc.)

-

- The results will always be hierarchical, even if the data are not.

51

K-means clustering • Advantage:  gives sharp partitions of the data • Disadvantage:  need to specify the number of clusters (K).

• Goal:  find a set of k clusters that minimizes the distances of each point in the cluster to the cluster mean:


52

K-means clustering algorithm • Initialize: choose k points as cluster means • Repeat until convergence:

- Assignment:  place each point Xi in the cluster with the closest mean.

- Update: recalculate the mean for each cluster


53


54

55

56

---

[← Unsupervised Learning](25-unsupervised-learning.md) · [Up: contents](index.md) · [What if you choose the wrong K? →](27-what-if-you-choose-the-wrong-k.md)
