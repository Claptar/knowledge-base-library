---
title: Unit 03 — dataIO Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 06 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_read_html()_ works by reading in the HTML as text and then parsing it to build up a tree containing the HTML elements. Then _html_nodes()_ finds the HTML tables and _html_table()_ converts them to data frames. rvest is part of the tidyverse, so it’s often used with piping, e.g.,

**library** (magrittr) tbls <- URL %>% **read_html** ("table") %>% **html_table** ()

It’s often useful to be able to extract the hyperlinks in an HTML document. We’ll find the link using CSS selectors, which allow you to search for elements within HTML:

URL <- "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year" _## approach 1: search for elements with href attribute_ links <- **read_html** (URL) %>% **html_nodes** ("[href]") %>% **html_attr** ('href') _## approach 2: search for HTML 'a' tags_

links <- **read_html** (URL) %>% **html_nodes** ("a") %>% **html_attr** ('href') **head** (links, n = 10)

---

[← 3 Webscraping and working with XML and JSON](05-3-webscraping-and-working-with-xml-and-json.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 07 — →](07-unit-03-dataio-part-07.md)
