---
title: Unit 03 — dataIO Part 10 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 10 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More generally, we may want to read an HTML document and parse it into its components (i.e., the HTML elements). Here we use the _XPath_ language in the second argument to _getNodeSet()_ . XPath can also be used for navigating through XML documents.

tutorials <- **htmlParse** ("http://statistics.berkeley.edu/computing/training/tutorials" listOfANodes <- **getNodeSet** (tutorials, "//a[@href]") **head** (listOfANodes) ## [[1]] ## <a href="#navigation" class="element-invisible element-focusable">Jump to ## ## [[2]] ## <a href="/" title="Home" rel="home" id="logo"> ## <img src="http://statistics.berkeley.edu/sites/all/themes/stats/logo.png" ## </a> ## ## [[3]] ## <a href="http://berkeley.edu">University of California, Berkeley</a> ## ## [[4]] ## <a href="/" title="Home" rel="home"> ## <span class="sitename-text">Department of Statistics</span> ## </a> ## ## [[5]] ## <a href="/cas">Log in</a> ## ## [[6]] ## <a href="http://github.com/berkeley-scf/tutorial-unix-basics">materials **sapply** (listOfANodes, xmlGetAttr, "href")[1:10]

13

---

[← [1] "?C=N;O=D" "?C=M;O=A"](09-1-c-n-o-d-c-m-o-a.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 11 — →](11-unit-03-dataio-part-11.md)
