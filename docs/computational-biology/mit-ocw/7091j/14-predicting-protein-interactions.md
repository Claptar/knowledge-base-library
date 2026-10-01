---
title: "14. Predicting Protein Interactions"
course: "MIT 7.091J"
chapter: 14
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Predicting Protein Interactions

## What this covers

The previous lecture tried to predict protein structure; this one asks a different question: given
two proteins, do they interact at all? The chapter covers two structure-based filtering algorithms
(PRISM and PrePPI), two high-throughput experimental assays and their failure modes (affinity
purification with mass spectrometry, and yeast two-hybrid), the statistical problem of deciding how
much of that experimental data to trust, and the Bayesian machinery — likelihood ratios, then full
Bayesian networks — used to combine many noisy sources into one probability of interaction. It
assumes the potential-energy functions and structural-comparison tools from the protein-structure
lectures.

## From "how strong" to "yes or no"

The natural first question about a protein complex is quantitative: given two proteins whose joint
structure is known, how does a specific mutation change the binding affinity? In principle this
should be tractable, since the potential-energy functions already score a structure. In practice it
turned out to be very hard: prediction algorithms for this problem, compared against simply scoring
mutations with the BLOSUM substitution matrix, almost never did meaningfully better than that simple
default, and many did worse.

So the lecture drops the quantitative question for a cheaper one: not *how strong*, but *does it
happen at all*. Even this is not trivial, because knowing the structures of two proteins does not
say which surfaces of them interact. The naive pipeline is: solve the docking problem (relative
position and orientation, allowing for local and sometimes global conformational change on binding),
score the result with an energy function, and compare it against a threshold.

This has two problems: run rigorously over every candidate partner it is very slow, and it is prone
to false positives, because an energy calculation only asks whether two proteins have a *favorable*
interaction, never whether it is the best one on offer. A protein's true partner is whichever
available molecule, at whatever concentration it is actually present, has the highest affinity — not
whichever one you happened to test. The lecture sets that competition problem aside and focuses on
the part with a computational answer: cutting the search space before paying for expensive
calculations.

## PRISM: filtering by structural match at the interface

PRISM works from the premise that the number of distinct architectures two proteins can use to
interact is limited, and that within one architecture, residues do not contribute equally to the
binding energy. If both are identifiable in advance, a candidate pair can be screened cheaply before
any expensive refinement.

The unevenness of residue contribution is the "hotspot" phenomenon, shown by Clackson and Wells
(1995) in a cell-surface receptor and its ligand: mutating every interface residue to alanine in turn
and measuring the change in binding free energy gave a sharply non-uniform result — large losses at
a few positions, almost no effect at most, a small gain at a few. In human growth hormone bound to
its receptor, the residues contributing more than about 1.5 kcal/mol are concentrated in small
patches, and roughly 10% of interface residues carry most of the binding energy. There is no simple
structural correlate (hotspots are not simply the residues with the largest surface area), though
they tend to be enriched in tryptophan, arginine and tyrosine, and are often ringed by an "o-ring" of
residues that exclude solvent from the interface without themselves contributing much energy.

PRISM uses this to decouple local from global similarity: two proteins can differ completely in
overall fold and still interact through a locally similar interface — chymotrypsin interacts with
several partners that share little global structure with each other but look alike at the contact
surface. The algorithm:

1. Start from a template pair known to interact; define the interface as residues of one chain in
close contact with the other.
2. Keep only the interfacial residues, discard the rest of the structure — comparison is done on the
interface alone.
3. Search a structural database for proteins whose local geometry matches that interface. The
comparison ignores chain order, so matching elements can sit in different, even widely separated,
parts of the chain — an insertion elsewhere does not disqualify a match.
4. Apply fast checks first: structural similarity at the interface, evolutionary conservation, and
whether the predicted hotspot positions match and are conserved.
5. Only pairs passing these checks go on to flexible structural refinement — energy minimization, as
in the structure-prediction lectures — to estimate the free energy of the complex.

Two worked cases: ASPP2 has no global resemblance to IκB, but matches IκB's interface with NF-κB
closely enough that PRISM proposes ASPP2 as an NF-κB partner. And starting from the known complex of
a cyclin-dependent kinase, its cyclin, and the inhibitor p27, PRISM finds other pairs with a matching
local interface but no global sequence similarity, carries them through refinement, and arrives at a
predicted interaction energy for each. PRISM's strength is ending in an actual refinement, so it
produces a real energy estimate; its weakness is the same refinement step, the expensive part of the
pipeline.

