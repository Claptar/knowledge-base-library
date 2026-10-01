---
title: "17. Logic Models of Cell Signaling"
course: "MIT 7.091J"
chapter: 17
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Logic Models of Cell Signaling

## What this covers

This chapter asks how to turn the kind of circuit diagram every cell-signaling paper draws —
arrows from receptors to kinases to transcription factors — into something you can actually
calculate with: fit to data, use to predict a new experiment, and use to compare one cell type
against another. It assumes you already know what a signaling pathway is (receptors, kinases,
phosphorylation, transcription factors) and have seen the idea of fitting a model to data while
penalizing complexity; it does not assume you have seen logic (Boolean) modeling before, and
builds the formalism from scratch. The guest lecturer was Doug Lauffenburger, working through a
specific published case study: logic modeling of growth-factor and cytokine signaling in primary
versus tumor liver cells (Saez-Rodriguez, Morris et al.).

## The problem: a circuit diagram is not a model

Mammalian cell behavior — proliferation, death, the cytokines a cell secretes — is controlled by
what the cell sees in its environment: growth factors, hormones, extracellular matrix, mechanical
forces, cell-cell contacts. These cues are read by cell-surface receptors and propagated through
cascades of mostly enzymatic reactions — kinases adding and removing phosphate groups, some
protein-protein docking, some second messengers — that ultimately govern gene expression,
metabolism and the cytoskeleton. Understanding a phenotype means understanding this network of
pathways operating together, not any one pathway in isolation.

