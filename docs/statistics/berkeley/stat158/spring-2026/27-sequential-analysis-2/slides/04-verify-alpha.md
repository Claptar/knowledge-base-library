---
title: verify alpha
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# verify alpha

**Source:** [`27-sequential-analysis-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

print(paste("\alpha", pbinom(cn, size = n, prob = p0, lower.tail = F)))
```

    [1] "\alpha 0.0384772455724324"

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← find cn](03-find-cn.md) · [Up: contents](index.md) · [calculate beta →](05-calculate-beta.md)
