---
title: Unit 07 — bigData Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — bigData Part 02 —

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

dbWriteTable(conn = db, name = "class", value = class, row.names = FALSE)

### **2.6 SAS**

SAS is quite good at handling large datasets, storing them on disk rather than in memory. I have used SAS in the past for subsetting and merging large datasets. Then I will generally extract the data I need for statistical modeling and do the analysis in R.

Here’s an example of some SAS code for reading in a CSV followed by some subsetting and merging and then output.

/* we can use a pipe - in this case to remove carriage returns, */ /* presumably because the CSV file was created in Windows */ filename tmp pipe "cat ~/shared/hei/gis/100w4kmgrid.csv | tr -d '\r'";

/* read in one data file */ data grid; infile tmp lrecl=500 truncover dsd firstobs=2;

informat gridID x y landMask dataMask; input gridID x y landMask dataMask;

run ;

filename tmp pipe "cat ~/shared/hei/GOES12/goes/Goes_int4km.csv | tr -d

/* read in second data file */ data match; infile tmp

11

lrecl=500 truncover dsd firstobs=2; informat goesID gridID areaInt areaPix; input goesID gridID areaInt areaPix; run ; /* need to sort before merging */ proc sort data=grid; by gridID; run; proc sort data=match; by gridID; run; /* notice some similarity to SQL */ data merged; merge match(in=in1) grid(in=in2); by gridID; /* key field */ if in1=1; /* also do some subsetting */ /* only keep certain fields */ keep gridID goesID x y landMask dataMask areaInt areaPix; run; /* do some subsetting */ data PA; /* new dataset */ set merged; /* original dataset */ if x<1900000 and x>1200000 and y<2300000 and y>1900000; run;

%let filename="~/shared/hei/code/model/GOES-gridMatchPA.csv"; /* output to CSV */ PROC EXPORT DATA= WORK.PA OUTFILE= &filename DBMS=CSV REPLACE; RUN;

Note that SAS is oriented towards working with data in a “data frame”-style format; i.e., rows

12

as observations and columns as fields, with different fields of possibly different types. As you can see in the syntax above, the operations concentrate on transforming one dataset into another dataset.

## **3 R and big data**

There has been a lot of work in recent years to allow R to work with big datasets.

- The _data.table_ package provides for fast operations on large data tables in memory. The _dplyr_ package has also been optimized to work quickly on large data tables in memory, including operating on _data.table_ objects from the _data.table_ package.

- The _ff_ and _bigmemory_ packages provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R.

- The _biglm_ package provides the ability to fit linear models and GLMs to big datasets, with integration with _ff_ and _bigmemory_ .

- Finally the _sqldf_ package provides the ability to use SQL queries on R dataframes and onthe-fly when reading from CSV files. The latter can help you avoid reading in the entire dataset into memory in R if you just need a subset of it.

In this section we’ll use an example of US government data on airline delays (1987-2008) available through the ASA 2009 Data Expo at http://stat-computing.org/dataexpo/2009/the-data.html.

First we’ll use UNIX tools to download the individual yearly CSV files and make a single CSV (~12 Gb). See the demo code file for the bash code. Note that it’s much smaller when compressed (1.7 Gb) or if stored in a binary format.

### **3.1 Working quickly with big datasets in memory: data.table**

In many cases, particularly on a machine with a lot of memory, R might be able to read the dataset into memory but computations with the dataset may be slow.

The _data.table_ package provides a lot of functionality for fast manipulation: indexing, merges/joins, assignment, grouping, etc.

Let’s read in the airline dataset, specifying the column classes so that _fread()_ doesn’t have to detect what they are. I’ll also use factors since factors are represented numerically. It only takes about 5 minutes to read the data in. We’ll see in the next section that this is much faster than with other approaches within R.

13

**require** (data.table) fileName <- '/tmp/AirlineDataAll.csv' dt <- **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6))) _#Read 123534969 rows and 29 (of 29) columns from # 11.203 GB file in 00:05:16_ **class** (dt) _# [1] "data.table" "data.frame"_

