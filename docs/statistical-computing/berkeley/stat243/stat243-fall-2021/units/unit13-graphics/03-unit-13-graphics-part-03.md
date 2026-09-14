---
title: Unit 13 — graphics Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit13-graphics.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — graphics Part 03 —

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit13-graphics.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

in2.pdf in3.pdf

## **7 Colors**

The default colors can be seen with _palette()_ . Using _col=i_ in a plot uses the ith element of the output of _palette()_ . You can change the palette:

palette(c(“black”, “yellowgreen”, “purple”)

See _colors()_ for the colors available by name. You can also use RGB levels, discussed next.

### **7.1 Colorspaces**

Colors live in a 3-dimensional space that can be parameterized in several ways. One standard parameterization is RGB, which is a set of three numbers indicating the intensity of red, green and blue. We can use RGB levels to specify colors in R.

**rgb** (0.5, 0.5, 0) _# each number is specified on scale of [0, 1]_ **plot** (x, y, col = **rgb** (0.5, 0.5, 0)) **col2rgb** ("yellowgreen") _# on scale of {0,...,255}_

n <- 16 **pie** ( **rep** (1, n), col = **rainbow** (n)) _# rainbow varies hue while keeping s and v constant_ **pie** ( **rep** (1, n), col = **rainbow** (n, s = .5)) _# reduce saturation_ **pie** ( **rep** (1, n), col = **rainbow** (n, v = .75)) _# reduce brightness_ **library** (colorspace) **pie** ( **rep** (1, n), col = **rainbow_hcl** (n, c = 70, l = 70)) _# colors in the HCL colorspace ## none of these colors stand out more than others, unlike the RGB rainbow_

33

Notice _rgb()_ gives us back the color as a hexadecimal number ( _#RRGGBB_ ), where each of _RR_ , _GG_ , and _BB_ is 2-digit hexadecimal number (base 16) in the range 0 (00) to 255 (FF), so red is #FF0000. A string in this format can be used to specify colors and you’ll run across this in R if you work with colors.

Another parameterization is HSV: _hue_ , _saturation_ (colorfulness metric), and _value_ (brightness). Let’s see the demo code to see how colors vary as we change HSV values using _rainbow()_ .

A parameterization that uses a more absolute measure of colorfulness than saturation is HCL (hue, chroma, luminance). In the example in the demo code, none of the colors stands out more than the others.

The _colorspace_ package provides a lot of helpful tools for manipulating colors (including for _ggplot2_ and _shiny_ ), including determining palettes for qualitative, sequential, and diverging values.

### **7.2 Color sequences**

If we’re using color to illustrate a continuous range of values, we need a meaningful color sequence. To construct a continuous color set giving a sequence of colors you can use a variety of color schemes: _rainbow()_ , _heat.colors()_ , _terrain.colors()_ , _topo.colors()_ , _temp.colors()_ , and (in the _fields_ package), _tim.colors()_ . I know Tim! He likes to fish.

The main thing to avoid is a sequence in which the colors do not appear to vary smoothly or in some cases may not even appear monotonic. Let’s examine a variety of the sequences (see the demo code).

_temp.colors()_ is a good blue to red “diverging” color scheme that emphasizes magnitudes around a central point, with two hues - one for each direction.

The _RColorBrewer_ package is good for choosing colors for unordered levels, sequential ordering, and two-way diverging color ordering and the _ColorBrewer_ website provides recommendations. We’ll see an example in the section on mapping.

### **7.3 Overplotting of points**

As a sidenote, if you have a scatterplot with many points that will overplot each other (as well as creating a huge file), consider the _scatterSmooth()_ function as well as the _hexbin_ package. The former creates a two-d density plots with outlying individual points included, while the latter creates an empirical two-d density by binning into hexagonal areas. A third approach is to have your color be partly transparent, so that overplotting results in darker colors. Note that this may not work on all devices. We can specify transparency level as either the 4th number in _rgb()_ on a scale of 0 (transparent) to 1 (opaque - the default), or as a fourth hexadecimal number on the scale of 00 to

34

FF (0 to 255); e.g., _#FF000080_ would be half-transparent red, since 80 is one-half of FF in base 16.

**require** (hexbin, quietly = TRUE) x <- **rnorm** (10000); y <- **rnorm** (10000) **par** (mfrow = **c** (1, 3)) **plot** (x, y, main = 'naive') **smoothScatter** (x, y, main = 'scatterSmooth') **plot** (x, y, col = **rgb** (0, 0, 0, .1), pch = 16, cex = .5, main = 'transparency')


<!-- Start of picture text -->
naive scatterSmooth transparency<br>−2 0 2 4 −2 0 2 4 −2 0 2 4<br>x x x<br>4 4 4<br>2 2 2<br>y y y<br>0 0 0<br>−2 −2 −2<br><!-- End of picture text -->

**par** (mfrow = **c** (1, 1)) bin <- **hexbin** (x,y) **plot** (bin, main = 'hexbin')

35


<!-- Start of picture text -->
hexbin<br>Counts<br>3<br>115<br>108<br>2 101<br>94<br>1 86<br>79<br>72<br>0 65<br>58<br>51<br>−1 44<br>37<br>−2 30<br>22<br>15<br>−3 8<br>1<br>−2 0 2 4<br>x<br>y<br><!-- End of picture text -->

### **7.4 Colorblindness**

One thing to be aware of is that 7-8% of men are color blind. As we see in the demo code, the standard result of this is to make it difficult to distinguish red and green, so one may want to avoid color schemes that have both of these in them. We can use _dichromat()_ from the _dichromat_ package to assess the effect of colorblindness on viewing of one’s images; see more in the demo code file.

**library** (dichromat)

showpal <- **function** (colors){ _# helper function to show colors_ n <- **length** (colors)

**plot** (1:n, **rep** (1, n), col = colors, pch = 16, cex = 4) }

**dev.off** () _# close the graphics windows to clear out old color stuff_ **par** (mfrow= **c** (2, 1))

**showpal** ( **palette** ()) _# show default palette colors # here's how those look with standard colorblindness_ **showpal** ( **dichromat** ( **palette** ())) _## notice red and green similarity_

36

---

[← convert from ps to jpeg](02-convert-from-ps-to-jpeg.md) · [Up: contents](index.md)
