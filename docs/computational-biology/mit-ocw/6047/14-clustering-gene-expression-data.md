---
title: "14. Clustering Gene Expression Data"
course: "MIT 6047"
chapter: 14
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Clustering Gene Expression Data

## What this covers

Given the expression level of thousands of genes measured across many conditions — developmental
stages, disease states, time points — how do you find groups of genes (or groups of samples) that
behave alike, with no labels given in advance? That is clustering, an unsupervised problem, and
this chapter works through the two families of algorithm used on gene expression data: partitional
methods (k-means and its fuzzy and probabilistic relatives) and agglomerative methods (hierarchical
clustering). It assumes basic probability — Gaussian densities, maximum likelihood — and comfort
with vectors and distance metrics. No prior exposure to microarrays or RNA-seq is assumed; the
chapter builds that up first, since it is what a row of the data being clustered actually means.
Classification, the supervised counterpart, is deliberately left for the next chapter, though the
distinction is worth having clearly in mind before either.

## Clustering versus classification

**Classification** assigns a new observation to one of a fixed set of categories, using a training
set of observations whose category is already known. It is *supervised*: the labels exist before
the algorithm runs, and the work is to find a rule — from a chosen set of features — that predicts
them accurately on new data.

**Clustering** has no labels to start from. It groups observations by some notion of inherent
similarity, typically distance between points in a vector space, and the labels it produces (which
group a point falls into) are the *output*, not an input. The difficulty is not choosing features
against known answers, but discovering structure that was not given.

The two are often confused because both produce "which group does this belong to" answers, but the
information available going in is completely different — that is the distinction to hold onto
before looking at either family of algorithm.

Clustering earns its place in computational biology because gene expression naturally raises
"who behaves like whom" questions with no pre-existing labels: genes that switch on and off
together across developmental stages plausibly share regulation, and if an uncharacterized gene
falls into that group, its function can be guessed *by association* with the characterized genes it
clusters with. The same logic applies to chromatin marks and regulatory motifs, letting predicted
regulator–target relationships feed models of gene expression that can, in turn, be used to reason
about disease states or engineer tissue-specific regulatory circuits. Large open datasets — the
ENCODE project (launched 2003, aiming at a complete catalogue of functional elements in the human
genome) is the standing example — are what make this practical at scale.

## Measuring gene expression: microarrays and RNA-seq

Directly measuring protein concentration is hard: proteins vary in location, modification state,
and the proteome itself is incompletely catalogued. mRNA is easier to measure and is usually a
reasonable proxy, at the cost of only seeing regulation up to the transcriptional level — anything
happening at translation or via protein degradation is invisible to it. Two technologies produce
the expression data that gets clustered.

**Microarrays** exploit hybridization between complementary DNA strands. Short DNA probes are
fixed to a solid surface (a "gene chip"). The RNA population of interest is reverse-transcribed to
cDNA — using the poly-A tail as a primer where one exists, or a ligated primer otherwise — because
cDNA hybridizes to the probe more readily than RNA does, and because reverse transcription sidesteps
the secondary structure that makes RNA reluctant to bind. The cDNA is washed over the chip, and
hybridization triggers fluorescence at each probe, whose intensity is read off to give relative
transcript abundance. Affymetrix chips use one spot per gene with long (hundreds-of-nucleotide)
probes; spotted oligonucleotide arrays tile each gene with many shorter probes (tens of bases).
Reverse transcription introduces its own errors — mismatches that weaken or misdirect hybridization
— which is one reason to use several probes per gene, since cross-hybridization differs from probe
to probe.

**RNA-seq** (whole-transcriptome shotgun sequencing) removes the need to design probes at all: it
sequences the cDNA directly, at whatever resolution the sequencing technology provides, rather than
reading fluorescence off a fixed set of preselected spots. It is the natural successor to
microarrays and has been adopted quickly in areas such as cancer transcriptomics, where fusion
transcripts and other rearrangements are exactly the sort of thing a fixed probe set would miss.
Once produced, RNA-seq data is clustered by the same methods as microarray data.

