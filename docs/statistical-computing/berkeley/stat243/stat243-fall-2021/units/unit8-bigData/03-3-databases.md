---
title: 3 Databases
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit8-bigData.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit8-bigData.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Databases

This material is drawn from the tutorial on Working with large datasets in SQL, R, and Python, though I won’t hold you responsible for all of the database/SQL material in that tutorial, only what appears here in this Unit.

## 3.1 Overview

Basically, standard SQL databases are *relational databases* that are a collection of rectangular format datasets (*tables*, also called *relations*), with each table similar to R or Pandas data frames, in that a table is made up of columns, which are called *fields* or *attributes*, each containing a single type (numeric, character, date, currency, enumerated (i.e., categorical), ...) and rows or *records* containing the observations for one entity. Some of the tables in a given database will generally have fields in common so it makes sense to merge (i.e., *join*) information from multiple tables. E.g., you might have a database with a table of student information, a table of teacher information and a table of school information, and you might join student information with information about the teacher(s) who taught the students. Databases are set up to allow for fast querying and merging (called *joins* in database terminology).

Formally, databases are stored on disk, while R and Python store datasets in memory. This would suggest that databases will be slow to access their data but will be able to store more data than can be loaded into an R or Python session. However, databases can be quite fast due in part to disk caching by the operating system as well as careful implementation of good algorithms for database operations. For more information about disk caching see the tutorial.

## 3.2 Interacting with a database

You can interact with databases in a variety of database systems (DBMS=database management system). Some popular systems are SQLite, MySQL, PostgreSQL, Oracle and Microsoft Access. We’ll concentrate on accessing data in a database rather than management of databases. SQL is the Structured Query Language and is a special-purpose high-level language for managing databases and making queries. Variations on SQL are used in many different DBMS.

Queries are the way that the user gets information (often simply subsets of tables or information merged across tables). The result of an SQL query is in general another table, though in some cases it might have only one row and/or one column.

Many DBMS have a client-server model. Clients connect to the server, with some authentication, and make requests (i.e., queries).

There are often multiple ways to interact with a DBMS, including directly using command line tools provided by the DBMS or via Python or R, among others.

We’ll concentrate on SQLite (because it is simple to use on a single machine). SQLite is quite nice in terms of being self-contained - there is no server-client model, just a single file on your hard drive that stores the database and to which you can connect to using the SQLite shell, R, Python, etc. However, it does not have some useful functionality that other DBMS have. For example, you can’t use ALTER TABLE to modify column types or drop columns.

## 3.3 Database schema and normalization

To truly leverage the conceptual and computational power of a database you’ll want to have your data in a normalized form, which means spreading your data across multiple tables in such a way that you don’t repeat information unnecessarily.

The schema is the metadata about the tables in the database and the fields (and their types) in those tables.

Let’s consider this using an educational example. Suppose we have a school with multiple teachers teaching multiple classes and multiple students taking multiple classes. If we put this all in one table organized per student, the data might have the following fields:

* student ID
* student grade level
* student name
* class 1
* class 2
* ...
* class n
* grade in class 1
* grade in class 2
* ...
* grade in class n
* teacher ID 1
* teacher ID 2
* ...
* teacher ID n
* teacher name 1
* teacher name 2
* ...
* teacher name n
* teacher department 1
* teacher department 2
* ...
* teacher department n
* teacher age 1
* teacher age 2
* ...
* teacher age n

There are a lot of problems with this. We’ll list some in class:

1. ???
2. ???
3. ???
4. ???

It would get even worse if there was a field related to teachers for which a given teacher could have multiple values (e.g., teachers could be in multiple departments). This would lead to even more redundancy - each student-class-teacher combination would be crossed with all of the departments for the teacher (so-called multivalued dependency in database theory).

An alternative organization of the data would be to have each row represent the enrollment of a student in a class.

* student ID
* student name
* class
* grade in class
* student grade level
* teacher ID
* teacher department
* teacher age

