---
title: "3. Experimental Design and Randomization"
course: "GTPB Psls20"
chapter: 3
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Experimental Design and Randomization

## What this covers

This chapter asks what has to be true of a study *before* any data analysis can be trusted: how
to compare a treated group to a group that tells you what would have happened anyway, and how to
assign subjects to those groups so that the comparison is fair. It assumes only the everyday
distinction between a population and a sample drawn from it, and sets up the vocabulary —
control, confounding, randomization, blocking — that later chapters on estimation and inference
rely on.

## Where design sits in a study

A statistical study runs in three stages, and design is the first of them, not an afterthought
bolted on before the "real" analysis begins.

<figure>
<svg viewBox="0 0 360 320" role="img" aria-label="Population, experimental design, sample, descriptive statistics, and inference arranged as a cycle">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="30" y="20" width="300" height="90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="38" font-size="12" fill="currentColor">Population</text>
  <circle cx="70" cy="65" r="3" fill="currentColor"/>
  <circle cx="95" cy="80" r="3" fill="currentColor"/>
  <circle cx="120" cy="60" r="3" fill="currentColor"/>
  <circle cx="150" cy="90" r="3" fill="currentColor"/>
  <circle cx="180" cy="70" r="3" fill="currentColor"/>
  <circle cx="210" cy="55" r="3" fill="currentColor"/>
  <circle cx="235" cy="85" r="3" fill="currentColor"/>
  <circle cx="265" cy="65" r="3" fill="currentColor"/>
  <circle cx="290" cy="80" r="3" fill="currentColor"/>
  <circle cx="150" cy="50" r="3" fill="currentColor"/>
  <circle cx="200" cy="95" r="3" fill="currentColor"/>
  <rect x="30" y="190" width="300" height="90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="208" font-size="12" fill="currentColor">Sample</text>
  <g fill="currentColor">
    <circle cx="70" cy="225" r="3"/><circle cx="130" cy="225" r="3"/><circle cx="190" cy="225" r="3"/><circle cx="250" cy="225" r="3"/><circle cx="300" cy="225" r="3"/>
    <circle cx="70" cy="250" r="3"/><circle cx="130" cy="250" r="3"/><circle cx="190" cy="250" r="3"/><circle cx="250" cy="250" r="3"/><circle cx="300" cy="250" r="3"/>
    <circle cx="70" cy="270" r="3"/><circle cx="130" cy="270" r="3"/><circle cx="190" cy="270" r="3"/><circle cx="250" cy="270" r="3"/><circle cx="300" cy="270" r="3"/>
  </g>
  <line x1="100" y1="112" x2="100" y2="188" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="108" y="155" font-size="11" fill="currentColor">Experimental design (1)</text>
  <line x1="270" y1="188" x2="270" y2="112" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="278" y="155" font-size="11" fill="currentColor">Estimation &#38;</text>
  <text x="278" y="169" font-size="11" fill="currentColor">inference (3)</text>
  <text x="180" y="300" text-anchor="middle" font-size="11" fill="currentColor">Data exploration &#38; descriptive statistics (2)</text>
</svg>
<figcaption>Individuals vary in the population (top). Experimental design (1) turns some of them
into a sample; data exploration and descriptive statistics (2) summarise what was observed in
that sample; estimation and inference (3) carries a conclusion back to the population.</figcaption>
</figure>

Design is stage (1): it decides who ends up in the sample and how they are allocated to
treatments, before any of the later stages can be trusted.

## Why you need a good control

To say anything about the effect of an intervention, you need a comparison group — a group that
tells you what would have happened to the same subjects without the intervention. This is harder
to arrange than it sounds:

- A **pretest/post-test design** — measuring subjects before and after giving them a drug, with no
  placebo group — cannot separate the drug's effect from anything else that changed over the same
  period. There is no control.
- In an **observational study**, the groups being compared (e.g. people who happened to take a
  drug versus those who did not) are often not comparable in the first place, and drawing a causal
  conclusion from them needs statistical methods beyond simple comparison.
- **Double blinding** — neither the subject nor the person assessing the outcome knows which
  treatment arm the subject is in — removes a further source of bias in how outcomes are reported
  or assessed.

Underlying all of this is **confounding**: a confounder is a variable that differs systematically
between the groups being compared and that also affects the outcome. When one is present, a
difference observed between the groups can be due to the confounder rather than to the treatment
under study, and the comparison stops being informative about the treatment at all.

A **randomized study** — assigning subjects to treatment arms at random rather than by any
systematic rule — is the standard way to make the groups comparable: since assignment does not
depend on any subject characteristic, no characteristic (measured or not) can systematically favour
one arm over another.

## Randomization

Randomization means allocating subjects to arms completely at random, with no systematic rule.
There is more than one way to do this, and they trade off differently between simplicity and
balance.

