---
title: 3. Databases
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Databases

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

This material is drawn from the tutorial on [Working with large datasets
in SQL, R, and
Python](https://berkeley-scf.github.io/tutorial-databases), though I
won't hold you responsible for all of the database/SQL material in that
tutorial, only what appears here in this Unit.

## Overview

Basically, standard SQL databases are *relational* databases that are a
collection of rectangular format datasets (*tables*, also called
*relations*), with each table similar to R or Pandas data frames, in
that a table is made up of columns, which are called *fields* or
*attributes*, each containing a single *type* (numeric, character, date,
currency, enumerated (i.e., categorical), ...) and rows or records
containing the observations for one entity. Some of the tables in a
given database will generally have fields in common so it makes sense to
merge (i.e., join) information from multiple tables. E.g., you might
have a database with a table of student information, a table of teacher
information and a table of school information, and you might join
student information with information about the teacher(s) who taught the
students. Databases are set up to allow for fast querying and merging
(called joins in database terminology).

Formally, databases are stored on disk, while R and Python store
datasets in memory. This would suggest that databases will be slow to
access their data but will be able to store more data than can be loaded
into an R or Python session. However, databases can be quite fast due in
part to disk caching by the operating system as well as careful
implementation of good algorithms for database operations. For more
information about disk caching see the tutorial.

## Interacting with a database

You can interact with databases in a variety of database systems
(*DBMS*=database management system). Some popular systems are SQLite,
MySQL, PostgreSQL, Oracle and Microsoft Access. We'll concentrate on
accessing data in a database rather than management of databases. SQL is
the Structured Query Language and is a special-purpose high-level
language for managing databases and making queries. Variations on SQL
are used in many different DBMS.

Queries are the way that the user gets information (often simply subsets
of tables or information merged across tables). The result of an SQL
query is in general another table, though in some cases it might have
only one row and/or one column.

Many DBMS have a client-server model. Clients connect to the server,
with some authentication, and make requests (i.e., queries).

There are often multiple ways to interact with a DBMS, including
directly using command line tools provided by the DBMS or via Python or
R, among others.

We'll concentrate on SQLite (because it is simple to use on a single
machine). SQLite is quite nice in terms of being self-contained - there
is no server-client model, just a single file on your hard drive that
stores the database and to which you can connect to using the SQLite
shell, R, Python, etc. However, it does not have some useful
functionality that other DBMS have. For example, you can't use `ALTER
TABLE` to modify column types or drop columns.

## Database schema and normalization

To truly leverage the conceptual and computational power of a database
you'll want to have your data in a normalized form, which means
spreading your data across multiple tables in such a way that you don't
repeat information unnecessarily.

The *schema* is the metadata about the tables in the database and the
fields (and their types) in those tables.

Let's consider this using an educational example. Suppose we have a
school with multiple teachers teaching multiple classes and multiple
students taking multiple classes. If we put this all in one table
organized per student, the data might have the following fields:

-   student ID
-   student grade level
-   student name
-   class 1
-   class 2
-    ...
-   class n
-   grade in class 1
-   grade in class 2
-    ...
-   grade in class n
-   teacher ID 1
-   teacher ID 2
-    ...
-   teacher ID n
-   teacher name 1
-   teacher name 2
-    ...
-   teacher name n
-   teacher department 1
-   teacher department 2
-    ...
-   teacher department n
-   teacher age 1
-   teacher age 2
-    ...
-   teacher age n

There are a lot of problems with this:

1.  A lot of information is repeated across rows (e.g., teacher age for students who have the same teacher)
    - this is a waste of space
    - it is hard/error-prone to update values in the database (e.g., after a teacher's birthday), because a given value needs to be updated in multiple places
2.  There are potentially a lot of empty cells (e.g., for a student who takes fewer than 'n' classes). This will generally result in a waste of space.
3.  It's hard to see the information that is not organized uniquely by row -- i.e., it's much easier to understand the information at the student level than the teacher level
4.  We have to know in advance how big 'n' is. Then if a single student takes more than 'n' classes, the whole database needs to be restructured.

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

-   ClassAssignment
    -   student_ID
    -   class_ID
    -   grade

The `ClassAssignment` table has one row per student-class pair. Having a table like
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
`Student.ID`, `Teacher.ID`, `Class.ID`, and for ClassAssignment a primary key
made of two
fields: `{ClassAssignment.studentID, ClassAssignment.class_ID}`.

Some examples of foreign keys would be:

-   `student_ID` as the foreign key in `ClassAssignment` for joining with
    `Student` on `Student.ID`

-   `teacher_ID` as the foreign key in `Class` for joining with `Teacher`
    based on `Teacher.ID`

-   `class_ID` as the foreign key in `ClassAssignment` for joining with
    `Class` based on `Class.ID`

### Queries that join data across multiple tables

Suppose we want a result that has the grades of all students in 9th
grade. For this we need information from the `Student` table (to determine
grade level) and information from the `ClassAssignment` table (to
determine the class grade). More specifically we need a query that:

 - joins `Student` with `ClassAssignment` based on matching rows in `Student` with
 rows in `ClassAssignment` where `Student.ID` is the same as `ClassAssignment.student_ID` and
 - filters the rows based on `Student.grade_level`:

```sql
SELECT Student.ID, grade FROM Student, ClassAssignment WHERE
  Student.ID = ClassAssignment.student_ID and Student.grade_level = 9;
```

Note that the query is a *join* (specifically an *inner join*), which is
like `merge()` (or `dplyr::join`) in R. We don't specifically use the JOIN keyword, but one
could do these queries explicitly using JOIN, as we'll see later.

## Stack Overflow metadata example

I've obtained data from [Stack Overflow](https://stackoverflow.com), the
popular website for asking coding questions, and placed it into a
normalized database. The SQLite version has metadata (i.e., it lacks the
actual text of the questions and answers) on all of the questions and
answers posted in 2016.

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

**Challenge**: How would you devise a schema to normalize the data.
I.e., what set of tables do you think we should create?

You can view [one reasonable schema](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/normalized_example.png).
The lines between tables indicate the relationship of foreign keys in
one table to primary keys in another table. The schema in the actual
database of Stack Overflow data we'll use in the examples here is similar
to but not identical to that.

You can download a [copy of the SQLite version of the Stack Overflow 2016
database](http://www.stat.berkeley.edu/share/paciorek/stackoverflow-2016.db).

## Accessing databases in R

The `DBI` package provides a front-end for manipulating databases from a
variety of DBMS (SQLite, MySQL, PostgreSQL, among others). Basically,
you tell the package what DBMS is being used on the back-end, link to
the actual database, and then you can use the standard functions in the
package regardless of the back-end. This is a similar style to how one
uses `foreach` for parallelization.

With SQLite, R processes make calls against the stand-alone SQLite
database (.db) file, so there are no SQLite-specific processes. With a
client-server DBMS like PostgreSQL, R processes call out to separate
Postgres processes; these are started from the overall Postgres
background process

You can access and navigate an SQLite database from R as follows.

```r
library(RSQLite)
drv <- dbDriver("SQLite")
dir <- '../data' # relative or absolute path to where the .db file is
dbFilename <- 'stackoverflow-2016.db'
db <- dbConnect(drv, dbname = file.path(dir, dbFilename))

---

[← sc <- sparkconnect(master = "local") # if doing on laptop](19-sc---sparkconnect-master-local-if-doing-on-laptop.md) · [Up: contents](index.md) · [simple query to get 5 rows from a table →](21-simple-query-to-get-5-rows-from-a-table.md)