Now let’s do some basic subsetting. We’ll see that setting a key and using binary search can improve lookup speed dramatically.

**system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.8 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000)) _## 12.7 seconds_

**system.time** ( **setkey** (dt, Origin, Distance)) _## 33 seconds: ## takes some time, but will speed up later operations_ **tables** () _## NAME NROW MB ##[1,] dt 123,534,969 27334 ##[2,] sfo 2,733,910 606 ##[3,] sfoShort 1,707,171 379 ## COLS ##[1,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[2,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[3,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ## KEY ##[1,] Origin,Distance_

14

_##[2,] ##[3,] ##Total: 28,319MB ## vector scan_ **system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.5 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000 )) _## 12.4 seconds ## binary search_ **system.time** (sfo <- dt[ **.** ('SFO'), ]) _## 0.8 seconds_

Setting a key in _data.table_ simply amounts to sorting based on the columns provided, which allows for fast lookup later using binary search algorithms, as seen with the last query. Think about the analogy of looking up by name vs. index that we discussed in Unit 4. From my fairly quick look through the _data.table_ documentation I don’t see a way to do the subsetting with distance less than 1000 using the specialized functionality of _data.table_ .

There’s a bunch more to _data.table_ and you’ll have to learn a modest amount of new syntax, but if you’re working with large datasets in memory, it will probably be well worth your while. Plus _data.table_ objects are data frames (i.e., they inherit from data frames) so they are compatible with R code that uses dataframes.

### **3.2 Working with big datasets on disk: ff and bigmemory**

Note that with our 12 Gb dataset, the data took up 27 Gb of RAM on the SCF server _radagast_ . Operations on the dataset would then use up additional RAM. So this would not be feasible on most machines. And of course other datasets might be so big that even _radagast_ wouldn’t be able to hold them in memory.

#### **3.2.1 ff**

Now we can read the data into R using the _ff_ package, in particular reading in as an _ffdf_ object. Note the arguments are similar to those for _read.{table,csv}()_ . _read.table.ffdf()_ reads the data in chunks.

15

**require** (ff) **require** (ffbase)

_# I put the data file on local disk on the machine I am using # (/tmp on radagast) # it's good to test with a small subset before # doing the full operations_ fileName <- '/tmp/test.csv' dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4), 'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor','factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6)))

fileName <- '/tmp/AirlineDataAll.csv' **system.time** ( dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4), 'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor', 'factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6))) ) _## takes about 22 minutes_

**system.time** ( **ffsave** (dat, file = '/tmp/AirlineDataAll')) _## takes 11 minutes ## file is saved (in a binary format) as AirlineDataAll.ffData ## with metadata in AirlineDataAll.RData_ **rm** (dat) _# pretend we are in a new R session_ **system.time** ( **ffload** ('/tmp/AirlineDataAll')) _# this is much quicker: # 107 seconds_

In the above operations, we wrote a copy of the file in the ff binary format that can be read more quickly back into R than the original reading of the CSV using _ffsave()_ and _ffload()_ . Also note the reduced size of the binary format file compared to the original CSV. It’s good to be aware of where

16

the binary ff file is stored given that for large datasets, it will be large. With _ff_ (I think _bigmemory_ is different in how it handles this) it appears to be stored in _/tmp_ in an R temporary directory. Note that as we work with large files we need to be more aware of the filesystem, making sure in this case that _/tmp_ has enough space.

Let’s look at the _ff_ and _ffbase_ packages to see what functions are available using library(help=ff). Notice that there is an _merge.ff()_ .

Note that a copy of an _ff_ object appears to be a shallow copy.

Next let’s do a bit of exploration of the dataset. Of course in a real analysis we’d do a lot more and some of this would take some time.

