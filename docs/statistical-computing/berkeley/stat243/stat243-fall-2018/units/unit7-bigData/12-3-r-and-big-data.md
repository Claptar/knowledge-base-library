---
title: 3 R and big data
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 R and big data

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There has been a lot of work in recent years to allow R to work with big datasets.

- The _data.table_ package provides for fast operations on large data tables in memory. The _dplyr_ package has also been optimized to work quickly on large data tables in memory, including operating on _data.table_ objects from the _data.table_ package.

- The _ff_ and _bigmemory_ packages provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R.

- The _biglm_ package provides the ability to fit linear models and GLMs to big datasets, with integration with _ff_ and _bigmemory_ .

- Finally the _sqldf_ package provides the ability to use SQL queries on R dataframes and onthe-fly when reading from CSV files. The latter can help you avoid reading in the entire dataset into memory in R if you just need a subset of it.

In this section we’ll use an example of US government data on airline delays (1987-2008) available through the ASA 2009 Data Expo at http://stat-computing.org/dataexpo/2009/the-data.html.

23

First we’ll use UNIX tools to download the individual yearly CSV files and make a single CSV (~12 Gb). (See the demo code file, _unit7-bigData.R_ , for the bash code.) Note that it’s much smaller when compressed (1.7 Gb) or if stored in a binary format. You can download a zipped version of the full CSV from http://www.stat.berkeley.edu/share/paciorek/AirlineDataAll.csv.zip.

### **3.1 Working quickly with big datasets in memory: data.table**

In many cases, particularly on a machine with a lot of memory, R might be able to read the dataset into memory but computations with the dataset may be slow.

The _data.table_ package provides a lot of functionality for fast manipulation: indexing, merges/joins, assignment, grouping, etc.

Let’s read in the airline dataset, specifying the column classes so that _fread()_ doesn’t have to detect what they are. I’ll also use factors since factors are represented numerically. It only takes about 5 minutes to read the data in. We’ll see in the next section that this is much faster than with other approaches within R.

**require** (data.table) dir = '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') dt <- **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6))) _#Read 123534969 rows and 29 (of 29) columns from # 11.203 GB file in 00:05:16_

**class** (dt) _# [1] "data.table" "data.frame"_

Now let’s do some basic subsetting. We’ll see that setting a key (which is how data.table refers to a database-style _index_ ) and using binary search can improve lookup speed dramatically.

**system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.8 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000))

24

_## 12.7 seconds_ **system.time** ( **setkey** (dt, Origin, Distance)) _## 33 seconds: ## takes some time, but will speed up later operations_ **tables** () _## NAME NROW MB ##[1,] dt 123,534,969 27334 ##[2,] sfo 2,733,910 606 ##[3,] sfoShort 1,707,171 379 ## COLS ##[1,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[2,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[3,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ## KEY ##[1,] Origin,Distance ##[2,] ##[3,] ##Total: 28,319MB ## vector scan_ **system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.5 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000 )) _## 12.4 seconds ## binary search_ **system.time** (sfo <- dt[ **.** ('SFO'), ]) _## 0.8 seconds_

Setting a key in _data.table_ simply amounts to sorting based on the columns provided, which allows for fast lookup later using binary search algorithms, as seen with the last query. From my fairly quick look through the _data.table_ documentation I don’t see a way to do the subsetting based on ranges of values (e.g., flights with distance less than 1000) using the specialized functionality of _data.table_ .

There’s a bunch more to _data.table_ and you’ll have to learn a modest amount of new syntax,

25

but if you’re working with large datasets in memory, it will probably be well worth your while. Plus _data.table_ objects are data frames (i.e., they inherit from data frames) so they are compatible with R code that uses dataframes.

### **3.2 Working with big datasets on disk: ff and bigmemory**

Note that with our 12 Gb dataset, the data took up 27 Gb of RAM on the SCF server _radagast_ . Operations on the dataset would then use up additional RAM. So this would not be feasible on most machines. And of course other datasets might be so big that even _radagast_ wouldn’t be able to hold them in memory.

