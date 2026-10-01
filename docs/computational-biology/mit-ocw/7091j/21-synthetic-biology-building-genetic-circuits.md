---
title: "21. Synthetic Biology: Building Genetic Circuits"
course: "MIT 7.091J"
chapter: 21
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Synthetic Biology: Building Genetic Circuits

## What this covers

This chapter is a guest lecture by Ron Weiss (Biological Engineering, EECS, and the Synthetic Biology
Center at MIT) on synthetic biology: engineering genetic *circuits* rather than individual genes. It
traces the field from its origin as a deliberate "flip" of computer-science ideas onto DNA, through the
basic parts (transcriptional logic gates), the practical difficulties of building and predicting circuit
behavior, and the responses the field has built — computational design tools, standardized part libraries,
explicit statistical thinking. It closes with the lecture's running application: a circuit that classifies
a cell as cancerous or healthy from several microRNA levels. It assumes familiarity with transcriptional
regulation (activators, repressors, promoters) and basic digital logic (AND, OR, NOT).

## From computing to biology, and back

**[02:14]–[03:21]** Synthetic biology, for Weiss, began as the reverse of an existing idea. In the
mid-1990s, amorphous computing — using huge numbers of simple, locally interacting elements to perform
robust computation, with biology as an obvious source of inspiration — initially ran one direction: use
biology to understand how to program large numbers of simple computing elements. At some point he "flipped
the arrow": use what is known about computing to program biology directly.

**[03:21]–[05:59]** Genetic engineering in the narrow sense — altering DNA to build sensors, regulatory
mechanisms, cell–cell communication, novel syntheses — predates synthetic biology by decades. What is new,
in Weiss's account, is the emphasis on **systems-level engineering**: not over-expressing one gene or a
handful of genes, but deliberately constructing *systems of interacting regulatory elements*, built and
composed with the discipline — reliability, predictability, efficiency — expected of engineered computer
systems.

**[05:59]–[09:20]** The field borrows vocabulary from disciplines that already know how to go from basic
devices, to modules with specific behaviors, to integrated autonomous systems, to communities of such
systems — a community of robots; here, a community of bacteria, or a tissue of communicating mammalian
cells. Part of the field's ongoing work, Weiss notes, is finding out not only what can be imported from
those disciplines but what is genuinely *different* about engineering biology.

## Sensors, processing, actuation

**[09:20]–[11:36]** A synthetic biology project is standardly decomposed into **sensors** (detecting
microRNA, messenger RNA, or protein levels in a live cell), **processing** (a regulatory network that
integrates several signals and makes a decision), and **actuation** (turning on a protein that changes the
cell or its environment). A sensor's job is not only a fluorescent readout but feeding into the regulatory
logic. The timescale of the computation is set by the application: a circuit responding over hours or days
is fine for tissue engineering, though useless for conventional electronics.

**[11:36]–[16:20]** Weiss uses the scale of engineered DNA as an organizing axis. A single over-expressed
or inducible gene is not, in his usage, synthetic biology; the field begins once circuitry introduces
interactions that did not previously exist in that cellular context. Most synthetic biology sits at the
scale of a handful of genes to a few thousand bases; the frontier is pushing toward 20,000–50,000 bases of
engineered DNA per construct. Beyond that lies the much harder, not-yet-realized goal of a genome built
from newly designed reactions rather than by deleting parts of an existing one — current "minimal life"
work knocks genes out of existing organisms rather than designing from scratch. The driver of this scaling
is the falling cost of DNA synthesis, which Weiss describes as following its own Moore's-law-like curve.

## Building a logic gate out of a promoter

**[17:29]–[20:40]** Every project starts from a toolbox of parts: transcriptional regulatory elements,
translational and protein–protein regulatory elements, cell–cell communication mechanisms, fluorescent
reporters for debugging, sensors and actuators. These were historically catalogued and physically stored —
Weiss mentions the iGEM part registry, once housed at MIT and now run independently, holding on the order
of 15,000 characterized parts.

