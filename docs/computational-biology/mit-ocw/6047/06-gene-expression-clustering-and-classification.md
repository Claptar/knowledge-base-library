---
title: "6. Gene Expression Clustering and Classification"
course: "MIT 6047"
chapter: 6
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Gene Expression Clustering and Classification

## What this covers

A gene-expression experiment produces a matrix of genes against conditions, and there are two
different questions to ask of it: find structure with no labels (**clustering**), or use labels
you already have to assign new points (**classification**). This chapter builds the two workhorse
clustering methods — k-means and hierarchical clustering — shows that k-means is a special case of
fitting a Gaussian mixture model by maximum likelihood, gives the distance measures the methods
run on, and covers how a clustering is checked against outside evidence. It closes with the setup
for classification: the generative/discriminative split and Bayes' rule for a single feature. It
assumes familiarity with basic probability (conditional probability, Bayes' rule) and with the idea
of a likelihood function, but no prior exposure to clustering algorithms.

## The expression matrix, and two questions about it

A microarray or an RNA-seq experiment measures the expression of thousands of genes (the "spots")
in each of some number of conditions. Stacking many experiments gives a matrix with $m$ genes as
rows and $n$ conditions as columns. (Microarrays and RNA-seq differ in how that number is produced —
hybridization to a probe versus counting mapped reads, either against known genes or against a
transcriptome reconstructed *de novo* from the reads — but they hand downstream analysis the same
kind of matrix.)

Once you have the matrix, two different questions are possible:

- **Clustering (unsupervised):** group genes with genes, or conditions with conditions, by
  similarity, with no prior labels — e.g. discovering that a set of genes is co-expressed in a
  panel of cell lines. The goal is to find hidden structure; correctness is checked afterwards,
  against evidence that was not used to build the clusters.
- **Classification (supervised):** you already have labels for some points — pan-B-cell,
  germinal-centre B-cell, T-cell, activated B-cell, proliferation, lymph node, say — and you want a
  rule that assigns the label correctly to points you have not seen. Correctness here has a direct
  meaning, classification accuracy on held-out points.

Clustering has a further split by *how* points are grouped:

- **Partitioning** (e.g. k-means): divide the objects into non-overlapping subsets, each object in
  exactly one cluster.
- **Agglomerative** (e.g. hierarchical clustering): build a nested hierarchy of clusters, i.e. a
  tree, rather than a single flat partition.

## K-means: clustering by partitioning

Fix the number of clusters $K$ in advance and look for $K$ compact groups. The algorithm alternates
two steps until nothing changes:

1. Initialize $K$ cluster centers $\mu_1, \dots, \mu_K$ at random.
2. Repeat:
   - **Assign** each point to the nearest center.
   - **Update** each center to the centroid (mean) of the points now assigned to it.
3. Stop when no point changes its assignment.

In symbols, the assignment step gives point $\mathbf{x}_i$ the label $k$ minimizing squared distance
to the center,
$$d_{i,k} = (\mathbf{x}_i - \boldsymbol{\mu}_k)^2,$$
and the update step recomputes
$$\boldsymbol{\mu}_k^{(n+1)} = \sum_{\mathbf{x}_i \text{ with label } k} \frac{\mathbf{x}_i}{|\mathbf{x}^k|},
\qquad |\mathbf{x}^k| = \#\{\mathbf{x}_i \text{ with label } k\}.$$

### Why the centroid is the right update

K-means can be read as minimizing a single cost function, the total squared distance from every
point to its own cluster's center:
$$\mathrm{COST} = \sum_k \sum_{\mathbf{x}_i \text{ with label } k} (\mathbf{x}_i - \boldsymbol{\mu}_k)^2.$$
Because the clusters don't interact in this sum, it can be minimized one term at a time. Expanding
the square inside a single cluster,
$$\sum_{\mathbf{x}_i \text{ with label } k} (\mathbf{x}_i - \boldsymbol{\mu}_k)^2
= \sum_i \mathbf{x}_i^2 - 2\boldsymbol{\mu}_k \sum_i \mathbf{x}_i + |\mathbf{x}^k|\,\boldsymbol{\mu}_k^2,$$
which, as a function of $\boldsymbol{\mu}_k$ alone, is a quadratic that opens upward. Its minimum is
where the derivative vanishes, $-2\sum_i \mathbf{x}_i + 2|\mathbf{x}^k|\boldsymbol{\mu}_k = 0$, i.e.
$$\boldsymbol{\mu}_k = \sum_{\mathbf{x}_i \text{ with label } k} \frac{\mathbf{x}_i}{|\mathbf{x}^k|},$$
the centroid. So the update step is not a heuristic — it is exactly the value that minimizes the
cost given the current assignment, and reassigning each point to its nearest center is exactly the
value that minimizes the cost given the current centers. K-means alternates two exact minimizations
of the same cost, which is why the cost never increases and the algorithm converges.

### Fuzzy k-means

A point roughly equidistant from two centers is forced by ordinary k-means into one of them, which
throws away real information. Fuzzy k-means replaces the hard assignment with a probability of
membership in every cluster,
$$P(\text{label } k \mid \mathbf{x}_i, \boldsymbol{\mu}_k),$$
and updates each center to the *weighted* mean of all the points, not just the ones "assigned" to
it:
$$\boldsymbol{\mu}_k^{(n+1)} =
\frac{\sum_i \mathbf{x}_i\, P(\boldsymbol{\mu}_k \mid \mathbf{x}_i)^b}{\sum_i P(\boldsymbol{\mu}_k \mid \mathbf{x}_i)^b}.$$
Ordinary k-means is the special case where the membership probability is forced to $0$ or $1$:
$$P(\text{label } k \mid \mathbf{x}_i, \boldsymbol{\mu}_k) =
\begin{cases} 1 & \mathbf{x}_i \text{ closest to } \boldsymbol{\mu}_k \\ 0 & \text{otherwise.} \end{cases}$$

## K-means as maximum likelihood: the EM view

K-means can also be derived, rather than assumed, by treating the data as generated from a model
and asking for the maximum-likelihood parameters of that model. The generative story is a
**Gaussian mixture model**: each point is drawn from one of $K$ unit-variance normal distributions,
$$P(\mathbf{x}_i \mid \boldsymbol{\mu}_j) = \frac{1}{\sqrt{2\pi}}
\exp\left\{-\frac{(\mathbf{x}_i - \boldsymbol{\mu}_j)^2}{2}\right\}.$$
Given only the samples, two things are unknown at once: the centroids and which point came from
which component. Neither is easy to get without the other — but each is easy *given* the other, and
that is what **Expectation-Maximization (EM)** exploits: hold one fixed, solve exactly for the
other, then swap.

- **M step** (assignments known $\to$ maximize over centers). Choosing $\boldsymbol{\mu}$ to
  maximize the log-likelihood of the labeled points,
  $$\arg\max_{\boldsymbol{\mu}} \sum_i \left\{-\tfrac12(\mathbf{x}_i - \boldsymbol{\mu})^2 +
  \log\tfrac{1}{\sqrt{2\pi}}\right\} = \arg\min_{\boldsymbol{\mu}} \sum_i (\mathbf{x}_i - \boldsymbol{\mu})^2,$$
  is exactly the least-squares problem solved above — the maximum-likelihood center is the
  centroid.
- **E step** (centers known $\to$ maximize over labels). Choosing the label $k$ that makes a given
  point most likely,
  $$\arg\max_k \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{(\mathbf{x}_i - \boldsymbol{\mu}_k)^2}{2}\right)
  = \arg\min_k (\mathbf{x}_i - \boldsymbol{\mu}_k)^2,$$
  is exactly "assign to the nearest center."

