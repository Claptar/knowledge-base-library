---
title: Unit 08 — bigData Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 05 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

output = lines.filter(findShortLines).map(computeKeyValue).groupByKey() medianResults = output.map(medianFun).collect()

18

Note that because we need to aggregate all the data by key before doing the reduction on the full data in each key (which is actually just a ’map’ operation in this case once the data are already grouped by key), this is much slower than a reduce operation like max or mean.

#### **2.3.10 Spark DataFrames and SQL queries**

In recent versions of Spark, one can work with more structured data objects than RDDs. Spark now provides _DataFrames_ , which are collections of row and behave like distributed versions of R or Pandas dataframes. DataFrames seem to be taking the place of RDDs, at least for general, high-level use. They can also be queried using SQL syntax.

Here’s some example code for using DataFrames.

### read the data in and process to create an RDD of Rows ### dir = '/global/scratch/paciorek/wikistats' lines = sc.textFile(dir + '/' + 'dated') ### create DataFrame and do some operations on it ###

def remove_partial_lines(line): vals = line.split(' ') if len(vals) < 6: return(False) else: return(True) def create_df_row(line): p = line.split(' ') return(int(p[0]), int(p[1]), p[2], p[3], int(p[4]), int(p[5]))

tmp = lines.filter(remove_partial_lines).map(create_df_row)

## 'sqlContext' is the Spark sqlContext management object, created via PySpark ## if you simply start Python without invoking PySpark, ## you would need to create the sqlContext object yourself

19

df = sqlContext.createDataFrame(tmp, schema = ["date", "hour", "lang", "site", df.printSchema()

## note similarity to dplyr and R/Pandas dataframes df.select('site').show() df.filter(df['lang'] == 'en').show() df.groupBy('lang').count().show()

And here’s how we use SQL with a DataFrame:

### use SQL with a DataFrame ### df.registerTempTable("wikiHits") # name of 'SQL' table is 'wikiHits' subset = sqlContext.sql("SELECT * FROM wikiHits WHERE lang = 'en' AND site subset.take(5) # [Row(date=20081022, hits=17, hour=230000, lang=u'en', langSummary = sqlContext.sql("SELECT lang, count(*) as n FROM wikiHits GROUP results = langSummary.collect() # [Row(lang=u'en', n=3417350075), Row(lang=u'de', n=829077196), Row(lang=u'ja',

#### **2.3.11 Other comments**

**Running a batch Spark job** We can run a Spark job using Python code as a batch script rather than interactively. Here’s an example, which computes the value of Pi by Monte Carlo simulation.

<mark>spark-submit --master $SPARK_URL $SPARK_DIR/examples/src/main/pyth</mark> on/pi.py

The file _example_spark_job.sh_ is an example SLURM job submission script that runs the PySpark code in _test_batch.py_ . If you want to run a Spark job as a batch submission to the scheduler you can follow that example, submitting the job using _sbatch_ : sbatch name_of_job_script.sh.

20

**Python vs. Scala/Java** Spark is implemented natively in Java and Scala, so all calculations in Python involve taking Java data objects converting them to Python objects, doing the calculation, and then converting back to Java. This process is called serialization and takes time, so the speed when implementing your work in Scala (or Java) may be faster. Here’s a http://apache-spark-userlist.1001560.n3.nabble.com/Scala-vs-Python-performance-differences-td4247.html on that.

#### **2.3.12 R interfaces to Spark**

Both _SparkR_ (from the Spark folks) and _sparklyr_ (from the RStudio folks) allow you to interact with Spark-based data from R. There are some limitations to what you can do (both in what is possible and in what will execute with reasonable speed), so for heavy use of Spark you may want to use Python or even the Scala or Java interfaces. We’ll focus on _sparklyr_ .

With _sparklyr_ , you can:

- use _dplyr_ functionality

- use distributed apply computations via _spark_apply()_ .

There are some limitations though:

- the _dplyr_ functionality translates operations to SQL so there are limited operations one can do, particularly in terms of computations on a given row of data.

- _spark_apply()_ appears to run very slowly, presumably because data is being serialized back and forth between R and Java data structures.

#### **2.3.13 sparklyr example**

Here’s some example code that works on Savio. One important note is that if you don’t adjust the memory, you’ll get obscure Java errors that occur because Spark runs out of memory, and this is only clear if you look in the right log files in the directory $SPARK_LOG_DIR.

_## see unit8-bigData.sh for starting Spark ## also invoke: ## module load r r-packages ## local installation on your own computer_ **if** (! **require** (sparklyr)) { **install.packages** ("sparklyr") _# spark_install() ## if spark not already installed_

21

} _### connect to Spark ###_

_## need to increase memory otherwise get hard-to-interpret Java ## errors due to running out of memory; total memory on the node is 64 GB_ conf <- **spark_config** () conf$spark.driver.memory <- "8G" conf$spark.executor.memory <- "50G" _# sc <- spark_connect(master = "local") # if doing on laptop_ sc <- **spark_connect** (master = **Sys.getenv** ("SPARK_URL"), config = conf) _# non-local ### read data in ###_ cols <- **c** (date = 'numeric', hour = 'numeric', lang = 'character', page = 'character', hits = 'numeric', size = 'numeric') _## takes a while even with only 1.4 GB (zipped) input data (100 sec.)_ wiki <- **spark_read_csv** (sc, "wikistats",

"/global/scratch/paciorek/wikistats/dated", header = FALSE, delimiter = ' ', columns = cols, infer_schema = FALSE)

**head** (wiki) **class** (wiki) **dim** (wiki) _# not all operations work on a spark dataframe ### some dplyr operations on the Spark dataset ###_ **library** (dplyr)

wiki_en <- wiki %>% **filter** (lang == "en") **head** (wiki_en)

22

table <- wiki %>% **group_by** (lang) %>% **summarize** (count = **n** ()) %>% **arrange** ( **desc** (count)) _## note the lazy evaluation: need to look at table to get computation to run_ table **dim** (table) **class** (table) _### distributed apply ### ## need to use spark_apply to carry out arbitrary R code ## the function transforms a dataframe partition into a dataframe ## see help(spark_apply) ## ## however this is _very_ slow, probably because it involves ## serializing objects between java and R_ wiki_plus <- **spark_apply** (wiki, **function** (data) { data$obama = stringr:: **str_detect** (data$page, "Barack_Obama") data }, columns = **c** ( **colnames** (wiki), 'obama'))

obama <- **collect** (wiki_plus %>% **filter** (obama))

_### SQL queries ###_

**library** (DBI) _## reference the Spark table (see spark_read_csv arguments) ## not the R tbl_spark interface object_ wiki_en2 <- **dbGetQuery** (sc, "SELECT * FROM wikistats WHERE lang = 'en' LIMIT 10") wiki_en2

_##################################################### # 3: Databases_

