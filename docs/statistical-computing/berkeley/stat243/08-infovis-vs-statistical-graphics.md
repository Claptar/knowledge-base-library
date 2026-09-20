---
title: "8. Infovis vs. Statistical Graphics"
course: "Berkeley Stat 243 Fall 2024"
chapter: 8
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Infovis vs. Statistical Graphics

## What this covers

This chapter reads Gelman and Unwin's "Infovis and Statistical Graphics: Different Goals, Different
Looks" (2013), the assigned reading for the graphics unit of Stat 243. The question it answers is
why two communities that both draw pictures of data — academic statisticians and information-
visualization (infovis) designers — routinely dislike each other's best work, and what a
statistician should say about an infographic that is visually excellent but statistically weak. It
assumes only that the reader already knows the standard chart types (scatterplot, histogram, line
plot, bar chart, pie chart) and does not assume any prior exposure to the infovis literature.

## Two communities, two vocabularies

Statistical graphics have had an odd history within statistics itself: exploratory and graphical
methods are a minor subfield, poorly integrated with modeling and inference. Howard Wainer's
observation, quoted by the authors, is that articles in the *Journal of Computational and Graphical
Statistics* are about 80% computation and 20% graphics. Outside statistics, the opposite is true —
infographics are everywhere, on the Web and in the *New York Times*, and their designers show
little interest in the statistical principles (Cleveland's, above all) about which comparisons a
graph should make easy.

The paper's occasion is concrete: in December 2008, statistician and blogger Nathan Yau (Flowing
Data — at the time roughly 15,000 subscribers, more than the largest academic statistics blogs)
posted a list of the five best data visualizations of the year. Gelman and Unwin were struck by how
far the visual appeal of these pieces diverged from ordinary statistical-graphics practice, and a
blog exchange with Yau convinced them that the disagreement was not about quality but about goals:
the two fields are optimizing different things, and disputes phrased as "this graph is bad" are
usually really about which goals it is supposed to serve.

Statisticians want effective, precise representations that let the reader draw their own
conclusions from a comparison that has been made easy. Infovis designers want to grab the reader's
attention and tell a story, and are willing to spend more of the graphic's real estate on context
and mood to do it. The paper puts it as: statisticians ask what can be extracted from the data
available; infovis uses the data to point at a wider issue. Both are legitimate goals.

One clarifying distinction the authors draw early on is between **exploratory** and **presentation**
graphics. Exploratory graphics are the thousands of throwaway plots an analyst makes for themselves
while working — fast, flexible, alternative views, with no audience but the maker. Presentation
graphics are the small number of graphs, prepared with care, that others will actually see; this is
where a graphic designer's skill has something to contribute, since it is not relevant to
exploratory work. The paper is written almost entirely about **static presentation graphics** — the
routine tool of the working statistician — leaving interactive and dynamic graphics aside as still
too early in their development to generalize about.

## Six goals of a graphic

Before proposing their own list, the authors quote a set of positions on why graphics matter at
all: Tufte ("At their best, graphics are instruments for reasoning about quantitative information"),
Cleveland ("Graphs are powerful tools for communicating quantitative information"), Chambers et al.
("There is no single statistical tool that is as powerful as a well-chosen graph"), and Fisher
("Diagrams prove nothing, but bring outstanding features readily to the eye"). All true, all vague.
Tukey was more specific, and his four-part statement of the true purpose of graphic display is
worth keeping whole:

1. Graphics are for the qualitative or descriptive — never for the carefully quantitative (tables
   do that better).
2. Graphics are for **comparison** of one kind or another, not for reading off individual amounts.
3. Graphics are for **impact** — "interocular impact if possible" — almost never for something that
   has to be worked at hard to be perceived.
4. Graphics should report the results of careful data analysis, not attempt to replace it.

Gelman and Unwin's own list, tuned for an era of much larger datasets and much more graphics-as-
communication, splits into two families:

**Discovery goals** — for the person doing the analysis:

- *Overview*: a qualitative sense of what is in a dataset, checking assumptions, confirming known
  results, spotting patterns.
- *Conveying scale and complexity*: a network graph may reveal almost nothing about structure but
  still give an impression of interconnectedness, of central and peripheral nodes — and that
  impression can be the point.
- *Exploration*: flexible displays — small multiples, or better, interactive graphics — that make
  comparisons easy and let unexpected features of the data surface.

**Communication goals** — for an audience:

- *Communication to self and others*: getting information out of the dataset in a form that can
  actually be read back out visually. Information density only helps if it can be extracted.
- *Telling a story* — Minard's Napoleon-in-Russia graph, popularized by Tufte, is the standing
  example of a graphic that communicates by narrating.
