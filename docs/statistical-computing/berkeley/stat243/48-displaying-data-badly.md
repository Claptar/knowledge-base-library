---
title: "48. Displaying Data Badly"
course: "Berkeley Stat 243"
chapter: 48
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 48. Displaying Data Badly

## What this covers

Howard Wainer's 1984 essay "How to Display Data Badly" takes the working definition of a *good*
data graphic — that it shows data, shows it accurately, and shows it clearly — and reads it
backwards. Each requirement gives a family of ways to fail it, and Wainer turns those families into
twelve named "rules," each pinned to a real published graph or table. Alongside the rules he uses
three quantities, mostly due to Edward Tufte, that make "bad" measurable rather than just felt: the
*data density index*, the *data-ink ratio*, and *perceptual distortion*. This chapter assumes only
that the reader knows what a statistical graphic is for; no prior exposure to Tufte is needed, though
Wainer draws several measures directly from him.

## The three ways to fail

Wainer starts from a definition of good display in three parts: (a) show data, (b) show it
accurately, (c) show it clearly. A display can go wrong in exactly three places, and the twelve rules
sort accordingly:

- Rules 1–2 attack **showing data** — leave it out, or hide it once it is there.
- Rules 3–5 attack **accuracy** — break the correspondence between the numbers and the picture.
- Rules 6–12 attack **clarity** — the data are present and undistorted, but obscured.

## Showing data: density and ink

### Rule 1 — minimize the data density

Tufte's **data density index (ddi)** is the number of numbers plotted per square inch. Wainer reports
newspaper and journal graphics ranging from a ddi of .1 up to 362. A graphic from *Social Indicators
III*, printed in four colors at 7 by 9 inches, carries only 18 numbers — ddi $18/63 \approx .3$ —
against a median of .6 for that book. A plot in a *JASA* article by Friedman and Rafsky (1981) shows
4 numbers in 8 square inches (ddi $.5$) against a *JASA* median of 27; Wainer's aside is that the
plot's actual point — a competing method of analysis had not been fruitful — could probably have been
made just as well in prose. High density does not guarantee a good graph and low density does not
guarantee a bad one, but it measures how efficiently a graphic does the one thing it does better than
a table: pack in information.

### Rule 2 — hide what data you do show

A graph with almost no information looks embarrassingly empty. The fix, for bad display, is
**chartjunk**: nondata ink filling the space to disguise the paucity of content (Wainer's example is
labor productivity, Japan versus the US, one number per year across three years, padded out with
decoration). Tufte's **data-ink ratio** — ink used to plot data over total ink in the graphic —
measures the opposite: it falls toward zero as more of the graphic becomes decoration.

Two further ways to bury data already on the page: plot points faintly against a fine grid (useful
while drawing, useless afterward), or choose a scale so large that real variation vanishes into it,
often defended as "honesty requires that we start the scale at zero." Wainer's example is a *Social
Indicators III* chart of private-school growth whose scale hides a clear mid-1950s rise; redrawn on
an appropriate scale, it immediately raises the question of a link to *Brown vs. Topeka School
Board*.

## Showing data accurately

An accurate graphic represents numbers, which have magnitude and order, by a visual metaphor whose
magnitude and order match. Rules 3–5 break that match three ways.

### Rule 3 — ignore the visual metaphor altogether

If the data are ordered and the encoding has a natural order, violate it: Wainer's example is a bar
chart in which the bar labeled 14.1 is drawn longer than the bar labeled 18. A subtler version changes
what the metaphor *means* partway through — one graph shades imports on one side of an axis and
exports on the other, while also shifting scale and time units across the switch. Wainer contrasts
this with an 1786 Playfair graph on the same import/export question, which needs no such trick and
tells the story clearly in one consistently scaled picture.

### Rule 4 — only order matters

The classic version encodes a quantity as the *length* of a shape when the eye actually perceives its
*area*. Because area grows with the square of a linear dimension, scaling a shape's radius or width
in direct proportion to a value inflates the apparent change far beyond the real one.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A bar pair scaled correctly by length next to a circle pair scaled by radius, showing the second pair looks far more different in area than the values warrant">
  <text x="70" y="18" text-anchor="middle" font-size="12" fill="currentColor">length encodes value</text>
  <rect x="45" y="150" width="26" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="85" y="105" width="26" height="65" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="70" y="185" text-anchor="middle" font-size="11" fill="currentColor">ratio 1 : 2.3</text>
  <text x="245" y="18" text-anchor="middle" font-size="12" fill="currentColor">radius encodes value</text>
  <circle cx="215" cy="150" r="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <circle cx="270" cy="145" r="23" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="245" y="185" text-anchor="middle" font-size="11" fill="currentColor">area ratio 1 : 5.3</text>
