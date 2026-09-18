---
title: Introduction
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

```python
#| echo: false
import re, os, sys, time, math
## As of 2024-09-15, I need to use the python/3.11 module to render,
## because of possible bug with libjpeg when using reticulate
## with matplotlib via knitr engine. I want to use knitr
## so that code output is interspersed with code in a chunk.
## But test run in 3.12 first so that can catch any 3.11->3.12 changes.
## Also, I have R chunks and bash chunks (though the latter might be handled with `!`
## if using jupyter.
```

[PDF](index.md){.btn .btn-dark}

!!! note "Note"
2024-10-05: There will be miminal further edits on this unit.
:::

## Overview

This unit covers a variety of programming concepts, illustrated in the
context of Python and with comments about and connections to other languages. It also serves as a way to teach some advanced features of
Python. In general the concepts are relevant in other languages, though other
languages may implement things differently. One of my goals for the unit is for us
to think about why things are the way they are in Python. I.e., what
principles were used in creating the language and what choices were
made? While other languages use different principles and made different
choices, understanding what one language does in detail will be helpful when you
are learning another language or choosing a language for a project.

!!! note "Note"
This document  uses the `knitr` engine for rendering to be able to run chunks in multiple languages (Python and bash, as well as a few R chunks. It has the Quarto configuration `ipynb-shell-interactivity: all`, so that output from all Python code in a chunk will print in the rendered document; when done with the `knitr` engine, the output is interspersed with the code in the chunk rather than printed all at the end.
:::

---

[Up: contents](index.md) · [1. Text manipulation, string processing and regular expressions (regex) →](02-1-text-manipulation-string-processing-and-regular-expression.md)
