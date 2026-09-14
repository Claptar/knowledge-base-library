---
title: Big data and databases
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Big data and databases

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Split into 23 sections.

1. [Introduction](01-introduction.md)
2. [1. A few preparatory notes](02-1-a-few-preparatory-notes.md)
3. [2. MapReduce, Dask, Hadoop, and Spark](03-2-mapreduce-dask-hadoop-and-spark.md)
4. [specify dtypes so Pandas doesn't complain about column type heterogeneity](04-specify-dtypes-so-pandas-doesn-t-complain-about-column-type.md)
5. [square 10k x 10k chunks](05-square-10k-x-10k-chunks.md)
6. [x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing array](06-x-da-fromarray-x-chunks-2500-40000-adjust-chunk-size-of-exis.md)
7. [for some reason the fromarray and da.mean calculations are not done lazily here](07-for-some-reason-the-fromarray-and-da-mean-calculations-are-n.md)
8. [check files on the HDFS, e.g.](08-check-files-on-the-hdfs-e-g.md)
9. [after processing can retrieve data from HDFS as needed](09-after-processing-can-retrieve-data-from-hdfs-as-needed.md)
10. [note delayed evaluation](10-note-delayed-evaluation.md)
11. [watch the UI and watch wwall as computation progresses](11-watch-the-ui-and-watch-wwall-as-computation-progresses.md)
12. [not clear if should repartition; will likely have small partitions if not](12-not-clear-if-should-repartition-will-likely-have-small-parti.md)
13. [Unit 07 — bigData Part 13 —](13-unit-07-bigdata-part-13.md)
14. [sum number of hits for each date-time-language value](14-sum-number-of-hits-for-each-date-time-language-value.md)
15. [128889 for full dataset](15-128889-for-full-dataset.md)
16. [have one partition because one file per partition is written out](16-have-one-partition-because-one-file-per-partition-is-written.md)
17. [Unit 07 — bigData Part 17 —](17-unit-07-bigdata-part-17.md)
18. [Unit 07 — bigData Part 18 —](18-unit-07-bigdata-part-18.md)
19. [sc <- sparkconnect(master = "local") # if doing on laptop](19-sc---sparkconnect-master-local-if-doing-on-laptop.md)
20. [3. Databases](20-3-databases.md)
21. [simple query to get 5 rows from a table](21-simple-query-to-get-5-rows-from-a-table.md)
22. [4. Sparsity](22-4-sparsity.md)
23. [5. Using statistical concepts to deal with computational bottlenecks](23-5-using-statistical-concepts-to-deal-with-computational-bott.md)

---

[Up: contents](../../index.md)
