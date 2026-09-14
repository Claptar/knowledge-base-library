---
title: Unit 03 — Rinput Part 12 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 12 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

12

|##|[20]|"/computing/software"|
|---|---|---|
|**sap**|**ply**(|listOfANodes, xmlValue)[1:20]|
|##|[1]|"Jump to navigation"|
|##|[2]|""|
|##|[3]|"University of California, Berkeley"|
|##|[4]|"Department of Statistics"|
|##|[5]|"Log in"|
|##|[6]|"materials on Github"|
|##|[7]|"screencast"|
|##|[8]|"materials on Github"|
|##|[9]|"screencast"|
|##|[10]|"materials on Github"|
|##|[11]|"materials on Github"|
|##|[12]|"materials on Github"|
|##|[13]|"materials on Github"|
|##|[14]|"materials on Github"|
|##|[15]|"screencast"|
|##|[16]|"SCF"|
|##|[17]|"Mission"|
|##|[18]|"Accounts"|
|##|[19]|"Help"|
|##|[20]|"Software"|


The XPath syntax above in getNodeSet() says to find all of the nodes that are named ‘a’ and have attribute _href_ .

Here’s another example of extracting specific components of information from a webpage. We can explore the underlying HTML source in advance of writing our code by looking at the page source (e.g., in Firefox see Developer -> Page Source and in Chrome More tools -> View Source)

doc <- **htmlParse** ("http://www.nytimes.com")

storyDivs <- **getNodeSet** (doc, "//h2[@class = 'story-heading']") **sapply** (storyDivs, xmlValue)[1:5]

---

[← Unit 03 — Rinput Part 11 —](11-unit-03-rinput-part-11.md) · [Up: contents](index.md) · [[1] "Migrant Chaos\nMounts While\nEurope Gropes\nfor a Response" →](13-1-migrant-chaos-nmounts-while-neurope-gropes-nfor-a-response.md)