This has some advantages relative to our original organization in terms of not having empty data slots, but it doesn’t solve the other three issues above.

Instead, a natural way to order this database is with the following tables.

* Student
  – ID
  – name
  – grade_level
* Teacher
  – ID
  – name
  – department
  – age
* Class
  – ID
  – topic
  – class_size
  – teacher_ID
* ClassAssignment
  – student_ID
  – class_ID
  – grade

Then we do queries to pull information from multiple tables. We do the joins based on keys, which are the fields in each table that allow us to match rows from different tables.

(That said, if all anticipated uses of a database will end up recombining the same set of tables, we may want to have a denormalized schema in which those tables are actually combined in the database. It is possible to be too pure about normalization! We can also create a virtual table, called a *view*, as discussed later.)

### 3.3.1 Keys

A key is a field or collection of fields that give(s) a unique value for every row/observation. A table in a database should then have a *primary key* that is the main unique identifier used by the DBMS. *Foreign keys* are columns in one table that give the value of the primary key in another table. When information from multiple tables is joined together, the matching of a row from one table to a row in another table is generally done by equating the primary key in one table with a foreign key in a different table.

In our educational example, the primary keys would presumably be: *Student.ID*, *Teacher.ID*, *Class.ID*, and for ClassAssignment two fields: {*ClassAssignment.studentID*, *ClassAssignment.class_ID*}. Some examples of foreign keys would be:

* student_ID as the foreign key in ClassAssignment for joining with Student on Student.ID
* teacher_ID as the foreign key in Class for joining with Teacher based on Teacher.ID
* class_ID as the foreign key in ClassAssignment for joining with Class based on Class.ID

### 3.3.2 Queries that join data across multiple tables

Suppose we want a result that has the grades of all students in 9th grade. For this we need information from the Student table (to determine grade level) and information from the ClassAssignment table (to determine the class grade). More specifically we need a query that joins Student with ClassAssignment based on Student.ID and ClassAssignment.student_ID and filters the rows based on Student.grade_level:

```sql
SELECT Student.ID, grade FROM Student, ClassAssignment WHERE
Student.ID = ClassAssignment.student_ID and Student.grade_level
= 9;
```

Note that the query is a join (specifically an *inner join*), which is like `merge()` in R. We don’t specifically use the JOIN keyword, but one could do these queries explicitly using JOIN, as we’ll see later.

## 3.4 Stack Overflow metadata example

I’ve obtained data from Stack Overflow, the popular website for asking coding questions, and placed it into a normalized database. The SQLite version has metadata (i.e., it lacks the actual text of the questions and answers) on all of the questions and answers posted in 2016.

We’ll explore SQL functionality using this example database.

Now let’s consider the Stack Overflow data. Each question may have multiple answers and each question may have multiple (topic) tags.

If we tried to put this into a single table, the fields could look like this if we have one row per question:

* question ID
* ID of user submitting question
* question title
* tag 1
* tag 2
* ...
* tag n
* answer 1 ID
* ID of user submitting answer 1
* age of user submitting answer 1
* name of user submitting answer 1
* answer 2 ID
* ID of user submitting answer 2
* age of user submitting answer 2
* name of user submitting answer 2
* ...

or like this if we have one row per question-answer pair:

* question ID
* ID of user submitting question
* question title
* tag 1
* tag 2
* ...
* tag n
* answer ID
* ID of user submitting answer
* age of user submitting answer
* name of user submitting answer

As we’ve discussed neither of those schema is particularly desirable.

**Challenge**: How would you devise a schema to normalize the data. I.e., what set of tables do you think we should create?

You can view one reasonable schema in the file *normalized_example.png*. The lines between tables indicate the relationship of foreign keys in one table to primary keys in another table. The schema in the actual databases of Stack Overflow data we’ll use in this tutorial is similar to but not identical to that.

You can download a copy of the SQLite version of the Stack Overflow 2016 database from http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2016.db.

## 3.5 Accessing databases in R

