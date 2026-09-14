---
title: calculate beta
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# calculate beta

**Source:** [`27-sequential-analysis-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

print(paste("1-\beta:", pbinom(cn, size = n, prob = p1, lower.tail = F)))
```

    [1] "1-\beta: 0.907466218485276"

Recall, using the SPRT we had on average less than 40 samples. Power calculations indicate we should have 77 samples.

## Always Do Sequential Testing Theorem

There is a theorem, which is hard to write down exactly, but I call it the **Always Do Sequential Testing Theorem** <span class="citation" cites="wald1948optimum">Wald and Wolfowitz (<a href="#/references" role="doc-biblioref" onclick="">1948</a>)</span>.

> If you pick <span class="math inline">\$n\$</span> via a power calculation, on average you could have gotten away with *fewer* samples had you used a sequential test instead.

---

[← verify alpha](04-verify-alpha.md) · [Up: contents](index.md) · [Use in Industry and Research →](06-use-in-industry-and-research.md)
