---
title: Unit 03 — dataIO Part 22 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 22 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

With strings already in R, you can convert between encodings with _iconv()_ :

text <- "_Melhore sua seguran\xe7a_" **Encoding** (text) ## [1] "unknown" **Encoding** (text) <- "latin1" text ## [1] "_Melhore sua segurança_" text <- "_Melhore sua seguran\xe7a_" textUTF8 <- **iconv** (text, from = "latin1", to = "UTF-8") **Encoding** (textUTF8)

33

---

[← 5 File and string encodings](21-5-file-and-string-encodings.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 23 — →](23-unit-03-dataio-part-23.md)
