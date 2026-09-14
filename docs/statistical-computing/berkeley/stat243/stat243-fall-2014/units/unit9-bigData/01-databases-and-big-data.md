---
title: Databases and Big Data
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Databases and Big Data

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 20, 2014

References:

- Murrell: Introduction to Data Technologies

- Adler: R in a Nutshell

- Spark Programming Guide

I’ve also pulled material from a variety of other sources, some mentioned in context below.

Note that for a lot of the demo code I ran the code separately outside of _knitr_ and this document because of the time involved in working with large datasets.

## **1 A few preparatory notes**

### **1.1 An editorial on ’big data’**

Big data is trendy these days.

Personally, I think some of the hype is justified and some is hype. Large datasets allow us to address questions that we can’t with smaller datasets, and they allow us to consider more sophisticated (e.g., nonlinear) relationships than we might with a small dataset. But they do not directly help with the problem of correlation not being causation. Having medical data on every American still doesn’t tell me if higher salt intake causes hypertension. Internet transaction data does not tell me if one website feature causes increased viewership or sales. One either needs to carry out a designed experiment or think carefully about how to infer causation from observational data. Nor does big data help with the problem that an ad hoc ’sample’ is not a statistical sample and does not provides the ability to directly infer properties of a population. A well-chosen smaller dataset may be much more informative than a much larger, more ad hoc dataset. However, having big datasets might allow you to select from the dataset in a way that helps get at causation or in a way that allows you to construct a population-representative sample.

1

Here’s a different way to summarize it.

Different people define the ’big’ in big data differently. One definition involves the actual size of the data. Our efforts here will focus on dataset sizes that are large for traditional statistical work but would probably not be thought of as large in some contexts such as Google or the NSA. Another definition of ’big data’ has more to do with how pervasive data and empirical analyses backed by data are in society and not necessarily how large the actual dataset size is.

### **1.2 Logistics**

One of the main drawbacks with R in working with big data is that all objects are stored in memory, so you can’t directly work with datasets that are more than 1-20 Gb or so, depending on the memory on your machine.

Note: in handling big data files, it’s best to have the data on the local disk of the machine you are using to reduce traffic and delays from moving data over the network.

### **1.3 What we already know about handling big data!**

UNIX operations are generally very fast, so if you can manipulate your data via UNIX commands and piping, that will allow you to do a lot. We’ve already seen UNIX commands for extracting columns. And various commands such as _grep_ , _head_ , _tail_ , etc. allow you to pick out rows based on certain criteria. As some of you have done in problem sets, one can use _awk_ to extract rows. So basic shell scripting may allow you to reduce your data to a more manageable size.

And don’t forget simple things. If you have a dataset with 30 columns that takes up 10 Gb but you only need 5 of the columns, get rid of the rest and work with the smaller dataset. Or you might be able to get the same information from a random sample of your large dataset as you would from doing the analysis on the full dataset. Strategies like this will often allow you to stick with the tools you already know.

Also, the example datasets in Section 3 are not good illustrations of this, but as we’ll see scattered throughout the Unit and as we saw in Unit 3, there are more compact ways of storing data than in flat text (e.g., csv) files.

## **2 Databases**

### **2.1 Overview**

A relational database stores data as a set of tables (or relations), which are rather similar to R data frames, in that a table is made up of columns or fields, each containing a single type (numeric,

2

character, date, currency, ...) and rows or records containing the observations for one entity. One principle of databases is that if a category is repeated in a given variable, you can more efficiently store information about each level of the category in a separate table; consider information about people living in a state and information about each state - you don’t want to include variables that only vary by state in the table containing information about individuals (at least until you’re doing the actual analysis that needs the information in a single table). Or consider students nested within classes nested within schools. Databases are set up to allow for fast querying and merging (called _joins_ in database terminology).

You can interact with databases in a variety of database systems (DBMS=database management system) (some systems are _SQLite_ , _MySQL_ , _postgreSQL_ , _Oracle_ , _Access_ ). We’ll concentrate on accessing data in a database rather than management of databases. SQL is the _Structured Query Language_ and is a special-purpose language for managing databases and making queries. Variations on SQL are used in many different DBMS.

Many DBMS have a client-server model. Clients connect to the server, with some authentication, and make requests. We’ll concentrate here on a simple DBMS, _SQLite_ , that allows us to just work on our local machine, with the database stored as a single file.

There are often multiple ways to interact with a DBMS, including directly using command line tools provided by the DBMS or via Python or R, among others.

We’ll use an SQLite database available on any SCF machine at _/mirror/data/pub/html/scf/cis.db_ as our example database. This is a database of the metadata (authors, titles, years, journal, etc.) for articles published in Statistics journals over the last century. First, let’s talk through how one would set up a relational database to store journal article information.

