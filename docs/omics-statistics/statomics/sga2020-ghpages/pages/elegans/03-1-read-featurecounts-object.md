---
title: 1 Read featurecounts object
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegans.html
source_file: sources/statomics-sga2020-ghpages/pages/elegans.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Read featurecounts object

**Source:** [`pages/elegans.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegans.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

We import the featurecounts object that we have stored.

``` r
fc <- readRDS("fcElegans.rds")
names(fc)
```

    ## [1] "counts"     "annotation" "targets"    "stat"

``` r
counts_featurecounts <- fc$counts
head(counts_featurecounts)
```

    ##                SRR1532959.bam SRR1532960.bam SRR1532961.bam SRR1532962.bam
    ## WBGene00197333              0              0              0              0
    ## WBGene00198386              0              0              0              0
    ## WBGene00015153              0              0              0              0
    ## WBGene00002061            152            253            157             95
    ## WBGene00255704              0              0              0              0
    ## WBGene00235314              0              0              0              0
    ##                SRR1532963.bam SRR1532964.bam
    ## WBGene00197333              0              0
    ## WBGene00198386              0              0
    ## WBGene00015153              1              2
    ## WBGene00002061            144            152
    ## WBGene00255704              0              0
    ## WBGene00235314              0              0

``` r
dim(counts_featurecounts)
```

    ## [1] 46904     6

``` r
fc$stat
```

    ##                           Status SRR1532959.bam SRR1532960.bam
    ## 1                       Assigned        1657500        1323934
    ## 2            Unassigned_Unmapped          98398         257946
    ## 3           Unassigned_Read_Type              0              0
    ## 4           Unassigned_Singleton              0              0
    ## 5      Unassigned_MappingQuality              0              0
    ## 6             Unassigned_Chimera              0              0
    ## 7      Unassigned_FragmentLength              0              0
    ## 8           Unassigned_Duplicate              0              0
    ## 9        Unassigned_MultiMapping              0              0
    ## 10          Unassigned_Secondary              0              0
    ## 11           Unassigned_NonSplit              0              0
    ## 12         Unassigned_NoFeatures           9430          11104
    ## 13 Unassigned_Overlapping_Length              0              0
    ## 14          Unassigned_Ambiguity          18542          17985
    ##    SRR1532961.bam SRR1532962.bam SRR1532963.bam SRR1532964.bam
    ## 1         2013110        1304759        2568046        2208253
    ## 2           67401          82920         108861          92578
    ## 3               0              0              0              0
    ## 4               0              0              0              0
    ## 5               0              0              0              0
    ## 6               0              0              0              0
    ## 7               0              0              0              0
    ## 8               0              0              0              0
    ## 9               0              0              0              0
    ## 10              0              0              0              0
    ## 11              0              0              0              0
    ## 12          10279           5867          11931           9791
    ## 13              0              0              0              0
    ## 14          26523          16467          47238          27401

## <span class="header-section-number">1.1</span> Read Meta Data

``` r
target<-readRDS("elegansMetaData.rds")
```

---

[← Contents {#contents}](02-contents-contents.md) · [Up: contents](index.md) · [2 Data Analysis →](04-2-data-analysis.md)
