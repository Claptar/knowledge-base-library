---
title: "16. Motif Discovery: EM and Gibbs"
course: "MIT 6047"
chapter: 16
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Motif Discovery: EM and Gibbs

## What this covers

A set of co-regulated genes shares a short DNA pattern upstream of each of them — the binding site
for the transcription factor that regulates all of them — but the pattern is not the same string
twice, its exact location varies, and no one has told you where it starts. This chapter answers:
given only the sequences, how do you recover the pattern and its locations at the same time? It
assumes the reader already has Bayes' rule, the idea of a hidden Markov model, and the general
shape of the EM algorithm (an E-step and an M-step iterated to convergence); it does not re-derive
EM from scratch, only applies it to this specific problem.

## Why motif-finding is hard

A **motif** is a short (6–8 base) recurring DNA (or RNA) pattern with a defined biological function
— a promoter or enhancer element, a splicing signal — and a specific stretch of sequence that
matches it in one gene's regulatory region is an **instance** of that motif. Motifs are read by
transcription factors, by microRNAs (via complementarity), by nucleosomes (via GC content), and by
other RNAs, and once bound they activate or repress the gene they sit near. Because a transcription
factor typically controls many genes involved in related processes, genes sharing a motif tend to
share a function — which is also how many motifs were first found: by looking upstream of genes
already known to be co-regulated.

Three things make finding a motif computationally from a set of sequences hard rather than a simple
string search:

- **Degeneracy.** A transcription factor does not check every base by opening the double helix and
  reading complementarity; many scan the major and minor grooves between the two backbones, so
  depending on the protein's shape it may only be sensitive to purine-vs-pyrimidine or strong-vs-weak
  base distinctions, or may not contact some positions of the motif at all. So a "motif" is really a
  family of related strings, not one fixed k-mer, and a plain local-alignment search for one k-mer
  will miss most of its instances.
- **Variable location.** The motif's distance and side (upstream or downstream) relative to the gene
  it regulates is not fixed — it can be anywhere from a few bases to $10^4$–$10^7$ bases away.

To keep the problem tractable, the methods in this chapter make two simplifying assumptions: bases
within the motif are **independent** of one another (no pairwise correlations — modelling those would
blow up the parameter space and invite overfitting), and every instance of the motif has the **same
fixed length**. Both are approximations to real biology, but without them the search space is
intractable.

## Representing a motif: the position weight matrix

Because instances vary, a motif is not stored as one string but as a **position weight matrix**
(PWM, also called a profile matrix): a table $p_{ck}$ giving the frequency of base $c$ at position
$k$ of the motif, for $k = 1, \dots, W$ where $W$ is the motif's width. A background frequency
$p_{c,0}$ — the distribution of base $c$ outside any motif — is kept alongside it. An example, for
an 8-base motif:

| position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A** | 0.1 | 0.3 | 0.1 | 0.2 | 0.2 | 0.4 | 0.3 | 0.1 |
| **C** | 0.5 | 0.2 | 0.1 | 0.1 | 0.6 | 0.1 | 0.2 | 0.7 |
| **G** | 0.2 | 0.2 | 0.6 | 0.5 | 0.1 | 0.2 | 0.2 | 0.1 |
| **T** | 0.2 | 0.3 | 0.2 | 0.2 | 0.1 | 0.3 | 0.3 | 0.1 |

Each column sums to 1; a column close to $(0.25,0.25,0.25,0.25)$ is a near-wildcard position, one
concentrated on a single base is a strongly conserved position — exactly the degeneracy described
above.

Given a target set of co-regulated sequences, several strategies can locate the shared motif:
local alignment of the sequences and inspection of high-scoring blocks; modelling the promoter
region with a hidden Markov model and pulling out non-random stretches; restricting the search using
prior knowledge of what the motif should look like; searching for blocks conserved between species;
counting k-mer frequencies directly; or the probabilistic family — EM, Gibbs sampling, and a greedy
variant — that this chapter develops. Plain k-mer counting is the cheapest of these but is also the
least reliable on its own: many common words in a promoter region are not motifs at all, and the
most frequent k-mer need not be the true motif, since a transcription factor can be unable to bind
if its motif is in excess. A partial fix is to score k-mers by their frequency in promoter regions
*relative to* background regions rather than by raw count — a useful post-processing filter, but
not by itself a discovery method.