</svg>
<figcaption>Scaling a shape's radius in proportion to a value, while the eye compares area, turns a
modest change (2.3x) into a much larger-looking one (5.3x in area) — the mechanism behind Rule 4 and
Tufte's perceptual-distortion measure.</figcaption>
</figure>

Wainer works a real example: a *Washington Post* graphic on the declining value of the dollar from
Eisenhower to Carter, ddi of only .1, data-ink ratio near zero. Tufte's **perceptual distortion (PD)**
is the ratio of perceived change to actual change; reading the value scale against the graphic's own
drawn sizes gives

$$\text{Actual} = \frac{1.00 - .44}{.44} = 1.27 \qquad \text{Measured} = \frac{22.00 - 2.06}{2.06} = 9.68$$

$$\text{PD} = 9.68 / 1.27 = 7.62,$$

over 700 percent distortion — substantial, Wainer notes dryly, "but by no means a record." A version
redrawn without the area trick, with the time axis matched to the actual spacing between the
presidents shown, removes it.

### Rule 5 — graph data out of context

The interval or scale chosen for a time series changes what the picture argues even when every
plotted point is correct. A sharp drop can vanish if the series starts just after it; a small meander
can become a sharp change by narrowing the window and stretching the scale. Wainer's example is a
chart used by President Reagan to argue for the effects of a tax cut, drawn over a narrow, favorable
interval; a companion *New York Times* chart over the fuller interval gives the same data a different
reading. Taken to the extreme — dropping the quantitative scale entirely and showing only relative
position — this is what Wainer calls Ordinal Graphics, combining Rules 4 and 5 into a picture with
almost no checkable content at all.

## Showing data clearly

The remaining seven rules assume the data are present and undistorted; the graphic obscures them
anyway.

### Rule 6 — change scales in mid-axis

A graph of two newspapers' circulation, one "skyrocketing" and one "plummeting," hides a
700,000-reader jump the $y$-axis makes partway up, so the curves look far more different than the raw
numbers warrant. A time series of physicians' incomes plotted against a horizontal axis that ticks
every eight years for most of its length and then every year at the end looks close to linear;
redrawn against a regular time axis, the story changes.

### Rule 7 — emphasize the trivial, ignore the important

When a data set has one large, interesting comparison and one small, incidental one, the graphic gets
worse by making the small comparison easy to read and the important one hard. Wainer's example
compares men's and women's incomes across education levels and time: the large main effects are
education and sex, and time is comparatively minor, yet the layout forces the sex comparison to be
made by transposing vertically between two panels, while the minor time trend is what each panel
displays most directly.

### Rule 8 — jiggle the baseline

