---
title: 3. Databases
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit7-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Databases

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

This material is drawn from the tutorial on [Working with large datasets
in SQL, R, and
Python](https://computing.stat.berkeley.edu/tutorial-databases), though I
won't hold you responsible for all of the database/SQL material in that
tutorial, only what appears here in this Unit.

## Overview

Standard SQL databases are *relational* databases that are a
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

### Memory and disk use

Formally, databases are stored on disk, while Python and R store
datasets in memory. This would suggest that databases will be slow to
access their data but will be able to store more data than can be loaded
into an Python or R session. However, databases can be quite fast due in
part to [disk caching by the operating system](../unit5-programming/index.md) as well as careful
implementation of good algorithms for database operations.

## Interacting with a database

You can interact with databases in a variety of database systems
(*DBMS*=database management system). Some popular systems are SQLite,
DuckDB, MySQL, PostgreSQL, Oracle and Microsoft Access. We'll concentrate on
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

We'll concentrate on DuckDB and SQLite (because they are simple to use on a single
machine). They are quite nice in terms of being self-contained - there
is no server-client model, just a single file on your hard drive that
stores the database and to which you can connect to using the SQLite
shell, R, Python, etc.

However, they may not have all the  useful
functionality that other DBMS have. For example, with SQLite you can't use `ALTER
TABLE` to modify column types or drop columns.

A good alternative to SQLite that I encourage you to consider is DuckDB. DuckDB stores data column-wise, which can lead to big speedups when doing queries operating on large portions of tables (so-called “online analytical processing” (OLAP)). Another nice feature of DuckDB is that it can interact
with data on disk without always having to read all the data into memory.

In the demo code, we'll have the option to use either SQLite or DuckDB.

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

There are a lot of problems with this (to be filled out in class):

  1. ???
  2. ???
  3. ???

```python
#| echo: false

---

[← For some reason the fromarray and da.mean calculations are not done lazily here.](06-for-some-reason-the-fromarray-and-da-mean-calculations-are-n.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 08 — →](08-unit-07-bigdata-part-08.md)
