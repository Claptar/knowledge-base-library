---
title: Unit 07 — bigData Part 13 —
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit7-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 07 — bigData Part 13 —

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```

It would get even worse if there was a field related to teachers for
which a given teacher could have multiple values (e.g., teachers could
be in multiple departments). This would lead to even more redundancy -
each student-class-teacher combination would be crossed with all of the
departments for the teacher (so-called multivalued dependency in
database theory).

An alternative organization of the data would be to have each row
represent the enrollment of a student in a class.

-   student ID
-   student name
-   class
-   grade in class
-   student grade level
-   teacher ID
-   teacher department
-   teacher age

This has some advantages relative to our original organization in terms
of not having empty cells, but it doesn't solve the other three
issues above.

Instead, a natural way to order this database is with the following
four tables.

-   Student
    -   ID
    -   name
    -   grade_level

-   Teacher
    -   ID
    -   name
    -   department
    -   age

-   Class
    -   ID
    -   topic
    -   class_size
    -   teacher_ID

-   Enrollment
    -   student_ID
    -   class_ID
    -   grade

The `Enrollment` table has one row per student-class pair. Having a table like
this handles "ragged" data where the number of observations per unit (in this case
classes per student) varies. Using such tables is a common pattern when considering how to normalize a database.
It's also a core part of the idea of "tidy data" and data in *long* format, seen in the `tidyr` package.

Then we do queries to pull information from multiple tables. We do the
joins based on *keys*, which are the fields in each table that allow us
to match rows from different tables.

(That said, if all anticipated uses of a database will end up
recombining the same set of tables, we may want to have a denormalized
schema in which those tables are actually combined in the database. It
is possible to be too pure about normalization! We can also create a
virtual table, called a *view*, as discussed later.)

### Keys

A *key* is a field or collection of fields that give(s) a unique value
for every row/observation. A table in a database should then have a
*primary key* that is the main unique identifier used by the DBMS.
*Foreign keys* are columns in one table that give the value of the
primary key in another table. When information from multiple tables is
joined together, the matching of a row from one table to a row in
another table is generally done by equating the primary key in one table
with a foreign key in a different table.

In our educational example, the primary keys would presumably be:
`Student.ID`, `Teacher.ID`, `Class.ID`, and for Enrollment a primary key
made of two
fields: `{Enrollment.studentID, Enrollment.class_ID}`.

Some examples of foreign keys would be:

-   `student_ID` as the foreign key in `Enrollment` for joining with
    `Student` on `Student.ID`

-   `teacher_ID` as the foreign key in `Class` for joining with `Teacher`
    based on `Teacher.ID`

-   `class_ID` as the foreign key in `Enrollment` for joining with
    `Class` based on `Class.ID`

### Queries that join data across multiple tables

Suppose we want a result that has the grades of all students in 9th
grade. For this we need information from the `Student` table (to determine
grade level) and information from the `Enrollment` table (to
determine the class grade). More specifically we need a query that:

 - joins `Student` with `Enrollment` based on matching rows in `Student` with
 rows in `Enrollment` where `Student.ID` is the same as `Enrollment.student_ID` and
 - filters the rows based on `Student.grade_level`:

```sql
#| eval: false
SELECT Student.ID, grade FROM Student, Enrollment WHERE
  Student.ID = Enrollment.student_ID and Student.grade_level = 9;
