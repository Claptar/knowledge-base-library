---
title: "15. Clustering and Inferring Regulatory Networks"
course: "MIT 7.091J"
chapter: 15
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Clustering and Inferring Regulatory Networks

## What this covers

This chapter answers two linked questions: given a pile of gene expression measurements, how do
you decide which genes behave alike and group them without knowing in advance how many groups
there are or what they mean — and once you have groups, how do you move from "these genes rise and
fall together" to "this transcription factor is driving that set of genes"? It assumes you already
have Bayesian networks as a tool for reasoning under uncertainty (nodes, edges, conditional
probability tables, hidden vs. observed variables), since the chapter opens by finishing off the
previous lecture's use of them for protein–protein interaction prediction before carrying the same
machinery over to gene regulation.

## Finishing protein–protein interaction prediction with Bayesian networks

A Bayesian network reasons from effects back to causes: the hidden node is whether two proteins
*truly* interact, and the observed nodes are whatever assays detected (or failed to detect) that
interaction. The lecture closed out this topic with a worked example from a paper out of Mark
Gerstein's lab, which combined high-throughput interaction assays — yeast two-hybrid and
affinity-capture mass spectrometry ("pull-downs") — with indirect evidence: expression correlation,
shared functional annotation, and essentiality (whether knocking the gene out is lethal in yeast).
Gold-standard positives came from MIPS, a hand-curated interaction database; negatives were protein
pairs localized to different parts of the cell.

Two separate networks were built: a **naive Bayes** over the indirect evidence, and a **fully
connected Bayes** over the four direct experimental assays — because naive Bayes' independence
assumption is a poor fit when the "evidence" is four assays that likely share detection biases. Some
numbers made the point: among gold-standard positives, about 50% had both proteins essential (EE),
against roughly 14–15% of negatives, a likelihood ratio just under 4 — essentiality is only weakly
informative. Expression correlation could carry a likelihood ratio over 100-fold when two genes were
very highly correlated. For the direct assays, the fully connected table was built the same way —
tabulating how often each combination of "detected/not detected" across the four assays occurred
among positives and negatives — but the pairs detected in *all four* assays were not the top-ranked
prediction, which the lecturer attributed to the statistics of small numbers in some of those
categories.

Plotting true positives against false positives at different likelihood-ratio thresholds, every
individual piece of evidence got more wrong than right; combined through the Bayesian network, both
the indirect-evidence and the direct-experimental networks could be tuned to get more right than
wrong. The lesson carried into the rest of the chapter: no single kind of evidence about a biological
relationship is very predictive alone, but weak evidence combines.

## Comparing gene expression profiles: distance metrics

Gene expression databases dwarf every other kind of high-throughput biological data — by this
lecture the field had passed a million deposited datasets — so methods for extracting meaning from
expression data matter disproportionately. Each gene's expression is a vector, one entry per
condition or time point, and the starting question is how similar two such vectors are.

A **distance metric** is a function $d(x,y)$ with $d(x,y) \ge 0$; $d(x,y)=0$ iff $x=y$; symmetry
$d(x,y)=d(y,x)$; and, to be a true metric rather than merely a similarity measure, the triangle
inequality $d(x,z)\le d(x,y)+d(y,z)$.

The most intuitive choice is **Euclidean distance**:

$$d(A,B) = \sqrt{\sum_k \left(x_{A,k} - x_{B,k}\right)^2}$$

but it is sensitive to the *absolute* level of expression, which is often close to arbitrary — array
intensities depend on hybridization efficiency, and there is no principled reason to treat 1,000 and
1,200 mRNA copies as fundamentally different. **Pearson correlation** instead compares *shape*:
convert each gene's expression to a z-score across conditions and correlate the two z-score vectors,

$$r(A,B) = \frac{1}{N}\sum_k z_{A,k}\, z_{B,k}, \qquad z_{g,k} = \frac{x_{g,k} - \bar{x}_g}{\sigma_g}$$

