---
title: 4. Recent tools and data storage formats
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit7-bigData.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Recent tools and data storage formats

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

There has been a lot of work in recent years to provide file formats and tools for working with very large datasets in ways other than traditional databases, often optimized for speed when doing large-scale analytics on the data.

Rather than being stored in a formal database, data are often stored in multiple files, often using Parquet ([discussed in Unit 2](../unit2-dataTech/index.md)) or CSV as the file format. When stored in the cloud, this is often referred to as a *data lake*.

We'll briefly discuss *Apache Arrow*. Apache Arrow provides efficient data structures for working with data in memory, usable via the `PyArrow` package in Python (and the `arrow` package in R). Data are stored by column, with values in a column stored sequentially and in such a way that one can access a specific value without reading the other values in the column (O(1) lookup).

Arrow is designed to read data from various file formats, including Parquet, native Arrow format, and text files. In general Arrow will only read data from disk as needed, avoiding keeping the entire dataset in memory. Here's a [good discussion comparing different file formats](https://stackoverflow.com/questions/56472727/difference-between-apache-parquet-and-arrow).

After loading the data in (which doesn’t initially involve actually reading the data from disk), you can then operate on the resulting object. PyArrow will only read the data it needs for your computations (how much has to be read depends on the file format, with the native `arrow` format best in this regard), which can reduce I/O and memory usage.

*Polars* is advertised as a very fast in-memory package for working with dataframes (i.e., an alternative to Pandas) that provides a Python interface. It uses the Arrow columnar format. It also provides a lazy execution model like Spark or Dask that allows for automatic optimization of queries.

---

[← 3. Databases](08-3-databases.md) · [Up: contents](index.md) · [5. Sparsity →](10-5-sparsity.md)
