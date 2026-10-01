---
title: "127. Evaluating Forecasting Hub Performance"
course: "Berkeley Stat 153"
chapter: 127
source: "https://doi.org/10.1038/s41467-024-50601-9"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Written from a paper.** Written from Mathis, S. M. et al. (2024). "Evaluation of FluSight influenza forecasting in the 2021–22 and 2022–23 seasons with a new target laboratory-confirmed influenza hospitalizations." *Nature Communications* 15, 6289 ([original](https://doi.org/10.1038/s41467-024-50601-9)), licensed CC BY 4.0. This adaptation carries the same licence.

# 127. Evaluating Forecasting Hub Performance

## What this covers

This chapter works from a very short excerpt — about a page — of a case study on how a
collaborative forecasting hub evaluates the models that submit to it, using the FluSight
influenza-hospitalization hub across the 2021–22 and 2022–23 seasons as its example. It answers a
narrow question: once many teams submit probabilistic forecasts of the same target, how do you
compare them, and does combining them into an ensemble actually help? It assumes you already know
what a forecasting hub is — several teams submitting forecasts of a shared target on a shared
schedule — and what it means for a forecast to be an ensemble of others. It does not itself define
the scoring rules it names, and that gap is flagged rather than papered over below.

## Forecasting hubs and why no single model wins

A collaborative forecasting hub lets many modeling teams submit forecasts of the same target on
the same schedule, which makes it possible to evaluate their performance systematically and, from
that pool of forecasts, build an ensemble. The models submitted to the hub described here span
four broad kinds: mechanistic, statistical, ensemble, and AI or machine-learning models.

The central empirical fact motivating the rest of the chapter is that no one kind of model
dominates. The diversity of model *types* among the top performers was consistent from one season
to the next, but which specific model was a top performer was not: an individual model's
performance varies a great deal both within a season and across seasons (the source cites this
variation directly, attributing it to a reference — numbered 13 in the original — that is not
included in this excerpt). Given that heterogeneity in the structure of the top performers, and
the many ways forecasting models can differ from one another, the excerpt states plainly that it
has not been possible to pin down which characteristics of an individual model are most often
associated with high performance.

This is the motivation for building an ensemble in the first place: if performance moves around
unpredictably at the level of individual models, and you cannot yet say why, then a unified
representation built from all the submitted models is useful for quickly reading off the expected
trend, and — the excerpt argues — an ensemble can also be more consistently reliable and
well-calibrated across different spatial jurisdictions than any single contributing model.

## Scoring forecasts: Absolute WIS, Relative WIS, and standardized rank

The excerpt names three ways of expressing the same underlying score without spelling out how any
of them is computed:

- **Weighted interval score (WIS).** The one metric given a full name, used to score each team's
  forecasts of weekly influenza hospital admissions at each jurisdiction and forecast horizon (the
  horizons considered run from one to four weeks ahead).
- **Absolute WIS** and **Relative WIS.** Two variants used side by side to rank teams; the excerpt
  reports the FluSight ensemble's standing on both without saying what distinguishes them.
- **Standardized rank.** A per-season summary built from the WIS values: each team's WIS is turned
  into a rank among all qualifying teams — those submitting at least 75% of the forecast targets —
  pooled over every jurisdiction and every horizon, standardized so that ranks are comparable
  across teams and seasons. A team's forecasts falling "in the top 50%" or "in the top 25%" is a
  statement about this standardized rank.

None of the three is defined algebraically in this excerpt; the details live in the source's own
Table 1, Supplementary Table 1, and figures, none of which are reproduced here (see Sources below).

## The FluSight ensemble's record across two seasons

Against that scoring, the excerpt gives a specific verdict on the ensemble itself. Over the full
evaluation period, both seasons, and all forecast jurisdictions, the FluSight ensemble was among
the top five performing models by both Absolute WIS and Relative WIS. Looking at rank rather than
raw score, the ensemble predicted weekly influenza hospital admissions more accurately than most
of the individually contributed models, with the majority of its forecasts landing in the top 50%
of all submitted forecasts.

## Accuracy against consistency: a trade-off across jurisdictions

The one comparison the excerpt draws out explicitly is a trade-off. Three individual models —
PSI-DICE, CMU-TimeSeries, and MOBS-GLEAM_FLUH — had *more* forecasts landing in the top 25% than
the FluSight ensemble did. But those same models showed higher spatial heterogeneity: their
standing changed more from one jurisdiction to another than the ensemble's did. So being
occasionally excellent and being reliably good across every jurisdiction are different properties,
and the excerpt's point is that the ensemble trades some occasional top-tier performance for
consistency across space. The text breaks off mid-sentence immediately after this point ("The
generally high accuracy of the…"), so whatever conclusion followed is not part of this excerpt.

## What this excerpt does not tell you

Because the supplied material is a single short passage with no accompanying transcript, slide
notes, or problem set, several things it refers to are not available to check against:

- The formulas for WIS, Absolute WIS, and Relative WIS, and how a raw score is turned into a
  standardized rank.
- Table 1 and Supplementary Table 1, which list the qualifying teams and season-by-season metrics.
- Figures 1, 2, and 3, which respectively show model-by-model performance across seasons,
  standardized rank by season for qualifying teams, and the spatial-heterogeneity comparison
  behind the trade-off described above.
- The reference (numbered 13 in the original) supporting the claim that model performance varies
  within and across seasons.
- Whatever conclusion the final, truncated sentence of the excerpt was building toward.

## Sources

- Everything above is drawn from a single supplied file: `mathis.md`
  (`lectures/advanced/mathis.pdf` in `berkeley-stat153`, fall 2024, CC BY 4.0), a model's
  reconstruction of a PDF slide/paper page with no usable text layer. The reconstruction itself
  flags that its prose is paraphrased in places and that every equation in the original is
  unverified — treat any numeric or formulaic detail here as a pointer back to the original PDF,
  not as verified.
- No transcript, written notes, or exercises were supplied for this chapter; there is accordingly
  no Exercises section.
- The excerpt is short (roughly one page) and ends mid-sentence; the terms Absolute WIS, Relative
  WIS, and standardized rank are used but not defined within it, and it references a numbered
  citation and three figures/tables that are not part of the supplied material, as noted above.

---

[← 126. Simple Linear Regression](126-simple-linear-regression.md) · [Contents](index.md) · [128. Supplementary Reading List →](128-supplementary-reading-list.md)