- *Attracting attention and stimulating interest*: graphs are "grabby" in newspapers and blogs in a
  way they are not expected to be in a submitted journal manuscript, where a theorem attributed to
  Barabási (echoing Hawking) holds that every graph in a book halves its audience — plausibly why a
  data-heavy book like *Freakonomics* contains none.

The two families pull in different directions. We communicate when we display a convincing pattern
and discover when we notice a deviation from expectation — and how a reader reacts depends on how
much background knowledge they bring, an analogy the authors draw to fine art (which rewards
sustained attention from someone who expects to work at it) versus advertising (an immediate hit or
nothing). Statisticians write for readers who already have the fine-art patience; designers write
for readers who need the advertising hit first. The best examples, the paper argues, manage both at
once — and the chapter returns to one such example, the Baby Name Wizard, at the end.

A graphic, in this view, is never a solitary object: working from the inside out there are
annotations, a legend, a title, a caption, surrounding text, an overall story, and a headline, plus
often a grid or sequence of related graphics. Novelty also plays a genuine cognitive role, footnoted
in the paper: readers who put in the extra effort a novel display demands acquire an emotional
commitment to having understood it (nobody wants to admit the effort was wasted), whether or not
they actually learned anything — a mechanism the authors compare to the small satisfaction of
finally working out how to do something in R.

## Statistical visualization and infographics, as ideal types

Section 6 of the paper names the two practices explicitly, in idealized form:

- **Statistical data visualization**: focused not on visual appeal but on facilitating an
  understanding of patterns in an applied problem — the discovery goals above — both by directing
  readers to specific information and by letting them see for themselves.
- **Infographics**: ideally attractive, attention-grabbing, story-telling, and designed to get the
  viewer thinking about a dataset both as individual measurements and as a representation of a
  larger pattern — the communication goals above.

The authors deliberately lump visualization of raw data together with visualization of statistical
models under the first heading, since the best data graphs are often implicit or explicit
comparisons to a model, and a model graph is more informative with the data plotted alongside it to
show fit.

## Reading the "five best of 2008" against the goals

The paper works through Yau's list item by item, explicitly not as a verdict on the designers'
craft but as an exercise in naming which of the six goals each piece actually serves.

**Wordle** (word clouds) grabs attention and gives an overview, and its randomness invites a kind of
exploration — but the very unorderedness that makes it eye-catching means every rendering looks
different and can bury an important word under color or position. The authors' central complaint is
that engaging with a Wordle pulls attention toward *how Wordle works* rather than toward the
document it is summarizing: the how-did-they-do-it curiosity overwhelms the data.

**The Obama–Clinton decision tree** (Amanda Cox, *New York Times*) drew criticism from both authors
for different reasons: Unwin objects that neither the importance nor the discriminating power of
each split is shown, so there is no way to judge how meaningful the tree is; Gelman, as a political
scientist, objects to the underlying model — voters, not counties, decide, and "decision tree"
invites a confused reading of what a county even does. It gives an overview of a kind, tells a
story, and the photos attract attention, but does not support exploration and implies the data
divide more cleanly than they do.

**The Radiohead video**, reconstructed from three-dimensional scanner data, is pretty and is a real
demonstration of statistical image-reconstruction methods, but the authors do not think "data
visualization" is the right category for it at all — it is data used to make art.

**The box-office streamgraphs** (stacked area charts of movie ticket sales, interactive) provoked
real online discussion, and Yau credited the discussion itself to the novelty of the streamgraph
form over an ordinary stacked bar chart. But stacking curves on top of one another makes the
trajectory of any individual film nearly unreadable. The authors' preferred fix names their central
methodological point for the whole paper: **two separate graphs** — total sales over time, and
individual film trajectories, color-coded — would show more than one graph trying to do both jobs
at once. The streamgraph's real achievement, they conclude, was attention, not information.

**"I Want You to Want Me"** (Jonathan Harris and Sep Kamvar) is visually appealing and, like the
Radiohead video, more of an attention-getter than a data display — the authors would want it paired
with a pointer to a more informative view for anyone whose interest it has actually caught.

**Britain From Above** (BBC, satellite-derived air-traffic visualization) is an impressive computing
and statistical achievement that tells a story and grabs attention — and does communicate one
specific thing well, the gaps in flight coverage that the video calls out as possible secret
installations — but distorts the map by rendering Britain from an angle rather than from directly
above, purely to sell the sensation of being in the plane.

Yau's own list, the authors conclude, consists of graphics that are visually attractive and
data-related without pursuing the traditional goals of statistical graphics — which does not
disqualify them as inspiration for what statistical graphics could become.