**ffload** ('/tmp/AirlineDataAll') _# [1] "tmp/RtmpU5Uw6z/ffdf4e684aecd7c4.ff" "tmp/RtmpU5Uw6z/ffdf4e687fb73a88.ff" # [3] "tmp/RtmpU5Uw6z/ffdf4e6862b1033f.ff" "tmp/RtmpU5Uw6z/ffdf4e6820053932.ff" # [5] "tmp/RtmpU5Uw6z/ffdf4e681e7d2235.ff" "tmp/RtmpU5Uw6z/ffdf4e686aa01c8.ff" # ..._

dat$Dest

_# ff (closed) integer length=123534969 (123534969) levels: BUR LAS LAX OAK # ABE ABQ ACV ALB ALO AMA ANC ATL AUS AVP AZO BDL BFL BGR BHM BIL BLI BNA BOI # CAK CCR CHS CID CLE CLT CMH CMI COS CPR CRP CRW CVG DAB DAL DAY DCA DEN DFW # EUG EVV EWR FAI FAR FAT FLG FLL FOE FSD GCN GEG GJT GRR GSO GSP GTF HNL HOU # ICT ILG ILM IND ISP JAN JAX JFK KOA LBB LEX LGA LGB LIH LIT LMT LNK MAF MBS # MFR MHT MIA MKE MLB MLI MOB MRY MSN MSP MSY OGG OKC OMA ONT ORD ORF PBI PHL # ..._

_# let's do some basic tabulation_ DestTable <- **sort** ( **table.ff** (dat$Dest), decreasing = TRUE) _# table is a generic, so shouldn't need explicit table.ff, # unless dat$Dest is not see as an ff object_

_# takes a while_

_# ORD ATL DFW LAX PHX DEN DTW IAH MSP_

_# 6638035 6094186 5745593 4086930 3497764 3335222 2997138 2889971 2765191_

17

_# STL EWR LAS CLT LGA BOS PHL PIT SLC # 2720250 2708414 2629198 2553157 2292800 2287186 2162968 2079567 2004414 # looks right - the busiest airports are ORD (O'Hare in Chicago) and ATL_ dat$DepDelay[1:50] _#opening ff /tmp/RtmpU5Uw6z/ffdf4e682d8cd893.ff # [1] 11 -1 11 -1 19 -2 -2 1 14 -1 5 16 17 1 21 3 13 -1 87 19 31 17 32 # [26] 29 26 15 5 54 0 25 -2 0 12 14 -1 2 1 16 15 44 20 15 3 21 -1 0_ **min.ff** (dat$DepDelay, na.rm = TRUE) _# [1] -1410_ **max.ff** (dat$DepDelay, na.rm = TRUE) _# [1] 2601 # why do I need to call min.ff and max.ff rather than min/max? # tmp <- clone(dat$DepDelay) # make a deep copy_

Let’s review our understanding of S3 methods. Why did I need to call _min.ff()_ rather than just simply calling _min()_ on the ff object? Could I have called _table()_ instead of _table.ff()_ ?

A note of caution. Debugging code involving _ff_ can be a hassle because the size gets in the way in various ways. Until you’re familiar with the various operations on ff objects, you’d be wise to try to run your code on a small test dataset loaded in as an ff object. Also, we want to be sure that the operations we use keep any resulting large objects in the _ff_ format and use _ff_ methods and not standard R functions.

#### **3.2.2 bigmemory**

The _bigmemory_ package is an alternative way to work with datasets in R that are kept stored on disk rather than read entirely into memory. _bigmemory_ provides a _big.matrix_ class, so it appears to be limited to datasets with a single type for all the variables. However, one nice feature is that one can use _big.matrix_ objects with _foreach_ (one of R’s parallelization tools, to be discussed soon) without passing a copy of the matrix to each worker. Rather the workers can access the matrix stored on disk.

18

#### **3.2.3 sqldf**

The _sqldf_ package provides the ability to use SQL queries on data frames (via _sqldf()_ ) as well as to filter an input CSV via an SQL query (via _read.csv.sql()_ ), with only the result of the subsetting put in memory in R. The full input data can be stored temporarily in an SQLite database on disk.