## PrePPI: filtering by homology alone, with no refinement

PrePPI never performs a structural refinement. For query proteins A and B:

1. Find sequence homologues of A and B among proteins of known structure: homology models $M_A$ and
$M_B$.
2. Find the *structural* neighbours of $M_A$ and $M_B$ (not sequence neighbours): $N_{A,1},\dots$ and
$N_{B,1},\dots$.
3. Ask whether any neighbour of $M_A$ and any neighbour of $M_B$ are a known interacting pair. If so,
that known pair ($T_A$/$T_B$) becomes a candidate model for how A and B might interact — two steps
removed from the query.
4. The published figure calls this step a structural superposition, but it is actually a sequence
alignment: align $M_A$/$M_B$ to $T_A$/$T_B$ and count what fraction of the template's interface
residues can be aligned at all.
5. Score whether the aligned residues are the kind typical of protein interfaces, using
machine-learning methods trained on known interfaces (the same statistics behind the hotspot
findings above).
6. Combine five such measures — structural similarity, fraction and count of alignable interface
residues, and interface-residue-type scores — with a Bayesian classifier to produce a probability of
interaction.

Because every step is a sequence alignment or a lookup against precomputed neighbours, PrePPI is
extremely fast and has been run over every protein pair in several whole genomes. The cost is
specificity in both directions: it cannot predict a genuinely novel interaction if no known
structural-neighbour pair is already known to interact, and without refinement it cannot capture
conformational change on binding — the detail PRISM keeps.

## Measuring interactions at scale

Structural prediction is one route to "do these interact?" The other is direct measurement, and the
major recent shift has been from pairwise measurement to bulk, high-throughput measurement.

**Affinity purification with mass spectrometry (AP-MS).** Tag one protein, attach it to a solid
support, let other proteins bind, wash, elute, run the eluate on a gel, identify whatever comes off
by mass spectrometry. Labour-intensive compared to one experiment, but far faster than resolving
structures one complex at a time, and it has mapped interaction partners across whole proteomes.
Its errors have identifiable causes:

- *False positives*: proteins that stick to the solid support itself regardless of bait, and
proteins that bind other proteins non-specifically rather than the bait.
- *False negatives*: weak or short-lived interactions washed away during purification; interactions
near the tag site, which the tag can sterically block; low-abundance proteins, which never
accumulate enough material for mass spec; and spurious hits from concentration effects — proteins
overexpressed together may bind even though, at natural concentrations and compartments, they never
meet.

**Tandem affinity purification (TAP-tags)** was built to cut the non-specific-sticking false
positives. A gene is modified by homologous recombination in yeast, so it still expresses at native
level from its native locus, to encode the protein followed by: a spacer, a calmodulin-binding
protein (CBP), a site cut by tobacco etch virus (TEV) protease, and protein A. Purification then runs
in two specific steps:

1. An IgG column binds protein A, pulling down the bait and whatever binds it — including anything
that sticks to the support non-specifically.
2. Rather than eluting with acid, salt, heat or detergent (which would also release non-specific
stickers), the complex is released by cleaving with TEV protease at its specific site, leaving
non-specific binders on the column.
3. A second purification captures only the eluted material via CBP binding calmodulin on a second
support, released specifically with EGTA, which chelates the calcium the CBP–calmodulin interaction
depends on.

The two specific elution steps remove most non-specific binders, at the cost of harsher, longer
handling — fewer false positives, more false negatives.

**Yeast two-hybrid (Y2H)** instead puts a reporter gene behind a promoter with a DNA-binding site.
A "bait" protein is fused to a DNA-binding domain that sits there; a "prey" protein is fused to a
transcriptional activation domain. If bait and prey do not interact, the activation domain is never
brought to the promoter and the reporter stays off; if they interact, it turns on. Nothing is
physically purified, so Y2H is more sensitive to low-abundance proteins and can catch transient
interactions AP-MS would wash away. Its bias is different: both proteins must express and fold well
in a yeast nucleus, so proteins that express poorly in yeast (including many human or plant
proteins), and membrane proteins unsuited to the nucleus, are systematically missed.