## Praised infographics that fail statistically

A second set of examples, not from Yau's list, illustrates specific statistical failure modes in
otherwise celebrated infographics.

**Plane crashes by country** (David McCandless, winner of a *Guardian* visualization contest) plots
raw counts of crashes per country rather than a rate, and — as the critic Daniel Lakeland is quoted
pointing out — a companion graphic on the same site mixes units freely (dollars per year against
total dollars ever spent). The authors' verdict is that a prize for this in a visualization contest
is "like deciding who won the Indy 500 by picking the car with the snazziest paint job," while
allowing that a graphic that is statistically wrong can still be useful for pulling readers toward
the underlying numbers.

**Florence Nightingale's coxcomb** is the paper's central worked historical example. The coxcomb
overlays each year's Crimean War mortality on the same circular clock face so that the same month in
different years lands in the same angular position — a device Nightingale herself described as
meant "to affect thro' the Eyes what we fail to convey to the public through their word-proof ears."
Gelman and Unwin's statistical complaint is specific: because each cause of death is measured
outward from the center, overlapping wedges make the *total* deaths per month from the three causes
impossible to read off, and the data for the first twelve months are drawn in one half of the
figure and the second twelve in the other — a convention broken for no stated reason. They redraw
the same data as a small multiple of ordinary time-series line plots (death rate) alongside a bar
chart (army size, since that is a count rather than a rate) and find the seasonal spike far more
legible that way. Their conclusion generalizes: the coxcomb is an excellent *infographic* — it is
unique, memorable, and undeniably helped draw political attention to the sanitary conditions
Nightingale was fighting — but a weak *statistical graphic*, since it does not directly aid
understanding of the pattern in the data. They suggest that on the Web the two could be layered: the
coxcomb to draw the reader in, a click revealing the time-series version, a further click revealing
the raw data.

**Health-care spending versus life expectancy** (a *National Geographic* graphic by Oliver Uberti,
redrawn as a scatterplot in the paper) is the cleanest single illustration of how a chart type can
manufacture a false impression. The original used a parallel-coordinate plot across countries, and
its visual effect is that the lines converge toward the right — suggesting to at least one
commentator, quoted as calling it "a masterpiece of succinct communication," that spending is "all
over the map" while life expectancy is essentially the same everywhere. Redrawn as an ordinary
scatterplot of spending against life expectancy, and with the United States — a clear outlier —
removed, a strong positive correlation between the two variables appears immediately, a pattern the
parallel-coordinate scaling had actively hidden. The authors are candid that the scatterplot is also
the more boring, more familiar chart, which is part of why the flashier original went on to win the
praise it did; their proposed resolution, again, is to do both — make the informative chart, and
find a way to make it eye-catching too.

**The Afghanistan planning flowchart**, prepared by a military contractor for the Joint Chiefs of
Staff, is offered as a case outside the usual histogram-and-scatterplot territory entirely: a tangle
of arrows connecting vaguely defined concepts, with every node drawn the same size, giving no sense
of priority. The authors, disclaiming any expertise in military planning, restrict their comment to
the graphic itself: they would lighten the arrows and reduce how many there are, but even then it is
unclear what a reader is meant to take from a graph that functions more like a conceptual map (find
a concept, trace what connects to it) than like a display of information.

## Old tools, new tools, and the question of technological lag

The paper draws a literary analogy for the two houses' default style: statisticians tend toward
Orwell's "good prose is like a window pane" — plain, load-bearing, familiar forms (line plots for
time series, histograms for univariate data, scatterplots for bivariate data, predictors on the
horizontal axis) that an experienced reader absorbs quickly precisely because they are unoriginal.
Infovis designers lean toward the harder-won, more demanding style of a Martin Amis or Chris Ware.
Both, the authors note, take real skill to do well — their own health-care scatterplot needed real
work and applied experience to look as clean as it does — and both directions can also produce
lasting influence: "yesterday's experiments can be tomorrow's standards."

The pie chart is offered as a case where both verdicts are simultaneously defensible: it introduced
millions of people to data and gave them a physical sense of proportions, and its later elaborations
(three-dimensional pies, exploding wedges) are a dead end that gets in the way of clearer displays.
Excel is treated the same way — a genuinely useful default tool, whose problem is only that people
often stop at the default, spending fifteen minutes on the graph after spending dozens of hours on
the model and dozens more on the prose.

The authors end this discussion honestly uncertain about their own side's conservatism: are dot
plots and line plots actually the best available choice, or does new graphical technology simply
take decades to become usable as statistical methodology? Infovis, they note, is working much
further out on the technological frontier than statistics typically does.