A motivating observation for working at the protein-pathway level rather than the gene level:
gene-sequencing of patient tumors (the lecture's example was pancreatic cancer) shows dozens of
mutations per tumor, and the specific mutations are mostly different from one patient to the next.
Matched gene-for-gene, two patients' tumors look unrelated. But the mutations tend to land in the
same small number of signaling and cell-cycle pathways — two patients with entirely different
point mutations can both have the TGF-$\beta$ pathway dysregulated. Pathways, not individual genes,
are where disparate genomic lesions converge on a common functional consequence, which is why it
is worth modeling at the level of protein activity in pathways even before the genomic story is
understood.

The standard picture for this — ligands at the top, receptors and kinases in the middle,
transcription factors at the bottom, all wired together like a circuit board — is a genuinely
useful metaphor, but by itself it supports no calculation. It is wiring with no behavior: nothing
in the picture tells you what the circuit does, let alone what prediction it makes or how it would
respond to an inhibitor. The goal of logic modeling is to turn that picture into an *actionable*
model: something you can fit to data, use to predict new data, and use to generate and test a
biological hypothesis.

Where does such a formalism sit, mathematically? At one extreme, if every component and rate
constant were known, you could write differential equations for the dozens of interacting species
and predict their dynamics — but for most of the pathway complexity underlying real cell behavior,
that much mechanistic knowledge simply does not exist. At the other extreme, large data sets
(sequencing, transcriptional profiles) are analyzed by multivariate regression, clustering, mutual
information — methods that find statistical associations without requiring a theory of mechanism.
Logic modeling sits between these: it needs less prior knowledge than a differential-equation model
but produces more than a statistical association. One property that recommends it in particular:
the same formalism can be run in a *theory-driven* mode — write down a logic model from what you
believe about who influences whom, then test it against data — or in a *data-driven* mode — start
from large data sets with no assumed structure and fit a logic model that reproduces them. The
case study below is, in effect, a hybrid: start from whatever prior-knowledge wiring diagram you
have, admit it is incomplete or wrong in detail, and let data correct it.

## Where the prior knowledge comes from, and why it disagrees with itself

Before any logic can be assigned, you need a scaffold: a graph of which molecular species are
plausibly connected to which. Two complementary kinds of database supply this.

- **Pathway databases** organize a few hundred literature-curated gene products into pathways,
  with upstream/downstream relationships based on biological knowledge — they assert functional
  order, not necessarily physical contact.
- **Interactome databases** record evidence of direct physical association (yeast two-hybrid,
  mass spectrometry, literature curation) — they assert "these two touch," without necessarily
  saying who is upstream of whom.

A pointed finding from comparing six or seven such databases for signaling downstream of
receptors: their overlap is very small. Most of the information in any one database is
non-redundant with the others — coloring nodes by which single database contains them shows large
swaths that appear in only one of the six, and an exceedingly small core present in all of them.
This was described as a genuine surprise. The underlying reason is that these databases pool
evidence across very different contexts — different cell types, species, treatment conditions,
mutations — so an edge present in one and absent in another may not actually be in conflict; it may
simply have been observed in a lymphocyte versus a hepatocyte versus a cardiac myocyte. A
cell-type- and condition-specific scaffold would be far smaller and more reliable, but it mostly
does not exist pre-assembled.

A second caution concerns a popular idea in network biology: that purely topological properties of
such a graph — a highly connected node must be more important, more likely to be disease-relevant —
carry biological meaning. This idea is appealing but, in the lecturer's assessment, has thin
experimental support; whether it is actually true is treated as an open question rather than a
working assumption.

The consequence drawn from both points is that a database-derived scaffold is only a *starting
point* — a hypothesis about what might be going on — and by itself supports no calculation. It
has to be mapped against empirical data from the actual cell type and conditions under study
before it earns any confidence.

## From a wiring diagram to Boolean logic

The move that turns the diagram into a model is to replace each node's inputs with a Boolean logic
gate. A conceptual diagram typically shows signed arrows — $a$ and $b$ both activate $e$, $b$
inhibits $f$, $c$ activates $f$, and there is an inhibitory feedback from $g$ back to $a$ — and the
modeling step is to decide, for every node, how its inputs combine: is it the AND of its
activators, the OR, is one input a NOT that blocks activation by another? Concretely, the example
used in lecture reads as: $e$ turns on only when *both* $a$ and $b$ are on (AND), while $f$ turns
on when $c$ is on *and* $b$ is off (AND-NOT).

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A signed interaction diagram converted into Boolean AND and AND-NOT gates, with an inhibitory feedback arc">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 6,3 0,6" fill="currentColor"/>
    </marker>
    <marker id="tee" markerWidth="8" markerHeight="10" refX="4" refY="5" orient="auto">
      <line x1="4" y1="0" x2="4" y2="10" stroke="currentColor" stroke-width="2"/>
    </marker>
  </defs>
  <circle cx="50" cy="40" r="16" fill="none" stroke="currentColor"/>
  <text x="50" y="44" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <circle cx="50" cy="110" r="16" fill="none" stroke="currentColor"/>
  <text x="50" y="114" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <circle cx="50" cy="180" r="16" fill="none" stroke="currentColor"/>
  <text x="50" y="184" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <circle cx="230" cy="60" r="16" fill="none" stroke="currentColor"/>
  <text x="230" y="64" text-anchor="middle" font-size="12" fill="currentColor">e</text>
  <circle cx="230" cy="160" r="16" fill="none" stroke="currentColor"/>
  <text x="230" y="164" text-anchor="middle" font-size="12" fill="currentColor">f</text>
  <circle cx="330" cy="110" r="16" fill="none" stroke="currentColor"/>
  <text x="330" y="114" text-anchor="middle" font-size="12" fill="currentColor">g</text>
  <line x1="64" y1="46" x2="214" y2="62" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="64" y1="104" x2="214" y2="66" stroke="currentColor" marker-end="url(#arrow)"/>
  <text x="140" y="42" text-anchor="middle" font-size="11" fill="currentColor">AND</text>
  <line x1="64" y1="116" x2="214" y2="158" stroke="currentColor" marker-end="url(#tee)"/>
  <line x1="64" y1="178" x2="214" y2="164" stroke="currentColor" marker-end="url(#arrow)"/>
  <text x="140" y="190" text-anchor="middle" font-size="11" fill="currentColor">AND-NOT</text>
  <path d="M 246 72 C 300 110 300 150 246 158" fill="none" stroke="currentColor" marker-end="url(#arrow)"/>
  <path d="M 314 98 C 260 10 60 10 50 24" fill="none" stroke="currentColor" marker-end="url(#tee)"/>
</svg>
<figcaption>A hand-drawn interaction diagram becomes computable only once every node's inputs are
assigned a gate: e fires only if a and b are both on; f fires only if c is on and b is off; g
feeds back to inhibit a.</figcaption>
</figure>

Turning a published diagram into this kind of statement for every node gives a Boolean network:
given the on/off state of the stimuli and inhibitors, every downstream node's state is computed by
propagating these gates through the graph.

## The case study: primary versus tumor liver cells

The worked example (joint work with Peter Sorger) asked how liver cells respond, in their
signaling, to growth factors and cytokines, and specifically what is different about that response
between **primary, healthy human hepatocytes** (from liver donors) and **four hepatocellular tumor
cell lines**. The motivating logic: if a piece of signaling logic differs between normal and tumor
cells, intervening there should matter; if the logic is unchanged, intervening there should do
nothing, so such a difference is a candidate drug target.

The data: the phosphorylation state of 17 signaling proteins (phosphorylation being the standard
proxy for a kinase or transcription factor's activity) was measured in each of the five cell types,
under 7 extracellular stimuli (growth factors, cytokines, and bacterial metabolic products) crossed
with 7 small-molecule kinase inhibitors (plus unstimulated controls), at three time points (0, 30
minutes, 3 hours). Each measurement was coded by when and how strongly it responded: gray for no
change, yellow for an early transient response, purple for a late-appearing response, green for an
early and sustained response. Inspecting the primary cells against one tumor line side by side, the
coloring is visibly different across most of the grid — the two cell types respond with different
signaling dynamics to the same panel of treatments, and the modeling problem is to say *where* the
logic differs and whether that difference is biologically meaningful.

The prior-knowledge scaffold came from the Ingenuity database, restricted to the roughly 82 nodes
and about 100 edges lying downstream of the seven stimuli and upstream of the transcription factors
of interest — with one gap patched by hand, since the database turned out to be missing basic
insulin-receptor signaling entirely.

## Fitting logic models to data

The scaffold is first stripped of any node that could not possibly be judged against the data (no
stimulus reaches it, or it was never measured), leaving a graph whose *topology* is given but whose
*logic* — which combination of AND, OR, NOT gates governs each node — is not. Many different
assignments of gates are consistent with the stripped topology, and the question is which of those
candidate Boolean networks best reproduces the measured data.

Model quality was scored by an objective function, written as a quantity $\theta$ to minimize,
combining two terms:

- a **data-fit error**: the model's Boolean output (0 or 1) for every node, under every stimulus
  and inhibitor condition, compared against the actual experimental measurement — which is *not*
  itself binary but normalized to lie between 0 and 1 (a real measurement might read 0.7 or 0.25),
  so even a perfectly correct set of edges still incurs some quantitative mismatch against a model
  restricted to 0/1 outputs;
- a **size penalty**: the number of nodes in the model, multiplied by a penalty weight $\alpha$,
  to discourage simply adding components until the fit improves.

The search over candidate logic networks used a genetic algorithm, since the space of possible
networks is far too large to search exhaustively. Starting from a population of networks derived
from the Ingenuity scaffold by randomly adding or removing edges, each member is scored against the
objective function; the best-scoring ("elite") members survive unchanged into the next generation,
others are mutated (an edge added or removed with some probability) or produced by crossover (a
"daughter" network inherits some edges from one "parent" network and some from another). Iterating
this produces successive populations, tracked until a population of models fits the data within a
chosen tolerance. The elite-survival step matters because without it the best networks found so far
could be lost between generations. The method has no guarantee of finding a global optimum and can
get stuck in a local one — addressed by rerunning the whole search from several different random
starting populations and checking whether they converge on similar consensus models.

A genuinely counter-intuitive result came out of this fitting process: **even with a negligible
size penalty, the best-fitting models were already substantially smaller than the full Ingenuity
scaffold.** The naive expectation — a bigger model should always fit the data at least as well as
a smaller one — turns out to be false in practice. The explanation offered in discussion: adding an
extra arc to fix one measurement can introduce logic that degrades the model's agreement with two
or three *other* measurements, producing new false positives and false negatives elsewhere that
outweigh the gain. Only once the size penalty is pushed larger still does the model keep shrinking
at the direct cost of fit quality — so there is a regime, used in the actual fitting, where the
penalty is large enough to strip out non-essential nodes and edges but not so large that it starts
to hurt the data fit.

A further point about what fitting produces: **not a single best model, but a family.** Within the
noise level of the experimental measurements, a substantial number of distinct networks fit about
equally well, and there is no principled way to reject the others in favor of one. Plotting, for
each candidate edge, how often it appears across the best-fitting population shows that only a
small subset of edges are in (nearly) all of them; which edges are "core" versus "optional" depends
on how tight a fit tolerance is demanded. The practical object of interest is therefore a
**consensus model**: drawn from the family of best-fitting networks, with each edge's line
thickness proportional to the fraction of the family in which it appears. This connects to a
receiver-operating-characteristic-style trade-off: moving the size penalty trades false negatives
against false positives, and the best-predicting model sits at the size penalty where the model is
as small as possible without yet degrading the experimental fit.

## Validating the model: a priori prediction

Fitting a model to data it was trained on proves nothing about its predictive value by itself. The
validation step: having chosen the family of best-fit models from the original training data set
(the seven single stimuli crossed with the seven single inhibitors), a genuinely new data set was
collected using *combinations* of inhibitors and stimuli that had never been used before — the kind
of combinatorial drug question that is prohibitively expensive to test exhaustively in the wet lab,
and exactly where this kind of model is meant to be useful. The model, untouched since training,
was run forward to predict the outcome on this new condition set.

The comparison of three fits, by fraction of measurements the model got wrong:

- the unmodified Ingenuity scaffold, fit as a Boolean model with no edges added or removed: about
  **45% error** — roughly half the measurements were wrong;
- the best-fit, stripped-down model on its original training data: under **10% error**;
- the same best-fit model, predicting the new combinatorial data set it had never seen: about
  **11% error** — essentially matching its training performance.

The first comparison shows that taking a literature-curated scaffold at face value, without
pruning it against the specific cell type and conditions under study, does not work well — the
database mixes in evidence from other cell types and conditions that simply does not apply here,
and misses interactions that were never tested in this cell type at all. The second and third
together are the validation: a model trained on one data set predicted a new, structurally
different data set about as well as it fit the data it was trained on.

## What the model revealed: normal versus tumor liver signaling

With a validated consensus model for the primary hepatocytes and, separately, for each of the four
tumor cell lines, the edges can be classified by which cell types' best-fit family they appear in:
an edge present in the consensus models of all five cell types is a shared "core"; an edge present
in the primary cells but absent from the tumor lines is signaling logic normal liver cells use that
the tumor lines have lost; an edge present only in the tumor lines is logic the normal cells did
not need but the tumor lines have gained. Three specific, literature-checked examples were worked
through:

- A downstream node (HSP27) is activated via one pathway in normal cells; in the tumor cells, that
  link is lost and the node is instead driven, more weakly, through a different pathway — so even
  though the node is overexpressed in the tumor cells, it ends up *less* activated than gene
  expression alone would suggest. This pattern is reported as consistent with the liver tumor
  literature.
- Activating the IKK pathway, which drives the transcription factor NF-$\kappa$B, requires in
  normal hepatocytes the *simultaneous* activity of a pathway downstream of the insulin receptor
  **and** a pathway downstream of a cytokine — an AND condition. In the tumor cell lines that check
  is lost: either pathway alone is sufficient. This looser regulation of NF-$\kappa$B is reported as
  consistent with the liver-cancer-progression literature.
- Insulin signaling, which in normal hepatocytes is mainly a metabolic stimulus, acquires a
  proliferative downstream arc in the tumor cell lines that is absent in the primary cells — again
  consistent with literature describing a shift of insulin signaling from metabolism toward
  proliferation in tumor cells.

A separate follow-up study (referenced but not detailed) reported that killing these liver tumor
cells required combination inhibitors against all three of exactly these pathways simultaneously —
the same three pathways the logic model had flagged as the loci of difference between normal and
tumor signaling.

## Tracing an edge the literature could not explain

One edge in the tumor consensus model — from IKK up to STAT3 — had no support anywhere in the
literature, yet was required to fit the data; it is marked as a dashed line in the published model
to flag this. Rather than discard or ignore it, the edge was traced back to the specific
experimental measurements that forced it in: it turned out to come from the condition using a
small-molecule inhibitor intended to block IKK specifically. Two explanations were considered: a
real, perhaps transcriptional, mechanism linking IKK activity to STAT3's expression or
responsiveness; or an artifact of the inhibitor itself having an unintended **off-target effect** on
the JAK/STAT3 kinase. Direct testing of the inhibitor's activity against that other kinase
confirmed the off-target effect — the compound used to target IKK did, in fact, also inhibit the
JAK2/STAT3 pathway, which is why the logic model needed an edge with no mechanistic basis to fit
the data generated with that inhibitor.

This had a pharmacological payoff beyond explaining the artifact: this same small molecule, aimed
at IKK, had independently been found to be the most effective of a whole panel of IKK inhibitors at
treating lung airway inflammation. The off-target hit on the second kinase is offered as a
candidate explanation — the drug's extra activity may itself be therapeutically useful, pointing
toward combination inhibition of both pathways as the operative treatment logic.

This example made a broader point about model identifiability: an edge the fitting process
*removes* from the scaffold is comparatively easy to accept (the prior database edge was simply not
needed to explain this cell type's data). An edge the fitting process *adds*, that was not in the
scaffold, demands scrutiny — check the literature first; where the literature does turn out to
support it, the gap was simply a curation gap in the database rather than a biological discovery.
The IKK–STAT3 case was unusual in having neither a literature explanation nor remaining
unexplained — it could be traced directly to a specific inhibitor's off-target behavior. Asked
whether that tracing is generally possible, the honest answer given was no: there is no guarantee
an unexplained added edge can always be traced back to a specific experimental cause, and this is
flagged as an open methodological challenge rather than a solved one.

## From Boolean to continuous: constrained fuzzy logic

A standing objection to this whole approach is that biochemistry is not actually binary: comparing
a Boolean 0/1 model prediction against a continuous measurement of, say, 0.6 raises the question of
whether 0.6 should count as closer to 1 or to 0, and different normalization choices can flip a fit
from "correct" to "incorrect" for reasons that have nothing to do with the biology.

The fix described is to relax the step function at every gate into a graded, sigmoid-like transfer
function — an "analog" version of the same logic. A pure Boolean gate already has one hidden
parameter (where the switch from off to on sits); the graded version adds a second, the steepness
of that transition, and this generalizes to AND and OR gates as well as single inputs. The
practical cost is that every node or gate now carries an extra fitted parameter — fifty nodes means
fifty more parameters to estimate, so substantially more data is required to fit the model. The
payoff is that predictions become genuinely quantitative rather than just qualitative: the model
can predict how gradually the phosphorylation of a transcription factor such as CREB shifts in
response to partially inhibiting one upstream kinase versus another, distinguishing a strong effect
from a weak one rather than only predicting on/off outcomes. This relaxed formalism was referred to
in the lecture as a constrained fuzzy logic model.

## Open questions raised in discussion

Two questions from the audience, left genuinely open rather than answered definitively:

- **Identifiability of added edges.** Beyond checking the literature, is there a general way to
  trace a newly required edge back to the specific data that forced it, when the fitting process
  is itself stochastic (so repeating the fit need not reproduce exactly the same edge)? The
  IKK–STAT3 case was traceable, but there is no reason to expect that will always be possible, and
  no general method was offered.
- **Tumor heterogeneity.** Could the frequency with which an edge appears across the family of
  best-fit models — say, present in 80% rather than 100% of them — reflect an underlying mixture of
  tumor subtypes being averaged together in the measurement, rather than simple model uncertainty?
  This was described as an attractive but unverified idea: the relevant experiments to test it were
  not available at the time, and it was left open rather than claimed as a result.

## Sources

- Lecture 17 slides — title, central-topic framing ("cues → signals → response"), and the
  citations to Saez-Rodriguez (*Molecular Systems Biology* 5:331, 2009; *Cancer Research* 71:5400,
  2011) and Morris (*Biochemistry* 49:3216, 2010; *PLoS Computational Biology* 7:e1001099, 2011)
  that anchor the case study —
  `computational-biology/mit-ocw/7091j/lectures/17-slides.md`. The deck itself is almost entirely
  figures with no extractable text layer; this chapter draws its narrative content from the
  recording rather than the slide text.
- Lecture 17 transcript (guest lecture by Doug Lauffenburger), in full, [00:00]–[1:13:54] —
  `computational-biology/mit-ocw/7091j/recordings/lectures/17.md`. In particular: the pancreatic-
  cancer mutation motivation and the circuitry-metaphor/theory-vs-data-driven discussion
  [06:28]–[14:31]; pathway versus interactome databases and their lack of overlap [16:36]–[21:12];
  the Boolean gate example with nodes $a,b,c,e,f,g$ [24:43]–[25:47]; the hepatocyte case study and
  the Ingenuity scaffold [26:50]–[32:20]; the objective function, genetic algorithm, and the
  smaller-model-fits-better result [34:38]–[50:10]; a priori prediction on combinatorial data
  [51:17]–[53:25]; the normal-versus-tumor consensus-model differences [53:25]–[1:05:22]; the
  IKK–STAT3 edge and the off-target inhibitor [56:43]–[1:01:10]; constrained fuzzy logic
  [1:05:22]–[1:08:31]; and the closing audience questions on identifiability and heterogeneity
  [1:08:31]–[1:12:46].
- The lecture referred to, but did not itself contain, a separate paper comparing six or seven
  pathway/interactome databases for overlap, and a separate follow-up study identifying the
  combination of three pathway inhibitors needed to kill the liver tumor cell lines; neither
  citation was given in the recording, and neither source is covered further here.

---

[← 16. Factor Graphs and Interactome Networks](16-factor-graphs-and-interactome-networks.md) · [Contents](index.md) · [18. Reading Chromatin State and Genome Looping →](18-reading-chromatin-state-and-genome-looping.md)