_#####################################################_

23

_<mark>### 3.5 Accessing databases in R</mark>_

## **3 Databases**

This material is drawn from the tutorial on “Working with large datasets in SQL, R, and Python”, though I won’t hold you responsible for all of the database/SQL material in that tutorial, only what appears here in this Unit.

### **3.1 Overview**

Basically, standard SQL databases are _relational_ databases that are a collection of rectangular format datasets ( _tables_ , also called _relations_ ), with each table similar to R or Pandas data frames, in that a table is made up of columns, which are called _fields_ or _attributes_ , each containing a single _type_ (numeric, character, date, currency, enumerated (i.e., categorical), ...) and rows or records containing the observations for one entity. Some of the tables in a given database will generally have fields in common so it makes sense to merge (i.e., join) information from multiple tables. E.g., you might have a database with a table of student information, a table of teacher information and a table of school information, and you might join student information with information about the teacher(s) who taught the students. Databases are set up to allow for fast querying and merging (called joins in database terminology).

Formally, databases are stored on disk, while R and Python store datasets in memory. This would suggest that databases will be slow to access their data but will be able to store more data than can be loaded into an R or Python session. However, databases can be quite fast due in part to disk caching by the operating system as well as careful implementation of good algorithms for database operations. For more information about disk caching see the tutorial.

### **3.2 Interacting with a database**

You can interact with databases in a variety of database systems ( _DBMS_ =database management system). Some popular systems are SQLite, MySQL, PostgreSQL, Oracle and Microsoft Access. We’ll concentrate on accessing data in a database rather than management of databases. SQL is the Structured Query Language and is a special-purpose high-level language for managing databases and making queries. Variations on SQL are used in many different DBMS.

Queries are the way that the user gets information (often simply subsets of tables or information merged across tables). The result of an SQL query is in general another table, though in some cases it might have only one row and/or one column.

24

Many DBMS have a client-server model. Clients connect to the server, with some authentication, and make requests (i.e., queries).

There are often multiple ways to interact with a DBMS, including directly using command line tools provided by the DBMS or via Python or R, among others.

We’ll concentrate on SQLite (because it is simple to use on a single machine). SQLite is quite nice in terms of being self-contained - there is no server-client model, just a single file on your hard drive that stores the database and to which you can connect to using the SQLite shell, R, Python, etc. However, it does not have some useful functionality that other DBMS have. For example, you can’t use ALTER TABLE to modify column types or drop columns.

### **3.3 Database schema and normalization**

To truly leverage the conceptual and computational power of a database you’ll want to have your data in a normalized form, which means spreading your data across multiple tables in such a way that you don’t repeat information unnecessarily.

The schema is the metadata about the tables in the database and the fields (and their types) in those tables.

Let’s consider this using an educational example. Suppose we have a school with multiple teachers teaching multiple classes and multiple students taking multiple classes. If we put this all in one table organized per student, the data might have the following fields:

- student ID

- student grade level

- student name

- class 1

- class 2

-

- class n

- grade in class 1

- grade in class 2

- ...

- grade in class n

25

- teacher ID 1

- teacher ID 2

-

- teacher ID n

- teacher name 1

- teacher name 2

-

- teacher name n

- teacher department 1

- teacher department 2

- ...

- teacher department n

- teacher age 1

- teacher age 2

- ...

- teacher age n

There are a lot of problems with this. We’ll list some in class:

1. ???

2. ???

3. ???

4. ???

It would get even worse if there was a field related to teachers for which a given teacher could have multiple values (e.g., teachers could be in multiple departments). This would lead to even more redundancy - each student-class-teacher combination would be crossed with all of the departments for the teacher (so-called multivalued dependency in database theory).

An alternative organization of the data would be to have each row represent the enrollment of a student in a class.

26

- student ID

- student name

- class

- grade in class

- student grade level

- teacher ID

- teacher department

- teacher age

This has some advantages relative to our original organization in terms of not having empty data slots, but it doesn’t solve the other three issues above.

Instead, a natural way to order this database is with the following tables.

- Student

   - ID

   - name

   - grade_level

- Teacher

   - ID

   - name

   - department

   - age

- Class

   - ID

   - topic

   - class_size

   - teacher_ID

27

- ClassAssignment

   - student_ID

   - class_ID

   - grade

Then we do queries to pull information from multiple tables. We do the joins based on _keys_ , which are the fields in each table that allow us to match rows from different tables.

(That said, if all anticipated uses of a database will end up recombining the same set of tables, we may want to have a denormalized schema in which those tables are actually combined in the database. It is possible to be too pure about normalization! We can also create a virtual table, called a _view_ , as discussed later.)

#### **3.3.1 Keys**

A _key_ is a field or collection of fields that give(s) a unique value for every row/observation. A table in a database should then have a _primary key_ that is the main unique identifier used by the DBMS. _Foreign keys_ are columns in one table that give the value of the primary key in another table. When information from multiple tables is joined together, the matching of a row from one table to a row in another table is generally done by equating the primary key in one table with a foreign key in a different table.

In our educational example, the primary keys would presumably be: _Student.ID_ , _Teacher.ID_ , _Class.ID_ , and for ClassAssignment two fields: _{ClassAssignment.studentID, ClassAssignment.class_ID}_ . Some examples of foreign keys would be:

- student_ID as the foreign key in ClassAssignment for joining with Student on Student.ID

- teacher_ID as the foreign key in Class for joining with Teacher based on Teacher.ID

- class_ID as the foreign key in ClassAssignment for joining with Class based on Class.ID

#### **3.3.2 Queries that join data across multiple tables**

Suppose we want a result that has the grades of all students in 9th grade. For this we need information from the Student table (to determine grade level) and information from the ClassAssignment table (to determine the class grade). More specifically we need a query that joins _Student_ with _ClassAssignment_ based on _Student.ID_ and _ClassAssignment.student_ID_ and filters the rows based on _Student.grade_level_ :

SELECT Student.ID, grade FROM Student, ClassAssignment WHERE

28

Student.ID = ClassAssignment.student_ID and Student.grade_level = 9;

Note that the query is a _join_ (specifically an _inner join_ ), which is like _merge()_ in R. We don’t specifically use the JOIN keyword, but one could do these queries explicitly using JOIN, as we’ll see later.

### **3.4 Stack Overflow metadata example**

I’ve obtained data from Stack Overflow, the popular website for asking coding questions, and placed it into a normalized database. The SQLite version has metadata (i.e., it lacks the actual text of the questions and answers) on all of the questions and answers posted in 2016.

We’ll explore SQL functionality using this example database.

Now let’s consider the Stack Overflow data. Each question may have multiple answers and each question may have multiple (topic) tags.

If we tried to put this into a single table, the fields could look like this if we have one row per question:

- question ID

- ID of user submitting question

- question title

