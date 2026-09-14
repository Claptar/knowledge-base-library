---
title: 3. Graphics file formats
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit12-graphics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Graphics file formats

**Source:** [`units/unit12-graphics.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The `pdf()` function is a workhorse for creating an output file
containing your R graphics. Analogues of `pdf()` include `jpeg()`,
`png()`, `tiff()`, and `postscript()`. If you have already made the
plot in the graphics window and want to export it, you can use
`dev.copy2pdf()`, though in some cases the graphic has been optimized
for the computer screen window and won't display nicely in the resulting file.

## Vectorized vs. rasterized file formats

pdf and postscript images are *vectorized*. What that means is that in general elements of the
image are symbolic objects (such as points, text, symbols, line
segments, etc.) and when an image is resized, the items rescale
appropriately for the new size without losing resolution. In contrast,
with a *rasterized* format such as JPEG, individual pixels are plotted,
and when an image is rescaled, in particular enlarged, one is stuck with
the resolution that one used in plotting the figure (i.e., one has the
original pixels but if you zoom, you only show some of them, losing
resolution).

I strongly recommend using vectorized images in most situations.
That said, one downside to vectorized images is that with a lot of
points or line segments, they can be very large. And for 2-d images such as
created by `image()`, rasterized formats do make some sense inherently,
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
