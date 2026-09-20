---
title: "9. Molecular Evolution and Phylogenetics"
course: "MIT 6047"
chapter: 9
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Molecular Evolution and Phylogenetics

## What this covers

This chapter reconstructs Lecture 18 of 6.047/6.878, on molecular evolution and phylogenetics,
from the lecture's slide deck alone — no transcript, notes, or problem set was supplied for this
lecture. It assumes the reader already knows what a multiple sequence alignment is and can read a
substitution matrix. The lecture sets up phylogenetics as a general inference problem, then works
through the first half of the standard pipeline: turning an alignment into a pairwise distance, and
turning a set of pairwise distances into a tree. The slide deck itself stops partway through — it
breaks off mid-way through describing neighbor-joining, before reaching the parsimony and
maximum-likelihood half of the course's own stated agenda; that gap is real and is flagged where it
occurs, and again in Sources.

## The general problem of phylogenetics

Darwin's 1859 illustration in *On the Origin of Species* — his only figure in the whole book —
expresses the idea in one phrase: "descent with modification." Three concepts do the work:
selection, heredity, and variation. A phylogeny is the attempt to recover the tree of descent from
what is visible today.

Phylogenetics generalizes far past biology: the "objects" being related can be species, genes, cell
types, diseases, cancers, languages, or car and building styles, and the "traits" used to relate
them can be morphological, molecular, gene-expression-based, or behavioural (word usage, for
example). The historical record used to anchor a tree also varies wildly in quality: fossils,
geological dating, "living fossils," ancient DNA, or written and painted records. This lecture
restricts to the modern case — reconstructing a tree using only data from extant (currently living)
species or genes — which produces **gene trees** relating orthologs, paralogs, and homologs, rather
than trees built directly from a fossil record.

### Traditional vs. modern traits

Before molecular data, phylogenies were built from morphology: a small number of traits (hoofs,
nails, teeth, horns), each assumed "well-behaved" — arising once in evolutionary history — which
justified a simple parsimony / Occam's-razor argument: prefer the tree explaining the traits with
the fewest independent origins.

Molecular phylogenetics inverts both assumptions. The traits are now every nucleotide and every
amino-acid residue in an alignment — a huge number, not a handful — and they are frequently
ill-behaved: with only 4 letters (or 20), the same character state arises independently at unrelated
positions and lineages constantly, and back-mutations (a site reverting to an earlier state) are
common. This is why naive parsimony no longer suffices and the course turns to explicit
probabilistic models of how a sequence position changes over time.

### Terminology

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A rooted binary tree labelling the root, an internal node, a branch, and the terminal nodes that carry the taxa">
  <line x1="160" y1="20" x2="90" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="20" x2="230" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="90" x2="55" y2="165" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="90" x2="125" y2="165" stroke="currentColor" stroke-width="1.5"/>
  <line x1="230" y1="90" x2="195" y2="165" stroke="currentColor" stroke-width="1.5"/>
  <line x1="230" y1="90" x2="265" y2="165" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="20" r="4" fill="currentColor"/>
  <circle cx="90" cy="90" r="3" fill="none" stroke="currentColor"/>
  <circle cx="230" cy="90" r="3" fill="none" stroke="currentColor"/>
  <circle cx="55" cy="165" r="3" fill="currentColor"/>
  <circle cx="125" cy="165" r="3" fill="currentColor"/>
  <circle cx="195" cy="165" r="3" fill="currentColor"/>
  <circle cx="265" cy="165" r="3" fill="currentColor"/>
  <text x="160" y="12" text-anchor="middle" font-size="12" fill="currentColor">root</text>
  <text x="40" y="95" text-anchor="end" font-size="12" fill="currentColor">internal node</text>
  <text x="230" y="45" text-anchor="start" font-size="12" fill="currentColor">branch</text>
  <text x="55" y="182" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="125" y="182" text-anchor="middle" font-size="12" fill="currentColor">B</text>
  <text x="195" y="182" text-anchor="middle" font-size="12" fill="currentColor">C</text>
  <text x="265" y="182" text-anchor="middle" font-size="12" fill="currentColor">D</text>
</svg>
<figcaption>Terminal nodes (A-D) are the observed taxa; internal nodes are hypothesised ancestors;
the single node at the top is the root; each connecting edge is a branch or lineage.</figcaption>
</figure>

- **Terminal nodes** carry the taxa being compared — genes, populations, species.
- **Branches or lineages** are the connecting edges.
- **Internal nodes (divergence points)** are hypothesized ancestors.
- **The root** is the most ancestral node of the whole tree.

