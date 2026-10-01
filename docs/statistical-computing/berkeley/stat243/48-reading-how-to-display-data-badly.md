---
title: "48. Reading: How to Display Data Badly"
course: "Berkeley Stat 243"
chapter: 48
source: "https://doi.org/10.1080/00031305.1984.10483186"
licence: "summary only \u2014 the paper is not reproduced"
written: "2026-10-01"
---

> **Summary of a paper.** Wainer, H. (1984), "How to Display Data Badly," The American Statistician, 38(2), 137–147. ([original](https://doi.org/10.1080/00031305.1984.10483186)). The paper is © its rights holder and is not reproduced here: this is a short account of it in our own words, standing in for it in the reading of Berkeley Stat 243.

# 48. Reading: How to Display Data Badly

## What this covers

Howard Wainer's 1984 invited address to the American Statistical Association, "How to Display Data
Badly," asks what a *good* statistical graphic requires — that it show data, show it accurately, and
show it clearly — and then catalogues, through twelve named rules, the ways real published graphics
fail each requirement. It is a commentary aimed at practitioners and graphics educators, not a
research paper with a novel method.

## The question

By the early 1980s there was no shortage of advice on how to display data well (Bertin, Tufte, Schmid
and others), but Wainer notes that the opposite literature — a catalogue of the ways data display
routinely goes wrong — had never been gathered into one place, even though bad graphics were common
in newspapers, government reports and the scholarly literature alike. He sets out to collect and name
the recurring failure modes so that they could be recognised and, implicitly, avoided.

## The approach

Wainer takes a three-part working definition of good display — show data, show it accurately, show it
clearly — and treats each part as a place a graphic can fail. He groups his twelve "rules" under the
three failure types and illustrates every one with an actual published graph or table: newspapers,
government pamphlets, and even a refereed journal article all supply examples. To make "bad" more
than a matter of taste, he leans on quantitative measures mostly due to Edward Tufte: a *data density
index* (how much information per unit of ink or area a graphic actually carries), the *data-ink
ratio* (how much of the ink on the page is spent conveying data versus decoration), and a measure of
*perceptual distortion* (how far the visual change in a graphic's metaphor departs from the actual
change in the underlying numbers). Where a rule can be demonstrated rather than just asserted, he
redraws the offending graphic honestly alongside it for comparison.

## What it found

The rules fall into three groups matching the three ways a display can fail:

- **Showing too little data at all** — covered by minimising how much information per unit of space
  a graphic carries, and by hiding data that is present through chart-junk or a badly chosen scale.
- **Showing data inaccurately** — covered by breaking the link between the visual metaphor (length,
  area, position) and the numbers it is meant to represent, by representing only rank and not
  magnitude, by graphing data out of its proper context, or by changing scale partway through a plot
  so that a change looks bigger or smaller than it is.
- **Showing data unclearly, without actually distorting it** — covered by burying an important
  comparison while foregrounding a trivial one, failing to hold comparisons to a common baseline,
  ordering a display by something irrelevant to the data (alphabetically, say) instead of by a
  structure the data itself suggests, labelling poorly, piling on more decimal places or dimensions
  than the data justify, and reinventing a known-bad technique that a better one has already
  superseded.

Wainer finds that these failures are not independent: low data density tends to accompany a poor
data-ink ratio, and both tend to travel with high perceptual distortion, so a graphic that is bad by
one measure is usually bad by the others too. He closes with two counter-examples held up as the
opposite of everything the rules describe — Minard's 1861 graphic of Napoleon's Russian campaign,
which he nominates as a candidate for the best statistical graphic ever produced, and the historical
work of Playfair, as evidence that doing it well has always been possible and is mostly a matter of
care rather than technique.

## Limits and context

Wainer is explicit that the tone of the piece is deliberately light, aimed in the wrong direction on
purpose, but that the underlying point is serious: the twelve rules are offered as "only the
beginning" of such a catalogue, not an exhaustive taxonomy, and he leaves generalising his distortion
measure to other settings as further work for others. The essay does not propose a new statistical
method; its contribution is the organising scheme and the demonstration, case by case, that the
failures it names are common practice rather than rare accidents — including, by his own account, in
at least one graphic from a refereed statistics journal.

## Sources

Read from the course PDF:
`berkeley-stat243/fall-2024/units/graphics_files/wainer1984.pdf`.

## Citation

Wainer, H. (1984), "How to Display Data Badly," *The American Statistician*, 38(2), 137–147.
DOI: [10.1080/00031305.1984.10483186](https://doi.org/10.1080/00031305.1984.10483186). Rights
holder: the American Statistical Association / Taylor & Francis. The paper is not openly licensed;
this is a summary, not a reproduction.

---

[← 47. Simulation and Monte Carlo](47-simulation-and-monte-carlo.md) · [Contents](index.md)