#### **3.2.1 ff**

The _ff_ package stores datasets in columnar format, with one file per column, on disk, so is not limited by memory. It then provides fast access to the dataset from R.

If we need to work with a dataset in R but the dataset won’t fit in memory, we can read the data into R using the _ff_ package, in particular reading in as an _ffdf_ object. Note the arguments are similar to those for _read.{table,csv}()_ . _read.table.ffdf()_ reads the data in chunks.

**require** (ff) **require** (ffbase)

_# I put the data file on local disk on the machine I am using # (/tmp on radagast) # it's good to test with a small subset before # doing the full operations_ fileName <- **file.path** (dir, 'test.csv') dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4), 'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor','factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6)))

fileName <- '/tmp/AirlineDataAll.csv' **system.time** ( dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4),

26

'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor', 'factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6))) ) _## takes about 22 minutes_

**system.time** ( **ffsave** (dat, file = **file.path** (dir, 'AirlineDataAll'))) _## takes 11 minutes ## file is saved (in a binary format) as AirlineDataAll.ffData ## with metadata in AirlineDataAll.RData_ **rm** (dat) _# pretend we are in a new R session_

**system.time** ( **ffload** ( **file.path** (dir, 'AirlineDataAll'))) _# this is much quicker: # 107 seconds_

In the above operations, we wrote a copy of the file in the ff binary format that can be read more quickly back into R than the original reading of the CSV using _ffsave()_ and _ffload()_ . Also note the reduced size of the binary format file compared to the original CSV. It’s good to be aware of where the binary ff file is stored given that for large datasets, it will be large. With _ff_ (I think _bigmemory_ is different in how it handles this) it appears to be stored in _/tmp_ in an R temporary directory. Note that as we work with large files we need to be more aware of the filesystem, making sure in this case that _/tmp_ has enough space.

Let’s look at the _ff_ and _ffbase_ packages to see what functions are available using library(help=ff). Notice that there is an _merge.ff()_ .

Note that a copy of an _ff_ object does not appear to actually copy any data, but merely create another name referring to the same data object.

Next let’s do a bit of exploration of the dataset. Of course in a real analysis we’d do a lot more and some of this would take some time.

**ffload** ( **file.path** (dir, 'AirlineDataAll'))

_# [1] "tmp/RtmpU5Uw6z/ffdf4e684aecd7c4.ff" "tmp/RtmpU5Uw6z/ffdf4e687fb73a88.ff" # [3] "tmp/RtmpU5Uw6z/ffdf4e6862b1033f.ff" "tmp/RtmpU5Uw6z/ffdf4e6820053932.ff" # [5] "tmp/RtmpU5Uw6z/ffdf4e681e7d2235.ff" "tmp/RtmpU5Uw6z/ffdf4e686aa01c8.ff" # ..._

dat$Dest

27

_# ff (closed) integer length=123534969 (123534969) levels: BUR LAS LAX OAK # ABE ABQ ACV ALB ALO AMA ANC ATL AUS AVP AZO BDL BFL BGR BHM BIL BLI BNA BOI # CAK CCR CHS CID CLE CLT CMH CMI COS CPR CRP CRW CVG DAB DAL DAY DCA DEN DFW # EUG EVV EWR FAI FAR FAT FLG FLL FOE FSD GCN GEG GJT GRR GSO GSP GTF HNL HOU # ICT ILG ILM IND ISP JAN JAX JFK KOA LBB LEX LGA LGB LIH LIT LMT LNK MAF MBS # MFR MHT MIA MKE MLB MLI MOB MRY MSN MSP MSY OGG OKC OMA ONT ORD ORF PBI PHL # ..._

_# let's do some basic tabulation_ DestTable <- **sort** ( **table.ff** (dat$Dest), decreasing = TRUE) _# table is a generic, so shouldn't need explicit table.ff, # unless dat$Dest is not see as an ff object_

