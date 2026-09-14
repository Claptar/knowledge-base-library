---
title: Slides
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/30-implementing-ucb/slides.html
source_file: sources/berkeley-stat158/spring-2026/30-implementing-ucb/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Slides

**Source:** [`30-implementing-ucb/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/30-implementing-ucb/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# Implementing UCB {#implementing-ucb .title}

## UCB practice: snapshot at <span class="math inline">\$t=10\$</span>

Suppose the trial has reached patient <span class="math inline">\$t=10\$</span>, and the observed data so far are:

| <span class="math inline">\$t\$</span> | <span class="math inline">\$d\_i\$</span> | <span class="math inline">\$y\_i\$</span> |
|---:|:--:|:--:|
| 1 | A | 1 |
| 2 | A | 1 |
| 3 | A | 0 |
| 4 | A | 1 |
| 5 | A | 1 |
| 6 | A | 0 |
| 7 | A | 1 |
| 8 | B | 1 |
| 9 | B | 0 |
| 10 | B | 0 |

1.  Complete the next assignment, <span class="math inline">\$d\_{11}\$</span>, using a Wald-style upper bound.
2.  Complete the next assignment, <span class="math inline">\$d\_{11}\$</span>, using a Hoeffding-style upper bound.

---

[Up: contents](../index.md)
