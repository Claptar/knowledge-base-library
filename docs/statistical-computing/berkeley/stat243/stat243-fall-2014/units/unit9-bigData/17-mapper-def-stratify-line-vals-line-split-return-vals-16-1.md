---
title: 'mapper def stratify(line): vals = line.split('','') return(vals[16], 1)'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# mapper def stratify(line): vals = line.split(',') return(vals[16], 1)

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

result = lines.map(stratify).reduceByKey(add).collect() # reducer is simply the addition function

29

---

[← Unit 09 — bigData Part 16 —](16-unit-09-bigdata-part-16.md) · [Up: contents](index.md) · [Unit 09 — bigData Part 18 — →](18-unit-09-bigdata-part-18.md)
