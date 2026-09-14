---
title: 2 Get info on experiment
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html
source_file: sources/statomics-sga2020-ghpages/pages/elegansMappingCountTable.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Get info on experiment

**Source:** [`pages/elegansMappingCountTable.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">2.1</span> Get info on samples

Get all info from GEO. get sample info via getGEO (info from samples)

``` r
gse<-getGEO("GSE59943")
```

    ## Found 2 file(s)

    ## GSE59943-GPL13657_series_matrix.txt.gz

    ## Parsed with column specification:
    ## cols(
    ##   ID_REF = col_character(),
    ##   GSM1462557 = col_character(),
    ##   GSM1462558 = col_character(),
    ##   GSM1462559 = col_character(),
    ##   GSM1462560 = col_character()
    ## )

    ## File stored at:

    ## /var/folders/p1/3js9hvbs473g1klcmqm0d8wm0000gn/T//Rtmp4rfCmx/GPL13657.soft

    ## GSE59943-GPL9269_series_matrix.txt.gz

    ## Parsed with column specification:
    ## cols(
    ##   ID_REF = col_character(),
    ##   GSM1462555 = col_character(),
    ##   GSM1462556 = col_character()
    ## )

    ## File stored at:

    ## /var/folders/p1/3js9hvbs473g1klcmqm0d8wm0000gn/T//Rtmp4rfCmx/GPL9269.soft

``` r
length(gse)
```

    ## [1] 2

There are two objects because there were runs with two different machines. Combine the data from both files and add sample name column in order to be able to link the info to that from SRA.

``` r
pdata<-rbind(pData(gse[[1]]),pData(gse[[2]]))
pdata$SampleName<-rownames(pdata)
```

## <span class="header-section-number">2.2</span> Get info on sequencing files

Download SRA info. To link sample info to info sequencing: Go to corresponding SRA page and save the information via the “Send to: File button” This file can also be used to make a script to download sequencing files from the web. Note that sra files can be converted to fastq files via the fastq-dump function of the sra-tools.

``` r
sraInfo<-read.csv("SraRunInfo.csv")
pdata<-merge(pdata,sraInfo,by="SampleName")
pdata$Run
```

    ## [1] SRR1532959 SRR1532960 SRR1532961 SRR1532962 SRR1532963 SRR1532964
    ## 6 Levels: SRR1532959 SRR1532960 SRR1532961 SRR1532962 ... SRR1532964

The run is also the name of the SRA file so we will be able to link alignment file name to the experiment via the SRA file info.

---

[← 1 Background](03-1-background.md) · [Up: contents](index.md) · [3 Build index for C. elegans →](05-3-build-index-for-c-elegans.md)
