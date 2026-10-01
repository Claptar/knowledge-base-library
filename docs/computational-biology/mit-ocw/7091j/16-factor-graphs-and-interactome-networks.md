---
title: "16. Factor Graphs and Interactome Networks"
course: "MIT 7.091J"
chapter: 16
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Factor Graphs and Interactome Networks

## What this covers

The previous lectures built a toolbox for inferring a gene regulatory network from expression data
alone: mutual information, regression, Bayesian networks. This chapter opens by asking how well that
toolbox works once the data are real, and the answer forces a change of strategy. It then builds two
of the main responses: **factor graphs**, through the PARADIGM model, which reasons explicitly about
every regulatory step between a gene copy and a pathway's activity; and **interactome graphs** — the
large protein-protein interaction networks, and the algorithms (shortest paths, clustering,
prize-collecting Steiner trees) used to pull a focused, interpretable piece out of them. It assumes
the Bayesian-network and mutual-information material from the previous lectures, and the
gold-standard interaction-scoring approach from the protein-protein interaction lecture.

## How well does network inference actually work?

The DREAM challenge gave the community unlabeled expression data — synthetic (*in silico*)
data, and real data from *E. coli*, *S. cerevisiae*, and *S. aureus* — and asked people to
reconstruct the regulatory networks blind. Methods clustered into families (Bayesian networks,
regression, mutual information, a grab-bag of others, "meta" methods combining several families, and
a "community" prediction combining everything), scored by area under the precision-recall curve. The
picture worsens sharply as the data get more real: on *in silico* data the families are all roughly
level; on *E. coli* the best performer reaches under 10% of the achievable optimum, and Bayesian
networks do noticeably worse than the rest; on *S. cerevisiae* — the organism most of these
algorithms were originally developed and tuned on — results are, in the lecture's word, "terrible":
single-digit percentages for every method, with the community prediction no better than the
individual ones.

The explanation is in the data, not the algorithms: every method looks for the same signature,
a regulator whose own expression rises or falls together with its targets'. Plotting correlation
between unrelated gene pairs, pairs co-regulated by the same factor, and true regulator/target pairs
shows a clean separation between the three in the *in silico* data, a smaller one in *E. coli*, and
almost none in yeast — the signature the methods detect is barely there. So expression data are
powerful for classification and clustering but, alone, not sufficient to recover which regulators
caused a cluster of genes to move together — at least not in yeast, and there is every reason to
expect humans would be no better.

## Why mRNA levels do not predict protein levels

If expression correlation alone cannot identify regulators, the question is where the chain from
gene to protein breaks down. A 2009 study comparing microarray mRNA data to protein levels found a
trend ($R^2 \approx 0.22$) but a **1,000-fold spread** in protein concentration at any fixed mRNA
level — not a microarray artifact, since a careful 2012 study repeating the comparison with RNA-seq
and several ways of calling protein abundance from mass spectrometry got, at best, a correlation of
about $0.54$.

The reason: mRNA level is only one of several processes setting protein level. Translation happens at
its own, separately regulated rate, and mRNA and protein are each degraded at rates that can
themselves be regulated — and turn out to be essentially uncorrelated with each other. A 2011 study
measured this directly, labeling newly synthesized RNA and protein to recover half-lives rather than
steady-state abundance alone: protein half-lives span at least three orders of magnitude, abundance
spans from about $10^2$ to $10^8$ copies per cell, and protein and RNA degradation rates show no
correlation. Once a model includes translation rate and both degradation rates, RNA level accounts
for only about 40% of the variance in protein level — translation rate contributes more. Only
knowing the stability of every individual RNA and protein lets you predict protein level well from
RNA level; without it, you cannot.

This leaves two strategies for building regulatory models: look upstream of RNA synthesis, inferring
which transcription factors were active from changes in RNA (the subject of the course's later
epigenomic-data lecture), or stop treating "RNA up $\Rightarrow$ protein up $\Rightarrow$ pathway
active" as one step and instead model every regulatory step explicitly — the approach this chapter
turns to next.

## PARADIGM: modeling every regulatory step explicitly

PARADIGM keeps gene copy number, expression state (mRNA), protein level, and protein *activity* as
four distinct variables, connected by explicit regulatory steps — transcriptional regulation,
translational regulation and protein degradation, intracellular/extracellular signaling — rather
than one variable standing in for the whole chain. Protein level and activity are kept separate
because a kinase's activity depends on whether it has been phosphorylated, not just on how much of
it is present — exactly the step collapsed by a model that goes straight from expression to inferred
pathway state. Developed for cancer genomics, the inputs are array/SNP data for copy number and
microarray or RNA-seq for transcript level; the output is an estimate of how active a known pathway
is in a given sample.