- tag 1

- tag 2

- ...

- tag n

- answer 1 ID

- ID of user submitting answer 1

- age of user submitting answer 1

- name of user submitting answer 1

- answer 2 ID

- ID of user submitting answer 2

29

- age of user submitting answer 2

- name of user submitting answer 2

- ...

or like this if we have one row per question-answer pair:

- question ID

- ID of user submitting question

- question title

- tag 1

- tag 2

- ...

- tag n

- answer ID

- ID of user submitting answer

- age of user submitting answer

- name of user submitting answer

As we’ve discussed neither of those schema is particularly desirable.

**Challenge** : How would you devise a schema to normalize the data. I.e., what set of tables do you think we should create?

You can view one reasonable schema in the file _normalized_example.png_ . The lines between tables indicate the relationship of foreign keys in one table to primary keys in another table. The schema in the actual databases of Stack Overflow data we’ll use in this tutorial is similar to but not identical to that.

You can download a copy of the SQLite version of the Stack Overflow 2016 database from http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2016.db.

30

### **3.5 Accessing databases in R**

The _DBI_ package provides a front-end for manipulating databases from a variety of DBMS (SQLite, MySQL, PostgreSQL, among others). Basically, you tell the package what DBMS is being used on the back-end, link to the actual database, and then you can use the standard functions in the package regardless of the back-end. This is a similar style to how one uses _foreach_ for parallelization.

With SQLite, R processes make calls against the stand-alone SQLite database (.db) file, so there are no SQLite-specific processes. With a client-server DBMS like PostgreSQL, R processes call out to separate Postgres processes; these are started from the overall Postgres background process

You can access and navigate an SQLite database from R as follows.

**library** (RSQLite) drv <- **dbDriver** ("SQLite") dir <- '../data' _# relative or absolute path to where the .db file is_ dbFilename <- 'stackoverflow-2016.db'

db <- **dbConnect** (drv, dbname = **file.path** (dir, dbFilename))

|_# _|_simple query _|_to get 5 rows from a table_||
|---|---|---|---|
|**db**|**GetQuery**(db,|"select * from questions limit|5")|
|##|questionid|creationdate score vie|wcount|
|##|1<br>34552550|2016-01-01 00:00:03<br>0|108|
|##|2<br>34552551|2016-01-01 00:00:07<br>1|151|
|##|3<br>34552552|2016-01-01 00:00:39<br>2|1942|
|##|4<br>34552554|2016-01-01 00:00:50<br>0|153|
|##|5<br>34552555|2016-01-01 00:00:51<br>-1|54|
|##||||
|##|1||Scope b|
|##|2<br>Rails|- Unknown Attribute - Unable|to add a new field to a form on|
|##|3 Selenium F|irefox webdriver won't load a|blank page after changing Firef|
|##|4||Android Studio st|
|##|5|Java: reference|to non-finial local variables i|
|##|ownerid|||
|##|1 5684416|||
|##|2 2457617|||
|##|3 5732525|||
|##|4 5735112|||


31

<mark>## 5 4646288</mark>

#### We can easily see the tables and their fields:

**dbListTables** (db)

## [1] "answers" "questions" "questions_tags" "users" **dbListFields** (db, "questions") ## [1] "questionid" "creationdate" "score" "viewcount" ## [5] "title" "ownerid" **dbListFields** (db, "answers") ## [1] "answerid" "questionid" "creationdate" "score" ## [5] "ownerid"

Here’s how to make a basic SQL query. One can either make the query and get the results in one go or make the query and separately fetch the results. Here we’ve selected the first five rows (and all columns, based on the * wildcard) and brought them into R as a data frame.

results <- **dbGetQuery** (db, 'select * from questions limit 5') **class** (results)

## [1] "data.frame"

query <- **dbSendQuery** (db, "select * from questions") results2 <- **fetch** (query, 5) **identical** (results, results2) ## [1] TRUE **dbClearResult** (query) _# clear to prepare for another query_

To disconnect from the database:

**<mark>dbDisconnect</mark>** <mark>(db)</mark>

32

### **3.6 Basic SQL for choosing rows and columns from a table**

SQL is a declarative language that tells the database system what results you want. The system then parses the SQL syntax and determines how to implement the query.

Here are some examples using the Stack Overflow database.

_## find the largest viewcounts in the questions table_ **dbGetQuery** (db,

'select distinct viewcount from questions order by viewcount desc limit 10')

|##|view|c|ount|
|---|---|---|---|
|##|1<br>1|9|6469|
|##|2<br>1|7|4790|
|##|3<br>1|3|4399|
|##|4<br>1|2|9874|
|##|5<br>1|2|9624|
|##|6<br>1|2|7764|
|##|7<br>1|2|6752|
|##|8<br>1|1|2000|
|##|9<br>1|0|9422|
|##|10<br>1|0|6995|


_## now get the questions that are viewed the most_ **dbGetQuery** (db, 'select * from questions where viewcount > 100000')

|##||questionid|cre|ationdate score|viewcount|
|---|---|---|---|---|---|
|##|1|34579099|2016-01-03|16:55:16<br>8|129624|
|##|2|34814368|2016-01-15|15:24:36<br>206|134399|
|##|3|35062852|2016-01-28|13:28:39<br>730|112000|
|##|4|35429801|2016-02-16|10:21:09<br>400|100125|
|##|5|35588699|2016-02-23|21:37:06<br>57|126752|
|##|6|35890257|2016-03-09|11:25:05<br>51|129874|
|##|7|35990995|2016-03-14|15:01:17<br>104|127764|
|##|8|36668374|2016-04-16|18:57:19<br>20|196469|
|##|9|37280274|2016-05-17|15:21:49<br>23|106995|
|##|10|37806538|2016-06-14|08:16:21<br>223|174790|
|##|11|37937984|2016-06-21|07:23:00<br>202|109422|
|##||||||


33

|##|1|Fatal error|
|---|---|---|
|##|2||
|##|3||
|##|4||
|##|5|Response to p|
|##|6|Android- Error:Execut|
|##|7||
|##|8|How to solve|
|##|9|"SyntaxE|
|##|10|Code signing is required for product type 'Application' in SDK 'iOS 10|
|##|11||
|##||ownerid|
|##|1|3656666|
|##|2|3319176|
|##|3|2761509|
|##|4|5881764|
|##|5|2896963|
|##|6|1118886|
|##|7|1629278|
|##|8|1707976|
|##|9|4043633|
|##|10|1554347|
|##|11|2670370|


Let’s lay out the various verbs in SQL. Here’s the form of a standard query (though the ORDER BY is often omitted and sorting is computationally expensive):

SELECT <column(s)> FROM <table> WHERE <condition(s) on column(s)> ORDER BY <column(s)>

SQL keywords are often written in ALL CAPITALS though I won’t necessarily do that here. And here is a table of some important keywords:

34

_Table 1. Basic SQL keywords._

|Keyword|Usage|
|---|---|
|SELECT|select columns|
|FROM|which table to operate on|
|WHERE|filter(choose)rows satisfyingcertain conditions|
|LIKE,IN,<,>,==,etc.|used aspart of conditions|
|ORDER BY|sort based on columns|


For comparisons in a WHERE clause, some common syntax for setting conditions includes LIKE (for patterns), =, >, <, >=, <=, !=.

Some other keywords are: DISTINCT, ON, JOIN, GROUP BY, AS, USING, UNION, INTERSECT, SIMILAR TO.

**Question** : how would we find the youngest users in the database?

### **3.7 Grouping / stratifying**

A common pattern of operation is to stratify the dataset, i.e., collect it into mutually exclusive and exhaustive subsets. One would then generally do some operation on each subset. In SQL this is done with the GROUP BY keyword.

Here’s a basic example where we count the occurrences of different tags.

**dbGetQuery** (db, "select tag, count(*) as n from questions_tags group by tag order by n desc limit 25") ## tag n ## 1 javascript 290966 ## 2 java 219155 ## 3 android 184272 ## 4 php 177969 ## 5 python 171745 ## 6 c# 163637 ## 7 html 126851 ## 8 jquery 123707 ## 9 ios 95722 ## 10 css 86470 ## 11 angularjs 76951 ## 12 c++ 76260 ## 13 mysql 75458

35

|## 14|swift|61485|
|---|---|---|
|## 15|sql|58346|
|## 16|node.js|52827|
|## 17|r|48079|
|## 18|arrays|46739|
|## 19|json|45250|
|## 20|ruby-on-rails|39036|
|## 21|sql-server|37077|
|## 22|c|36080|
|## 23|asp.net|35610|
|## 24|excel|29924|
|## 25|angular2|28832|


In general ‘GROUP BY‘ statements will involve some aggregation operation on the subsets. Options include: COUNT, MIN, MAX, AVG, SUM.

**Challenge** : Write a query that will count the number of answers for each question, returning the most answered questions.

### **3.8 Getting unique results (DISTINCT)**

A useful SQL keyword is DISTINCT, which allows you to eliminate duplicate rows from any table (or remove duplicate values when one only has a single column or set of values).

tagNames <- **dbGetQuery** (db, "select distinct tag from questions_tags") **head** (tagNames)

## tag ## 1 c# ## 2 razor ## 3 flags ## 4 javascript ## 5 rxjs ## 6 node.js

**dbGetQuery** (db, "select count(distinct tag) from questions_tags") ## count(distinct tag) ## 1 41006

36

### **3.9 Simple SQL joins**

Often to get the information we need, we’ll need data from multiple tables. To do this we’ll need to do a database join, telling the database what columns should be used to match the rows in the different tables.

The syntax generally looks like this (again the WHERE and ORDER BY are optional):

SELECT <column(s)> FROM <table1> JOIN <table2> ON <columns to match on> WHERE <condition(s) on column(s)> ORDER BY <column(s)>

Let’s see some joins using the different syntax on the Stack Overflow database. In particular let’s select only the questions with the tag "python".

result1 <- **dbGetQuery** (db, "select * from questions join questions_tags on questions.questionid = questions_tags.questionid where tag = 'python'")

It turns out you can do it without using the JOIN keyword.

result2 <- **dbGetQuery** (db, "select * from questions, questions_tags where questions.questionid = questions_tags.questionid and tag = 'python'")

**head** (result1)

|##|questionid|cre|ationdate|score|viewcount|
|---|---|---|---|---|---|
|##|1<br>34553559|2016-01-01|04:34:34|3|96|
|##|2<br>34556493|2016-01-01|13:22:06|2|30|
|##|3<br>34557898|2016-01-01|16:36:04|3|143|
|##|4<br>34560088|2016-01-01|21:10:32|1|126|
|##|5<br>34560213|2016-01-01|21:25:26|1|127|
|##|6<br>34560740|2016-01-01|22:37:36|0|455|
|##||||||
|##|1||||Python nested loops only wor|
|##|2||||bool operator in for Timestamp i|
|##|3||||Pairwise haversin|
|##|4||||Stopwatch (chr|
|##|5 How to set|the type o|f a pyqtS|ignal|(variable of class X) that takes a|
|##|6||||Flask: Peewee model_to_d|
|##|ownerid que|stionid..7|tag|||


37

## 1 845642 34553559 python ## 2 4458602 34556493 python ## 3 2927983 34557898 python ## 4 5736692 34560088 python ## 5 5636400 34560213 python ## 6 3262998 34560740 python **identical** (result1, result2) ## [1] TRUE

Here’s a three-way join (using both types of syntax) with some additional use of aliases to abbreviate table names. What does this query ask for?

result1 <- **dbGetQuery** (db, "select * from questions Q join questions_tags T on Q.questionid = T.questionid join users U on Q.ownerid = U.userid where tag = 'python' and age > 60") result2 <- **dbGetQuery** (db, "select * from questions Q, questions_tags T, users U where Q.questionid = T.questionid and Q.ownerid = U.userid and tag = 'python' and age > 60") **identical** (result1, result2) ## [1] TRUE

**Challenge** : Write a query that would return all the answers to questions with the Python tag. **Challenge** : Write a query that would return the users who have answered a question with the Python tag.

38

### **3.10 Temporary tables and views**

You can think of a view as a temporary table that is the result of a query and can be used in subsequent queries. In any given query you can use both views and tables. The advantage is that they provide modularity in our querying. For example, if a given operation (portion of a query) is needed repeatedly, one could abstract that as a view and then make use of that view.

Suppose we always want the age and displayname of owners of questions to be readily available. Once we have the view we can query it like a regular table.

_## note there is a creationdate in users too, hence disambiguation_ **dbExecute** (db, "create view questionsAugment as select questionid, questions.creationdate, score, viewcount, title, ownerid, age, displayname from questions join users on questions.ownerid = users.userid")

## [1] 0 _## you'll see the return value is '0'_

**dbGetQuery** (db, "select * from questionsAugment where age < 15 limit 5")

|##|questionid|crea|tiondate sco|re viewcount|
|---|---|---|---|---|
|## 1|38096075|2016-06-29|09:50:36|0<br>23|
|## 2|38899284|2016-08-11|14:32:39|0<br>33|
|## 3|40051364|2016-10-14|20:18:18|1<br>37|
|## 4|37168422|2016-05-11|16:29:16|0<br>212|
|## 5|37188786|2016-05-12|13:43:41|0<br>25|
|##|||||
|## 1|Iterate ove|r an enum,|which saves|classes, then init the classes and pu|
|## 2||||Spark Framework puts HTML a|
|## 3||||OpenShift Maven does not use the|
|## 4||||Theming an ASP.net menu contr|
|## 5|||Using|IIS7 Url rewrite module to redirect t|
|##|ownerid age|displaynam|e||
|## 1|3809164<br>14|ArsenArse|n||
|## 2|3809164<br>14|ArsenArse|n||
|## 3|3809164<br>14|ArsenArse|n||


