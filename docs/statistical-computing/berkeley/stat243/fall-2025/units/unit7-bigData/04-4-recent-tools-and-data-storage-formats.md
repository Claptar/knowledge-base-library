---
title: 4. Recent tools and data storage formats
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit7-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4. Recent tools and data storage formats

There has been a lot of work in recent years to provide file formats and tools for working with very large datasets in ways other than traditional databases, often optimized for speed when doing large-scale analytics on the data.

Rather than being stored in a formal database, data are often stored in multiple files, often using Parquet ([discussed in Unit 2](../unit2-dataTech/index.md)) or CSV as the file format. When stored in the cloud, this is often referred to as a *data lake*.

We'll briefly discuss *Apache Arrow*. Apache Arrow provides efficient data structures for working with data in memory, usable via the `PyArrow` package in Python (and the `arrow` package in R). Data are stored by column, with values in a column stored sequentially and in such a way that one can access a specific value without reading the other values in the column (O(1) lookup).

Arrow is designed to read data from various file formats, including Parquet, native Arrow format, and text files. In general Arrow will only read data from disk as needed, avoiding keeping the entire dataset in memory. Here's a [good discussion comparing different file formats](https://stackoverflow.com/questions/56472727/difference-between-apache-parquet-and-arrow).

After loading the data in (which doesn’t initially involve actually reading the data from disk), you can then operate on the resulting object. PyArrow will only read the data it needs for your computations (how much has to be read depends on the file format, with the native `arrow` format best in this regard), which can reduce I/O and memory usage.

*Polars* is advertised as a very fast in-memory package for working with dataframes (i.e., an alternative to Pandas) that provides a Python interface. It uses the Arrow columnar format. It also provides a lazy execution model like Spark or Dask that allows for automatic optimization of queries.

## 5. Sparsity

A lot of statistical methods are based on sparse matrices. These
include:

-   Matrices representing the neighborhood structure (i.e., conditional
    dependence structure) of networks/graphs.
-   Matrices representing autoregressive models (neighborhood structure
    for temporal and spatial data)
-   A statistical method called the *lasso* is used in high-dimensional
    contexts to give sparse results (sparse parameter vector estimates,
    sparse covariance matrix estimates)
-   There are many others (I've been lazy here in not coming up with a
    comprehensive list, but trust me!)

When storing and manipulating sparse matrices, there is no need to store
the zeros, nor to do any computation with elements that are zero.

Python, R, and MATLAB all have functionality for storing and computing
with sparse matrices. We'll see this a bit more in the linear algebra
unit.

Here's a [blog
post](http://blog.revolutionanalytics.com/2011/05/the-neflix-prize-big-data-svd-and-r.html)
describing the use of sparse matrix manipulations for analysis of the
Netflix Prize data.

---

[← 3. Databases](03-3-databases.md) · [Up: contents](index.md) · 6. Using statistical concepts to deal with computational bottlenecks →