### Factor graphs and belief propagation

The representation is a **factor graph**: a bipartite graph of *variables* (circles) and *factors*
(squares), with an edge between a variable and a factor exactly when that variable is an argument of
the factor's function. A Bayesian network is a special case: three variables connected directly
become, in a factor graph, a factor node sitting between them. The point is that the joint
probability over every variable factors into a product of terms, each depending only on the small
set of variables it touches. In PARADIGM each variable takes one of three states: **activated**,
**nominal**, or **deactivated**.

The goal is to compute marginal probabilities efficiently — e.g. the probability a pathway is active,
summed over every setting of every other variable. Computed directly this needs an exponential sum;
the factor graph makes it efficient when the graph is a tree: redraw it with the variable of
interest as the root, and compute from the leaves upward.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="A factor graph redrawn as a tree, with messages accumulating from the leaves up to the root variable">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="60" cy="200" r="16" fill="none" stroke="currentColor"/>
  <text x="60" y="204" text-anchor="middle" font-size="12" fill="currentColor">y1</text>
  <rect x="112" y="184" width="28" height="28" fill="none" stroke="currentColor"/>
  <text x="126" y="202" text-anchor="middle" font-size="11" fill="currentColor">fE</text>
  <circle cx="200" cy="200" r="16" fill="none" stroke="currentColor"/>
  <text x="200" y="204" text-anchor="middle" font-size="12" fill="currentColor">y2</text>
  <rect x="222" y="184" width="28" height="28" fill="none" stroke="currentColor"/>
  <text x="236" y="202" text-anchor="middle" font-size="11" fill="currentColor">fD</text>
  <line x1="76" y1="195" x2="112" y2="195" stroke="currentColor"/>
  <line x1="216" y1="195" x2="222" y2="195" stroke="currentColor"/>
  <line x1="140" y1="190" x2="190" y2="130" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="236" y1="184" x2="195" y2="130" stroke="currentColor" marker-end="url(#arrow)"/>
  <circle cx="190" cy="115" r="18" fill="none" stroke="currentColor"/>
  <text x="190" y="119" text-anchor="middle" font-size="12" fill="currentColor">x3</text>
  <rect x="172" y="60" width="28" height="28" fill="none" stroke="currentColor"/>
  <text x="186" y="78" text-anchor="middle" font-size="11" fill="currentColor">fC</text>
  <line x1="190" y1="97" x2="186" y2="88" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="200" y1="74" x2="230" y2="35" stroke="currentColor" marker-end="url(#arrow)"/>
  <circle cx="240" cy="22" r="18" fill="none" stroke="currentColor"/>
  <text x="240" y="26" text-anchor="middle" font-size="12" fill="currentColor">x1</text>
  <text x="186" y="150" text-anchor="middle" font-size="11" fill="currentColor">summary wrt x3</text>
  <text x="222" y="55" text-anchor="middle" font-size="11" fill="currentColor">summary wrt x1</text>
</svg>
<figcaption>Each vertex waits for messages from all its children before sending its own message
up. A variable node sends the product of its children's messages; a factor node sends the
"summary" of the product of its children's functions, taken with respect to the parent.</figcaption>
</figure>

The computation is organized as **messages** flowing from leaves to root: each vertex waits to hear
from all of its children before sending a message to its parent. A **variable node** sends up the
product of its children's messages. A **factor node** sends up the "summary" of the product of its
children's functions — the lecture's name for what the sum-product literature calls the "not-sum":
the sum over every variable *except* the one the message is headed toward. This is purely a
definition that lets the marginal $\sum_{x_2}\sum_{x_3}\sum_{x_4}\sum_{x_5}(\text{global function at
}x_1=a)$ be rewritten as a nested product of summaries. Edges carry no direction, so the tree can be
re-rooted at any variable and the same leaves-up procedure computes its marginal. Doing this
separately for every variable is wasteful; the **sum-product (belief propagation) algorithm**
computes all the marginals at once, reusing the same messages — the details are left to the cited
paper and not re-derived in the lecture.

### Building the factors by hand

