---
title: data frame with 0 columns and 0 rows
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# data frame with 0 columns and 0 rows

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_## don't be confused by the "data frame with 0 columns and 0 rows" ## message -- it just means that nothing is returned to R; ## the view HAS been created_

**dbGetQuery** (db, "select * from questionsAugment where age < 15 limit 5") ## questionid creationdate score viewcount ## 1 38096075 2016-06-29 09:50:36 0 23 ## 2 38899284 2016-08-11 14:32:39 0 33 ## 3 40051364 2016-10-14 20:18:18 1 37 ## 4 37168422 2016-05-11 16:29:16 0 212 ## 5 37188786 2016-05-12 13:43:41 0 25 ## ## 1 Iterate over an enum, which saves classes, then init the classes ## 2 Spark Framework puts ## 3 OpenShift Maven does not use ## 4 Theming an ASP.net menu ## 5 Using IIS7 Url rewrite module to redirect ## ownerid age displayname ## 1 3809164 14 ArsenArsen ## 2 3809164 14 ArsenArsen ## 3 3809164 14 ArsenArsen ## 4 3932721 14 Bob ## 5 3932721 14 Bob

and put

puts HTML use the menu control

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

[← count(distinct tag) ## 1 41006](11-count-distinct-tag-1-41006.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 13 — →](13-unit-08-bigdata-part-13.md)