### From measurements to a gene expression matrix

Either technology, run across many conditions, produces a matrix: rows are genes, columns are
experiments (conditions, time points, samples), and each entry is typically a log ratio
$\log(T/R)$, where $T$ is the expression level in the test sample and $R$ in a reference sample. A
representative fragment of such a matrix looks like this:

| | Exp 1 | Exp 2 | Exp 3 | Exp 4 | Exp 5 | Exp 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gene 1 | -1.2 | -2.1 | -3 | -1.5 | 1.8 | 2.9 |
| Gene 2 | 2.7 | 0.2 | -1.1 | 1.6 | -2.2 | -1.7 |
| Gene 3 | -2.5 | 1.5 | -0.1 | -1.1 | -1 | 0.1 |
| Gene 4 | 2.9 | 2.6 | 2.5 | -2.3 | -0.1 | -2.3 |
| Gene 5 | 0.1 | | 2.6 | 2.2 | 2.7 | -2.1 |
| Gene 6 | -2.9 | -1.9 | -2.4 | -0.1 | -1.9 | 2.9 |

Rendered as a heatmap and clustered hierarchically, both dimensions can be reordered so that
similar rows sit near similar rows and similar columns near similar columns — this is
*biclustering*, clustering along both axes at once — and the resulting picture is what makes it
possible to read off, at a glance, which genes move together and under which conditions, which in
turn is what lets a hidden pattern in a stretch of genome be tied back to a disease mechanism.

Two difficulties come with this. First, the curse of dimensionality: as the number of conditions
(dimensions) grows, points spread out and apparent proximity becomes less informative, so it is
often necessary to reduce to a lower-dimensional representation before clustering on distance makes
sense. Second, the numbers are not a clean read-out of "gene activity": protein-coding exons show
higher signal than introns partly because introns are degraded quickly (though not all introns are
inert, and alternative splicing can be genuinely ambiguous), and non-sense-mediated decay removes
some aberrant transcripts before they can be measured at all.

## Clustering algorithms

Clustering methods split into two families. **Partitional** methods divide the data into
non-overlapping clusters, one label per point. **Agglomerative** methods build a nested hierarchy
of clusters, from individual points up to one cluster containing everything. K-means, in its
several variants, is the standard partitional method; hierarchical clustering is the standard
agglomerative one.

### K-means

K-means partitions $n$ points into $k$ clusters by minimizing the total distance from each point to
the center of the cluster it is assigned to — that is, it looks for the most compact clusters
possible under a chosen (usually Euclidean) distance. The algorithm:

1. **Fix** the number of clusters $k$.
2. **Initialize**: pick $k$ means $\mu_k$ at random, and assign each point $x_i$ to the nearest one,
   using $d_{i,k} = (x_i - \mu_k)^2$.
3. **Iterate**: recompute each centroid as the mean of the points currently assigned to it,
$$\mu_k(n+1) = \frac{\sum_{x_i \in k} x_i}{|x_k|},$$
   where $|x_k|$ is the number of points with label $k$; then reassign every point to its nearest
   new centroid.
4. **Terminate** on convergence, or after a fixed number of iterations. The iteration can get stuck
   at a local optimum rather than the global one.

Choosing $k$ is not given by the algorithm. One approach is simply to look at the data; another is
to try a range of values while penalizing model complexity, since increasing $k$ can always improve
the fit — clusters get smaller and tighter — until the model is overfitting rather than describing
real structure.

K-means can be read as minimizing a cost that grows as clusters become less compact, but the hard
assignment it makes is a real limitation: a point sitting almost exactly between two centers is
forced into one of them, with nothing recorded about the ambiguity.

### Fuzzy k-means