```

Note that the query is a *join* (specifically an *inner join*), which is
like `merge()` (or `dplyr::join`) in R. We don't specifically use the JOIN keyword, but one
could do these queries explicitly using JOIN, as we'll see later.

## Stack Overflow metadata example

I've obtained data from [Stack Overflow](https://stackoverflow.com), the
popular website for asking coding questions, and placed it into a
normalized database. The SQLite/DuckDB version has metadata (i.e., it lacks the
actual text of the questions and answers) on all of the questions and
answers posted in 2021.

We'll explore SQL functionality using this example database.

Now let's consider the Stack Overflow data. Each question may have
multiple answers and each question may have multiple (topic) tags.

If we tried to put this into a single table, the fields could look like
this if we have one row per question:

-   question ID
-   ID of user submitting question
-   question title
-   tag 1
-   tag 2
-    ...
-   tag n
-   answer 1 ID
-   ID of user submitting answer 1
-   age of user submitting answer 1
-   name of user submitting answer 1
-   answer 2 ID
-   ID of user submitting answer 2
-   age of user submitting answer 2
-   name of user submitting answer 2
-   ...

or like this if we have one row per question-answer pair:

-   question ID
-   ID of user submitting question
-   question title
-   tag 1
-   tag 2
-    ...
-   tag n
-   answer ID
-   ID of user submitting answer
-   age of user submitting answer
-   name of user submitting answer

As we've discussed neither of those schema is particularly desirable.

!!! tip "Tip"
How would you devise a schema to normalize the data.
I.e., what set of tables do you think we should create?
:::

You can view [one reasonable schema](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/normalized_example.png).
The lines between tables indicate the relationship of foreign keys in
one table to primary keys in another table. The schema in the actual
database of Stack Overflow data we'll use in the examples here is similar
to but not identical to that. In particular, our version of the database has these tables and fields:

 - questions: questionid, creationdate, score, viewcount, answercount, commentcount, favoritecount, title, ownerid
 - answers: answerid, questionid, creationdate, score, ownerid
 - users: userid, creationdate, lastaccessdate, location, reputation, displayname, upvotes, downvotes, age, accountid
 - questions_tags: questionid, tag

You can download a [copy of the SQLite version of the Stack Overflow 2021
database](http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2021.db)
or a [copy of the DuckDB version of the Stack Overflow 2021
database](http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2021.duckdb).

## Accessing databases in Python

Python provides a variety of front-end packages for manipulating databases from a
variety of DBMS (SQLite, DuckDB, MySQL, PostgreSQL, among others). Basically,
you start with a bit of code that links to
the actual database, and then you can easily query the database using SQL
syntax regardless of the back-end. The Python function calls that wrap
around the SQL syntax will also look the same regardless of the back-end
(basically `execute("SOME SQL STATEMENT")`).

With SQLite, Python processes make calls against the stand-alone SQLite
database (.db) file, so there are no SQLite-specific processes. With a
client-server DBMS like PostgreSQL, Python processes call out to separate
Postgres processes; these are started from the overall Postgres
background process

You can access and navigate an SQLite database from Python as follows.

```python
import sqlite3 as sq
dir_path = '/mirror/data/pub/users/paciorek/share'  # Replace with the actual path
db_filename = 'stackoverflow-2021.db'
## Download from http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2021.db.

con = sq.connect(os.path.join(dir_path, db_filename))
db = con.cursor()
db.execute("select * from questions limit 3")  # simple query
db.fetchall() # retrieve results
```

Alternatively, we could use DuckDB, but I haven't run this code
while rendering this document.

```python
#| eval: false
import duckdb as dd
dir_path = '../data'  # Replace with the actual path
db_filename = 'stackoverflow-2021.duckdb'
## Download from http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2021.duckdb.

con = dd.connect(os.path.join(dir_path, db_filename))
db = con.cursor()
db.execute("select * from questions limit 5")  # simple query
db.fetchall() # retrieve results
```


We can (fairly) easily see the tables in SQLite (this is easier from R):

```python
def db_list_tables(db):
    db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = db.fetchall()
    return [table[0] for table in tables]

db_list_tables(db)
```

Or it's easy in DuckDB (code not executed while rendering).

```python
#| eval: false
con.execute("show tables").fetchall()
```

To see the fields in the table, if you've just queried the table, you can look at `description`:

```python
db.execute("select * from questions")

[item[0] for item in db.description]

def get_fields():
    return [item[0] for item in db.description]
```

Here's how to make a basic SQL query. One can either make the query and
get the results in one go or make the query and separately fetch the
results. Here we've selected the first five rows (and all columns, based
on the \* wildcard) and brought them into Python as list of tuples.

```python
#| cache: true
results = db.execute("select * from questions limit 5").fetchall()  # simple query
type(results)
type(results[0])

