---
title: Algorithms for Adaptive Assignment
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/29-adaptive-algorithms/slides.html
source_file: sources/berkeley-stat158/spring-2026/29-adaptive-algorithms/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Algorithms for Adaptive Assignment

**Source:** [`29-adaptive-algorithms/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/29-adaptive-algorithms/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# Regret

##

<span class="math display">\\$$ \\begin{array}{c\|c\|c} \\text{Patient} & Y\_i(A) & Y\_i(B) \\\\ \\hline 1 & 1 & 0 \\\\ 2 & 1 & 0 \\\\ 3 & 1 & 1 \\\\ 4 & 0 & 0 \\\\ 5 & 0 & 1 \\\\ 6 & 0 & 1 \\\\ 7 & 1 & 0 \\\\ 8 & 0 & 1 \\\\ 9 & 0 & 1 \\\\ 10 & 1 & 1 \\end{array} \\$$</span>

##

<span class="math display">\\$$ \\begin{array}{c\|c\|c\|c\|c} \\text{Patient} & Y\_i(A) & Y\_i(B) & Max & \\textrm{Regret}\_i \\\\ \\hline 1 & 1 & 0 \\\\ 2 & 1 & 0 \\\\ 3 & 1 & 1 \\\\ 4 & 0 & 0 \\\\ 5 & 0 & 1 \\\\ 6 & 0 & 1 \\\\ 7 & 1 & 0 \\\\ 8 & 0 & 1 \\\\ 9 & 0 & 1 \\\\ 10 & 1 & 1 \\end{array} \\$$</span>

In your groups:

1.  Add a Max column
2.  Add a Regret column
3.  Compute the total regret

---

[Up: contents](../index.md)
