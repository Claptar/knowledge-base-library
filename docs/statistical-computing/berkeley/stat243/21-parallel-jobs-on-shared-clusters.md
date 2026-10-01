---
title: "21. Parallel Jobs on Shared Clusters"
course: "Berkeley Stat 243"
chapter: 21
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Parallel Jobs on Shared Clusters

## What this covers

This is not a lecture but a problem set — Problem Set 5 of Stat 243 (Statistical Computing, UC
Berkeley) — followed across three offerings of the course: fall 2021, fall 2024 and fall 2025. Its
constant piece, present in every year, is a worked case study in running a parallelised,
data-intensive job responsibly on a shared Linux cluster: filtering a real Wikipedia traffic log
for pages about the 2008 US election. Around that constant piece, each offering hangs a different
second topic — SQL query practice in 2024 and 2025, and the limits of double-precision
floating-point arithmetic (plus a simulation-study reading) in 2021. The set supplies little
exposition of its own; it assumes the parallel-computing constructs already taught earlier in the
course (`map` and delayed tasks or Dask bags in Python, `foreach`/`future_lapply` in R), ordinary
file I/O, and, where floating point comes up, the double-precision format introduced earlier in
the course. What follows draws out the reasoning the assignment itself gives for its instructions,
then reproduces its problems as exercises.

## The recurring example: Wikipedia traffic on election night

Every offering filters the same kind of file: space-delimited logs of Wikipedia page visits, one
line per page per hour, with columns for date, time, language, page title, number of hits, and
page size. The task is to keep only the rows whose page title contains "Barack_Obama" and use them
to see how traffic moved around the 2008 US election, in which Obama was elected on November 4.
Two versions of the task recur:

- A single day (November 4, 2008) worth of files, filtered and tabulated by hour of day. Because
  the timestamps are in UTC, a plot of that single day does not show the moment the result was
  announced — that happens on the next version of the exercise.
- A full month, October 15 to November 15, 2008 (roughly 40 GB zipped), filtered and grouped by
  day and hour, which is large enough to show the spike in traffic around election day and the
  announcement of the result at 11 pm Eastern on November 4.

In 2024 and 2025 both versions are done in Python with Dask: the first using `map` or a list of
delayed tasks over the files, the second using Dask's distributed data structures (a Dask bag
converted to a Dask data frame, or `foldby()` from `dask.bag`) so that the grouping and
summarisation also run in parallel. In 2021 the same first version is done in R with the `future`
package, using either `future_lapply` or `foreach` with the `doFuture` backend.

## Working on a shared cluster

The comments spend most of their words on cluster etiquette, and the reasoning behind each
instruction is stated directly in the source, not left implicit.

**Interactive versus batch.** An `srun` session gives an interactive shell on a cluster node,
useful for developing and testing code; `sbatch` submits the same work as a batch job that runs
unattended, wherever the scheduler places it. The exercises ask for both: get the pipeline working
interactively first, then resubmit the working version as a batch job. Because a batch job can
land on any node, a submission script has to do everything the interactive session did by hand —
including copying the input files onto that node's local disk and removing them again — since it
cannot assume the node it lands on is the one it was tested on.

**Copy to local disk once.** Data files are copied into a subdirectory of `/tmp` on the compute
node before processing, rather than read repeatedly from network storage. When a program reads the
same files more than once, this avoids that repeated cost of copying data across the network. The
files should be removed from `/tmp` again once the job finishes: `/tmp` is only cleared out when
the machine reboots, which can take a while, and many students copying files onto the same disk at
once can otherwise run it out of space.

**Ask for only the cores you need, and read that number, don't hard-code it.** Both the `srun`
invocation and the code itself should agree on how many cores to use — four for the single-day
exercise, at most sixteen for the full-month one — so that the rest of the shared machine, and
other students' jobs, are not starved. Because the same code may run with a different core count
on a different submission, it is better to read the number of workers from the Slurm environment
variables `SLURM_NTASKS` or `SLURM_CPUS_PER_TASK` (set by `--ntasks-per-node` or `--cpus-per-task`)
than to fix it as a constant.