Fuzzy k-means replaces the hard 0/1 assignment with a probability of membership in each cluster,
built from distance (for instance, inversely related to it), so a point between two centers can
belong partially to both. Initialization, iteration and termination follow the same outline as
plain k-means, but the centroid update becomes a probability-weighted average,
$$\mu_k(n+1) = \frac{\sum_{x_i \in k} x_i \times P(\mu_k \mid x_i)^b}{\sum_{x_i \in k} P(\mu_k \mid x_i)^b},$$
with membership itself recomputed each round (one possible choice among several):
$$P(\mu_k \mid x_i) = \left( \sum_{j=1}^k \left( \frac{d_{ik}}{d_{jk}} \right)^{\frac{2}{b-1}} \right)^{-1}.$$
The exponent $b$ controls how fuzzy the partition is: as $b \to 1$ the assignment becomes hard
(recovering ordinary k-means), and as $b \to \infty$ every membership tends to $1/k$, the fuzziest
possible state. There is no theoretical rule for choosing $b$; empirically useful values run over
$[1, 30]$, with $1.5 \le b \le 3.0$ working well in most studies. Ordinary k-means is exactly the
special case where the membership "probability" is $1$ for the nearest centroid and $0$ elsewhere.

### K-means as a generative model

A **generative model** specifies how observable data is produced from hidden parameters — a full
probability model of everything, in contrast to a **discriminative model**, which only models the
target variable(s) conditional on what is observed. K-means can be recast as generative by assuming
that points in cluster $k$ are drawn from a Gaussian centered at $\mu_k$ with variance fixed at $1$:
$$P(x_i \mid \mu_k) = \frac{1}{\sqrt{2\pi}} \exp\left\{-\frac{(x_i - \mu_k)^2}{2}\right\}.$$
This turns clustering into a maximum-likelihood problem, and it is worth checking that the answer
it gives back is exactly the original algorithm.

Assigning each point its most likely label given the current means (an "E-like" step) means
choosing $k$ to maximize $P(x_i \mid \mu_k)$; because the exponential is a decreasing function of
$(x_i - \mu_k)^2$ and the prefactor does not depend on $k$, this is the same as
$$\arg\max_k P(x_i \mid \mu_k) = \arg\min_k (x_i - \mu_k)^2,$$
i.e. assignment to the nearest center — identical to the k-means rule.

Re-estimating the mean given the labels (an "M-like" step) means maximizing the log-likelihood over
$\mu$:
$$\arg\max_\mu \left\{ \log \prod_i P(x_i \mid \mu) \right\} = \arg\max_\mu \sum_i \left\{ -\tfrac{1}{2}(x_i - \mu)^2 + \log\tfrac{1}{\sqrt{2\pi}} \right\} = \arg\min_\mu \sum_i (x_i - \mu)^2,$$
and the constant term drops out of the argmax entirely. The minimizer of a sum of squared
deviations is the mean of the data — exactly the centroid recomputation k-means already does. So
under a fixed-variance, axis-independent Gaussian assumption, maximum likelihood *is* k-means; the
two are not merely analogous, they coincide.

That fixed-variance, independent-axes assumption is also the source of k-means's blind spot: it
cannot represent clusters that are elongated or correlated across axes (oblong distributions),
because covariance between axes is never modeled. Lifting that restriction is exactly what
generalizing to full expectation maximization buys.

### K-means as an instance of expectation maximization

Seen this way, k-means is a special case of the EM algorithm: the E step estimates the hidden
labels $Q$ given the current parameters (assign each point to its nearest center), and the M step
re-estimates the parameters to maximize the expected likelihood given those labels (move each
center to the mean of its assigned points). Because k-means commits to a single hard labeling at
each E step, it is analogous to *Viterbi learning* in a hidden Markov model — alternating between
the single best hidden path and re-estimating parameters from it. Fuzzy k-means, which keeps a full
distribution over labels rather than committing to one, is the corresponding analogue of
*Baum-Welch*, which uses expected (soft) counts.

Once k-means is seen as EM on a Gaussian mixture with a fixed, shared, isotropic variance, that
restriction is easy to lift: allowing a full covariance matrix in the Gaussian lets clusters have
different sizes, and letting variance differ across axes produces oblong clusters — capabilities
plain k-means, tied to nearest-centroid assignment, simply does not have.

