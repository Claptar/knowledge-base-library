---
title: Unit 13 — graphics Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit13-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — graphics Part 03 —

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit13-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

|**naive**|
|---|


|**scatterSmooth**|
|---|


###### **transparency**

###### GG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG **GG** GGGGGGGGGGGGGGGGGGGGGG **G** GGGGGGG **G** GGGG **G** GGGGGGGGGGGGG **G** GGGGGGGGGGGGGGGGGGG **G** G **G** GGGG **G** GGGGGGGG **G** GG **GGG** GGGGGGGGGGGGGG **G** GGG **G** G **G** GGGGGG **G** GGGGGG **G** GGGG **GGG** G **G** G **G** GGGGGGG **G** GGGG **GGG** GG **G** GGGG **GG** GGGGGGGG **GGG** GG **G** GGGGG **G** GGGGGGG **G** GGG **G** G **G** GG **G** G **G** GG **G** GGG **G** G **G** GGGG **GG** GGGG **GG** GGGGGGGGGGGGG **GG** GGGG **G** GGGGGG **G** G **G** GGG **G** GGG **GG** GGG **G** GG **G** GGGG **G** GG **G** GG **G** GGGGGGGGG **GG** GGG **GG** GG **G** G **G** G **GGGGG** GG **G** G **GG** G **G** G **G** GGG **G** G **G** GGGG **GG** GG **GGG** GGGGG **GG** GG **GG** G **G** GGGGGGG **G** GG **G** GG **G** GGG **GG** GGGG **G** G **G** G **G** G **GGGG** G **G** GG **G** GGG **GG** G **G** G **GGG** GGG **GG** G **G** GGGGGGG **G** GGG **G** G **GGG** G **GG** G **G** GGGG **GGG** GGG **GG** GGGGG **GG** GGG **GG** GG **G** G **G** G **GG** GGGG **G** GGGGGGG **G** GGG **GG** GGG **GG** GGGGG **G** G **GGGG** G **GGG** GGG **GGG** GG **G** G **GG** GGG **GG** GG **G** G **G** G **G** G **GG** GG **GG** G **G** GGG **G** G **GG** GGG **GG** G **G** GGG **G** GGGG **G** GG **GG** G **GG** GGG **GGG** GGGG **G** G **G** G **GG** G **GGGG** G **GGGG** GG **G** G **GG** G **G** GG **GGG** GG **GGGG** G **G** GGGG **GGGGG** G **G** G **G** G **G** GGGGGGG **G** GGGG **GG** GG **G** GG **G** G **G** G **G** G **G** G **G** G **G** GGG **GG** GG **GG** G **GG** GGGGG **GG** GG **G** GG **GGGGGG** G **G** G **GGGGGG** G **GGGGGG** GG **GGGGGG** G **G** G **GG** GG **GG** GG **G** GG **G** G **G** GGGGGGG **GGGGGGG** G **GGGGG** G **G** GGG **GGGG** G **G** GG **GG** G **GG** G **G** G **GG**<sup>G</sup> G **GGGGGGGG** GGG **G** GGGGG **G** GGGG **GG** GG **GG** GG **GG** GGG **G** GGG **GGGG** GGG **GGGGG** GGG **GGG** GG **GGGG** G **GG** G **G** GG **G** G **G** G **GGG** G **GG** G **G** GGGGG **GG** G **G** G **GG** G **G** GGG **GG** G **GG** GG **G** G **GGGGGG** GG **GGG** G **G** GGGG **G** G **GGG** GGG **GGGGGG**<sup>**G**</sup> G **GG** GG **GGG**<sup>**G**</sup> **GGGG** G **G** G **G** G **GG** GG **G** GGGG **GG** GG **G** G **G** GG **GG** G **GGGGGG** GG **GGG** G **GGG** GGG **GGG** GG **GG** G **GGG** GG **GGGG** G **GGGG** G **GGGGGGGG** GGGGG **GGGGGG** G **G** G **GG** GG **GGGGGGGG** G **G** G **GG** GGG **GG** G **G** GG **G** G **GGGG** G **GG** G **G** GG **GGG** GG **G** GG **GGGGG** G **G** G **G** G **GGGG** GG **G** G **GGGGGG** GGG **GGGGGGGG** G **GGGGG** G **GG** G **GG** G **G** GG **G** GG **GG** G **GGGGGG** G **GGG** G **G** GGG **GG** GG **GG** GG **GG** G **GG** G **GGGGGG** G **GGG** GGGGGG **GGG** G **G** G **GGGGGGG** G **GGG** GGG **GG** G **GG** G **G** G **GGGGG**<sup>**G**</sup> **GGG** G **GGGGGG** GG **GG** GGG **G** G **GGGGG** GG **GGG** GG **G** G **GG** G **G** G **GGG** G **G** G **GGG** GGG **G** GG **GG** GG **G** G **GG** G **G** G **GGG** G **GG** GG **GGGGGG** GG **G** GG **GGGGGGG** GG **GG** G **GGG** G **G** GG **GG** G **GGG** G **GG** G **G** G **G** G **GG** G **GG** GG **GG** G **GGGG** G **G** G **G** G **GG** G **GGGG** GGGG **GGGG** G **GG** G **GGG** G **G** GG **G** G **G** GG **G** GGGG **GGG** G **G** GG **GG** G **G** G **G** G **G** G **GG** G **G** GG **GGGGG** GG **GG** G **GGG** G **GGGG** G **GG** G **G** G **GGG** G **G** G **G** G **GGGGGGGG** G **GG** G **G** G **GG** G **GGGG** GGG **GGG** GGGGGG **GGGG** GG **GGGGG** GGG **G** G **GGGGG** G **G** G **GGGGGG** G **GG** G **G** G **G** GG **GG** GG **GGGGG** GG **GGGG** G **GGGG** G **GGGG** GG **G** G **G** GGG **GG** G **G** G **GGG** G **GGGGGGG**<sup>**G**</sup> G **GGG** GGG **GGGG** G **GGGG** G **GGG** G **G** GGG **G** GG **G** G **GGGGGGGG** G **G** G **G** GGGG **GGGG** G **GGGG** G **G** G **GGG** G **G** GG **GGGG** GGG **G** G **G** G **GGG** GG **GG** GG **G** G **GGGGGG** G **GG** G **G** GG **G** G **G**<sup>**G**</sup> **G** G **G** G **GG** GGGGG **GG** G **GGG** GG **GG** G **GGGGGG** G **GG** GG **G** G<sup>**G**</sup> **GGG** G **GGGGG** G **GG** G **GGGGGGG** G **GGGGGG** G **GGGGG** GG **GG** G **GG** G **G** G **G**<sup>**G**</sup> **G** G **GGGG** GG **GGGGGGGGGGG** G **G** G **GG** G **G** GGGGGGG **G**<sup>**G**</sup> **G** G<sup>**G**</sup> GGG **G** G **GGGG** G **GG** G **GGGGG** G **GGG** GG **GG** G **GGGGGGGG** GG **GGG** G **GGGGG** G **G** G **GG** G **GGG** GG **GGGGGGG** G **GG** G **GGG** G **GG** GG **GG** G **G** G **G** G **GG** GG **GGG** G **GGGGG** GG **GGGGGGG** G **GG** G **G** G **G** G **GG** GGG **GGGG** GG **GG** G **GGGGGGGGGG** G **GG** G **G** G **GGG** G **GGGGGG** G **GG** G **GGG** GG **GGGG** G **GG** G **G** G **GG** GG **GGG** G **GGG** G **G** GG **GG** G **GGG** G **GGGGGGGG** GG **GGG** GGG **GGGGGG** G **GGGGG** GG **G** G **GGGG** G **G** G **GG** G **GGGG** G **G** GG **G** GGG **GG** G **GGGGG** GG **GGGGG**<sup>**G**</sup> **GG** GG **GGGGGGGGGGGG** GG **GGGGGG** GG **GGGGGGG** G **GGG** GG **GGG** G **GGGGG** G **GG** GGG **G** G **G** GGG **G** G **GG** G **GGG** G **GGGGGGG**<sup>**G**</sup> **G** G **GG** GGG **GG** G **G** GG **GG** G **GG** GGGGGG **GG**<sup>G</sup> **G** GGG **G** G **GG** GG **G** G **G** G **G** G **GGGG** G **GGG** G **GGGGG** G **G** G **GGG** G **GG** GG **GGGG**<sup>**G**</sup> GGG **G** GG **GG** G **G** GGG **GGGGG** G **GGGGG** G **GGGGGGGGG** G **G** GG **GG** G **GGGG** GGG **GGG** G **G** G **GGGGGGGGG** G **GG** GG **GGGGGG** G **G** G **GG** GGG **GGGGGGGGGGGG** GG **GG** GG **GG** G **GGGGGG** G **GGGGGGGGG** GG **GGG** GGG **GG** G **GGGGGGGG** G **GGGGGGGGGGGGG** GG **GG** G **GG** GGG **GGGGGG** G **GGGGGG** G **G** GG **G** GG **G** G **GGG** G **GGGGG** GG **G** G **GG** G **GG** G **GGGGGGG** G **G** GGGGGG **GGGGG** G **GGGGGGGGG** GG **G** G **G** G **GGGG** G **GGGGG** G **GG** GGG **GGGGGG** G **GGGG** GG **G** GG **GGGGGG** G **GGGG** GGG **G** G **GGG** G **GG** G **G** G **GGGGG** G **GGGGGG** G **GGGGGGGG** GGGG **G** G **G** G **GGG** G **GG** GG **G** G **G** G **G** G **G** G **GGGGG** G **GGG** GG **G** GG **GGGG** G **GGGGG** G **G** GGGG **GG** G **GGGG** G **GGG** G **GGGGGGGGGGGG** GGG **GGG** GGG **GG** G **GGGGGGG** G **G** G **GG** GGG **GGGGGGGGGG** G **GGGGG** G **G** G **GGG** G **GGG** GGG **GG** G **GGG** GGG **GG** G **GGG** G **GGGG** G **GGG** G **GGG** GGGG<sup>**G**</sup> **G** G **GG** G **G** GGG **G** GG **G** GG **GG** G **G** G **GG** G **G** G **G** GG **GGG** G **GG** G **G** G **G** G **GG** G **GG** G **G** GGG **GG** G **GGGG** GG **GGGG** GGGG **GG** G **GG** G **GG** G **G** GGGGG **G**<sup>**G**</sup> G **G** G **G** GG **G** G **GG** G **G** G **GG** GGG **GG** G **GGGGGGG** G **G** GGGGGGGG **GGGGGGGG** GGG **GG** G **G** G **G** G **GGGG** G **GG** G **G** GGGG **GGGGGG** G **G** G **GGG** GGG **GGGGGG** G **GGGGG** G **G** G **GG** G **GGGGGGGG** G **GGGGGG** GG **GGGGGGGGGG** G **GGG** GG **GG** GG **GG** G **GG** GG **G** G **GGGGG** G **G**<sup>**G**</sup> **G** G **GG** GG **GG** GG **G** G **G** GG **GGGG** GG **G** GGG **GGG** G **G** GG **GGGG** GGGG **GGGG** G **G** G **GGG** GGGG **G** GG **G** G **GGG** G **GGG** G **GGGGGGGGGGGGG** GG **GGGGGGGGGG** GG **G** GGG **GGGGG** GG **G** G **G** G **GGG** GGG **GGGGGGGGGGG** G **GGGGG** GGGG **G** G **GGGG** G **GG** GG **GG** G **G** G **GGG** GGG **G** G **G** G **GGGG** G **G** GGG **GGGGGG** G **GG** GG **G** GG **GGG** G **GG**<sup>**G**</sup> **GG** G **G** GGG **GGG** G **G** G **GGGG** GG **G** GGG **G** G **G**<sup>**G**</sup> G **G** G **G** G **GGG** GGG **GGGGGGGGG** G **GG** GG **G** G **G** GG **GG** GGG **GGGGG** GG **G** GG **G** G **GGG** G **G** GGGG **GGG** G **G** G **GGG** GGG **G** G **G** GG **G** GG **GG** G **G** GG **GGGGG** G **GG** G **G** GG **G** G **GG** G **GGGG** G **G** GG **GGGGG** G **GGGGG** G **G** G **GG** G **GG** G **G** G **G** G<sup>G</sup> **G** GG **G** GGG **G** G **G** G **G** GGG **G** GGG **GGGG** G **G** G **GGG** G **G** G **G** GG **G** G **G** GG **GGG** G **GG** G **G** G **G** G<sup>**G**</sup> G **GGG** G **G** G **GG** G **GG** G **G** GGG **GG** G **G**<sup>**G**</sup> G **GGGGGGG** G **GGGGGGGGGGGGG**<sup>G</sup> **G** G **GG** GG **G** GG **GGG** G **G** G **G** GGG **G** G **G** GG **GG** G **G** G **GGGG** GGGGG **GGGG** G **GG** G **GG** GGGG **G** G **GG** GGG **G** GGG **G** GGGG **G** G **GG** GGG **G** G **GG** G **G** G **G** G **GG** G **G** GG **GG** GG **GG** G **G** G **G** G **GG** GG **GGG** GGG **GGGG** GG **G** G<sup>**G**</sup> **GGGGGGGG** GG **GGGGGGGG** G **G** G **GGG** GG **GG** G **GGGG** GGGG **GGG** GGGGG **G** G **G** G **G**<sup>**G**</sup> **GGG** GGG **GGG** G **GGGGG** G **G** G **GGGG** GG **G** GG **G** GG **GGGGGGGGGGG** GG **GG** GGG **GGGG** GGGGG **G** GGG **G** GGGGG **G** G **GGG** GGG **GGGGG** GGG **G** GGG **GGG** GGG **GG** GGGG **G** G **G** GG **G** GGGGG **GGG** G **GG** G **GG** G **GGGG** G **GG** G **G** G **G** GGGGG **GG** GGG **G** G **GGG** GG **G** G **GGGGG** G **G** G **GG** GG **G** GGG **G** GGG **GG** GG **GG** GG **GGGGG** GGGG **GG** GGG **G** G **G** G **G** GGG **G** GGGGGGGGGG **G** GG<sup>G</sup> **G** G **G** G **G** GGGGG **GG** G **GGGGGGGG**<sup>**G**</sup> G **GGG** GG **G** GGG **G** GG **GGG** GGGG **GG** G **GG** G **GGG** GGG **G** GG **G** GGGGG **G** GG **G** G **G** GG **G** GG **G** GGG **GG** GGG **GG** GG **G** G **G** G **GGGGG** G **G** G **G** GGGG **GG** GGG **G** GGGG **G** G **GG** G **GGG** GG **G** G **GG** GGGG **G** GG **G** G **GG** G **GGG**<sup>G</sup> GG **GGG** G **GG** G **G** G **G** GGGGG **GG** G **G** GG **G** GGG **GG** G **GG** GG **G** GGGGGGGGGGGGGGGG **G** GGG **G** G **G** GGGGGGGGGG **G** G **G** GG **G** GGG **GG** G **G** GGG **G** GG **G** GGGGGGGG **G** GGGGGG **G** GGG **G** G **G**<sup>**G**</sup> GGGG **G** GGGGGG<sup>G</sup> GGG **G** GGGGG **G** GGGGGGG **G** GGGGGGGG **G** GGGGGG **G** GGGGGGG **G** GG **G** GGG **G** GGG **G** GGGGGGGGGGGG **G** GGGGGGGGGGGGGGGGGGGGGGGGGGGGG **G** GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GG −4 −2 0 2 −4 −2 0 2 x x

|−3<br>−2<br>−1<br>0<br>1<br>2<br>3<br>y|||
|---|---|---|
||−4|−2<br>0<br>2<br>x|


|**par**(mfrow = **c**(1, 1))|
|---|
|bin <- **hexbin**(x,y)|
|**plot**(bin, main = 'hexbin')|


35


<!-- Start of picture text -->
hexbin<br>4<br>Counts<br>96<br>90<br>2 84<br>78<br>72<br>66<br>60<br>0 54<br>48<br>43<br>37<br>31<br>−2 25<br>19<br>13<br>7<br>1<br>−4 −2 0 2<br>x<br>y<br><!-- End of picture text -->

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