_# takes a while_

_# ORD ATL DFW LAX PHX DEN DTW IAH MSP # 6638035 6094186 5745593 4086930 3497764 3335222 2997138 2889971 2765191 # STL EWR LAS CLT LGA BOS PHL PIT SLC # 2720250 2708414 2629198 2553157 2292800 2287186 2162968 2079567 2004414 # looks right - the busiest airports are ORD (O'Hare in Chicago) and ATL_ dat$DepDelay[1:50] _#opening ff /tmp/RtmpU5Uw6z/ffdf4e682d8cd893.ff # [1] 11 -1 11 -1 19 -2 -2 1 14 -1 5 16 17 1 21 3 13 -1 87 19 31 17 32 # [26] 29 26 15 5 54 0 25 -2 0 12 14 -1 2 1 16 15 44 20 15 3 21 -1 0_

**min.ff** (dat$DepDelay, na.rm = TRUE) _# [1] -1410_ **max.ff** (dat$DepDelay, na.rm = TRUE) _# [1] 2601 # why do I need to call min.ff and max.ff rather than min/max?_

28

_# tmp <- clone(dat$DepDelay) # make an explicit copy_

Let’s review our understanding of S3 methods. Why did I need to call _min.ff()_ rather than just simply calling _min()_ on the ff object? Could I have called _table()_ instead of _table.ff()_ ?

A note of caution. Debugging code involving _ff_ can be a hassle because the size gets in the way in various ways. Until you’re familiar with the various operations on ff objects, you’d be wise to try to run your code on a small test dataset loaded in as an ff object. Also, we want to be sure that the operations we use keep any resulting large objects in the _ff_ format and use _ff_ methods and not standard R functions.

#### **3.2.2 bigmemory**

The _bigmemory_ package is an alternative way to work with datasets in R that are kept stored on disk rather than read entirely into memory. _bigmemory_ provides a _big.matrix_ class, so it appears to be limited to datasets with a single type for all the variables. However, one nice feature is that one can use _big.matrix_ objects with _foreach_ (one of R’s parallelization tools, to be discussed soon) without passing a copy of the matrix to each worker. Rather the workers can access the matrix stored on disk.

#### **3.2.3 sqldf**

The _sqldf_ package provides the ability to use SQL queries on data frames (via _sqldf()_ ) as well as to filter an input CSV via an SQL query (via _read.csv.sql()_ ), with only the result of the subsetting put in memory in R. The full input data can be stored temporarily in an SQLite database on disk.

**require** (sqldf) dir = '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') _# read in file, with temporary database in memory_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **NULL** , header = TRUE)) _# read in file, with temporary database on disk_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **tempfile** (), header = TRUE))

29

### **3.3 dplyr package**

You should already be familiar with using _dplyr._ One very nice feature is that with _dplyr_ one can work with data stored in the _data.table_ format, in external databases, and in Spark. There is also an extension to dplyr that allows for dplyr operations to be done in parallel.

**library** (dplyr) _## with database_ dir <- '../data' _# relative or absolute path to where the .db file is_ dbFilename <- 'stackoverflow-2016.db' db <- **src_sqlite** ( **file.path** (dir, dbFilename)) questions <- **tbl** (db, "questions") questions _## with data.table_ dir <- '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') flights <- **tbl_dt** ( **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6))))

_# now use dplyr functionality on 'flights'_

flights %>% **group_by** (UniqueCarrier) %>% **summarize** (mnDelay = **mean** (DepDelay, na.rm=TRUE)) _# Source: local data table [29 x 2] # # UniqueCarrier mean(DepDelay, na.rm = TRUE) #1 PS 8.928104 #2 TW 7.658251 #3 UA 9.667930 #4 WN 9.077167 #5 EA 8.674051_

30

_#6 HP 8.107790 #7 NW 6.007974 #8 PA (1) 5.532442 #9 PI 9.560336 #10 CO 7.695967 #.. ... ..._