**Two smaller mechanical points.** A standalone Dask script run via `sbatch` needs its Dask code
placed inside an `if __name__ == '__main__':` block, as Dask's own documentation on standalone
scripts explains. And requesting `--mem-per-cpu` explicitly (5G, in these exercises) turned out to
be necessary for a Dask job under Slurm even though memory does not normally need to be requested
on this cluster — the set describes this as an unresolved quirk of how the two interact, not as a
general rule.

<figure>
<svg viewBox="0 0 680 260" role="img" aria-label="Data flow for a parallel job on the shared cluster: files are copied once from network storage to local /tmp, read and filtered by several workers running in parallel, collected into one data frame, and then removed from /tmp.">
  <defs>
    <marker id="arrow-c21" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0L10,5L0,10z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="10" y="105" width="120" height="50" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="70" y="134" text-anchor="middle" font-size="12" fill="currentColor">network storage</text>

  <line x1="130" y1="130" x2="176" y2="130" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <text x="153" y="120" text-anchor="middle" font-size="11" fill="currentColor">copy once</text>

  <rect x="180" y="105" width="120" height="50" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="240" y="128" text-anchor="middle" font-size="12" fill="currentColor">/tmp on the</text>
  <text x="240" y="143" text-anchor="middle" font-size="12" fill="currentColor">compute node</text>

  <line x1="300" y1="120" x2="378" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <line x1="300" y1="130" x2="378" y2="130" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <line x1="300" y1="140" x2="378" y2="205" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <text x="330" y="95" text-anchor="middle" font-size="11" fill="currentColor">read + filter</text>
  <text x="330" y="108" text-anchor="middle" font-size="11" fill="currentColor">(in parallel)</text>

  <rect x="380" y="30" width="120" height="40" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="440" y="55" text-anchor="middle" font-size="12" fill="currentColor">worker 1</text>
  <rect x="380" y="110" width="120" height="40" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="440" y="135" text-anchor="middle" font-size="12" fill="currentColor">worker 2</text>
  <rect x="380" y="190" width="120" height="40" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="440" y="215" text-anchor="middle" font-size="12" fill="currentColor">worker N</text>

  <line x1="500" y1="50" x2="558" y2="118" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <line x1="500" y1="130" x2="558" y2="130" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <line x1="500" y1="210" x2="558" y2="142" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-c21)"/>
  <text x="530" y="90" text-anchor="middle" font-size="11" fill="currentColor">collect</text>

  <rect x="560" y="105" width="110" height="50" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="615" y="126" text-anchor="middle" font-size="12" fill="currentColor">single data</text>
  <text x="615" y="141" text-anchor="middle" font-size="12" fill="currentColor">frame</text>

  <line x1="240" y1="155" x2="240" y2="222" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-c21)"/>
  <text x="240" y="240" text-anchor="middle" font-size="11" fill="currentColor">removed once the job ends</text>
</svg>
<figcaption>Files travel from shared network storage to a compute node's local disk once, are read
and filtered there by several workers in parallel, and are collected into one result before the
local copy is cleaned up.</figcaption>
</figure>

## Test small before you scale

The set is explicit about why: reading and filtering the full month of data takes on the order of
30 minutes even with 16 cores, so a bug caught only at that scale wastes a slot on a machine other
students are also queued for. Every version of the exercise therefore asks for the same discipline
before submitting the full job: test the filtering function serially on a single input file, then
on a small subset of files — on a laptop or one of the standalone SCF machines — and only then run
it at full scale on the cluster. For the large, month-long dataset there is a second reason not to
copy it locally at all: it already sits in a shared, read-only location on every cluster node, and
each student making a personal copy would overload the disks that everyone else is also using.

## Reading real, messy data

The raw files are not clean space-delimited tables, and the set's tips describe exactly what
breaks a naive read: some lines have fewer than the expected six fields, and some fields contain
literal quote characters that a parser could mistake for field delimiters. In pandas, this is
handled by forcing `dtype=str` on the date and time columns specifically — so as not to lose
information needed later to reconstruct a timestamp — while leaving the other columns to be
inferred, and by passing pandas' `quoting` argument so that literal quotes are treated as text
rather than as separators. In R, `readr::read_delim()` copes with the short lines on its own,
simply issuing a warning rather than failing. Once the timestamp is parsed, the hour-of-day
extraction should use `datetime`/Pandas date-time functions rather than string manipulation on the
raw date and time fields.

## Exercises