Encoding a known pathway as a factor graph is currently manual (or semi-manual): convert the pathway
to a graph, label each edge positive (activating) or negative (repressing), and define a factor at
each node around an **expected state** — a majority vote of the parents, where a parent on a positive
edge votes its own state and one on a negative edge votes the negative of its own state. A vote of
zero abstains; no votes gives expected state zero; a tie resolves to $-1$, weighting repressors and
deletions more heavily. The factor is then

$$\phi_i(x_i, \mathrm{Parents}(x_i)) = \begin{cases} 1-\epsilon & x_i \text{ is the expected state from } \mathrm{Parents}(x_i) \\ \epsilon/2 & \text{otherwise} \end{cases}$$

with $\epsilon = 0.001$. The same mechanism extends beyond majority vote: an edge labeled "minimum"
gives an AND-like vote equal to the minimum of its variables (e.g. formation of a protein complex, active
only when every component is); an edge labeled "maximum" gives an OR-like vote equal to the maximum
(e.g. a gene family, active if any member is). Compared with a plain Bayesian network over the same
variables, the factor graph lets the regulatory step itself — transcription, translation, complex
formation, family membership — sit as an explicit, inspectable node, rather than being folded
invisibly into one conditional probability table. The joint probability of the whole graph is the
normalized product of all these factors,

$$P(X) = \frac{1}{Z}\prod_{j=1}^m \phi_j(X_j), \qquad Z = \prod_j \sum_{S \sqsubseteq X_j} \phi_j(S),$$

with $S \sqsubseteq X_j$ ranging over settings of the variables in factor $j$. Parameters not fixed by
hand are estimated by expectation-maximization from data, as in the earlier Bayesian-network
lectures — the graph's structure is imposed from known biology, not learned. Given a fully specified
graph $\Phi$ and data $D$, the marginal and likelihood are

$$P(x_i = a \mid \Phi) = \frac{1}{Z}\prod_{j=1}^m \sum_{S \sqsubseteq A_i(a)\, X_j} \phi_j(S), \qquad
P(x_i = a, D \mid \Phi) = \frac{1}{Z}\prod_{j=1}^m \sum_{S \sqsubseteq A_i(a)\cup D\, X_j} \phi_j(S),$$

where $A_i(a)$ denotes the constraint $x_i = a$. To decide whether a pathway is active, PARADIGM
compares the likelihood of the data under "active" against "not active," via a log-likelihood ratio:

$$L(i,a) = \log\!\left(\frac{P(D \mid x_i = a, \Phi)}{P(D \mid x_i \ne a, \Phi)}\right).$$

### A worked example

The lecture's toy examples: MDM2 inhibits TP53, and TP53 activates apoptosis, with each of MDM2 and
TP53 represented by its own chain of factors (DNA, mRNA, protein, active protein) feeding the shared
apoptosis node. In a second example, PAK2 represses MYC/MAX, which activates two downstream genes and
represses a third. Given copy-number, methylation, and expression data showing the two activation
targets active, the repression target repressed, but the third (expected-active) target *not*
active, the model infers MYC/MAX is active anyway, explaining away the inconsistent target by a
difference in its epigenetic state. Belief propagation then carries that inferred state back up the
graph, updating the inferred activity of the upstream repressor, PAK2.

## From known pathways to interactome graphs

PARADIGM reasons over pathways already known and manually encoded. The complementary question is
whether high-throughput data can suggest pathways nobody has annotated — and for that the lecture
turns to **interactome graphs**: very large networks built from protein-protein interaction data
(two-hybrid, affinity-capture mass spectrometry, genetic screens) or other large-scale relationships
such as co-expression. A graph here is vertices (proteins) and edges, undirected (e.g. two-hybrid,
where there's no telling which protein "did" what to the other) or directed (e.g. "this kinase
phosphorylates this target"), possibly weighted by confidence. Useful vocabulary: *degree* (edges
touching a node), *path* (a sequence of vertices connecting two nodes without retracing steps), and
*path length* (edge count, or sum of edge weights if weighted) — naturally represented as an
**adjacency matrix**, a form computer science already has fast algorithms for.

### Scoring confidence, and why shortest path is most probable path

