---
title: Fixed vs. Sequential
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Fixed vs. Sequential

**Source:** [`27-sequential-analysis-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Why Sequential Testing?

First, why should we do sequential testing? Why not just prespecify <span class="math inline">\$n\$</span>?

## Recall the Artillery Example

- We have access to a stream of <span class="math inline">\$0,1\$</span> data.
- Testing if our bullets are faulty or are they good (enough)?
- Specify <span class="math inline">\$n\$</span> beforehand using a power calculation.

## Power Calculations

We can calculate the number of samples using a power calculation *(Boardwork)*

## Verify {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
n <- 77; alpha <- 0.05; beta <- 0.1; p0 <- 0.05; p1 <- 0.15

---

[← Sequential Testing for Experimental Design](01-sequential-testing-for-experimental-design.md) · [Up: contents](index.md) · [find cn →](03-find-cn.md)