query = db.execute("select * from questions")  # simple query
results2 = query.fetchmany(5)
results == results2
```


To disconnect from the database:

```python
#| eval: false
db.close()
```

It's convenient to get a Pandas dataframe back as the result. To do that we can
execute queries like this:

```python
import pandas as pd
results = pd.read_sql("select * from questions limit 5", con)
```

If I do that with DuckDB rather than SQLite, I get a warning, but it seems to work.

## Basic SQL for choosing rows and fields from a table

SQL is a declarative language that tells the database system what
results you want. The system then parses the SQL syntax and determines
how to implement the query.

!!! note "Note"
An *imperative* language is one where you provide the sequence of commands you want to be run, in order. A *declarative* language is one where you declare what result you want and rely on the system that interprets the commands to determine how to actually do it. Most of the languages we're generally familiar with are imperative. (That said, even in languages like Python, function calls in many ways simply say what we want rather than exactly how the computer should carry out the granular operations.)
:::

Here are some examples using the Stack Overflow database of getting questions that
have been viewed a lot (the `viewcount` field is large).

```python
#| cache: true
## Get the questions for which the viewcount field is large.
results = db.execute('select title, viewcount from questions where viewcount > 100000').fetchall()
results[0:3]

## Find the 10 largest viewcounts (and associated titles) in the questions table,
## by sorting in descending order based on viewcount and returning the first 10.
db.execute(
'select title, viewcount from questions order by viewcount desc limit 10').fetchall()
```


Let's lay out the various verbs in SQL. Here's the form of a standard
query (though the ORDER BY is often omitted and sorting is
computationally expensive):

```
SELECT <column(s)> FROM <table> WHERE <condition(s) on column(s)> ORDER BY <column(s)>
```

SQL keywords are often written in ALL CAPITALS, although I won't
necessarily do that in this document.

And here is a table of some important keywords:

|            Keyword          |                         Usage  |
|  ----------------------------| ----------------------------------------------------|
|             SELECT           |                    select columns   |
|              FROM            |              which table to operate on   |
|             WHERE            |  filter (choose) rows satisfying certain conditions   |
|   LIKE, IN, \<, \>, ==, etc. |              used as part of conditions   |
|            ORDER BY          |                sort based on columns   |


For logical comparisons in a `WHERE` clause, some common syntax for setting
conditions includes `LIKE` (for patterns), `=`, `>`, `<`, `>=`, `<=`, `!=`.

Some other keywords are: `DISTINCT`, `ON`, `JOIN`, `GROUP BY`, `AS`, `USING`, `UNION`,
`INTERSECT`, `SIMILAR TO`.

!!! tip "Tip"
What are a couple ways we could find the oldest users in the database? How do the different ways scale
as a function of the number of records in the table?
:::

## The result of a query

The result of an SQL query (e.g., from `.execute` in Python) is an SQL table. It might only have one field or one row.

For example, `select count(*) from questions` will produce a table with one row and one field.

When we return the result to Python (e.g., via `fetch` or `fetchall`), we create a Python object, which in the most basic case is a list of tuples (but with `pandas.read_sql` is a DataFrame).

## Grouping / stratifying

A common pattern of operation is to stratify the dataset, i.e., collect
it into mutually exclusive and exhaustive subsets. One would then
generally do some (reduction) operation on each subset (e.g., counting records, calculating the mean of a column, taking the max of a column). In SQL this is done with the
GROUP BY keyword.

The basic syntax looks like this:

```
SELECT <reduction_operation>(<column(s)>) FROM <table> GROUP BY <column(s)>
```


Here's a basic example where we count the occurrences of different tags.
Note that we use `as` to define a name for the new column that is
created based on the aggregation operation (`count` in this case).

```python
#| cache: true
db.execute("select tag, count(*) as n from questions_tags \
           group by tag \
           order by n desc limit 25").fetchall()
