---
title: "24. Experimental Design and Blocking"
course: "StatOmics Sga21"
chapter: 24
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Experimental Design and Blocking

## What this covers

A quantitative proteomics workflow (estimate peptide/protein abundances, then test them for
differential abundance) sits on top of an experimental design, and the design decides how much of
that later analysis can actually be trusted. This chapter covers the vocabulary for talking about
design — experimental units versus observational units, pseudo-replication, blocking and
confounding — and then applies it to two real datasets used later in the tutorial (a mouse T-cell
proteome and a heart proteome) to see what a good and a bad design look like in practice. It assumes
the generic differential-abundance workflow (protein/peptide abundances from a quantitative LC-MS
run, tested with a model such as msqrob2) as background, and asks how the way the samples were
collected should change that model.

## Experimental units versus observational units

Two kinds of "unit" are easy to conflate in a proteomics experiment:

- An **experimental unit** is the object a treatment is actually applied to — a biological repeat.
  In a knockout-versus-wild-type experiment this is a mouse, a culture, a patient: e.g. three
  knockout mice and three wild-type mice.
- An **observational unit** is what is actually measured. In a shotgun proteomics run this is an
  individual peptide intensity, and there are many peptides per protein per sample.

The number of experimental units in a proteomics experiment is typically small (a handful of
biological repeats per condition); the number of observational units is large, because every
protein is represented by many peptides, each measured in every sample.

## Pseudo-replication

Because each protein has many peptide-level measurements per sample, treating each peptide
intensity as an independent replicate of the *biological* effect is a mistake: it inflates the
apparent sample size without adding real biological information. The peptide intensities within
one sample are correlated (they all reflect the same underlying protein abundance in that one
biological repeat), and a model that ignores this — pretending peptide count is replicate count —
will systematically understate the uncertainty on a protein's estimated effect. This is
**pseudo-replication**.

Two ways to deal with it, both supported by msqrob2:

1. **Summarize first.** Collapse the peptide intensities into one protein expression value per
   sample during preprocessing, then fit the statistical model at the protein level. There is no
   more pseudo-replication, because now there is exactly one value per experimental unit.
2. **Model the correlation.** Keep the peptide-level data and fit a mixed model with a random
   effect for sample, which explicitly absorbs the correlation between peptides belonging to the
   same protein measured in the same sample.

The tutorial works with the summarization approach: it is computationally lighter, and the
resulting model is simpler to teach, even though the mixed-model route is available too.

A related point about what design *can't* fix: in a typical proteomics dataset, the technical
variability of an intensity measurement (how much a peptide's measured intensity fluctuates on
its own) can be estimated very precisely, because there are so many peptide measurements. But the
ability to generalize an observed effect from the sampled biological repeats to the wider
population is limited by how many biological repeats there are — and that is usually small. Hence
the standing advice: plan for at least three biological repeats per condition, and preferably more.
No amount of peptide-level precision substitutes for biological replication.

## Blocking

A **block** is a group of experimental units that share some source of unwanted variability —
a batch, a day, a culture, a mass spectrometer, a lab. Blocking is deliberately arranging the
treatments so that each block contains (as close as possible to) an equal share of every
treatment, rather than letting them fall wherever they happen to land. This is a **randomized
complete block design (RCB)**: within each block, treatments are still randomized to units, but
every block gets every treatment.

The payoff is that the between-block variability can be estimated and subtracted out of the
treatment comparison, rather than adding noise to it — a good design factors the block out of the
question being asked.

The requirement that makes this work is strict: **every treatment must appear inside every
block.** If instead a block contains only one treatment, the treatment effect becomes completely
**confounded** with the block effect: there is no way, from the design alone, to tell whether an
observed difference is due to the treatment or due to whatever else distinguishes that block. The
only escape is to assume the block effect is negligible — an assumption the design gives no way to
check.

<figure>
<svg viewBox="0 0 400 230" role="img" aria-label="Two block designs: one where every block contains both treatments, and one where each block contains only one treatment">
  <text x="88" y="16" text-anchor="middle" font-size="12" fill="currentColor">A — blocked (both treatments per block)</text>
  <text x="300" y="16" text-anchor="middle" font-size="12" fill="currentColor">B — confounded (one treatment per block)</text>

  <rect x="20" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="56" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="92" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="128" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>

  <circle cx="29" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="29" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="40" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="40" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <circle cx="65" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="65" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="76" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="76" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <circle cx="101" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="101" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="112" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="112" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <circle cx="137" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="137" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="148" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="148" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <text x="34" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 1</text>
  <text x="70" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 2</text>
  <text x="106" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 3</text>
  <text x="142" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 4</text>

  <rect x="212" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="248" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="284" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>
  <rect x="320" y="30" width="28" height="110" fill="none" stroke="currentColor" stroke-width="1"/>

  <circle cx="221" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="221" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="232" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="232" cy="95" r="4.5" fill="currentColor"/>

  <circle cx="257" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="257" cy="95" r="4.5" fill="currentColor"/>
  <circle cx="268" cy="55" r="4.5" fill="currentColor"/>
  <circle cx="268" cy="95" r="4.5" fill="currentColor"/>

  <circle cx="293" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="293" cy="95" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="304" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="304" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <circle cx="329" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="329" cy="95" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="340" cy="55" r="4.5" fill="none" stroke="currentColor"/>
  <circle cx="340" cy="95" r="4.5" fill="none" stroke="currentColor"/>

  <text x="226" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 1</text>
  <text x="262" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 2</text>
  <text x="298" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 3</text>
  <text x="334" y="152" text-anchor="middle" font-size="10" fill="currentColor">block 4</text>

  <circle cx="140" cy="205" r="4.5" fill="currentColor"/>
  <text x="150" y="209" font-size="11" fill="currentColor">treatment 1</text>
  <circle cx="230" cy="205" r="4.5" fill="none" stroke="currentColor"/>
  <text x="240" y="209" font-size="11" fill="currentColor">treatment 2</text>
