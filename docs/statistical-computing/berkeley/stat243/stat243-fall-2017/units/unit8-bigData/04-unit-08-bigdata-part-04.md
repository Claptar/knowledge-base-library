---
title: Unit 08 — bigData Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 04 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s how to make a basic SQL query. One can either make the query and get the results in one go or make the query and separately fetch the results. Here we’ve selected the first five rows (and all columns, based on the * wildcard) and brought them into R as a data frame.

results <- **dbGetQuery** (db, 'select * from questions limit 5') **class** (results)

---

[← 2 Databases](03-2-databases.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 05 — →](05-unit-08-bigdata-part-05.md)
