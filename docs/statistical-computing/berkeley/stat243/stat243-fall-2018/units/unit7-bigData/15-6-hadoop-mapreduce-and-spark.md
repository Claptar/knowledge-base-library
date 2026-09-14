---
title: 6 Hadoop, MapReduce, and Spark
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Hadoop, MapReduce, and Spark

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Traditionally, high-performance computing (HPC) has concentrated on techniques and tools for message passing such as MPI and on developing efficient algorithms to use these techniques. In the last 20 years, focus has shifted to technologies for processing large datasets that are distributed across multiple machines, but can be manipulated as if they are one dataset.

### **6.1 Overview**

A basic paradigm for working with big datasets is the _MapReduce_ paradigm. The basic idea is to store the data in a distributed fashion across multiple nodes and try to do the computation in pieces on the data on each node. Results can also be stored in a distributed fashion.

A key benefit of this is that if you can’t fit your dataset on disk on one machine you can on a cluster of machines. And your processing of the dataset can happen in parallel. This is the basic idea of _MapReduce_ .

The basic steps of _MapReduce_ are as follows:

35

- read individual data objects (e.g., records/lines from CSVs or individual data files)

- map: create key-value pairs using the inputs (more formally, the map step takes a key-value pair and returns a new key-value pair)

- reduce - for each key, do an operation on the associated values and create a result - i.e., aggregate within the values assigned to each key

- write out the {key,result} pair

