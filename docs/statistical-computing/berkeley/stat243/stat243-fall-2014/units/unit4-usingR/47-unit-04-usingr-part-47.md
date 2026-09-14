---
title: Unit 04 — usingR Part 47 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 47 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

64

_## matches <- ## gregexpr('(1[-\\.])?([[:digit:]]{3}[-\\.]){1,2}[[:digit:]]{4}', ## text) ## regmatches(text, matches)_

Parentheses are also used with a pipe (|) to indicate any one of a set of multi-character sequences, such as (http|ftp).

text <- **c** ("at the site http://www.ibm.com", "other text", "ftp://ibm.com") **str_locate** (text, "(http|ftp):\\/\\/") ## start end ## [1,] 13 19 ## [2,] NA NA ## [3,] 1 6 _## gregexpr('(http|ftp):\\/\\/', text)_

It’s often helpful to be able to save a pattern as a variable and refer back to it. Here’s an example that might have been helpful in dealing with the extra commas in the comma-delimited FEC elections data file in PS1:

text <- ("\"H4NY07011\",\"ACKERMAN, GARY L.\",\"H\",\"$13,242\",,,") **str_replace_all** (text, "([^\",]),", "\\1")

---

[← Unit 04 — usingR Part 46 —](46-unit-04-usingr-part-46.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 48 — →](48-unit-04-usingr-part-48.md)
