---
title: output is a sequence of bytes.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# output is a sequence of bytes.

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← 2. Reading data into Python](03-2-reading-data-into-python.md) · [Up: contents](index.md) · [3. Output from Python →](05-3-output-from-python.md)
