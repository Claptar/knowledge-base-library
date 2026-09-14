---
title: Exercise
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exercise

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Consider the Wikipedia traffic data in `/scratch/users/paciorek/wikistats/dated_2017_small/dated`
on the SCF cluster.

1) In an interactive shell:
    - Copy the first 30 files to your `/tmp` directory. (recall the use of wildcards
    in file globbing to select a set of files, from the unit/tutorial on bash)
    - Run R code to do the following: Using the future package, with either future_lapply
or foreach with the doFuture backend, write code that, in parallel, reads in the
space-delimited file and filters to only the rows that refer to pages where "Barack_Obama"
appears. You can use the code from unit7-parallel.R as a template, in particular
the chunks labeled 'rf-example', 'foreach' and 'future_lapply'. Collect all the results
into a single data frame. Run your code using an interactive session.

3) Now replicate what you did above but using sbatch to submit your job as a batch
job, where step 2 involves running R from the command line using R CMD BATCH.

Note that as we will see in class, the data are the number of hits on different Wikipedia
pages for November 4, 2008. The columns are: date, time, language, webpage, number of hits, and page size. `Barack_Obama` will be found in the 4th column.

---

[← Monitoring jobs and the job queue](15-monitoring-jobs-and-the-job-queue.md) · [Up: contents](index.md)