ranging from $+1$ (perfectly correlated) to $-1$ (perfectly anti-correlated); the corresponding
distance is usually $1-r$. In the lecture's worked example, a "red" and "blue" gene with very
different absolute levels but the same up-down trajectory looked dissimilar under Euclidean distance
but had $r=1$; a third "green," nearly-flat gene had $r\approx 0$ against both. Which metric to use
is a judgment call, not something settled in advance. For missing values, the options mentioned were
dropping the affected row/column, substituting an arbitrary small value, or **imputing** from the
genes with the most similar expression.

## Clustering gene expression data

Clustering is **unsupervised**: the classes, and even their number, are not known in advance. The
standard presentation is a heat map, genes as rows and experiments (time points, perturbations,
patients) as columns, red for increased and green for decreased expression. Clustering rows finds
genes that behave similarly — candidates for shared function or regulation; clustering columns finds
experiments or patients that respond similarly.

### Hierarchical clustering

Hierarchical clustering is **agglomerative** (start with every point in its own cluster and
repeatedly merge the most similar pair) or **divisive** (the reverse). Comparing individual genes is
settled by the distance metrics above; comparing two *clusters* needs a linkage rule:

- **Single linkage** — the minimum distance between any member of one cluster and any of the other.
- **Complete linkage** — the maximum such distance.
- **UPGMC** (centroid method) — distance between the two clusters' centroids.
- **UPGMA** (average method) — the average of all pairwise distances between members.

These behave differently: single linkage tends to **chain** clusters together through points that
happen to be close, even when the clusters it joins are otherwise different; complete linkage
resists being misled by a single outlier. With compact, well-separated data the choice barely
matters; with noisy biological data it can change the result, and there is no principled way to pick
between them without prior knowledge of the data.

The output is a **dendrogram**: the height at which two branches join reflects how far apart the two
groups are, and cutting the dendrogram at any height partitions the data without needing the number
of clusters in advance. But a dendrogram is produced whether or not the data actually has
hierarchical structure — it reflects the procedure, not necessarily anything fundamental about the
data.

### K-means clustering

**K-means** fixes the number of clusters $K$ in advance and minimizes total squared distance to
cluster centroids:

$$\min_{C} \sum_{i=1}^{K} \sum_{x_j \in C_i} \lVert x_j - \mu_i \rVert^2, \qquad
\mu_i = \frac{1}{|C_i|}\sum_{x_j \in C_i} x_j$$

Algorithm: choose $K$ initial points as cluster means, then repeat — assign every point to the
nearest centroid, then recompute each centroid as the mean of its assigned points. The objective
never increases, so the algorithm converges, but not necessarily to the global optimum: a bad
initialization can converge to a poor local minimum, so it is standard to restart from several
random initializations. K-means always returns exactly $K$ clusters, right or wrong: told to find
three clusters in data generated from five true groups, it merges some groups and splits others. One
empirical way to choose $K$ is to plot the within-cluster sum of squared distances against $K$: this
drops sharply up to the true number of groups, then levels off — an "elbow."

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Within-cluster distance dropping sharply then leveling off as K increases, with an elbow at the true number of clusters">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="20" x2="40" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">K</text>
  <text x="18" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 100)">within-cluster distance</text>
  <polyline points="55,40 90,75 125,105 160,130 195,145 230,152 265,157 295,161"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="195" cy="145" r="4" fill="currentColor"/>
  <text x="200" y="135" font-size="11" fill="currentColor">elbow (K = true number of clusters)</text>
</svg>
<figcaption>The within-cluster distance keeps dropping as K grows, but the drop is large only up to
the true number of clusters, after which each extra cluster buys little.</figcaption>
</figure>

A point sitting between two well-separated clusters forces K-means into an arbitrary hard choice.
**Fuzzy K-means** replaces hard assignment with a membership variable $\mu_{ij}$ (the degree to
which point $j$ belongs to cluster $i$), and recomputes each centroid as a weighted average:

$$J = \sum_i \sum_j \mu_{ij} \lVert x_j - c_i \rVert^2, \qquad
c_i = \frac{\sum_j \mu_{ij}\, x_j}{\sum_j \mu_{ij}}$$

Setting every $\mu_{ij}$ to 0 or 1 recovers ordinary K-means; otherwise genes split between clusters
get intermediate membership, shown on a continuous color scale.

K-means also requires that a "centroid" (an average) be a meaningful object, which fails for
qualitative data or for something like a set of sequence motifs, where an "average motif" need not
correspond to anything real. **K-medoids** restricts the cluster center to an actual data point:

- Initialize: choose $k$ points from the data as cluster medoids.
- Repeat until convergence:
  - Assignment: place each point $X_i$ in the cluster with the closest medoid.
  - Update: recompute the medoid of each cluster.

A student asked whether a discrete medoid update could break the convergence guarantee; the lecturer
agreed this was a reasonable concern without a settled answer. Self-organizing maps and affinity
propagation (Frey and Dueck, 2007, *Science*) were named as further methods but not developed.

## Why cluster: from gene groups to clinical signatures

An early, influential example clustered microarray data from diffuse large B-cell lymphoma
patients — genes as rows, patients as columns — and found a sharp division into two large groups.
Checked against the pathologist's independent diagnosis, one cluster corresponded almost entirely to
one histological subtype (germinal-center B-like DLBCL) and the other to activated B-like DLBCL
(Alizadeh, Eisen, et al., *Nature* 403, 2000). That purely molecular clustering recovered a clinical
distinction was exciting, but the further claim — that expression could stratify patients the
clinician already called low-risk into groups with different actual outcomes — is what set off wide
interest in gene expression "signatures."

## A caution: most gene signatures look predictive

Statistical association with outcome does not mean mechanistic relevance. Venet, Dumont and Detours
(*PLoS Computational Biology* 7, 2011) tested this in a breast cancer dataset: a signature built from
genes associated with **post-prandial laughter** was significantly associated with survival (hazard
ratio 1.8, CI 1.2–2.9, $p=0.0072$); one built from human homologs of genes associated with **social
defeat in mice** did even better (hazard ratio 2.4, CI 1.5–3.9, $p=0.00014$). Across many published
signature studies, a large fraction of randomly chosen gene sets — or sets pulled from pathway
databases — predicted outcome about as well as the published signature.

The explanation offered was coexpression: a very large fraction of the genome is coexpressed with
PCNA (proliferating cell nuclear antigen), a long-known marker of proliferation, so almost any random
gene set carries some PCNA-correlated signal, and high expression of that set becomes a workable, if
mechanistically empty, proxy for a proliferation-driven prognosis. A correlation with outcome can be
real and reproducible and still have nothing to do with disease mechanism — it does not license
treating the genes in the signature as a drug target, and such predictions can fail entirely on a
population where the coexpression structure differs.

## From clusters to modules

The slides draw an explicit distinction: a **cluster** is purely phenomenological, no claim of
causality; a **module** implies a more mechanistic connection — typically a transcription factor and
the genes it actually regulates, not merely genes that move together. The rest of the lecture turns
to methods that try to recover that mechanistic structure.

The organizing reference is the **DREAM5** challenge (Marbach, Costello, et al., *Nature Methods* 9,
2012), a blind benchmark of regulatory-network inference methods. Organizers supplied expression
data from a simulated ("in silico") network and from three real organisms (*E. coli*, *S.
cerevisiae*, *S. aureus*), with hundreds of regulators and thousands of genes each, across hundreds
of arrays and experimental conditions (knockouts, antibiotics, toxins, and more), and withheld the
true regulatory structure — known exactly for the simulation, and assessed against experimentally
determined interactions and ChIP motifs for the real organisms. Groups submitted anonymized
predictions; organizers also built a consensus ("wisdom of crowds") prediction from the individual
submissions. Submitted methods fell into a few broad families — regression, Bayesian networks,
mutual information and correlation, and a catch-all "other" — the same families covered below.
Predictions were scored by area under the precision–recall curve (AUPR); the lecture set this
comparison up but left the actual head-to-head results for the next lecture.