The *DBI* package provides a front-end for manipulating databases from a variety of DBMS (SQLite, MySQL, PostgreSQL, among others). Basically, you tell the package what DBMS is being used on the back-end, link to the actual database, and then you can use the standard functions in the package regardless of the back-end. This is a similar style to how one uses *foreach* for parallelization.

With SQLite, R processes make calls against the stand-alone SQLite database (.db) file, so there are no SQLite-specific processes. With a client-server DBMS like PostgreSQL, R processes call out to separate Postgres processes; these are started from the overall Postgres background process

You can access and navigate an SQLite database from R as follows.

```r
library(RSQLite)
drv <- dbDriver("SQLite")
dir <- '../data' # relative or absolute path to where the .db file is
dbFilename <- 'stackoverflow-2016.db'
db <- dbConnect(drv, dbname = file.path(dir, dbFilename))
# simple query to get 5 rows from a table
dbGetQuery(db, "select * from questions limit 5")
```

```
##   questionid        creationdate score viewcount
## 1   34552550 2016-01-01 00:00:03     0       108
## 2   34552551 2016-01-01 00:00:07     1       151
## 3   34552552 2016-01-01 00:00:39     2      1942
## 4   34552554 2016-01-01 00:00:50     0       153
## 5   34552555 2016-01-01 00:00:51    -1        54
##                                                                                      title
## 1                                                                     Scope between methods
## 2 Rails - Unknown Attribute - Unable to add a new field to a form on create/update
## 3 Selenium Firefox webdriver won't load a blank page after changing Firefox preferences
## 4                                                              Android Studio styles.xml Error
## 5                    Java: reference to non-finial local variables inside a thread
##   ownerid
## 1 5684416
## 2 2457617
## 3 5732525
## 4 5735112
## 5 4646288
```

```
## http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2016.db
```

We can easily see the tables and their fields:

```r
dbListTables(db)
```

```
## [1] "answers"        "questions"      "questions_tags" "users"
```

```r
dbListFields(db, "questions")
```

```
## [1] "questionid"   "creationdate" "score"        "viewcount"    "title"
## [6] "ownerid"
```

```r
dbListFields(db, "answers")
```

```
## [1] "answerid"     "questionid"   "creationdate" "score"        "ownerid"
```

Here’s how to make a basic SQL query. One can either make the query and get the results in one go or make the query and separately fetch the results. Here we’ve selected the first five rows (and all columns, based on the `*` wildcard) and brought them into R as a data frame.

```r
results <- dbGetQuery(db, 'select * from questions limit 5')
class(results)
```

```
## [1] "data.frame"
```

```r
query <- dbSendQuery(db, "select * from questions")
results2 <- fetch(query, 5)
identical(results, results2)
```

```
## [1] TRUE
```

```r
dbClearResult(query) # clear to prepare for another query
```

To disconnect from the database:

```r
dbDisconnect(db)
```

## 3.6 Basic SQL for choosing rows and columns from a table

SQL is a declarative language that tells the database system what results you want. The system then parses the SQL syntax and determines how to implement the query.

Here are some examples using the Stack Overflow database.

```r
## find the largest viewcounts in the questions table
dbGetQuery(db,
'select title, viewcount from questions order by viewcount desc limit 10')
```

```
##                                                                                                                         title
## 1                                      How to solve "server DNS address could not be found" error in windows 10?
## 2  Code signing is required for product type 'Application' in SDK 'iOS 10.0' - StickerPackExtension requires a development team error
## 3                                                                          "Gradle Version 2.10 is required." Error
## 4                               Android- Error:Execution failed for task ':app:transformClassesWithDexForRelease'
## 5                                            Fatal error: Uncaught Error: Call to undefined function mysql_connect()
## 6                                                                 Unsupported major.minor version 52.0 in my app
## 7                                             Response to preflight request doesn't pass access control check AngularJs
## 8                                                          NPM vs. Bower vs. Browserify vs. Gulp vs. Grunt vs. Webpack
## 9                                                                             Git refusing to merge unrelated histories
## 10                                                     "SyntaxError: Unexpected token < in JSON at position 0" in React App
##    viewcount
## 1     196469
## 2     174790
## 3     134399
## 4     129874
## 5     129624
## 6     127764
## 7     126752
## 8     112000
## 9     109422
## 10    106995
```