**require** (sqldf) _# read in file, with temporary database in memory_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **NULL** , header = TRUE)) _# read in file, with temporary database on disk_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **tempfile** (), header = TRUE))

### **3.3 dplyr package**

The _dplyr_ package is the successor to the _plyr_ package, providing plyr type functionality for data frames with enhancements for working with large tables and accessing databases (among other things). With _dplyr_ one can work with data stored in the _data.table_ format and in external databases.

_# with database_ cis <- **src_sqlite** ("/tmp/cis.db") authors <- **tbl** (cis, "authors") authors _# with data.table_ fileName <- '/tmp/AirlineDataAll.csv' flights <- **tbl_dt** ( **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6)))) _# now use dplyr functionality on 'authors' or 'flights' # example analysis_

19

**summarize** ( **group_by** (flights, UniqueCarrier), **mean** (DepDelay, na.rm=TRUE))

|_# Source: local data table [29 x 2]_|
|---|
|_#_|
|_#_<br>_UniqueCarrier mean(DepDelay, na.rm = TRUE)_|
|_#1_<br>_PS_<br>_8.928104_|
|_#2_<br>_TW_<br>_7.658251_|
|_#3_<br>_UA_<br>_9.667930_|
|_#4_<br>_WN_<br>_9.077167_|
|_#5_<br>_EA_<br>_8.674051_|
|_#6_<br>_HP_<br>_8.107790_|
|_#7_<br>_NW_<br>_6.007974_|
|_#8_<br>_PA (1)_<br>_5.532442_|
|_#9_<br>_PI_<br>_9.560336_|
|_#10_<br>_CO_<br>_7.695967_<br>_#.._<br>_..._<br>_..._|


### **3.4 Fitting models to big datasets: biglm**

The _biglm_ package provides the ability to fit large linear models and GLMs. _ffbase_ has a _bigglm.ffdf()_ function that builds on _biglm_ for use with _ffdf_ objects. Let’s fit a basic model on the airline data. Note that we’ll also fit the same model on the dataset when we use Spark at the end of the Unit.

**require** (ffbase) **require** (biglm)

datUse <- **subset** (dat, ArrDelay < 60*12 & ArrDelay > (-30) & ! **is.na** (ArrDelay) & ! **is.na** (Distance) & ! **is.na** (DayOfWeek)) datUse$Distance <- datUse$Distance / 1000 _# helps stabilize numerics # 119971791 records_

_# any concern about my model?_

**system.time** (mod <- **bigglm** (ArrDelay ~ Distance + DayOfWeek, data = datUse)) _# 542.149 11.248 550.779_ **summary** (mod)

20

coef <- **summary** (mod)$mat[,1]

Here are the results. Day 1 is Monday, so that’s the baseline category for the ANOVA-like part of the model.

