---
title: 'count(distinct tag) ## 1 41006'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# count(distinct tag) ## 1 41006

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

17

### **2.10 Indexes**

An index is an ordering of rows based on one or more fields. DBMS use indexes to look up values quickly, either when filtering (if the index is involved in the WHERE condition) or when doing joins (if the index is involved in the JOIN condition). So in general you want your tables to have indexes.

DBMS use indexing to provide sub-linear time lookup. Without indexes, a database needs to scan through every row sequentially, which is called linear time lookup – if there are n rows, the lookup is O(n) in computational cost. With indexes, lookup may be logarithmic – O(log(n)) – (if using tree-based indexes) or constant time – O(1) – (if using hash-based indexes). A binary treebased search is logarithmic; at each step through the tree you can eliminate half of the possibilities.

Here’s how we create an index, with some time comparison for a simple query.

**system.time** ( **dbGetQuery** (db, "select * from questions where viewcount > 10000")) _# 10 seconds_ **system.time** ( **dbGetQuery** (db,

"create index count_index on questions (viewcount)")) _# 19 seconds_ **system.time** ( **dbGetQuery** (db, "select * from questions where viewcount > 10000")) _# 3 seconds_

In other contexts, an index can save huge amounts of time. So if you’re working with a database and speed is important, check to see if there are indexes.

That being said, using indexes in a lookup is not always advantageous, as discussed in the tutorial.

### **2.11 Temporary tables and views**

You can think of a view as a temporary table that is the result of a query and can be used in subsequent queries. In any given query you can use both views and tables. The advantage is that they provide modularity in our querying. For example, if a given operation (portion of a query) is needed repeatedly, one could abstract that as a view and then make use of that view.

Suppose we always want the age and displayname of owners of questions to be readily available. Once we have the view we can query it like a regular table.

_## note there is a creationdate in users too, hence disambiguation_ **dbGetQuery** (db, "create view questionsAugment as select

questionid, questions.creationdate, score, viewcount, title, ownerid, age, displayname

18

from questions join users on questions.ownerid = users.userid")

**## Error in result_create(conn@ptr, statement): table questionsAugment already exists**

_## don't be confused by the "data frame with 0 columns and 0 rows" ## message -- it just means that nothing is returned to R; ## the view HAS been created_

**dbGetQuery** (db, "select * from questionsAugment where age < 15 limit 5") ## questionid creationdate score viewcount ## 1 38096075 2016-06-29 09:50:36 0 23 ## 2 38899284 2016-08-11 14:32:39 0 33 ## 3 40051364 2016-10-14 20:18:18 1 37 ## 4 37168422 2016-05-11 16:29:16 0 212 ## 5 37188786 2016-05-12 13:43:41 0 25 ## ## 1 Iterate over an enum, which saves classes, then init the classes ## 2 Spark Framework puts ## 3 OpenShift Maven does not use ## 4 Theming an ASP.net menu ## 5 Using IIS7 Url rewrite module to redirect ## ownerid age displayname ## 1 3809164 14 ArsenArsen ## 2 3809164 14 ArsenArsen ## 3 3809164 14 ArsenArsen ## 4 3932721 14 Bob ## 5 3932721 14 Bob

and put puts HTML use the menu control

redirect

One use of a view would be to create a mega table that stores all the information from multiple tables in the (unnormalized) form you might have if you simply had one data frame in R or Python.

### **2.12 Creating database tables**

One can create tables from within the ‘sqlite‘ command line interfaces (discussed in the tutorial), but often one would do this from R or Python. Here’s the syntax from R.

19

_## Option 1: pass directly from CSV to database_ **dbWriteTable** (conn = db, name = "student", value = "student.csv", row.names = FALSE, header = TRUE) _## Option 2: pass from data in an R data frame ## create data frame 'student' in some fashion #student <- data.frame(...) #student <- read.csv(...)_ **dbWriteTable** (conn = db, name = "student", value = student, row.names = FALSE, append = FALSE)

### **2.13 More on joins**

We’ve seen a bunch of joins but haven’t discussed the full taxonomy of types of joins. There are various possibilities for how to do a join depending on whether there are rows in one table that do not match any rows in another table.

**Inner joins** : In database terminology an inner join is when the result has a row for each match of a row in one table with the rows in the second table, where the matching is done on the columns you indicate. If a row in one table corresponds to more than one row in another table, you get all of the matching rows in the second table, with the information from the first table duplicated for each of the resulting rows. For example in the Stack Overflow data, an inner join of questions and answers would pair each question with each of the answers to that question. However, questions without any answers or (if this were possible) answers without a corresponding question would not be part of the result.

**Outer joins** : Outer joins add additional rows from one table that do not match any rows from the other table as follows. A _left outer join_ gives all the rows from the first table but only those from the second table that match a row in the first table. A _right outer join_ is the converse, while a _full outer join_ includes at least one copy of all rows from both tables. So a left outer join of the Stack Overflow questions and answers tables would, in addition to the matched questions and their answers, include a row for each question without any answers, as would a full outer join. In this case there should be no answers that do not correspond to question, so a right outer join should be the same as an inner join.

**Cross joins** : A cross join gives the Cartesian product of the two tables, namely the pairwise combination of every row from each table, analogous to _expand.grid()_ in R. I.e., take a row from the first table and pair it with each row from the second table, then repeat that for all rows from the first table. Since cross joins pair each row in one table with all the rows in another table, the

20

resulting table can be quite large (the product of the number of rows in the two tables). In the Stack Overflow database, a cross join would pair each question with every answer in the database, regardless of whether the answer is an answer to that question.

Simply listing two or more tables separated by commas as we saw earlier is the same as a _cross join_ . Alternatively, listing two or more tables separated by commas, followed by conditions that equate rows in one table to rows in another is the same as an _inner join_ .

In general, inner joins can be seen as a form of cross join followed by a condition that enforces matching between the rows of the table. More broadly, here are four equivalent joins that all perform the equivalent of an inner join:

---

[← tag ## 1 c# ## 2 razor ## 3 flags ## 4 javascript ## 5 rxjs ## 6 node.js](09-tag-1-c-2-razor-3-flags-4-javascript-5-rxjs-6-node-js.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 11 — →](11-unit-07-bigdata-part-11.md)
