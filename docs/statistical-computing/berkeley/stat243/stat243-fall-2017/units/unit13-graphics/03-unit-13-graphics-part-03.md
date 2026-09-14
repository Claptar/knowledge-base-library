---
title: Unit 13 — graphics Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit13-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — graphics Part 03 —

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit13-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

|**require**(hexbin,|quietly = TRUE)|
|---|---|
|x <- **rnorm**(10000|); y <- **rnorm**(10000)|
|**par**(mfrow = **c**(1,|3))|
|**plot**(x, y, main|= 'naive')|
|**smoothScatter**(x,|y, main = 'scatterSmooth')|
|**plot**(x, y, col =|**rgb**(0, 0, 0, .1), pch = 16,|
|cex = .5, main|= 'transparency')|


###### **naive scatterSmooth transparency** G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG **G** GGGGGGGG **G** GGGG **G** GGGGG **G** GGGGG **G** GGGGGGGGGGGGGGGGGG **GG** G **GGGG** GG **G** G **G** GGGGG **G** GGGG **G** GGGGGGGGGGGGGGGGGG **GG** G **GG** GGGGGG **GG** GG **G** GGG **G** GGG **G** GG **G** GGGGG **GGG** GG **G** GGGGG **GGG** G **G** GGGGG **G** G **G** G **G** GGGGGG **GG** GGG **G** G **GG** GGG **G** G **G** G **G** G **G** GG **G** GG **G** GGGG **G** GG **G** G **GG** G **G** G **G** GGG **GG** GG **GG** GG **G** G **G** GGG **G** GGG **G** G **G** G **G** GGGGGG **G** GGG **G** G **GGG** G **GG** GGGG **G** G **GG** GGGGGGGGGGGGGGGGGG **G** G **G** G **GG** G **G** GGGG **G** G **G** G **GG** G **G** G **G** GGGGG **G** G **G** G **G** G **G** GGGGG **G** GG **G** GG **G** G **G** GGGG **G** GGG **GGG** GG **GG** G **GGG** GGG **G** GGG **GG** GGGG **GGG** G **G** GG **GG** G **G** G **G** G **GGGG** G **G** GGG **G** G **G** G **G** GG **GG** GG **G** G **GG** G **G** GG **GGGG** G **G** GGG **GG** G **G** GGGGG **GG** G **GG** G **GG** G **GG** G **GG** GG **G** G **GG** GG **G** GGGG **GG** GG **GG** GG **G** GGGGG **G** G **G** G **G** GG **G** GG **GG** G **G** G **GG** GG **G** G **G** GGG **GG** G **G** G **GGG** GGG **G** G **GGGGG** G **GG** GG **G** G **G** G **G** G **GGG** G **GGGG** GGG **G** GGGGG **GGG** G **G** GGG **G** GG **G** GGG **GGG** G **G** GG **G** GGG **G** G **GGG** GG **GGGG** G **G** GGG **GG** G **GGG** G **G** GGG **G** GGGGGG **G** GGG **GGGGG** GG **G** GG **GG** GGG **G** GGGG **GGGG** GG **G** GGGG **GGG** G **G** G **GGGGGG** G **GGGG** GGG **GGG** G **G** G **GG** G **G** GG **G** G **G** G **G** GGG **GG** GG **G** G **GGG** GG **G** GG **G** G **G** G **GGG** G **GG** GGGGG **GG** G **GGG** GG **G** GGG **GG** G **G** GG **G** GGG **G** GGG **GG** G **GG** G **GGG** G **G** GG **GGG** G **GGG** G **GGGGGG** G **GGGG** G **G** GGGG **G** G **G** G **GG** G **GG**<sup>G</sup> G **GGGG** G **G** G **GGGGGGGG** G **G** GGGG **G** GG **G** GGGG **GGG** GGG **G** G **G** G **G** G **G** GGG **GG** GG **G** G **G** G **G** GG **G** GG **GGGGG** G **G** G **G** G **GGGGGG** G **GGGGGGGGGG** GG **GGG** G **GG** GG **G** GGG **GGGG** G **G** G **G** G **GGGGGG** GG **GGGG** G **G** GG **G** G **GG**<sup>**G**</sup> GG **G** G **GG** GG **GGG** G **GGGG** GG **GG** GG **GGGGGGGGGGGGGG** GGGG **GG** G **GG** GG<sup>**G**</sup> **GGGGG** G **GG** G **GG** G **G** GGGG **GGG** GG **GG** G **G** G **GGGGGG** G **GG** G **G** GGG **G** GGG **GGGGG** GGG **G** GG **GGGG** GG **GGGG** GGG **GGG** G **GGGG** GG **GGG** G **GG** G **G** G **GGG** GG **GGGG** G **GGGGG** GGG **G** GG **GGGGG** G **G** GG **G** G **GG** G **GGGG** G<sup>**G**</sup> G **GG** G **GG** GGGGGG **G** G **G** G **GG** G **GGG** G **GGGG** GG **GGGGGGGGG** GG **G** G **GG** G **G** GGG **GGG** G **G** GG **G** GG **GGG** G **GGGG** GGGGGG **G** G **G** G **GGGGGG** G **GG** GGG **GGG** G **G** G **GG** G **GG** G **GGG** G **G** GG **GG** G **GG** G **GGGGG** G **GG** G **GG** GGG **G** G **GG** G **GGGGGGG** G **GGG** GG **G** G **GG** G **GG** G **GGGG** GGGGG **G** G **G** G **GGG** G **G** GGGG **GGGG** G **G** G **G** GG **GG** G **GGGGGGGG** G **G** GG **G** G **GGGGGGGG** G **GG** G **GG** G **GGG** GG **GG** G **GGG** GG **GG** GG **G** G **GG** G **GGG** G **GGGGGG** GG **GGGG** GG **G** GG **GG** GG **GGGGG** G **G** GGG **GGG** GG **G** G **GGGG** GG **G** GG **GG** G **GGG** G **GGGGG** G **GGGGGGGGG** GG **G** GGG **GGGG** G **GGGGGGGG** GG **G** GG **GGGG** GG **GGGGGGGG** G **G** GGG **G** GGGG **G** GG **G**<sup>**G**</sup> GGG **GGGGGGGGGGGGG** G **G** G **GGGGGGGGG** G **G** G **GGGGG** GG **GGGGGG** GGG **G** GGG **GGGG** G **GGGG** G **GG** GG **GGGGGGG** G **GG** G **GG** GG **GGGG** G **GGG** G **G** GG **GG** G **GGGGGG** GGGGG **G** GG **G** G **GGGGGGG** GG **GGGGGGGG** G **GGGG** GG **GGGG** G **GGGGGGGG**<sup>**G**</sup> **GGGGGGGGG** G **GGGG** G **G** G **G** GG **GGGG** G **G** G **GGG** G **GGGGG** G **G** GG **G** GG **G** G **GGGGG** G **GGGGG** G **G** GG **GGG** G **GGG** G **GGGGG** GGGG **GGG**<sup>**G**</sup> **GG** G **GGG** G **G** G **GG** GG **GG**<sup>**G**</sup> G **GGGGGGG** GGG **GGGG** G **GGG** GG **GGG** G **GG** G **GGGGG** GGGGG **GGG** GG **GGG** G **GGGGGGGGGGGGGG** GGG **GGGGG** GG **GGG** GGG **G** GG **GGG** G **G** G **G** G **GG** G **GGG** GG **GGGG** G<sup>G</sup> **GGGGGG** G **GGGG** G **GGGG** G **GG** GG **G** G<sup>**G**</sup> **GGGGG** GG **G** G **GGG** G **G** GG **G** GG **GGGGGG** G **G** G **GG** G **GG** G **G** GG **GG** G **GGGG** G **G** G **G** G **GGG** GGG **GGGG** G **GGGG** G **GGGGG** GG **GGG** G **G** G **GG** GG **GGG** G **GGG** G **GGGGG** G **G** G **GGG** G **G** GGG **GGG** G **G** G **GG** G **G** G **GGG** GG **GG** GG **G** GGGGG **G** GG **G** G **G** G **GG** G **GGGG** GG **GGGGGG** GG **G** G **G** G **GGGG** G **GGGGGGGGGGG** G **G** G **GGG** G **GGGGG** GG **GGGGGGGGGG** G **G** G **GGG** G **GGG** G **GGGGGGGGG** G **GG** G **GGGG** GG **GGGGGGGG** G **GG** G **GGG** G **GGGGG** G **GG** G **GG** G **GGGG** G **GG** G **G** G **GGGGGG** GG **GGG** G **GGG** G **GGGGGGG** G **GGGGGGGGGG** GG **GGG** G **GGGGG**<sup>**G**</sup> **GGGGG** G **GGGG** G **GG** GG **GGGGGGGGG** GG **GGG** G **G** G **GGGGG** G **GGGGGG** GG **GGGGG** GG **GG** G **GG** GGG **GG** G **GGG** G **GGGGGGGGG** G **G** GG **GGG** G **GGGG** G **G** G **G** G **GGGGGGGGG** GG **GG** G **GG** G **GGG** G **G** G **GGGG** GG<sup>**G**</sup> **GGG** G **G** GGGG **GGGGGG** G **GG** GG **GG** G **GGGGGG** G **GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG** GGGG **GGGGGGG** G **GG** GG **GGGGGGGG** G **GG** G **G** G **G** GGG **G** GG **GGG** GG **GGGGGGG**<sup>**G**</sup> **G** GGGGG **GG** G **GGGGGG** G **GGGGG** GGGGGG **GGGGGGGGGGGGGGGGGGG** G **GGGGG** G **GG** G **GGGGGGGGGGGG** G **G** G **G** G **GGG** G **GGG** G **G** G<sup>**G**</sup> G **GGGG** G **G** G **G** G **GGG** G **GGGG** G **GGGG** GG **G** GG **G** G **G** GGG **GG** G **G** G **GG** GG **G** GGG **GGGG** GGG **GGGG** G **GGGGG** G **G** G **GGGGGG** GG **GG** G **G** G **GG** G **G** G **GGGG** G **G** GG<sup>G</sup> **GGG** G **GGGGGGGGGGGGGGG** GGGGGG **G** GGG **GGGGG** GGGG **GGG** G **G** G **GG** G **GG** G **G** GG **G** GGG **GGGGGGG** G **GGGGGGGGG** GG **GGGGG** G **GG** G **GGG** G **G** G **G** G **GGGGG** GGG **GG** G **G** G **GGG** G **G** G **G** G GGGG **G** GGG **GG** GG **GGG** G **GG** G **GG** G **GG** G **GGGGGGG** G **GGG** G **GG** G **GGG** G **G** G **G** G **GGGGGGG** GGG **GG** G **GGG** G **G** G **G** GGGGG **GG** GG **GG** G **GGG** G **GG** G **GG** G **GG** GGG **GG** GG **GG** GGG **G** G **G** G **GG** G **G** GG **GGGGGG** GGG **GGGGGGGGG** GG **G** G **GG** G **G** GG **G** G **G** G **GGGGG** G **G** GG **GGGG** G **GG** GG **GG** G **GGG**<sup>**G**</sup> G **G** G **GGGGGGGGG** G **GGGGGG** G **G** G **GGG** G **GG** G **GG** G **GGGGG**<sup>G</sup> **GGGGG** G **GGG** G **GGGG** GGG **GG** G **G** G **GG** G **GG** GG **GG** G **GGG** G **G** G **G** G **GGGG** GG **GG** GGG **G** G **GGG** G **GG** G **GG** GGG **G** GGG **G** G **GG** G **GGGGG** G **G** GG **G** GG **G** G **G** GG **GGG** G **GG** G **GG** G **GG** G **G** G **GGG** G **G** G **G** G **GG** G **GGGGGGGGGG** G **GG** G **G** G **G** GG **GGGG** G **G** G **GGGG** GG **GGG** GGGGG **G** G **GGGGGGGGG** GGGG **GGG** GG **GGGGG** GGG **GG** G **G** G **G** GGG **GGGG** GG **GG** GG **GGG** G **GG** GG **GG** G **GG** G **GGGG** G **GGG** GGG **GG** G **GG** G **G** GG **G** G **GG** G **G** GGGGGGG **GG** G **GG** G **GGGGGGGGGG** G **GGGGG** G **GG** G **GGGGG** G **GG** GG **GG** G **G** G **GG** GGG **GGGG** G **G** GGG **G** G **G** G **GGG** G **GGGGGGGG** G **G** GG **GGGGGG**<sup>G</sup> **GG** GG **GG** GG **G** G **G** GG **G** GG **G** G **G** GG **GG** G **G** GG **GG** GG **G** GG **G** G **GGG** GG **G** G **G** GGGG **GG** GGGGG **G** GG **GG** GGGG **GGGG** G **G** G **GG** GG **GGG** G **GGGGGGG** GGG **G**<sup>G</sup> G **GGGG** GG **G** G **G** GG **GGGGG** G **GG** G **G** GGG **G** G **G** GGGG **GG** GG **GGG** G **GGG** GGGGGG **GGGG** G **GGGG** G<sup>**G**</sup> G **G** G **GG** G **GG** G **G** GG **GGG** GGGGG **G** G **G** G<sup>G</sup> **GGG** G **G** GG **GGG** G **GG** G **G** GG **G** GGGG **GG** GGGG **G** G **G** G **G** G **G** GG **GG** G **G** G **G** G **GG** G **G** G **GG** GGGG **G** G **G** GG **GGG** GG **GG** G **G** G **GGGG** GGG **G** G **GGG** G **G** G **GGG** GG **G** GGG **GG** G **GGG** G **G** G **G** GGGGG **G** G **G** GGGG **GG** GGG **G** G **GGGG** GG **G** GGGG **GG** GG **G** G **G** G **G** G **GG** GG **GGG** G **G** GG **GGG** G **GGG** GG **G** GG **GG** GG **GGG** G<sup>G</sup> G **GGG** GG **G** GGGG<sup>G</sup> GGGG **GG** GGGGG **GGG** G **G** GG **GGG** GGGGG **G** GG **G** GG **GGG** G **G** G **G** G **GG** GGG **G** GGGGG **GGGG** GGGG **GGG** G **G** G **GG** GGG **G** GGGGG **G** GG **G** GGG **GG** G **GG** G **GGG** G **G** G **G** GGGGG **G** GGG **G** G **G** GGGG **GGG** G **G** GGGG **GG** G **G** G **G** G **G** GGG **G** GGGGGGGGGGGG **G** G **G** G **G** GGG **G** GGGGGGGG **G** G **G** GGGGGGG **G** GG **G** GG **G** G **G** G **G** GG **G** G **GG** GGGGGG **G** G **G** GGGG **G** GGGGGG **G** GGG **G** GGGG **G** GGGGG **G** GGGGGGGGGGGG **G** GGG **G** GGGGGGGG **G** GGGGGGG **G** G **G** GGGGGGGGGGG **GGG** GGGGGGGGGG **G** GGGGGGG<sup>G</sup> GGGGGGGGGGGGGGGGGGGGGG **G** GGGGGGGGGGGGGG **G** GGGGG **G** GGGGGGGGGGGGGGGGGGGGG G G G G G −4 −2 0 2 4 −4 −2 0 2 4 −4 −2 0 2 4 x x x

|**par**(mfrow = **c**(1, 1))|
|---|
|bin <- **hexbin**(x,y)|
|**plot**(bin, main = 'hexbin')|


34


<!-- Start of picture text -->
hexbin<br>4 Counts<br>111<br>104<br>2 97<br>90<br>84<br>77<br>0 70<br>63<br>56<br>49<br>42<br>−2 35<br>28<br>22<br>15<br>8<br>−4 1<br>−4 −2 0 2 4<br>x<br>y<br><!-- End of picture text -->

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
