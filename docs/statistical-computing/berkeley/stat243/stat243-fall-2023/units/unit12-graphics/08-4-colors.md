---
title: 4. Colors
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit12-graphics.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Colors

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

I haven't converted this section to use Python, but the concepts
are still relevant in Python or other languages.

## Colors in R

The default colors can be seen with `palette()`. Using `col=i` in a plot
uses the ith element of the output of `palette()`. You can change the
palette:

```r
palette(c(“black”, “yellowgreen”, “purple”)`
```

See `colors()` for the colors available by name. You can also use RGB
levels, discussed next.

## Colorspaces

Colors live in a 3-dimensional space that can be parameterized in
several ways. One standard parameterization is RGB, which is a set of
three numbers indicating the intensity of red, green and blue. We can
use RGB levels to specify colors in R.

```r
x <- rnorm(10); y <- rnorm(10)
rgb(0.5, 0.75, 0) # each number is specified on scale of [0, 1]
plot(x, y, col = rgb(0.5, 0.75, 0))
col2rgb("yellowgreen") # on scale of {0,...,255}
```


Notice `rgb()` gives us back the color as a hexadecimal number
(`#RRGGBB`), where each of *RR*, *GG*, and *BB* is 2-digit hexadecimal
number (base 16) in the range 0 (00) to 255 (FF), so red is `#FF0000`
(all red, no green, no blue). A
string in this format can be used to specify colors and you'll run
across this in R if you work with colors.

Another parameterization is HSV: *hue*, *saturation* (colorfulness
metric), and *value* (brightness). Let's see the demo code to see how
colors vary as we change HSV values using *rainbow()*.

```r
n <- 16
par(mfrow = c(1,2))
## rainbow varies hue while keeping s and v constant
pie(rep(1, n), col = rainbow(n, s = .5))  # reduce saturation
pie(rep(1, n), col = rainbow(n, v = .75)) # reduce brightness
```

A parameterization that uses a more absolute measure of colorfulness
than saturation is HCL (hue, chroma, luminance). In the example code below,
none of the colors stands out more than the others, unlike
the RGB or HSV (see above) based rainbows.

```r
library(colorspace)
par(mfrow = c(1,2))
pie(rep(1, n), col = rainbow_hcl(n, c = 70, l = 70), main = 'HCL')
pie(rep(1, n), col = rainbow(n), main = 'RGB')
```

The `colorspace` package provides a lot of helpful tools for
manipulating colors (including for `ggplot2` and `shiny`), including
determining palettes for qualitative, sequential, and diverging values.

## Color sequences

If we're using color to illustrate a continuous range of values, we need
a meaningful color sequence. To construct a continuous color set giving
a sequence of colors you can use a variety of color schemes:
`rainbow()`, `heat.colors()`, `terrain.colors()`, `topo.colors()`,
`temp.colors()`, and (in the `fields` package), `tim.colors()`. (I know
the Tim of `tim.colors`! He likes to fish.)

The main thing to avoid is a sequence in which the colors do not appear
to vary smoothly or in some cases may not even appear monotonic. Let's
examine a variety of the sequences:

```r
library(fields) # includes image.plot(), which takes image() and adds a legend; also includes tim.colors

n <- 20; xs <- ys <- 1:n
gr <- expand.grid(xs, ys)
U <- chol(exp(-rdist(gr)/6))
par(mfrow = c(2, 2))

## rainbow color sequence
image.plot(1:n, 1:n, matrix(crossprod(U, rnorm(n^2)), n, n),
                col = rainbow(32),
                xlab = '', ylab = '', main = 'rainbow colors')

## heat.colors
image.plot(1:n, 1:n, matrix(crossprod(U, rnorm(n^2)), n, n),
                col = heat.colors(32),
                xlab = '', ylab = '', main = 'heat colors')

## temp.colors
temp.colors <- function(n=25){
  m <- floor(n/2)
  blues <- hsv(h=.65, s=seq(1,0,length=m+1)[1:m])
  reds <- hsv(h=0, s=seq(1,0,length=m+1)[1:m])
  c(blues,if(n%%2!=0) "#FFFFFF", reds[m:1])
}

image.plot(1:n, 1:n, matrix(crossprod(U, rnorm(n^2)), n, n),
                col = temp.colors(33), zlim = c(-3.5, 3.5),
                xlab = '', ylab = '', main = 'temp colors')
 ## here I force zlim to be symmetric about zero and use an odd number (33) of levels so that the midpoint is white

## tim.colors
image.plot(1:n, 1:n, matrix(crossprod(U, rnorm(n^2)), n, n),
                col = tim.colors(32),
                xlab = '', ylab = '', main = 'tim colors')
```

`temp.colors()` is a good blue-to-red "diverging" color scheme that
emphasizes magnitudes around a central point, with two hues - one for
each direction.

The `RColorBrewer` package is good for choosing colors for unordered
levels, sequential ordering, and two-way diverging color ordering and
the `ColorBrewer` website provides recommendations. We'll see an example
in the section on mapping.

## Overplotting of points

As a sidenote, if you have a scatterplot with many points that will
overplot each other (as well as creating a huge file if using a vectorized format), consider the
`scatterSmooth()` function as well as the `hexbin` package. The former
creates a two-d density plots with outlying individual points included,
while the latter creates an empirical two-d density by binning into
hexagonal areas. A third approach is to have your color be partly
transparent, so that overplotting results in darker colors. Note that
this may not work on all devices. We can specify transparency level as
either the 4th number in `rgb()` on a scale of 0 (transparent) to 1
(opaque - the default), or as a fourth hexadecimal number on the scale
of 00 to FF (0 to 255); e.g., `#FF000080` would be half-transparent red,
since 80 is one-half of FF in base 16.

```r
library(hexbin, quietly = TRUE)
x <- rnorm(10000); y <- rnorm(10000)
par(mfrow = c(1, 3))
plot(x, y, main = 'naive')
smoothScatter(x, y, main = 'scatterSmooth')
plot(x, y, col = rgb(0, 0, 0, .1), pch = 16,
  cex = .5, main = 'transparency')
```

```r
par(mfrow = c(1, 1))
bin <- hexbin(x,y)
plot(bin, main = 'hexbin')
```

## Colorblindness

One thing to be aware of is that 7-8% of men are color blind. As we see
in the demo code, the standard result of this is to make it difficult to
distinguish red and green, so one may want to avoid color schemes that
have both of these in them. We can use `dichromat()` from the
`dichromat` package to assess the effect of colorblindness on viewing of
one's images.

```r
library(dichromat)
showpal <- function(colors){ # helper function to show colors
  n <- length(colors)
  plot(1:n, rep(1, n), col = colors, pch = 16, cex = 4)
}

dev.off() # close the graphics windows to clear out old color stuff
par(mfrow=c(2, 1))
showpal(palette()) # show default palette colors

---

[← merge pdf files into one pdf](07-merge-pdf-files-into-one-pdf.md) · [Up: contents](index.md) · [here's how those look with standard colorblindness →](09-here-s-how-those-look-with-standard-colorblindness.md)
