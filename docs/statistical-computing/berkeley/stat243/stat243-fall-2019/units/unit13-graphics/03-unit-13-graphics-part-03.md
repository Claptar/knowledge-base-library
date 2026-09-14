---
title: Unit 13 — graphics Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit13-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — graphics Part 03 —

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit13-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

The _colorspace_ package provides tools for manipulating colors.

### **7.2 Color sequences**

If we’re using color to illustrate a continuous range of values, we need a meaningful color sequence. To construct a continuous color set giving a sequence of colors you can use a variety of color schemes: _rainbow()_ , _heat.colors()_ , _terrain.colors()_ , _topo.colors()_ , _temp.colors()_ , and (in the _fields_ package), _tim.colors()_ . I know Tim! He likes to fish.

The main thing to avoid is a sequence in which the colors do not appear to vary smoothly or in some cases may not even appear monotonic. Let’s examine a variety of the sequences (see the demo code).

_temp.colors()_ is a good blue to red “diverging” color scheme that emphasizes magnitudes around a central point, with two hues - one for each direction.

The _RColorBrewer_ package is good for choosing colors for unordered levels, sequential ordering, and two-way diverging color ordering and the _ColorBrewer_ website provides recommendations. We’ll see an example in the section on mapping.

### **7.3 Overplotting of points**

As a sidenote, if you have a scatterplot with many points that will overplot each other (as well as creating a huge file), consider the _scatterSmooth()_ function as well as the _hexbin_ package. The former creates a two-d density plots with outlying individual points included, while the latter creates an empirical two-d density by binning into hexagonal areas. A third approach is to have your color be partly transparent, so that overplotting results in darker colors. Note that this may not work on all devices. We can specify transparency level as either the 4th number in _rgb()_ on a scale of 0 (transparent) to 1 (opaque - the default), or as a fourth hexadecimal number on the scale of 00 to FF (0 to 255); e.g., _#FF000080_ would be half-transparent red, since 80 is one-half of FF in base 16.

34

**require** (hexbin, quietly = TRUE) x <- **rnorm** (10000); y <- **rnorm** (10000) **par** (mfrow = **c** (1, 3)) **plot** (x, y, main = 'naive') **smoothScatter** (x, y, main = 'scatterSmooth') **plot** (x, y, col = **rgb** (0, 0, 0, .1), pch = 16, cex = .5, main = 'transparency')

###### **scatterSmooth**