So k-means *is* EM for this particular generative model, with the E step replaced by its
hard-assignment version — pick the single most likely label rather than carry a distribution over
labels. That is also why fuzzy k-means, which keeps $P(\text{label} \mid \mathbf{x}_i)$ instead of
collapsing it, is the more general (soft) form of the same alternation.

<figure>
<svg viewBox="0 0 320 190" role="img" aria-label="EM alternates between fixing the centers and re-estimating labels, then fixing the labels and re-estimating centers">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="30" width="120" height="50" fill="none" stroke="currentColor"/>
  <text x="80" y="60" text-anchor="middle" font-size="12" fill="currentColor">centers known</text>
  <rect x="180" y="120" width="120" height="50" fill="none" stroke="currentColor"/>
  <text x="240" y="150" text-anchor="middle" font-size="12" fill="currentColor">labels known</text>
  <path d="M 140 60 C 200 60, 220 80, 220 118" fill="none" stroke="currentColor" marker-end="url(#arr)"/>
  <text x="215" y="90" font-size="12" fill="currentColor">E</text>
  <path d="M 180 145 C 110 150, 60 130, 65 82" fill="none" stroke="currentColor" marker-end="url(#arr)"/>
  <text x="90" y="150" font-size="12" fill="currentColor">M</text>
  <text x="160" y="20" text-anchor="middle" font-size="12" fill="currentColor">each arrow is an exact minimization of the same cost</text>
