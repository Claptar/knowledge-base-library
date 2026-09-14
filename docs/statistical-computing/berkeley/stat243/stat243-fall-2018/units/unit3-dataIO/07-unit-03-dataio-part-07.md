---
title: Unit 03 — dataIO Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 07 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More generally, we may want to read an HTML document, parse it into its components (i.e., the HTML elements), and navigate through the tree structure of the HTML. Here we use the _XPath_ language to specify elements rather than CSS selectors. XPath can also be used for navigating through XML documents.

12

_## find all 'a' nodes that have attribute href; then ## extract the 'href' attribute_ links <- **read_html** (URL) %>% **html_nodes** (xpath = "//a[@href]") %>% **html_attr** ('href') **head** (links) ## [1] "?C=N;O=D" "?C=M;O=A" ## [3] "?C=S;O=A" "?C=D;O=A" ## [5] "/pub/data/ghcn/daily/" "1763.csv.gz" _## we can extract various information_ listOfANodes <- **read_html** (URL) %>% **html_nodes** (xpath = "//a[@href]") listOfANodes %>% **html_attr** ('href') %>% **head** (n = 10)

---

[← Unit 03 — dataIO Part 06 —](06-unit-03-dataio-part-06.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 08 — →](08-unit-03-dataio-part-08.md)
