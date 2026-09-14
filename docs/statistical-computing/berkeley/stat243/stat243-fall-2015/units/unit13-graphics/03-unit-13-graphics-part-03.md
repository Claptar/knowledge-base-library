---
title: Unit 13 — graphics Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit13-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — graphics Part 03 —

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit13-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

32

Notice _rgb()_ gives us back the color as a hexadecimal number ( _#RRGGBB_ ), where each of _RR_ , _GG_ , and _BB_ is 2-digit hexadecimal number (base 16) in the range 0 (00) to 255 (FF), so red is #FF0000. A string in this format can be used to specify colors and you’ll run across this in R if you work with colors.

Another parameterization is HSV: _hue_ , _saturation_ (colorfulness metric), and _value_ (brightness). Let’s see the demo code to see how colors vary as we change HSV values using _rainbow()_ .

A parameterization that uses a more absolute measure of colorfulness than saturation is HCL (hue, chroma, luminance). In the example in the demo code, none of the colors stands out more than the others.

The _colorspace_ package provides tools for manipulating colors.

### **7.2 Color sequences**

If we’re using color to illustrate a continuous range of values, we need a meaningful color sequence. To construct a continuous color set giving a sequence of colors you can use a variety of color schemes: _rainbow()_ , _heat.colors()_ , _terrain.colors()_ , _topo.colors()_ , _temp.colors()_ , and (in the _fields_ package), _tim.colors()_ . I know Tim! He likes to fish.

The main thing to avoid is a sequence in which the colors do not appear to vary smoothly or in some cases may not even appear monotonic. Let’s examine a variety of the sequences (see the demo code).

_temp.colors()_ is a good blue to red “diverging” color scheme that emphasizes magnitudes around a central point, with two hues - one for each direction.

The _RColorBrewer_ package is good for choosing colors for unordered levels, sequential ordering, and two-way diverging color ordering and the _ColorBrewer_ website provides recommendations. We’ll see an example in the section on mapping.

### **7.3 Overplotting of points**

As a sidenote, if you have a scatterplot with many points that will overplot each other (as well as creating a huge file), consider the _scatterSmooth()_ function as well as the _hexbin_ package. The former creates a two-d density plots with outlying individual points included, while the latter creates an empirical two-d density by binning into hexagonal areas. A third approach is to have your color be partly transparent, so that overplotting results in darker colors. Note that this may not work on all devices. We can specify transparency level as either the 4th number in _rgb()_ on a scale of 0 (transparent) to 1 (opaque - the default), or as a fourth hexadecimal number on the scale of 00 to FF (0 to 255); e.g., _#FF000080_ would be half-transparent red, since 80 is one-half of FF in base 16.

33

**require** (hexbin, quietly = TRUE) x <- **rnorm** (10000); y <- **rnorm** (10000) **par** (mfrow = **c** (1, 3)) **plot** (x, y, main = 'naive') **smoothScatter** (x, y, main = 'scatterSmooth') **plot** (x, y, col = **rgb** (0, 0, 0, .1), pch = 16, cex = .5, main = 'transparency')


<!-- Start of picture text -->
naive scatterSmooth transparency<br>G<br>GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GG GGGGGGG GGGGGGGGGGGGG G GGGGGG G GGGGGGGGGGGGGGG G GGGGG G G G GGGGGGGGGGGG G GG G GGGGGGGGGG G GGG G GG G G GGGGG GG GGG GGGGGGGGGGGGGGGG G GG G G GGGG GGGG G GGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGG G G G GGGG G G G GG G GGGG G G GG GGGGGG G G G GGGGGG GG GGGG G GGG GGG GGGG G G G GG G GGGGGG G G G G GGG G G G G GG GGGGG GG GGGG G GG G G GGGGG GGGGG G G G GGG GGGG G GGGGG GG G GGGGG G GGG G G G G GG GG G G GGG GG GG GG G GG GGGG G G G G GG G GG G GG G G G G G GGG G GGG GGGGGGGGG G GG G GGGGG G G G G G G G GGGGGG GG G GG GGGG GG G G G GG GG GGG GGGG G G GG GGG G GGG G G G G GGGG G G GGG GGGGG GG GG G GG GGGGG G GG GG G GG G GG G GGGG G GG GG G GGG GGG G GGGG GGGG GGGGG G G G G GGG G G G GGGG G GG G GGGGG G GG GGG G G GGGG GGGGGGG G GGGGG G GG GGGG G GG G GGGGGG G GG GGG GG GG GGG G G GGG GG G G G G GG GG G GGG G GGGG G G GG G G GG G G GG GGGGG GG GGGGGG GG G GG GG G G G GGG GG G GG G G G GGG GGGGGGG GG GG G GGG G GGGGG G GGGGG G G GG GG G G GGGGG GGGGG G G G G GG G GG GG G G GG G G GGG GGGG GGG G G G G G GGGGGGGG GG GGG G GG GG GG G G G GGGG GG G GG G G GGGGGGGGGG G G G G GGGG GG GGGG GG G GG G G GG G G GG G G G G GG GGG G G GGG GG GG GG G G GGG GG G G GGG G GG G GGGG GG GGG G GGG GGG GGG G G G GGGGGG G GGG G GG GGGGGG GGGG G G GGGG GGG G G G GG G GGG G G G GG G GGG G GG G G GG G GGG GGG G GGGG G GG G GGG GG GGG G GGGGGGG GGGGGGG G G GGGGGG G GGGG G GGG GG G G GGGGGGGG GGG G GG GGGGGG GG G GGG GGGGGGGG G G GG GGG G G G G GGGG G GGGGG G G G GGGG GGG G G GGG G G GG GG GG GG GGGGGG G GG GGGGGGGGG GG G GG GG GG G G G G G G GG GG G G GGGGGGGGGGG GG GGGGG G G G G G G GG G G G GG G GGGGG G G G GGG GG GG GG GG G G GG GGGGGG G GGGGGG GGG GGGGG GG GG G GGGGGG G GGG GG G GGG GGGG G G GG GGG GG GG G G G GG G GG G GGGGGGGGGGGGG GGG G G G G G G GGGG GGGG GGGG G G GGG GGG GG GGGGGGG G GGG GGGGG G GG GG GGGG G GG GGGGGGGGGG GG GGGGGGGG G G G GGG G GGGGGGGGGGGG G GGG G GG G GGG GG G G G GG GGGGG GG G G G G G G GGG GGG G GGGG GGG GG G GG GG GG G GG GGG G GGG G GGG G GG G GGGGG G G G G GGGGGGGGGGGGGGG G G G G GG G GG GGGG G G GG GGGGG G G GG GG G GGGGGG G GG G G GG GGGGGGGGGGG G G G GGGGGGGGGGGGGGG G GGGGGG GGGG G G G GGG GG GG GGGGG G GG G GGGGG G GGGG G GG GG G GGG G GGGG G GGGGG GG GGGG G GGGGGGGG GG GG G G G G GG G G GGG G GGGGGG GG GGGGG G G G GGGG G GG G GGGG G GG G GGGGGGG GG G G GGGG G GGG G GG G GG G GGGGGGGGGG G GGGGGG GGGG GGGG GGG GGGG G G G GGGGGGGGGGG GG G GG G G G G G G GGG GG GGGGGGGGG G G G GGGGGGGGGGG GG G G GG G G GG G G G G GGGGGG G GGGGG G GGGGG GG GGGGG G GGGGGG G G GGG GGG G GGG GG GG G GGG G G GGGG GGG G GGGG GG G G GG GGG GGGG GGG G G GG G G G G GGG G GG GGGGG G GGGG G GG G GGGGGGGGGGG GGG GG G GGGG GG G GG GGG G G G G G GGG G G G GG G GG GG GG G GG G GG G GGGGGGGGGGGG GG GGG G G GG G GG GGG G GGG G GG G GGG G GGGGG G G G G G GGG GGG G G GG G GGGGGGGGG GG GGG G GGGGGGG G GGGGGG G G G G G GGG G GGG GG GGG GGG GGGG GGG G G GGGGGGG G GGG G G G GGGG G G GG GGGG G G GG GGGG G GGGG G GGGGG G GGG GGG G G GGGGGG G GG G G G G G GG G GGGGG G G GG G GG GG GGGG GG GG GGG G GG G G GG G G G GG G GGGGG G GGGG G GGGGGGGG G G G GGGGG G G G GGGGGGG G GG GG GGGGG G GGGG GGG GG G GGGGGGGGGGGG GG G G GGG GGG GGGG GGG GGGGG GG GGGGG G G GGG GG GGG GGGGG G G GGGG G GGGGG GGG G G G GG G GG GG GGG GGGGG GG G G GG G GG GGG G G G GGG G GGG G G G GGGG GG G GGGG GG G GG GGGG GGGGGG G G GGG G G GGGGGGG GG GG GGG GGG GGG GGGGGG GGG GGGGGGGGGGGGGGGG G GG G GGG G GGGGG G G G GGG G GG G GGGGGGG G GGGGGGGGG G G G G G G G GGG G G G GGGGG G G G G G GGGGGGGGG GGGGG GGG G G GG GGGG GG G G GGG G GGGG G GG GG GGGGGGG GGG GGGGGGGG G GG GG G G GGGGGGGGGGGG GGG GGGGGGG G GGG GGGG GGGGGG G GGG G G G GG GGG G GGG G G GG G GGG GG GGGGG GGGG GGG G GGG G GG G GGGGGG G GG G G G GG G G GG G GG G GGGGGGGG G G G GG GG GGG G GG G GGG GG GGG G G GG G G GGGGG GG G G G G G G G G GGGGGG GG GGGGG G GGGGGGGGG GGGG GGG G GGGG G G G GGGGGGGG G GG GGGGGGGG GGGGGG GG G GG GGG G GGGGGGGGGG G GG G G G GG G GGGGG G G G G GGGG GGGGG GG G GG GGGGGG G G G GG G G GG GGGG G GG G G G G GGGG GGGGGGGGGG G GGG GG GGGG G GG GG GG G G G GGGGGGG G G G G GGG GGGGGG G G GG GG GG G GGG GGG GG GGG G G G GGG G G GGGG GGG G GG G GG GGG G G G GG GG GG GGG GGG GGGGGGG GGG GGGGG G G G G G G G GGGGGG GG GGG G GG G G G G GG GG G GG GGGG GGGGGGGGGGGG G GGG G G GG GGG G G G G G G G GG G G G GGGG G G G GGG G G GG GG G G GG GGGGGGG G GG G G G G G G GG G G GG G G G GG G GGGGGGGGG GGGG GGGG G G G GGG G G G G G GG G GGGG GG GG G GG G G G GG GG G G G GGGG G G G G G GGGG GGGGG G G GG GG GGG G GG G G GG G GG GG GG G GG G GGGGG G G G GGGGG G GG G GGGG GGG GG G GGG GGG G G G G GGG G GGGGGG GG GGG G GGG G GG GG G GG G G G GGG G G G G GG G GGG G GG G GG GGG GG GGGGG GGGG G G GG G G G G GGGGGGG G GG G G G GGGGG GG GG GG G G GGGG GGG G GG GG G GG GGG G G GG GGGG GG GG G GG GG G G GG G GGGG GGG GG GG GG G G GG GGG GGG G G G GGGGG GG G GGGGG GG G G GGGG GGG GG GG G GG G G GGGG GG G GGG G GG G GGG GG GG G GGGGG G GGG G GG G G GGG GGG G G G GGG GGG GGG G G GG G G G GG GGGG G G GGGGG GGGGGG GGGG G GG G GGGG G G GGGG GG G GGGGGGG GG G G GGG GG G GGG GG G G GG GGG GG G GGGGG GGG GG G GG GGG G GG G G GG G G GG G GG G GG GGGG G GGGG G G GGGGG G GGGGG G GG G G GGG GGGGG GG G GG G G G G G GGG G G GG G GG GG G G GGGGG G GG GG GG G GG G GG G G G GGGG G G GG GGG G G G G GG G G GGG GG GGG G G G GGGGGG G GGGGGGGGGGG G GGGGG GG G G GG G GGG G GGG GGG G G GGG GG GGGG G GG G GG G G GGG G GGGGGGG GG GG G G G GG G GGGGGGGGG GG GGGG G GG GGG GG G GGGGG G GGG G G G GG G G G GGGGGGGGGGGGG G GGGG G G GG GGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGGGGGGGG G G G GGGGGGGGGGGGGGGGGGG G G G GGGGGG G G GGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGG<br>G G G<br>G<br>−2 0 2 4 −2 0 2 4 −2 0 2 4<br>x x x<br>par (mfrow = c (1, 1))<br>bin <- hexbin (x,y)<br>plot (bin, main = 'hexbin')<br>4 4 4<br>2 2 2<br>0 0 0<br>y y y<br>−2 −2 −2<br>−4 −4 −4<br><!-- End of picture text -->

34


<!-- Start of picture text -->
hexbin<br>4<br>Counts<br>116<br>2 109<br>102<br>94<br>87<br>80<br>0 73<br>66<br>58<br>51<br>−2 44<br>37<br>30<br>23<br>15<br>−4 8<br>1<br>−2 0 2 4<br>x<br>y<br><!-- End of picture text -->

### **7.4 Colorblindness**

One thing to be aware of is that 7-8% of men are color blind. As we see in the demo code, the standard result of this is to make it difficult to distinguish red and green, so one may want to avoid color schemes that have both of these in them. We can use _dichromat()_ from the _dichromat_ package to assess the effect of colorblindness on viewing of one’s images; see more in the demo code file.

**library** (dichromat)

showpal <- **function** (colors){ _# helper function to show colors_ n <- **length** (colors)

**plot** (1:n, **rep** (1, n), col = colors, pch = 16, cex = 4) }

**dev.off** () _# close the graphics windows to clear out old color stuff_ **par** (mfrow= **c** (2, 1))

**showpal** ( **palette** ()) _# show default palette colors # here's how those look with standard colorblindness_ **showpal** ( **dichromat** ( **palette** ())) _## notice red and green similarity_

35

---

[← convert from ps to jpeg](02-convert-from-ps-to-jpeg.md) · [Up: contents](index.md)