</svg>
<figcaption>The E step assigns points to the nearest of the current centers (minimizing cost over
labels); the M step recomputes each center as the centroid of its assigned points (minimizing cost
over centers). k-means is this loop with a hard E step.</figcaption>
</figure>

### The same alternation elsewhere

The lecture frames this three-way choice of assignment rule — pick the single best label, average
over all labels weighted by probability, or sample a label at random according to its probability
— as a pattern that recurs across several algorithms built later in the course, not just k-means:

| Update rule | What the E step does | Expression clustering | HMM learning | Motif discovery |
|---|---|---|---|---|
| Pick a best | assign each point to its single best label | **k-means**: nearest cluster | **Viterbi training**: best state path | **Greedy**: best motif match per sequence |
| Average all | assign each point to all labels, weighted by probability | **Fuzzy k-means**: weighted by proximity | **Baum-Welch**: posterior over all paths | **MEME**: every position weighted by match score |
| Sample one | draw one label at random, with probability proportional to its likelihood | (not used) | (not used) | **Gibbs sampling**: one position sampled from the match scores |

In every row, the M step is the same kind of operation: recompute the model parameters from
whichever version of the labels the E step produced (a hard assignment, a full weighted average, or
a single sample).

## Hierarchical clustering: clustering by agglomeration

K-means has an awkward free parameter: $K$ must be chosen up front, and there is no natural way to
tell whether $K$ or $K+1$ clusters is "right" — compactness only ever improves as $K$ grows, up to
the degenerate case where every point is its own cluster. Hierarchical clustering sidesteps the
question by not fixing $K$ at all.

The algorithm, the one most widely used on expression data:

1. Start with every point in its own cluster.
2. Repeatedly find the two **closest** clusters and merge them.
3. Continue until one cluster remains.

The result is a tree of nested clusters rather than a flat partition — structurally the same object
as a phylogeny, and built the same way when the merge rule is the *unweighted pair group method
with arithmetic mean* (**UPGMA**). A flat clustering is recovered afterwards by choosing a "cut
level" and taking the clusters that exist at that level.