Assigning confidence weights to interaction edges was covered earlier, using Bayesian networks
trained against gold standards (Jansen et al.: separate naive-Bayes classifiers combine mRNA
co-expression, GO process, MIPS function, and essentiality into a probabilistic interactome, then
combined with classifiers over pull-down and two-hybrid data). That works where gold standards
exist — more often yeast than mammalian data, where databases are larger and gold standards scarcer,
so scores tend to be more ad hoc. PSICQUIC/PSISCORE is one standardized route: a common exchange
format pools data from many interaction databases, traceable to the underlying experiment, then
scored by a chosen server (e.g. co-expression, functional similarity, or explanation via known
domain-domain interactions). The MIscore algorithm scores an interaction from the number of
supporting publications, the experimental method, and the annotated interaction type, each a $[0,1]$
score combined with adjustable weights,

$$S_{MI} = \frac{K_p S_p(n) + K_m S_m(cv) + K_t S_t(cv)}{K_p + K_m + K_t}.$$

Once every edge carries a confidence, set its weight to $-\log P_{ij}$. Since total path length is
then a sum of $-\log$ probabilities, the shortest path between two nodes simultaneously *maximizes*
the product of edge probabilities along it — the most probable physical route between them. Standard
shortest-path algorithms thus double as most-probable-path algorithms at no extra cost. Example: a
sequence-specificity scan against kinase motifs typically implicates a whole *family* of kinases for
a phosphorylation site; among family members matching the sequence equally well, the one directly or
closely connected to the target in the physical network is the more likely true regulator — turning
"which specific kinase" into a most-probable-path question once there are many candidates to check.

## Using network position to annotate unknown proteins

Many genes in well-studied genomes have no known function, and nodes close together in an
interaction network tend to be functionally similar (measured, where function is known, by higher
semantic similarity at shorter network distance). The direct approach — copy the annotation of a
node's $k$ nearest neighbors — breaks down once the neighborhood is mixed: two unknown nodes with
identical neighbor sets might still plausibly belong with different parts of it.

A better-behaved formulation treats each annotation separately: set nodes known to carry it to $+1$,
nodes known not to (or unknown) to $-1$, and choose each unknown node's setting to maximize the sum,
over its neighbors, of the product of its own setting and each neighbor's. Iterating to convergence
is a local optimization, not guaranteed to reach the global optimum: if three nodes A, B, C would all
plausibly carry an annotation together, flipping any one alone can fail to help — or make things
worse — even though flipping all three together would. Since no single local move helps, local
search gets stuck; recovering the global optimum calls for the same remedy used earlier in the course
for side-chain placement: **simulated annealing**, accepting a worse move with a probability
depending on how much worse it is, letting the search climb over a local barrier.

## Finding modules in a large graph

A **topological module** is a locally dense part of the graph, with more edges among its own nodes
than to the rest; a **functional module** is a region with a high density of nodes sharing a specific
function or activity. Two clustering approaches:

**Edge betweenness clustering** asks, for every edge, how many all-pairs shortest paths pass through
it. An edge that is the sole connection between two otherwise-separate clusters has very high
betweenness, since every shortest path crossing the two sides must use it; an edge inside a dense
cluster typically has low betweenness. The algorithm repeatedly removes the highest-betweenness edge
and recomputes, progressively pulling the graph apart into its more internally-connected pieces.

**Markov clustering** exploits random walks: starting on one side of the network, a walker is far
more likely to stay there than to wander across to a distant part of the graph. Made precise: the
$n$-th power of the adjacency matrix counts, for every pair of nodes, the number of paths of length
$n$ between them (the first power counts direct edges). Normalizing each column to sum to 1 turns it
into a **transition matrix** — a one-step move probability — whose higher powers give the probability
of moving between nodes in a given number of steps. Repeated multiplication alone blurs rather than
sharpens the partition, so Markov clustering adds an **inflation operator**: raise each entry to a
power $r$ and renormalize each column, exaggerating the spread (the lecture's example: $0.9$ and
$0.1$, squared and renormalized, move toward roughly $0.99$ and $0.01$). Starting from the graph with
self-loops added (so a walker can stay put), the algorithm alternately multiplies and inflates until
the matrix stops changing, leaving sharp partitions — used, for example, to cluster proteins by BLAST
similarity into families (catching relationships a single best hit, dominated by one shared domain,
would miss) and to cluster genes by expression correlation across tissues.

However a cluster is found, assigning it a function, when its members carry several different
annotations, is a job for the hypergeometric distribution used earlier in the course for
over-representation testing.

## Finding the subnetwork relevant to your data

A harder, more specific problem: given a list of proteins implicated in one condition, find the part
of the interactome connecting them that is plausibly relevant — the **active subgraph** problem. The
naive approach, connecting the hits by shortest paths, tends to produce "hairballs": since the
interactome is mostly one connected component with both false positive and false negative edges, even
a small, clean hit list can be connected by a subgraph of hundreds or thousands of nodes — one cancer
example in the lecture started from a small hit list whose shortest-path network came out almost as
large as the interactome itself.

