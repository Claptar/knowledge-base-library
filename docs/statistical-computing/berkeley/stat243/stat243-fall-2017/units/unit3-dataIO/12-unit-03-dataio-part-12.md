---
title: Unit 03 — dataIO Part 12 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 12 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The XPath syntax above in getNodeSet() says to find all of the nodes (i.e., elements) that are named ‘a’ and have attribute _href_ .

Here’s another example of extracting specific components of information from a webpage. We can explore the underlying HTML source in advance of writing our code by looking at the page source (e.g., in Firefox see Developer -> Page Source and in Chrome More tools -> View Source)

doc <- **htmlParse** ( **readLines** ("https://www.nytimes.com")) storyDivs <- **getNodeSet** (doc, "//h2[@class = 'story-heading']") **sapply** (storyDivs, xmlValue)[1:5]

---

[← Unit 03 — dataIO Part 11 —](11-unit-03-dataio-part-11.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 13 — →](13-unit-03-dataio-part-13.md)