### **2.2 Accessing databases in R**

In R, the _DBI_ package provides a front-end for manipulating databases from a variety of DBMS (MySQL, SQLite, Oracle, among others). Basically, you tell the package what DBMS is being used on the backend, link to the actual database, and then you can use the syntax in the package.

First we’ll connect to the database and get some information on the _schema_ , i.e., the structure of the database.

**library** (RSQLite) _## Loading required package: DBI_ fileName <- "/mirror/data/pub/html/scf/cis.db" drv <- **dbDriver** ("SQLite")

3

db <- **dbConnect** (drv, dbname = fileName) _# using a connection once again! # con <- dbConnect(SQLite(), dbname = fileName) # alternative # get information on the database schema_ **dbListTables** (db)

## [1] "articles" "authors" "authorships" "books" ## [5] "contacts" "delayed_jobs" "isbns" "issns" ## [9] "issues" "journals" "tag_relations" "taggings" ## [13] "tags" "volumes" **dbListFields** (db, "articles") ## [1] "id" "type" "id_entity" "id_title" "title" ## [6] "year" "volume" "number" "page_start" "page_end" ## [11] "url" "journal" "journal_id" "volume_id" "issue_id" ## [16] "zmath"

**dbListFields** (db, "authors")

## [1] "id" "name" **dbListFields** (db, "authorships") ## [1] "id" "id_title" "author_id" ## [4] "editor" "sequence" "publication_id" ## [7] "publication_type"

#### For queries, SQL has statements like:

SELECT var1, var2, var3 FROM tableX WHERE condition1 AND condition2 ORDER BY var4

E.g., _condition1_ might be latitude > 80 or name = ’Breiman’ or company in (’IBM’, ’Apple’, ’Dell’). Now we’ll do some queries to pull together information we want. Because of the relational structure, to extract the titles for a given author, we need to do a series of queries.

auth <- **dbSendQuery** (db, "select * from authorships") **fetch** (auth, 5)

4

|##|id id_title|author_id|editor|sequence|publication_id|publication_type|
|---|---|---|---|---|---|---|
|##|1<br>3<br>2|1|f|0|1|Article\n|
|##|2<br>4<br>3|3|f|0|2|Article\n|
|##|3<br>5<br>4|4|f|0|3|Article\n|
|##|4<br>6<br>5|5|f|0|4|Article\n|
|##|5<br>7<br>6|6|f|0|5|Article\n|


**dbClearResult** (auth) ## [1] TRUE query <- "select id from authors where name like 'Breiman%'" a_ids <- **dbGetQuery** (db, query) a_ids <- **as.list** ( **unlist** (a_ids)) query <- **paste** ("select id_title from authorships where author_id in (", **paste** ( **rep** ("?", **length** (a_ids)), collapse = ","), ")") query ## [1] "select id_title from authorships where author_id in ( ?,? )" a_ids ## $id1 ## [1] 532 ## ## $id2 ## [1] 1141 t_ids <- **dbGetQuery** (db, query, a_ids) t_ids$id_title[1:5] ## [1] 593 1062 1087 1089 1440 t_ids <- **as.list** ( **unlist** (t_ids)) query <- **paste** ("select * from articles where id_title in (", **paste** ( **rep** ("?", **length** (t_ids)), collapse = ","), ")") titles <- **dbGetQuery** (db, query, t_ids) **head** (titles)

5

|##|id|type<br>id_entity|id_title||
|---|---|---|---|---|
|## 1|445|Article 1000000073|593||
|## 2|913|Article 1000000105|1062||
|## 3|938|Article 1000000105|1087||
|## 4|940|Article 1000000105|1089||
|## 5|1863|Article 1000000145|2156||
|## 6|2287|Article 1000000161|2580||
|##||||tit|
|## 1|The i|ndividual ergodic t|heorem of information theory (Corr: V31|p809-81|
|## 2||The capaciti|es of certain channel classes under rand|om codi|
|## 3|||On the completeness of order s|tatisti|
|## 4||The strong|law of large numbers for a class of Mark|ov chai|
|## 5|||The Poisson tendency in traffic d|istorti|
|## 6|||Consistent estimates and zero|-one se|
|##|year|volume number page_|start page_end url journal journal_id vo|lume_id|
|## 1|1957|28<br>0|809<br>811<br>1748|7998|
|## 2|1960|31<br>0|558<br>567<br>1748|9117|
|## 3|1960|31<br>0|794<br>797<br>1748|9117|
|## 4|1960|31<br>0|801<br>803<br>1748|9117|
|## 5|1963|34<br>0|308<br>311<br>1748|9865|
|## 6|1964|35<br>0|157<br>161<br>1748|10084|
|##|issue|_id zmath|||
|## 1||74<br>\n|||
|## 2||106<br>\n|||
|## 3||106<br>\n|||
|## 4||106<br>\n|||
|## 5||146<br>\n|||
|## 6||162<br>\n|||
|_# do_|_a goo_|_gle scholar check t_|_o see that things seem to be ok_||