The simplest logic device is the genetic **inverter**: a promoter repressed by a single repressor protein.
No repressor, high output; repressor present, output repressed — a NOT gate. Building and characterizing
one took about three years of Weiss's own PhD; the same kind of device can now be built in a day.

**[21:44]–[23:03]** A second device adds a small molecule that inactivates the repressor: when present, it
prevents the repressor binding its promoter, so output is made even with the repressor present. As a truth
table this is "not $A$ or $B$" — the **material conditional**, $A \Rightarrow B$ — repressor and small
molecule as the two inputs. Weiss calls it a function with essentially no dedicated gate in ordinary
digital computers, but a useful one for externally controlling gene expression.

## From single gates to digital circuits: signal restoration

**[23:03]–[27:34]** Can gates be chained into a **logic circuit** that stays reliable despite noisy
biological components? Weiss's example is a cascade of the conditional-logic inverter above. As the
cascade lengthens, the input–output steady-state curve becomes progressively more step-like: over 1000-fold
change in output for only a 2- to 4-fold change in input, with good noise margins, once the cascade is long
enough.

Each stage's output being a cleaner approximation of a digital 0/1 than its input is **signal
restoration** — the reason digital computation is reliable at all, in electronics or in cells: without it,
noise accumulates stage by stage. Nature found mechanisms for this long before electronics or synthetic
biology; cooperativity in gene regulation is one, producing the sharp, nearly all-or-nothing transitions at
the end of many natural signaling cascades — exactly the discrete decision a cell needs to make, for
instance committing to one cell type rather than another during differentiation.

## Analog behavior: building a pulse

**[27:34]–[29:44]** Digital behavior is not the only target. Weiss describes a cell–cell communication
circuit in which "sender" cells secrete a small diffusible molecule that "receiver" cells detect, engineered
to respond with a **pulse** — GFP rises and then falls. The circuit is a feed-forward motif: the signal
activates a transcriptional activator, which simultaneously (i) activates GFP directly and (ii) activates a
repressor of GFP. GFP rises quickly through the direct path; the repressor accumulates more slowly and
eventually shuts GFP back down.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Feed-forward motif producing a pulse: a signal activates GFP directly and also activates a repressor that later shuts GFP off">
  <defs>
    <marker id="arrowA" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="95" width="70" height="30" fill="none" stroke="currentColor"/>
  <text x="55" y="114" text-anchor="middle" font-size="12" fill="currentColor">signal</text>
  <rect x="150" y="95" width="90" height="30" fill="none" stroke="currentColor"/>
  <text x="195" y="114" text-anchor="middle" font-size="12" fill="currentColor">activator</text>
  <rect x="300" y="30" width="80" height="30" fill="none" stroke="currentColor"/>
  <text x="340" y="49" text-anchor="middle" font-size="12" fill="currentColor">GFP</text>
  <rect x="300" y="160" width="80" height="30" fill="none" stroke="currentColor"/>
  <text x="340" y="179" text-anchor="middle" font-size="12" fill="currentColor">repressor</text>
  <line x1="90" y1="110" x2="146" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowA)"/>
  <line x1="240" y1="103" x2="296" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowA)"/>
  <line x1="240" y1="118" x2="296" y2="166" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowA)"/>
  <line x1="340" y1="160" x2="340" y2="62" stroke="currentColor" stroke-width="1.5"/>
  <line x1="330" y1="62" x2="350" y2="62" stroke="currentColor" stroke-width="2"/>
</svg>
<figcaption>The incoherent feed-forward motif behind the pulse generator: the signal activates both GFP (fast path) and a repressor of GFP (slow path), so GFP rises first and is then shut off, producing a pulse rather than a step.</figcaption>
</figure>

