---
title: "39. Good Practices for Graphics"
course: "Berkeley Stat 243"
chapter: 39
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 39. Good Practices for Graphics

## What this covers

How do you make a statistical graphic that shows the data rather than distorting it, and how do
you get it out of R (or any plotting language) into a file that still looks right when someone
else opens it? This chapter covers the principles behind a good graphic, the difference between
vector and raster file formats and when to use each, and how to choose colors — including
colors that still work for colorblind readers. It assumes you can already produce a basic plot
(a scatterplot, a bar chart) in some language, and asks what to do differently once you can.

## Principles for a good graphic

A graphic earns its place when it has a high density of information relative to the space it
takes up, and when the relationships and patterns that jump out visually are the ones you
actually want the reader to see — not artifacts of how the data happen to be ordered or scaled.
A few principles follow from that goal.

**Reorder to reveal structure.** Categories or groups plotted in an arbitrary order (alphabetical,
say, or the order they appear in the data file) hide comparisons that a deliberate ordering — by
size, by time, by whatever the plot is actually about — would show immediately.

**Use more than two visual dimensions, carefully.** Beyond position on two axes, a plot can carry
information in color, in symbol or line type, or by splitting into multiple panels. Color is the
easiest of these to overuse: added where it isn't informative, it adds visual noise rather than
information. Multi-panel plots — often called *trellis* plots, or "small multiples" when every
panel shares the same scale and axes — are one of the most reliable ways to add a dimension
without overloading a single panel, precisely because the reader compares panels using the same
learned scale.

**Avoid 3-d graphics** unless the third dimension truly carries information a 2-d version would
lose — most 3-d plots in practice make comparison harder, not easier, because perspective distorts
apparent size and position.

