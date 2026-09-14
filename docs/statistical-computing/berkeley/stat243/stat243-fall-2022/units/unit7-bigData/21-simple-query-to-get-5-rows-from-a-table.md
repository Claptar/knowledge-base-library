---
title: simple query to get 5 rows from a table
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# simple query to get 5 rows from a table

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

dbGetQuery(db, "select * from questions limit 5")

## http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2016.db
```


We can easily see the tables and their fields:

```r
dbListTables(db)
dbListFields(db, "questions")
dbListFields(db, "answers")
```


Here's how to make a basic SQL query. One can either make the query and
get the results in one go or make the query and separately fetch the
results. Here we've selected the first five rows (and all columns, based
on the \* wildcard) and brought them into R as a data frame.

```r
results <- dbGetQuery(db, 'select * from questions limit 5')
class(results)

query <- dbSendQuery(db, "select * from questions")
results2 <- fetch(query, 5)
identical(results, results2)
dbClearResult(query)  # clear to prepare for another query
```


To disconnect from the database:

```r
dbDisconnect(db)
```


## Basic SQL for choosing rows and columns from a table

SQL is a declarative language that tells the database system what
results you want. The system then parses the SQL syntax and determines
how to implement the query.

> **Note**: An *imperative* language is one where you provide the sequence of commands you want to be run, in order. A *declarative* language is one where you declare what result you want and rely on the system that interprets the commands how to actually do it. Most of the languages we're generally familiar with are imperative.

Here are some examples using the Stack Overflow database.

```r
## find the largest viewcounts in the questions table
dbGetQuery(db,
'select title, viewcount from questions order by viewcount desc limit 10')
## now get the questions that are viewed the most
dbGetQuery(db, 'select * from questions where viewcount > 100000')
```


Let's lay out the various verbs in SQL. Here's the form of a standard
query (though the ORDER BY is often omitted and sorting is
computationally expensive):

```
SELECT <column(s)> FROM <table> WHERE <condition(s) on column(s)> ORDER BY <column(s)>
```

SQL keywords are often written in ALL CAPITALS, although I won't
necessarily do that here.

And here is a table of some important keywords:

|            Keyword          |                         Usage  |
|  ----------------------------| ----------------------------------------------------|
|             SELECT           |                    select columns   |
|              FROM            |              which table to operate on   |
|             WHERE            |  filter (choose) rows satisfying certain conditions   |
|   LIKE, IN, \<, \>, ==, etc. |              used as part of conditions   |
|            ORDER BY          |                sort based on columns   |


For comparisons in a `WHERE` clause, some common syntax for setting
conditions includes `LIKE` (for patterns), `=`, `>`, `<`, `>=`, `<=`, `!=`.

Some other keywords are: `DISTINCT`, `ON`, `JOIN`, `GROUP BY`, `AS`, `USING`, `UNION`,
`INTERSECT`, `SIMILAR TO`.

**Question**: how would we find the oldest users in the database?

## Grouping / stratifying

A common pattern of operation is to stratify the dataset, i.e., collect
it into mutually exclusive and exhaustive subsets. One would then
generally do some operation on each subset. In SQL this is done with the
GROUP BY keyword.

Here's a basic example where we count the occurrences of different tags.
Note that we use `as` to define a name for the new column that is
created based on the aggregation operation (`count` in this case).

```r
dbGetQuery(db, "select tag, count(*) as n from questions_tags
                group by tag order by n desc limit 25")
```


In general `GROUP BY` statements will involve some aggregation operation
on the subsets. Options include: `COUNT`, `MIN`, `MAX`, `AVG`, `SUM`.

If you filter after using `GROUP BY`, you need to use `having` instead of `where`.

**Challenge**: Write a query that will count the number of answers for
each question, returning the most answered questions.

## Getting unique results (DISTINCT)

A useful SQL keyword is `DISTINCT`, which allows you to eliminate
duplicate rows from any table (or remove duplicate values when one only
has a single column or set of values).

```r
tagNames <- dbGetQuery(db, "select distinct tag from questions_tags")
head(tagNames)
dbGetQuery(db, "select count(distinct tag) from questions_tags")
```


## Simple SQL joins

Often to get the information we need, we'll need data from multiple
tables. To do this we'll need to do a database join, telling the
database what columns should be used to match the rows in the different
tables.

The syntax generally looks like this (again the `WHERE` and `ORDER BY` are
optional):

```
SELECT <column(s)> FROM <table1> JOIN <table2> ON <columns to match on> WHERE <condition(s) on column(s)> ORDER BY <column(s)>
```

Let's see some joins using the different syntax on the Stack Overflow
database. In particular let's select only the questions with the tag
python.

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
identical(result1, result2)
```


Here's a three-way join (using both types of syntax) with some
additional use of aliases to abbreviate table names. What does this
query ask for?

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


**Challenge**: Write a query that would return all the answers to
questions with the Python tag.

**Challenge**: Write a query that would return the users who have
answered a question with the Python tag.

## Temporary tables and views

You can think of a view as a temporary table that is the result of a
query and can be used in subsequent queries. In any given query you can
use both views and tables. The advantage is that they provide modularity
in our querying. For example, if a given operation (portion of a query)
is needed repeatedly, one could abstract that as a view and then make
use of that view.

Suppose we always want the age and displayname of owners of questions to
be readily available. Once we have the view we can query it like a
regular table.

```r
dbExecute(db, "create view questionsAugment as select
                questionid, questions.creationdate, score, viewcount,
                title, ownerid, age, displayname
                from questions join users
                on questions.ownerid = users.userid")
## you'll see the return value is '0'

dbGetQuery(db, "select * from questionsAugment where age > 70 limit 5")
```


One use of a view would be to create a mega table that stores all the
information from multiple tables in the (unnormalized) form you might
have if you simply had one data frame in R or Python.

```r
dbExecute(db, "drop view if exists questionsAugment") # drop so can create again in next step
```

## More on joins

We've seen a bunch of joins but haven't discussed the full taxonomy of
types of joins. There are various possibilities for how to do a join
depending on whether there are rows in one table that do not match any
rows in another table.

**Inner joins**: In database terminology an inner join is when the
result has a row for each match of a row in one table with the rows in
the second table, where the matching is done on the columns you
indicate. If a row in one table corresponds to more than one row in
another table, you get all of the matching rows in the second table,
with the information from the first table duplicated for each of the
resulting rows. For example in the Stack Overflow data, an inner join of
questions and answers would pair each question with each of the answers
to that question. However, questions without any answers or (if this
were possible) answers without a corresponding question would not be
part of the result.

**Outer joins**: Outer joins add additional rows from one table that do
not match any rows from the other table as follows. A *left outer join*
gives all the rows from the first table but only those from the second
table that match a row in the first table. A *right outer join* is the
converse, while a *full outer join* includes at least one copy of all
rows from both tables. So a left outer join of the Stack Overflow
questions and answers tables would, in addition to the matched questions
and their answers, include a row for each question without any answers,
as would a full outer join. In this case there should be no answers that
do not correspond to question, so a right outer join should be the same
as an inner join.

**Cross joins**: A cross join gives the Cartesian product of the two
tables, namely the pairwise combination of every row from each table,
analogous to `expand.grid()` in R. I.e., take a row from the first table
and pair it with each row from the second table, then repeat that for
all rows from the first table. Since cross joins pair each row in one
table with all the rows in another table, the resulting table can be
quite large (the product of the number of rows in the two tables). In
the Stack Overflow database, a cross join would pair each question with
every answer in the database, regardless of whether the answer is an
answer to that question.

Simply listing two or more tables separated by commas as we saw earlier
is the same as a *cross join*. Alternatively, listing two or more tables
separated by commas, followed by conditions that equate rows in one
table to rows in another is equivalent to an *inner join*.

In general, inner joins can be seen as a form of cross join followed by
a condition that enforces matching between the rows of the table. More
broadly, here are four equivalent joins that all perform the equivalent
of an inner join:

```
## explicit inner join:
select * from table1 join table2 on table1.id = table2.id
## non-explicit join without JOIN
select * from table1, table2 where table1.id = table2.id
## cross-join followed by matching
select * from table1 cross join table2 where table1.id = table2.id
## explicit inner join with 'using'
select * from table1 join table2 using(id)
```

**Challenge**: Create a view with one row for every question-tag pair,
including questions without any tags.

**Challenge**: Write a query that would return the displaynames of all
of the users who have *never* posted a question. The NULL keyword will
come in handy it's like 'NA' in R. Hint: NULLs should be produced if you
do an outer join.

## Indexes

An index is an ordering of rows based on one or more fields. DBMS use
indexes to look up values quickly, either when filtering (if the index
is involved in the `WHERE` condition) or when doing joins (if the index is
involved in the `JOIN` condition). So in general you want your tables to
have indexes.

DBMS use indexing to provide sub-linear time lookup. Without indexes, a
database needs to scan through every row sequentially, which is called
linear time lookup if there are n rows, the lookup is O(n) in
computational cost. With indexes, lookup may be logarithmic O(log(n))
(if using tree-based indexes) or constant time O(1) (if using hash-based
indexes). A binary tree-based search is logarithmic; at each step
through the tree you can eliminate half of the possibilities.

Here's how we create an index, with some time comparison for a simple
query.

```r
system.time(dbGetQuery(db,
  "select * from questions where viewcount > 10000"))   # 10 seconds
system.time(dbExecute(db,
  "create index count_index on questions (viewcount)")) # 19 seconds
system.time(dbGetQuery(db,
  "select * from questions where viewcount > 10000"))   # 3 seconds

```

In other contexts, an index can save huge amounts of time. So if you're
working with a database and speed is important, check to see if there
are indexes. That said, as seen above it takes time to create the index,
so you'd only want to create it if you were doing multiple queries
that could take advantage of the index. See the databases tutorial
for more discussion of how using indexes in a lookup is not always advantageous.

## Creating database tables

One can create tables from within the 'sqlite' command line interfaces
(discussed in the tutorial), but often one would do this from R or
Python. Here's the syntax from R.

```r
## Option 1: pass directly from CSV to database
dbWriteTable(conn = db, name = "student", value = "student.csv",
             row.names = FALSE, header = TRUE)

## Option 2: pass from data in an R data frame
## create data frame 'student' in some fashion
#student <- data.frame(...)
#student <- read.csv(...)
dbWriteTable(conn = db, name = "student", value = student,
             row.names = FALSE, append = FALSE)
```

---

[← 3. Databases](20-3-databases.md) · [Up: contents](index.md) · [4. Sparsity →](22-4-sparsity.md)