## The shared trick: positions and the motif determine each other

The probabilistic methods all exploit the same observation. If you already knew where the motif
started in every sequence, computing the PWM would be trivial — just count bases at each offset.
Conversely, if you already had the PWM, finding the most likely start position in each sequence
would also be easy — score every window against the PWM. Neither is known in advance, so all three
algorithms iterate between the two: guess starting positions, estimate a PWM from them, use the PWM
to re-estimate the starting positions, and repeat until the PWM stops changing.

Formalize the guess about positions as a matrix $Z$, where $Z_{ij}$ is the probability that a motif
instance starts at position $j$ in sequence $i$. EM, Gibbs sampling, and the greedy algorithm differ
only in **how they turn $Z_{i\cdot}$, the row of position-probabilities for one sequence, into an
update** — this is the one distinction worth holding onto through the next three sections, and it is
made visually explicit in the [comparison figure](#comparing-the-three-what-each-does-with-the-same-z)
below.

## Expectation–Maximization

**Step 1 — initialize.** Start from some initial PWM. If starting locations for the motif in each
sequence are already known (e.g. from an alignment), the PWM is just the base frequencies at those
locations; otherwise, initialize by choosing starting positions at random. Zero counts in the PWM
are dangerous (they make some sequence infinitely improbable), so pseudocounts are added wherever a
cell would otherwise be zero.

**Step 2 — expectation.** Compute $Z_{ij}$, the probability that sequence $i$'s motif instance
starts at $j$, from the current PWM by Bayes' rule:

$$Z_{ij}^t = \frac{\Pr^t(X_i \mid Z_{ij}=1)\,\Pr^t(Z_{ij}=1)}{\sum_{k=1}^{L-W+1} \Pr^t(X_i \mid Z_{ik}=1)\,\Pr^t(Z_{ik}=1)}$$

where $L$ is the length of sequence $X_i$ and $W$ the motif width, and the likelihood of the whole
sequence given a start at $j$ factors into three independent pieces — background before the motif,
the motif itself, and background after it:

$$\Pr(X_i \mid Z_{ij}=1, p) = \underbrace{\prod_{k=1}^{j-1} p_{c_k,0}}_{\text{before motif}} \cdot \underbrace{\prod_{k=j}^{j+W-1} p_{c_k,\,k-j+1}}_{\text{motif}} \cdot \underbrace{\prod_{k=j+W}^{L} p_{c_k,0}}_{\text{after motif}}$$

Here $c_k$ denotes whichever base actually sits at position $k$ of sequence $X_i$. In EM, $Z$ is not
a single guess but a full distribution over every candidate start — every position in every sequence
gets some (possibly tiny) weight of "being" the motif.

**Step 3 — maximization.** Re-estimate the PWM and background distribution as the $Z$-weighted base
counts, plus pseudocounts $d_{c,k}$:

$$p_{c,k}^{(t+1)} = \frac{n_{c,k} + d_{c,k}}{\sum_b (n_{b,k} + d_{b,k})}, \qquad n_{c,k} = \begin{cases} \displaystyle\sum_i \sum_{\{j\,\mid\,X_{i,j+k-1}=c\}} Z_{ij} & k > 0 \ (\text{motif position}) \\[4pt] n_c - \sum_{j=1}^{W} n_{c,j} & k = 0 \ (\text{background}) \end{cases}$$

where $n_c$ is the total count of base $c$ over all the sequences. So every occurrence of base $c$ at
the right offset from a candidate start contributes to that motif column, weighted by how likely
that start is; leftover counts of $c$, not attributed to any motif position, go to the background.

**Step 4 — repeat** steps 2 and 3 until the PWM stops changing appreciably (a convenient convergence
test is to track the largest per-cell change in the PWM and stop once it drops below a threshold).

EM is **deterministic**: given the same starting positions it always converges to the same answer,
because the M-step averages over the *entire* distribution $Z$ rather than committing to any one
guess. That averaging is also its weakness — it makes EM prone to getting stuck at a local maximum
close to wherever it started, so in practice it is run many times from different random
initializations to get a sense of the solution landscape and reduce the chance the reported motif is
just a local optimum.

## Gibbs sampling

Gibbs sampling solves the same chicken-and-egg problem but replaces EM's *average* with a *sample*,
which makes it stochastic rather than deterministic. It also restricts the E-step-like calculation to
the motif window itself, rather than scoring the whole sequence against background.

**Step 1 — initialize.** As with EM, start from a random choice of starting position in every
sequence (and hence a random initial PWM).

**Step 2 — remove.** Pick one sequence $X_i$ and take it, together with its current guessed start
position, out of the set.

**Step 3 — update.** Recompute the PWM from the *remaining* sequences only, counting bases at each
motif offset (with pseudocounts as before).

**Step 4 — sample.** Using this updated PWM, score every candidate start position $j$ in the excluded
sequence $X_i$ by the odds that the window at $j$ was generated by the motif model rather than by
background:

$$A_{ij} = \frac{\prod_{k=j}^{j+W-1} p_{c_k,\,k-j+1}}{\prod_{k=j}^{j+W-1} p_{c_k,0}}$$

Normalizing these scores across all candidate $j$ turns them into the sampling distribution $Z_{ij}$,
and a **new** starting position for $X_i$ is drawn at random from it — not necessarily the
highest-scoring one.

**Step 5 — iterate.** Put $X_i$ back with its newly sampled position, and loop to step 2 (removing a
different sequence) until the PWM converges.

Because each round commits to one sampled position rather than smearing weight across all of them,
Gibbs sampling depends much less on where it started than EM does, and is correspondingly less prone
to getting trapped in a local optimum — though it is not guaranteed to find the global one either,
so it too is normally run several times and the results compared. It is also simpler to implement
than EM. Two motif-finding programs built on this scheme are AlignACE and BioProspector, both of
which run the sampler from several starting values and report the motifs that recur; a general-purpose
Gibbs sampler (not specific to motifs) is implemented in WinBUGS.

## Finding motifs de novo, and validating them

Both algorithms above assume you already have a set of genes suspected to be co-regulated — from a
differential-expression experiment, say, or a ChIP-seq pulldown for a transcription factor of
interest. Both routes carry a cost: differential expression requires knowing what biological
condition to probe for, and is subject to the biases of that experiment; ChIP-seq requires already
having a transcription factor of interest and a working, specific antibody against it, which can be
expensive to develop.

An alternative that needs neither is to use **genome-wide conservation**: because functional
elements tend to be conserved across related species while most surrounding sequence drifts freely,
aligning genomes from close species and scanning specifically within the conserved "islands" enriches
strongly for functional motifs. This is not perfect on its own — bases flanking a motif are
sometimes conserved too, without being part of the functional element — so the useful move is to look
for *enrichment*: conserved k-mers that occur disproportionately in intergenic, upstream regions
compared to a control region such as coding sequence, since a true regulatory motif should cluster
near promoters rather than appear at the background rate everywhere. The same conservation signal can
be pushed further to find **degenerate** motifs, by searching for two shorter, non-degenerate blocks
conserved together with a variable-length gap between them, then extending the match greedily toward
a local optimum. Evolutionary substitution patterns can also reveal which motifs are degenerate in
the first place: if one k-mer is repeatedly replaced by a related one across evolutionary time, that
substitution pattern is evidence the two are instances of the same, degenerate motif, and clustering
motifs by this kind of substitution can group them accordingly. The underlying biological argument —
that conservation of a sequence implies selective pressure on it — was made by Professor Kellis in
2003; his thesis is the source referred to but not reproduced here.

Whatever the discovery route, a predicted motif is treated as more credible if it also shows one or
more of: enrichment among co-regulated genes (or more broadly among genes expressed in a common
tissue); overlap with independent transcription-factor binding data; enrichment among genes in the
same protein complex; a positional bias relative to the transcription start site, or a bias toward
intergenic versus coding sequence (motifs are generally depleted in coding regions); or similarity to
an already-known transcription factor motif — though a match to a "known" motif is only weak
evidence, since not every real motif is conserved and not every catalogued motif is itself exactly
right.

## The greedy algorithm, and why it is rarely used

The greedy algorithm is Gibbs sampling with one change to Step 4: instead of *sampling* a new start
position from $Z_{i\cdot}$, it always picks the single highest-scoring position outright. This makes
it a little faster than Gibbs sampling per iteration, but considerably less likely to land on the
global optimum — most damagingly when the distribution over candidate positions is fairly flat, in
which case greedy throws away almost all of that distribution's information to keep only its single
largest entry. It is included here mainly as a foil for the comparison below, since it is not much
used in practice.

## Comparing the three: what each does with the same $Z$

All three algorithms compute essentially the same thing — a distribution $Z_{i\cdot}$ over where the
motif could plausibly start in sequence $i$ — and differ only in what they do with it: greedy keeps
only its mode, EM folds the whole distribution into a weighted average, and Gibbs draws one sample
from it.

<figure>
<svg viewBox="0 0 500 210" role="img" aria-label="The same distribution over candidate motif start positions used three different ways: greedy keeps only the tallest bar, EM uses all bars weighted by height, Gibbs samples one bar at random.">
  <text x="90" y="20" text-anchor="middle" font-size="12" fill="currentColor">Greedy</text>
  <line x1="20" y1="170" x2="160" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <rect x="36" y="155" width="18" height="15" fill="currentColor" fill-opacity="0.15"/>
  <rect x="66" y="90" width="18" height="80" fill="currentColor"/>
  <rect x="96" y="125" width="18" height="45" fill="currentColor" fill-opacity="0.15"/>
  <rect x="126" y="150" width="18" height="20" fill="currentColor" fill-opacity="0.15"/>
  <text x="45" y="184" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="75" y="184" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="105" y="184" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="135" y="184" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="90" y="200" text-anchor="middle" font-size="11" fill="currentColor">keeps the mode only</text>

  <text x="260" y="20" text-anchor="middle" font-size="12" fill="currentColor">EM (average)</text>
  <line x1="190" y1="170" x2="330" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <rect x="206" y="155" width="18" height="15" fill="currentColor" fill-opacity="0.35"/>
  <rect x="236" y="90" width="18" height="80" fill="currentColor" fill-opacity="0.35"/>
  <rect x="266" y="125" width="18" height="45" fill="currentColor" fill-opacity="0.35"/>
  <rect x="296" y="150" width="18" height="20" fill="currentColor" fill-opacity="0.35"/>
  <text x="215" y="184" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="245" y="184" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="275" y="184" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="305" y="184" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="260" y="200" text-anchor="middle" font-size="11" fill="currentColor">every position counts, weighted</text>

  <text x="430" y="20" text-anchor="middle" font-size="12" fill="currentColor">Gibbs (sample)</text>
  <line x1="360" y1="170" x2="500" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <rect x="376" y="155" width="18" height="15" fill="currentColor" fill-opacity="0.15"/>
  <rect x="406" y="90" width="18" height="80" fill="currentColor" fill-opacity="0.15"/>
  <rect x="436" y="125" width="18" height="45" fill="currentColor"/>
  <rect x="466" y="150" width="18" height="20" fill="currentColor" fill-opacity="0.15"/>
  <text x="445" y="115" text-anchor="middle" font-size="11" fill="currentColor">drawn</text>
  <text x="385" y="184" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="415" y="184" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="445" y="184" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="475" y="184" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="430" y="200" text-anchor="middle" font-size="11" fill="currentColor">one draw, not the mode</text>
</svg>
<figcaption>The same row of the Z matrix — a distribution over where the motif starts in one
sequence — used three ways. Greedy discards everything but the tallest bar (position 2 here).
EM folds all four positions into the next PWM, weighted by height, so it never fully discards a
candidate. Gibbs draws a single position at random according to the heights — in this draw,
position 3, not the tallest — which is why its trajectory does not collapse onto whatever looked
best at the first step.</figcaption>
</figure>

This difference in how much of $Z$ survives each update is exactly why EM is deterministic and
prone to local optima, greedy is fast but brittle, and Gibbs sampling explores more of the space at
the cost of a slower, noisier search.

## Sequence models: OOPS, ZOOPS, and TCM

The algorithms above implicitly assumed **exactly one** motif occurrence per sequence — this
assumption is itself a named model, **OOPS** (One-Occurrence-Per-Sequence). Lawrence and Reilly
(1990) generalized it to **ZOOPS** (Zero-or-One-Occurrence-Per-Sequence), which allows a sequence to
carry no instance of the motif at all rather than forcing one. A third model, **TCM**
(Two-Component Mixture) — allowing more than one occurrence per sequence — is named in the source
material but its description is not developed there beyond the name.

## Exercises

No problem set was supplied with this lecture.

## Sources

All content is from the MIT OCW 6.047 (Computational Biology, Fall 2015) compiled course notes
chapter *Regulatory Motifs, Gibbs Sampling, and EM* (numbered as Chapter 17 in that compiled
volume), sections 17.1 through 17.9 — specifically:

- Motif basics, degeneracy, and the two simplifying assumptions: §17.1.1–17.1.2.
- The PWM, its example table (reused here for both the PWM definition and the worked EM/Gibbs
  example, corresponding to the source's Figures 17.2 and 17.5, which share the same numbers), and
  the six discovery strategies with the caveats on k-mer counting: §17.1.3.
- The $Z$-matrix idea and the E-step/M-step derivation, including the Bayes'-rule formula for
  $Z_{ij}$, the before/motif/after factorization, and the PWM update formula: §17.2.
- Gibbs sampling steps 1–5 and the $A_{ij}$ score, plus AlignACE, BioProspector, and WinBUGS as named
  implementations: §17.3.
- De novo discovery via evolutionary conservation, the degenerate-motif extension, motif clustering
  by evolutionary substitution, and the validation criteria: §17.4. Professor Kellis's 2003 PhD
  thesis is named there as the source of the selective-pressure argument but its content is not
  itself reproduced in the lecture notes — a pointer, not a supplied source.
- The greedy algorithm: §17.7.1.
- The Z-matrix comparison across greedy/EM/Gibbs (source Figures 17.4/17.9, both captioned
  identically): §17.8. The SVG diagram in this chapter is a redrawing of that comparison; the
  underlying argument is the source's, the specific bar heights are illustrative.
- OOPS/ZOOPS/TCM: §17.9. The source's own text breaks off mid-sentence immediately after naming TCM
  ("Finally, TCM (Two-Component Mixture)"), before defining what distinguishes it from OOPS and
  ZOOPS — this chapter does not supply that missing definition.

Two headings present in the source table of contents and body but without any accompanying body
text — "17.5 Evolutionary signatures for instance identification" and "17.6 Phylogenies, Branch
length score, Confidence score" (with sub-heading "Foreground vs. background. Real vs. control
motifs.") — are omitted here for the same reason: there is nothing under them to draw from. The
source's table of contents also lists further figures (17.10–17.13, covering OOPS/ZOOPS sequence
diagrams, an entropy/information-content treatment of sequence logos, and a worked lexA
binding-site example using low-GC content and Kullback–Leibler distance) that are referenced by
number but whose text is not present in the supplied material, so information content, sequence
logos, and the lexA example are not covered in this chapter.

The source file itself notes that it was reconstructed by a model from a PDF with no extractable
text layer, and that every equation in it is unverified against the original — a caveat worth
keeping in mind if the exact formulas here matter for later work, and the reason for standardizing
one notational slip in the original (an early paragraph calls the *motif* length $L$, while the
E-step section uses $L$ for the *sequence* length and $W$ for the motif; this chapter uses $L$ for
sequence length and $W$ for motif width throughout, matching the later, more detailed section).

---

[← 15. Naive Bayes and SVM Classification](15-naive-bayes-and-svm-classification.md) · [Contents](index.md)
