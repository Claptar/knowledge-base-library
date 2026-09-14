---
title: Ps 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps5.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/ps5.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 05 —

**Source:** [`ps/ps5.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps5.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 5, Due Monday Oct. 26, 10 am

October 14, 2020

This covers Units 6-7.

It’s due **as PDF submitted to Gradescope** and submitted via GitHub at 10 am on Oct. 26. Comments:

1. The formatting requirements are the same as previous problem sets.

2. As discussed in the Piazza post, we are happy to help troubleshoot problems you may have with the SCF, parallelizing R, submitting jobs to the SCF cluster, etc. We are not so happy to do it the weekend of Oct. 24 if it is clear that you didn’t put in time in section and during the week of Oct. 19 to get up to speed.

3. Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

## **Problems**

1. Consider the following estimates of the variance of a set of numbers. Mathematically the variance of _x_ and variance of _z_ are identical. But the results depend on whether the magnitude of the numbers is large or small.

**set.seed** (2) z <- **rnorm** (10, 0, 1) **formatC** (z[1:5], 20, format = 'f') ## [1] "-0.89691454662498137917" "0.18484918464674249261" ## [3] "1.58784533120882320745" "-1.13037567424628537793" ## [5] "-0.08025175655098928940" x <- z + 1e12 **formatC** (x[1:5], 20, format = 'f') ## [1] "999999999999.10302734375000000000" ## [2] "1000000000000.18481445312500000000" ## [3] "1000000000001.58789062500000000000" ## [4] "999999999998.86962890625000000000" ## [5] "999999999999.91979980468750000000"

1

**formatC** ( **var** (z), 20, format = 'f') ## [1] "0.97020065227876062242" **formatC** ( **var** (x), 20, format = 'f') ## [1] "0.97024419572618270102"

How many digits do these two estimates agree on? Explain why that is the case when mathematically the variance of _z_ and the variance of _x_ are exactly the same. Which of the two is the more accurate answer? You can assume that for a vector _w_ , var( _w_ ) is calculated as<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_wi −w_¯)2</sup><sup>_/_(</sup><sup>_n −_1)</sup>

2. Numerical problems in logistic regression. Consider that in logistic regression the linear predictor, _Xiβ_ , (where _Xi_ is the ith row of the predictor matrix, _X_ ) is transformed into a probability using the inverse logistic (expit) transformation.


where


This mathematical expression for the _expit_ function doesn’t work numerically on a computer for large values of _z_ . Explain why not and re-express the function such that if implemented in computer code, it is numerically stable. Also explain what happens if you use your re-expression but for very small values of _z_ .

3. This problem asks you to use the _future_ package to process some Wikipedia traffic data. The files in **_/scratch/users/paciorek/wikistats/dated_2017_small/dated_** (on the SCF) contain data on the number of visits to different Wikipedia pages on November 4, 2008 (which was the date of the US election in 2008 in which Barack Obama was elected). The columns are: date, time, language, webpage, number of hits, and page size. (Note that in Unit 8 and in PS6, we’ll work with a larger set of the same data using Python’s Dask package.)

   - (a) In an interactive shell on one of the SCF Linux servers named gandalf, radagast, or arwen:

      - i. Copy the files to the ‘/tmp‘ directory. (Recall the use of wildcards in file globbing to select a set of files, from our work with bash.) Putting the files on the local hard drive of the machine you are computing on reduces the amount of copying data across the network (in the situation where you read the data into your program multiple times) and should speed things up in step ii.

      - ii. Write efficient R code to do the following: Using the _future_ package, with either _future_lapply_ or _foreach_ with the _doFuture_ backend, write code that, in parallel, reads in the spacedelimited files and filters to only the rows that refer to pages where "Barack_Obama" appears in the page title (column 4). You can use the code from _unit7-parallel.R_ as a template, in particular the chunks labeled ’rf-example’, ’foreach’ and ’future_lapply’. Collect all the results into a single data frame. Please use 4 cores in your parallelization (the machines have more cores, but other students may be using them at the same time). IMPORTANT: before running the code on the full set of data, please test your code on a small subset first.

2

   - iii. Tabulate the number of hits for each hour of the data. (I don’t care how you do this - you could use _dplyr_ or base R functions or something else.) Make a (time-series) plot showing how the number of visits varied over the day.

- (b) Now replicate steps i and ii but using _sbatch_ to submit your job as a batch job to the SCF Linux cluster, where step ii involves running R from the command line using R CMD BATCH. You don’t need to make the plot again.

Hints: (a) _readr::read_delim()_ should be quite fast if you give it information about the structure of the files, (b) there are lines with fewer than 6 fields, but _read_delim()_ should still work and simply issue a warning, and (c) there are lines that have quotes that should be treated as part of the text of the fields and not as separators.

4. Extra credit: This problem explores the smallest positive number that R can represent and how R represents numbers just larger than the smallest positive number that can be represented. (Note: if you did this in Python you’d get the same results.)

   - (a) By experimentation in R, find the base 10 representation of the smallest positive number that can be represented in R. Hint: it’s rather smaller than 1 _×_ 10<sup>_−_308</sup> .

   - (b) Explain how it can be that we can store a number smaller than 1 _×_ 2<sup>_−_1022</sup> , which is the value of the smallest positive number that we discussed in class. Start by looking at the bit-wise representation of 1 _×_ 2<sup>_−_1022</sup> . What happens if you then figure out the natural representation of 1 _×_ 2<sup>_−_1023</sup> ? You should see that what you get is actually a well-known number that is not equal to 1 _×_ 2<sup>_−_1023</sup> . Given the actual bit-wise representation of 1 _×_ 2<sup>_−_1023</sup> , show the progression of numbers smaller than that that can be represented exactly and show the smallest number that can be represented in R written in both base 2 and base 10.

Hint: you’ll be working with numbers that are not normalized (i.e., denormalized; numbers that do not have 1 as the fixed number before the decimal point in the representation at the bottom of page 7 of Unit 6).

3

---

[Up: contents](../index.md)