A similar paradigm that is implemented in _dplyr_ is the split-apply-combine strategy (http://www.jstatsoft.org/v40/i01/paper Note that the idea of concepts of map and reduce are core concepts in functional programming (and that we said R was a functional programming language). The various apply commands are a version of a map operation in base R.

_Hadoop_ is an infrastructure for enabling MapReduce across a network of machines. The basic idea is to hide the complexity of distributing the calculations and collecting results. Hadoop includes a file system for distributed storage (HDFS), where each piece of information is stored redundantly (on multiple machines). Calculations can then be done in a parallel fashion, often on data in place on each machine thereby limiting the amount of communication that has to be done over the network. Hadoop also monitors completion of tasks and if a node fails, it will redo the relevant tasks on another node. Hadoop is based on Java but there are projects that allow R to interact with Hadoop, in particular _RHadoop_ and _RHipe_ . _Rhadoop_ provides the _rmr_ , _rhdfs_ , and _rhbase_ packages. Given the popularity of Spark, I’m not sure how much usage these approaches currently see. For more details on _RHadoop_ see Adler and http://blog.revolutionanalytics.com/2011/09/mapreducehadoop-r.html.

Setting up a Hadoop cluster can be tricky. Hopefully if you’re in a position to need to use Hadoop, it will be set up for you and you will be interacting with it as a user/data analyst.

Ok, so what is Spark? You can think of Spark as in-memory Hadoop. Spark allows one to treat the memory across multiple nodes as a big pool of memory. So just as _data.table_ was faster than _ff_ because we kept everything in memory, Spark should be faster than Hadoop when the data will fit in the collective memory of multiple nodes. In cases where it does not, Spark will make use of the HDFS (and generally, Spark will be reading the data initially from HDFS.)

### **6.2 MapReduce and RHadoop**

Let’s see some examples of the MapReduce approach using R syntax of the sort one would use with _RHadoop_ . While we’ll use R syntax in the second piece of code below, the basic idea of what the map and reduce functions are is not specific to R. Note that using Hadoop with R may be rather slower than actually writing Java code for Hadoop.

36

First, let’s consider a basic word-counting example. Suppose we have many, many individual text documents distributed as individual files in the HDFS. Here’s pseudo code from Wikipedia. Here in the map function, the input {key,value} pair is the name of a document and the words in the document and the output {key, value} pairs are each word and the value 1. Then the reduce function takes each key (i.e., each word) and counts up the number of ones. The output {key, value} pair from the reduce step is the word and the count for that word.

function map(String name, String document): // name (key): document name // document (value): document contents for each word w in document: return (w, 1)

function reduce(String word, Iterator partialCounts): // word (key): a word // partialCounts (values): a list of aggregated partial counts sum = 0 for each pc in partialCounts: sum += pc return (word, sum)

Now let’s consider an example where we calculate mean and standard deviation for the income of individuals in each state. Assume we have a large collection of CSVs, with each row containing information on an individual. _mapreduce()_ and _keyval()_ are functions in the _RHadoop_ package. I’ll assume we’ve written a separate helper function, _my_readline()_ , that manipulates individual lines from the CSVs.

**library** (rmr) mymap <- **function** (k, v) { record <- **my_readline** (v) key <- record[['state']] value <- record[['income']] **keyval** (key, value) } myreduce <- **function** (k, v){

37

**keyval** (k, **c** ( **length** (v), **mean** (v), **sd** (v))) } incomeResults <- **mapreduce** ( input = "incomeData", map = mymap, reduce = myreduce, combine = **NULL** , input.format = 'csv', output.format = 'csv') **from.dfs** (incomeResults, format = 'csv', structured = TRUE)

A few additional comments. In our map function, we could exclude values or transform them in some way, including producing multiple records from a single record. And in our reduce function, we can do more complicated analysis. So one can actually do fairly sophisticated things within what may seem like a restrictive paradigm. But we are constrained such that in the map step, each record needs to be treated independently and in the reduce step each key needs to be treated independently. This allows for the parallelization.

### **6.3 Spark**

#### **6.3.1 Overview**

We’ll focus on Spark rather than Hadoop for the speed reasons described above and because I think Spark provides a very nice environment/interface in which to work. Plus it comes out of the (former) AmpLab here at Berkeley. We’ll start with the Python interface to Spark and then see a bit of the _sparklyr_ R package for interfacing with Spark.

More details on Spark are in the Spark programming guide. Some key aspects of Spark:

- Spark can read/write from various locations, but a standard location is the HDFS, with read/write done in parallel across the cores of the Spark cluster.

- The basic data structure in Spark is a _Resilient Distributed Dataset (RDD)_ , which is basically a distributed dataset of individual units, often individual rows loaded from text files.

- RDDs are stored in chunks called _partitions_ , stored on the different nodes of the cluster (either in memory or if necessary on disk).

38

- Spark has a core set of methods that can be applied to RDDs to do operations such as filtering/subsetting, transformation/mapping, reduction, and others.

- The operations are done in parallel on the different partitions of the data

- Some operations such as reduction generally involve a _shuffle_ , moving data between nodes of the cluster. This is costly.

- Recent versions of Spark have a distributed _DataFrame_ data structure and the ability to run SQL queries on the data.

Question: what do you think are the tradeoffs involved in determining the number of partitions to use?

Note that some headaches with Spark include:

- whether and how to set the amount of memory available for Spark workers (executor memory) and the Spark master process (driver memory)

- hard-to-diagnose failures (including out-of-memory issues)

#### **6.3.2 Getting started**

We’ll use Spark on Savio. You can also use Spark on NSF’s XSEDE Bridges supercomputer (among other XSEDE resources), and via commercial cloud computing providers, as well as on your laptop (but obviously only to experiment with small datasets). The demo works with a dataset of Wikipedia traffic, ~110 GB of zipped data (~500 GB unzipped) from October-December 2008, though for in-class presentation we’ll work with a much smaller set of 1 day of data.

The Wikipedia traffic are available through Amazon Web Services storage. The steps to get it are:

1. Start an AWS EC2 virtual machine that mounts the data onto the VM

2. Install Globus on the VM

3. Transfer the data to Savio via Globus

Details on how I did this are in _get_wikipedia_data.sh_ . The resulting data are available to you in _/global/scratch/paciorek/wikistats_full/raw_ on Savio.

39

#### **6.3.3 Storing data for use in Spark**

In many Spark contexts, the data would be stored in a distributed fashion across the hard drives attached to different nodes of a cluster (i.e., in the HDFS).

On Savio, Spark is set up to just use the scratch file system, so one would NOT run the code here, but I’m including it to give a sense for what it’s like to work with HDFS. First we would need to get the data from the standard filesystem to the HDFS. Note that the file system commands are like standard UNIX commands, but you need to do hadoop fs in front of the command.

_## DO NOT RUN THIS CODE ON SAVIO ## ## data for Spark on Savio is stored in scratch ##_ hadoop fs -ls / hadoop fs -ls /user hadoop fs -mkdir /user/paciorek/data hadoop fs -mkdir /user/paciorek/data/wikistats hadoop fs -mkdir /user/paciorek/data/wikistats/raw hadoop fs -mkdir /user/paciorek/data/wikistats/dated

hadoop fs -copyFromLocal /global/scratch/paciorek/wikistats/raw/* _\_ /user/paciorek/data/wikistats/raw

_# check files on the HDFS, e.g.:_ hadoop fs -ls /user/paciorek/data/wikistats/raw _## now do some processing with Spark, e.g., preprocess.{sh,py} # after processing can retrieve data from HDFS as needed_ hadoop fs -copyToLocal /user/paciorek/data/wikistats/dated .

#### **6.3.4 Using Spark on Savio**

Here are the steps to use Spark on Savio. We’ll demo using an interactive job (the _srun_ line here) but one could include the last three commands in the SLURM job script.

40

tmux new -s spark _## to get back in if disconnected: tmux a -t spark_

_## having some trouble with ic_stat243 and 4 nodes; check again_ srun -A ic_stat243 -p savio2 --nodes=4 -t 1:00:00 --pty bash module load java spark/2.1.0 python/3.5 source /global/home/groups/allhands/bin/spark_helper.sh spark-start _## note the environment variables created_ env | grep SPARK

spark-submit --master **$SPARK_URL $SPARK_DIR** /examples/src/main/python/pi.py

First we’ll load Python; then we can use Spark via the Python interface interactively. We’ll see how to submit batch jobs later.

_# PySpark using Python 3.5 (Spark 2.1.0 doesn’t support Python 3.6) # HASHSEED business has to do ensuring consistency across Python sessions_ pyspark --master **$SPARK_URL** --conf "spark.executorEnv.PYTHONHASHSEED=321" --executor-memory 60G

#### **6.3.5 Preprocessing the Wikipedia traffic data**

At this point, one complication is that the date-time information on the Wikipedia traffic is embedded in the file names. We’d like that information to be fields in the data files. This is done by running the code in _preprocess_wikipedia.py_ in the Python interface to Spark (pyspark). Note that trying to use multiple nodes and to repartition in various ways caused various errors I was unable to diagnose, but the code as is should work albeit somewhat slowly. The resulting data are available to you in _/global/scratch/paciorek/wikistats_full/dated_ . These are the data you will use for PS6.

In principle one could run _preprocess_wikipedia.py_ as a batch submission, but I was having problems getting that to run successfully.

#### **6.3.6 Spark in action: processing the Wikipedia traffic data**

Now we’ll do some basic manipulations with the Wikipedia dataset, with the goal of analyzing traffic to Barack Obama’s sites during the time around his election as president in 2008. Here are the steps we’ll follow:

41

- Count the number of lines/observations in our dataset.

- Filter to get only the Barack Obama sites.

- Map step that creates key-value pairs from each record/observation/row.

- Reduce step that counts the number of views by hour and language, so hour-day-lang will serve as the key.

- Map step to prepare the data so it can be output in a nice format.

Note that Spark uses _lazy evaluation_ . Actual computation only happens when one asks for a result to be returned or output written to disk.

First we’ll see how we read in the data and filter to the observations (lines / rows) of interest.

dir = ’/global/scratch/paciorek/wikistats’ _### read data and do some checks ### ## ’sc’ is the SparkContext management object, created via PySpark ## if you simply start Python, without invoking PySpark, ## you would need to create the SparkContext object yourself_ lines = sc. **textFile** (dir + ’/’ + ’dated’) lines. **getNumPartitions** () _# 16800 (480 input files) for full dataset # note delayed evaluation_ lines. **count** () _# 9467817626 for full dataset # watch the UI and watch wwall as computation progresses_ testLines = lines. **take** (10) testLines[0] testLines[9] _### filter to sites of interest ###_ **import** re **from** operator **import** add **def find** (line, regex = "Barack_Obama", language = **None** ): vals = line. **split** (’ ’) **if** len(vals) _<_ 6: **return** ( **False** ) tmp = re. **search** (regex, vals[3]) **if** tmp **is None or** (language != **None and** vals[2] != language): **return** ( **False** ) **else** :

42

**return** ( **True** ) lines.filter(find). **take** (100) _# pretty quick_

_# not clear if should repartition; will likely have small partitions if not # obama = lines.filter(find).repartition(480) # ∼ 18 minutes for full dataset (but remember lazy evaluation)_ obama = lines.filter(find) _# use this for demo in section_ obama. **count** () _# 433k observations for full dataset_

Now let’s use the mapReduce paradigm to get the aggregate statistics we want.

_### map-reduce step to sum hits across date-time-language triplets ###_ **def stratify** (line): _# create key-value pairs where: # key = date-time-language # value = number of website hits_ vals = line. **split** (’ ’) **return** (vals[0] + ’-’ + vals[1] + ’-’ + vals[2], int(vals[4])) _# sum number of hits for each date-time-language value_ counts = obama.map(stratify). **reduceByKey** (add) _# 5 minutes # 128889 for full dataset ### map step to prepare output ###_ **def transform** (vals): _# split key info back into separate fields_ key = vals[0]. **split** (’-’) **return** (",". **join** ((key[0], key[1], key[2], str(vals[1])))) _### output to file ### # have one partition because one file per partition is written out_ outputDir = dir + ’/’ + ’obama-counts’ counts.map(transform). **repartition** (1). **saveAsTextFile** (outputDir) _# 5 sec._

43

#### **6.3.7 Spark monitoring**

There are various interfaces to monitor Spark and the HDFS.

- http://<master_url>:8080 – general information about the Spark cluster

- http://<master_url>:4040 – information about the Spark tasks being executed

- http://<master_url>:50070 – information about the HDFS

When one runs _spark-start_ on Savio, it mentions some log files. If you look in the log file for the master, you should see a line that says “Bound MasterWebUI to 0.0.0.0 and started at http://10.0.5.93:8080” that indicates what the <master_url> is (here it is 10.0.5.93). We need to connect to that URL to view the web UI.

On Savio, to view the interfaces in a web browser, you need to start a remote desktop (VNC) session, following these instructions: https://research-it.berkeley.edu/services/high-performancecomputing/using-brc-visualization-node-realvnc; I suggest using the VNC add-on to the Chrome browser. Once you have a window onto Savio in your VNC session, start a browser from the terminal windows by entering: /global/scratch/kmuriki/otterbrowser <master_url>:8080, e.g. 10.0.5.93:8080.

#### **6.3.8 Spark operations**

Let’s consider some of the core methods we used.

- _filter()_ : create a subset

- _map()_ : take an RDD and apply a function to each element, returning an RDD

- _reduce()_ and _reduceByKey()_ : take an RDD and apply a reduction operation to the elements, doing the reduction stratified by the key values for reduceByKey(). Reduction functions need to be associative (order across records doesn’t matter) and commutative (order of arguments doesn’t matter) and take 2 arguments and return 1, all so that they can be done in parallel in a straightforward way.

- _collect()_ : collect results back to the master

- _cache()_ : tell Spark to keep the RDD in memory for later use

- _repartition()_ : rework the RDD so it is divided into the specified number of partitions

Note that all of the various operations are OOP methods applied to either the SparkContext management object or to a Spark dataset, called a Resilient Distributed Dataset (RDD). Here _lines, obama,_ and _counts_ are all RDDs. However the result of _collect()_ is just a standard Python object.

44

#### **6.3.9 Nonstandard reduction**

Finding the median of a set of values is an example where we don’t have a simple commutative/associative reducer function. Instead we group all the observations for each key into a socalled iterable object. Then our second map function treats each key as an element, iterating over the observations grouped within each key.

As an example we could find the median page size by language (this is not a particularly interesting/useful computation in this dataset, but I wanted to illustrate how this would work).

**import** numpy **as** np **def findShortLines** (line): vals = line. **split** (’ ’) **if** len(vals) _<_ 6: **return** ( **False** ) **else** : **return** ( **True** ) **def computeKeyValue** (line): vals = line. **split** (’ ’) _# key is language, val is page size_ **return** (vals[2], int(vals[5])) **def medianFun** (input): _# input[1] is an iterable object containing the page sizes for one key # this list comprehension syntax creates a list from the iterable object_ med = np. **median** ([val **for** val **in** input[1]]) _# input[0] is the key # return a tuple of the key and the median for that key_ **return** ((input[0], med)) output = lines.filter(findShortLines).map(computeKeyValue). **groupByKey** () medianResults = output.map(medianFun). **collect** ()

Note that because we need to aggregate all the data by key before doing the reduction on the full data in each key (which is actually just a ’map’ operation in this case once the data are already grouped by key), this is much slower than a reduce operation like max or mean.

45

#### **6.3.10 Spark DataFrames and SQL queries**

In recent versions of Spark, one can work with more structured data objects than RDDs. Spark now provides _DataFrames_ , which are collections of row and behave like distributed versions of R or Pandas dataframes. DataFrames seem to be taking the place of RDDs, at least for general, high-level use. They can also be queried using SQL syntax.

Here’s some example code for using DataFrames.

_### read the data in and process to create an RDD of Rows ###_ dir = ’/global/scratch/paciorek/wikistats’ lines = sc. **textFile** (dir + ’/’ + ’dated’) _### create DataFrame and do some operations on it ###_ **def remove_partial_lines** (line): vals = line. **split** (’ ’) **if** len(vals) _<_ 6: **return** ( **False** ) **else** : **return** ( **True** ) **def create_df_row** (line): p = line. **split** (’ ’) **return** (int(p[0]), int(p[1]), p[2], p[3], int(p[4]), int(p[5])) tmp = lines.filter(remove_partial_lines).map(create_df_row) _## ’sqlContext’ is the Spark sqlContext management object, created via PySpark ## if you simply start Python without invoking PySpark, ## you would need to create the sqlContext object yourself_ df = sqlContext. **createDataFrame** (tmp, schema = ["date", "hour", "lang", "site", "hits", "size"]) df. **printSchema** () _## note similarity to dplyr and R/Pandas dataframes_ df. **select** (’site’). **show** () df.filter(df[’lang’] == ’en’). **show** () df. **groupBy** (’lang’). **count** (). **show** ()

And here’s how we use SQL with a DataFrame:

46

_### use SQL with a DataFrame ###_ df. **registerTempTable** ("wikiHits") _# name of ’SQL’ table is ’wikiHits’_ subset = sqlContext. **sql** ("SELECT * FROM wikiHits WHERE lang = ’en’ AND site LIKE ’%Barack_Obama%’") subset. **take** (5)

_# [Row(date=20081022, hits=17, hour=230000, lang=u’en’, size=145491), Row(date=20081026, hits=41, hour=220000, lang=u’en’, site=u’Public_image_of_Barack_Obama’, size=1256906), Row(date=20081112, hits=8, hour=30000, lang=u’en’, site=u’Electoral_history_of_Barack_Obama’, size=141176), Row(date=20081104, hits=13890, hour=110000, lang=u’en’, site=u’Barack_Obama’, size=2291741206), Row(date=20081104, hits=6, hour=110000, lang=u’en’, site=u’Barack_Obama%2C_Sr.’, size=181699)]_ langSummary = sqlContext. **sql** ("SELECT lang, count(*) as n FROM wikiHits GROUP BY lang ORDER BY n desc limit 20") _# 38 minutes_ results = langSummary. **collect** () _# [Row(lang=u’en’, n=3417350075), Row(lang=u’de’, n=829077196), Row(lang=u’ja’, n=734184910), Row(lang=u’fr’, n=466133260), Row(lang=u’es’, n=425416044), Row(lang=u’pl’, n=357776377), Row(lang=u’commons.m’, n=304076760), Row(lang=u’it’, n=300714967), Row(lang=u’ru’, n=256713029), Row(lang=u’pt’, n=212763619), Row(lang=u’nl’, n=194924152), Row(lang=u’sv’, n=105719504), Row(lang=u’zh’, n=98061095), Row(lang=u’en.d’, n=81624098), Row(lang=u’fi’, n=80693318), Row(lang=u’tr’, n=73408542), Row(lang=u’cs’, n=64173281), Row(lang=u’no’, n=48592766), Row(lang=u’he’, n=46986735), Row(lang=u’ar’, n=46968973)]_

#### **6.3.11 Analysis results**

The file _obama_plot.R_ does some manipulations to plot the hits as a function of time, shown here:

47


<!-- Start of picture text -->
1008 1028 1117 1207 1227<br>time<br>G<br>G<br>G<br>GGGGG<br>G GG<br>G G GG<br>GG GGGG GGGGGG<br>GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG<br>1103 1105 1107 1109<br>time<br>250000<br>hits 100000<br>0<br>250000<br>hits<br>100000<br>0<br><!-- End of picture text -->

_Figure 1. Obama Wikipedia traffic results._

So there you have it – from big data (500 GB unzipped) to knowledge (a 17 KB file of plots).

#### **6.3.12 Other comments**

**Running a batch Spark job** We can run a Spark job using Python code as a batch script rather than interactively. Here’s an example, which computes the value of Pi by Monte Carlo simulation.

<mark>spark-submit --master</mark> **<mark>$SPARK_URL $SPARK_DIR</mark>** <mark>/examples/src/main/pyth</mark> on/pi.py

The file _example_spark_job.sh_ is an example SLURM job submission script that runs the PySpark code in _test_batch.py_ . If you want to run a Spark job as a batch submission to the scheduler you can follow that example, submitting the job using _sbatch_ : sbatch name_of_job_script.sh.

**Python vs. Scala/Java** Spark is implemented natively in Java and Scala, so all calculations in Python involve taking Java data objects converting them to Python objects, doing the calculation,

48

and then converting back to Java. This process is called serialization and takes time, so the speed when implementing your work in Scala (or Java) may be faster. Here’s a http://apache-spark-userlist.1001560.n3.nabble.com/Scala-vs-Python-performance-differences-td4247.html on that.

#### **6.3.13 R interfaces to Spark**

Both _SparkR_ (from the Spark folks) and _sparklyr_ (from the RStudio folks) allow you to interact with Spark-based data from R. There are some limitations to what you can do (both in what is possible and in what will execute with reasonable speed), so for heavy use of Spark you may want to use Python or even the Scala or Java interfaces. We’ll focus on _sparklyr_ .

With _sparklyr_ , you can:

- use _dplyr_ functionality

- use distributed apply computations via _spark_apply()_ .

There are some limitations though:

- the _dplyr_ functionality translates operations to SQL so there are limited operations one can do, particularly in terms of computations on a given row of data.

- _spark_apply()_ appears to run very slowly, presumably because data is being serialized back and forth between R and Java data structures.

#### **6.3.14 sparklyr example**

Here’s some example code that works on Savio. One important note is that if you don’t adjust the memory, you’ll get obscure Java errors that occur because Spark runs out of memory, and this is only clear if you look in the right log files in the directory $SPARK_LOG_DIR.

_## see unit8-bigData.sh for starting Spark ## also invoke: ## module load r r-packages ## local installation on your own computer_ **if** (! **require** (sparklyr)) { **install.packages** ("sparklyr") _# spark_install() ## if spark not already installed_ }

49

_### connect to Spark ### ## need to increase memory otherwise get hard-to-interpret Java ## errors due to running out of memory; total memory on the node is 64 GB_ conf <- **spark_config** () conf$spark.driver.memory <- "8G" conf$spark.executor.memory <- "50G" _# sc <- spark_connect(master = "local") # if doing on laptop_ sc <- **spark_connect** (master = **Sys.getenv** ("SPARK_URL"), config = conf) _# non-local_

_### read data in ###_ cols <- **c** (date = 'numeric', hour = 'numeric', lang = 'character', page = 'character', hits = 'numeric', size = 'numeric') _## takes a while even with only 1.4 GB (zipped) input data (100 sec.)_ wiki <- **spark_read_csv** (sc, "wikistats", "/global/scratch/paciorek/wikistats/dated", header = FALSE, delimiter = ' ', columns = cols, infer_schema = FALSE)

**head** (wiki) **class** (wiki) **dim** (wiki) _# not all operations work on a spark dataframe ### some dplyr operations on the Spark dataset ###_ **library** (dplyr) wiki_en <- wiki %>% **filter** (lang == "en") **head** (wiki_en) table <- wiki %>% **group_by** (lang) %>% **summarize** (count = **n** ()) %>%

50

**arrange** ( **desc** (count)) _## note the lazy evaluation: need to look at table to get computation to run_ table **dim** (table) **class** (table) _### distributed apply ### ## need to use spark_apply to carry out arbitrary R code ## the function transforms a dataframe partition into a dataframe ## see help(spark_apply) ## ## however this is _very_ slow, probably because it involves ## serializing objects between java and R_ wiki_plus <- **spark_apply** (wiki, **function** (data) { data$obama = stringr:: **str_detect** (data$page, "Barack_Obama") data }, columns = **c** ( **colnames** (wiki), 'obama')) obama <- **collect** (wiki_plus %>% **filter** (obama)) _### SQL queries ###_ **library** (DBI) _## reference the Spark table (see spark_read_csv arguments) ## not the R tbl_spark interface object_ wiki_en2 <- **dbGetQuery** (sc, "SELECT * FROM wikistats WHERE lang = 'en' LIMIT 10") wiki_en2

51

---

[← 5 Using statistical concepts to deal with computational bottlenecks](14-5-using-statistical-concepts-to-deal-with-computational-bott.md) · [Up: contents](index.md)
