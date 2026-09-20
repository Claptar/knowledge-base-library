---
title: "45. Preparatory Notes on Big Data"
course: "Berkeley Stat 243 Fall 2024"
chapter: 45
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 45. Preparatory Notes on Big Data

## What this covers

This is the scene-setting lecture that opens Stat 243's unit on "big data." It does not teach a
technique yet — that comes in the sections that follow, on MapReduce/Dask and on databases — but it
calibrates the unit: what "big" is going to mean here, roughly how large a dataset has to be before
the tools you already use (Python, R, objects held in memory) stop working, and how much of the
problem the skills you already have from earlier in the course — the shell, `grep`, `awk`, and an
understanding of disk versus memory — already solve before you reach for anything new. It assumes
you can work from the command line and have used basic UNIX tools such as `grep`, `head`, `tail`,
and `awk` to filter and extract fields from a text file.

The unit itself concentrates on Dask and on databases/SQL; material on Spark is included for
reference only and is not treated as required.

## An editorial on "big data"

"Big data" was a trend before it was a fixture: it is not the buzzphrase it once was, mostly
because it has been absorbed into the AI/ML wave, which itself depends on having enormous datasets
available or scrapeable online. The size of the hype is worth separating from the size of the
benefit.

Large datasets genuinely let you address questions that smaller ones cannot, and they let you
entertain more sophisticated — for instance nonlinear — relationships than a small dataset would
support. What they do not do is solve the problem that correlation is not causation. Medical data on
every American still does not establish that higher salt intake causes hypertension; internet
transaction data does not establish that a website feature caused a change in sales. Either you run
a designed experiment, or you reason carefully about how to get at causation from observational
data — size alone does not substitute for that reasoning. The difficulties in drawing firm
conclusions about Covid despite enormous quantities of data illustrate the same point from the other
direction: the data were large but incomplete and non-representative, and an ad hoc "sample"
collected because it happened to be available is not a statistical sample. It does not license
inference about a population the way a designed sample does. A well-chosen small dataset can be far
more informative than a much larger but haphazard one.

That said, a big dataset can help you get closer to a genuine answer, precisely because its size
gives you room to select from it: you can construct something closer to a population-representative
sample, or select in a way that helps isolate a causal effect. And a large dataset invites a large
number of analyses and tests, which raises multiple testing as a serious concern — run enough tests
and something will look interesting purely by chance, with no underlying reality behind it.
(Recorded examples of this kind of bias turning up in analyses of electronic health records, a
common data source in health research, are given at
[doi.org/10.1093/jrsssa/qnae039](https://doi.org/10.1093/jrsssa/qnae039) and
[doi.org/10.1093/jrsssa/qnae005](https://doi.org/10.1093/jrsssa/qnae005).)

People also disagree about what "big" means. One definition is about actual size — the number of
bytes, and sometimes the rate at which they arrive. On that definition, this unit's techniques are
aimed at datasets that are large by the standards of ordinary statistical work but would not count
as large at all to, say, Google or the NSA. A second, looser definition has less to do with the size
of any one dataset and more to do with how pervasive data-backed empirical analysis has become in
society generally.

## Scale and logistics

Python and R both keep their objects in memory. That is the practical constraint that determines
when you need something beyond the tools you already know: you cannot directly work with a dataset
much larger than roughly 1–20 GB, depending on how much memory your machine has.

The tools this unit covers — apart from the brief treatment of MapReduce/Spark, included for
reference only — are aimed at datasets of a few gigabytes up to a few tens of gigabytes. They can
scale further if the machine has more memory, or if you simply have enough disk space and are
willing to wait. As a rule of thumb, if you have tens of gigabytes of data, you want tens of
gigabytes of memory on the machine you're using. Beyond that — hundreds of gigabytes, terabytes, or
petabytes — the better bet is a carefully-administered database, a cloud platform such as AWS or
Google Cloud, or a tool such as Spark.

One detail that is easy to overlook: when working with a big data file, keep the data on the local
disk of the machine doing the computing. Moving data over the network adds traffic and delay that
a local disk avoids.

## What you already know that already helps

Before reaching for a new tool, it's worth remembering how much of the problem ordinary UNIX
operations already solve. UNIX operations are fast, and manipulating data via shell commands and
piping goes a long way. Extracting columns, and commands such as `grep`, `head`, and `tail` for
picking out rows by some criterion, are things you've already used; `awk` for extracting rows is
something several of you have already used in problem sets. Basic shell scripting can shrink a
dataset to something manageable before it ever needs to be loaded anywhere.

[GNU parallel](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/running-your-jobs/gnu-parallel/)
lets you parallelize operations from the command line, and is a standard tool for working on Linux
clusters.

A few other simple habits go a long way, and let you keep using tools you already know rather than
adopting new ones:

- If a dataset has 30 columns and takes up 10 GB but you only need 5 of them, drop the rest before
  you do anything else.
- A random sample of a large dataset may give you the same information as an analysis of the full
  dataset — check whether you actually need all of it.
- Data stored in a binary format is usually far more compact than the same data in flat text (e.g.,
  CSV).
- For many applications, simply storing the data in a standard database is enough — the subject of
  the next part of this unit.

## Sources

- Berkeley Stat 243, Fall 2024, Unit 7 ("A few preparatory notes"):
  `docs/statistical-computing/berkeley/stat243/fall-2024/units/unit7-bigData/01-1-a-few-preparatory-notes.md`.
- Berkeley Stat 243, Fall 2025, Unit 7 ("A few preparatory notes"):
  `docs/statistical-computing/berkeley/stat243/fall-2025/units/unit7-bigData/01-1-a-few-preparatory-notes.md`
  — nearly identical to the Fall 2024 version; used as the primary text here because it is the more
  recent revision and adds the citations on bias in electronic-health-record analyses.
- Course references named in both versions: the SCF tutorial "Working with large datasets in SQL,
  R, and Python" (`computing.stat.berkeley.edu/tutorial-databases`), the tutorial on parallel
  processing with Dask/`future` (`computing.stat.berkeley.edu/tutorial-dask-future`), and Murrell,
  *Introduction to Data Technologies* — named as course reading, not reproduced here.
- Also read for context, but not part of this lecture and not used above: the rest of the same
  unit's material on MapReduce/Dask/Hadoop/Spark, databases and SQL, recent storage formats, and
  using statistical ideas against computational bottlenecks (Fall 2024 and Fall 2025 files 02–05 of
  `unit7-bigData`), which belong to later sections of the unit; Fall 2026's `unit7-dataTech`, where
  this unit slot was reorganized around a different topic (web APIs, HTML/XML/JSON, and file
  encodings) and no longer contains a "preparatory notes" counterpart; and Fall 2021's
  `unit7-parallel` (scenarios for parallelization, overview of parallel processing), which is an
  older, unrelated topic that this course now covers under its parallelization unit rather than
  under "big data" — that file is also an LLM reconstruction from a PDF with no text layer, flagged
  by its source as unverified in its equations.

---

[← 44. Principles of Parallel Computing](44-principles-of-parallel-computing.md) · [Contents](index.md) · [46. Floating-Point Numbers and Precision →](46-floating-point-numbers-and-precision.md)
