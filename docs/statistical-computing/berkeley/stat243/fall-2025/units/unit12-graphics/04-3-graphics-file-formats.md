---
title: 3. Graphics file formats
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Graphics file formats

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Vectorized vs. rasterized file formats

*pdf* images are *vectorized*. What that means is that in general elements of the
image are symbolic objects (such as points, text, symbols, line
segments, etc.) and when an image is resized, the items rescale
appropriately for the new size without losing resolution. In contrast,
with a *rasterized* format such as *jpeg* or *png* or *tiff*, individual pixels are plotted,
and when an image is rescaled, in particular enlarged, one is stuck with
the resolution that one used in plotting the figure (i.e., one has the
original pixels but if you zoom, you only show some of them, losing
resolution).

I strongly recommend using vectorized images in most situations.
That said, one downside to vectorized images is that with a lot of
points or line segments, they can be very large. And for 2-d images, rasterized formats do make some sense inherently,
though the other features in the file (such as any text) is also
rasterized.


## Conversion utilities

UNIX has a lot of utilities for converting between image formats.
Windows and Mac also have GUI-style programs for doing this.

In UNIX, `pdftops` will convert pdf to postscript and with the optional
argument `-eps` to encapsulated postscript, while `ps2epsi` will create
encapsulated postscript. `gs` (Ghostscript) will do a lot of different
manipulations of ps and pdf files, including converting to jpeg and
other formats and merging and splitting pages of pdf files. Here are
some examples of command-line calls from within a UNIX shell:

```bash

---

[← 2. Graphics devices](03-2-graphics-devices.md) · [Up: contents](index.md) · [convert from pdf to jpeg →](05-convert-from-pdf-to-jpeg.md)