EM is guaranteed to converge, but not necessarily to the global optimum: local maxima of the
likelihood surface can trap it. Running the algorithm from several random initializations, and
comparing the results, is the standard way to guard against settling on a poor local optimum.

### Limitations of k-means

Four limitations are worth keeping in mind before reaching for k-means:

- **It needs a metric.** There is no distance between, say, a set of words without imposing one, so
  k-means cannot be applied directly to unstructured categorical data.
- **It is sensitive to noise.** Running a principal component analysis beforehand can help, as can
  weighting each variable — down-weighting the noisier ones — with weights recomputed dynamically
  at every iteration.
- **Initial centers matter.** Different starting centers can lead to different final clusterings;
  various heuristics exist for choosing them, none of them perfect.
- **$k$ has to be known in advance.** Running the algorithm repeatedly over a range of $k$ values
  (with a complexity penalty to avoid simply choosing the largest $k$) is one workaround; a rule of
  thumb, $k \approx \sqrt{n/2}$, is a cheap alternative when computation is limited. Hierarchical
  clustering, discussed next, sidesteps the problem by not requiring $k$ up front at all.

### Hierarchical clustering

Similarity in biological data is often hierarchical — not just "close" but close at some level of
resolution and not another — and this is exactly what the partitional methods above ignore.
Hierarchical (agglomerative) clustering builds that structure directly:

1. **Initialize**: treat every point as its own cluster.
2. **Iterate**: find the two closest clusters, merge them into a new cluster, and replace the two
   originals with it in the list.

Recording the distance at which each merge happens produces a tree (a dendrogram) showing, for
every pair of points, how similar they had to become before being grouped together. Choosing a
number of clusters is then just choosing a height at which to cut the tree: every branch the cut
crosses is one cluster. This convenience comes with a real pitfall, though — points can be close in
the original space and still end up on different sides of a given cut, if the merges that would
have joined them happen only at a much larger distance than the cut allows.

<figure>
<svg viewBox="0 0 360 270" role="img" aria-label="A dendrogram over five points cut into two clusters, next to the same points placed by their actual value on one feature, showing two spatially close points split by the cut">
  <text x="60" y="215" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <text x="120" y="215" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <text x="180" y="215" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="240" y="215" text-anchor="middle" font-size="12" fill="currentColor">d</text>
  <text x="300" y="215" text-anchor="middle" font-size="12" fill="currentColor">e</text>

  <line x1="60" y1="200" x2="60" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="120" y1="200" x2="120" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="60" y1="160" x2="120" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="160" x2="90" y2="60" stroke="currentColor" stroke-width="1.5"/>

  <line x1="180" y1="200" x2="180" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <line x1="240" y1="200" x2="240" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <line x1="180" y1="150" x2="240" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="150" x2="210" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <line x1="300" y1="200" x2="300" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="110" x2="300" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <line x1="255" y1="110" x2="255" y2="60" stroke="currentColor" stroke-width="1.5"/>

  <line x1="90" y1="60" x2="255" y2="60" stroke="currentColor" stroke-width="1.5"/>

  <rect x="45" y="60" width="90" height="140" fill="currentColor" fill-opacity="0.1"/>
  <rect x="165" y="60" width="150" height="140" fill="currentColor" fill-opacity="0.1"/>

  <line x1="30" y1="85" x2="330" y2="85" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="338" y="89" font-size="11" fill="currentColor">cut</text>

  <line x1="30" y1="240" x2="330" y2="240" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="50" cy="240" r="3" fill="currentColor"/>
  <text x="50" y="257" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <circle cx="130" cy="240" r="3" fill="currentColor"/>
  <text x="130" y="257" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <circle cx="215" cy="240" r="3" fill="currentColor"/>
  <text x="215" y="257" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <circle cx="228" cy="240" r="3" fill="currentColor"/>
  <text x="228" y="257" text-anchor="middle" font-size="12" fill="currentColor">e</text>
  <circle cx="310" cy="240" r="3" fill="currentColor"/>
  <text x="310" y="257" text-anchor="middle" font-size="12" fill="currentColor">d</text>
  <text x="180" y="230" text-anchor="middle" font-size="11" fill="currentColor">position on one feature</text>