```r
## now get the questions that are viewed the most
dbGetQuery(db, 'select * from questions where viewcount > 100000')
```

```
##    questionid        creationdate score viewcount
## 1    34579099 2016-01-03 16:55:16     8    129624
## 2    34814368 2016-01-15 15:24:36   206    134399
## 3    35062852 2016-01-28 13:28:39   730    112000
## 4    35429801 2016-02-16 10:21:09   400    100125
## 5    35588699 2016-02-23 21:37:06    57    126752
## 6    35890257 2016-03-09 11:25:05    51    129874
## 7    35990995 2016-03-14 15:01:17   104    127764
## 8    36668374 2016-04-16 18:57:19    20    196469
## 9    37280274 2016-05-17 15:21:49    23    106995
## 10   37806538 2016-06-14 08:16:21   223    174790
## 11   37937984 2016-06-21 07:23:00   202    109422
##                                                                                                   title
## 1                              Fatal error: Uncaught Error: Call to undefined function mysql_connect()
## 2                                                              "Gradle Version 2.10 is required." Error
## 3                                           NPM vs. Bower vs. Browserify vs. Gulp vs. Grunt vs. Webpack
## 4                                                  This action could not be completed. Try Again (-22421)
## 5                              Response to preflight request doesn't pass access control check AngularJs
## 6                                Android- Error:Execution failed for task ':app:transformClassesWithDexForRelease'
## 7                                                                  Unsupported major.minor version 52.0 in my app
## 8                                       How to solve "server DNS address could not be found" error in windows 10?
## 9                                                      "SyntaxError: Unexpected token < in JSON at position 0" in React App
## 10 Code signing is required for product type 'Application' in SDK 'iOS 10.0' - StickerPackExtension requires a development team error
## 11                                                                              Git refusing to merge unrelated histories
##    ownerid
## 1  3656666
## 2  3319176
## 3  2761509
## 4  5881764
## 5  2896963
## 6  1118886
## 7  1629278
## 8  1707976
## 9  4043633
## 10 1554347
## 11 2670370
```

Let’s lay out the various verbs in SQL. Here’s the form of a standard query (though the ORDER BY is often omitted and sorting is computationally expensive):

```sql
SELECT <column(s)> FROM <table> WHERE <condition(s) on column(s)>
ORDER BY <column(s)>
```

SQL keywords are often written in ALL CAPITALS though I won’t necessarily do that here.

And here is a table of some important keywords:

*Table 1. Basic SQL keywords.*

| Keyword | Usage |
| :--- | :--- |
| SELECT | select columns |
| FROM | which table to operate on |
| WHERE | filter (choose) rows satisfying certain conditions |
| LIKE, IN, <, >, ==, etc. | used as part of conditions |
| ORDER BY | sort based on columns |

For comparisons in a WHERE clause, some common syntax for setting conditions includes LIKE (for patterns), =, >, <, >=, <=, !=.

Some other keywords are: DISTINCT, ON, JOIN, GROUP BY, AS, USING, UNION, INTERSECT, SIMILAR TO.

**Question**: how would we find the youngest users in the database?

## 3.7 Grouping / stratifying

A common pattern of operation is to stratify the dataset, i.e., collect it into mutually exclusive and exhaustive subsets. One would then generally do some operation on each subset. In SQL this is done with the GROUP BY keyword.

Here’s a basic example where we count the occurrences of different tags.

```r
dbGetQuery(db, "select tag, count(*) as n from questions_tags
group by tag order by n desc limit 25")
```

