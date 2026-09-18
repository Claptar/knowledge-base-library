---
title: 2. Reading data into Python
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) — berkeley-stat243 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2. Reading data into Python

The main downside to working with datasets in Python (true for R and most other languages as well) is that the entire
dataset resides in memory, so using standard Python tools can be problematic
in some cases; we'll discuss some alternatives later.

## (BACKGROUND) Core Python functions for text files

The `read_table`  and `read_csv` functions in the Pandas package are  commonly used for reading
in data. They read in delimited files (CSV specifically in the latter case).
The key arguments are the
delimiter (the `sep` argument) and whether the file contains a header, a
line with the variable names. We can use `read_fwf()` to read from a
fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how
Pandas determines the types of the fields that are read in. While Pandas
will try to determine the types automatically, it can be safer (and faster)
to tell Pandas what the types are, using the `dtype` argument to `read_table()`.

Let's work through a couple examples. Before we do that, let's look at
the arguments to `read_table`. Note that `sep=''` can use regular expressions
(which would be helpful if you want to separate on any amount of white space, as one example).

```python
import os
import pandas as pd

dat = pd.read_table(os.path.join('..', 'data', 'RTADataSub.csv'),
                    sep = ',', header = None)
dat.dtypes.head()   # 'object' is string or mixed type
dat.loc[0,1]
type(dat.loc[0,1]) # string!
## Whoops, there is an 'x', presumably indicating missingness:
dat.loc[:,1].unique()
```

```python
## Let's treat 'x' as a missing value indicator.
dat2 = pd.read_table(os.path.join('..', 'data', 'RTADataSub.csv'),
                     sep = ',', header = None, na_values = 'x')
dat2.dtypes.head()
dat2.loc[:,1].unique()
```

Using `dtype` is a good way to control how data are read in.
Here's an example with a CSV file containing some HIV genome sequence information.

```python
dat = pd.read_table(os.path.join('..', 'data', 'hivSequ.csv'),
                  sep = ',', header = 0,
                  dtype = {
                  'PatientID': int,
                  'Resp': int,
                  'PR Seq': str,
                  'RT Seq': str,
                  'VL-t0': float,
                  'CD4-t0': int})
dat.dtypes
dat.loc[0,'PR Seq']
```

Note that you can avoid reading in one or more columns by using the
`usecols` argument. Also,
specifying the `dtype` argument explicitly should make for faster
file reading.

If possible, it's a good idea to look through the input file in the
shell or in an editor before reading into Python to catch such issues in
advance. Using the UNIX command `less` on `RTADataSub.csv` would have revealed these
various issues, but note that `RTADataSub.csv` is a 1000-line subset of
a much larger file of data available from the kaggle.com website. So
more sophisticated use of UNIX utilities (as we will see in Unit 3) is often
useful before trying to read something into a program.

If the file is not nicely arranged by field (e.g., if it has ragged
lines), we'll need to do some more work. We can read each line
as a separate string, after which we can process the
lines using text manipulation. Here's an example from some US
meteorological data where I know from metadata (not provided here) that
the 4-11th values are an identifier, the 17-20th are the year, the
22-23rd the month, etc.

```python
file_path = os.path.join('..', 'data', 'precip.txt')
with open(file_path, 'r') as file:
     lines = file.readlines()

ids = [line[3:11] for line in lines]
year = [int(line[17:21]) for line in lines]
month = [int(line[21:23]) for line in lines]
nvalues = [int(line[27:30]) for line in lines]
year[0:5]
```

Actually, that file, `precip.txt`, is in a "fixed-width" format (i.e.,
every element in a given column has the exact same number of
characters),so reading in using `pandas.read_fwf()` would be a good strategy.

!!! tip "Tip"
The use of `with` above is the standard Python way to open files. It automatically closes the file after the body of the `with` statement finishes.
:::

## Connections and streaming

Python allows you to read in not just from a file but from a more general
construct called a *connection*. This can include reading in text from the output of running a shell command and from unzipping a file on the fly.

