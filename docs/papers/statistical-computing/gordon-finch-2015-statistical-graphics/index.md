---
title: "Gordon & Finch 2015 — Statistician Heal Thyself: Have We Lost the Plot?"
paper: "summary"
source: "https://doi.org/10.1080/10618600.2014.989324"
licence: "© ASA, IMS and Interface Foundation — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Gordon, I., & Finch, S. (2015). Statistician Heal Thyself: Have We Lost the Plot? Journal of Computational and Graphical Statistics, 24(4), 1210-1229. ([original](https://doi.org/10.1080/10618600.2014.989324)). Rights: © ASA, IMS and Interface Foundation — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Statistician Heal Thyself: Have We Lost the Plot?

## What this covers

An empirical audit of graph quality in top-ranked statistics and applied-science journals,
speaking to the practice of statistical graphics rather than to any statistical method.

## The question

Cleveland argued in 1984 that statisticians should lead the improvement of graphical
communication in science. Thirty years on, the authors ask whether that leadership actually
happened: are graphs in the best statistics journals better than those in the best applied
science journals, and are either any good by the standards statisticians themselves teach? The
motivation is a gap they had noticed between how often foundational works on graphical design
(Tufte, Cleveland and McGill) are cited and how graphs actually look in print, and a running
disagreement in the literature over whether graphs need to support precise quantitative reading
or only convey a rough pattern.

## The approach

The authors first set out a framework of five principles distilled from Cleveland and Tufte:
show the data clearly (avoid clutter and "detection" problems), use simplicity in design (a high
data-to-ink ratio), align quantities to be compared on a common scale, make the visual encoding
transparent (the viewer should barely notice decoding it), and prefer a small set of standard
graphical forms (histograms, dot plots, boxplots, line plots, bar/dot charts, scatterplots,
possibly in panels) over novel ones. They illustrate how these principles cut against some common
recommendations — for example, they argue against the view that grid lines are mere "chartjunk"
and against treating graphs as suited only to broad patterns rather than accurate estimation.

They then sampled real journals rather than relying on anecdote. Using the Australian Research
Council's 2010 journal ratings, they identified the A*-rated (top 5%) journals in statistics and
in applied science/allied disciplines, drew a simple random sample from each group, and took the
first graph from a randomly chosen page in the most recent issues until they had worked through
three issues per journal. Each sampled graph was coded on more than 60 features tied to the five
principles (labelling, detection problems, scale alignment, use of color, grid lines, standard vs
non-standard form, and so on) by both authors independently, with disagreements resolved by
discussion, and also given a holistic rating of poor, adequate, good, or exemplary.

## What it found

The sample comprised 47 statistics graphs and 50 applied-science graphs (97 total). No graph in
either group was rated exemplary, and about 39% overall were rated poor, with a somewhat higher
poor rate among the applied-science graphs than the statistics graphs. Graphs with worse overall
ratings reliably had more of the coded undesirable features, supporting the coherence of the
rating scheme. Detection problems (clutter, overlap, or data that could not be reliably read off)
affected roughly 45% of all graphs; undefined abbreviations affected over half, and undefined
graphical elements affected close to a quarter. Only about a third of graphs had axis labels the
authors judged fully adequate, and in 30% of graphs at least one axis's tick labels were not
horizontal — a pattern they attribute largely to software defaults rather than deliberate choice.
Point estimates were plotted as bars rather than points in a substantial share of applied-science
graphs (41%), a practice the principles argue against since bars obscure uncertainty and invite
the reader to compare areas rather than positions. Uncertainty around an estimate was shown only
in a minority of graphs with estimates, and where "error bars" appeared their meaning (standard
error, standard deviation, or confidence interval) was frequently left unstated. Grid lines were
used in under a third of graphs, and where present were often judged too heavy; the authors argue
this is also a software-default effect, since well-chosen light grid lines in their view aid
accurate reading rather than constituting clutter. Differences between the statistics and
applied-science samples on most features were small, though a worked comparison of mean
undesirable-feature counts by discipline and rating level shows statisticians' graphs tending to
use standard forms and points-rather-than-bars more consistently, while applied scientists more
often used bars, non-horizontal labels, and redundant color.

## Limits and context

The authors note the finding runs against Cleveland's expectation that statisticians would lead
graphical practice: in this sample, statistics journals were not clearly better than applied
science journals, and in some respects were similar or only modestly ahead. They flag that their
study covered only static graphs reproduced in print, not the dynamic or interactive graphics
increasingly used elsewhere, and that it did not examine the "missing values" problem of articles
that omit a graph where one would have aided communication — they suggest that as a worthwhile
follow-up. They also position their five principles against two views they explicitly reject:
that graphs need only communicate a rough qualitative pattern and need not support precise
numeric reading, and the related claim that grid lines are inherently chartjunk; the paper argues
for graphs that support accurate estimation as well as pattern recognition. Their central
diagnosis is that software defaults, more than deliberate choice, are driving many of the faults
they catalogue, and they close with a detailed checklist intended for authors, editors and
reviewers rather than with a claim to have settled why good principles are so widely cited yet so
rarely followed in practice.

## Citation

Gordon, I., & Finch, S. (2015). Statistician Heal Thyself: Have We Lost the Plot? *Journal of
Computational and Graphical Statistics*, 24(4), 1210–1229. https://doi.org/10.1080/10618600.2014.989324
Available via Taylor & Francis Online (subscription), journal homepage http://www.tandfonline.com/loi/ucgs20.
