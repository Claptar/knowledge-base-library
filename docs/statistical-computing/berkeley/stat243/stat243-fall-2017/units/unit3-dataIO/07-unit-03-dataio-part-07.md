---
title: Unit 03 — dataIO Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 07 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_readHTMLTable()_ works by using _htmlParse()_ and then looking for _<table>_ tags. In the example above, there were multiple tables, so we need to either specify or (after reading all of them) extract the one of interest. There is a related function, _readHTMLList()_ .

It’s often useful to be able to extract the hyperlinks in an HTML document. In this example, I’m not sure why the _relative_ argument (see help(getHTMLLinks)) doesn’t seem to work in terms of giving back absolute paths.

URL <- "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year" html <- **readLines** (URL)

links <- **getHTMLLinks** (html) **head** (links, n = 10)

---

[← 3 Webscraping and working with XML and JSON](06-3-webscraping-and-working-with-xml-and-json.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 08 — →](08-unit-03-dataio-part-08.md)
