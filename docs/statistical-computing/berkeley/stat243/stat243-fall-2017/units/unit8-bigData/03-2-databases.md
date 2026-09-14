---
title: 2 Databases
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Databases

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This material is drawn from the tutorial on “Working with large datasets in SQL, R, and Python”, though I won’t hold you responsible for all of the database/SQL material in that tutorial, only what appears here in this Unit.

### **2.1 Overview**

Basically, standard SQL databases are _relational_ databases that are a collection of rectangular format datasets ( _tables_ , also called _relations_ ), with each table similar to R or Pandas data frames, in that a table is made up of columns, which are called _fields_ or _attributes_ , each containing a single _type_ (numeric, character, date, currency, enumerated (i.e., categorical), ...) and rows or records containing the observations for one entity. Some of the tables in a given database will generally have fields in common so it makes sense to merge (i.e., join) information from multiple tables. E.g., you might have a database with a table of student information, a table of teacher information and a table of school information, and you might join student information with information about the teacher(s) who taught the students. Databases are set up to allow for fast querying and merging (called joins in database terminology).

Formally, databases are stored on disk, while R and Python store datasets in memory. This would suggest that databases will be slow to access their data but will be able to store more data than can be loaded into an R or Python session. However, databases can be quite fast due in part to disk caching by the operating system as well as careful implementation of good algorithms for database operations. For more information about disk caching see the tutorial.

### **2.2 Interacting with a database**

You can interact with databases in a variety of database systems ( _DBMS_ =database management system). Some popular systems are SQLite, MySQL, PostgreSQL, Oracle and Microsoft Access. We’ll concentrate on accessing data in a database rather than management of databases. SQL is the Structured Query Language and is a special-purpose high-level language for managing databases and making queries. Variations on SQL are used in many different DBMS.

3

Queries are the way that the user gets information (often simply subsets of tables or information merged across tables). The result of an SQL query is in general another table, though in some cases it might have only one row and/or one column.

Many DBMS have a client-server model. Clients connect to the server, with some authentication, and make requests (i.e., queries).

There are often multiple ways to interact with a DBMS, including directly using command line tools provided by the DBMS or via Python or R, among others.

We’ll concentrate on SQLite (because it is simple to use on a single machine). SQLite is quite nice in terms of being self-contained - there is no server-client model, just a single file on your hard drive that stores the database and to which you can connect to using the SQLite shell, R, Python, etc. However, it does not have some useful functionality that other DBMS have. For example, you can’t use ALTER TABLE to modify column types or drop columns.

### **2.3 Database schema and normalization**

To truly leverage the conceptual and computational power of a database you’ll want to have your data in a normalized form, which means spreading your data across multiple tables in such a way that you don’t repeat information unnecessarily.

The schema is the metadata about the tables in the database and the fields (and their types) in those tables.

Let’s consider this using an educational example. Suppose we have a school with multiple teachers teaching multiple classes and multiple students taking multiple classes. If we put this all in one table organized per student, the data might have the following fields:

- student ID

- student grade level

- student name

- class 1

- class 2

- ...

- class n

- grade in class 1

- grade in class 2

4

- ...

- grade in class n

- teacher ID 1

- teacher ID 2

-

- teacher ID n

- teacher department 1

- teacher department 2

- ...

- teacher department n

- teacher age 1

- teacher age 2

- ...

- teacher age n

There are a lot of problems with this.

1. ’n’ needs to be the maximum number of classes a student might take. If one ambitious student takes many classes, there will be a lot of empty data slots.

2. All the information about individual teachers (department, age, etc.) is repeated many times, meaning we use more storage than we need to.

3. If we want to look at the data on a per teacher basis, this is very poorly organized for that.

4. If one wants to change certain information (such as the age of a teacher) one needs to do it in many locations, which can result in errors and is inefficient.

It would get even worse if there was a field related to teachers for which a given teacher could have multiple values (e.g., teachers could be in multiple departments). This would lead to even more redundancy - each student-class-teacher combination would be crossed with all of the departments for the teacher (so-called multivalued dependency in database theory).

An alternative organization of the data would be to have each row represent the enrollment of a student in a class.

5

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

6

- ClassAssignment

   - student_ID

   - class_ID

   - grade

Then we do queries to pull information from multiple tables. We do the joins based on _keys_ , which are the fields in each table that allow us to match rows from different tables.

(That said, if all anticipated uses of a database will end up recombining the same set of tables, we may want to have a denormalized schema in which those tables are actually combined in the database. It is possible to be too pure about normalization! We can also create a virtual table, called a _view_ , as discussed later.)

#### **2.3.1 Keys**

A _key_ is a field or collection of fields that give(s) a unique value for every row/observation. A table in a database should then have a _primary key_ that is the main unique identifier used by the DBMS. _Foreign keys_ are columns in one table that give the value of the primary key in another table. When information from multiple tables is joined together, the matching of a row from one table to a row in another table is generally done by equating the primary key in one table with a foreign key in a different table.

In our educational example, the primary keys would presumably be: _Student.ID_ , _Teacher.ID_ , _Class.ID_ , and for ClassAssignment two fields: _{ClassAssignment.studentID, ClassAssignment.class_ID}_ . Some examples of foreign keys would be:

- student_ID as the foreign key in ClassAssignment for joining with Student on Student.ID

- teacher_ID as the foreign key in Class for joining with Teacher based on Teacher.ID

- class_ID as the foreign key in ClassAssignment for joining with Class based on Class.ID

#### **2.3.2 Queries that join data across multiple tables**

Suppose we want a result that has the grades of all students in 9th grade. For this we need information from the Student table (to determine grade level) and information from the ClassAssignment table (to determine the class grade). More specifically we need a query that joins _Student_ with _ClassAssignment_ based on _Student.ID_ and _ClassAssignment.student_ID_ and filters the rows based on _Student.grade_level_ :

SELECT Student.ID, grade FROM Student, ClassAssignment WHERE

7

Student.ID = ClassAssignment.student_ID and Student.grade_level = 9;

Note that the query is a _join_ (specifically an _inner join_ ), which is like _merge()_ in R. We don’t specifically use the JOIN keyword, but one could do these queries explicitly using JOIN, as we’ll see later.

### **2.4 Stack Overflow metadata example**

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

8

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

9

### **2.5 Accessing databases in R**

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


10

<mark>## 5 4646288</mark>

We can easily see the tables and their fields:

**dbListTables** (db)

---

[← 1 A few preparatory notes](02-1-a-few-preparatory-notes.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 04 — →](04-unit-08-bigdata-part-04.md)