```


In general `GROUP BY` statements will involve some aggregation operation
on the subsets. Options include: `COUNT`, `MIN`, `MAX`, `AVG`, `SUM`.
The number of results will be the same as the number of groups; in the example
above there should be one result per tag.

!!! tip "Tip"
If you filter after using `GROUP BY`, you need to use `having` instead of `where`.
:::

!!! tip "Tip"
Write a query that will count the number of answers for
each question, returning the most answered questions. Why can we do this with only a single table?
:::

## Getting unique results (DISTINCT)

A useful SQL keyword is `DISTINCT`, which allows you to eliminate
duplicate rows from any table (or remove duplicate values when one only
has a single column or set of values).

```python
#| cache: true
## Get the unique tags from the questions_tags table.
tag_names = db.execute("select distinct tag from questions_tags").fetchall()
tag_names[0:5]
## Count the number of unique tags.
db.execute("select count(distinct tag) from questions_tags").fetchall()
```


## Simple SQL joins

Often to get the information we need, we'll need data from multiple
tables. To do this we'll need to do a database join, telling the
database what columns should be used to match the rows in the different
tables.

The syntax generally looks like this (again the `WHERE` and `ORDER BY` are
optional):

```
SELECT <column(s)> FROM <table1> JOIN <table2> ON <columns to match on>
WHERE <condition(s) on column(s)> ORDER BY <column(s)>
```

Let's see some joins using the different syntax on the Stack Overflow
database. In particular let's select only the questions with the tag
'python'. By selecting `*` we are selecting all columns from
both the questions and questions_tags tables.

```python
#| cache: true
result1 = db.execute("select * from questions join questions_tags \
        on questions.questionid = questions_tags.questionid \
        where tag = 'python'").fetchall()
get_fields()
```


It turns out you can do it without using the JOIN keyword.

```python
#| cache: true
result2 = db.execute("select * from questions, questions_tags \
        where questions.questionid = questions_tags.questionid and \
        tag = 'python'").fetchall()

result1[0]
result1[1]
result1 == result2
```


Here's a three-way join (using both types of syntax) with some
additional use of aliases to abbreviate table names. What does this
query ask for?

```python
#| cache: true
result1 = db.execute("select * from \
        questions Q \
        join questions_tags T on Q.questionid = T.questionid \
        join users U on Q.ownerid = U.userid \
        where tag = 'python' and \
        viewcount > 1000").fetchall()

result2 = db.execute("select * from \
        questions Q, questions_tags T, users U where \
        Q.questionid = T.questionid and \
        Q.ownerid = U.userid and \
        tag = 'python' and \
        viewcount > 1000").fetchall()

result1 == result2
```

!!! tip "Tip"
Write a query that would return all the answers to
questions with the Python tag.
:::
!!! tip "Tip"
Write a query that would return the users who have
answered a question with the Python tag.
:::

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

```python
#| cache: true
db.execute("create view questionsAugment as select \
                questionid, questions.creationdate, score, viewcount, \
                title, ownerid, age, displayname \
                from questions join users \
                on questions.ownerid = users.userid")
## you'll see the return value is '0'

db.execute("select * from questionsAugment where viewcount > 1000 limit 3").fetchall()
```


One use of a view would be to create a mega table that stores all the
information from multiple tables in the (unnormalized) form you might
have if you simply had one data frame in Python or R.

```python
#| include: false
db.execute("drop view if exists questionsAugment") # Drop view, so can create again in next step.
```

## More on joins

We've seen a bunch of joins but haven't discussed the full taxonomy of
types of joins. There are various possibilities for how to do a join
depending on whether there are rows in one table that do not match any
rows in the other table.

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
tables, namely the pairwise combination of every row from each table.
I.e., take a row from the first table
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

```sql
## explicit inner join:
select * from table1 join table2 on table1.id = table2.id
## non-explicit join without JOIN
select * from table1, table2 where table1.id = table2.id
## cross-join followed by matching
select * from table1 cross join table2 where table1.id = table2.id
## explicit inner join with 'using'
select * from table1 join table2 using(id)
```

!!! tip "Tip"
Create a view with one row for every question-tag pair,
including questions without any tags.
:::

!!! tip "Tip"
Write a query that would return the displaynames of all
of the users who have *never* posted a question. The NULL keyword will
come in handy it's like 'NA' in R. Hint: NULLs should be produced if you
do an outer join.
:::

## Indexes

An index is an ordering of rows based on one or more fields. DBMS use
indexes to look up values quickly, either when filtering (if the index
is involved in the `WHERE` condition) or when doing joins (if the index is
involved in the `JOIN` condition). So in general you want your tables to
have indexes.

DBMS use indexing to provide sub-linear time lookup. Without indexes, a
database needs to scan through every row sequentially, which is called
linear time lookup. If there are 'n' rows, the lookup is $O(n)$ in
computational cost. With indexes, lookup may be logarithmic $O(log(n))$
(if using tree-based indexes) or constant time $O(1)$ (if using hash-based
indexes). A binary tree-based search is logarithmic; at each step
through the tree you can eliminate half of the possibilities.

While that seems to suggest hash-based indexes are better, that is
only the case when looking for exact matches (such as particular specific
tags), as the hash index would be based on hashing the value of the field
or fields used for the index. If one wanted to look for a range of values
(such as a range of viewcount values), then a tree-based index would be
more natural.

Here's how we create an index, with some time comparison for a simple
query.

```python
#| eval: false
t0 = time.time()
results = db.execute(
  "select * from questions where viewcount > 10000").fetchall()