**[29:44]–[31:51]** A motif that looks simple once drawn is a different matter to build from scratch in a
new organism: this circuit took about three years, and the first working version was a flat line — no
response at all. The fix came from a computational model and a **sensitivity analysis** of which rate
constants the behavior is most sensitive to. Here, the repressor's degradation rate and its promoter
binding affinity were the most influential parameters; adjusting them produced a working pulse. Weiss
treats the cycle — build, observe failure, model, identify sensitive parameters, adjust, rebuild — as a
basic fact of life in the field.

## Why prediction is hard, and how far it has come

**[31:51]–[36:25]** Can rate constants be predicted from DNA sequence directly? Weiss says no — predicting
rate constants from an arbitrary sequence someone hands you is, in his words, a problem you pose to an
adversary, not a friend. The tractable version restricts the building blocks to a known, pre-characterized
set (specific promoters, ribosome binding sites, proteins with specific degradation tags) and asks only to
predict what a circuit built from *those* parts will do.

Even so, typical published accuracy for predicting an unseen circuit's behavior is on the order of 5- to
10-fold error — impressive for biology, inadequate for engineering a circuit meant to control production of
a protein that kills a cell inside a human body. More recent work, in preparation at the time of the
lecture, does better: with extensive characterization of regulatory elements such as repressor–promoter
pairs, mammalian-cell circuit behavior can be predicted to within about 20% on average. This does not
require the underlying rate constants (binding affinities, polymerase binding rates, transcription or
translation rates) — only the empirically measured input–output behavior of the repressor–promoter pair,
which turns out to be enough. Weiss names building fast, predicting behavior, and a large library of
well-characterized parts as the field's three central bottlenecks.

## Thinking about populations, not cells

**[36:25]–[38:38]** Returning to the pulse circuit, the actual bacterial population reproduces the
predicted pulse closely on average, but single-cell behavior is highly heterogeneous — the spread in peak
height and buildup time among individual cells is, in Weiss's word, "staggering." Stochastic simulations
built from this correlate reasonably well with the population-level spread.

The methodological point: engineering a *single* cell to behave reliably is the wrong target, because it
will fail. The right target is **statistical engineering** — designing a circuit so that a population of
cells produces a known *distribution* of behaviors. Weiss contrasts this with ordinary software, where "if
90% of the time the computer doesn't crash, that's pretty good" is not a standard anyone would actually
accept — but it is closer to what biology forces on this field than most engineers expect.

## Scaling to populations: pattern formation

**[38:38]–[43:22]** The same cell–cell communication idea extends from a single pulse to spatial pattern
formation, using an **incoherent feed-forward motif with two branches of different sensitivity**: the
diffusible signal activates one branch that turns the output *on*, and a second, less sensitive branch that
turns it *off* again — as a function of signal *concentration*, not time. The sensitive branch sets a low
threshold below which nothing activates; the less sensitive branch sets a high threshold above which the
output is repressed again. The result is a non-monotonic, low–high–low response — a **band-detect**
circuit.

With sender cells in the middle of a plate and receiver cells everywhere, a diffusing, decaying chemical
gradient forms, and each receiver reads its local concentration against the band-detect response —
producing a ring, or "bullseye," pattern where concentration falls inside the band. Modeling (about three
weeks) was fast; getting the circuit to work was again on the order of three years. Varying the thresholds
and reporters produced multiple ring patterns, and different sender placements more elaborate arrangements.

**[43:22]–[45:42]** Weiss connects this to ongoing work embedding the same circuitry in human iPS cells, so
communicating cells make coordinated differentiation decisions — one color meaning "become a neuron,"
another "muscle," another "bone" — toward designed three-dimensional tissue. He reports engineered cell–cell
communication working, programmed stem cell differentiation working, and iPS-cell-derived embryonic liver
buds (images shown but not described in enough detail to reconstruct) containing the range of cell types
known in the embryonic liver. The near-term application: differentiating a patient's own iPS cells into a
liver-like tissue on a chip and testing drug candidates on it, as a more predictive alternative to testing
in a mouse.

