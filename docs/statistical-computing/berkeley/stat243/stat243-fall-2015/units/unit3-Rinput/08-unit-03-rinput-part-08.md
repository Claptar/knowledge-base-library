---
title: Unit 03 — Rinput Part 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 08 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_readHTMLTable()_ works by using _htmlParse()_ and then looking for _<table>_ tags. In the example above, there were multiple tables, so we need to either specify or (after reading all of them) extract the one of interest. There is a related function, _readHTMLList()_ .

It’s often useful to be able to extract the hyperlinks in an HTML document. In this example, I’m not sure why the _relative_ argument (see help(getHTMLLinks)) doesn’t seem to work in terms of giving back absolute paths.

links <- **getHTMLLinks** ("http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year" **head** (links, n = 10)

---

[← Unit 03 — Rinput Part 07 —](07-unit-03-rinput-part-07.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 09 — →](09-unit-03-rinput-part-09.md)