Note that we were able to insert values from R into the set used to do the selection.

Now let’s see a _join_ (by default this is an “ _inner join_ ” – see below) of multiple tables, combined with a query. This allows us to extract the information on Breiman’s articles more easily.

6

_# alternatively, we can do a query that involves multiple tables_ info <- **dbGetQuery** (db, "select * from articles, authors, authorships where\n _# 'select * from articles, authors, authorships where authors.name like # 'Breiman%' and authors.id = authorships.author_id and authorships.id_title # = articles.id_title'_

**head** (info)

|##|id|type<br>id_en|tity id_title|||
|---|---|---|---|---|---|
|## 1|445|Article 100000|0073<br>593|||
|## 2|913|Article 100000|0105<br>1062|||
|## 3|938|Article 100000|0105<br>1087|||
|## 4|940|Article 100000|0105<br>1089|||
|## 5|1863|Article 100000|0145<br>2156|||
|## 6|2287|Article 100000|0161<br>2580|||
|##|||||tit|
|## 1|The i|ndividual ergo|dic theorem of|information theory (Corr: V31 p|809-81|
|## 2||The cap|acities of cert|ain channel classes under rando|m codi|
|## 3||||On the completeness of order st|atisti|
|## 4||The st|rong law of lar|ge numbers for a class of Marko|v chai|
|## 5|||The|Poisson tendency in traffic di|storti|
|## 6||||Consistent estimates and zero-|one se|
|##|year|volume number|page_start page|_end url journal journal_id vol|ume_id|
|## 1|1957|28<br>0|809|811<br>1748|7998|
|## 2|1960|31<br>0|558|567<br>1748|9117|
|## 3|1960|31<br>0|794|797<br>1748|9117|
|## 4|1960|31<br>0|801|803<br>1748|9117|
|## 5|1963|34<br>0|308|311<br>1748|9865|
|## 6|1964|35<br>0|157|161<br>1748|10084|
|##|issue|_id zmath<br>id|name|id id_title author_id editor||
|## 1||74<br>\n 532|Breiman, Leo\n|696<br>593<br>532<br>f||
|## 2||106<br>\n 532|Breiman, Leo\n|1355<br>1062<br>532<br>f||
|## 3||106<br>\n 532|Breiman, Leo\n|1391<br>1087<br>532<br>f||
|## 4||106<br>\n 532|Breiman, Leo\n|1393<br>1089<br>532<br>f||
|## 5||146<br>\n 532|Breiman, Leo\n|2847<br>2156<br>532<br>f||
|## 6||162<br>\n 532|Breiman, Leo\n|3413<br>2580<br>532<br>f||
|##|seque|nce publicatio|n_id publicatio|n_type||


7

|##|1<br>0|445|Article\n|
|---|---|---|---|
|##|2<br>1|913|Article\n|
|##|3<br>2|938|Article\n|
|##|4<br>0|940|Article\n|
|##|5<br>0|1863|Article\n|
|##|6<br>0|2287|Article\n|


Finally, let’s see the idea of creating a _view_ , which you can think of as a new table, though the DBMS is not actually explicitly constructing such a table.

_# that db is read-only; to create a view we need to be able to modify it_ **system** ( **paste0** ("cp ", fileName, " /tmp/.")) **dbDisconnect** (db)

## [1] TRUE

db <- **dbConnect** (drv, dbname = "/tmp/cis.db")

_# finally, we can create a view that amounts to joining the tables_ fullAuthorInfo <- **dbSendQuery** (db, "create view fullAuthorInfo as select *\n _# 'create view fullAuthorInfo as select * from authors join authorships on # authorships.author_id = authors.id'_