## A compiler for genetic circuits

**[45:42]–[55:38]** Weiss distinguishes two uses of computational modeling in the field's history. For
roughly its first eight to ten years, a model was typically built *after* a circuit already worked in the
lab, mainly to produce a figure correlating with already-obtained data for publication — not a design tool;
he says his own group is "just as guilty" of this. What is changing is the move toward circuits complex
enough (he cites a 20–25 component example related to a diabetes application) that intuition genuinely
breaks down, and a model supplies insight unobtainable by reasoning on a blackboard.

A more ambitious use is specifying a *desired behavior* and letting a tool propose candidate
implementations to build and test — a recent framework in his lab generates around 200 circuit variants in
about three hours. This motivates a **bio-compiler**, built with collaborators at BBN (Jake Beal) and
Boston University (Doug Densmore), on explicit analogy with a software compiler: a programmer in a
high-level language like MATLAB does not need to know the chip's microarchitecture, and a circuit designer
should not need to know a specific repressor's ribosome binding site. The pipeline: a program in a small
high-level language (Weiss shows a Lisp-like example — "if input is high, make cyan fluorescent protein,
else yellow") is translated into a **data-flow graph**, then an **abstract gene circuit** (an "IPTG sensor"
box expands into the small-molecule–repressor motif that implements it; a NOT box into a repressor–promoter
pair), and finally, matched against a library of characterized parts — a tool called "matchmaker" picks
specific proteins to avoid unwanted interactions — into an actual DNA sequence and robot instructions for
liquid-handling assembly.

**[55:38]–[59:53]** The compiler also optimizes, using techniques borrowed directly from software compilers.
Example: a naively generated circuit has an input repressing protein $A$, $A$ repressing $B$, and $B$
activating the output — four stages, where the output depends on $A$ only indirectly. Recognizing that $A$
represses $B$ and $B$ activates what $A$ could regulate directly is **copy propagation**: the compiler
rewrites $A$ to regulate the output directly, finds $B$ and its promoter now unused, and removes them,
shrinking the circuit to its true minimum without a human spotting the redundancy by eye. The difference
between four parts and three may not matter much, Weiss notes, but the same optimization applied to fifteen
versus five components materially changes how feasible a circuit is to build and debug. The tool handles
not just combinational logic but circuits with state and some spatial behavior; in an undergraduate course
he taught concurrently, students with no lab experience were taught to design with the tool — using only
the abstraction "a repressor reduces output when present" — before being taught the underlying mechanism
(for example, lac repressor DNA looping), a deliberate inversion of the usual teaching order that he
describes as untested before that term.

**[59:53]–[1:01:59]** Physically, a library of promoter–gene pairs lets new circuits be assembled in the
lab in about five days; Weiss cites circuits of 61–64 kilobases built this way by the same previously
inexperienced undergraduates.

## Composing modules: the loading problem

**[1:01:59]–[1:05:23]** Connecting separately-working modules introduces a failure mode single-module
engineering does not see. Weiss's example is a relaxation oscillator (an activator that activates itself,
repressed by a separate repressor of the activator) that works as simulated in isolation but stops working
once connected downstream. The cause is **retroactivity**, or loading: a downstream module is not a passive
load — because it draws on shared cellular resources, it has an "upstream" effect on the module driving it,
even though the circuit diagram's arrows point only one way. This is the phenomenon electronics engineers
solved decades ago with load drivers for high-fan-out circuits. With collaborator Domitilla Del Vecchio,
Weiss's group built an analogous genetic **load driver**, using a timescale-separation argument, restoring
a badly disrupted signal to close to its unloaded behavior — a step toward predictable composition from
pre-characterized modules.

## Application: a microRNA-based cancer classifier

