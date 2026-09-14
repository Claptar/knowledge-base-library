---
title: '[1] TRUE'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] TRUE

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s a three-way join (using both types of syntax) with some additional use of aliases to abbreviate table names. What does this query ask for?

result1 <- **dbGetQuery** (db, "select * from questions Q, questions_tags T, users U where Q.questionid = T.questionid and Q.ownerid = U.userid and tag = 'python' and age < 18") result2 <- **dbGetQuery** (db, "select * from questions Q

15

join questions_tags T on Q.questionid = T.questionid join users U on Q.ownerid = U.userid where tag = 'python' and age < 18") **identical** (result1, result2) ## [1] TRUE

**Challenge** : Write a query that would return all the answers to questions with the Python tag. **Challenge** : Write a query that would return the users who have answered a question with the Python tag.

### **2.8 Grouping / stratifying**

A common pattern of operation is to stratify the dataset, i.e., collect it into mutually exclusive and exhaustive subsets. One would then generally do some operation on each subset. In SQL this is done with the GROUP BY keyword.

Here’s a basic example where we count the occurrences of different tags.

**dbGetQuery** (db, "select tag, count(*) as n from questions_tags group by tag order by n desc limit 25")

---

[← Unit 08 — bigData Part 07 —](07-unit-08-bigdata-part-07.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 09 — →](09-unit-08-bigdata-part-09.md)