```
##           tag      n
## 1  javascript 290966
## 2        java 219155
## 3     android 184272
## 4         php 177969
## 5      python 171745
## 6          c# 163637
## 7        html 126851
## 8      jquery 123707
## 9         ios  95722
## 10        css  86470
## 11  angularjs  76951
## 12        c++  76260
## 13      mysql  75458
## 14      swift  61485
## 15        sql  58346
## 16    node.js  52827
## 17          r  48079
## 18     arrays  46739
## 19       json  45250
## 20 ruby-on-rails 39036
## 21 sql-server  37077
## 22          c  36080
## 23    asp.net  35610
## 24      excel  29924
## 25   angular2  28832
```

In general ‘GROUP BY‘ statements will involve some aggregation operation on the subsets. Options include: COUNT, MIN, MAX, AVG, SUM.

**Challenge**: Write a query that will count the number of answers for each question, returning the most answered questions.

## 3.8 Getting unique results (DISTINCT)

A useful SQL keyword is DISTINCT, which allows you to eliminate duplicate rows from any table (or remove duplicate values when one only has a single column or set of values).

```r
tagNames <- dbGetQuery(db, "select distinct tag from questions_tags")
head(tagNames)
```

```
##     tag
## 1    c#
## 2 razor
## 3 flags
## 4 javascript
## 5      rxjs
## 6   node.js
```

```r
dbGetQuery(db, "select count(distinct tag) from questions_tags")
```

```
##   count(distinct tag)
## 1               41006
```

## 3.9 Simple SQL joins

Often to get the information we need, we’ll need data from multiple tables. To do this we’ll need to do a database join, telling the database what columns should be used to match the rows in the different tables.

The syntax generally looks like this (again the WHERE and ORDER BY are optional):

```sql
SELECT <column(s)> FROM <table1> JOIN <table2> ON <columns to match
on> WHERE <condition(s) on column(s)> ORDER BY <column(s)>
```

Let’s see some joins using the different syntax on the Stack Overflow database. In particular let’s select only the questions with the tag "python".

```r
result1 <- dbGetQuery(db, "select * from questions join questions_tags
on questions.questionid = questions_tags.questionid
where tag = 'python'")
```

It turns out you can do it without using the JOIN keyword.

```r
result2 <- dbGetQuery(db, "select * from questions, questions_tags
where questions.questionid = questions_tags.questionid and
tag = 'python'")

head(result1)
```

```
##   questionid        creationdate score viewcount
## 1   34553559 2016-01-01 04:34:34     3        96
## 2   34556493 2016-01-01 13:22:06     2        30
## 3   34557898 2016-01-01 16:36:04     3       143
## 4   34560088 2016-01-01 21:10:32     1       126
## 5   34560213 2016-01-01 21:25:26     1       127
## 6   34560740 2016-01-01 22:37:36     0       455
##                                                                                              title
## 1                                              Python nested loops only working on the first pass
## 2                                             bool operator in for Timestamp in Series does not work
## 3                                                      Pairwise haversine distance calculation
## 4                                                        Stopwatch (chronometre) doesn't work
## 5 How to set the type of a pyqtSignal (variable of class X) that takes a X instance as argument
## 6                                                    Flask: Peewee model_to_dict helper not working
##   ownerid questionid    tag
## 1  845642   34553559 python
## 2 4458602   34556493 python
## 3 2927983   34557898 python
## 4 5736692   34560088 python
## 5 5636400   34560213 python
## 6 3262998   34560740 python
```

```r
identical(result1, result2)
```

```
## [1] TRUE
```

Here’s a three-way join (using both types of syntax) with some additional use of aliases to abbreviate table names. What does this query ask for?

```r
result1 <- dbGetQuery(db, "select * from
questions Q
join questions_tags T on Q.questionid = T.questionid
join users U on Q.ownerid = U.userid
where tag = 'python' and
age > 60")

result2 <- dbGetQuery(db, "select * from
questions Q, questions_tags T, users U where
Q.questionid = T.questionid and
Q.ownerid = U.userid and
tag = 'python' and
age > 60")

identical(result1, result2)
```