### **3.4 Fitting models to big datasets: biglm**

The _biglm_ package provides the ability to fit large linear models and GLMs. _ffbase_ has a _bigglm.ffdf()_ function that builds on _biglm_ for use with _ffdf_ objects. Let’s fit a basic model on the airline data. Note that we’ll also fit the same model on the dataset when we use Spark at the end of the Unit.

**require** (ffbase) **require** (biglm)

dir = '/tmp' datUse <- **subset** (dat, ArrDelay < 60*12 & ArrDelay > (-30) & ! **is.na** (ArrDelay) & ! **is.na** (Distance) & ! **is.na** (DayOfWeek)) datUse$Distance <- datUse$Distance / 1000 _# helps stabilize numerics # 119971791 records_

_# any concern about my model?_ **system.time** (mod <- **bigglm** (ArrDelay ~ Distance + DayOfWeek, data = datUse)) _# 542.149 11.248 550.779_ **summary** (mod)

coef <- **summary** (mod)$mat[,1]

Here are the results. Day 1 is Monday, so that’s the baseline category for the ANOVA-like part of the model.

Large data regression model: bigglm(DepDelay ~ Distance + DayOfWeek, data = Sample size = 119971791

Coef (95% CI) SE p

31

|(Intercept)|6.3662|6.3504|6.3820|0.0079 0|
|---|---|---|---|---|
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

**for** (p **in** 1:nChunks) { x1 <- **runif** (chunkSize) x2 <- **runif** (chunkSize) x3 <- **runif** (chunkSize) y <- **rnorm** (chunkSize, .001*x1, 1) **write.table** ( **cbind** (y,x1,x2,x3), file = **file.path** (dir, 'signif.csv'), sep = ',', col.names = FALSE, row.names = FALSE, append = TRUE, quote = FALSE) } fileName <- **file.path** (dir, 'signif.csv') **system.time** ( dat <- **read.csv.ffdf** (file = fileName,

32

header = FALSE, colClasses = **rep** ('numeric', 4))) _# 922.213 18.265 951.204 -- timing is on an older machine than radagast_ **names** (dat) <- **c** ('y', 'x1','x2', 'x3') **ffsave** (dat, file = **file.path** (dir, 'signif'))

**system.time** ( **ffload** ( **file.path** (dir, 'signif'))) _# 52.323 7.856 60.802 -- timing is on an older machine_ **system.time** (mod <- **bigglm** (y ~ x1 + x2 + x3, data = dat)) _# 1957.358 8.900 1966.644 -- timing is on an older machine_ **options** (digits = 12) **summary** (mod) _# R^2 on a subset (why can it be negative?)_ coefs <- **summary** (mod)$mat[,1] wh <- 1:1000000 1 - **sum** ((dat$y[wh] - coefs[1] + coefs[2]*dat$x1[wh] + coefs[3]*dat$x2[wh] + coefs[4]*dat$x3[wh])^2) / **sum** ((dat$y[wh] - **mean** (dat$y[wh]))^2)

Here are the results:

Large data regression model: bigglm(y ~ x1 + x2 + x3, data = dat) Sample size = 1.5e+08

Coef (95% CI) SE p (Intercept) -0.0001437 -0.0006601 0.0003727 0.0002582 0.5777919 x1 0.0013703 0.0008047 0.0019360 0.0002828 0.0000013 x2 0.0002371 -0.0003286 0.0008028 0.0002828 0.4018565 x3 -0.0002620 -0.0008277 0.0003037 0.0002829 0.3542728 ### and here is the R^2 calculation (why can it be negative?) [1] -1.111046828e-06

So, do I care the result is highly significant? Perhaps if I’m hunting the Higgs boson... As you

have hopefully seen in statistics courses, statistical significance _̸_ = practical significance.

33

---

[← Unit 07 — bigData Part 11 —](11-unit-07-bigdata-part-11.md) · [Up: contents](index.md) · [4 Sparsity →](13-4-sparsity.md)