One partial fix for both methods: proteins appearing in essentially every purification ("frequent
fliers") can simply be subtracted out. This does not catch a protein with genuine but non-specific
affinity for many baits — sticky enough to be a problem, not ubiquitous enough to be filtered this
way.

## How much of this data can you trust?

Any high-throughput experiment needs checking against a **gold standard** — interactions known with
very high confidence from a more direct method such as structural work, not from two-hybrid or AP-MS
themselves. Comparing one experiment to the gold standard gives clean categories for the overlap
(true positives) and gold-standard pairs the experiment missed (false negatives, if the gold standard
is correct). What it cannot resolve is everything detected with no gold-standard entry at all — some
are genuinely novel true interactions (finding those is the point of the experiment) and some are
false positives, with no way from one experiment to tell which.

Two independent experiments plus a gold standard do give a way. Consider the overlap of experiment 1
and experiment 2. If the two experiments' errors are genuinely independent (say one is Y2H, one is
AP-MS), there is no reason a false positive in one would also be a false positive in the other, so
this overlap is a "consensus" set of true positives. Within it, some fraction lands in the gold
standard and some does not (the gold standard itself is incomplete). The argument: this fraction —
how much of a true-positive set the gold standard happens to catch — should be the same whether the
true positives came from the consensus or from a single experiment alone. So take the fraction of the
consensus set in the gold standard, and apply it to the pairs detected by only one experiment, to
split those into estimated true and false positives.

Working this through for one pair of experiments: the consensus set held roughly 2,000 pairs, of
which 347 fell in the gold standard; applying that ratio to the region unique to one experiment gave
an estimated 1,123 true positives against almost 15,000 false positives. Across a number of published
experiments, the estimated false-positive fraction ranged from about 50% to over 90%.

Blunt fixes are each unsatisfying. Requiring every method to agree pushes accuracy up sharply — on a
plot of accuracy against gold-standard coverage, three-method agreement reaches something like
80–90% accuracy — but coverage then drops to well under 1%, discarding almost everything. Dropping
suspiciously frequent "sticky" proteins helps a little but is blunt. What is wanted instead is a
*probability* of interaction from all the data at once — the Bayesian approach developed next.

## A Bayesian likelihood ratio for combining evidence

Bayes' rule gives the probability an interaction is true given the data in terms of the probability
of the data given a true interaction, times a prior:

$$P(\text{true} \mid \text{data}) \propto P(\text{data} \mid \text{true})\, P(\text{true})$$

Dividing the "true" expression by the "false" one gives the posterior odds, and the prior
probability of the data cancels out entirely:

$$\frac{P(\text{true}\mid \text{data})}{P(\text{false}\mid \text{data})}
= \frac{P(\text{data}\mid\text{true})}{P(\text{data}\mid\text{false})}\cdot
\frac{P(\text{true})}{P(\text{false})}$$

If this ratio exceeds 1, call the pair interacting; below 1, reject it. For *ranking* every candidate
pair rather than thresholding, even less is needed: taking logs turns the ratio into a sum, and the
prior-odds term is the same constant for every pair, so it does not affect the ranking at all. What
must actually be estimated is only the likelihood ratio: the probability of a given pattern of
experimental results given the interaction is true, over the same given it is false.

As a first simplification, treat data from different experiments as independent, so the likelihood
ratio factors into a product over experiments. This needs gold-standard *negatives* as well as
positives. Since almost nobody publishes "protein X does not interact with protein Y," this set is
built from indirect evidence: pairs annotated to different, unrelated complexes; pairs localized to
different parts of the cell; pairs with anti-correlated gene expression. None are guarantees
(annotations can be wrong, and RNA level is not always a good proxy for protein level), but combining
several criteria gives a workable negative set.

Ranking every pair by this likelihood ratio and varying the threshold produces a curve of accuracy
against gold-standard coverage, validated against two independent reference databases (MIPS and
SGD) — recovering far more of the gold standard at a given accuracy than the "everybody agrees" rule
did.

## Bayesian networks: a graph for causes and effects

The likelihood-ratio calculation is the simplest case of a more general tool: a **Bayesian network**,
a graph of causes and effects together with a set of probabilities, set by hand from prior knowledge
or learned from data.

