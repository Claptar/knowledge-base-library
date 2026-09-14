---
title: '$loanamount ## $loanamount[[1]] ## [1] "100"'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $loanamount ## $loanamount[[1]] ## [1] "100"

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_## alternatively, extract only the 'loans' info (and use pipes)_ loansNode <- doc %>% **xml_nodes** ('loans') loanInfo <- loansNode %>% **xml_children** () %>% **as_list** () **length** (loanInfo)

---

[← Unit 03 — dataIO Part 10 —](10-unit-03-dataio-part-10.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 12 — →](12-unit-03-dataio-part-12.md)