<!-- Start of picture text -->
naive scatterSmooth transparency<br>G<br>GGGGGGGGGGGG G GGGGGGGGGGGGGG G GGGGGGGGGG G GGGGGGGGGGGG G GGGGGGG G GGGGGGGGGGG G GGGGGGGGG G GGGGGG GG GGGGG G GGGGGGGG G G G GGGGG G GGGG G G GG GGGGGGGG G GGGG G GG G GGGG G GGGGGGGGGG GG GG G GG G GGGGG G GGGGGGGGGGG GG GGG G GGGGGGGG G GG G GGGGGGG G GG G GGGGGG G GGGGGGGGG G GGG G GGGG G G G GG G GGGGGGGGGGG G GG G G GG GGG G GGGGG G GGGGGGG G GGGG G G G GGGGG GG GGGGGGGG G GGGG G G G G G G GGGG GG G G GGGGG GG G GGGG G GG GGGGG GGGGGGGG G GG G GG G G GG G G GGGGG G GGGGGGG GG G G GG G GG G G GGG GGGGGGG GG G G GGG GG G GG GGG G G G G G GGGGG GGGG GGGGGGGGG G GG G GG GG GGGGG G GGGGGGG G G G G GG GGGG G GG G G G GG G G G G G G GGG GG G G GG G GGGG GG G G GG G G GG GG GGG G G G GG G GGGGG G G G GGG G G GG GG GG G GG GGGGG GG G G GG G GG G GG GGG GGG GGG GG GG GG GG G GGG GGG G GG GG G G G G GGGGG G GG G GGG G GG G GG G G GG G GGG G G G G G GGG G GG GG G G GG GGGG G G GGGG GG GG G GG GGGGGG G G GGGG GGGGGG G G GGGG G G G G GG G GG GGGG G G GG GG G GGGGGG G GG GG GG G G G GGGG G GG GG GGGG GG G GGG GGGGG G GG GG GG G G GGG GG GGGG GGGG GGG GGGG G GGGG GG G G G G G G G G GGG G GGG GG GGGG G G G GGGGG G GG GGGG GGG G G GGG GG G GG G GGGG GGGGGGGG GGG GG GGGG GG GGGG G GG G GG G GGG GG GGG G G GG GGG G GGGG G G GGGG GGG G GGG GG G GGG G G G GGG G GG GG G GGG GG GGG GGG GG G GGG G GGGGGGGG G GG G G GGGGG G G GGGG G G GG G GGGG G GGG G G G G GG GGGG G GG G G G G G GGGGG GGG G G GG G GGG GGGG GGG GG GGG GG G GG GGGGG G G GG G GG G G G G GG GGG GG GGG GGG GG G G GGGG GG GG G G GG G G G G GG G G GG GGGGG G GG GG G GGG GGGG GG GGGG G GGGGGGG G G G GGGG GGG G GGG G G G GGGG G GG GG G GGGGGGG G GGG G GGG G GGGGG G GGGGGGGGGG GG G G GGG GG G GG G G GG G GG G G GGGG GG GG GGG G G G GGGG G GGG GG GG G GG G GG G G GG GG G GGGGGGGG GGGG GG GG GGGG GG GGGGG G G G GG G GG GG GG GG GG G GG GG GG G G G G G G G GGGGGGGG G GGGGGGG GG GGGGGG G G G G G GGG G GGGG GG G GG GGGG G G G GG G GG G GG GG GGGGGGGGG G G G G G GG GG GGGGGGG G G G G G G G GGGGG GG GGG GG GG G GGGGGG G GGGG G G GG G G GGGGGG GG G G G GGG GGGG G G GG G G GGGGGG G GG G GGG G GGGGGGGGG G GGGG GGGGG GGGG G G G G G GGG G GG G G G GG G GG G G G G G G G GGGG GGG GGGG G GGGG G G G GGGG GGG G GG GGGGGG G GGGG G GG G G G G GG GGG GG G GGGGG GG G GG GGG G G GGG GG G G GG G G GG G GGGGGGGG GG GGGGGGGG GG G G GGG G GGGG G GGGGGGG G GGGG GGG G GG GGG GG GGGG GGGGGG G GG GG GG G G G GGGGGGG GG G G GGGG G GGGG G G GGGG GGGG G G GG G G G G G GGG GGG G G G GGG G GG GGG GG GG G G GGGG GG GGGG G GGG G GG G GG G GGG GG G G G G GGGG G G GG G G GGGGGGGGG GG GGG G GGGGG G GGGGGGGG G G GG GGG GG GGGGGGG G GG G G G G G G G GG G GG GG GGG G GG G GGGG G GGGG G GGG GG GG G G G GGG G G G G GG GGGGG G GG GG GG GGGG GG GG G G GGG G GGGGGGGGG GG G G G G GG G GGG G GGG GGG G G GGGGGGG G G G GGG G GG G GG G G G GG G GGGG G G GGG G G GG G GGGGGGGGGGG G G G GGGG GG G G G GG GG G GGG GGG GG GGGGGGG G GG GGGG G GGG GG GGG G GGGGG G GG G GGGGGGGGG G GG G G G GG G G G G GG GGGG GG GGGGG G GGG G GG GG GGGG GG GGGGG G G GG G GG G G GG GG GG GGGG G G GG GG GG G GGGGGGGGGG G GGGGGG G GGG G G G GGGGGG G G G G G GGGGG G GG G GGGGG G GGG G GGG G GG GGG G G GGGG GG GG G G G G G GGGGGG GGG GGGGGGGG G GG GGG GG G GG G GGGG G GG GG G G GG G GGGGGGGG GGG GG GGG GG GGG G G GG G GGG G G GG G GG G G G GG G G GG G GGGGGGGG G G G GGG GG G G GGGGG GGGG G G GGGGG G G G GGG GG GGGG GG GGG G G G GGG G G GGGG GGGGG GGG G GG G G G G G GG G GGG GG GGG GG G GGG G GGG GGG GG G GG GGGG G GGGG GG GGG G G GG GGGGGGGG GGG G GGG GG G G G G GGGGGGGGGGGGGGG GG GG G G GG GGG G G G G GGG GGGG G GG GG GGG GG G G G GG GGGG G GGG GG GGG G G G GGG G G G GGGG G G G GGG G GG G GGG G GG GG GG G GG G GGGGGGGG G G G GG GG GGG G GGGGG G GGGG GGGG G G GGGGG GG GG G GGGG GG GGGG G G GGG GGGGG G GGG G GG G G G GG G G G GGGG G GG GG G G GGGGGG G G G GG G GGGGGGGGGGG GG GGGGG G G G GGG G GG GG G GG GG GGGG GG G GGGGG GG G G GGGG G G G GGG GG G GG GGG G G GGGG GGGGGG G G GGGGG G G GG G GGGGGGG G GGG G GGG G GGGGGGGG G G GG GG G GG G G G GGGGGGG GG GG G GG G GG G G G GG GG G G G G G G GGGGGG G GGG GG G G G GG G GG GGGG G GG GG G G GGGGGGG G GG GGGGGG G GGG GGG G GG GGG GG G G GG G G GG GG GGGG G GGG GG GGG G G G GGG G GGG GGG GGG GG G GGG GG GG GGGG G GG GG GG G GGGGGGGG G G G G G G G G G G GGGG GGGGGG GG GGG GG GGGGG G GGGGG G GGGGGGGGGGGGGGGGG G GGGGGGGGGGG G G G GGGG G GGGGG G G G GGGGGGG GG GGGG G G G G G G G GG GG GG GG GGGGG G GGG G GGGGG GG G G GGGGGGGGGGGG G GG G G G G GG G G GG G G GG G G GGG GGGGGG G GGG GG G G G GGG GG GG GGG GG GG GGG GGGG GG GGGGGG G G G G G G GGG GGGGGGGG G GG G GG G G G GG G GGGG G GGG G G G GG GG GG G G GG GG G G G G GGG GGG G G G GG G GG G GGGGGGG G GGG G GGGGG G GGG G G GG G GG GG G GG G GG GGG GG GGGG G GG G G GG G G G GGGG GG GG GG GGGG G G G GGG GGG GG G G G G GG GGGGGGG GGG G G GG G GGGGGGGGGGG G G G GG G G G GGG GGG G GG GGGGGGGG G GG GGG GGG GGGG G GG GGGGGGGGG G G G G G G G G G G GG GG G GG G G GG GGG G GG GGGG GGG G G G GG G G G GG GGGGG GGG G G G GGGGGGG G G GGG G G G G G G GG GG GGG G GGGGG G GGGG GGG G GGGG GGG G GG G G G GGGGG G GGG G G G GG G GG G GG GGG GG GG G GGG G GGGGG GGGG GGG GGGG G G G GG GG GGGGG GGG G GG GG G GGG GG G GGG GGGGGGGGG G G G G GG G G G G GGGG G G G GG GG GG GG G GG GG G GG G G GG GGGG GG GG GGGGG G GG G GGG GGGGG G G G G G G G G GGG GGG GGG GGGG G G GGGG G GGGGGGGG G GGG G GG GGGG G GG GG GG GGG GGGG G GG GG G G G GGGG G GG GGGGGG G GG GG G GGGGGGG GGG G G G G GGGGG GG GG G G G G G G GGG G GG GGG G G GG GG GG G G G GGGGG G G GGGG GG GG GG GG G G G G GGG G G G G G G GGGGG GGGG GGG GGG G GGG GG G G G GGG G G GGG GG GGGG G GGG GG GGG GGG G G G GGG GG GGGG GGGGGGG GGGG G G G GGGG G GGG G G G GGG GG G G G GGG GG G G GG G GGG GG GGGGGGGGGGGGGGG G GGG GG GGGGGGGGG GG GG G GG G GG G GGG GGGG GGG G GGGGG GG GGGGGGGG GG G G GG G GGGGGGGGGGGG G G GG GGGGG GGG G G G G GGG G GG G GGGG G G G GG GG G G GGGGGG G G GG GGG GGG GGGGGG GG GGGGGGGG G GGG G GGG G GGGGGGGGG G GGGGGG G GG G GGGGGGGG G G G GGGGGG GG GG G G G GGGG G G G GGGGGGGGG G GG G GGGGG G GGGGGGGGGGGG G GGGGG G GGGG G G G GG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGG<br>G G GG<br>G<br>−4 −2 0 2 −4 −2 0 2 −4 −2 0 2<br>x x x<br>2 2 2<br>0 0 0<br>y y y<br>−2 −2 −2<br>−4 −4 −4<br><!-- End of picture text -->

**par** (mfrow = **c** (1, 1)) bin <- **hexbin** (x,y) **plot** (bin, main = 'hexbin')

35


<!-- Start of picture text -->
hexbin<br>Counts<br>90<br>2 84<br>79<br>73<br>68<br>62<br>0 57<br>51<br>46<br>40<br>34<br>−2 29<br>23<br>18<br>12<br>7<br>−4 1<br>−4 −2 0 2<br>x<br>y<br><!-- End of picture text -->

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
