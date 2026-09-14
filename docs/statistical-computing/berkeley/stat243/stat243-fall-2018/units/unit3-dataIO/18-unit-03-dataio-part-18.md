---
title: Unit 03 — dataIO Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 18 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

With strings already in R, you can convert between encodings with _iconv()_ :

text <- "_Melhore sua seguran\xe7a_" **Encoding** (text) ## [1] "unknown" **Encoding** (text) <- "latin1" text ## [1] "_Melhore sua segurança_" text <- "_Melhore sua seguran\xe7a_" textUTF8 <- **iconv** (text, from = "latin1", to = "UTF-8") **Encoding** (textUTF8) ## [1] "UTF-8" textUTF8 ## [1] "_Melhore sua segurança_" **iconv** (text, from = "latin1", to = "ASCII", sub = "???") ## [1] "_Melhore sua seguran???a_"

You can also mark a string with an encoding, so R knows how to display it correctly:

x <- "fa\xE7ile" **Encoding** (x) <- "latin1" x ## [1] "façile"

34

_## playing around..._ x <- "\xa1 \xa2 \xa3 \xf1 \xf2" **Encoding** (x) <- "latin1" x

---

[← 5 File and string encodings](17-5-file-and-string-encodings.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 19 — →](19-unit-03-dataio-part-19.md)