## The Baby Name Wizard: an example that does both

The paper's positive counter-example is an interactive tool built by Laura and Martin Wattenberg,
which the authors judge to combine the eye-catching quality of the best infovis with the directness
of the best statistical graphics: colors used sparingly and only to carry information, axes that
start at zero and are labeled clearly, names labeled directly on the curves rather than through a
separate legend, and a design where every one of the paper's six goals is satisfied at once.

The Wattenbergs also used the same name database to build a conventional statistical graphic — a
small multiple of histograms of the *last letters* of boys' names, over time — that the authors
adapt for their own Figure 10, and it carries a genuine, striking discovery: about a century ago,
some ten letters shared the bulk of the ending sounds; sixty years ago that had narrowed to about
six; today a single letter, N, ends 36% of American boys' names. Their explanation, following
Wattenberg (2007): a century ago parents had little practical freedom in naming — a handful of very
common names (John, William) dominated, often chosen from among relatives — and that constraint,
paradoxically, produced a broad, close-to-random spread of ending sounds. Today parents have far
more freedom, no single name dominates, but the abundance of soundalike choices (Aidan, Jaden,
Hayden) clusters heavily on shared endings. The paradox the authors flag explicitly: a century ago
the distribution of *names* was concentrated but the distribution of *sounds* was broad; today the
distribution of names is diffuse but the distribution of sounds is concentrated. Less constraint on
name choice leads, through the mechanism of soundalike clustering, to more concentration in how
names end — a genuine social-science insight produced by combining an interactive exploratory tool
with a plain statistical graphic.

## Discussion: what the two fields could learn from each other

The paper closes by naming the structural differences behind all the examples above. Infovis prizes
unique, distinctive displays; statisticians build generic methods meant to look and feel the same
across applications, valuing replication and objectivity over creativity and difference — an old
tension the authors compare to Adolf Loos's dictum in architecture that ornament is a crime. The two
fields also assume different audiences: statisticians write for readers who are already interested
and want a structured argument, so a graphic there is part of an explanation; infovis designers
write for readers who are not yet interested, so a graphic there is a door opener. This shows up
even in how each field uses interactivity — infovis leans on video and animation to sustain
engagement, while statisticians, when they use interactivity at all, use it to link a graphic to
other graphics or to a model, in service of following an argument further.

The Baby Name Wizard leads the authors to an uncomfortable comparison: if it is indeed the best of
the examples discussed, then something built in 2005 outperformed, on their criteria, everything on
a "best of 2008" list — a reminder that technology in this area lags behind what would be genuinely
useful, in both directions. They close with a historical parallel rather than a resolution: a
century ago, the standard statistical display was the table, and the attractive, hand-drawn time
series and maps of that era were themselves the "infographics" of their day, not yet routine enough
for anyone to have learned what worked. Graphs eventually displaced tables as the default. The
authors' hope, stated plainly, is that today's infographics might undergo the same evolution into
tomorrow's statistical tools — and that naming the different goals openly, rather than trading
one-line verdicts of "good" or "bad," is what would let that happen.

## Sources

All material in this chapter is drawn from Andrew Gelman and Antony Unwin, "Infovis and Statistical
Graphics: Different Goals, Different Looks," *Journal of Computational and Graphical Statistics*
22:1 (2013), 2–28 — the sole assigned reading behind this chapter of Stat 243 (Berkeley), catalogued
under `units/graphics_files/gelmanUnwin2013` and reused, unit for unit, across three offerings of
the course (fall 2021, fall 2024, fall 2025). No slide deck, lecture transcript, or problem set
accompanied this reading in the material supplied; the chapter follows the paper's own eleven
sections. The source markdown is itself a model's reconstruction of a PDF with no extractable text
layer (its own banner: "the prose is a paraphrase in places... treat it as a pointer into the
original, never as a citable source"), so quotations reproduced here — from Tukey, Tufte, Cleveland,
Chambers et al., Fisher, Chatfield, Norman, Rehmeyer, and Yau — should be checked against the
original article before being cited elsewhere. The paper's own figures (the *Onion* parody of a USA
Today chart, the Wordle example, Nightingale's coxcomb, the redrawn Crimean War time series, the
health-spending scatterplot, the Afghanistan flowchart, and the Baby Name Wizard screenshot) are
referenced by the text but were not supplied as image files and are not reproduced here.

---

[← 7. First Three Weeks Logistics](07-first-three-weeks-logistics.md) · [Contents](index.md) · [9. Adaptive Rejection Sampling for Gibbs Sampling →](09-adaptive-rejection-sampling-for-gibbs-sampling.md)
