---
title: Slides
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/31-interference-1/slides.html
source_file: sources/berkeley-stat158/spring-2026/31-interference-1/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Slides

**Source:** [`31-interference-1/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/31-interference-1/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# Interference {#interference .title}

## Study: School Attendance

A school district in a large city wants to boost student attendance rates. They identify 20,000 households, each containing exactly two enrolled students. In 10,000 randomly-chosen households, the parents receive no mail. In the remaining 10,000 households, the parents receive a letter about one of their two children, chosen at random. Attendance rates are then measured for the remainder of the school year for all children.

> Measurement unit? Experimental Unit? Response? Factors? Design?

## Study: School Attendance

- Measurement unit: student
- Experimental unit: student and household
- Response: attendance rate
- Experimental factor: mail (yes/no)
- Design: Mix of *cluster* design (household is cluster) and *CB* (block is household).

> This *multistage design* is specifically constructed to handle interference.

##

**Question**: How many potential outcomes are needed to represent this design?

> 3: <span class="math inline">\$Y\_{ij}(1, 0), Y\_{ij}(0, 1), Y\_{ij}(0, 0)\$</span>

---

[Up: contents](../index.md)
