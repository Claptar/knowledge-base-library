---
title: "6. The msqrob2gui Analysis Workflow"
course: "StatOmics Sga21"
chapter: 6
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. The msqrob2gui Analysis Workflow

## What this covers

This chapter walks through `msqrob2gui`, the Shiny app front end to `msqrob2`, on a concrete
dataset (the CPTAC spike-in study, treatment conditions A and B) — from launching the app through
input, preprocessing, protein summarization, model fitting, hypothesis testing and reporting. It
assumes the underlying statistics of `msqrob2` — peptide-to-protein summarization, the two-stage
robust procedure, and testing linear-model contrasts — are already understood; the point here is
how those pieces are exposed as tabs in the GUI and in what order they have to be used, plus one
running question the tutorial keeps returning to: how do the two summarization methods on offer
actually compare, given that this dataset lets you check the answer against a known truth.

## Launching the app

`msqrob2gui` is an R package that wraps `msqrob2` in a `shinyApp`. After installing `msqrob2` and
`msqrob2gui`, the sequence is:

1. Open RStudio.
2. In the console, run
   ```
   library(msqrob2gui)
   launchMsqrob2App()
   ```
   The first line loads the package and its dependencies; the second launches the app.
3. A new window opens with the app running inside RStudio's viewer.
4. It is advisable to open the app in an actual browser tab instead, using the `Open in Browser`
   button above the app's navigation bar.

Everything that follows happens inside this one running app, moving left to right across its tabs:
Input, Preprocessing, Summarization, Model (with Inference and DetailPlots inside it), and Report.

## The Input tab

The first three things to set are the project name, the peptide-level data, and the design.

- **Project name.** A name such as `project_CPTAC_AvsB`; the app appends a timestamp to it when
  results are downloaded, so results from repeated runs don't overwrite each other.
- **The peptides file.** This is `peptides.txt`, the peptide-level intensity table. For a MaxQuant
  search, it lives by default in `path_to_raw_files/combined/txt/`.
- **The experimental annotation file**, a tab-delimited or `.xlsx` file that links MS runs to the
  design. One column, always called `run`, holds the names of the runs — for a MaxQuant search
  these are the names in MaxQuant's `Experiment` column, and they must be unique. The remaining
  columns hold whatever other design variables might affect protein expression; in this dataset
  that is only the treatment (spike-in) condition.

If the annotation file doesn't exist yet, uploading the peptides file first and clicking
`Create annotation file` generates a template containing just the `run` column, populated with the
run names found in the peptides file — the other columns still have to be filled in by hand,
according to the actual design.

Once the output location, the peptides file and the annotation file are all set, the input screen
is complete and preprocessing can begin.

## The Preprocessing tab

### Log-transformation and normalization

The first preprocessing step is log-transformation, applied by default; the second is
normalization. Both act on the peptide intensities before anything else happens to them.
Normalization is not one-size-fits-all — because the nature and extent of bias differs across
datasets, no single method dominates the others in every dataset — so several normalization
methods are offered rather than one fixed choice.

Clicking `Start Normalization` is what actually runs the remaining preprocessing steps and builds
the normalized peptide object that every later tab depends on. Two diagnostic plots appear once it
finishes:

- the distribution of peptide intensities within each run, after normalization;
- an **MDS plot**: a scatter plot placing each run so that the distance between two runs on the
  plot approximates the Euclidean distance between them computed over the top 500 most-differing
  peptides. Once the data are log-transformed, these distances are related to log fold changes, so
  runs plotted close together are more similar (in the peptides that vary the most) than runs far
  apart. The plot can be read as dots, as labels, or both, and a region can be dragged and
  double-clicked to zoom in.

### Filtering peptides

Several filters, applied after normalization, decide which peptides make it into the summarization
step:

- **Razor peptides** — peptides that cannot be uniquely attributed to one protein or protein
  group — are removed by default, since it's unclear which protein group their intensity should be
  credited to. The option `Remove comprising protein groups` extends this: it removes every peptide
  in a protein group if any of that group's peptides also maps to a protein present in some other,
  smaller, protein group.
- **Minimal number of peptides**, a threshold $T$ (default 2), on how many times a peptide
  *sequence* must occur in the data to be kept. The reason is practical rather than a rule about
  proteins: the model needs to estimate a peptide effect for each peptide, and that effect cannot
  be estimated from a single occurrence. This is not the "two-peptide rule" for protein
  identification — a protein can still be quantified from a single peptide sequence, as long as
  that one sequence was itself observed in more than one sample.
- **Filter columns**, for removing reverse (decoy) sequences left over from the MaxQuant search and
  potential contaminant proteins (keratin from skin and hair, residual trypsin from digestion),
  by naming the relevant columns of the peptides file.

## The Summarization tab

Before a protein-level model can be fit, peptide intensities have to be summarized into one value
per protein per run. Two methods are offered:

- **Median summarization** — the naive approach, included mainly for didactic reasons, to show
  what can go wrong with a naive summary.
- **Robust summarization** — the two-stage procedure that fits the actual `msqrob2` model, and is
  the one used for the downstream analysis. It is described as "novel and much faster" than
  earlier robust approaches.

`Start Summarization!` has to be clicked to build the object the rest of the app needs, and can
take a while depending on the method. Once it finishes, an MDS plot of the summarized (protein-
level) intensities is generated, the same way it was for the peptide-level data after
normalization.

## The Model tab

### Specifying the formula

`msqrob2` fits linear models to the (preprocessed, summarized) protein intensities, and the model
is specified symbolically, using the names of the design variables, in a formula of the form
`~ terms`:

- `variable1` alone models the intensity as a function of `variable1`. If `variable1` is
  continuous this is an intercept and a slope. If it is a factor, this is an intercept for a
  reference class plus slope parameters, one per non-reference level, each interpreted as the
  average difference between that level's intensity and the reference level's.
- `variable1 + variable2` includes the main-effect terms of both variables.
- `variable1:variable2` is the interaction: the terms formed by crossing every term of `variable1`
  with every term of `variable2`, i.e. it lets the effect of `variable1` change with the value of
  `variable2`.
- `variable1*variable2` is shorthand for the full cross, `variable1 + variable2 + variable1:variable2`.

### The design in this dataset

Here the design has one factor, `treatment`, with two levels: spike-in condition A and condition B.
The formula is

$$
{\sim} \text{treatment}
$$

As soon as this is entered, the app visualizes the design as group means built from model
parameters:

- the group mean for treatment A is the parameter `(Intercept)` on its own;
- the group mean for treatment B is the linear combination `(Intercept) + treatmentB`.

<figure>
<svg viewBox="0 0 380 170" role="img" aria-label="Two group means on a log2-abundance axis, showing that the model parameter treatmentB is the log2 fold change between them">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="120" x2="350" y2="120" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="345" y="140" text-anchor="end" font-size="12" fill="currentColor">log2 abundance</text>

  <circle cx="110" cy="120" r="4" fill="currentColor"/>
  <text x="110" y="100" text-anchor="middle" font-size="12" fill="currentColor">log2 A</text>
  <text x="110" y="140" text-anchor="middle" font-size="11" fill="currentColor">(Intercept)</text>

  <circle cx="290" cy="120" r="4" fill="currentColor"/>
  <text x="290" y="100" text-anchor="middle" font-size="12" fill="currentColor">log2 B</text>
  <text x="290" y="140" text-anchor="middle" font-size="11" fill="currentColor">(Intercept) + treatmentB</text>

  <line x1="110" y1="60" x2="290" y2="60" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="200" y="45" text-anchor="middle" font-size="12" fill="currentColor">treatmentB = log2FC</text>
</svg>
<figcaption>The two group means the model tab visualizes: condition A sits at the intercept,
condition B at the intercept plus the treatmentB parameter, so treatmentB is exactly the log2 fold
change between them.</figcaption>
</figure>

Since the intensities were log2-transformed, the parameter `treatmentB` is itself the average
difference in log-intensity between the two conditions:

$$
\log_2 FC_{B-A} = \log_2 B - \log_2 A = \log_2\frac{B}{A} = \text{treatmentB}.
$$

A linear combination of model parameters like this is called a **contrast**. Its sign carries the
direction: a positive estimate means the protein is on average more abundant in B, negative means
more abundant in A, and zero means the estimated abundances agree. A log2 fold change of 1 means
the average abundance in B is exactly twice that in A.

Once the formula is entered, `Fit Model!` fits this model separately for every protein, after which
formal hypothesis testing on each protein's contrast becomes possible.

## The Inference tab

The hypothesis being tested, protein by protein, is

$$
H_0:\ \log_2 B - \log_2 A = 0 \qquad\text{against}\qquad H_1:\ \log_2 B - \log_2 A \neq 0,
$$

entered in the app as the null hypothesis `treatmentB = 0`. Under $H_0$ there is no effect of the
treatment on that protein's abundance; the p-value is the probability, if $H_0$ were true, of
observing a fold change at least as extreme (in either direction) as the one actually seen, by
chance alone.

Once the null hypothesis is specified, the tab fills in:

- a **volcano plot**: statistical significance ($-\log_{10}$ of the p-value) on the y-axis against
  effect size ($\log_2FC$) on the x-axis. A y-value of 1 corresponds to $p=0.1$, a y-value of 2 to
  $p=0.01$, and so on.
- a **results table**, showing by default only the proteins significant at the chosen significance
  level; unticking `only significant features in table` shows every protein instead.
- a **boxplot** of the log2 fold changes of whichever proteins are currently selected in the table.

