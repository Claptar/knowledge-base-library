---
title: 1 Background
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html
source_file: sources/statomics-sga2020-ghpages/pages/elegansMappingCountTable.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Background

**Source:** [`pages/elegansMappingCountTable.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

After fertilization but prior to the onset of zygotic transcription, the C. elegans zygote cleaves asymmetrically to create the anterior AB and posterior P1 blastomeres, each of which goes on to generate distinct cell lineages. To understand how patterns of RNA inheritance and abundance arise after this first asymmetric cell division, we pooled hand-dissected AB and P1 blastomeres and performed RNA-seq. <http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59943>

``` r
library(Rsubread)
```

    ## Warning: package 'Rsubread' was built under R version 3.6.1

``` r
library( "GEOquery" )
```

    ## Loading required package: Biobase

    ## Loading required package: BiocGenerics

    ## Loading required package: parallel

    ##
    ## Attaching package: 'BiocGenerics'

    ## The following objects are masked from 'package:parallel':
    ##
    ##     clusterApply, clusterApplyLB, clusterCall, clusterEvalQ,
    ##     clusterExport, clusterMap, parApply, parCapply, parLapply,
    ##     parLapplyLB, parRapply, parSapply, parSapplyLB

    ## The following objects are masked from 'package:stats':
    ##
    ##     IQR, mad, sd, var, xtabs

    ## The following objects are masked from 'package:base':
    ##
    ##     Filter, Find, Map, Position, Reduce, anyDuplicated, append,
    ##     as.data.frame, basename, cbind, colnames, dirname, do.call,
    ##     duplicated, eval, evalq, get, grep, grepl, intersect,
    ##     is.unsorted, lapply, mapply, match, mget, order, paste, pmax,
    ##     pmax.int, pmin, pmin.int, rank, rbind, rownames, sapply,
    ##     setdiff, sort, table, tapply, union, unique, unsplit, which,
    ##     which.max, which.min

    ## Welcome to Bioconductor
    ##
    ##     Vignettes contain introductory material; view with
    ##     'browseVignettes()'. To cite Bioconductor, see
    ##     'citation("Biobase")', and for packages 'citation("pkgname")'.

    ## Setting options('download.file.method.GEOquery'='auto')

    ## Setting options('GEOquery.inmemory.gpl'=FALSE)

We will use the Rsubread read mapper because that is avaible in R for all platforms (Linux, Windows and Mac). For real projects I prefer the use of STAR.

---

[← Contents {#contents}](02-contents-contents.md) · [Up: contents](index.md) · [2 Get info on experiment →](04-2-get-info-on-experiment.md)
