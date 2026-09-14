---
title: 1. A few preparatory notes
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit5-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. A few preparatory notes

**Source:** [`units/unit5-bigData.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## An editorial on 'big data'

'Big data' was trendy for a while, though I guess it's not quite the
buzzword/buzzphrase that it was a few years ago, given the AI/ML
revolution, but of course that revolution is largely based on having
massive datasets available (or scrapeable) online.

Personally, I think some of the hype around giant datasets is justified and some is hype.
Large datasets allow us to address questions that we can't with smaller
datasets, and they allow us to consider more sophisticated (e.g.,
nonlinear) relationships than we might with a small dataset. But they do
not directly help with the problem of correlation not being causation.
Having medical data on every American still doesn't tell me if higher
salt intake causes hypertension. Internet transaction data does not tell
me if one website feature causes increased viewership or sales. One
either needs to carry out a designed experiment or think carefully about
how to infer causation from observational data. Nor does big data help
with the problem that an ad hoc 'sample' is not a statistical sample and
does not provide the ability to directly infer properties of a
population. Consider the immense difficulties we've seen in
answering questions about Covid despite large amounts of data, because it
is incomplete/non-representative. A well-chosen smaller dataset may be much more informative
than a much larger, more ad hoc dataset. However, having big datasets
might allow you to select from the dataset in a way that helps get at
causation or in a way that allows you to construct a
population-representative sample. Finally, having a big dataset also
allows you to do a large number of statistical analyses and tests, so
multiple testing is a big issue. With enough analyses, something will
look interesting just by chance in the noise of the data, even if there
is no underlying reality to it. Here are some examples ([1](https://doi.org/10.1093/jrsssa/qnae039), [2](https://doi.org/10.1093/jrsssa/qnae005)) of bias in analyzing electronic health records (EHR), a common data source for health research.

Different people define the 'big' in big data differently. One
definition involves the actual size of the data, and in some cases the
speed with which it is collected. Our efforts here will focus on dataset
sizes that are large for traditional statistical work but would probably
not be thought of as large in some contexts such as Google or the US
National Security Agency (NSA). Another definition of 'big data' has
more to do with how pervasive data and empirical analyses backed by data
are in society and not necessarily how large the actual dataset size is.


## Logistics and data size

One of the main drawbacks with Python (and R) in working with big data is that all
objects are stored in memory, so you can't directly work with datasets
that are more than 1-20 Gb or so, depending on the memory on your
machine.

The techniques and tools discussed in this Unit  are designed for datasets in the range of gigabytes
to tens of gigabytes, though they may scale to larger if you have a
machine with a lot of memory or simply have enough disk space and are
willing to wait. Also note that if you have 10s of gigabytes of data, you'll be better
off if your machine has 10s of GBs of memory, as discussed in this Unit.

If you're scaling to 100s of GBs, terabytes or petabytes, tools such as
carefully-administered databases, cloud-based tools such as provided by AWS and Google Cloud Platform,
and Spark or other such tools are probably your best bet.

Note: in handling big data files, it's best to have the data on the
local disk of the machine you are using to reduce traffic and delays
from moving data over the network.

## What we already know about handling big data!

UNIX operations are generally very fast, so if you can manipulate your
data via UNIX commands and piping, that will allow you to do a lot.
We've already seen UNIX commands for extracting columns. And various
commands such as `grep`, `head`, `tail`, etc. allow you to pick out rows
based on certain criteria. As some of you have done in problem sets, one
can use `awk` to extract rows. So basic shell scripting may allow you to
reduce your data to a more manageable size.

The tool [GNU parallel](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/running-your-jobs/gnu-parallel/)
allows you to parallelize operations from the command line and is
commonly used in working on Linux clusters.

And don't forget simple things. If you have a dataset with 30 columns
that takes up 10 Gb but you only need 5 of the columns, get rid of the
rest and work with the smaller dataset. Or you might be able to get the
same information from a random sample of your large dataset as you would
from doing the analysis on the full dataset. Strategies like this will
often allow you to stick with the tools you already know.

Also, remember that we can often store data more compactly in binary
formats than in flat text (e.g., csv) files.

Finally, for many applications, storing large datasets in a standard
database will work well.

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. MapReduce and Dask →](03-2-mapreduce-and-dask.md)
