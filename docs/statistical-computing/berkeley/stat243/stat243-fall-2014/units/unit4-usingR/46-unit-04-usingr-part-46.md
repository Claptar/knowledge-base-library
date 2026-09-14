---
title: Unit 04 — usingR Part 46 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 46 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Challenge** : How would I extract an email address from an arbitrary text string?

**Grouping and references** We often want to be able to look for multi-character patterns and to be able to refer back to the patterns that are found. Both are accomplished with parentheses. For example, the phone number detection problem could have been done a bit more compactly (and more generally, in case the area code is omitted or a 1 is included) as:

text <- **c** ("Here's my number: 919-543-3300.", "hi John, good to meet you", "They bought 731 bananas", "Please call 1.919.554.3800", "I think he said it was 337.4355")

**str_extract_all** (text, "(1[-\\.])?([[:digit:]]{3}[-\\.]){1,2}[[:digit:]]{4}")

---

[← [[1]] ## [1] "919-543-3300" ## ## [[2]] ## character(0)](45-1-1-919-543-3300-2-character-0.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 47 — →](47-unit-04-usingr-part-47.md)
