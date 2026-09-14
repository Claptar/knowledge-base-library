---
title: 'count(distinct tag) ## 1 41006'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# count(distinct tag) ## 1 41006

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

---

[← tag ## 1 c# ## 2 razor ## 3 flags ## 4 javascript ## 5 rxjs ## 6 node.js](10-tag-1-c-2-razor-3-flags-4-javascript-5-rxjs-6-node-js.md) · [Up: contents](index.md) · [data frame with 0 columns and 0 rows →](12-data-frame-with-0-columns-and-0-rows.md)