## Bayesian networks for regulatory relationships

The same machinery used for protein interactions carries over to asking whether a pathway is active.
Take "is the p53 pathway activated in this tumor?" Several pieces of evidence suggest themselves,
each with a hole: known p53 targets being up-regulated could be caused by another pathway; pathway
genes (ATM, ATR, CHK1, …) being expressed can be true even when the pathway has not been activated;
and those genes being differentially expressed still does not prove a change in activity, since
expression changes are not uniquely tied to protein level or post-translational activation (e.g.
phosphorylation, invisible to expression data).

Formulated probabilistically, the goal is $P(\text{p53 active}\mid\text{data})$. The tractable
quantity is $p(X\text{ up}\mid\text{TF up})$, estimated by tabulating across experiments how often a
target $X$ is up when the transcription factor is up, up when it is not, and so on. Bayes' rule then
gives the quantity wanted:

$$P(\text{TF up}\mid X\text{ up}) = \frac{p(X\text{ up}\mid\text{TF up})\, p(\text{TF up})}{p(X\text{ up})}$$

A Bayesian network lets this reasoning use more than the downstream targets alone. The lecturer
recalled the network's "explaining away" property: if the grass is wet and it is already known to
have rained, that makes the sprinkler less likely, even with no causal link between rain and
sprinklers. Applied here, if targets downstream of transcription factor A are on, and there is
independent evidence the pathway upstream of A is active, that reduces the inferred probability that
some *other* factor B — one regulating overlapping targets — is responsible, letting the network
reason over upstream regulators as well as downstream targets. These networks can have many layers,
but, as always, no cycles.

As before, there are two things to learn: the network's structure (when not known a priori) and the
conditional probability tables once structure is fixed. And as before, observational data alone
cannot establish *direction*: if $X$ and $Y$ are highly correlated, that is equally consistent with
either activating the other. Resolving direction needs **perturbation** — if inhibiting $X$
abolishes activation of $Y$, but inhibiting $Y$ leaves the full range of $X$ intact, that asymmetry
identifies $X$ as the activator. A further issue: a compact model will often omit a true
intermediate regulator (measured or not). If the true chain is $X\to Y\to Z$ and $X\to Y\to W$ but
$Y$ is missing, the $X$–$Z$ and $X$–$W$ associations can still be detected, but noisier, since the
direct evidence running through $Y$'s tables is unavailable.

## Regression-based inference

The regression approach assumes a target gene's expression is a function of its regulators'
expression:

$$y_g = f\!\left(X_{t(g)}\right) + \epsilon$$

with the simplest specific choice linear:

$$y_g = \sum_i \beta_i x_i + \epsilon$$

Each $\beta_i$ measures how strongly regulator $i$ influences gene $g$: zero means no inferred
influence, larger magnitude means greater influence. The $\beta$'s are learned by minimizing residual
sum of squares. Plain least-squares tends to spread influence across many small, unstable $\beta$
values instead of cleanly separating real regulators from irrelevant ones — small changes in training
data can substantially change the ranking. Techniques that constrain most $\beta$'s to exactly zero
trade some of this instability for more robust identification of the regulators with the largest
real effect (the lecture pointed to a paper that did well on this in the DREAM challenge, and to the
textbook *Elements of Statistical Learning* for the general machinery).

## Mutual information

Mutual information asks whether knowing one variable reduces uncertainty about another, without
being restricted to linear relationships. The information content of an event $E$ is
$I(E) = \log_2(1/P(E))$, and entropy sums this over outcomes:

$$H(S) = \sum_i p_i \log_2 \frac{1}{p_i}, \qquad H(f) = -\int f(x)\ln f(x)\,dx \text{ (continuous case)}$$

Mutual information is

$$I(X,Y) = H(X) + H(Y) - H(X,Y)$$

