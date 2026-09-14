---
title: Unit 04 — usingR Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 44 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

What does this match: ^[^[:lower:]]$ ?

**Repetitions** Now suppose I wanted to be able to detect phone numbers, email addresses, etc. I often need to be able to deal with repetitions of character sets.

I can indicate repetitions as indicated in these examples:

- [[:digit:]]* – any number of digits (zero or more)

- [[:digit:]]+ – at least one digit

- [[:digit:]]? – zero or one digits

- [[:digit:]]{1,3} – at least one and no more than three digits

- [[:digit:]]{2,} – two or more digits

An example is that \$$.*\$$ is the pattern of any number of characters ( _.*_ ) separated by square brackets.

So a search for US/Canadian/Caribbean phone numbers might become:

text <- **c** ("Here's my number: 919-543-3300.", "hi John, good to meet you", "They bought 731 bananas", "Please call 919.554.3800") pattern <- "[[:digit:]]{3}[-\\.][[:digit:]]{3}[-\\.][[:digit:]]{4}" **str_extract_all** (text, pattern)

---

[← Unit 04 — usingR Part 43 —](43-unit-04-usingr-part-43.md) · [Up: contents](index.md) · [[[1]] ## [1] "919-543-3300" ## ## [[2]] ## character(0) →](45-1-1-919-543-3300-2-character-0.md)