Large data regression model: bigglm(DepDelay ~ Distance + DayOfWeek, data = Sample size = 119971791

||Coef|(95%|CI)|SE p|
|---|---|---|---|---|
|(Intercept)|6.3662|6.3504|6.3820|0.0079 0|
|Distance|0.7638|0.7538|0.7737|0.0050 0|
|DayOfWeek2|-0.6996|-0.7197|-0.6794|0.0101 0|
|DayOfWeek3|0.3928|0.3727|0.4129|0.0101 0|
|DayOfWeek4|2.2247|2.2046|2.2449|0.0101 0|
|DayOfWeek5|2.8867|2.8666|2.9068|0.0101 0|
|DayOfWeek6|-2.4273|-2.4481|-2.4064|0.0104 0|
|DayOfWeek7|-0.1362|-0.1566|-0.1158|0.0102 0|


Of course as good statisticians/data analysts we want to do careful assessment of our model, consideration of alternative models, etc. This is going to be harder to do with large datasets than with more manageable ones. However, one possibility is to do the diagnostic work on subsamples of the data.

Now let’s consider the fact that very small substantive effects can be highly statistically significant when estimated from a large dataset. In this analysis the data are generated from _Y ∼ N_ (0 + 0 _._ 001 _x,_ 1), so the _R_<sup>2</sup> is essentially zero.

n <- 150000000 _# n*4*8/1e6 Mb of RAM (~5 Gb) # but turns out to be 11 Gb as a text file_ nChunks <- 100 chunkSize <- n/nChunks **set.seed** (0)

**for** (p **in** 1:nChunks) { x1 <- **runif** (chunkSize) x2 <- **runif** (chunkSize) x3 <- **runif** (chunkSize)

21

y <- **rnorm** (chunkSize, .001*x1, 1) **write.table** ( **cbind** (y,x1,x2,x3), file = '/tmp/signif.csv', sep = ',', col.names = FALSE, row.names = FALSE, append = TRUE, quote = FALSE) } fileName <- '/tmp/signif.csv' **system.time** ( dat <- **read.csv.ffdf** (file = fileName, header = FALSE, colClasses = **rep** ('numeric', 4))) _# 922.213 18.265 951.204 -- timing is on an older machine than radagast_ **names** (dat) <- **c** ('y', 'x1','x2', 'x3') **ffsave** (dat, file = '/tmp/signif')

**system.time** ( **ffload** ('/tmp/signif')) _# 52.323 7.856 60.802 -- timing is on an older machine_ **system.time** (mod <- **bigglm** (y ~ x1 + x2 + x3, data = dat)) _# 1957.358 8.900 1966.644 -- timing is on an older machine_ **options** (digits = 12) **summary** (mod) _# R^2 on a subset (why can it be negative?)_ coefs <- **summary** (mod)$mat[,1] wh <- 1:1000000 1 - **sum** ((dat$y[wh] - coefs[1] + coefs[2]*dat$x1[wh] + coefs[3]*dat$x2[wh] + coefs[4]*dat$x3[wh])^2) / **sum** ((dat$y[wh] - **mean** (dat$y[wh]))^2)

Here are the results:

Large data regression model: bigglm(y ~ x1 + x2 + x3, data = dat) Sample size = 1.5e+08

22

Coef (95% CI) SE p (Intercept) -0.0001437 -0.0006601 0.0003727 0.0002582 0.5777919 x1 0.0013703 0.0008047 0.0019360 0.0002828 0.0000013 x2 0.0002371 -0.0003286 0.0008028 0.0002828 0.4018565 x3 -0.0002620 -0.0008277 0.0003037 0.0002829 0.3542728 ### and here is the R^2 calculation (why can it be negative?) [1] -1.111046828e-06

So, do I care the result is highly significant? Perhaps if I’m hunting the Higgs boson... As you have hopefully seen in statistics courses, statistical significance _̸_ = practical significance.

## **4 Sparsity**

A lot of statistical methods are based on sparse matrices. These include:

- Matrices representing the neighborhood structure (i.e., conditional dependence structure) of networks/graphs.

- Matrices representing autoregressive models (neighborhood structure for temporal and spatial data)

- A statistical method called the _lasso_ is used in high-dimensional contexts to give sparse results (sparse parameter vector estimates, sparse covariance matrix estimates)

- There are many others (I’ve been lazy here in not coming up with a comprehensive list, but trust me!)

When storing and manipulating sparse matrices, there is no need to store the zeros, nor to do any computation with elements that are zero. A few of you exploited sparse matrices in PS4.

R, Matlab and Python all have functionality for storing and computing with sparse matrices. We’ll see this a bit more in the linear algebra unit.

**require** (spam) mat = **matrix** ( **rnorm** (1e8), 1e4) mat[mat > (-2)] <- 0 sMat <- **as.spam** (mat) **print** ( **object.size** (mat), units = 'Mb') ## 762.9 Mb

23

**print** ( **object.size** (sMat), units = 'Mb') ## 26 Mb vec <- **rnorm** (1e4) **system.time** (mat %*% vec) ## user system elapsed ## 0.385 0.000 0.385 **system.time** (sMat %*% vec) ## user system elapsed ## 0.015 0.000 0.015

Here’s a blog post describing the use of sparse matrix manipulations for analysis of the Netflix Prize data.

## **5 Using statistical concepts to deal with computational bottlenecks**

As statisticians, we have a variety of statistical/probabilistic tools that can aid in dealing with big data.

1. Usually we take samples because we cannot collect data on the entire population. But we can just as well take a sample because we don’t have the ability to process the data from the entire population. We can use standard uncertainty estimates to tell us how close to the true quantity we are likely to be. And we can always take a bigger sample if we’re not happy with the amount of uncertainty.

2. There are a variety of ideas out there for making use of sampling to address big data challenges. One idea (due in part to Prof. Michael Jordan here in Statistics/EECS) is to compute estimates on many (relatively small) bootstrap samples from the data (cleverly creating a reduced-form version of the entire dataset from each bootstrap sample) and then combine the estimates across the samples. Here’s the arXiv paper on this topic.

3. Randomized algorithms: there has been a lot of attention recently to algorithms that make use of randomization. E.g., in optimizing a likelihood, you might choose the next step in the

24

optimization based on random subset of the data rather than the full data. Or in a regression context you might choose a subset of rows of the design matrix (the matrix of covariates) and corresponding observations, weighted based on the statistical leverage [recall the discussion of regression diagnostics in a regression course] of the observations. Here’s another arXiv paper that provides some ideas in this area.

## **6 Hadoop, MapReduce, and Spark**

Here we’ll talk about a fairly recent development in parallel computing. Traditionally, highperformance computing (HPC) has concentrated on techniques and tools for message passing such as MPI and on developing efficient algorithms to use these techniques.

### **6.1 Overview**

A basic paradigm for working with big datasets is the _MapReduce_ paradigm. The basic idea is to store the data in a distributed fashion across multiple nodes and try to do the computation in pieces on the data on each node. Results can also be stored in a distributed fashion.

A key benefit of this is that if you can’t fit your dataset on disk on one machine you can on a cluster of machines. And your processing of the dataset can happen in parallel. This is the basic idea of _MapReduce_ .

The basic steps of _MapReduce_ are as follows:

- read individual data objects (e.g., records/lines from CSVs or individual data files)

- map: create key-value pairs using the inputs (more formally, the map step takes a key-value pair and returns a new key-value pair)

- reduce - for each key, do an operation on the associated values and create a result - i.e., aggregate within the values assigned to each key

- write out the {key,result} pair

A similar paradigm that is being implemented in some R packages by Hadley Wickham is the split-apply-combine strategy (http://www.jstatsoft.org/v40/i01/paper).

_Hadoop_ is an infrastructure for enabling MapReduce across a network of machines. The basic idea is to hide the complexity of distributing the calculations and collecting results. Hadoop includes a file system for distributed storage (HDFS), where each piece of information is stored redundantly (on multiple machines). Calculations can then be done in a parallel fashion, often on data in place on each machine thereby limiting the amount of communication that has to be done over

25

the network. Hadoop also monitors completion of tasks and if a node fails, it will redo the relevant tasks on another node. Hadoop is based on Java but there are projects that allow R to interact with Hadoop, in particular _RHadoop_ and _RHipe_ . _Rhadoop_ provides the _rmr_ , _rhdfs_ , and _rhbase_ packages. For more details on _RHadoop_ see Adler and http://blog.revolutionanalytics.com/2011/09/mapreducehadoop-r.html.

Setting up a Hadoop cluster can be tricky. Hopefully if you’re in a position to need to use Hadoop, it will be set up for you and you will be interacting with it as a user/data analyst.

Ok, so what is Spark? You can think of Spark as in-memory Hadoop. Spark allows one to treat the memory across multiple nodes as a big pool of memory. So just as _data.table_ was faster than _ff_ because we kept everything in memory, Spark should be faster than Hadoop when the data will fit in the collective memory of multiple nodes. In cases where it does not, Spark will make use of the HDFS.

### **6.2 MapReduce and RHadoop**

Let’s see some examples of the MapReduce approach using R syntax of the sort one would use with _RHadoop_ . While we’ll use R syntax in the second piece of code below, the basic idea of what the map and reduce functions are is not specific to R. Note that using Hadoop with R may be rather slower than actually writing Java code for Hadoop.

First, let’s consider a basic word-counting example. Suppose we have many, many individual text documents distributed as individual files in the HDFS. Here’s pseudo code from Wikipedia. Here in the map function, the input {key,value} pair is the name of a document and the words in the document and the output {key, value} pairs are each word and the value 1. Then the reduce function takes each key (i.e., each word) and counts up the number of ones. The output {key, value} pair from the reduce step is the word and the count for that word.

function map(String name, String document):

- // name (key): document name

- // document (value): document contents

for each word w in document:

return (w, 1)

function reduce(String word, Iterator partialCounts):

- // word (key): a word

- // partialCounts (values): a list of aggregated partial counts sum = 0

for each pc in partialCounts:

26

sum += pc return (word, sum)

Now let’s consider an example where we calculate mean and standard deviation for the income of individuals in each state. Assume we have a large collection of CSVs, with each row containing information on an individual. _mapreduce()_ and _keyval()_ are functions in the _RHadoop_ package. I’ll assume we’ve written a separate helper function, _my_readline()_ , that manipulates individual lines from the CSVs.

**library** (rmr) mymap <- **function** (k, v) { record <- **my_readline** (v) key <- record[['state']] value <- record[['income']] **keyval** (key, value) } myreduce <- **function** (k, v){ **keyval** (k, **c** ( **length** (v), **mean** (v), **sd** (v))) } incomeResults <- **mapreduce** ( input = "incomeData", map = mymap, reduce = myreduce, combine = **NULL** , input.format = 'csv', output.format = 'csv') **from.dfs** (incomeResults, format = 'csv', structured = TRUE)

A few additional comments. In our map function, we could exclude values or transform them in some way, including producing multiple records from a single record. And in our reduce function, we can do more complicated analysis. So one can actually do fairly sophisticated things within what may seem like a restrictive paradigm. But we are constrained such that in the map step, each record needs to be treated independently and in the reduce step each key needs to be treated independently. This allows for the parallelization.

27

### **6.3 Spark**

We’ll focus on Spark rather than Hadoop for the speed reasons described above and because I think Spark provides a very nice environment in which to work. Plus it comes out of the AmpLab here at Berkeley. One downside is we’ll have to know a bit of Python to use it.

#### **6.3.1 Getting set up on Spark and the HDFS**

We’ll use Spark on an Amazon EC2 virtual cluster. Thankfully, Spark provides a Python-based script for setting up such a cluster. Occasionally the setup process goes awry but usually it’s pretty easy. We need our Amazon authentication keys as well as public-private keypair for SSH. **Make sure you don’t hard code your Amazon key information into any public file (including Github public repositories) - hackers will find the keys and use them to spin up instances, probably to mine bitcoin or send Spam; this happened in this class in 2014.**

We start by downloading the Spark package as a .tgz file (choosing the “source code” option) and untarring/zipping it. This all works from the VM. Also, on the SCF it’s available on the Linux machines at _/usr/local/src/pd/spark-1.4.0/spark-1.4.0/ec2_ .

export SPARK_VERSION=1.5.1 export CLUSTER_SIZE=12 # number of slave nodes export mycluster=sparkvm-paciorek # need unique name relative to other users

---

[← Unit 7: Databases and Big Data](01-unit-7-databases-and-big-data.md) · [Up: contents](index.md) · [I unzipped the Spark tarball to /usr/lib/spark via sudo on BCE cd /usr/lib/spark/ec2 →](03-i-unzipped-the-spark-tarball-to-usr-lib-spark-via-sudo-on-bc.md)