```
## [1] TRUE
```

**Challenge**: Write a query that would return all the answers to questions with the Python tag.

**Challenge**: Write a query that would return the users who have answered a question with the Python tag.

## 3.10 Temporary tables and views

You can think of a view as a temporary table that is the result of a query and can be used in subsequent queries. In any given query you can use both views and tables. The advantage is that they provide modularity in our querying. For example, if a given operation (portion of a query) is needed repeatedly, one could abstract that as a view and then make use of that view.

Suppose we always want the age and displayname of owners of questions to be readily available. Once we have the view we can query it like a regular table.

```r
## note there is a creationdate in users too, hence disambiguation
dbExecute(db, "create view questionsAugment as select
questionid, questions.creationdate, score, viewcount,
title, ownerid, age, displayname
from questions join users
on questions.ownerid = users.userid")
```

```
## [1] 0
```

```r
## you'll see the return value is '0'

dbGetQuery(db, "select * from questionsAugment where age < 15 limit 5")
```

```
##   questionid        creationdate score viewcount
## 1   34587110 2016-01-04 08:23:32     1        63
## 2   34634653 2016-01-06 13:45:22     0       372
## 3   35240563 2016-02-06 11:39:26     2        46
## 4   35330718 2016-02-11 04:19:39     0        36
## 5   35335506 2016-02-11 09:36:50     0       108
##                                                                             title ownerid age
## 1                                How to set the selected item of UITabBar by code 5034145  13
## 2                              WooCommerce is complaining about wrong consumer key 5034145  13
## 3                Cannot receive post parameter using forms created by PHP echo 5034145  13
## 4                                    How to test whether two color are equivalent 5034145  13
## 5 How to set custom dismissal animation for UIViewController 5034145  13
##   displayname
## 1    Tom Shen
## 2    Tom Shen
## 3    Tom Shen
## 4    Tom Shen
## 5    Tom Shen
```

One use of a view would be to create a mega table that stores all the information from multiple tables in the (unnormalized) form you might have if you simply had one data frame in R or Python.

## 3.11 More on joins

We’ve seen a bunch of joins but haven’t discussed the full taxonomy of types of joins. There are various possibilities for how to do a join depending on whether there are rows in one table that do not match any rows in another table.

**Inner joins**: In database terminology an inner join is when the result has a row for each match of a row in one table with the rows in the second table, where the matching is done on the columns you indicate. If a row in one table corresponds to more than one row in another table, you get all of the matching rows in the second table, with the information from the first table duplicated for each of the resulting rows. For example in the Stack Overflow data, an inner join of questions and answers would pair each question with each of the answers to that question. However, questions without any answers or (if this were possible) answers without a corresponding question would not be part of the result.

**Outer joins**: Outer joins add additional rows from one table that do not match any rows from the other table as follows. A *left outer join* gives all the rows from the first table but only those from the second table that match a row in the first table. A *right outer join* is the converse, while a *full outer join* includes at least one copy of all rows from both tables. So a left outer join of the Stack Overflow questions and answers tables would, in addition to the matched questions and their answers, include a row for each question without any answers, as would a full outer join. In this case there should be no answers that do not correspond to question, so a right outer join should be the same as an inner join.

**Cross joins**: A cross join gives the Cartesian product of the two tables, namely the pairwise combination of every row from each table, analogous to `expand.grid()` in R. I.e., take a row from the first table and pair it with each row from the second table, then repeat that for all rows from the first table. Since cross joins pair each row in one table with all the rows in another table, the resulting table can be quite large (the product of the number of rows in the two tables). In the Stack Overflow database, a cross join would pair each question with every answer in the database, regardless of whether the answer is an answer to that question.

Simply listing two or more tables separated by commas as we saw earlier is the same as a *

---

[← 2 Hadoop, MapReduce, Spark, and Dask](02-2-hadoop-mapreduce-spark-and-dask.md) · [Up: contents](index.md)