The problems below are reproduced from the assignment; they are not solved here.

**Wikipedia traffic, single day (2024/2025 version, using Dask).**

1. Using the November 4, 2008 Wikipedia traffic files on the SCF cluster (six columns: date, time,
   language, page title, number of hits, page size):
   a. Start an interactive session on the cluster with `srun`, requesting four cores. Copy the
      day's files into a subdirectory of `/tmp` on the node. Using Dask (`map` or a list of
      delayed tasks), read and filter the files in parallel to the rows whose page title contains
      "Barack_Obama", using exactly four cores, and collect the result into a single data frame.
      Test your filtering function on one file serially, and your parallel code on a small subset,
      before running it on the full day. Tabulate the number of hits by hour of day and plot how
      traffic varied over the day, using proper datetime handling rather than string manipulation.
      Remove the copied files from `/tmp` when done.
   b. Repeat the copy-and-filter steps as a batch job submitted with `sbatch`, running your Python
      script from the command line with its Dask code inside an `if __name__ == '__main__':`
      block. The submission script itself must copy the files to `/tmp` and remove them at the
      end, since the job may run on any node. You do not need to remake the plot.

2. Now consider the full October 15 – November 15, 2008 traffic (already present, unzipped, in a
   shared read-only location on every cluster node — do not make a personal copy). As in problem
   1, filter to English-language pages with "Barack_Obama" in the title, but this time using Dask's
   distributed data structures (a Dask bag, converted to a Dask data frame for the grouping step,
   or `foldby()`). Group the results by day and hour. Time how long the Dask portion of the
   computation takes. Test on a small subset of files before running at full scale — the full
   filtering pass takes roughly 30 minutes on 16 cores — and use no more than 16 cores in your job
   submission (drop to 8 if the job sits queued too long). Read the number of workers to start from
   the `SLURM_NTASKS` or `SLURM_CPUS_PER_TASK` environment variable rather than hard-coding it.
   Once you have the day-hour counts, produce plots (using any tool) showing traffic over the whole
   month, and in particular over November 3–5.

**SQL practice (2024/2025 version), using the Stack Overflow database.**

3. a. Find all users, including their `displayname`, who have asked a question but never answered
      one. Provide as many separate queries as needed to demonstrate, between them, all of: a
      subquery in a `WHERE` clause, a subquery in a `FROM` clause, a set operation
      (`INTERSECT`, `UNION`, or `EXCEPT`), and an outer join (SQLite has no right outer join, so
      express it some other way). Confirm that the different queries return the same count of
      results. Note that both the questions and answers tables contain rows with a `NULL`
      `ownerid`, which can break some forms of these queries; start by creating views that exclude
      those rows, and build the main queries on top of the views.
   b. Compare how much time the different query approaches take, and compare running them under
      SQLite versus DuckDB.

**Floating-point representation (2021 version).**

4. Recall the normalised double-precision format $(-1)^S \times 1.d \times 2^{e-1023}$, where $d$
   is represented with 52 bits. Show, for a few small cases, how the integers
   $1, 2, 3, \dots, 2^{53}-1$ are stored exactly in this format. Then show that $2^{53}$ and
   $2^{53}+2$ can be represented exactly but $2^{53}+1$ cannot — so at that magnitude the spacing
   between representable numbers is 2 — and that from $2^{54}$ onward the spacing is 4. (You may
   write the exponent in base 10.) Confirm that evaluating $2^{53}-1$, $2^{53}$, and $2^{53}+1$ in
   R is consistent with what you showed.

5. Consider summing the number 1 together with 10,000 copies of $1 \times 10^{-16}$; mathematically
   the result is $1.000000000001$.
   a. Given finite precision, how many digits of accuracy can the stored result have at best — that
      is, if $1.000000000001$ itself is stored on a computer, how many of its digits are accurate?
   b. In R, build the vector $x = c(1, 10^{-16}, \dots, 10^{-16})$ (10,000 copies of $10^{-16}$).
      Does `sum(x)` match the accuracy from part (a)?
   c. Do the same in Python (`vec = np.array([1e-16] * 10001)`), using `decimal.Decimal` to display
      extra digits.
   d. Using a loop, compute the sum left to right, $((x_1 + x_2) + x_3) + \dots$. Does it match the
      expected accuracy? Repeat with the single 1 moved to the end of the vector instead of the
      start. If either loop version does not match, how many decimal places of accuracy does it
      have? Do both variants in Python as well. Your results from (b) and (d) should show that R's
      `sum()` is not simply adding the numbers left to right.