**Think carefully about the baseline.** The lowest value shown on an axis is doing real work: zero
is usually the right baseline, because it makes the length of a bar or the height of a point mean
what it visually appears to mean. The clearest place this goes wrong is a stacked bar chart. The
segment that sits directly on the axis has a common baseline across every bar, so its length reads
off correctly at a glance. Every segment stacked above it does not: its top and bottom both float,
so the reader has to mentally subtract two positions to recover its length, and in practice people
don't — they compare the *position* of the top edge, which conflates the segment's own size with
the sizes of everything stacked underneath it.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="Two stacked bars showing why a shared baseline matters for comparing segment length">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="195" x2="340" y2="195" stroke="currentColor" stroke-width="1.5"/>
  <text x="20" y="199" font-size="12" fill="currentColor">0</text>

  <!-- Bar 1: bottom segment 60, top segment 40 -->
  <rect x="100" y="135" width="50" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="100" y="95" width="50" height="40" fill="currentColor" fill-opacity="0.4" stroke="currentColor"/>
  <text x="125" y="222" text-anchor="middle" font-size="12" fill="currentColor">Bar 1</text>

  <!-- Bar 2: bottom segment 110, top segment 40 (same value as Bar 1's top) -->
  <rect x="230" y="85" width="50" height="110" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="230" y="45" width="50" height="40" fill="currentColor" fill-opacity="0.4" stroke="currentColor"/>
  <text x="255" y="222" text-anchor="middle" font-size="12" fill="currentColor">Bar 2</text>

  <line x1="70" y1="195" x2="70" y2="135" stroke="currentColor" stroke-width="1.5" marker-start="url(#arrowhead)" marker-end="url(#arrowhead)"/>
  <line x1="200" y1="195" x2="200" y2="85" stroke="currentColor" stroke-width="1.5" marker-start="url(#arrowhead)" marker-end="url(#arrowhead)"/>
  <text x="10" y="168" font-size="11" fill="currentColor">shared</text>
  <text x="10" y="180" font-size="11" fill="currentColor">baseline</text>

  <line x1="310" y1="135" x2="310" y2="95" stroke="currentColor" stroke-width="1.5" marker-start="url(#arrowhead)" marker-end="url(#arrowhead)"/>
  <line x1="330" y1="85" x2="330" y2="45" stroke="currentColor" stroke-width="1.5" marker-start="url(#arrowhead)" marker-end="url(#arrowhead)"/>
  <text x="285" y="70" font-size="11" fill="currentColor">40</text>
  <text x="335" y="65" font-size="11" fill="currentColor">40</text>
</svg>
<figcaption>The bottom segment of each bar starts at zero, so its length can be compared directly
between bars. The two darker top segments are the same size (40 units) in both bars, but they sit
at different heights because the segments beneath them differ — so they do not look the same size,
which is exactly the failure a shifting baseline causes.</figcaption>
</figure>

**Avoid encoding data as area, volume or angle.** Studies of graphical perception find that people
are much worse at comparing areas, volumes and angles than at comparing positions or lengths, and
worse yet at angles than areas. That rules out pie charts for anything beyond the crudest
comparison, and it is also the reason a stacked bar's floating segments are hard to read: the
reader is implicitly being asked to compare lengths that don't share a baseline, which is most of
the way to comparing areas. Where you have a choice, encode a quantity as position along a common
axis, or as length from a common baseline — horizontal position is generally read slightly more
accurately than vertical.

**Label and scale consistently.** Axes should be labeled with units, a legend should appear
wherever a color or symbol needs decoding, and when a figure has multiple panels the axis ranges
should match across panels wherever that's feasible — otherwise a difference in apparent slope or
spread may just be a difference in scale.

**Handle overplotting rather than living with it.** When you have too many points to see them all,
jittering helps only up to a point; beyond that you need a genuinely different strategy — smoothing
the density, binning, or using transparency — covered below under [colors](#overplotting-of-points).

**Prefer vector formats.** PDF and Postscript/EPS describe a plot as symbolic objects — points,
lines, text — and rescale without pixelation. JPEG, PNG and TIFF store a fixed grid of pixels, so
enlarging them beyond their native resolution loses quality, and a raster file at high resolution
can be very large. The trade-off runs the other way for genuinely 2-d image data (a satellite image,
a heatmap of a very fine grid): rasterizing that data is natural, though any text or symbols laid
over it are then rasterized too. See [file formats](#vectorized-vs-rasterized-file-formats) below.

Rob Hyndman's [list of 20 rules for good graphics](http://robjhyndman.com/hyndsight/graphics/)
covers much of the same ground; see also the guidelines collected in
[this article](https://www.tandfonline.com/doi/full/10.1080/10618600.2014.989324).

## Reading real graphics critically

The best way to internalize these principles is to hold them up against graphics that were
actually published, some of which violate them and some of which don't. The course poses several
as discussion cases, worth working through against the list above rather than taking on faith:

- A [pie chart circulating online](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/graphics_files/trafficking.jpeg) intended to raise awareness of human trafficking — what does the pie-chart encoding cost it?
- Several time series of categorical data: a [New York Times piece on drug-overdose deaths](https://www.nytimes.com/interactive/2024/09/27/opinion/fentanyl-overdose-deaths.html), a [FlowingData graphic on causes of mortality by age and sex](https://flowingdata.com/2016/01/05/causes-of-death), a [New York Times piece on US electricity sources by state](https://www.nytimes.com/interactive/2024/08/02/climate/electricity-generation-us-states.html), and a [New York Times piece on Olympic medal counts by country over time](http://www.nytimes.com/interactive/2016/08/08/sports/olympics/history-olympic-dominance-charts.html).
- A [scatterplot of life-expectancy statistics across European countries](https://academic.oup.com/view-large/figure/81018073/dyr146f2.gif), from a [paper in the International Journal of Epidemiology](https://academic.oup.com/ije/article/40/6/1703/801755) — what can and can't be read off it, and what other encoding might show the pattern in the data better?
- A miscellaneous [online graphic](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/graphics_files/exampleGraphic.png) to critique directly.
- A [blog post walking through improving a real visualization](https://www.r-bloggers.com/2021/07/improving-a-visualization/) of streaming-service market share between 2020 and 2021 — useful as an example of the *process* of revision, not just a finished product.

The course materials also point to three items that were not converted along with this chapter and
are worth tracking down separately: a striking bad pie chart from a 2014 New York Times
advertisement, Howard Wainer's 1984 article on graphical failures (dated examples, but the failure
modes recur in modern graphics), and Gelman and Unwin's 2013 piece reinterpreting Florence
Nightingale's famous graphic on causes of death in the British Army during the Crimean War. See
[Sources](#sources).

## Graphics devices

A plot is drawn onto a *device*. Historically this meant an actual physical device; today it just
means the context a plot is rendered into — a window on screen, or a file in some format. On
Unix-like systems the on-screen device is traditionally X11, a window managed by the X windowing
system; in practice, on-screen plotting today is handled by whatever window manager your operating
system and plotting software use.

The reason this matters practically: a plot's proportions on screen and on paper are not the same
thing. The aspect ratio (width to height), the margins relative to the plotting area, and the size
of symbols and text relative to the whole plot all typically need to be re-tuned once you print or
export to a file — what looks right in an interactive window is often wrong once it's a fixed-size
image in a PDF or a slide.

## File formats

### Vectorized vs. rasterized file formats

A **vectorized** format — PDF is the standard example — stores a plot as a set of symbolic objects:
points, line segments, text, symbols. Resizing the image just rescales those objects, so there's no
loss of resolution no matter how much you zoom in or blow the image up. A **rasterized** format —
JPEG, PNG, TIFF — instead stores a fixed grid of pixel values. Enlarging a raster image beyond its
native resolution doesn't create new detail; it just shows you more of the same pixels, which is
what "pixelation" looks like. At high resolution, raster files can also become very large, since
every pixel is stored explicitly.

The practical recommendation is to use vector formats in most situations — the two exceptions being
(a) plots with so many individual points or line segments that the vector file itself becomes huge,
and (b) inherently two-dimensional image data (a photograph, a fine grid of raw pixel values), for
which rasterizing is the natural representation anyway — with the caveat that any text or symbols
overlaid on such an image get rasterized along with it.

### Conversion utilities

Unix systems carry a set of standard command-line tools for moving between formats (Windows and
Mac have GUI equivalents). `pdftops` converts PDF to Postscript, and with the `-eps` flag, to
Encapsulated Postscript; `ps2epsi` also produces Encapsulated Postscript. `gs` (Ghostscript) is the
general-purpose tool: it converts between Postscript/PDF and raster formats, and can extract or
merge pages of a PDF.

```bash
# convert from pdf to jpeg
gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.pdf

# extract pages from a pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

# merge pdf files into one pdf
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf \
   -dBATCH in1.pdf in2.pdf in3.pdf
```

## Colors

The examples below are R, but the underlying ideas about colorspaces, palettes and colorblindness
apply regardless of what language you plot in.

### Colors in R

`palette()` shows the current default set of colors; `col = i` in a plot refers to the `i`-th
element of that palette. You can install your own:

```r
palette(c("black", "yellowgreen", "purple"))
```

`colors()` lists every color available by name. Colors can also be specified numerically, as RGB
levels, discussed next.

### Colorspaces

Color is 3-dimensional, and there's more than one way to parameterize that space.

**RGB** specifies a color by the intensity of red, green and blue.

```r
x <- rnorm(10); y <- rnorm(10)
rgb(0.5, 0.75, 0)                 # each number is on a scale of [0, 1]
plot(x, y, col = rgb(0.5, 0.75, 0))
col2rgb("yellowgreen")            # on a scale of {0, ..., 255}
```

`rgb()` returns a color as a hexadecimal string `#RRGGBB`, where `RR`, `GG`, `BB` are each a
two-digit base-16 number from `00` (0) to `FF` (255) — so pure red is `#FF0000`. This is the format
you'll see whenever a color needs to be written down rather than looked up by name.

**HSV** (hue, saturation, value) parameterizes color by hue, a colorfulness measure (saturation),
and brightness (value). Varying hue while holding saturation and value fixed is exactly how
`rainbow()` generates a color sequence:

```r
n <- 16
par(mfrow = c(1, 2))
pie(rep(1, n), col = rainbow(n, s = .5))   # reduce saturation
pie(rep(1, n), col = rainbow(n, v = .75))  # reduce brightness
```

**HCL** (hue, chroma, luminance) uses a more perceptually absolute measure of colorfulness than
HSV's saturation. The practical difference shows up directly: an HCL-based rainbow has every hue
appear equally vivid, whereas an RGB- or HSV-based rainbow has some hues (yellow, in particular)
read as visually louder than others even at "the same" saturation and value.

```r
library(colorspace)
par(mfrow = c(1, 2))
pie(rep(1, n), col = rainbow_hcl(n, c = 70, l = 70), main = "HCL")
pie(rep(1, n), col = rainbow(n), main = "RGB")
```

The `colorspace` package builds on this to generate whole palettes — qualitative, sequential, or
diverging — for use with `ggplot2` or `shiny`.

### Color sequences

To represent a continuous quantity with color, you need a sequence in which the colors vary
smoothly and, ideally, monotonically — a sequence that visually plateaus or reverses direction
partway through misrepresents the data even if every individual color is fine on its own. R offers
several built-in sequences (`rainbow()`, `heat.colors()`, `terrain.colors()`, `topo.colors()`), and
the `fields` package adds `tim.colors()`.

A **diverging** sequence — two hues moving away from a shared central value, useful when the
quantity has a meaningful zero or midpoint — can be built directly from HSV, forcing an odd number
of levels so the midpoint lands exactly on white:

```r
temp.colors <- function(n = 25) {
  m <- floor(n / 2)
  blues <- hsv(h = .65, s = seq(1, 0, length = m + 1)[1:m])
  reds  <- hsv(h = 0,   s = seq(1, 0, length = m + 1)[1:m])
  c(blues, if (n %% 2 != 0) "#FFFFFF", reds[m:1])
}
image.plot(1:n, 1:n, z, col = temp.colors(33), zlim = c(-3.5, 3.5))
# zlim forced symmetric about zero, and an odd number of levels (33),
# so the midpoint of the color scale is exactly white
```

`RColorBrewer` is a good default for choosing palettes systematically, whether the underlying
values are unordered categories, a single sequential ordering, or a two-sided diverging one; the
ColorBrewer website gives the same recommendations interactively.

### Overplotting of points

A scatterplot with many points overlapping is a case where the points themselves stop conveying
information — and, in a vector format, it also inflates the file size, since every point is stored
individually. Three fixes:

- `smoothScatter()` renders a 2-d density estimate with the outlying individual points still drawn on top.
- The `hexbin` package builds an empirical 2-d density by binning into hexagonal cells.
- Partial transparency lets overlapping points darken where they overlap, though this doesn't render on every device. Transparency is set as a fourth number to `rgb()` on a scale of 0 (fully transparent) to 1 (opaque, the default), or as a fourth hex pair from `00` to `FF` — e.g. `#FF000080` is half-transparent red, since `80` is half of `FF` in base 16.

```r
library(hexbin, quietly = TRUE)
x <- rnorm(10000); y <- rnorm(10000)
par(mfrow = c(1, 3))
plot(x, y, main = "naive")
smoothScatter(x, y, main = "scatterSmooth")
plot(x, y, col = rgb(0, 0, 0, .1), pch = 16, cex = .5, main = "transparency")
```

```r
par(mfrow = c(1, 1))
bin <- hexbin(x, y)
plot(bin, main = "hexbin")
```

### Colorblindness

Roughly 7-8% of men are color blind, most commonly in a way that makes red and green hard to tell
apart — so a palette that leans on red versus green as its main contrast will fail for a meaningful
fraction of readers. The `dichromat` package simulates this directly, letting you check a palette
before committing to it:

```r
library(dichromat)
showpal <- function(colors) {
  n <- length(colors)
  plot(1:n, rep(1, n), col = colors, pch = 16, cex = 4)
}
par(mfrow = c(2, 1))
showpal(palette())               # default palette
showpal(dichromat(palette()))    # the same palette, simulated colorblind view
```

`tim.colors()` from `fields`, checked the same way, holds up reasonably well under the simulation —
worth knowing if you already favor it for spatial data.

## Sources

- Fall 2025 offering, unit 12: [1. Good practices for graphics](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd), [3. Graphics file formats](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd), and [4. Colors](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd) — used as the primary text throughout, since it is the more recent, essentially-identical revision of the Fall 2024 version of the same three sections. The Fall 2024 version was also supplied and cross-checked; the two differ only in a couple of added links and a filename fix.
- Referenced but not supplied in either offering, and therefore not covered here beyond naming them: an example bad pie chart from a December 2014 New York Times advertisement (`graphics_files/shell.md` in the course repository), Howard Wainer's 1984 article on graphical failures (`graphics_files/wainer1984.md`), and Gelman and Unwin's 2013 reinterpretation of Florence Nightingale's Crimean War mortality graphic (`graphics_files/gelmanUnwin2013/index.md`).
- Two further files were supplied alongside these — `stat243-fall-2021/units/unit12-integ/01-1-differentiation.md` and `02-2-integration-optional.md` — but they cover numerical differentiation and integration, an unrelated topic that shares only the "unit 12" label with the graphics unit in a different year's offering of the course. They are not used in this chapter.

---

[← 38. Numerical Optimization for Statistics](38-numerical-optimization-for-statistics.md) · [Contents](index.md) · [40. Data Storage, Formats, and I/O →](40-data-storage-formats-and-i-o.md)
