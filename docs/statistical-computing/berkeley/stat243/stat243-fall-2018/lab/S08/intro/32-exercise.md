---
title: Exercise
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exercise

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Consider the Wikipedia traffic data in */global/scratch/paciorek/wikistats_small/dated/* on Savio.

Using either foreach or parSapply (or parLapply), write code that, in parallel, reads in the space-delimited file and filters to only the rows that refer to pages where "Barack_Obama" appears. Collect all the results across the 192 files into a single data frame. Run your code using an interactive session on either the Savio2 or Savio partition.

You should be able to use *looFit.R* as a template for your answer here. In addition, Section 4.3 of Unit 8 has example R code for doing either a parallel for loop or a paralllel lapply/sapply.

Note that as we saw in class, the data are the number of hits on different Wikipedia pages for November 4, 2008. The columns are: date, time, language, webpage, number of hits, and page size.

---

[← Monitoring jobs and the job queue](31-monitoring-jobs-and-the-job-queue.md) · [Up: contents](index.md)