equal to zero exactly when $X$ and $Y$ are independent. The reason to prefer it over correlation here
is that network structure can produce relationships with essentially no linear correlation but
substantial mutual information. The lecture's example was an **incoherent feed-forward loop**: a
regulator $A$ directly activates $B$ and also activates $C$, while $C$ inhibits $B$ — one path
pressing the accelerator, the other the brake. The slide's numbers for this configuration: mutual
information 1.7343 against correlation $-0.0464$ — essentially no linear correlation, substantial
shared information.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="An incoherent feed-forward loop: A activates both B and C, while C inhibits B">
  <defs>
    <marker id="arrow15" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="160" cy="30" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="35" text-anchor="middle" font-size="13" fill="currentColor">A</text>
  <circle cx="80" cy="160" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="165" text-anchor="middle" font-size="13" fill="currentColor">B</text>
  <circle cx="240" cy="160" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="240" y="165" text-anchor="middle" font-size="13" fill="currentColor">C</text>
  <line x1="147" y1="46" x2="92" y2="143" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow15)"/>
  <line x1="173" y1="46" x2="228" y2="143" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow15)"/>
  <line x1="220" y1="160" x2="100" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="100" y1="153" x2="100" y2="167" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="185" text-anchor="middle" font-size="11" fill="currentColor">C inhibits B</text>
</svg>
<figcaption>A activates both B and C directly, while C inhibits B — a configuration that leaves A and
B almost uncorrelated even though A strongly constrains B's distribution.</figcaption>
</figure>

**ARACNe** (Basso, Margolin, et al., *Nature Genetics* 37, 2005) computes mutual information between
every gene pair to propose regulatory relationships. Two problems arise. First, significance:
ARACNe shuffles the expression data to destroy any real relationship and computes the resulting null
distribution of mutual information, against which observed values are compared. Second, mutual
information cannot distinguish direct from indirect relationships: if $G_2$ regulates both $G_1$ and
$G_3$, then $G_1$ and $G_3$ will also show high mutual information, purely through $G_2$, without
either regulating the other. ARACNe resolves this with the **data processing inequality**,

$$I(g_1,g_3) \le \min\left[I(g_1,g_2),\ I(g_2,g_3)\right]$$

dropping, from every triangle of genes, the edge with the smallest mutual information, since a direct
edge should never carry less mutual information than a path routed through a third gene.

**MINDy** (Wang, Saito, et al., *Nature Biotechnology* 27, 2009) looks for **modulators** — proteins
that switch a transcription factor's regulatory effect on or off, rather than regulating the target
directly — assuming

$$[T] = C\cdot[TF]^i\cdot[M]^j$$

Candidates are filtered first by two criteria: the modulator's and the transcription factor's
expression must be statistically independent, and the modulator's expression must have sufficient
range (further filters, e.g. by molecular function, may also apply). The signature sought: split
experiments by whether the modulator is at its highest or lowest expression, and compare the
TF–target relationship within each group. A relationship present only when the modulator is high
suggests an activating modulator; present only when the modulator is low suggests an inhibitory one.
MINDy calls the direction from the sign of the Pearson correlation $\rho$ between TF and target
combined with the difference in target means $\mu_t^+-\mu_t^-$ between high- and low-modulator
conditions:

$$\begin{cases}
\text{activator} & \text{if } \rho\left(\mu_t^+ - \mu_t^-\right) > 0 \\
\text{antagonist} & \text{if } \rho\left(\mu_t^+ - \mu_t^-\right) < 0 \\
\text{undetermined} & \text{if } \rho\left(\mu_t^+ - \mu_t^-\right) \approx 0
\end{cases}$$

with the difference in means assessed by a two-sided two-sample $t$-test, left undetermined if the
null $\mu_t^+=\mu_t^-$ cannot be rejected at $\alpha=0.1$. The slides note the scheme assumes the
TF–target relationship never saturates, a real simplification. Applied to "what regulates MYC?" in
254 B-cell expression profiles, MINDy was checked against known modulators and against four
experimentally tested candidates; one example, SDK38, showed essentially no MYC–target relationship
when SDK38 was low but a clear one when SDK38 was high — the signature of an activator. Out of
candidate pools of a few hundred to a few thousand genes, MINDy typically selects 10–20% as
modulators.