39

|## 4|3932721|14|Bob|
|---|---|---|---|
|## 5|3932721|14|Bob|


One use of a view would be to create a mega table that stores all the information from multiple tables in the (unnormalized) form you might have if you simply had one data frame in R or Python.

### **3.11 More on joins**

We’ve seen a bunch of joins but haven’t discussed the full taxonomy of types of joins. There are various possibilities for how to do a join depending on whether there are rows in one table that do not match any rows in another table.

**Inner joins** : In database terminology an inner join is when the result has a row for each match of a row in one table with the rows in the second table, where the matching is done on the columns you indicate. If a row in one table corresponds to more than one row in another table, you get all of the matching rows in the second table, with the information from the first table duplicated for each of the resulting rows. For example in the Stack Overflow data, an inner join of questions and answers would pair each question with each of the answers to that question. However, questions without any answers or (if this were possible) answers without a corresponding question would not be part of the result.

**Outer joins** : Outer joins add additional rows from one table that do not match any rows from the other table as follows. A _left outer join_ gives all the rows from the first table but only those from the second table that match a row in the first table. A _right outer join_ is the converse, while a _full outer join_ includes at least one copy of all rows from both tables. So a left outer join of the Stack Overflow questions and answers tables would, in addition to the matched questions and their answers, include a row for each question without any answers, as would a full outer join. In this case there should be no answers that do not correspond to question, so a right outer join should be the same as an inner join.

**Cross joins** : A cross join gives the Cartesian product of the two tables, namely the pairwise combination of every row from each table, analogous to _expand.grid()_ in R. I.e., take a row from the first table and pair it with each row from the second table, then repeat that for all rows from the first table. Since cross joins pair each row in one table with all the rows in another table, the resulting table can be quite large (the product of the number of rows in the two tables). In the Stack Overflow database, a cross join would pair each question with every answer in the database, regardless of whether the answer is an answer to that question.

Simply listing two or more tables separated by commas as we saw earlier is the same as a _cross join_ . Alternatively, listing two or more tables separated by commas, followed by conditions that equate rows in one table to rows in another is the same as an _inner join_ .

40

In general, inner joins can be seen as a form of cross join followed by a condition that enforces matching between the rows of the table. More broadly, here are four equivalent joins that all perform the equivalent of an inner join:

## explicit inner join: select * from table1 join table2 on table1.id = table2.id ## non-explicit join without JOIN select * from table1, table2 where table1.id = table2.id ## cross-join followed by matching select * from table1 cross join table2 where table1.id = table2.id ## explicit inner join with 'using' select * from table1 join table2 using(id)

**Challenge** : Create a view with one row for every question-tag pair, including questions without any tags.

**Challenge** : Write a query that would return the displaynames of all of the users who have *never* posted a question. The NULL keyword will come in handy – it’s like ‘NA‘ in R. Hint: NULLs should be produced if you do an outer join.

### **3.12 Indexes**

An index is an ordering of rows based on one or more fields. DBMS use indexes to look up values quickly, either when filtering (if the index is involved in the WHERE condition) or when doing joins (if the index is involved in the JOIN condition). So in general you want your tables to have indexes.

DBMS use indexing to provide sub-linear time lookup. Without indexes, a database needs to scan through every row sequentially, which is called linear time lookup – if there are n rows, the lookup is O(n) in computational cost. With indexes, lookup may be logarithmic – O(log(n)) – (if using tree-based indexes) or constant time – O(1) – (if using hash-based indexes). A binary treebased search is logarithmic; at each step through the tree you can eliminate half of the possibilities.

Here’s how we create an index, with some time comparison for a simple query.

**system.time** ( **dbGetQuery** (db,

"select * from questions where viewcount > 10000")) _# 10 seconds_ **system.time** ( **dbExecute** (db,

"create index count_index on questions (viewcount)")) _# 19 seconds_ **system.time** ( **dbGetQuery** (db,

"select * from questions where viewcount > 10000")) _# 3 seconds_

41

In other contexts, an index can save huge amounts of time. So if you’re working with a database and speed is important, check to see if there are indexes.

That being said, using indexes in a lookup is not always advantageous, as discussed in the tutorial.

### **3.13 Creating database tables**

One can create tables from within the ‘sqlite‘ command line interfaces (discussed in the tutorial), but often one would do this from R or Python. Here’s the syntax from R.

_## Option 1: pass directly from CSV to database_ **dbWriteTable** (conn = db, name = "student", value = "student.csv", row.names = FALSE, header = TRUE) _## Option 2: pass from data in an R data frame ## create data frame 'student' in some fashion #student <- data.frame(...) #student <- read.csv(...)_ **dbWriteTable** (conn = db, name = "student", value = student, row.names = FALSE, append = FALSE)

### **3.14 SAS (optional)**

SAS is quite good at handling large datasets, storing them on disk rather than in memory. I have used SAS in the past for subsetting and merging large datasets. Then I will generally extract the data I need for statistical modeling and do the analysis in R.

Here’s an example of some SAS code for reading in a CSV followed by some subsetting and merging and then output.

/* we can use a pipe - in this case to remove carriage returns, */ /* presumably because the CSV file was created in Windows */ filename tmp pipe "cat ~/shared/hei/gis/100w4kmgrid.csv | tr -d '\r'";

/* read in one data file */ data grid; infile tmp

42

lrecl=500 truncover dsd firstobs=2; informat gridID x y landMask dataMask; input gridID x y landMask dataMask; run ;

filename tmp pipe "cat ~/shared/hei/goes/Goes_int4km.csv | tr -d '\r'";

/* read in second data file */ data match; infile tmp lrecl=500 truncover dsd firstobs=2; informat goesID gridID areaInt areaPix; input goesID gridID areaInt areaPix; run ;

/* need to sort before merging */ proc sort data=grid; by gridID; run; proc sort data=match; by gridID; run; /* notice some similarity to SQL */ data merged; merge match(in=in1) grid(in=in2); by gridID; /* key field */ if in1=1; /* also do some subsetting */ /* only keep certain fields */ keep gridID goesID x y landMask dataMask areaInt areaPix; run; /* do some subsetting */ data PA; /* new dataset */ set merged; /* original dataset */ if x<1900000 and x>1200000 and y<2300000 and y>1900000;

43

run;

%let filename="~/shared/hei/code/model/GOES-gridMatchPA.csv"; /* output to CSV */

PROC EXPORT DATA= WORK.PA

OUTFILE= &filename DBMS=CSV REPLACE;

