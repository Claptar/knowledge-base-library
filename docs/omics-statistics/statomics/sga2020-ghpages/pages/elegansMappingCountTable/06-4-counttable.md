---
title: 4 CountTable
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html
source_file: sources/statomics-sga2020-ghpages/pages/elegansMappingCountTable.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 CountTable

**Source:** [`pages/elegansMappingCountTable.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

``` r
fcElegans<-featureCounts(files=bamfls,annot.ext=paste0(path,"Caenorhabditis_elegans.WBcel235.98.gtf.gz"),isGTFAnnotationFile=TRUE, GTF.featureType = "exon", GTF.attrType = "gene_id", useMetaFeatures = TRUE, strandSpecific = 0,
                    isPairedEnd = FALSE)
```

    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //========================== featureCounts setting ===========================\\
    ## ||                                                                            ||
    ## ||             Input files : 6 BAM files                                      ||
    ## ||                           o SRR1532959.bam                                 ||
    ## ||                           o SRR1532960.bam                                 ||
    ## ||                           o SRR1532961.bam                                 ||
    ## ||                           o SRR1532962.bam                                 ||
    ## ||                           o SRR1532963.bam                                 ||
    ## ||                           o SRR1532964.bam                                 ||
    ## ||                                                                            ||
    ## ||              Annotation : Caenorhabditis_elegans.WBcel235.98.gtf.gz (GTF)  ||
    ## ||      Dir for temp files : .                                                ||
    ## ||                 Threads : 1                                                ||
    ## ||                   Level : meta-feature level                               ||
    ## ||              Paired-end : no                                               ||
    ## ||      Multimapping reads : counted                                          ||
    ## || Multi-overlapping reads : not counted                                      ||
    ## ||   Min overlapping bases : 1                                                ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================================= Running ==================================\\
    ## ||                                                                            ||
    ## || Load annotation file Caenorhabditis_elegans.WBcel235.98.gtf.gz ...         ||
    ## ||    Features : 273641                                                       ||
    ## ||    Meta-features : 46904                                                   ||
    ## ||    Chromosomes/contigs : 7                                                 ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532959.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 1783870                                              ||
    ## ||    Successfully assigned alignments : 1657500 (92.9%)                      ||
    ## ||    Running time : 0.06 minutes                                             ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532960.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 1610969                                              ||
    ## ||    Successfully assigned alignments : 1323934 (82.2%)                      ||
    ## ||    Running time : 0.05 minutes                                             ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532961.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 2117313                                              ||
    ## ||    Successfully assigned alignments : 2013110 (95.1%)                      ||
    ## ||    Running time : 0.07 minutes                                             ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532962.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 1410013                                              ||
    ## ||    Successfully assigned alignments : 1304759 (92.5%)                      ||
    ## ||    Running time : 0.05 minutes                                             ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532963.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 2736076                                              ||
    ## ||    Successfully assigned alignments : 2568046 (93.9%)                      ||
    ## ||    Running time : 0.12 minutes                                             ||
    ## ||                                                                            ||
    ## || Process BAM file SRR1532964.bam...                                         ||
    ## ||    Single-end reads are included.                                          ||
    ## ||    Total alignments : 2338023                                              ||
    ## ||    Successfully assigned alignments : 2208253 (94.4%)                      ||
    ## ||    Running time : 0.07 minutes                                             ||
    ## ||                                                                            ||
    ## ||                                                                            ||
    ## \\============================================================================//

``` r
countTableElegans<-fcElegans$counts
```

We save the countTable for future use

``` r
saveRDS(fcElegans,file="fcElegans.rds")
saveRDS(pdata,file="elegansMetaData.rds")
```

---

[← 3 Build index for C. elegans](05-3-build-index-for-c-elegans.md) · [Up: contents](index.md)