These methods share real limitations: they need large datasets to estimate mutual information
reliably; they miss modulators whose own expression does not change, modulators highly correlated
with their target, and modulators that both activate and repress depending on context; and, being
built on correlative rather than perturbational structure, the resulting networks can be enormous and
hard to interpret — examples given were the dense neighborhood of a single node in an ARACNe network,
and a conditional mutual-information network of microRNA modulators with roughly 248,000 interactions
(Sumazin, Yang, et al., *Cell* 147, 2011).

## An open question: do expression levels tell you about protein levels?

The lecture's closing thought: gene expression data is useful for classification and clustering, but
on its own was "not sufficient for reconstructing regulatory networks in yeast." That raises a
further question posed, not answered, here — can protein levels be inferred from gene expression at
all? The slides cite evidence that they cannot, well: protein concentrations can range over roughly
a thousand-fold span, and independent mass-spectrometry-based estimates of protein abundance
correlate strongly with each other (around 0.9) but only weakly (roughly 0.4–0.5) with RNA-seq or
microarray measurements of the same genes (de Sousa Abreu, Penalva, et al., *Molecular Biosystems* 5,
2009; Ning, Fermin, and Nesvizhskii, *Journal of Proteome Research* 11, 2012). A further study of the
same question is cited (Schwanhäusser, Busse, et al., *Nature* 473, 2011) without its findings being
given on the slide.

## Sources

- Slides: `15-slides/01-outline.md` (k-medoids pseudocode, outline); `02-distinct-types-of-diffuse-
  large-b-cell-lymphoma-identified-b.md` (Alizadeh et al. 2000; Venet et al. 2011 hazard ratios);
  `03-15-slides-part-03.md` (Venet et al. figures; "Reconstructing Regulatory Networks" and
  "Clustering vs. modules" slides); `04-wisdom-of-crowds-for-robust-gene-network-inference.md`
  (DREAM5 overview; Bayesian-network and p53-pathway slides; information-theory definitions; mutual
  information; incoherent FFL numbers; ARACNe; MINDy model); `05-filters.md` (MINDy filters and
  mode-of-action table; MYC/SDK38 example; MINDy limitations; network-size examples; MINDy-modulator
  counts table); `06-aupr-area-under-precision-recall-curve.md` (AUPR naming; DREAM5 community-network
  figures; closing "Thoughts on Gene Expression Data"); `07-approach.md` (mRNA-vs-protein correlation
  table and citations).
- Transcript: `recordings/lectures/15.md`, 00:00–13:05 (finishing the PPI Bayesian-network example),
  13:05–24:09 (distance metrics), 24:09–43:31 (hierarchical, K-means, fuzzy K-means, K-medoids),
  43:31–55:27 (DLBCL clustering and the random-signature caution), 55:27–1:02:51 (DREAM5 setup and
  p53 Bayesian-network reasoning, including the "explaining away" recap and the perturbation-vs-
  correlation argument), 1:04:58–1:09:21 (regression), 1:09:21–end (mutual information, ARACNe,
  MINDy). The opening Creative Commons/donation notice has been removed.
- Named but not contained in the supplied material: the "explaining away" wet-grass-and-sprinkler
  example was introduced in an earlier lecture and only recalled here; the Gerstein-lab PPI paper and
  the DREAM-challenge regression paper were referred to by the lecturer without a full citation; the
  head-to-head comparison of regression, Bayesian-network, mutual-information and consensus methods
  on the DREAM5 data was explicitly deferred to the next lecture.

---

[← 14. Predicting Protein Interactions](14-predicting-protein-interactions.md) · [Contents](index.md) · [16. Factor Graphs and Interactome Networks →](16-factor-graphs-and-interactome-networks.md)