This machinery is needed because a full joint probability table over $N$ binary variables needs
$2^N-1$ independent numbers (the $-1$ because probabilities must sum to one) — unworkable beyond a
handful of nodes. A Bayesian network instead encodes, in its graph, which variables are causes and
which are effects, with an arrow from cause to effect — here the interaction itself is the hidden
cause, and what is observed is the noisy result of a specific experiment. The graph need not treat
every observation as independent: if a protein is a membrane protein, that might bias one assay
(two-hybrid) without biasing another (AP-MS), and a graph reflecting that captures the data better
than flat independence.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A toy Bayesian network for admissions, with causes Smart and Grade Inflation feeding Grades and GRE, which together cause Admit">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="80" cy="35" r="26" fill="none" stroke="currentColor"/>
  <text x="80" y="39" text-anchor="middle" font-size="12" fill="currentColor">Smart</text>
  <circle cx="240" cy="35" r="34" fill="none" stroke="currentColor"/>
  <text x="240" y="31" text-anchor="middle" font-size="11" fill="currentColor">Grade</text>
  <text x="240" y="44" text-anchor="middle" font-size="11" fill="currentColor">inflation</text>
  <circle cx="60" cy="115" r="24" fill="none" stroke="currentColor"/>
  <text x="60" y="119" text-anchor="middle" font-size="12" fill="currentColor">GRE</text>
  <circle cx="190" cy="115" r="26" fill="none" stroke="currentColor"/>
  <text x="190" y="119" text-anchor="middle" font-size="12" fill="currentColor">Grades</text>
  <circle cx="150" cy="190" r="26" fill="none" stroke="currentColor"/>
  <text x="150" y="186" text-anchor="middle" font-size="11" fill="currentColor">Admit</text>
  <text x="150" y="199" text-anchor="middle" font-size="9" fill="currentColor">(effect)</text>
  <line x1="74" y1="58" x2="62" y2="92" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="95" y1="52" x2="170" y2="93" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="222" y1="60" x2="200" y2="91" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="80" y1="137" x2="130" y2="172" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="175" y1="140" x2="160" y2="165" stroke="currentColor" marker-end="url(#arrow)"/>
</svg>
<figcaption>The toy admissions network: Smart and Grade inflation are parents of Grades; Smart alone
is a parent of GRE; Grades and GRE together are the parents of Admit. Prediction reasons top to
bottom from observed causes; inference reasons bottom to top from an observed effect.</figcaption>
</figure>

The key simplifying fact: a node is conditionally independent of its non-descendants given its own
parents. In the admissions network above, GRE scores depend only on whether the student is smart,
not on grade inflation, so that dependency needs no parameter at all. More generally, once a node's
immediate parents are known, anything further back up the graph adds nothing. This is also why
conditional probabilities ($P(\text{smart}\mid\text{good grades})$, etc.) are the natural currency
here rather than full joint tables: the same information, but in the form the graph actually
constrains.

The network supports two kinds of reasoning. A **prediction** problem reasons from observed causes
to an unobserved effect — given grades and GRE scores, predict admission. An **inference** problem
reasons the other way, from an observed effect back to an unobserved cause — knowing only that
someone attends MIT, inferring that they are probably smart.

## Explaining away