<figure>
<svg viewBox="0 0 370 160" role="img" aria-label="A dendrogram built by repeatedly merging the closest clusters, cut at a chosen height to give a flat clustering">
  <line x1="40" y1="190" x2="40" y2="140" stroke="currentColor"/>
  <line x1="110" y1="190" x2="110" y2="140" stroke="currentColor"/>
  <line x1="40" y1="140" x2="110" y2="140" stroke="currentColor"/>
  <line x1="75" y1="140" x2="75" y2="60" stroke="currentColor"/>
  <line x1="180" y1="190" x2="180" y2="120" stroke="currentColor"/>
  <line x1="250" y1="190" x2="250" y2="120" stroke="currentColor"/>
  <line x1="180" y1="120" x2="250" y2="120" stroke="currentColor"/>
  <line x1="215" y1="120" x2="215" y2="60" stroke="currentColor"/>
  <line x1="75" y1="60" x2="215" y2="60" stroke="currentColor"/>
  <circle cx="40" cy="190" r="3" fill="currentColor"/>
  <circle cx="110" cy="190" r="3" fill="currentColor"/>
  <circle cx="180" cy="190" r="3" fill="currentColor"/>
  <circle cx="250" cy="190" r="3" fill="currentColor"/>
  <line x1="15" y1="100" x2="300" y2="100" stroke="currentColor" stroke-dasharray="4 3"/>
  <text x="310" y="104" font-size="12" fill="currentColor">cut level</text>
  <text x="75" y="55" text-anchor="middle" font-size="12" fill="currentColor" dy="-4"></text>
</svg>
<figcaption>Merging always joins the two closest clusters, from single points up to one tree.
Cutting the tree at the dashed height, before the final merge but after the two pairwise merges,
recovers two disjoint clusters.</figcaption>
</figure>

### Distance between clusters

Every step needs a notion of distance between two *clusters* $X$ and $Y$, built from the
point-to-point distance $D$ between their members. Four common choices, each extending $D$
differently:

- **Single-link:** $\mathrm{CD}(X,Y) = \min_{x \in X,\, y \in Y} D(x,y)$ — distance between the
  closest pair.
- **Complete-link:** $\mathrm{CD}(X,Y) = \max_{x \in X,\, y \in Y} D(x,y)$ — distance between the
  farthest pair.
- **Average-link:** $\mathrm{CD}(X,Y) = \mathrm{avg}_{x \in X,\, y \in Y} D(x,y)$ — average over all
  pairs.
- **Centroid method:** $\mathrm{CD}(X,Y) = D(\mathrm{avg}(X), \mathrm{avg}(Y))$ — distance between
  the two cluster means.

The choice affects both the shape of the resulting clusters and how expensive the algorithm is to
run.

### Distance between points

All four cluster-distance rules are built on top of a point-to-point distance $D$ between two
expression profiles — and that choice is itself a modeling decision. For two genes $f$ and $g$ with
expression $e_{fc}$, $e_{gc}$ across conditions $c$:

| Measure | Formula |
|---|---|
| Manhattan ($L_1$) | $d_{fg} = \sum_c \lvert e_{fc} - e_{gc} \rvert$ |
| Euclidean ($L_2$) | $d_{fg} = \sqrt{\sum_c (e_{fc} - e_{gc})^2}$ |
| Mahalanobis | $d_{fg} = (\mathbf{e}_f - \mathbf{e}_g)' \Sigma^{-1} (\mathbf{e}_f - \mathbf{e}_g)$, $\Sigma$ the (full or within-cluster) covariance of the data |
| Pearson correlation | $d_{fg} = 1 - r_{fg}$, $\; r_{fg} = \dfrac{\sum_c (e_{fc}-\bar e_f)(e_{gc}-\bar e_g)}{\sqrt{\sum_c (e_{fc}-\bar e_f)^2 \sum_c (e_{gc}-\bar e_g)^2}}$ |
| Uncentered correlation (cosine) | as Pearson, but with $e_{fc}, e_{gc}$ in place of the centered deviations: $r_{fg} = \dfrac{\sum_c e_{fc} e_{gc}}{\sqrt{\sum_c e_{fc}^2 \sum_c e_{gc}^2}}$ |
| Spearman rank correlation | as Pearson, but with each $e_{gc}$ replaced by its rank within gene $g$'s values across conditions |
| Absolute / squared correlation | $d_{fg} = 1 - \lvert r_{fg} \rvert$ or $d_{fg} = 1 - r_{fg}^2$ |