The **prize-collecting Steiner tree** addresses this directly. (The name is from telecommunications:
wiring customers together can be cheaper through one shared, unconnected junction — a Steiner node —
than by a direct wire between every pair.) Every node with supporting data gets a *prize*, larger the
more confident the data; every edge gets a *cost*, lower for higher-confidence interactions. The
optimization balances the two:

$$\sum_{v \notin T} \beta \cdot \mathrm{penalty}(v) + \sum_{e \in T} \mathrm{cost}(e),$$

minimizing the penalty paid for every supported node left *out* of the tree $T$ plus the cost paid
for every edge included — so a node is connected only if its prize outweighs the cost of reaching it,
letting probable false positives be dropped instead of forcibly connected.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A Steiner node lets several terminals connect through one shared junction instead of pairwise, trading edge cost against the prize for including each terminal">
  <circle cx="60" cy="40" r="14" fill="none" stroke="currentColor"/>
  <text x="60" y="44" text-anchor="middle" font-size="11" fill="currentColor">A</text>
  <circle cx="280" cy="40" r="14" fill="none" stroke="currentColor"/>
  <text x="280" y="44" text-anchor="middle" font-size="11" fill="currentColor">B</text>
  <circle cx="170" cy="190" r="14" fill="none" stroke="currentColor"/>
  <text x="170" y="194" text-anchor="middle" font-size="11" fill="currentColor">C</text>
  <circle cx="170" cy="100" r="12" fill="none" stroke="currentColor" stroke-dasharray="3,2"/>
  <text x="170" y="104" text-anchor="middle" font-size="10" fill="currentColor">S</text>
  <line x1="72" y1="48" x2="160" y2="95" stroke="currentColor"/>
  <line x1="268" y1="48" x2="180" y2="95" stroke="currentColor"/>
  <line x1="170" y1="112" x2="170" y2="176" stroke="currentColor"/>
  <line x1="70" y1="52" x2="270" y2="52" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="2,3"/>
  <line x1="65" y1="52" x2="165" y2="180" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="2,3"/>
  <text x="170" y="215" text-anchor="middle" font-size="11" fill="currentColor">terminals A, B, C have prizes; Steiner node S has none, only cost to reach it</text>
</svg>
<figcaption>Connecting three terminals through one shared Steiner junction (solid lines) costs
fewer edges than wiring every pair directly (faint dashed lines); the prize-collecting
formulation lets the algorithm drop a terminal instead of paying for an expensive edge to it.</figcaption>
</figure>

Solving it exactly is computationally demanding (integer linear programming, at considerable
memory cost, or signal/message-passing), but the payoff is that a hairball of thousands of edges
reduces to a compact, clusterable subnetwork enriched for recognizable processes (e.g. DNA damage,
cell cycle, in a cancer-derived network). In one example, Steiner nodes with no direct experimental
support but central to the network had a high probability of being validated cancer drug targets when
tested directly (ranks under 27 out of 11,637 candidates were far more often true hits than nodes
ranked in the low hundreds to thousands). Interactome graphs also give a natural way to combine data
types that otherwise do not line up — an RNA node, a transcription factor inferred from epigenomic
data, and protein-protein interaction edges can sit in the same Steiner tree, recovering a physical
link between a changing transcript and the pathway above it even though RNA and protein barely
correlate.

A related approach, used for a pheromone-response test case (perturbing Ste5), instead asked for the
network maximizing the product of path reliabilities between the perturbed gene and its
differentially-expressed targets, formulated as a minimum-cost-flow problem with edge cost
$f_{ij}\cdot(-\log P_{ij})$ — the same probability-multiplies/$-\log$-adds idea used for shortest-path
scoring above. Restricting paths to length 3 gave a 193-node, 778-edge network; the flow-based
reliability approach instead gave a much more compact 49-node, 96-edge network, significantly
enriched for the pheromone response pathway ($p < 10^{-18}$).

## When different omics disagree

The disagreement is not limited to mRNA versus protein. Across 156 yeast perturbation experiments
with both genetic (knockout) and transcriptional data, differentially expressed genes and genetic
hits overlap far less than chance would predict — in one case (DNA damage via MMS), 198 genes were
differentially expressed and 1,448 were genetic hits, with only 43 in both. Genetic data across these
156 perturbations were enriched for transcriptional regulation and signal transduction; expression
data for metabolic processes.

