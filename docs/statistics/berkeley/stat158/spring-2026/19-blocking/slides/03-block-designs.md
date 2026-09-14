---
title: Block Designs
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/19-blocking/slides.html
source_file: sources/berkeley-stat158/spring-2026/19-blocking/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Block Designs

**Source:** [`19-blocking/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/19-blocking/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Block Designs

**Complete Block Design <span class="math inline">\$CB$$\]\$</span>**

Units are partitioned into blocks based on a blocking factor. Treatments are assigned to units such that every treatment is applied exactly once per block. Examples: Study 1 and Study 2.

**Generalized Complete Block Design <span class="math inline">\$GCB\[$$\$</span>**

Similar to <span class="math inline">\$CB$$\]\$</span>, but treatments can appear more than once per block and in unequal numbers. Example: Study 3.

> In both, units are randomly assigned to treatments within each block.

## Why Block?

Remove unwanted variability.

Draw data frame with columns “id”, “run#”, d, and y where id is the unit id, run# is the order in which the units were run, d is the treatment assignment, and y is the response. Show a time trend in the data by making y increase with run#.

Ask: How could I control for the “run” trend?

Answer: form blocks of size two and randomly assign the two units in each block to the two treatments. This way, the time trend is controlled for within each block, and we can more accurately estimate the treatment effect.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

## Forming Blocks

> Blocks should be selected to *maximize the variability in the response between blocks* and to *minimize the variability within each block*.

1.  Sort units into blocks based on a shared characteristic

2.  Subdivide chunks into smaller pieces

3.  Reuse material / subjects

---

[← Examples](02-examples.md) · [Up: contents](index.md) · [Study 2: Drugs and Tapping →](04-study-2-drugs-and-tapping.md)