</svg>
<figcaption>The dendrogram (top) merges a with b, then c with d, then that pair with e, then
everything at the root; cutting it at the dashed line gives clusters {a, b} and {c, d, e}. But
placed by their actual value on one feature (bottom), b and e are the closest pair of all five —
and the cut still separates them, because the merges that would join them happen only higher up
the tree.</figcaption>
</figure>

A distance between *clusters*, not just between points, is also needed to decide what "closest"
means at each merge step. Common choices are the minimum distance between any pair of points in the
two clusters (single linkage), the maximum such distance (complete linkage), the average distance
over all pairs, or the distance between the two clusters' centroids — and different choices can
produce different trees from the same data.

Computing every pairwise distance at every step is expensive in both time and space. A cheaper
scheme: partition the feature space into bounding boxes, compute distances only within each box,
then shift the box boundaries and recompute, taking the closest pair found across all the shifted
partitions as the merge candidate.

### Evaluating a clustering

A clustering can be checked against outside knowledge — a cluster that is enriched for a known
functional group of genes, or more generally correlates with a confirmed biological association, is
evidence the clustering is real rather than an artifact. Where no such biological reference is
available, purely statistical checks are available too: a robust cluster should reappear when the
algorithm is run on only a subset of the data, and the significance of a given cluster's makeup can
be assessed with variants of the hypergeometric distribution — for instance, the probability of
getting more than $r$ "positive" items by chance when drawing $k$ elements from a pool of $N$, of
which some are positive, gives a way to ask whether an observed enrichment could plausibly be due to
chance.

## Scaling clustering to larger, higher-dimensional data

Two properties of modern datasets stress these algorithms: sheer size, and dimensionality. For
size, a common strategy is a coarse pre-clustering pass — *canopy clustering* — that partitions the
data cheaply before a standard algorithm like k-means is run to refine each coarse group. For
dimensionality, the usual approach is a two-stage process: first find relevant lower-dimensional
subspaces via some transformation of the original feature space, then cluster within those
subspaces, since distance in the full high-dimensional space becomes less meaningful as
dimensionality grows (the curse of dimensionality already noted above, in more general form).

## Sources

- MIT OCW 6.047 *Computational Biology* (Fall 2015), lecture notes "Gene Regulation 1 – Gene
  Expression Clustering," compiled chapter 15 of the course notes compilation:
  `docs/computational-biology/mit-ocw/6047/compiled/compiled-compiled/05-gene-regulation-1-gene-expression-clustering.md`
  in the knowledge-base-library. This document is machine-reconstructed from a PDF with no text
  layer (route: llm, fidelity: reconstructed); the prose is paraphrased in the original conversion
  and its equations are marked unverified there, so this chapter should be treated as a pointer
  into the source lecture (MIT OCW, CC BY-NC-SA 4.0), not a citable primary account of it.
- All figures referenced in the source (15.1–15.15) are described only in caption form in the
  material available here — no image data was supplied — so the dendrogram diagram above is newly
  drawn to carry the specific pitfall the source describes (its own Figure 15.13 example, using
  points "e" and "b"), not a reproduction of the original figure.
- The lecture named, but did not itself explain, a number of external resources: Hastie, Tibshirani
  and Friedman's *The Elements of Statistical Learning*; *Numerical Recipes*; McLachlan and
  Basford's *Mixture Models: Inference and Applications to Clustering*; Bezdek, Ehrlich and Full's
  1984 paper introducing fuzzy c-means; the ENCODE project (genome.ucsc.edu/ENCODE); and several
  software packages for clustering gene expression data (Cluster 3.0, MATLAB's k-means/fuzzy
  c-means/hierarchical clustering functions, Orange, R, and SAS CLUSTER). None of these were read
  as part of preparing this chapter.

---

[← 13. HMM Posterior Decoding and Learning](13-hmm-posterior-decoding-and-learning.md) · [Contents](index.md) · [15. Naive Bayes and SVM Classification →](15-naive-bayes-and-svm-classification.md)