The explanation: genetic hits tend to be **master regulators** — e.g. DNA-damage sensors that signal
to the nucleus and arrest the cell cycle — kept at a fairly constant, low level and regulated
post-translationally, so knocking them out has a large phenotypic effect with little expression
change. Differentially expressed genes tend to be **effectors** — e.g. DNA repair enzymes — turned on
only under the relevant condition but often redundant, so knocking any one out has little effect
despite its expression clearly changing. The lecture's analogy: a smoke detector is on all the time
and does not change with conditions, but losing it is serious; a sprinkler only comes on during a
fire, but there are enough that losing one hardly matters. Both sit on the same underlying pathway,
and reconstructing it needs both kinds of data layered onto an interaction network, not either
alone.

## Putting it together

The lecture closes by placing the methods covered across these lectures along two axes: whether a
system's components are already known or unknown, and whether the relationships sought are physical
or statistical.

| | Known components | Unknown components |
|---|---|---|
| **Physical relationships** | differential equations, Boolean logic, decision trees | interactome models |
| **Statistical relationships** | Bayesian networks | mutual information, regression, clustering |

Mutual information, regression, and clustering are cheap to run genome- or proteome-wide with no
external data, but only establish statistical association, with no guarantee of a functional link.
Bayesian networks are somewhat more causal, but need substantial intervention data to be reliably so,
and performed poorly in the DREAM comparison. Interactome models — most of this chapter — establish
physical relationships and work well across large omic datasets, but need the interactome itself as
external data, so only work where that exists; and the subgraph or Steiner tree they produce says
nothing about what happens under perturbation, only that the nodes belong together. Quantitative
questions about perturbation — does inhibiting a node activate or repress the downstream process —
are left to logic-based, differential-equation, and related models, which is where the next lecture
(signaling network modeling) picks up.

## Sources

- Transcript `recordings/lectures/16.md`, 00:00–16:13: DREAM challenge method comparison (no slide
  for this lecture covers it); 08:38–14:02: mRNA/protein correlation studies (de Sousa Abreu et al.
  2009; Ning et al. 2012; an unnamed 2011 RNA/protein-labeling study), motivating PARADIGM.
- Slides `01-messages-flow-up-from-leaves.md`, `02-mdm2-tp53-apoptosis.md`, `03-a.md` with transcript
  16:13–37:17: factor graphs and belief propagation/sum-product (Kschischang, Frey & Loeliger 2001),
  PARADIGM (Vaske et al. 2010), the G/E/T/P/A variable set (Goldstein et al. 2013).
- Slide `05-a-bayesian-networks-approach-for-predicting-protein-protein.md` with transcript
  37:17–48:28: interaction-confidence scoring (Jansen et al. 2003), PSICQUIC/PSISCORE and MIscore
  (Aranda et al. 2011), topological vs. functional modules (Barabási, Gulbahce et al. 2011), and the
  kinase-target distance problem.
- Transcript 48:28–1:01:39: network-based function annotation, local optimization, simulated
  annealing, edge betweenness clustering, Markov clustering.
- Slide `05-...` (Steiner tree panels) with transcript 1:01:39–1:12:53: active subgraphs, hairballs,
  the prize-collecting Steiner tree and drug-target validation example (Huang, Clarke et al. 2013).
- Slides `06-approach.md`, `07-for-156-perturbations.md` with transcript 1:12:53–1:20:19:
  genetic-vs-expression disagreement, master regulators vs. effectors, the Ste5 test case and
  minimum-cost-flow network (from "Bridging high-throughput genetic and transcriptional data reveals
  cellular responses to alpha-synuclein toxicity," *Nature Genetics*, 2009; edge probabilities per
  Myers et al., *Genome Biology*, 2005, and Jansen et al. 2003), and the closing summary table.
- Named but not supplied: the DREAM challenge's own publication (discussed in the transcript, but no
  DREAM slide or paper was given for this lecture); the upcoming epigenomic-data lecture (Professor
  Gifford) and signaling-network-modeling lecture (Professor Lauffenburger), both referred to but not
  given here.

---

[← 15. Clustering and Inferring Regulatory Networks](15-clustering-and-inferring-regulatory-networks.md) · [Contents](index.md) · [17. Logic Models of Cell Signaling →](17-logic-models-of-cell-signaling.md)