A consequence of reasoning over these graphs that is not obvious on first encounter is called
**explaining away**. The classic example (from Judea Pearl's work on Bayesian networks at Stanford):
the grass outside is wet, which could be because it rained or because the sprinkler was on. There is
no causal link between rain and the sprinkler. But once the wet grass is observed, that independence
breaks: knowing it rained makes the sprinkler *less* likely to have been on, purely because rain
alone already explains the wet grass.

The same structure appears in a simple formal example: toss a coin twice, scoring a point if both
tosses match (heads–heads or tails–tails), none if they differ. The two tosses are causally
independent — neither influences the other. But conditioned on the score, they are not: told the
score was 1 (a match) and the first toss was tails, the probability the second was heads is exactly
zero, not the unconditional probability of heads. Observing a shared effect (the score) induces a
dependence between its causes, even with no causal arrow between them — a routine feature of
reasoning over these graphs, not an exception to it.

## Learning a Bayesian network

Building a network from data splits into two problems: learning the probability tables given a fixed
structure, and learning the structure itself.

Given the structure, learning the probabilities means choosing an objective and optimizing it. Two
standard choices: **maximum likelihood** — choose parameters $\theta$ (all the conditional
probability tables) maximizing $P(\text{data}\mid\theta)$ — and **maximum a posteriori**, which
additionally folds in a prior over the data and the parameters themselves. Either is then optimized
by the same kind of search used elsewhere in the course: gradient descent, expectation-maximization,
or Gibbs sampling.

Learning the structure is much harder: possible graphs grow combinatorially, and without strong
prior knowledge it can be effectively impossible to recover from a realistic amount of data. The
usual workaround is domain knowledge restricting which nodes may even be causes — in a
transcriptional network, letting only transcription factors or signaling molecules serve as causes,
rather than letting any of several thousand genes cause any other.

## Other evidence to fold into the network

Beyond the direct assays, several other kinds of data correlate with whether two proteins interact,
set up here to be combined, next lecture, with the assay data inside a Bayesian network.

**Gene expression.** Interacting proteins are expected to be present at the same time, so
anti-correlated expression argues against interaction. Correlation the other way is only a trend, not
a rule: plotting distance between expression profiles for known-interacting versus known
non-interacting pairs shows interacting pairs shifted toward smaller distances, but the two
distributions overlap heavily — no threshold cleanly separates them.

**Co-evolution (phylogenetic profiles).** A pair of genes that interacts should tend to be present or
absent together across genomes, but the *pattern* of presence/absence across a tree carries more
information than presence/absence alone. A pattern confined to a single branch can be explained by
one shared gain-or-loss event, with the genes simply co-inherited afterward — weak evidence on its
own. A pattern scattered across several independent branches is stronger evidence, because it
requires the same pair to be jointly gained or lost more than once independently — unlikely as
coincidence unless the two genes are functionally linked.

**Gene fusion ("Rosetta Stone").** A related signal: whether the same pair of genes appears fused
into one gene in some genomes and as two separate genes in others, used as evidence the two proteins
interact or work together functionally.

## Sources

- Transcript `lectures/recordings/14.md` **[00:00]–[13:55]**: recap of the affinity-prediction
problem and the BLOSUM comparison; the switch to the binary interaction question and the docking
pipeline's speed/false-positive problems; PRISM, including hotspots (Clackson and Wells, 1995,
cell-surface receptor/ligand; human growth hormone and receptor), the o-ring, the chymotrypsin
example, and the ASPP2/IκB–NF-κB and CDK–cyclin–p27 worked examples.
- Transcript **[13:55]–[20:22]**: PrePPI, its five scoring measures, Bayesian classifier, and its
de novo/refinement limitations. Slides `14-slides.md` name both papers ("PRISM", "PrePPI"), but the
deck's reconstructed text does not carry full citations; the lecturer notes both papers were posted
to the course website (not supplied here).
- Transcript **[20:22]–[37:18]**: AP-MS, its false positives/negatives, TAP-tags (TEV protease,
calmodulin-binding protein, EGTA elution), yeast two-hybrid, the "frequent flier" control, and the
gold-standard Venn-diagram argument with its numbers (347 of ~2,000 consensus pairs; estimated 1,123
true versus ~15,000 false positives in the single-experiment region; 50–90% false-positive range
across experiments), plus the consensus-only accuracy/coverage plot.
- Transcript **[37:18]–[47:13]**: the Bayesian likelihood-ratio framework, the independence
assumption, gold-standard negatives, and the MIPS/SGD validation.
- Transcript **[47:13]–[1:02:22]**: Bayesian networks in general, the $2^N-1$ parameter count, the
admissions toy example, conditional independence of a node from its ancestors given its parents, the
prediction/inference distinction, and explaining away (sprinkler/rain/wet-grass, attributed to Judea
Pearl at Stanford; the two-coin-toss example). Slide `14-slides.md`'s line "Graphical Structure
Expresses our Beliefs" matches this section.
- Transcript **[1:02:22]–[1:11:05]**: learning a Bayesian network (parameter estimation by maximum
likelihood or maximum a posteriori; structure learning and domain knowledge restricting the search —
the lecturer refers to a worked toy-probability example in separate course notes, not supplied with
this lecture); then gene expression correlation, co-evolution/phylogenetic profiles, and gene fusion
("Rosetta Stone"), previewed as inputs to next lecture's combined Bayesian network.
- Slides `14-slides.md`: course outline (L12–L17) and a figure credited to Lindorff-Larsen, Piana et
al., "How Fast-folding Proteins Fold," *Science* 334 (2011): 517–20 — captioned in the deck but not
discussed in the supplied transcript for this lecture.

---

[← 13. Refining and Predicting Protein Structure](13-refining-and-predicting-protein-structure.md) · [Contents](index.md) · [15. Clustering and Inferring Regulatory Networks →](15-clustering-and-inferring-regulatory-networks.md)