Proteins can be selected either in the table, or by dragging a region on the volcano plot and
double-clicking to zoom in (double-clicking an empty area resets the view); selecting a protein in
one view highlights it in the other. A search field above the table filters by name — typing `ups`,
for instance, restricts the table to proteins whose name contains that string.

For this dataset, among the 20 proteins ranked most significant, nearly all are the spiked-in
proteins; only one yeast protein appears in that top 20.

## The DetailPlots tab

Selecting a single protein — in the results table or by clicking its point on the volcano plot —
and switching to DetailPlots shows the normalized peptide intensities and the summarized protein
intensity underlying that protein's fit, for every run. The plot can be recolored or split
horizontally or vertically by any design variable.

## The Report tab

The Report tab compiles a reproducible record of the analysis: an R Markdown script together with
its rendered HTML report. Before generating it, the number of detail plots to include can be set
(default 10, meaning detail plots for the 10 most significant proteins in the current top list —
fewer if fewer than 10 proteins are significant at the chosen FDR).

Clicking `Generate report` re-runs every step from every tab, which takes a while, and produces a
downloadable zip file containing:

- `features.txt` — the raw intensity data, tab-delimited;
- `annotation.xlsx` — the design annotation;
- `report.Rmd` — the R Markdown source, which can be re-knitted in RStudio;
- `report.html` — the compiled report.

The whole analysis is therefore stored in a way that can be regenerated from scratch. The same
analysis can also be run directly as a script rather than through the GUI, which trades the point-
and-click interface for more flexibility and for the ability to automate and document the pipeline.

## Evaluating the two summarization methods

Because this is a spike-in dataset, the true fold change between conditions A and B is known for
each of the two protein groups that appear in the results — separately from whatever the model
estimates — which makes it possible to actually check the summarization methods against ground
truth rather than just against each other.

The check uses the boxplot of log2 fold-change estimates below the results table:

1. Untick `only significant features in table` so every protein is shown, not just the significant
   ones.
2. Search for `ups` to restrict the table (and its boxplot) to the spiked-in proteins; searching
   for the complementary set isolates the background (yeast) proteins instead.
3. Compare the resulting boxplot, for each protein group, between the robust summarization and the
   naive median summarization.

This comparison — spiked proteins versus background proteins, robust versus median summarization —
is the exercise the tutorial builds up to, and is left as such below.

## Exercises

The bracketed labels below follow the tutorial's own numbering, so a specific question can be
referred back to.

1. **[Preprocessing — log-transformation]** Why is log-transformation of the peptide intensities
   needed? Untick the "Log-transform data" checkbox and compare the resulting intensity
   distribution with the log-transformed one to see why.
2. **[Preprocessing — base 2]** Why is base 2 specifically chosen for the log-transformation, given
   how the fold-change contrasts are interpreted later on?
3. **[Preprocessing — MDS after normalization]** What can be read off the MDS plot generated after
   normalization?
4. **[Summarization]** What changes in the data when robust summarization is used in place of
   median summarization, and why would that be the case?
5. **[Evaluating summarization, spiked proteins]** The true fold change for the spike-in proteins
   is known. Looking at the boxplot of log2 fold-change estimates for just those proteins (using
   the `ups` search filter), what do you observe?
6. **[Evaluating summarization, background proteins]** Now select all the yeast (background)
   proteins instead. What is their true fold change, and what does the boxplot of estimates show?
7. **[Evaluating summarization, method comparison]** Repeat the previous two questions using median
   summarization instead of robust summarization. How do the results compare to the robust
   summarization case, and how would you explain the difference?

## Sources

- Notes: `01-2-2-starting-msqrob.md` through `05-2-3-5-the-report-tab.md`
  (`docs/omics-statistics/statomics/sga21/cptac_robust_gui/`), converted from
  `cptac_robust_gui.Rmd` in the statOmics SGA21 course repository — sections 2.2 (Starting MSqRob),
  2.2.1 (Input tab), 2.3.2–2.3.3 (Preprocessing and Summarization tabs), 2.3.4 (Model, Inference and
  DetailPlots tabs), and 2.3.5–2.3.6 (Report tab and evaluating summarization).
- The tutorial refers to a description of the CPTAC dataset itself ("see description of the data
  2.2") and to installation instructions in a separate `software` page; neither is among the
  supplied files, so the exact spike-in concentrations and the resulting true fold changes are not
  given here — only that they exist and are known for this dataset.
- Numbered citations in the source text ([6] for the MaxQuant search, [8] on normalization method
  performance, [9] on the two-peptide rule, [10] on contaminants) point to a reference list that
  was not included in the supplied files.

---

[← 5. Robust Summarization in Proteomics](05-robust-summarization-in-proteomics.md) · [Contents](index.md) · [8. Interaction Effects and Stage-wise Testing →](08-interaction-effects-and-stage-wise-testing.md)
