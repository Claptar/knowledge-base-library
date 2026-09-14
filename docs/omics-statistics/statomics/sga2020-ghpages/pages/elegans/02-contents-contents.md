---
title: Contents {#contents}
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegans.html
source_file: sources/statomics-sga2020-ghpages/pages/elegans.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Contents {#contents}

**Source:** [`pages/elegans.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegans.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

- <span class="toc-section-number">1</span> Read featurecounts object
  - <span class="toc-section-number">1.1</span> Read Meta Data
- <span class="toc-section-number">2</span> Data Analysis
  - <span class="toc-section-number">2.1</span> Setup count object edgeR
  - <span class="toc-section-number">2.2</span> Normalisation
  - <span class="toc-section-number">2.3</span> Data exploration
  - <span class="toc-section-number">2.4</span> Differential analysis
    - <span class="toc-section-number">2.4.1</span> Filtering
    - <span class="toc-section-number">2.4.2</span> Model
    - <span class="toc-section-number">2.4.3</span> Plots

After fertilization but prior to the onset of zygotic transcription, the C. elegans zygote cleaves asymmetrically to create the anterior AB and posterior P1 blastomeres, each of which goes on to generate distinct cell lineages. To understand how patterns of RNA inheritance and abundance arise after this first asymmetric cell division, we pooled hand-dissected AB and P1 blastomeres and performed RNA-seq. <http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59943>

The reads have been aligned to the genome and summarized to gene level in the Rsubread tutorial.

``` r
library(edgeR)
```

    ## Loading required package: limma

---

[← Elegans: DE analysis {#elegans-de-analysis .title .toc-ignore}](01-elegans-de-analysis-elegans-de-analysis-title-toc-ignore.md) · [Up: contents](index.md) · [1 Read featurecounts object →](03-1-read-featurecounts-object.md)
