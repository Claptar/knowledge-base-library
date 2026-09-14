---
title: 2. Graphics devices
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Graphics devices

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Graphics are plotted on a *device*. In the old days when computer
monitors were not high resolution or in color, this referred to a
physical device, but nowadays this is a general term that denotes the
context in which the plot is being made: typically on screen or as a
file in a particular file format. The standard device in a UNIX
environment is X11, basically a graphics window set up in the X11
windowing system. On-screen plotting is generally done with the software
you are using (e.g., Python or R)
interacting with a window manager for the operating system.

Often one needs to
iterate to get a plot to look good when printed to a file; in particular
the aspect (width to height ratio), the margin sizes relative to the size of the core
plot, and size of plotting symbols and text relative to the size of the
plot. In other words, the relative sizes when seen in a graphics window on the
screen may be very different when printed to a file.

---

[← 1. Good practices for graphics](02-1-good-practices-for-graphics.md) · [Up: contents](index.md) · [3. Graphics file formats →](04-3-graphics-file-formats.md)