</svg>
<figcaption>Design A puts both treatments (filled and open circles) inside every block, so the
block-to-block variability can be estimated and subtracted from the treatment comparison. Design B
gives each block only one treatment, so the treatment effect and the block effect cannot be told
apart — they are confounded.</figcaption>
</figure>

## Worked example: mouse Treg versus Tconv proteomes

Duguet et al. (2017) compared the proteomes of mouse regulatory T cells (Treg) and conventional T
cells (Tconv), purified by flow cytometry, to find differentially regulated proteins between the
two populations. The data used in the tutorial are a subset of dataset PXD004436 on PRIDE, and come
in three versions built from the same underlying experiment:

- `peptidesCRD.txt` — Tconv cells from 4 biological repeats, and Treg cells from 4 *different*
  biological repeats. The two cell types are profiled in different mice, with no block tying a
  Treg sample to a particular Tconv sample: a **completely randomized design (CRD)**.
- `peptidesRCB.txt` — 4 biological repeats, but for *each* one, both the Treg and the Tconv
  proteome are profiled. The mouse is now the block: since every mouse contributes both cell types,
  mouse-to-mouse variability can be factored out of the Treg-versus-Tconv comparison — a
  **randomized complete block design (RCB)**.
- `peptides.txt` — the same paired (RCB) design, scaled up to 7 biological repeats.

This is Figure 1's abstract picture made concrete: block = mouse, treatment = cell type. In the CRD
file, mouse-to-mouse biological variability is not shared between the two groups and so enters the
comparison as extra noise; in the RCB file, pairing each mouse's own Treg and Tconv samples gives
the design a way to remove that source of variability instead. Which of the two designs actually
finds more differentially abundant proteins, and why, is worked out in the exercises below.

## Worked example: heart proteome across chambers

Researchers assessed the proteome of different heart regions for 3 patients (identifiers 3, 4 and
8): for each patient, the left atrium (LA), right atrium (RA), left ventricle (LV) and right
ventricle (RV) were sampled. The data are a small subset of the public dataset PXD006675 on PRIDE.

| | left | right |
| --- | --- | --- |
| **atrium** | LA | RA |
| **ventricle** | LV | RV |

Each of the 3 patients is a block, and within each patient the four regions cross two factors —
side (left/right) and chamber type (atrium/ventricle). The questions the researchers actually want
answered are about that ventricular-versus-atrial contrast: comparing LA to LV, RA to RV, the
average ventricular versus atrial proteome, and whether the ventricular-versus-atrial shift itself
differs between the left and right side of the heart.

## Exercises

**Mouse Treg/Tconv dataset** (`peptidesCRD.txt`, `peptidesRCB.txt`, `peptides.txt`; design
described above)

1. How would you analyse the CRD data?
2. How would you analyse the RCB data?
3. Explain the difference in the number of proteins that can be discovered as differentially
   abundant between the two designs.

**Heart dataset** (4 regions — LA, RA, LV, RV — for each of 3 patients; design described above)

1. Which factors will you use in the mean model?
2. Spell out the contrast for each of the four research questions: LA vs LV, RA vs RV, the average
   ventricular vs atrial effect, and whether that effect differs between the left and right side.
3. Interpret the estimate for the top hit under each contrast.
4. Explain why the number of significant proteins found differs so much between the contrasts.

## Sources

- Experimental units vs observational units, pseudo-replication, biological vs technical
  variability, blocking and confounding — statOmics SGA21, *3.1 Basic Statistical Concepts*
  ([`01-3-1-basic-statistical-concepts.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd),
  CC BY-NC-SA 4.0). The lecture refers to, but does not include, the MSqRob GUI/paper (numbered
  reference [1]) and the paper "Experimental design and data-analysis in label-free quantitative
  LC/MS proteomics: A tutorial with MSqRob" (reference [2]), and the Nature Methods "Points of
  Significance" column series it says the section draws on
  (nature.com/collections/qghhqm/pointsofsignificance). Figure 1 ("Blocking") is a photo/diagram
  hosted on GitHub (`blocking.png`) that is not reproduced here; the diagram above is redrawn from
  its caption text, not from the original image.
- Mouse Treg/Tconv worked example — statOmics SGA21, *3.2 Blocking: Mouse T-cell example*
  ([`02-3-2-blocking-mouse-t-cell-example.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd)).
  References Duguet et al. 2017 and dataset PXD004436 on PRIDE, and analysis scripts
  (`cptac_robust.html`, `cptac_robust_gui.html`) on the PDA21 course repository — none of these are
  included here. Figure 2 ("Design Mouse Study", `mouseTcell_RCB_design.png`) is likewise not
  reproduced.
- Heart dataset worked example and exercises — statOmics SGA21, *3.3 Heart dataset*
  ([`03-3-3-heart-dataset.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd)).
  References dataset PXD006675 on PRIDE and the same analysis scripts as above. Figure 3 ("Heart",
  `heart.png`) is not reproduced.

---

[← 23. Peptide-Level Models for Summarization](23-peptide-level-models-for-summarization.md) · [Contents](index.md) · [25. Case-Study Datasets for msqrob2 →](25-case-study-datasets-for-msqrob2.md)