### Simple randomization

Each subject's arm is decided independently, as if by an independent fair coin toss. This is the
simplest scheme, but it can produce unequal numbers of subjects in each arm purely by chance: in
about 5% of studies of 100 subjects you would see an imbalance of at least 60:40, and in about 5%
of studies of 1000 subjects an imbalance of at least 531:469 (these are the tail probabilities of a
$\mathrm{Binomial}(n, \tfrac12)$ split). An imbalance of this kind is not wrong — it is simply what
independent random assignment does — but it costs precision: a comparison between two groups is
most precise when the groups are the same size.

### Balanced randomization

To avoid that loss of precision, subjects can be randomized in blocks that are constrained to
contain equal numbers of each treatment. For two arms A and B, a block of 2 is either the sequence
AB or BA (chosen at random); a block of 4 is one of AABB, ABAB, ABBA, BABA, BAAB, BBAA. Blocking in
this way guarantees, up to the block size, equal numbers of subjects in each arm.

Balanced randomization only balances the *count* in each arm — it does nothing to guarantee that,
say, the number of men receiving the treatment equals the number of men in the control arm. In a
small study it is entirely possible for the arms to be unbalanced in some other characteristic
(gender, race, age, ...) purely by chance. That, too, is not a mistake — it is what happens at
random — but it is again a loss of precision, and if the characteristic is a confounder it can
distort the comparison.

### Stratified randomization

If a particular characteristic — gender, say — is one you want to guard against imbalance in
specifically, you can avoid it by stratifying: split the subjects into strata by that
characteristic first, then run balanced randomization separately *within* each stratum. This
guarantees the treatment arms are balanced within every stratum, and hence balanced overall.

## Blocking

**Blocking** is the general version of the same idea: when a nuisance factor (something not of
scientific interest, but which could affect the outcome) is known in advance, assign treatments so
that they are spread evenly across it, rather than letting the treatment happen to line up with it.

The lecture illustrated the failure this is meant to prevent with a qPCR gene-expression example
comparing three conditions — diabetic medium (dm), non-diabetic medium (nd), and a control (co) —
using 4 biological replicates and 2 technical replicates per biological replicate. When those
replicates were run across two plates, A and B, treatment and plate ended up almost entirely
confounded: essentially every sample of a given treatment sat on the same plate. Any batch effect
between plate A and plate B — a systematic difference having nothing to do with the treatment,
just with which plate a sample happened to be processed on — is then indistinguishable from a
treatment effect, because the data give no way to tell the two apart. Blocking the design by plate
(spreading each treatment across both plates) would have separated the two.

## Sample size

The sample size, together with the design, determines how precise the eventual estimate of the
treatment effect will be: the larger the sample, the more precise the result.

## Putting it together

Design is what makes the later stages of a study — descriptive statistics and inference — mean
what they claim to mean. To assess the effect of a treatment you need comparable and
representative groups with and without it, which is exactly what a good control provides. Whether
that comparison can be made cleanly depends on the kind of study: in an *observational* study the
researcher does not choose who gets the treatment — the subject or their doctor did — so the
treated and untreated groups may differ in ways connected to that choice; in an *experimental*
study the researcher assigns the treatment, and randomization is what makes the resulting groups
comparable despite that assignment. Confounding that has not been designed away this way can
sometimes still be corrected for afterwards in the statistical analysis, but only for the
confounders that were actually registered — which is one more reason to design the comparison
correctly from the start rather than to rely on fixing it up later.

## Sources

- Notes: `theory/03-experimentalDesign/01-introduction.md` — the population/sample/design/
  inference figure (reconstructed here from the R plotting code that drew it) and the "Need for a
  good control" points (pretest/post-test design, observational studies, double blinding,
  confounding, randomized studies).
- Notes: `theory/03-experimentalDesign/02-randomization.md` — simple, balanced, and stratified
  randomization; the blocking section and qPCR example; sample size; and the wrap-up points on
  observational versus experimental studies and correcting for registered confounders.
- Referred to but not reproduced here, since only alt text and a link were supplied, not the
  images or document themselves: a stratification diagram (`assets/figs/stratification.png`), two
  qPCR design diagrams (`assets/figs/qpcrBadDesign1.png`, `assets/figs/qpcrBadDesign2.png`), and
  the Nature Methods "Points of Significance: Blocking" article (`nmeth.3005.pdf`).
- Both source files: GTPB PSLS20, `theory/03-experimentalDesign.Rmd`, licensed CC BY 4.0.

---

[← 2. Population, Sample, and Random Variables](02-population-sample-and-random-variables.md) · [Contents](index.md) · [4. Describing and Relating Quantitative Data →](04-describing-and-relating-quantitative-data.md)