RUN;

Note that SAS is oriented towards working with data in a “data frame”-style format; i.e., rows as observations and columns as fields, with different fields of possibly different types. As you can see in the syntax above, the operations concentrate on transforming one dataset into another dataset.

## **4 R and big data (optional)**

There has been a lot of work in recent years to allow R to work with big datasets.

- The _data.table_ package provides for fast operations on large data tables in memory. The _dplyr_ package has also been optimized to work quickly on large data tables in memory, including operating on _data.table_ objects from the _data.table_ package.

- The _ff_ and _bigmemory_ packages provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R.

- The _biglm_ package provides the ability to fit linear models and GLMs to big datasets, with integration with _ff_ and _bigmemory_ .

- Finally the _sqldf_ package provides the ability to use SQL queries on R dataframes and onthe-fly when reading from CSV files. The latter can help you avoid reading in the entire dataset into memory in R if you just need a subset of it.

In this section we’ll use an example of US government data on airline delays (1987-2008) available through the ASA 2009 Data Expo at http://stat-computing.org/dataexpo/2009/the-data.html.

First we’ll use UNIX tools to download the individual yearly CSV files and make a single CSV (~12 Gb). (See the demo code file, _unit7-bigData.R_ , for the bash code.) Note that it’s much smaller when compressed (1.7 Gb) or if stored in a binary format. You can download a zipped version of the full CSV from http://www.stat.berkeley.edu/share/paciorek/AirlineDataAll.csv.zip.

44

### **4.1 Working quickly with big datasets in memory: data.table**

In many cases, particularly on a machine with a lot of memory, R might be able to read the dataset into memory but computations with the dataset may be slow.

The _data.table_ package provides a lot of functionality for fast manipulation: indexing, merges/joins, assignment, grouping, etc.

Let’s read in the airline dataset, specifying the column classes so that _fread()_ doesn’t have to detect what they are. I’ll also use factors since factors are represented numerically. It only takes about 5 minutes to read the data in. We’ll see in the next section that this is much faster than with other approaches within R.

**require** (data.table) dir = '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') dt <- **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6))) _#Read 123534969 rows and 29 (of 29) columns from # 11.203 GB file in 00:05:16_ **class** (dt) _# [1] "data.table" "data.frame"_

Now let’s do some basic subsetting. We’ll see that setting a key (which is how data.table refers to a database-style _index_ ) and using binary search can improve lookup speed dramatically.

**system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.8 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000)) _## 12.7 seconds_

**system.time** ( **setkey** (dt, Origin, Distance)) _## 33 seconds: ## takes some time, but will speed up later operations_

45

**tables** () _## NAME NROW MB ##[1,] dt 123,534,969 27334 ##[2,] sfo 2,733,910 606 ##[3,] sfoShort 1,707,171 379 ## COLS ##[1,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[2,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ##[3,] Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarr ## KEY ##[1,] Origin,Distance ##[2,] ##[3,] ##Total: 28,319MB ## vector scan_ **system.time** (sfo <- **subset** (dt, Origin == "SFO")) _## 8.5 seconds_ **system.time** (sfoShort <- **subset** (dt, Origin == "SFO" & Distance < 1000 )) _## 12.4 seconds ## binary search_ **system.time** (sfo <- dt[ **.** ('SFO'), ]) _## 0.8 seconds_

Setting a key in _data.table_ simply amounts to sorting based on the columns provided, which allows for fast lookup later using binary search algorithms, as seen with the last query. From my fairly quick look through the _data.table_ documentation I don’t see a way to do the subsetting based on ranges of values (e.g., flights with distance less than 1000) using the specialized functionality of _data.table_ .

There’s a bunch more to _data.table_ and you’ll have to learn a modest amount of new syntax, but if you’re working with large datasets in memory, it will probably be well worth your while. Plus _data.table_ objects are data frames (i.e., they inherit from data frames) so they are compatible with R code that uses dataframes.

46

### **4.2 Working with big datasets on disk: ff and bigmemory**

Note that with our 12 Gb dataset, the data took up 27 Gb of RAM on the SCF server _radagast_ . Operations on the dataset would then use up additional RAM. So this would not be feasible on most machines. And of course other datasets might be so big that even _radagast_ wouldn’t be able to hold them in memory.

#### **4.2.1 ff**

The _ff_ package stores datasets in columnar format, with one file per column, on disk, so is not limited by memory. It then provides fast access to the dataset from R.

If we need to work with a dataset in R but the dataset won’t fit in memory, we can read the data into R using the _ff_ package, in particular reading in as an _ffdf_ object. Note the arguments are similar to those for _read.{table,csv}()_ . _read.table.ffdf()_ reads the data in chunks.

**require** (ff) **require** (ffbase)

_# I put the data file on local disk on the machine I am using # (/tmp on radagast) # it's good to test with a small subset before # doing the full operations_ fileName <- **file.path** (dir, 'test.csv') dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4), 'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor','factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6)))

fileName <- '/tmp/AirlineDataAll.csv' **system.time** ( dat <- **read.csv.ffdf** (file = fileName, header = TRUE, colClasses = **c** ('integer', **rep** ('factor', 3), **rep** ('integer', 4), 'factor', 'integer', 'factor', **rep** ('integer', 5), 'factor', 'factor', **rep** ('integer', 4), 'factor', **rep** ('integer', 6))) ) _## takes about 22 minutes_

47

**system.time** ( **ffsave** (dat, file = **file.path** (dir, 'AirlineDataAll'))) _## takes 11 minutes ## file is saved (in a binary format) as AirlineDataAll.ffData ## with metadata in AirlineDataAll.RData_

**rm** (dat) _# pretend we are in a new R session_

**system.time** ( **ffload** ( **file.path** (dir, 'AirlineDataAll'))) _# this is much quicker: # 107 seconds_

In the above operations, we wrote a copy of the file in the ff binary format that can be read more quickly back into R than the original reading of the CSV using _ffsave()_ and _ffload()_ . Also note the reduced size of the binary format file compared to the original CSV. It’s good to be aware of where the binary ff file is stored given that for large datasets, it will be large. With _ff_ (I think _bigmemory_ is different in how it handles this) it appears to be stored in _/tmp_ in an R temporary directory. Note that as we work with large files we need to be more aware of the filesystem, making sure in this case that _/tmp_ has enough space.

Let’s look at the _ff_ and _ffbase_ packages to see what functions are available using library(help=ff). Notice that there is an _merge.ff()_ .

Note that a copy of an _ff_ object does not appear to actually copy any data, but merely create another name referring to the same data object.

Next let’s do a bit of exploration of the dataset. Of course in a real analysis we’d do a lot more and some of this would take some time.

**ffload** ( **file.path** (dir, 'AirlineDataAll'))

