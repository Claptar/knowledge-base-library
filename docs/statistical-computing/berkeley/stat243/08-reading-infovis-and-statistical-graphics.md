---
title: "8. Reading: Infovis and Statistical Graphics"
course: "Berkeley Stat 243"
chapter: 8
source: "https://doi.org/10.1080/10618600.2012.761137"
licence: "summary only \u2014 the paper is not reproduced"
written: "2026-10-01"
---

> **Summary of a paper.** Gelman, A. and Unwin, A. (2013), "Infovis and Statistical Graphics: Different Goals, Different Looks," Journal of Computational and Graphical Statistics, 22(1), 2-28. ([original](https://doi.org/10.1080/10618600.2012.761137)). The paper is © its rights holder and is not reproduced here: this is a short account of it in our own words, standing in for it in the reading of Berkeley Stat 243.

# 8. Reading: Infovis and Statistical Graphics

## What this covers

A statistical-graphics perspective on information visualization ("Infovis"): why the most
celebrated eye-catching visualizations outside statistics so often fail the goals statisticians
care about, and what each field could learn from the other's strengths. Speaks to the practice and
theory of data visualization, not to any single dataset or model.

## The question

The authors noticed that the visualizations most praised outside statistics — lists of "best data
visualizations of the year," prize-winning infographics — routinely violate principles statisticians
take for granted, while ordinary statistical graphics are widely dismissed by the public and by
graphic designers as dull. Rather than re-running the old argument over decoration versus
minimalism, they set out to name the different goals the two communities actually pursue, so each
can learn from the other's strongest work instead of trading in mutual disregard. They are explicit
that the aim is not to rule on which approach is "right."

## The approach

Instead of a formal taxonomy, the paper works through a sequence of contrasting examples. It opens
by laying out a set of goals a graphic can serve, grouped into two broad families: "discovery" goals
(an overview of a dataset, a sense of its scale and complexity, open-ended exploration) and
"communication" goals (conveying information clearly, telling a story, grabbing attention). The
authors argue statisticians tend to prize the first family and Infovis designers the second, and
that a single display rarely serves both well at once. They then apply this lens to real cases:
Nathan Yau's 2008 list of the year's best data visualizations (Wordle, a decision-tree map of the
Obama-Clinton primary vote, a 3-D-scanned music video, stacked streamgraphs of box-office receipts,
an art piece built from personal data, and an aerial survey of British air traffic); several widely
praised infographics (a world map of plane crashes, Florence Nightingale's coxcomb diagram of
Crimean War mortality, a health-spending-versus-life-expectancy graphic, and a military contractor's
flowchart for Afghanistan planning); and, finally, one example held up as serving both families of
goals at once, the Wattenbergs' "Baby Name Wizard." For two of the cases — the health-spending
comparison and a trend in the last letters of boys' names — the authors build their own alternative
graphs using conventional statistical forms (scatterplot, small multiples of time series) to show
directly what a plainer, "statistical" redisplay of the same data looks like.

## What it found

Working through the examples, the authors find each one serves some goals well and others badly.
Wordle grabs attention and gives a rough overview but actively works against reading off the word
frequencies it nominally displays, since position and color carry no information. The decision tree
of the Obama-Clinton vote tells a story and draws the eye but hides the relative size and
discriminating power of its splits. Nightingale's coxcomb is historically important and visually
striking, yet when the same Crimean War mortality data is redrawn as an ordinary time series, the
rise and fall in death rates is far easier to read off. The parallel-coordinate plot of health
spending against life expectancy creates a false impression that spending barely matters, which a
plain scatterplot of the same two variables dispels, especially once the US is set aside as an
outlier. The plane-crash map and the Afghanistan planning flowchart are judged to convey almost no
usable statistical information despite being visually arresting or informationally dense. Against
this, the Baby Name Wizard stands out for combining real statistical content — direct labelling,
axes anchored at zero, color used to encode rather than decorate — with the appeal and
interactivity associated with the best Infovis work. From these cases the authors draw several
general claims: that discovery and communication goals genuinely pull in different directions; that
familiar graphical conventions (axis placement, bar area) do real interpretive work that a novel
form forfeits; that novelty itself can function as a kind of commitment device that keeps a reader
engaged without necessarily teaching them anything; and that neither community's default style is
simply correct — each has something to learn from the other's best work.

## Limits and context

The authors describe the piece as a position paper built around a small, informally chosen set of
examples, not a systematic survey, and they explicitly decline to pass final judgment on the design
quality of the works discussed — several of which they say they admire as design or as art even
where they fault them as statistical displays. They restrict the discussion to static,
presentation-style graphics, setting aside interactive and dynamic visualization as a separate and
still-developing area they do not attempt to evaluate here. They acknowledge their perspective is
unavoidably that of statisticians and invite designers and visualization researchers to respond.
Several questions are raised but left open rather than settled, including whether statisticians'
preference for plain, old graphical forms is itself justified or just unexamined habit, and how a
field might formally measure what a graphic actually teaches its viewers rather than just how
memorable it is.

## Sources

Read from the PDF at `sources/berkeley-stat243/fall-2024/units/graphics_files/gelmanUnwin2013.pdf`.

## Citation

Gelman, A. and Unwin, A. (2013), "Infovis and Statistical Graphics: Different Goals, Different
Looks," *Journal of Computational and Graphical Statistics*, 22(1), 2-28.
DOI: https://doi.org/10.1080/10618600.2012.761137. Rights held by the American Statistical
Association, the Institute of Mathematical Statistics and the Interface Foundation of North
America (distributed via Taylor & Francis); all rights reserved, so this is a summary only, not a
reproduction.

---

[← 7. First Three Weeks Logistics](07-first-three-weeks-logistics.md) · [Contents](index.md) · [9. Reading: Adaptive Rejection Sampling for Gibbs Sampling →](09-reading-adaptive-rejection-sampling-for-gibbs-sampling.md)