**Wikipedia traffic, single day (2021 version, using the `future` package in R).**

6. a. In an interactive shell on one of the standalone SCF Linux servers, copy the day's files to a
      subdirectory of `/tmp`. Using the `future` package (`future_lapply`, or `foreach` with the
      `doFuture` backend), read and filter the files in parallel to the rows with "Barack_Obama" in
      the page title, using four cores, and collect the result into one data frame. Test your
      function serially on one file, and in parallel on a small subset, before running the full
      day. Tabulate hits by hour and plot how traffic varied over the day.
   b. Repeat the copy-and-filter steps as a batch job submitted with `sbatch`, running R from the
      command line with `R CMD BATCH`. The submission script must copy the files to `/tmp` itself.
      You do not need to remake the plot.

**Reading and critiquing a simulation study (2021 version).**

7. Read Sections 1, 2.1, and 4 of Cao et al. (2015, *Journal of the Royal Statistical Society,
   Series B*). You do not need to understand their estimating-equation method or its theory; treat
   it as a black-box alternative to least squares, and treat their kernel as simply downweighting
   pairs of observation and covariate that are measured far apart in time. In a few sentences each:
   a. What are the goals of their simulation study, and what metrics do they use to assess their
      method?
   b. What choices did the authors have to make in designing the simulation study? Which aspects
      of their data-generating mechanism might affect how favourably their method is assessed?
   c. Looking at their Tables 1 and 3, what would you want to see, numerically, in those columns
      for a method to count as good?

**Extra credit: the smallest representable double (2021 version).**

8. a. By experimentation in R, find the smallest positive number R can represent, in base 10. (It
      is considerably smaller than $1 \times 10^{-308}$.)
   b. Explain how a number smaller than $2^{-1022}$ — the smallest normalised double discussed in
      lecture — can be represented at all. Start from the bit-wise representation of $2^{-1022}$,
      then work out what bit pattern would naturally follow for $2^{-1023}$; you should find it
      equals a different, well-known number rather than literally $2^{-1023}$. Using that pattern,
      show the progression of representable numbers below $2^{-1022}$ down to the smallest one,
      writing the smallest in both base 2 and base 10. (These are denormalised numbers — numbers
      whose representation does not have a leading 1 before the binary point.)

## Sources

- Cluster-etiquette comments, the Wikipedia single-day and full-month Dask exercises, and the
  parsing tips: `fall-2024/ps/ps5/01-comments.md` and `fall-2024/ps/ps5/02-problems.md` (problems 1
  and 2), due 2024-10-28, and the equivalent combined `fall-2025/ps/ps5.md` (problems 1 and 2), due
  2025-10-29 — both converted losslessly from the course's `ps5.qmd`, licensed CC BY 4.0.
- The SQL exercise: `fall-2024/ps/ps5/02-problems.md` and `fall-2025/ps/ps5.md`, problem 3 in each.
- The floating-point, summation-accuracy, R/`future`-package parallel processing, simulation-study,
  and extra-credit exercises: `stat243-fall-2021/ps/ps5.md`, problems 1, 2, 3, 4, and 5. This file
  is a model's reconstruction of a PDF with no extractable text layer (`fidelity: reconstructed`,
  licensed CC0-1.0); the source itself flags every equation as unverified, so the floating-point
  format equation and the numerical values reproduced above should be treated as a paraphrase and
  checked against the original PDF rather than cited directly.
- Referred to but not supplied: the Unit 6 and Unit 7 course notes (the parallel-computing and
  floating-point background these exercises assume, including `unit7-parallel.R` and the specific
  page of the Unit 6 notes on denormalised numbers), the Unit 9 notes on simulation studies, and
  Cao et al. (2015), *Journal of the Royal Statistical Society, Series B* (`cao_etal_2015.pdf`).

---

[← 20. Problem Set 4](20-problem-set-4.md) · [Contents](index.md) · [22. Floating-Point Precision and Importance Sampling →](22-floating-point-precision-and-importance-sampling.md)
