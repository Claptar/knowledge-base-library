---
title: merge pdf files into one pdf
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit15-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# merge pdf files into one pdf

**Source:** [`units/unit15-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf -dBATCH in1.pdf

in2.pdf in3.pdf

### **7 Colors**

The default colors can be seen with _palette()_ . Using _col=i_ in a plot uses the ith element of the output of _palette()_ . You can change the palette:

palette(c(“black”, “yellowgreen”, “purple”)

See _colors()_ for the colors available by name. You can also use RGB levels, discussed next.

#### **7.1 Colorspaces**

Colors live in a 3-dimensional space that can be parameterized in several ways. One standard parameterization is RGB, which is a set of three numbers indicating the intensity of red, green and blue. We can use RGB levels to specify colors in R.

**rgb** (0.5, 0.5, 0) _# specified on scales of [0, 1]_ **plot** (x, y, col = **rgb** (0.5, 0.5, 0)) **col2rgb** ('yellowgreen') _# on scale of {0,...,255}_

Notice _rgb()_ gives us back the color as a hexadecimal number ( _#RRGGBB_ ), where each of _RR_ , _GG_ , and _BB_ is 2-digit hexadecimal number (base 16) in the range 0 (00) to 255 (FF), so red is #FF0000. A string in this format can be used to specify colors and you’ll run across this in R if you work with colors.

Another parameterization is HSV: _hue_ , _saturation_ (colorfulness metric), and _value_ (brightness). Let’s see the demo code to see how colors vary as we change HSV values using _rainbow()_ .

A parameterization that uses a more absolute measure of colorfulness than saturation is HCL (hue, chroma, luminance). In the example in the demo code, none of the colors stands out more than the others.

The _colorspace_ package provides tools for manipulating colors.

principles in Murrell’s piece in JCGS 2013#1 Murrell points out colorspace and

28

#### **7.2 Color sequences**

If we’re using color to illustrate a continuous range of values, we need a meaningful color sequence. To construct a continuous color set giving a sequence of colors you can use a variety of color schemes: _rainbow()_ , _heat.colors()_ , _terrain.colors()_ , _topo.colors()_ , _temp.colors()_ , and (in the _fields_ package), _tim.colors()_ . I know Tim! He likes to fish.

The main thing to avoid is a sequence in which the colors do not appear to vary smoothly or in some cases may not even appear monotonic. Let’s examine a variety of the sequences (see the demo code).

_temp.colors()_ is a good blue to red “diverging” color scheme that emphasizes magnitudes around a central point, with two hues - one for each direction.

The _RColorBrewer_ package is good for choosing colors for unordered levels, sequential ordering, and two-way diverging color ordering and the _ColorBrewer_ website provides recommendations. We’ll see an example in the section on mapping.

#### **7.3 Overplotting of points**

As a sidenote, if you have a scatterplot with many points that will overplot each other (as well as creating a huge file), consider the _scatterSmooth()_ function as well as the _hexbin_ package. The former creates a two-d density plots with outlying individual points included, while the latter creates an empirical two-d density by binning into hexagonal areas. A third approach is to have your color be partly transparent, so that overplotting results in darker colors. Note that this may not work on all devices. We can specify transparency level as either the 4th number in _rgb()_ on a scale of 0 (transparent) to 1 (opaque - the default), or as a fourth hexadecimal number on the scale of 00 to FF (0 to 255); e.g., _#FF000080_ would be half-transparent red, since 80 is one-half of FF in base 16.

**require** (hexbin, quietly = TRUE) x <- **rnorm** (10000); y <- **rnorm** (10000) **par** (mfrow = **c** (1, 3)) **plot** (x, y, main = 'naive') **smoothScatter** (x, y, main = 'scatterSmooth') _## KernSmooth 2.23 loaded ## Copyright M. P. Wand 1997-2009_ **plot** (x, y, col = **rgb** (0, 0, 0, .1), pch = 16, cex = .5, main = 'transparency')

29

###### **scatterSmooth**

###### **naive**


<!-- Start of picture text -->
naive scatterSmooth transparency<br>GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G GG G G G GGGG G GG G GGGG G GGGG G GGGGGG G GGGGGGGGGGGGG GG GGGGG GG GGGGGG G GGGGGGGGGGGGGG G G G G G GGGGG G GGGGGGG G GGGGG G GGGGGGGG GG GGGGGG G G G GGGG G GGGGGGGGG G G G G GGGG G GG GGGGGGGG GG GG GG GGG G G GG GGGGGGG G G GG G GGGGG G G G GGGGGGGGG GGGG G GGGG GGGGG G G G G GG GGGGGGGG G GG GG GGG GG GGG G G G G GG G G GG G GG G G G GGG GG GGGGGGGG G GGG G GG G GG G GG GG GG GG G G GGGGGGG GG G GG GG G G G GG G GGGGG GGGG GG G G G G G G GG G GGG GG GG G GGGG GG G G GGGG G G G GG GG GG G G G G G GGG G G GGG G GG GGG G GG GGGGGG GG GGGGGGGG G GGG GG GGGG G G GG G GG GG G GGGGG GG GG GGG GGG GG GG GG GGGG GG GG GG GGGGGGGGGGGGGGGGG G GG GG GG GGG G GG G GGGGGGG GGGG GG GGG G GG GG GG G G G G G GGG GG G GGGG G G G GG G G G GG GG G G GGG G G GGGGG GGG GG GG G G G G GG G GGG G G GGGGGG G GGGGG GGG GGG G G G GGGG G G G GGGG GGGG G GGGGG G G G GG G GGG G G GG G G G GG GG GGG G GGG G GG G GGGGG G G G G GGG G GG GGGGG G G G GGGGG G GGG G G G GGG GGG G G GG G G G G GGG GG GG GGGG GG G GG G G GG G G GG G G G G GGGG G G G GGGG G G G G G GGG G G G GGG GG GG G GG G GGG G G G GGGG GG GGGG G G GGG GGGGG G G GGGG G GGG GG G GGG G G GGGG G G G G G GG GGGGGGG GG GGG GGGGG GG GGG GG G G G GG G GG GG G G GGGG GG GGGG G GG GGG GGGG GGGG GGGGGG G GG GGGGGGGG GG GG GG GGG G G GGG G G G G G G GGG G G G GG G GG G GGG G G GGGGG G GG GG G G GG GGG G G GG G GG GG GG G G G GG G GG G G G G G GG GG GGG GGG GG G GG GG GG G GG G GGGGGG GGG G G G G GG GGGGG GG G G G GGGGGG GGGGGG G G GGGGGGG GG GG GG GGG GG GG GGGG G G G GGGGG GG GGGGG G GGG GG G G GGG GG GG GGG GGG GG G GG GGG G G G GGGGGGGGGGGGGGG GG G G GG GGGG GGGGG G GG G G G GG GGG G GG GG GG GG GGG G GGGGGG GG G G G G G GGG GGG G GGG GGG GGG G GG G G G GGGG G GG GG G G GG GG G G GGG GGG G G GG G G GGG GGGGGGG G GGGG G GGGG GG GGG GG GG G GG GGG GGGGGG GGG G G G GG GGGG GG GG G GGGGGGGG G GGG G GGG G GGG G G GGG GGG G G G GG G GGGGG G G G GGGG GG GGG GGG GGG G GGGGG G G G GG GGG GGGGG G GG GGG G GGG GG G G G GGGG G GGGG G GG GG G GGG GGGG G GGGGGGG G G G G G GGGGGGGG G GGG G G GG G G GGGGG G G G GGG GG G GG GG G G GGGGGGGGG G GGGG GG G GG G GG GG G GG GGG GG G GGGGGG GG GG G G G GGG G G G GGGG G GG G G G GGGGGG G GG G GG GG G G GGGG GG GG GG GGGG G GGGGGG G G G GG GG GG G G G GG GGGG GGGGGGG G GGGGGGG G G GG GGG GG GG G G GGG G G G GG GGG G GGGGGGG G G G GGGG G GGG G GGGGG G GGGG GGG G GG GG G G G GGGGGGGG G G G GGGGGG GG G GGG G G GGG G GGG G GGGGGGG G G G GG G GGGG GG GGGG GG GGGGGGGGGGGG GG GGGGG GG GG GGGGG G G GG G GG GGG G GGG GG G G G GGG G GGGGGGG G GGGGGG GGG G GGGG GGGGG G GG G GGGGGG G G GG GGGGG G GGGG G GG GG G G G G GGGGGGGG GG G GG G G GGG G GG G G GG GGG GG GG G GG GG GGG G GG G G GG GG GG GG GGG GGGG GG GGGGG G GGG GGG GGG GGGGG GGG GG GG G GGG G G G G G G GG G GGGGGGGGGGG G GG G GG G GGGGGG G GGGGG G GGG GG GG G GGG G GG G GGG G G GGGGGGGGGG GG GGGGG G GGGGG G GGG GG GGG G GG G G G GGGGG G GG G G G GGG GGGG G G G GGGGGGG G GG G GGG G GGGG G G G GG G GGGG GGG GGGGG GGGG GGG G G GG GGGGG G G GG GG GG G G G G G GG GGGGGGGGGG G GGGGGGG G GGGGGGGG G GGG G GGG G G G GGGGG G GG G GG G G GGG GG G G GG GGGGGG G GG GG G GG G G GGGGG GGGGG G GGGGG G GGGG G GG G GGGG GGG G G G G G G GGGG G GGGGG G GG GG GG G GG GG GG GGG G G G G GGG G G GGGG G GGG G GG G G GGG G G GGG GG GG G G GG GGGGG G GGG G G G G GGGGGGGGG G G GGG GG G GG GG GG G GGG GGG GG G GGG G GGG GG GGGG G GGG GG GG G GG G GGG GGG GG G GGG G GGGG G GGGGGGGG G GGGGG GG G GGGGGGG GG G GG GGG G GG G GGGGGGG GG GG G GG GGG GGG G GGGGG GGG G G G G GGGGGGGG G GG G G G GGGG GG GGGGGG G G G GG G GGGGGG G GGGGG G GG GG GG G G G G GGGGG GGGGG GG G GGG GGGGGGGGGGGGGGGGGGGGG G G G G G G G GG GG GGGG G GGG GG G G GGG GGG GG G G G GG GG GG G GGG GGG G GG GGG G GGG GG G GG GGGGGGGGGG GGG GG G G G GG GG GGGG GG G G GG G GGG G GG G GGG G GGG G G G G G GG G GG G GGG GG GGGGG G G G GGG G GG G GGGGGGGGGGGG G G GG GGGGG G GGG G GGGGG G GGGG G G G G GG GGG G GGGGGGGG GGG GG G G G G GGG GGGG G G G GGG GGG GGG G GGGGGG GG GG G G G G G G GGGGG GGG GGGGGGGG G GG GG G G GGG GGGGG GG GGG G GGGG GGGG G G GGGG G GG GG G GGG GG GGGGGG GGGG G G G GGGG GGG G GG G GG G G GGGG G G G GG G GG GGG GG G GGGG G GGGG GG GGG G G G GG GG G GGG G GGGGGGGGGG GGGGG GGGGGGG G G GG GGG G GGGG GG GGGG G GGG GG GG G GGGG GGG GGG GG GGGG G GGG G GG GG GGGG G G G GG G G G G G G G GGGGGGGGGGG GG GGGG G G GG GG GG GGG GG GG G G G G GG GGG GGG G G GGG G GGGG G GGG G GGGGGGGG GG G GGG G G GGG G GG GGG G G GG GGG G GGG GG GGGG G G GG GGGGG GG G GGGG GGG G GG GG G GGG G G G G G G G G GGGG GG GG GG G GGGG GG GG GG GGGGG GG GGGG G GGGG G G G G GG GGG GG G G GG GG GGGGG G G GGG GGGG G G G GGG G GGGGG GGG G G GGGG G GGG GG GG GGG G G G GGGG GG G GGG G GGGGGGG G G G GGG G GG GG G G GG G GG GG GGGG GG G G G G G G G GG GGG G G G GG G GGG G GGG GGG GGGG GG GGGG G GG G G G G GGGGGG G G G GG G G GG GG G G GGG GG G G G G G G G G GGGG GGG GGG G G G GGGGGG G GG GG G G G G GGG G GG GGG G GG GG G GG GGGGG GG G GG G G G GGG GGG GG G GGG GG GG G G GGGGGGGGG G GG GG G GG GGGG G G GGG G G GG GGG G GGGGGG G G G GGGG G GG GGGG G GGG G GG GG G G G GGG GG G GGG G G G GGGGGGG GGGG G GG G GGG G G GG GGG GG GG GG GG G GG G G G GGGGGG G G GGGGG GG G G G GG GG GGGGGG G G GG GGG G G GG G G GGG GGGGGGG GGG GG G GGGGG G G GG G G G G GGGG G GG G G GG G GG GGG G GGGGG GGGG G G G G G GGGGG GG GG GG GG GGG G GG GG G GGGG G G GGGGG GGG GG G GGGGG GG GG G GGG GG GG G G G G GGG G GG G GG GG G GGG G GGG GGG GG G G GG GGGGGGGGG G GGGGG G GGG G G GG G GG GGG GGG GG GG GG GG  GG GGGGGG GG G GGGG GGG G G GG GG GG G GGGGGG G G G GGGGGG GGG GGG G G G GGGGGGG G GGGGG G G G GG GG G G GGG G GG G G G G GG G GGG GGG G GGGGGG G GGG G GGGGGGGG G G G G G GG G GGGGGGG GGG G G GGGG G GG G GG GG GGGGGGG GG GGGGGGGGGGGG G GG GGGG GGGGGGG GG GGGG G GGG GGGG GGG G G GGG GGGGGG G GGGGG G GGGGG G GGG GGG GGGGGGGGGGGGG GG GGGGGG GG GGGG G GGGGG GGG GGGGG G GGGGGGGGGGG G GGGG G GG GG G G GG GG GGGGGGGG G GG G G G G GG GGGGG G G G GGGGGGG G GGGGGGGGGG G G G GGGGGGGGGG G GGGGGG G GGG G GGGGGG G GGGGGGG G G G GGGGG G G G GGGGGGGG G GGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG<br>G G<br>G<br>G<br>−2 0 2 4 −2 0 2 4 −2 0 2 4<br>x x x<br>2 2 2<br>0 0 0<br>y y y<br>−2 −2 −2<br>−4 −4 −4<br><!-- End of picture text -->

**par** (mfrow = **c** (1, 1)) bin <- **hexbin** (x,y) **plot** (bin, main = 'hexbin')

## hexbin


<!-- Start of picture text -->
Counts<br>96<br>2 90<br>84<br>78<br>72<br>66<br>0 60<br>54<br>48<br>43<br>37<br>−2 31<br>25<br>19<br>13<br>7<br>−4 1<br>−2 0 2 4<br>x<br>y<br><!-- End of picture text -->

30

#### **7.4 Colorblindness**

One thing to be aware of is that 7-8% of men are color blind. As we see in the demo code, the standard result of this is to make it difficult to distinguish red and green, so one may want to avoid color schemes that have both of these in them. We can use _dichromat()_ from the _dichromat_ package to assess the effect of colorblindness on viewing of one’s images; see more in the demo code file.

showpal = **function** (colors){ n = **length** (colors); **plot** (1:n, **rep** (1, n), col = **showpal** ( **palette** ())

**showpal** ( **dichromat** (palette))

31

---

[← extract pages from a pdf gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m](03-extract-pages-from-a-pdf-gs--sdevice-pdfwrite--dnopause--dqu.md) · [Up: contents](index.md)
