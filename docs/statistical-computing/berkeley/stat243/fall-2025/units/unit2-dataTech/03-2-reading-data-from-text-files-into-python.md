---
title: 2. Reading data from text files into Python
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Reading data from text files into Python

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Core Python functions

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

id = [line[3:11] for line in lines]
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

---

[← 1. Data storage and file formats on a computer](02-1-data-storage-and-file-formats-on-a-computer.md) · [Up: contents](index.md) · [output is a sequence of bytes. →](04-output-is-a-sequence-of-bytes.md)
