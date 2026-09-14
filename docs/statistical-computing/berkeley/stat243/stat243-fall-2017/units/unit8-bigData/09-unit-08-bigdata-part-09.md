---
title: Unit 08 — bigData Part 09 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 09 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

16

|## 14|swift|61485|
|---|---|---|
|## 15|sql|58346|
|## 16|node.js|52827|
|## 17|r|48079|
|## 18|arrays|46739|
|## 19|json|45250|
|## 20|ruby-on-rails|39036|
|## 21|sql-server|37077|
|## 22|c|36080|
|## 23|asp.net|35610|
|## 24|excel|29924|
|## 25|angular2|28832|


In general ‘GROUP BY‘ statements will involve some aggregation operation on the subsets. Options include: COUNT, MIN, MAX, AVG, SUM.

**Challenge** : Write a query that will count the number of answers for each question, returning the most answered questions.

### **2.9 Getting unique results (DISTINCT)**

A useful SQL keyword is DISTINCT, which allows you to eliminate duplicate rows from any table (or remove duplicate values when one only has a single column or set of values).

tagNames <- **dbGetQuery** (db, "select distinct tag from questions_tags") **head** (tagNames)

---

[← [1] TRUE](08-1-true.md) · [Up: contents](index.md) · [tag ## 1 c# ## 2 razor ## 3 flags ## 4 javascript ## 5 rxjs ## 6 node.js →](10-tag-1-c-2-razor-3-flags-4-javascript-5-rxjs-6-node-js.md)
