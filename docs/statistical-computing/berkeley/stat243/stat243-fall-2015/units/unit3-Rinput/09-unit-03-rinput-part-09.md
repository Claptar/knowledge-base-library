---
title: Unit 03 — Rinput Part 09 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 09 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More generally, we may want to read an HTML document and parse it into its components. Here we use the _XPath_ language in the second argument to _getNodeSet()_ . XPath can also be used for navigating through XML documents.

tutors <- **htmlParse** ("http://statistics.berkeley.edu/computing/training/tutorials" listOfANodes <- **getNodeSet** (tutors, "//a[@href]") **head** (listOfANodes)

---

[← Unit 03 — Rinput Part 08 —](08-unit-03-rinput-part-08.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 10 — →](10-unit-03-rinput-part-10.md)