Here are some examples of connections:

```python
#| eval: false
import gzip
with gzip.open('dat.csv.gz', 'r') as file:
     lines = file.readlines()

import zipfile
with zipfile.ZipFile('dat.zip', 'r') as archive:
     with archive.open('data.txt', 'r') as file:
          lines = file.readlines()

import subprocess
command = "ls -al"
output = subprocess.check_output(command, shell = True)
# `output` is a sequence of bytes.
with io.BytesIO(output) as stream:  # Create a file-like object.
    content = stream.readlines()

df = pd.read_csv("https://download.bls.gov/pub/time.series/cu/cu.item", sep="\t")
```

If a file is large, we may want to read it in in chunks (of lines), do
some computations to reduce the size of things, and iterate. This is referred
to as online processing, streaming, or chunking, and can be done [using Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking) (among other tools).

```python
#| eval: false
file_path = os.path.join('..', 'data', 'RTADataSub.csv')
chunksize = 50 # Obviously this would be much larger in any real application.

with pd.read_csv(file_path, chunksize = chunksize) as reader:
     for chunk in reader:
         # Manipulate the lines and store the key stuff.
         print(f'Read {len(chunk)} rows.')

```

More details on sequential (on-line) processing of large files can be
found in the tutorial on large datasets mentioned in the reference list
above.

One cool trick that can come in handy is to 'read' from a string as if it were a text
file. Here's an example:

```python
import io

file_path = os.path.join('..', 'data', 'precip.txt')
with open(file_path, 'r') as file:
     text = file.read()

stringIOtext = io.StringIO(text)
df = pd.read_fwf(stringIOtext, header = None, widths = [3,8,4,2,4,2])
```

We can create connections for writing output too. Just make sure to open
the connection first.

## File paths

A few notes on file paths, related to ideas of reproducibility.

1.  In general, you don't want to hard-code absolute paths into your
    code files because those absolute paths won't be available on the
    machines of anyone you share the code with. Instead, use paths
    relative to the directory the code file is in, or relative to a
    baseline directory for the project, e.g.:\

    ```python
    #| eval: false
    dat = pd.read_csv('../data/cpds.csv')
    ```

2.  Using UNIX style directory separators will work in Windows, Mac or
    Linux, but using Windows-style separators is not portable across
    operating systems.

    ```python
    #| eval: false
    ## good: will work on Windows
    dat = pd.read_csv('../data/cpds.csv')
    ## bad: won't work on Mac or Linux
    dat = pd.read_csv('..\data\cpds.csv')
    ```

3.  Even better, use `os.path.join` so that paths are constructed
    specifically for the operating system the user is using:\

    ```python
    #| eval: false
    ## good: operating-system independent
    dat = pd.read_csv(os.path.join('..', 'data', 'cpds.csv'))
    ```

## Reading data quickly: Arrow and Polars

Apache Arrow provides efficient data structures for working with data in memory, usable in Python via the PyArrow package. Data are stored by column, with values in a column stored sequentially and in such a way that one can access a specific value without reading the other values in the column (O(1) lookup). Arrow is designed to read data from various file formats, including Parquet, native Arrow format, and text files. In general Arrow will only read data from disk as needed, avoiding keeping the entire dataset in memory.

Other options for avoiding reading all your data into memory include the Dask package and using `numpy.load` with the `mmap_mode` argument.

`polars` is designed to be a faster alternative to Pandas for working with data in-memory.

```python
import polars
import time
t0 = time.time()
dat = pd.read_csv(os.path.join('..', 'data', 'airline.csv'))
t1 = time.time()
dat2 = polars.read_csv(os.path.join('..', 'data', 'airline.csv'), null_values = ['NA'])
t2 = time.time()
print(f"Timing for Pandas: {t1-t0}.")
print(f"Timing for Polars: {t2-t1}.")
```

---

[← 1. Text manipulation, string processing and regular expressions (regex)](02-1-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [3. Output from Python →](04-3-output-from-python.md)
