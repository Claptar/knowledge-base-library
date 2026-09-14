---
title: Unit 04 — usingR Part 43 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 43 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Challenge** : how would we find a spam-like pattern with digits or non-letters inside a word? E.g., I want to find "V1agra" or "Fancy repl!c@ted watches".

**Location-specific matches** To find a pattern at the beginning of the string, we use ^ (note this was also used for negation, but in that case occurs only inside square brackets) and to find it at the end we use $.

text <- **c** ("john", "jennifer pierce", "Juan carlos rey") **str_detect** (text, "^[[:upper:]]") _# text starting with upper case letter_

62

---

[← [[1]] ## start end ## ## [[2]] ## start end](42-1-start-end-2-start-end.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 44 — →](44-unit-04-usingr-part-44.md)