**[1:05:23]–[1:09:01]** The lecture's running application is cancer therapeutics, where Weiss identifies
**specificity** as perhaps the single most important open problem: a therapeutic that reliably distinguishes
a tumor cell from a healthy cell can be made far more aggressive, since its side effects are controlled by
specificity rather than dose. His cautionary example is engineered killer T-cell therapy: a single
cell-surface marker is, unsurprisingly, rarely unique to tumor cells, so therapies built around one marker
have caused serious side effects in healthy tissue sharing that marker — driving current efforts (progress
in dishes, not yet clinical trials) toward multi-input logic, requiring one marker present *and* another
absent.

**[1:09:01]–[1:13:47]** Weiss, with a collaborator named in the transcript as "Coby Benson," pursued a
version where classification happens *entirely inside the cell*, using bioinformatically identified
microRNA profiles rather than surface markers: for HeLa cells, specific microRNAs that must be low and
others that must be high together distinguish HeLa from other tested cell types, as a Boolean statement
over microRNA levels. Weiss argues this is close to true by definition for any cell type — something must
differ, or it would not be a distinguishable type. The scheme also addresses tumor heterogeneity: distinct
subpopulations with different microRNA profiles each get their own AND-type classifier, combined with an OR
— like a drug cocktail targeting several cell states at once. The overall circuit computes this Boolean
function inside the cell and, only if it evaluates true, expresses a killer protein.

**[1:13:47]–[1:16:11]** Requiring several microRNAs to all be *low* is implemented directly: placing a
target site for each in the output (killer) gene's transcript, so the mRNA is degraded whenever any one of
those microRNAs is present, surviving only when all are absent — a multi-input AND gate over inverted
inputs. Requiring a microRNA to be *high* is harder, since a microRNA cannot activate, only repress. The
solution reuses the earlier repressor cascade: a microRNA represses a repressor protein (named in the
lecture as LacI), which represses the output gene, so high microRNA gives low repressor gives high output —
a double negative behaving like a positive requirement, composing with the direct target-site logic on the
same gene into a function of the form "this microRNA is high, and these others are low."

## Combining several "must be high" inputs: AND or OR, by wiring

**[1:16:11]–[1:20:35]** The most carefully developed point in the lecture, worked through with the
audience rather than stated outright, is what happens when *more than one* microRNA must be required high.
If miR-21 and miR-17 must both be high, one wiring is: each microRNA represses its **own, separate copy**
of the LacI gene, and both copies independently repress the same output promoter. Since either copy alone
suffices to repress the output, it can turn on only if *both* copies are silenced, requiring *both*
microRNAs present — if only one is present, the other LacI copy still blocks the output. This wiring
realizes an **AND** over the two inputs.