_# [1] "tmp/RtmpU5Uw6z/ffdf4e684aecd7c4.ff" "tmp/RtmpU5Uw6z/ffdf4e687fb73a88.ff" # [3] "tmp/RtmpU5Uw6z/ffdf4e6862b1033f.ff" "tmp/RtmpU5Uw6z/ffdf4e6820053932.ff" # [5] "tmp/RtmpU5Uw6z/ffdf4e681e7d2235.ff" "tmp/RtmpU5Uw6z/ffdf4e686aa01c8.ff" # ..._

dat$Dest

_# ff (closed) integer length=123534969 (123534969) levels: BUR LAS LAX OAK # ABE ABQ ACV ALB ALO AMA ANC ATL AUS AVP AZO BDL BFL BGR BHM BIL BLI BNA BOI # CAK CCR CHS CID CLE CLT CMH CMI COS CPR CRP CRW CVG DAB DAL DAY DCA DEN DFW # EUG EVV EWR FAI FAR FAT FLG FLL FOE FSD GCN GEG GJT GRR GSO GSP GTF HNL HOU_

48

_# ICT ILG ILM IND ISP JAN JAX JFK KOA LBB LEX LGA LGB LIH LIT LMT LNK MAF MBS # MFR MHT MIA MKE MLB MLI MOB MRY MSN MSP MSY OGG OKC OMA ONT ORD ORF PBI PHL # ..._

_# let's do some basic tabulation_ DestTable <- **sort** ( **table.ff** (dat$Dest), decreasing = TRUE) _# table is a generic, so shouldn't need explicit table.ff, # unless dat$Dest is not see as an ff object_

_# takes a while # ORD ATL DFW LAX PHX DEN DTW IAH MSP # 6638035 6094186 5745593 4086930 3497764 3335222 2997138 2889971 2765191 # STL EWR LAS CLT LGA BOS PHL PIT SLC # 2720250 2708414 2629198 2553157 2292800 2287186 2162968 2079567 2004414 # looks right - the busiest airports are ORD (O'Hare in Chicago) and ATL_ dat$DepDelay[1:50] _#opening ff /tmp/RtmpU5Uw6z/ffdf4e682d8cd893.ff # [1] 11 -1 11 -1 19 -2 -2 1 14 -1 5 16 17 1 21 3 13 -1 87 19 31 17 32 # [26] 29 26 15 5 54 0 25 -2 0 12 14 -1 2 1 16 15 44 20 15 3 21 -1 0_

**min.ff** (dat$DepDelay, na.rm = TRUE) _# [1] -1410_ **max.ff** (dat$DepDelay, na.rm = TRUE) _# [1] 2601 # why do I need to call min.ff and max.ff rather than min/max? # tmp <- clone(dat$DepDelay) # make an explicit copy_

Let’s review our understanding of S3 methods. Why did I need to call _min.ff()_ rather than just

49

simply calling _min()_ on the ff object? Could I have called _table()_ instead of _table.ff()_ ?

A note of caution. Debugging code involving _ff_ can be a hassle because the size gets in the way in various ways. Until you’re familiar with the various operations on ff objects, you’d be wise to try to run your code on a small test dataset loaded in as an ff object. Also, we want to be sure that the operations we use keep any resulting large objects in the _ff_ format and use _ff_ methods and not standard R functions.

#### **4.2.2 bigmemory**

The _bigmemory_ package is an alternative way to work with datasets in R that are kept stored on disk rather than read entirely into memory. _bigmemory_ provides a _big.matrix_ class, so it appears to be limited to datasets with a single type for all the variables. However, one nice feature is that one can use _big.matrix_ objects with _foreach_ (one of R’s parallelization tools, to be discussed soon) without passing a copy of the matrix to each worker. Rather the workers can access the matrix stored on disk.

#### **4.2.3 sqldf**

The _sqldf_ package provides the ability to use SQL queries on data frames (via _sqldf()_ ) as well as to filter an input CSV via an SQL query (via _read.csv.sql()_ ), with only the result of the subsetting put in memory in R. The full input data can be stored temporarily in an SQLite database on disk.

**require** (sqldf) dir = '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') _# read in file, with temporary database in memory_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **NULL** , header = TRUE)) _# read in file, with temporary database on disk_ **system.time** (sfo <- **read.csv.sql** (fn, sql = "select * from file where Origin = 'SFO'", dbname= **tempfile** (), header = TRUE))

### **4.3 dplyr package**

You should already be familiar with using _dplyr._ One very nice feature is that with _dplyr_ one can work with data stored in the _data.table_ format, in external databases, and in Spark. There is also

50

an extension to dplyr that allows for dplyr operations to be done in parallel.

**library** (dplyr) _## with database_ dir <- '../data' _# relative or absolute path to where the .db file is_ dbFilename <- 'stackoverflow-2016.db'

db <- **src_sqlite** ( **file.path** (dir, dbFilename)) questions <- **tbl** (db, "questions") questions _## with data.table_ dir <- '/tmp' fileName <- **file.path** (dir, 'AirlineDataAll.csv') flights <- **tbl_dt** ( **fread** (fileName, colClasses= **c** ( **rep** ("numeric", 8), "factor", "numeric", "factor", **rep** ("numeric", 5), **rep** ("factor", 2), **rep** ("numeric", 4), "factor", **rep** ("numeric", 6))))

_# now use dplyr functionality on 'flights'_

flights %>% **group_by** (UniqueCarrier) %>% **summarize** (mnDelay = **mean** (DepDelay, na.rm=TRUE))

_# Source: local data table [29 x 2] # # UniqueCarrier mean(DepDelay, na.rm = TRUE) #1 PS 8.928104 #2 TW 7.658251 #3 UA 9.667930 #4 WN 9.077167 #5 EA 8.674051 #6 HP 8.107790 #7 NW 6.007974 #8 PA (1) 5.532442_

51

_#9 PI 9.560336 #10 CO 7.695967 #.. ... ..._

### **4.4 Fitting models to big datasets: biglm**

The _biglm_ package provides the ability to fit large linear models and GLMs. _ffbase_ has a _bigglm.ffdf()_ function that builds on _biglm_ for use with _ffdf_ objects. Let’s fit a basic model on the airline data. Note that we’ll also fit the same model on the dataset when we use Spark at the end of the Unit.

**require** (ffbase) **require** (biglm) dir = '/tmp' datUse <- **subset** (dat, ArrDelay < 60*12 & ArrDelay > (-30) & ! **is.na** (ArrDelay) & ! **is.na** (Distance) & ! **is.na** (DayOfWeek)) datUse$Distance <- datUse$Distance / 1000 _# helps stabilize numerics # 119971791 records # any concern about my model?_ **system.time** (mod <- **bigglm** (ArrDelay ~ Distance + DayOfWeek, data = datUse)) _# 542.149 11.248 550.779_ **summary** (mod) coef <- **summary** (mod)$mat[,1]