Comparisons are easiest when every series starts from the same baseline, which is exactly why a bad
graphic avoids one. A stacked chart of U.S. meat imports (beef, veal, pork, and others, from the
USDA's *Handbook of Agricultural Charts*) shades under each line to show that quantities are
cumulative, but this means every line except the bottom one is read against a wandering baseline set
by everything stacked below it: total volume is easy to see, and correspondingly it is hard to tell
whether, say, pork imports are rising or falling. An explicit total line, with each meat's own
quantity read against the flat time axis instead of against the meat below it, restores the
comparison.

### Rule 9 — Austria First! (order alphabetically)

Alphabetical order is a real convenience for looking something up, and a reliable way to hide any
structure the data have. Wainer's example is life expectancy by sex across ten industrialized nations,
listed alphabetically (the USSR alphabetized as "Russia"): read this way, the graph mostly conveys
"not much variation, women live a bit longer." Reordering the same numbers — all a stem-and-leaf
display does — makes the sex gap obvious at a glance and reveals the USSR as an outlier among the men.
Nothing about the data changed; only the order shown.

### Rule 10 — label (a) illegibly, (b) incompletely, (c) incorrectly, (d) ambiguously

Wainer's example is a *New York Times* graphic (August 1978) arguing that airline fare cuts were
lowering travel agents' commissions: the bar showing the decline carries a tiny label noting it
covers only the first half of 1978, omitting the year's heaviest travel — Labor Day, Thanksgiving,
Christmas. Even doubling that half-year figure for rough comparability with the full-year bars beside
it reverses the story: agents were doing quite well compared to earlier years.

### Rule 11 — more is murkier: more decimal places, more dimensions

A table gets harder to read by reporting more precision than anyone can use or the data justify.
Wainer takes a table from Dhariyal and Dudewicz (1981, *JASA*) on an optimal-stopping problem, giving
expected gain to five decimal places — for $N=10$: .62948, 6.92358, 69.86462 across three cost ratios.
Rounded to one decimal these become roughly .6, 6.9, 69.9, which reveals what the five-decimal version
buried: the gain columns are close to proportional to the cost ratio $b/c$, so the table likely
carries redundancy a coarser table would have exposed rather than concealed.

The same logic applies to dimensions: an extra dimension is an extra chance for ambiguity (length,
area, or volume?), and human judgment of area and volume is far less reliable than of length. Wainer's
example is a three-dimensional bar chart of per-share earnings and dividends over six years confusing
enough to have misled its own artist: one year's value is drawn as the *side* of a bar rather than its
face, a mistake a plain line chart could not make.

### Rule 12 — if it has been done well before, do it differently

The last rule is an appeal by counterexample: Wainer contrasts the U.S. Census Bureau's two-variable
color map — which uses varying color saturation and, building on earlier work by Wainer and Francolini
(1980), seduces readers into overreading what it communicates — with G. von Mayr's 1874 two-variable
map, done a century earlier with bars of varying width and frequency, "gracefully" rather than
"clumsily."

He closes with his nominee for "World's Champion Graph": Minard's 1861 depiction of Napoleon's 1812
Russian campaign, reproduced from Tufte. A single static picture carries six variables at once — army
size (422,000 crossing into Russia, down to 100,000 at a sacked and deserted Moscow), its
two-dimensional path, direction of movement, and, on the retreat, dates linked to a temperature scale
as the army collapsed to 10,000 recrossing into Poland. Wainer holds it up as the positive image
against which all twelve rules read as a negative.

## Summing up: the measures interlock

Wainer's closing point is that the three measures describe one underlying quality from different
angles: data density cannot be high if a graphic is cluttered with chartjunk; the data-ink ratio grows
as more of what is plotted is data rather than decoration; perceptual distortion shows up most where
an extra dimension or an inappropriate metaphor has been introduced. The rule for a *good* graphic,
read forward, is correspondingly simple: understand the data well enough to know what they say, let
the display say it with minimum adornment, keep scale and labeling straightforward, and — Wainer's
last piece of advice — spend time with the masters: Playfair, Minard, Tukey's *Exploratory Data
Analysis* (236 graphs, little chartjunk), and Francis Walker's 1894 *Statistical Atlas of the United
States*.

## Sources

- Howard Wainer, "How to Display Data Badly" (commentary; received September 1982, revised September
  1983), *The American Statistician*. Read from the STAT243 graphics-unit reading, identical across
  the Berkeley STAT243 fall-2021, fall-2024, and fall-2025 offerings
  (`units/wainer1984.pdf` / `units/graphics_files/wainer1984.pdf`).
- No lecture slides or transcript were supplied alongside this reading, and no problem-set questions
  were supplied; this chapter follows the paper alone, which is why it carries no Exercises section.
- The library conversion is model-reconstructed from a scan with no text layer; its header notes the
  prose is a paraphrase in places and every equation is unverified, which applies to the
  perceptual-distortion calculation and the decimal-place figures reproduced here. The paper's own
  Figures 1–25 survive in the conversion only as unlabeled per-page scanned images, not as numbered,
  captioned figures, so this chapter describes what the text says about them rather than reproducing
  them. The diagram above (length-versus-area schematic for Rule 4) is original to this chapter, built
  from the mechanism the text describes, not a redrawing of the paper's own figures.

---

[← 47. Simulation and Monte Carlo](47-simulation-and-monte-carlo.md) · [Contents](index.md)