Three tree types differ only in how much of this structure is filled in: a **cladogram** records
topology only; a **chronogram** adds divergence times at each node; a **phylogram** adds divergence
times *and* rates, so its branch lengths are drawn to scale (e.g. 3, 5, 1, 1, 1, 6 substitutions in
the deck's own example).

### Two routes into a tree

Given a set of aligned sequences, the course frames two strategies:

1. **Distance-based**: alignment $\to$ pairwise distance matrix $\to$ tree (this lecture's focus).
2. **Character-based**: alignment $\to$ tree directly, by scoring candidate trees against the
   alignment itself (parsimony or maximum likelihood) — named on the agenda slide but not reached
   in the supplied material.

## From alignments to distances: modelling sequence evolution

Turning an alignment into a distance requires a model of how a nucleotide changes over time —
otherwise the natural raw measure (fraction of mismatched sites) systematically *underestimates*
the true amount of change, because once enough time has passed some positions mutate more than
once, including flipping back to their original state:
$N_{\text{actual mutations}} > N_{\text{observed substitutions}}$.

The deck lists three levels at which "rate of evolution" can be measured, from crudest to most
refined:

- **nucleotide divergence** — a single uniform rate, i.e. overall percent identity;
- **transitions and transversions** — a two-parameter model, since purine$\leftrightarrow$purine and
  pyrimidine$\leftrightarrow$pyrimidine changes (A$\leftrightarrow$G, C$\leftrightarrow$T, the
  *transitions*) happen more often than the other four *transversions*;
- **synonymous vs. non-synonymous substitution** ($K_a/K_s$) — separating substitutions that do and
  do not change the encoded amino acid.

### A concrete random model

Before the general machinery, the deck works one specific example: start at nucleotide A; at each
time step, stay at the current letter with probability $0.7$ and switch to each of the other three
with probability $0.1$. Iterating gives the probability of being at each state over time:

| State | t=1 | t=2 | t=3 | t=4 | t=5 |
| --- | --- | --- | --- | --- | --- |
| A | 1 | 0.7 | 0.52 | 0.412 | 0.3472 |
| C, G, T (each) | 0 | 0.1 | 0.16 | 0.196 | 0.2176 |

At $t=2$, for instance, $P(A) = 0.7\times0.7 + 3\times(0.1\times0.1) = 0.52$: stay at A twice, or
leave and come back. The probability of being at any one letter is visibly drifting toward $1/4$ —
the process is forgetting its starting state.

### The general continuous-time formulation

Over an infinitesimal interval $\Delta t$, there isn't time for two substitutions to hit the same
site, so a transition matrix

$$S(\Delta t) = \begin{pmatrix} P(A|A,\Delta t) & \cdots & P(A|T,\Delta t) \\ \vdots & & \vdots \\ P(T|A,\Delta t) & \cdots & P(T|T,\Delta t) \end{pmatrix}$$

can be estimated directly. Assuming the process is a stationary (time-homogeneous) Markov chain
gives the multiplicative law

$$S(t+t') = S(t)S(t'), \qquad P(x\mid y, t+t') = \sum_z P(x\mid z,t)\,P(z\mid y,t'),$$

the Chapman-Kolmogorov relation: evolving for $t+t'$ is the same as evolving for $t$ then for $t'$.

**Jukes-Cantor** is the simplest instance: a single constant rate $\alpha$ for every substitution.
Over a short interval $\varepsilon$,

$$S(\varepsilon) = \begin{pmatrix} 1-3\alpha\varepsilon & \alpha\varepsilon & \alpha\varepsilon & \alpha\varepsilon \\ \alpha\varepsilon & 1-3\alpha\varepsilon & \alpha\varepsilon & \alpha\varepsilon \\ \alpha\varepsilon & \alpha\varepsilon & 1-3\alpha\varepsilon & \alpha\varepsilon \\ \alpha\varepsilon & \alpha\varepsilon & \alpha\varepsilon & 1-3\alpha\varepsilon \end{pmatrix},$$

and solving the recursion for arbitrary $t$ gives every entry in terms of two functions,

$$r(t) = \tfrac14\bigl(1+3e^{-4\alpha t}\bigr), \qquad s(t) = \tfrac14\bigl(1-e^{-4\alpha t}\bigr),$$

where $r(t)$ is the probability of no net change and $s(t)$ the probability of ending at any one
particular other base. Both approach $1/4$ as $t\to\infty$ — the chain saturates at the uniform
distribution, matching the drift seen in the worked example above.

**Kimura's model** relaxes the single-rate assumption by giving transitions their own rate $\alpha$
separate from transversions' rate $\beta$:

$$S(t) = \begin{pmatrix} r(t) & s(t) & u(t) & u(t) \\ s(t) & r(t) & u(t) & u(t) \\ u(t) & u(t) & r(t) & s(t) \\ u(t) & u(t) & s(t) & r(t) \end{pmatrix} \quad (\text{rows/columns } A,G,C,T),$$

with

$$s(t)=\tfrac14\bigl(1-e^{-4\beta t}\bigr), \qquad u(t) = \tfrac14\bigl(1+e^{-4\beta t}-e^{-2(\alpha+\beta)t}\bigr), \qquad r(t)=1-2s(t)-u(t).$$

(These equations are reproduced exactly as given in the slide deck; see Sources for a reliability
caveat on the deck's equations generally.)

### From substitution probability to distance

The naive distance between two aligned sequences $x^i, x^j$ is the observed mismatch fraction
$f$ — the fraction of sites $u$ with $x^i[u]\neq x^j[u]$. Under Jukes-Cantor this is corrected to an
estimate of the actual number of substitutions per site,

$$d_{ij} = -\tfrac34\log\!\left(1-\tfrac{4f}{3}\right),$$

which agrees with $f$ for small divergence but grows much faster as $f$ approaches its saturation
value of $3/4$ — beyond which two sequences look no more similar than chance. The deck's own worked
values: observed $f = 0.1,0.2,\dots,0.7$ corrects to $d = 0.11, 0.23, 0.38, 0.57, 0.82, 1.21, 2.03$
— nearly linear at first, then diverging.

### A hierarchy of models

The deck situates Jukes-Cantor and Kimura inside a family ordered by how many distinct substitution
rates are allowed, each further split by whether base frequencies are forced equal or left free:

| # substitution types | unequal base frequency | equal base frequency |
| --- | --- | --- |
| 4 (general) | GTR | SYM |
| 3 | TrN | K3ST |
| 2 | HKY85 / F84 | K2P |
| 1 | F81 | JC |

Analogous models exist for amino acids and codons.

## From distances to trees

A candidate tree $T$ with branch lengths implies its own pairwise leaf-to-leaf distance $M_{ij}$:
the sum of branch lengths on the path between $i$ and $j$. Given an observed distance matrix
$D_{ij}$ (built as above), the task is to find the tree whose implied distances best match it, for
instance by least squares:

$$\min_T \sum_{ij} (D_{ij}-M_{ij})^2.$$

The deck's own illustration writes each pairwise entry as a *concatenation of edge labels* rather
than a number (the human-dog entry appears as "h.z.x.d"), making visible that a tree distance is
literally a sum of lengths along a shared path.

Whether this minimization is easy depends on what kind of matrix $D$ is.

### Ultrametric distances

$D$ is **ultrametric** if for every triple $i,j,k$, the two largest of the three pairwise distances
are equal and the third is no larger — the deck states it as: relabel so that

$$d(i,j) \le d(i,k) = d(j,k).$$

If $i,j$ share a most recent common ancestor at depth $a$ below $k$'s point of divergence at depth
$b\ge a$, this reads $a+a \le a+b = a+b$. The consequence is strong: every leaf sits at the *same
total distance from the root* — a rooted tree with a constant, uniform rate of evolution along every
lineage (a strict molecular clock).

<figure>
<svg viewBox="0 0 260 210" role="img" aria-label="A three-leaf ultrametric tree in which the closer pair B and C merge before joining A, so every leaf sits the same distance from the root">
  <line x1="30" y1="180" x2="30" y2="85" stroke="currentColor" stroke-width="1"/>
  <line x1="26" y1="180" x2="30" y2="180" stroke="currentColor" stroke-width="1"/>
  <line x1="26" y1="120" x2="30" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="26" y1="90" x2="30" y2="90" stroke="currentColor" stroke-width="1"/>
  <text x="20" y="184" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <text x="20" y="124" text-anchor="end" font-size="11" fill="currentColor">1</text>
  <text x="20" y="94" text-anchor="end" font-size="11" fill="currentColor">1.5</text>
  <text x="30" y="75" text-anchor="middle" font-size="11" fill="currentColor">height</text>
  <line x1="70" y1="180" x2="70" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="180" x2="160" y2="120" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="180" x2="220" y2="120" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="120" x2="220" y2="120" stroke="currentColor" stroke-width="1.5"/>
  <line x1="190" y1="120" x2="190" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="70" y1="90" x2="190" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="70" cy="180" r="3" fill="currentColor"/>
  <circle cx="160" cy="180" r="3" fill="currentColor"/>
  <circle cx="220" cy="180" r="3" fill="currentColor"/>
  <circle cx="190" cy="120" r="3" fill="none" stroke="currentColor"/>
  <circle cx="130" cy="90" r="4" fill="currentColor"/>
  <text x="70" y="196" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="160" y="196" text-anchor="middle" font-size="12" fill="currentColor">B</text>
  <text x="220" y="196" text-anchor="middle" font-size="12" fill="currentColor">C</text>
  <text x="222" y="112" text-anchor="start" font-size="11" fill="currentColor">merge B,C at 1</text>
  <text x="132" y="80" text-anchor="middle" font-size="11" fill="currentColor">root at 1.5</text>
</svg>
<figcaption>Because d(B,C)=2 is smaller than d(A,B)=d(A,C)=3, B and C merge first at height 1 and A
joins at height 1.5, the root — every leaf ends up exactly 1.5 above the root, the defining property
of an ultrametric tree.</figcaption>
</figure>

Formally, given a symmetric, zero-diagonal $n\times n$ matrix $D$, an ultrametric tree for $D$ has
$n$ leaves (one per row/column); every internal node is binary and labelled with a time from $D$;
times strictly decrease along any root-to-leaf path; and for any two leaves $i,j$, their lowest
common ancestor is labelled exactly $D(i,j)$.

Real data is rarely exactly ultrametric — two otherwise identical matrices differing in a single
entry (a $B$-$C$ distance of 5 vs. 4, in the deck's example) is enough to break it. "Ultrametrifying"
a matrix uses a minimum spanning tree: build the complete graph on $n$ vertices with edge weight
$D(i,j)$; find its MST (Prim's algorithm, using the facts that a spanning tree has a unique path
between any two vertices, that adding any edge to it creates exactly one cycle, and that any edge on
that cycle can be dropped to restore a spanning tree); then set the corrected $D'(i,j)$ to the
*largest* edge weight on the unique MST path between $i$ and $j$.

### Additive distances

$D$ is **additive** if every quartet of taxa $i,j,k,l$ can be relabelled so that

$$d(i,j)+d(k,l) \le d(i,k)+d(j,l) = d(i,l)+d(j,k)$$

— the *four-point condition*. Writing the four pendant edges as $a,b,c,d$ and the internal
connecting edge as $m$, this reads $(a+b)+(c+d) \le (a+m+c)+(b+m+d) = (a+m+d)+(b+m+c)$. Additivity
is weaker than ultrametricity: it says only that the distances come from summing branch lengths
along *some* tree, with no constraint that lineages evolve at the same rate.

### General distances

In practice a distance matrix is neither, for two kinds of reasons: **noise** (distances are
measured, not exact, and the substitution model is itself an approximation) and genuine
**fluctuation** (the aligned region may be unrepresentative of the whole genome's history, gene
conversion or lateral transfer can replace one lineage's copy with another's, and mutation rates
vary across lineages). Building a tree from a noisy matrix then means choosing among: exhaustively
scoring every tree topology (correct in principle, computationally infeasible beyond a handful of
taxa), **neighbor-joining** (usually gives a good tree even off exact additivity), or **UPGMA**
(fast, but — as below — often gives a poor tree).

### UPGMA

UPGMA (Unweighted Pair Group Method with Arithmetic mean) is agglomerative clustering applied to
the distance matrix:

- **Initialize**: one cluster $C_i$ per sequence, each a leaf at height 0.
- **Iterate**: find the pair $C_i, C_j$ with minimal $d_{ij}$; merge into $C_k = C_i \cup C_j$;
  place the new internal node at height $d_{ij}/2$; delete $C_i, C_j$.
- **Terminate**: once two clusters remain, place the root at height $d_{ij}/2$ between them.

If the input distance is genuinely ultrametric, UPGMA is guaranteed to recover the correct tree: the
topology consistent with an ultrametric matrix is unique (given a binary tree), and UPGMA's
construction obeys the pairwise distances by design.

Its weakness is exactly the assumption that makes it correct: a strict molecular clock, meaning
every lineage evolves at the same rate. This is false whenever some lineages evolve unusually
fast — the deck names mouse and rat as the standard example — and UPGMA will then cluster by
*amount of change* rather than *true recency of common ancestry*, misplacing the fast-evolving
lineages in the tree.

### Neighbor-joining, as far as the deck reaches

Neighbor-joining is guaranteed correct when the distance is additive, and tends to perform well
even when it is not. Its first step identifies which pair of leaves is a true "cherry" (siblings in
the tree) using a corrected distance

$$D_{ij} = d_{ij} - (r_i+r_j), \qquad r_i = \frac{1}{|L|-2}\sum_k d_{ik},$$

where $r_i$ averages leaf $i$'s distance to every other leaf. The claim is that this correction is
exactly what is needed: $D_{ij}$ is minimized if and only if $i$ and $j$ are neighbors in the true
tree. The deck states the claim but defers its proof — "beyond the scope of this lecture" — to
Durbin, Eddy, Krogh and Mitchison's *Biological Sequence Analysis*, p. 189.

The supplied slide material ends here, one step into neighbor-joining. The deck's own agenda
promises parsimony and maximum-likelihood tree scoring (the "peeling algorithm") and a section on
the tree of life in the genomic era, and neither is present in what was supplied — see Sources.

## Sources

All content is drawn from a single input: the reconstructed slide deck for Lecture 18, "Molecular
Evolution and Phylogenetics,"
`computational-biology/mit-ocw/6047/lectures/18-slides.md` (6.047/6.878, MIT OCW, Fall 2015,
CC BY-NC-SA 4.0). No transcript, written notes, or problem set was supplied for this lecture.

- Darwin quote, tree-of-life motivation, Darwinian concepts (selection/heredity/variation): slides
  "Concepts of Darwinian Evolution" and "Tree of Life."
- General problem statement, objects/traits/historical-record examples, gene trees: slide
  "Phylogenetics."
- Terminology (terminal/internal nodes, branches, root): slide "Common Phylogenetic Tree
  Terminology."
- Traditional vs. modern traits, parsimony motivation: slide "From physiological traits to DNA
  characters"; molecular character table (kangaroo/elephant/dog/mouse/human): slide "Inferring
  Phylogenies: Traits and Characters."
- Cladogram/chronogram/phylogram: slide "Three types of trees." Two routes (distance-based vs.
  character-based): slides "Two basic approaches for phylogenetic inference" and the "Goals for
  today" agenda slides.
- Random substitution example table, $S(\Delta t)$, Chapman-Kolmogorov relation, Jukes-Cantor and
  Kimura matrices, distance-correction formula and worked $f\to d$ table, model hierarchy table:
  slides "'Evolving' a nucleotide under random model" through "Many nucleotide models have been
  developed."
- Least-squares tree-fitting criterion and symbolic distance-matrix example: slide "Distance
  matrix $\Leftrightarrow$ Phylogenetic tree."
- Ultrametric three-point condition, formal definition, worked A/B/C example, near-ultrametric
  matrix pair: slides "Ultrametric distances & 3 Point Condition" through "Ultrametric Matrix
  Construction," credited on the slides themselves to Ran Libeskind-Hadas's lecture slides
  (Fall 2013).
- MST facts and the ultrametrification algorithm: slides "Minimum Spanning Tree (MST)" and "The
  'Ultrametrification' Algorithm," also credited to Libeskind-Hadas.
- Four-point condition (additive distances) and the general-distances discussion (noise,
  fluctuation, algorithm choices): slides "Distances: (b) Additive distances" and "Distances: (c)
  General distances."
- UPGMA algorithm, its correctness argument, and its molecular-clock weakness: slides "Algorithms:
  (a) UPGMA," "Ultrametric Distances & UPGMA," "Weakness of UPGMA."
- Neighbor-joining setup and the deferred proof: slide "Algorithms: (b) Neighbor-Joining," which
  explicitly refers the reader to Durbin, Eddy, Krogh & Mitchison, *Biological Sequence Analysis*,
  p. 189 — not itself supplied here.

**Referred to but not contained in the supplied material**: the deck's agenda (repeated twice)
promises a section on alignment-based tree scoring — parsimony (greedy union/intersection vs.
dynamic-programming cost-summing) and maximum-likelihood/MAP inference via the "peeling algorithm"
— and a closing section on the tree of life in the genomic era (the prokaryotic problem, horizontal
gene transfer, interpreting a "forest of life"). Neither appears in the supplied slide file, which
ends partway through describing neighbor-joining. Several slides also reference images removed for
copyright (an archosaur/dinosaur/bird phylogeny, a mammal family tree, a UPGMA-vs-correct-tree
comparison figure) that are not reconstructable from the text.

**Reliability note**: the source markdown is itself flagged by its own conversion metadata as
machine-reconstructed from a PDF with no text layer, with "every equation... unverified." The
equations above are reproduced as given, not independently checked against a primary source.

---

[← 8. Evolutionary Signatures for Genome Annotation](08-evolutionary-signatures-for-genome-annotation.md) · [Contents](index.md) · [10. Disease Epigenomics and Genetic Epidemiology →](10-disease-epigenomics-and-genetic-epidemiology.md)
