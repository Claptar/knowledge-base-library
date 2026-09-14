---
title: 3 Build index for C. elegans
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html
source_file: sources/statomics-sga2020-ghpages/pages/elegansMappingCountTable.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Build index for C. elegans

**Source:** [`pages/elegansMappingCountTable.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/elegansMappingCountTable.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

Download the Caenorhabditis\_elegans.WBcel235.dna.toplevel.fa.gz from ensembl. Note that there is no info on multiple haplotypes so the primary assembly files are missing. So the info in toplevel file is the primary assembly.

``` r
path<-"~/Downloads/elegans/"
elegansGenome<-paste0(path,"Caenorhabditis_elegans.WBcel235.dna.toplevel.fa.gz")
system("mkdir elegans_index")
indexName<-"elegans_index/elegans_index_WBcel235_rsubread"
buildindex(basename=indexName,reference=elegansGenome)
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
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## ||                Index name : elegans_index_WBcel235_rsubread                ||
    ## ||               Index space : base space                                     ||
    ## ||               Index split : no-split                                       ||
    ## ||          Repeat threshold : 100 repeats                                    ||
    ## ||              Gapped index : no                                             ||
    ## ||                                                                            ||
    ## ||       Free / total memory : 5.5GB / 16.0GB                                 ||
    ## ||                                                                            ||
    ## ||               Input files : 1 file in total                                ||
    ## ||                             o Caenorhabditis_elegans.WBcel235.dna.topl ... ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================================= Running ==================================\\
    ## ||                                                                            ||
    ## || Check the integrity of provided reference sequences ...                    ||
    ## || No format issues were found                                                ||
    ## || Scan uninformative subreads in reference sequences ...                     ||
    ## || 6850 uninformative subreads were found.                                    ||
    ## || These subreads were excluded from index building.                          ||
    ## || Estimate the index size...                                                 ||
    ## ||  608%,   0 mins elapsed, rate=698969.1k bps/s                              ||
    ## ||  616%,   0 mins elapsed, rate=205637.9k bps/s                              ||
    ## ||  624%,   0 mins elapsed, rate=123384.7k bps/s                              ||
    ## ||  633%,   0 mins elapsed, rate=90251.0k bps/s                               ||
    ## ||  641%,   0 mins elapsed, rate=71222.3k bps/s                               ||
    ## ||  649%,   0 mins elapsed, rate=58548.4k bps/s                               ||
    ## ||  658%,   0 mins elapsed, rate=50270.5k bps/s                               ||
    ## ||  666%,   0 mins elapsed, rate=43910.5k bps/s                               ||
    ## ||  674%,   0 mins elapsed, rate=39180.1k bps/s                               ||
    ## ||  683%,   0 mins elapsed, rate=35402.6k bps/s                               ||
    ## ||  691%,   0 mins elapsed, rate=31815.0k bps/s                               ||
    ## ||  699%,   0 mins elapsed, rate=28910.4k bps/s                               ||
    ## || 1.9 GB of memory is needed for index building.                             ||
    ## || Build the index...                                                         ||
    ## ||    8%,   0 mins elapsed, rate=1152.6k bps/s                                ||
    ## ||   16%,   0 mins elapsed, rate=1296.9k bps/s                                ||
    ## ||   24%,   0 mins elapsed, rate=1345.2k bps/s                                ||
    ## ||   33%,   0 mins elapsed, rate=1386.0k bps/s                                ||
    ## ||   41%,   0 mins elapsed, rate=1391.9k bps/s                                ||
    ## ||   49%,   0 mins elapsed, rate=1406.0k bps/s                                ||
    ## ||   58%,   0 mins elapsed, rate=1406.9k bps/s                                ||
    ## ||   66%,   0 mins elapsed, rate=1408.6k bps/s                                ||
    ## ||   74%,   0 mins elapsed, rate=1450.8k bps/s                                ||
    ## ||   83%,   0 mins elapsed, rate=1458.0k bps/s                                ||
    ## ||   91%,   1 mins elapsed, rate=1478.6k bps/s                                ||
    ## || Save current index block...                                                ||
    ## ||  [ 0.0% finished ]                                                         ||
    ## ||  [ 10.0% finished ]                                                        ||
    ## ||  [ 20.0% finished ]                                                        ||
    ## ||  [ 30.0% finished ]                                                        ||
    ## ||  [ 40.0% finished ]                                                        ||
    ## ||  [ 50.0% finished ]                                                        ||
    ## ||  [ 60.0% finished ]                                                        ||
    ## ||  [ 70.0% finished ]                                                        ||
    ## ||  [ 80.0% finished ]                                                        ||
    ## ||  [ 90.0% finished ]                                                        ||
    ## ||  [ 100.0% finished ]                                                       ||
    ## ||                                                                            ||
    ## ||                      Total running time: 2.7 minutes.                      ||
    ## ||Index elegans_index/elegans_index_WBcel235_rsubread was successfully b ... ||
    ## ||                                                                            ||
    ## \\============================================================================//

## <span class="header-section-number">3.1</span> set path to reads and output

``` r
fastqDir  <- paste0(path,"fastQ")
fls <- list.files(fastqDir, "fastq.gz", full=TRUE)
names(fls) <- sub("small.fastq.gz", "", basename(fls))
system("mkdir bamDir")
bamDir<-"./bamDir"
bamfls<-paste0(bamDir,"/",names(fls),".bam")
names(bamfls)<-names(fls)
```

## <span class="header-section-number">3.2</span> Readmapping

The offset for the phred scores is 64. We find info on illumina incoding in quality control step of fastQC.

``` r
phredOffset<-64
align(index=indexName,readfile1=fls,input_format="gzFASTQ",output_format="BAM",output_file=bamfls,phredOffset=phredOffset)
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
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532959small.fastq.gz                                   ||
    ## || Output file   : SRR1532959.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:22:16, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,40]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.1 mins elapsed, rate=42.5k reads per second             ||
    ## ||    7% completed, 0.1 mins elapsed, rate=49.3k reads per second             ||
    ## ||   13% completed, 0.2 mins elapsed, rate=39.8k reads per second             ||
    ## ||   19% completed, 0.2 mins elapsed, rate=42.5k reads per second             ||
    ## ||   26% completed, 0.2 mins elapsed, rate=40.3k reads per second             ||
    ## ||   33% completed, 0.3 mins elapsed, rate=39.6k reads per second             ||
    ## ||   39% completed, 0.4 mins elapsed, rate=39.3k reads per second             ||
    ## ||   45% completed, 0.5 mins elapsed, rate=33.9k reads per second             ||
    ## ||   52% completed, 0.6 mins elapsed, rate=30.9k reads per second             ||
    ## ||   59% completed, 0.6 mins elapsed, rate=30.2k reads per second             ||
    ## ||   66% completed, 0.7 mins elapsed, rate=31.4k reads per second             ||
    ## ||   70% completed, 0.7 mins elapsed, rate=28.2k reads per second             ||
    ## ||   73% completed, 0.8 mins elapsed, rate=28.6k reads per second             ||
    ## ||   76% completed, 0.8 mins elapsed, rate=28.7k reads per second             ||
    ## ||   80% completed, 0.8 mins elapsed, rate=29.1k reads per second             ||
    ## ||   83% completed, 0.8 mins elapsed, rate=29.4k reads per second             ||
    ## ||   86% completed, 0.9 mins elapsed, rate=29.8k reads per second             ||
    ## ||   89% completed, 0.9 mins elapsed, rate=30.1k reads per second             ||
    ## ||   93% completed, 0.9 mins elapsed, rate=30.5k reads per second             ||
    ## ||   96% completed, 0.9 mins elapsed, rate=30.7k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 1783870                                      ||
    ## ||                      Mapped : 1685472 (94.5%)                              ||
    ## ||             Uniquely mapped : 1632698                                      ||
    ## ||               Multi-mapping : 52774                                        ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 98398                                        ||
    ## ||                                                                            ||
    ## ||                      Indels : 2512                                         ||
    ## ||                                                                            ||
    ## ||                Running time : 1.0 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532960small.fastq.gz                                   ||
    ## || Output file   : SRR1532960.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:23:14, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,40]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.1 mins elapsed, rate=21.5k reads per second             ||
    ## ||    7% completed, 0.2 mins elapsed, rate=41.3k reads per second             ||
    ## ||   14% completed, 0.2 mins elapsed, rate=45.1k reads per second             ||
    ## ||   20% completed, 0.2 mins elapsed, rate=45.3k reads per second             ||
    ## ||   27% completed, 0.3 mins elapsed, rate=47.4k reads per second             ||
    ## ||   34% completed, 0.3 mins elapsed, rate=48.5k reads per second             ||
    ## ||   40% completed, 0.3 mins elapsed, rate=49.2k reads per second             ||
    ## ||   47% completed, 0.4 mins elapsed, rate=50.1k reads per second             ||
    ## ||   54% completed, 0.4 mins elapsed, rate=49.9k reads per second             ||
    ## ||   61% completed, 0.4 mins elapsed, rate=50.0k reads per second             ||
    ## ||   70% completed, 0.5 mins elapsed, rate=36.6k reads per second             ||
    ## ||   73% completed, 0.5 mins elapsed, rate=36.6k reads per second             ||
    ## ||   76% completed, 0.6 mins elapsed, rate=36.8k reads per second             ||
    ## ||   79% completed, 0.6 mins elapsed, rate=37.1k reads per second             ||
    ## ||   83% completed, 0.6 mins elapsed, rate=37.1k reads per second             ||
    ## ||   86% completed, 0.6 mins elapsed, rate=37.2k reads per second             ||
    ## ||   89% completed, 0.7 mins elapsed, rate=37.1k reads per second             ||
    ## ||   93% completed, 0.7 mins elapsed, rate=37.1k reads per second             ||
    ## ||   96% completed, 0.7 mins elapsed, rate=37.0k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 1610969                                      ||
    ## ||                      Mapped : 1353023 (84.0%)                              ||
    ## ||             Uniquely mapped : 1300506                                      ||
    ## ||               Multi-mapping : 52517                                        ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 257946                                       ||
    ## ||                                                                            ||
    ## ||                      Indels : 2303                                         ||
    ## ||                                                                            ||
    ## ||                Running time : 0.7 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532961small.fastq.gz                                   ||
    ## || Output file   : SRR1532961.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:23:58, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,39]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.0 mins elapsed, rate=37.0k reads per second             ||
    ## ||    6% completed, 0.1 mins elapsed, rate=47.4k reads per second             ||
    ## ||   12% completed, 0.1 mins elapsed, rate=45.2k reads per second             ||
    ## ||   19% completed, 0.2 mins elapsed, rate=34.3k reads per second             ||
    ## ||   25% completed, 0.3 mins elapsed, rate=37.3k reads per second             ||
    ## ||   31% completed, 0.3 mins elapsed, rate=38.9k reads per second             ||
    ## ||   38% completed, 0.4 mins elapsed, rate=40.0k reads per second             ||
    ## ||   45% completed, 0.4 mins elapsed, rate=40.6k reads per second             ||
    ## ||   51% completed, 0.5 mins elapsed, rate=40.8k reads per second             ||
    ## ||   58% completed, 0.5 mins elapsed, rate=41.4k reads per second             ||
    ## ||   64% completed, 0.6 mins elapsed, rate=41.2k reads per second             ||
    ## ||   70% completed, 0.7 mins elapsed, rate=36.2k reads per second             ||
    ## ||   73% completed, 0.7 mins elapsed, rate=36.0k reads per second             ||
    ## ||   76% completed, 0.8 mins elapsed, rate=36.1k reads per second             ||
    ## ||   80% completed, 0.8 mins elapsed, rate=36.1k reads per second             ||
    ## ||   83% completed, 0.8 mins elapsed, rate=35.9k reads per second             ||
    ## ||   87% completed, 0.9 mins elapsed, rate=36.1k reads per second             ||
    ## ||   90% completed, 0.9 mins elapsed, rate=36.1k reads per second             ||
    ## ||   93% completed, 0.9 mins elapsed, rate=36.2k reads per second             ||
    ## ||   96% completed, 0.9 mins elapsed, rate=36.4k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 2117313                                      ||
    ## ||                      Mapped : 2049912 (96.8%)                              ||
    ## ||             Uniquely mapped : 2005307                                      ||
    ## ||               Multi-mapping : 44605                                        ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 67401                                        ||
    ## ||                                                                            ||
    ## ||                      Indels : 7289                                         ||
    ## ||                                                                            ||
    ## ||                Running time : 1.0 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532962small.fastq.gz                                   ||
    ## || Output file   : SRR1532962.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:24:56, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,40]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.0 mins elapsed, rate=39.5k reads per second             ||
    ## ||    6% completed, 0.1 mins elapsed, rate=43.9k reads per second             ||
    ## ||   12% completed, 0.1 mins elapsed, rate=45.2k reads per second             ||
    ## ||   19% completed, 0.1 mins elapsed, rate=45.7k reads per second             ||
    ## ||   25% completed, 0.2 mins elapsed, rate=46.0k reads per second             ||
    ## ||   31% completed, 0.2 mins elapsed, rate=46.7k reads per second             ||
    ## ||   38% completed, 0.2 mins elapsed, rate=46.7k reads per second             ||
    ## ||   45% completed, 0.3 mins elapsed, rate=47.0k reads per second             ||
    ## ||   52% completed, 0.3 mins elapsed, rate=47.4k reads per second             ||
    ## ||   58% completed, 0.3 mins elapsed, rate=47.7k reads per second             ||
    ## ||   64% completed, 0.4 mins elapsed, rate=47.0k reads per second             ||
    ## ||   70% completed, 0.4 mins elapsed, rate=39.5k reads per second             ||
    ## ||   73% completed, 0.4 mins elapsed, rate=38.8k reads per second             ||
    ## ||   76% completed, 0.5 mins elapsed, rate=38.8k reads per second             ||
    ## ||   80% completed, 0.5 mins elapsed, rate=38.7k reads per second             ||
    ## ||   83% completed, 0.5 mins elapsed, rate=38.7k reads per second             ||
    ## ||   86% completed, 0.5 mins elapsed, rate=38.9k reads per second             ||
    ## ||   90% completed, 0.5 mins elapsed, rate=39.1k reads per second             ||
    ## ||   93% completed, 0.6 mins elapsed, rate=39.1k reads per second             ||
    ## ||   96% completed, 0.6 mins elapsed, rate=39.0k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 1410013                                      ||
    ## ||                      Mapped : 1327093 (94.1%)                              ||
    ## ||             Uniquely mapped : 1299154                                      ||
    ## ||               Multi-mapping : 27939                                        ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 82920                                        ||
    ## ||                                                                            ||
    ## ||                      Indels : 4824                                         ||
    ## ||                                                                            ||
    ## ||                Running time : 0.6 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532963small.fastq.gz                                   ||
    ## || Output file   : SRR1532963.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:25:33, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,41]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.0 mins elapsed, rate=35.7k reads per second             ||
    ## ||    6% completed, 0.1 mins elapsed, rate=54.0k reads per second             ||
    ## ||   13% completed, 0.2 mins elapsed, rate=54.9k reads per second             ||
    ## ||   20% completed, 0.2 mins elapsed, rate=53.2k reads per second             ||
    ## ||   26% completed, 0.3 mins elapsed, rate=51.6k reads per second             ||
    ## ||   33% completed, 0.3 mins elapsed, rate=51.0k reads per second             ||
    ## ||   40% completed, 0.4 mins elapsed, rate=50.8k reads per second             ||
    ## ||   46% completed, 0.5 mins elapsed, rate=49.0k reads per second             ||
    ## ||   53% completed, 0.5 mins elapsed, rate=48.7k reads per second             ||
    ## ||   60% completed, 0.6 mins elapsed, rate=48.6k reads per second             ||
    ## ||   69% completed, 0.8 mins elapsed, rate=40.4k reads per second             ||
    ## ||   73% completed, 0.8 mins elapsed, rate=39.4k reads per second             ||
    ## ||   76% completed, 0.9 mins elapsed, rate=38.2k reads per second             ||
    ## ||   79% completed, 1.0 mins elapsed, rate=37.4k reads per second             ||
    ## ||   83% completed, 1.0 mins elapsed, rate=36.7k reads per second             ||
    ## ||   86% completed, 1.1 mins elapsed, rate=36.0k reads per second             ||
    ## ||   89% completed, 1.2 mins elapsed, rate=35.4k reads per second             ||
    ## ||   93% completed, 1.2 mins elapsed, rate=34.8k reads per second             ||
    ## ||   96% completed, 1.3 mins elapsed, rate=34.2k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 2736076                                      ||
    ## ||                      Mapped : 2627215 (96.0%)                              ||
    ## ||             Uniquely mapped : 2451220                                      ||
    ## ||               Multi-mapping : 175995                                       ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 108861                                       ||
    ## ||                                                                            ||
    ## ||                      Indels : 11317                                        ||
    ## ||                                                                            ||
    ## ||                Running time : 1.4 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ##
    ##         ==========     _____ _    _ ____  _____  ______          _____
    ##         =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
    ##           =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
    ##             ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
    ##               ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
    ##         ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
    ##        Rsubread 1.34.7
    ##
    ## //================================= setting ==================================\\
    ## ||                                                                            ||
    ## || Function      : Read alignment (RNA-Seq)                                   ||
    ## || Input file    : SRR1532964small.fastq.gz                                   ||
    ## || Output file   : SRR1532964.bam (BAM)                                       ||
    ## || Index name    : elegans_index_WBcel235_rsubread                            ||
    ## ||                                                                            ||
    ## ||                    ------------------------------------                    ||
    ## ||                                                                            ||
    ## ||                               Threads : 1                                  ||
    ## ||                          Phred offset : 64                                 ||
    ## ||                             Min votes : 3 / 10                             ||
    ## ||                        Max mismatches : 3                                  ||
    ## ||                      Max indel length : 5                                  ||
    ## ||            Report multi-mapping reads : yes                                ||
    ## || Max alignments per multi-mapping read : 1                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//
    ##
    ## //================= Running (27-Oct-2019 15:26:54, pid=8867) =================\\
    ## ||                                                                            ||
    ## || The input file contains base space reads.                                  ||
    ## || The range of Phred scores observed in the data is [2,41]                   ||
    ## || Load the 1-th index block...                                               ||
    ## ||    0% completed, 0.1 mins elapsed, rate=15.4k reads per second             ||
    ## ||    7% completed, 0.1 mins elapsed, rate=37.0k reads per second             ||
    ## ||   13% completed, 0.2 mins elapsed, rate=42.5k reads per second             ||
    ## ||   20% completed, 0.3 mins elapsed, rate=43.7k reads per second             ||
    ## ||   27% completed, 0.3 mins elapsed, rate=44.5k reads per second             ||
    ## ||   33% completed, 0.4 mins elapsed, rate=45.4k reads per second             ||
    ## ||   40% completed, 0.4 mins elapsed, rate=46.5k reads per second             ||
    ## ||   46% completed, 0.5 mins elapsed, rate=46.9k reads per second             ||
    ## ||   53% completed, 0.5 mins elapsed, rate=47.2k reads per second             ||
    ## ||   60% completed, 0.6 mins elapsed, rate=46.8k reads per second             ||
    ## ||   70% completed, 0.7 mins elapsed, rate=39.1k reads per second             ||
    ## ||   73% completed, 0.7 mins elapsed, rate=38.9k reads per second             ||
    ## ||   76% completed, 0.8 mins elapsed, rate=38.8k reads per second             ||
    ## ||   80% completed, 0.8 mins elapsed, rate=38.4k reads per second             ||
    ## ||   83% completed, 0.9 mins elapsed, rate=38.0k reads per second             ||
    ## ||   86% completed, 0.9 mins elapsed, rate=37.9k reads per second             ||
    ## ||   90% completed, 0.9 mins elapsed, rate=37.4k reads per second             ||
    ## ||   93% completed, 1.0 mins elapsed, rate=37.4k reads per second             ||
    ## ||   96% completed, 1.0 mins elapsed, rate=37.4k reads per second             ||
    ## ||                                                                            ||
    ## ||                           Completed successfully.                          ||
    ## ||                                                                            ||
    ## \\====================================    ====================================//
    ##
    ## //================================   Summary =================================\\
    ## ||                                                                            ||
    ## ||                 Total reads : 2338023                                      ||
    ## ||                      Mapped : 2245445 (96.0%)                              ||
    ## ||             Uniquely mapped : 2184002                                      ||
    ## ||               Multi-mapping : 61443                                        ||
    ## ||                                                                            ||
    ## ||                    Unmapped : 92578                                        ||
    ## ||                                                                            ||
    ## ||                      Indels : 8247                                         ||
    ## ||                                                                            ||
    ## ||                Running time : 1.1 minutes                                  ||
    ## ||                                                                            ||
    ## \\============================================================================//

    ##                       SRR1532959.bam SRR1532960.bam SRR1532961.bam
    ## Total_reads                  1783870        1610969        2117313
    ## Mapped_reads                 1685472        1353023        2049912
    ## Uniquely_mapped_reads        1632698        1300506        2005307
    ## Multi_mapping_reads            52774          52517          44605
    ## Unmapped_reads                 98398         257946          67401
    ## Indels                          2512           2303           7289
    ##                       SRR1532962.bam SRR1532963.bam SRR1532964.bam
    ## Total_reads                  1410013        2736076        2338023
    ## Mapped_reads                 1327093        2627215        2245445
    ## Uniquely_mapped_reads        1299154        2451220        2184002
    ## Multi_mapping_reads            27939         175995          61443
    ## Unmapped_reads                 82920         108861          92578
    ## Indels                          4824          11317           8247

---

[← 2 Get info on experiment](04-2-get-info-on-experiment.md) · [Up: contents](index.md) · [4 CountTable →](06-4-counttable.md)