(D'haeseleer 2005, *Nature Biotechnology* — the source of this table.)

## Evaluating a clustering

A clustering algorithm will always produce clusters; nothing in k-means or hierarchical clustering
checks whether they mean anything. Two ways of checking, independent of the data used to build the
clusters:

- **Robustness.** Repeatedly draw a random subsample of the data and re-cluster it. A cluster that
  keeps reappearing across subsamples is robust; one that appears once and never again is likely an
  artifact of that particular sample.
- **Category enrichment.** Check whether a cluster is over-represented for some outside category —
  a functional annotation, in the expression case; the same idea is used to evaluate motif
  discovery.

### The hypergeometric test for enrichment

Suppose $N$ experiments (or genes) are labeled, from outside information, as $p$ positive and
$N - p$ negative, and a cluster of $k$ elements contains $m$ of the positives. If the cluster were
just a random size-$k$ subset of the $N$ elements, the chance of drawing exactly $m$ positives and
$k - m$ negatives is
$$\frac{\binom{p}{m}\binom{N-p}{k-m}}{\binom{N}{k}},$$
the number of ways to choose $m$ from the $p$ positives times the number of ways to choose the
remaining $k-m$ from the $N-p$ negatives, divided by the number of ways to choose any $k$ of the $N$
elements. Summing over all outcomes at least as extreme gives the p-value for the cluster being
this enriched by chance:
$$P(\mathrm{pos} \ge r) = \sum_{m \ge r} \frac{\binom{p}{m}\binom{N-p}{k-m}}{\binom{N}{k}}.$$
A small p-value says the cluster is too rich in positives to be explained by drawing $k$ elements
at random — i.e. the clustering has picked out real structure that lines up with the outside label.

<figure>
<svg viewBox="0 0 370 130" role="img" aria-label="N items with p marked positive; a cluster of k items drawn from them contains m of the positives">
  <rect x="20" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="44" y="20" width="18" height="18" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <rect x="68" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="92" y="20" width="18" height="18" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <rect x="116" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="140" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="164" y="20" width="18" height="18" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <rect x="188" y="20" width="18" height="18" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <rect x="212" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="236" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <rect x="260" y="20" width="18" height="18" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <rect x="284" y="20" width="18" height="18" fill="none" stroke="currentColor"/>
  <text x="320" y="34" font-size="12" fill="currentColor">$N$ items</text>
  <path d="M 92 55 L 92 65 L 236 65 L 236 55" fill="none" stroke="currentColor"/>
  <text x="164" y="80" text-anchor="middle" font-size="12" fill="currentColor">k elements (this cluster)</text>
  <text x="164" y="98" text-anchor="middle" font-size="12" fill="currentColor">shaded = positive; m of the k fall inside the bracket</text>
</svg>
<figcaption>Shaded squares are the $p$ positives among $N$ items; the bracketed run of $k$ squares
is the cluster, containing $m$ shaded ones. The hypergeometric p-value asks how likely a random
size-$k$ draw is to contain $m$ or more shaded items.</figcaption>
</figure>

### Two worked cases from the lecture

- **Eisen (1998), PNAS.** Clustering 8600 human genes by an expression time course in fibroblasts
  produced clusters that lined up with recognizable functional categories: cholesterol
  biosynthesis, cell cycle, immediate early response, signalling and angiogenesis, and wound
  healing — the enrichment check confirming that the expression-based grouping tracked real
  biology.
- **Tavazoie & Church (1999).** Clustering expression across 15 time points of the yeast cell cycle,
  then checking clusters for shared upstream regulatory motifs rather than functional annotation:
  a ribosomal-gene cluster was enriched for the Rap1 motif, a methionine/sulphur-metabolism cluster
  for Met31/32p and Cbf1p sites, and an RNA-metabolism/translation cluster for two further motifs.
  The evaluation here is motif content standing in for the category-enrichment test above.

## From clustering to classification

Classification starts from the opposite situation: some points already carry labels, and the task
is a rule for labeling new ones. Two broad strategies:

- **Generative** (e.g. naive Bayes): pose the problem in probabilistic terms, model how each
  feature is distributed *within* each class, and use probability calculus to decide.
- **Discriminative** (e.g. support vector machines): do not model the underlying distributions at
  all; decide from the new point's distance to a boundary that was fit directly. (The lecture names
  gene finding with HMMs versus with conditional random fields as the corresponding generative/
  discriminative pair in that setting.)

