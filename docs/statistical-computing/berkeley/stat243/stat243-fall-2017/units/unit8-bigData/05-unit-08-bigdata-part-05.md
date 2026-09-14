---
title: Unit 08 — bigData Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 05 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To disconnect from the database:

11

**<mark>dbDisconnect</mark>** <mark>(db)</mark>

### **2.6 Basic SQL for choosing rows and columns from a table**

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


_## now get the questions that are viewed the most_

**dbGetQuery** (db, 'select * from questions where viewcount > 100000')

|##|questionid|cre|ationdate score|viewcount|
|---|---|---|---|---|
|## 1|34579099|2016-01-03|16:55:16<br>8|129624|
|## 2|34814368|2016-01-15|15:24:36<br>206|134399|
|## 3|35062852|2016-01-28|13:28:39<br>730|112000|
|## 4|35429801|2016-02-16|10:21:09<br>400|100125|
|## 5|35588699|2016-02-23|21:37:06<br>57|126752|
|## 6|35890257|2016-03-09|11:25:05<br>51|129874|
|## 7|35990995|2016-03-14|15:01:17<br>104|127764|
|## 8|36668374|2016-04-16|18:57:19<br>20|196469|
|## 9|37280274|2016-05-17|15:21:49<br>23|106995|


12

|##|10|37806538 2016-06-14 08:16:21|223<br>174790||
|---|---|---|---|---|
|##|11|37937984 2016-06-21 07:23:00|202<br>109422||
|##|||||
|##|1|||Fatal error|
|##|2||||
|##|3||||
|##|4||||
|##|5|||Response to p|
|##|6|||Android- Error:Execut|
|##|7||||
|##|8|||How to solve|
|##|9|||"SyntaxE|
|##|10|Code signing is required for pr|oduct type 'Appli|cation' in SDK 'iOS 10|
|##|11||||
|##||ownerid|||
|##|1|3656666|||
|##|2|3319176|||
|##|3|2761509|||
|##|4|5881764|||
|##|5|2896963|||
|##|6|1118886|||
|##|7|1629278|||
|##|8|1707976|||
|##|9|4043633|||
|##|10|1554347|||
|##|11|2670370|||


Let’s lay out the various verbs in SQL. Here’s the form of a standard query (though the ORDER BY is often omitted and sorting is computationally expensive):

SELECT <column(s)> FROM <table> WHERE <condition(s) on column(s)> ORDER BY <column(s)>

SQL keywords are often written in ALL CAPITALS though I won’t necessarily do that here. And here is a table of some important keywords:

13

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

### **2.7 Simple SQL joins**

It turns out that the syntax of using multiple tables we’ve seen can be viewed formally as a table join and could also be implemented using the JOIN keyword.

The syntax generally looks like this (again the WHERE and ORDER BY are optional):

SELECT <column(s)> FROM <table1> JOIN <table2> ON <columns to match on> WHERE <condition(s) on column(s)> ORDER BY <column(s)>

Let’s see some joins using the different syntax on the Stack Overflow database. In particular let’s select only the questions with the tag "python".

Here’s a join using similar syntax to what we saw above, without using the JOIN keyword.

result1 <- **dbGetQuery** (db, "select * from questions, questions_tags where questions.questionid = questions_tags.questionid and tag = 'python'")

And here’s how we do it with an explicit JOIN:

result2 <- **dbGetQuery** (db, "select * from questions join questions_tags on questions.questionid = questions_tags.questionid where tag = 'python'")

**head** (result1)

---

[← Unit 08 — bigData Part 04 —](04-unit-08-bigdata-part-04.md) · [Up: contents](index.md) · [questionid creationdate score viewcount →](06-questionid-creationdate-score-viewcount.md)