<figure>
<svg viewBox="0 0 420 230" role="img" aria-label="Two wirings of the same repressor that realize AND versus OR logic over two microRNA inputs">
  <defs>
    <marker id="arrB" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <text x="90" y="16" text-anchor="middle" font-size="12" fill="currentColor">separate copies: AND</text>
  <rect x="10" y="30" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="45" y="47" text-anchor="middle" font-size="11" fill="currentColor">miR-21</text>
  <rect x="10" y="80" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="45" y="97" text-anchor="middle" font-size="11" fill="currentColor">miR-17</text>
  <rect x="110" y="30" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="145" y="47" text-anchor="middle" font-size="11" fill="currentColor">LacI copy A</text>
  <rect x="110" y="80" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="145" y="97" text-anchor="middle" font-size="11" fill="currentColor">LacI copy B</text>
  <rect x="220" y="55" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="255" y="72" text-anchor="middle" font-size="11" fill="currentColor">output</text>
  <line x1="80" y1="43" x2="106" y2="43" stroke="currentColor" marker-end="url(#arrB)"/>
  <line x1="80" y1="93" x2="106" y2="93" stroke="currentColor" marker-end="url(#arrB)"/>
  <line x1="180" y1="43" x2="224" y2="60" stroke="currentColor"/>
  <line x1="214" y1="55" x2="224" y2="60" stroke="currentColor" stroke-width="2"/>
  <line x1="180" y1="93" x2="224" y2="76" stroke="currentColor"/>
  <line x1="214" y1="80" x2="224" y2="76" stroke="currentColor" stroke-width="2"/>
  <text x="90" y="145" text-anchor="middle" font-size="12" fill="currentColor">shared copy: OR</text>
  <rect x="10" y="158" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="45" y="175" text-anchor="middle" font-size="11" fill="currentColor">miR-21</text>
  <rect x="10" y="194" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="45" y="211" text-anchor="middle" font-size="11" fill="currentColor">miR-17</text>
  <rect x="150" y="176" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="185" y="193" text-anchor="middle" font-size="11" fill="currentColor">LacI</text>
  <rect x="280" y="176" width="70" height="26" fill="none" stroke="currentColor"/>
  <text x="315" y="193" text-anchor="middle" font-size="11" fill="currentColor">output</text>
  <line x1="80" y1="171" x2="146" y2="183" stroke="currentColor" marker-end="url(#arrB)"/>
  <line x1="80" y1="207" x2="146" y2="195" stroke="currentColor" marker-end="url(#arrB)"/>
  <line x1="220" y1="189" x2="276" y2="189" stroke="currentColor"/>
  <line x1="266" y1="184" x2="276" y2="189" stroke="currentColor" stroke-width="2"/>
</svg>
<figcaption>Two wirings of the same repressor relative to two microRNA inputs: separate target copies of the repressor realize an AND over the microRNAs, a single shared copy realizes an OR.</figcaption>
</figure>

If instead both target sites sit on a **single shared copy** of LacI, either microRNA alone is enough to
degrade that one transcript and relieve repression — the output turns on if miR-21 is present *or* miR-17
is present, an OR over the same two inputs, from the same repressor acting through the same promoter.
Weiss's point, reached only after walking the audience through both cases and a wrong guess about what
converging branches would do, is that the AND/OR distinction is set purely by whether the repressor's
targets are separate gene copies or sites on one shared copy — not by anything about the microRNAs or the
promoter themselves.

## Sources

All material is from the lecture transcript: `recordings/lectures/21.md` (MIT 7.91J, Foundations of
Computational and Systems Biology, Spring 2014; guest lecture by Prof. Ron Weiss). Timestamps given inline
above locate each section within that file.

Referred to in the lecture but not contained in the transcript (no slides were supplied for this guest
lecture):

- The circuit diagrams/slides for the inverter, the implies gate, the logic cascade, the pulse generator,
  the band-detect/pattern-formation circuit, the compiler pipeline, the oscillator, and the final microRNA
  classifier circuit were shown on screen and described verbally; they are not reproduced here beyond what
  the narration itself recovers. The two figures above reconstruct only the mechanisms the lecture
  explicitly argued through step by step: the pulse-generating feed-forward motif, and the AND/OR wiring of
  convergent repression.
- Photographs of the bullseye bacterial pattern on a plate, the iPS-cell-derived embryonic liver bud, and
  the organ-on-a-chip concept were shown but not described in enough detail in speech to reconstruct.
- The bio-compiler's online design tool ("there's a website... get a free account") is referred to but not
  named in the transcript.
- A paper on mammalian-cell prediction accuracy is referred to as submitted/in preparation at the time of
  the lecture but not identified by title or venue.
- The name of Weiss's microRNA-classifier collaborator is transcribed as "Coby Benson," very likely a
  mis-hearing of a proper name; reproduced here as transcribed rather than silently corrected.

---

[← 20. Genome-Wide Association Studies](20-genome-wide-association-studies.md) · [Contents](index.md) · [22. Engineering Genomes to Test Causality →](22-engineering-genomes-to-test-causality.md)