print(time.time() - t0)  # 10 seconds
t0 = time.time()
db.execute(
  "create index count_index on questions (viewcount)")
print(time.time() - t0)  # 19 seconds
t0 = time.time()
db.execute(
  "select * from questions where viewcount > 10000").fetchall()
print(time.time() - t0)  # 3 seconds

```

In other contexts, an index can save huge amounts of time. So if you're
working with a database and speed is important, check to see if there
are indexes. That said, as seen above it takes time to create the index,
so you'd only want to create it if you were doing multiple queries
that could take advantage of the index. See the databases tutorial
for more discussion of how using indexes in a lookup is not always advantageous.

## Set operations: union, intersect, except

You can do set operations like union, intersection, and set difference using the UNION, INTERSECT, and EXCEPT keywords, respectively, on tables that have the same schema (same column names and types), though most often these would be used on single columns (i.e., single-column tables).

While one can often set up an equivalent query without using INTERSECT or UNION, set operations can be very handy. In the example below one could do it with a join, but the syntax is often more complicated.

Consider the following example of using `INTERSECT`. What does it return?


```python
#| eval: false
result1 = db.execute("select displayname, userid from \
                     questions Q join users U on U.userid = Q.ownerid \
                     intersect \
                     select displayname, userid from \
                     answers A join users U on U.userid = A.ownerid")

```

!!! tip "Tip"
What if you wanted to find users who had neither asked nor answered a question?
:::

## Subqueries

A subquery is a full query that is embedded in a larger query.
These can be quite handy in building up complicated queries. One could instead use temporary tables (views), but it often
is easier to write all in one query (and that lets the database's query optimizer operate on the entire query).

### Subqueries in the FROM statement

We can use subqueries in the FROM statement to create a temporary table to use in a query. Here we'll do it in the context of a join.

!!! tip "Tip"
What does the following do?
:::

```python
#| eval: false
db.execute("select * from questions join answers A \
           on questions.questionid = A.questionid \
           join \
           (select ownerid, count(*) as n_answered from answers \
           group by ownerid order by n_answered desc limit 1000) most_responsive \
           on A.ownerid = most_responsive.ownerid")
```

It might be hard to just come up with that full query all at once. A good strategy is probably to think about creating a view that is the result of the inner query and then have the outer query use that. You can then piece together the complicated query in a modular way. For big databases, you are likely to want to submit this as a single query and not two queries so that the SQL optimizer can determine the best way to do the operations. But you want to start with code that you're confident will give you the right answer!

Note we could also have done that query using a subquery in the WHERE statement, as discussed in the next section.

### Subqueries in the WHERE statement

Instead of a join, we can use subqueries as a way to combine information across tables, with the subquery involved in a WHERE statement. The subquery creates a set and we then can check for inclusion in (or exclusion from with `not in`) that set.

For example, suppose we want to know the average number of UpVotes for users who have posted a question with the tag "python".

```python
db.execute("select avg(upvotes) from users where userid in \
           (select distinct ownerid from \
           questions join questions_tags \
           on questions.questionid = questions_tags.questionid \
           where tag = 'python')").fetchall()
```


## Creating database tables

One can create tables from within the 'sqlite' command line interfaces
(discussed in the tutorial), but often one would do this from
Python or R. Here's the syntax from Python, creating the table
from a Pandas dataframe.

```python
#| eval: false
## Create data frame 'student_data' in some fashion.
con = sq.connect(db_path)
student_data.to_sql('student', con, if_exists='replace', index=False)
```

---

[← Unit 07 — bigData Part 12 —](12-unit-07-bigdata-part-12.md) · [Up: contents](index.md) · [4. Recent tools and data storage formats →](14-4-recent-tools-and-data-storage-formats.md)