### Bayesian classification with a single feature

The generative approach needs $P(\text{feature} \mid \text{class})$ — the distribution of some
measurable quantity in each class. The lecture's examples: DNA-repair genes show higher expression
under stress; protein-coding regions show higher conservation than non-coding; regulatory regions
show higher GC content than background. In each case there is a foreground distribution and a
background distribution to be told apart.

Two distinct problems are hiding inside "classify with this": if the two class-conditional
distributions are already known, how should a new point be classified — by picking a cutoff, by
minimizing the classification error, or by maximizing the posterior probability? And if instead you
have many already-labeled examples, how are the distributions themselves estimated — parametrically
or non-parametrically, and what priors on the classes are assumed?

Both questions are governed by **Bayes' rule**, which turns the class-conditional distribution
around into the quantity actually wanted, the probability of the class given the feature:
$$P(\text{Class} \mid \text{Feature}) =
\frac{\overbrace{P(\text{Feature} \mid \text{Class})}^{\text{likelihood}}\,
\overbrace{P(\text{Class})}^{\text{prior}}}
{\underbrace{P(\text{Feature})}_{\text{evidence}}},$$
where the left-hand side is the **posterior**. The lecture reaches this point — the statement of
Bayes' rule for a single feature — and stops there; naive Bayes with multiple features, and the
discriminative alternative (SVMs), are named on the lecture's own agenda but are not in the slides
supplied for this chapter.

## Sources

- Slides: `01-lecture-7.md` — expression matrices, clustering vs. classification, k-means (the
  algorithm, the update rule, the cost-function derivation, fuzzy k-means), k-means as a Gaussian
  mixture model fit by EM.
- Slides: `03-three-options-for-assigning-points-and-their-parallels-acros.md` — the pick-best/
  average-all/sample-one table across k-means, HMM training and motif discovery; the challenge of
  choosing $K$; hierarchical clustering and UPGMA; the four cluster-distance measures.
- Slides: `04-point-to-point-dis-similarity-measures.md` — the point-to-point distance/similarity
  table (D'haeseleer 2005, *Nature Biotechnology*); evaluating clusters by robustness and category
  enrichment; the hypergeometric enrichment test; the Eisen (1998, PNAS) and Tavazoie & Church
  (1999) examples; the generative/discriminative split for classification; Bayesian classification
  with a single feature and Bayes' rule.
- No transcript, notes or exercises were supplied for this lecture; nothing in this chapter draws
  on them.
- The supplied slides break off partway through the lecture's own agenda (item 4, naive Bayes):
  discriminant functions, training/testing, combining multiple features, and the optional
  support-vector-machine material (item 5) are named in the agenda slide repeated throughout the
  deck but are not present in the three files supplied here, and so are not covered.
- HMM training (Viterbi, Baum-Welch), MEME and Gibbs sampling for motif discovery are referred to
  by name in the assignment-rule table as parallels to k-means, but are not themselves explained in
  this lecture's slides — they belong to other lectures in the course.

---

[← 5. Training Hidden Markov Models](05-training-hidden-markov-models.md) · [Contents](index.md) · [7. Challenges in Regulatory Genomics →](07-challenges-in-regulatory-genomics.md)
