---
title: 3. Graphics file formats
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3. Graphics file formats

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
# convert from pdf to jpeg
gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.pdf

# extract pages from a pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

# merge pdf files into one pdf
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf \
   -dBATCH in1.pdf in2.pdf in3.pdf
```

---

[← 1. Good practices for graphics](01-1-good-practices-for-graphics.md) · [Up: contents](index.md) · [4. Colors →](03-4-colors.md)