partialArticleInfo <- **dbSendQuery** (db, "create view partialArticleInfo as\n _# 'create view partialArticleInfo as select * from articles join # fullAuthorInfo on articles.id_title=fullAuthorInfo.id_title'_

fullInfo <- **dbSendQuery** (db, "select * from journals join partialArticleInfo\n _# 'select * from journals join partialArticleInfo on journals.id = # partialArticleInfo.journal_id')_

subData <- **fetch** (fullInfo, 3) subData

## id name articles_count min_year ## 1 1748 The Annals of Mathematical Statistics 0 \\N ## 2 452 Econometrica 0 \\N ## 3 1746 The American Statistician 0 \\N

8

|##|max_year|||publisher url mathscinet_id|
|---|---|---|---|---|
|## 1|\\N|Instit|ute of Mathema|tical Statistics<br>\\N|
|## 2|\\N|Blackwe|ll Scientific|Publications Ltd<br>\\N|
|## 3|\\N|Am|erican Statist|ical Association<br>\\N|
|##|english_|only ele|ctronic_only u|rl_only publisher_society admin_comments|
|## 1||\\N|\\N|\\N<br>\\N<br>\\N|
|## 2||\\N|\\N|\\N<br>\\N<br>\\N|
|## 3||\\N|\\N|\\N<br>\\N<br>\\N|
|##|core id|type|id_entity id|_title|
|## 1|\\N\n<br>1|Article|1000000001|2|
|## 2|\\N\n<br>2|Article|1000000002|3|
|## 3|\\N\n<br>3|Article|1000000003|4|
|##|||||
|## 1|The non-|central|Wishart distri|bution and certain problems of multivaria|
|## 2|||Capital expa|nsion, rate of growth, and employment (Re|
|## 3|||||
|##|year vol|ume numb|er page_start|page_end url journal journal_id volume_id|
|## 1|1946|17|0<br>409|431<br>1748<br>4170|
|## 2|1946|14|0<br>137|147<br>452<br>2723|
|## 3|1947|1|0<br>7|11<br>1746<br>273|
|##|issue_id|zmath i|d:1|name id:2 id_title:1 author_id|
|## 1|2|\n|1<br>Ander|son, T. W.\n<br>3<br>2<br>1|
|## 2|3|\n|3<br>Domar|, Evsey D.\n<br>4<br>3<br>3|
|## 3|4|\n|4 Tumbleson,|Robert C.\n<br>5<br>4<br>4|
|##|editor s|equence|publication_id|publication_type|
|## 1|f|0|1|Article\n|
|## 2|f|0|2|Article\n|
|## 3|f|0|3|Article\n|


**dbClearResult** (fullInfo)

## [1] TRUE

As seen above, you can also use _dbSendQuery()_ combined with _fetch()_ to pull in a fixed number of records at a time, if you’re working with a big database.

9

### **2.3 Details on joins**

A bit more on joins - as we saw with _merge()_ in R, there are various possibilities for how to do the merge depending on whether there are rows in one table that are not in another table. In other words, we need to think about whether the relationship between tables is one-to-one, one-to-many, or many-to-many. In database terminology an _inner join_ is when you get the rows for which there is data in both tables. A _left outer join_ gives all the rows from the first table but only those from the second table that match a row in the first table. A _right outer join_ is the reverse, while a _full outer join_ returns all rows from both tables. A _cross join_ gives the Cartesian product, namely the combination of every row from each table, analogous to _expand.grid()_ in R. However a _cross join_ with a _where_ statement can duplicate the result of an _inner join_ :

select * from table1 cross join table2 where table1.id = table2.id select * from table1 join table2 on table1.id = table2.id

### **2.4 Keys and indices**

A key is a field or collection of fields that gives a unique value for every row/observation. A table in a database should then have a primary key that is the main unique identifier used by the DBMS. Foreign keys are columns in one table that give the value of the primary key in another table.

An index is an ordering of rows based on one or more fields. DBMS use indices to look up values quickly. (Recall our discussion in Unit 6 on looking up values by name vs. index and the benefits of hashing.) So in general you want your tables to have indices. And having indices on the columns used in the matching for a join allows for quick joins. DBMS use indexing to provide sub-linear time lookup, so that lookup is faster than linear time ( _O_ ( _n_ ) when there are _n_ rows), which is what would occur if one had to look at each row sequentially. Lookup may be logarithmic [ _O_ ( _log_ ( _n_ ))] or constant time [ _O_ (1)]. A binary search is logarithmic while looking up based on numeric position is _O_ (1).

So if you’re working with a database and speed is important, check to see if there are indices.

### **2.5 Creating SQLite database tables from R**

I won’t do a full demo of this, but the basic syntax for this is as follows. You can read from a CSV to create the table or from an R dataframe. The following assumes you have two tables stored as CSVs, with one table of student info and one table of class info.

- dbWriteTable(conn = db, name = "student", value = "student.csv", row.names = FALSE, header = TRUE)

10

dbWriteTable(conn = db, name = "class", value = "class.csv", row.names = FALSE, header = TRUE)

---

[Up: contents](index.md) · [Unit 09 — bigData Part 02 — →](02-unit-09-bigdata-part-02.md)