Here are the results. Day 1 is Monday, so that’s the baseline category for the ANOVA-like part of the model.

Large data regression model: bigglm(DepDelay ~ Distance + DayOfWeek, data = Sample size = 119971791 Coef (95% CI) SE p (Intercept) 6.3662 6.3504 6.3820 0.0079 0 Distance 0.7638 0.7538 0.7737 0.0050 0 DayOfWeek2 -0.6996 -0.7197 -0.6794 0.0101 0

52

DayOfWeek3 0.3928 0.3727 0.4129 0.0101 0 DayOfWeek4 2.2247 2.2046 2.2449 0.0101 0 DayOfWeek5 2.8867 2.8666 2.9068 0.0101 0 DayOfWeek6 -2.4273 -2.4481 -2.4064 0.0104 0 DayOfWeek7 -0.1362 -0.1566 -0.1158 0.0102 0

Of course as good statisticians/data analysts we want to do careful assessment of our model, consideration of alternative models, etc. This is going to be harder to do with large datasets than with more manageable ones. However, one possibility is to do the diagnostic work on subsamples of the data.

Now let’s consider the fact that very small substantive effects can be highly statistically significant when estimated from a large dataset. In this analysis the data are generated from _Y ∼ N_ (0 + 0 _._ 001 _x,_ 1), so the _R_<sup>2</sup> is essentially zero.

n <- 150000000 _# n*4*8/1e6 Mb of RAM (~5 Gb) # but turns out to be 11 Gb as a text file_ nChunks <- 100 chunkSize <- n/nChunks **set.seed** (0) **for** (p **in** 1:nChunks) { x1 <- **runif** (chunkSize) x2 <- **runif** (chunkSize) x3 <- **runif** (chunkSize) y <- **rnorm** (chunkSize, .001*x1, 1) **write.table** ( **cbind** (y,x1,x2,x3), file = **file.path** (dir, 'signif.csv'), sep = ',', col.names = FALSE, row.names = FALSE, append = TRUE, quote = FALSE) } fileName <- **file.path** (dir, 'signif.csv') **system.time** ( dat <- **read.csv.ffdf** (file = fileName, header = FALSE, colClasses = **rep** ('numeric', 4))) _# 922.213 18.265 951.204 -- timing is on an older machine than radagast_

53

**names** (dat) <- **c** ('y', 'x1','x2', 'x3') **ffsave** (dat, file = **file.path** (dir, 'signif'))

**system.time** ( **ffload** ( **file.path** (dir, 'signif'))) _# 52.323 7.856 60.802 -- timing is on an older machine_ **system.time** (mod <- **bigglm** (y ~ x1 + x2 + x3, data = dat)) _# 1957.358 8.900 1966.644 -- timing is on an older machine_ **options** (digits = 12) **summary** (mod) _# R^2 on a subset (why can it be negative?)_ coefs <- **summary** (mod)$mat[,1] wh <- 1:1000000 1 - **sum** ((dat$y[wh] - coefs[1] + coefs[2]*dat$x1[wh] + coefs[3]*dat$x2[wh] + coefs[4]*dat$x3[wh])^2) / **sum** ((dat$y[wh] - **mean** (dat$y[wh]))^2)

Here are the results:

Large data regression model: bigglm(y ~ x1 + x2 + x3, data = dat) Sample size = 1.5e+08

Coef (95% CI) SE p (Intercept) -0.0001437 -0.0006601 0.0003727 0.0002582 0.5777919 x1 0.0013703 0.0008047 0.0019360 0.0002828 0.0000013 x2 0.0002371 -0.0003286 0.0008028 0.0002828 0.4018565 x3 -0.0002620 -0.0008277 0.0003037 0.0002829 0.3542728 ### and here is the R^2 calculation (why can it be negative?) [1] -1.111046828e-06

So, do I care the result is highly significant? Perhaps if I’m hunting the Higgs boson... As you have hopefully seen in statistics courses, statistical significance _̸_ = practical significance.

54

## **5 Sparsity**

A lot of statistical methods are based on sparse matrices. These include:

- Matrices representing the neighborhood structure (i.e., conditional dependence structure) of networks/graphs.

- Matrices representing autoregressive models (neighborhood structure for temporal and spatial data)

- A statistical method called the _lasso_ is used in high-dimensional contexts to give sparse results (sparse parameter vector estimates, sparse covariance matrix estimates)

- There are many others (I’ve been lazy here in not coming up with a comprehensive list, but trust me!)

When storing and manipulating sparse matrices, there is no need to store the zeros, nor to do any computation with elements that are zero. A few of you exploited sparse matrices in PS4.

R, Matlab and Python all have functionality for storing and computing with sparse matrices. We’ll see this a bit more in the linear algebra unit.

**require** (spam) mat = **matrix** ( **rnorm** (1e8), 1e4) mat[mat > (-2)] <- 0 sMat <- **as.spam** (mat) **print** ( **object.size** (mat), units = 'Mb') _# 762.9 Mb_ **print** ( **object.size** (sMat), units = 'Mb') _# 26 Mb_

vec <- **rnorm** (1e4) **system.time** (mat %*% vec) _# 0.385 seconds_ **system.time** (sMat %*% vec) _# 0.015 seconds_

Here’s a blog post describing the use of sparse matrix manipulations for analysis of the Netflix Prize data.

## **6 Using statistical concepts to deal with computational bottlenecks**

As statisticians, we have a variety of statistical/probabilistic tools that can aid in dealing with big data.

55

1. Usually we take samples because we cannot collect data on the entire population. But we can just as well take a sample because we don’t have the ability to process the data from the entire population. We can use standard uncertainty estimates to tell us how close to the true quantity we are likely to be. And we can always take a bigger sample if we’re not happy with the amount of uncertainty.

2. There are a variety of ideas out there for making use of sampling to address big data challenges. One idea (due in part to Prof. Michael Jordan here in Statistics/EECS) is to compute estimates on many (relatively small) bootstrap samples from the data (cleverly creating a reduced-form version of the entire dataset from each bootstrap sample) and then combine the estimates across the samples. Here’s the arXiv paper on this topic, also published as Kleiner et al. in Journal of the Royal Statistical Society (2014) 76:795.

3. Randomized algorithms: there has been a lot of attention recently to algorithms that make use of randomization. E.g., in optimizing a likelihood, you might choose the next step in the optimization based on random subset of the data rather than the full data. Or in a regression context you might choose a subset of rows of the design matrix (the matrix of covariates) and corresponding observations, weighted based on the statistical leverage [recall the discussion of regression diagnostics in a regression course] of the observations. Here’s another arXiv paper that provides some ideas in this area.

56

---

[← Unit 08 — bigData Part 04 —](04-unit-08-bigdata-part-04.md) · [Up: contents](index.md)
