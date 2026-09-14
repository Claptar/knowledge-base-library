---
title: Unit 04 — usingR Part 48 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 48 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can have multiple sets of parentheses, referred to using \\1, \\2, etc. **Challenge** : Suppose a text string has dates in the form “Aug-3”, “May-9”, etc. and I want them in the form “3 Aug”, “9 May”, etc. How would I do this search/replace?

**Greedy matching** It turns out the pattern matching is ’greedy’ - it looks for the longest match possible.

Suppose we want to strip out html tags as follows:

65

text <- "Do an internship <b> in place </b> of <b> one </b> course." **str_replace_all** (text, "<.*>", "")

---

[← Unit 04 — usingR Part 47 —](47-unit-04-usingr-part-47.md) · [Up: contents](index.md) · [[1] "Do an internship course." ## gsub('<.>', '', text) →](49-1-do-an-internship-course-gsub-text.md)
