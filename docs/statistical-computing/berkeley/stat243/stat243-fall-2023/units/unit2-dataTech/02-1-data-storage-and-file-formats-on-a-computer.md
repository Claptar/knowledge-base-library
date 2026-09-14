---
title: 1. Data storage and file formats on a computer
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Data storage and file formats on a computer

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

This unit largely covers topics relevant for early on in the data analysis pipeline: getting data,
reading data in, writing data out to disk, and webscraping. We'll focus
on doing these manipulations in Python, but the concepts and tools involved
are common to other languages, so familarity with these in Python should
allow you to pick up other tools easily. The main downside to
working with datasets in Python (true for R and most other languages as well) is that the entire
dataset resides in memory, so using standard Python tools can be problematic
in some cases; we'll discuss some alternatives later.  Python (and similar
languages) has the capability to read in a wide variety of file formats.

## Text and binary files

In general, files can be divided into text files and binary files. In
both cases, information is stored as a series of bits. Recall that a bit
is a single value in base 2 (i.e., a 0 or a 1), while a byte is 8 bits.

A **text file** is one in which the bits in the file encode individual
characters. Note that the characters can include the digit characters
0-9, so one can include numbers in a text file by writing down the
digits needed for the number of interest. Examples of text file formats
include CSV, XML, HTML, and JSON.

Text files may be simple ASCII files (i.e., files encoded using ASCII)
or files in other encodings such as UTF-8, both covered in Section 5.
[ASCII](http://en.wikipedia.org/wiki/ASCII) files have 8 bits (1 byte)
per character and can represent 128 characters (the 52 lower and upper
case letters in English, 10 digits, punctuation and a few other things
-- basically what you see on a standard US keyboard). UTF-8 files have
between 1 and 4 bytes per character.

Some text file formats, such as JSON or HTML, are not easily interpretable/manipulable
on a line-by-line basis (unlike, e.g., CSV), so they are not as amenable
to processing using shell commands.


A **binary file** is one in which the bits in the file encode the
information in a custom format and not simply individual characters.
Binary formats are not (easily) human readable but can be more
space-efficient and faster to work with (because it can allow random
access into the data rather than requiring sequential reading). The
meaning of the bytes in such files depends on the specific binary format
being used and a program that uses the file needs to know how the format
represents information. Examples of binary files include netCDF files, Python pickle files,
R data (e.g., .Rda) files, , and compiled code files.

Numbers in binary files are usually stored as 8 bytes per number. We'll
discuss this much more in Unit 8.

## Common file types

Here are some of the common file types, some of which are text formats and some of which are binary formats.

1.  'Flat' text files: data are often provided as simple text files.
    Often one has one record or observation per row and each column or
    field is a different variable or type of information about the
    record. Such files can either have a fixed number of characters in
    each field (*fixed width format*) or a special character (a *delimiter*)
    that separates the fields in each row. Common delimiters are tabs,
    commas, one or more spaces, and the pipe (\|). Common file
    extensions are `.txt` and `.csv`. Metadata (information about the
    data) are often stored in a separate file. CSV files are quite
    common, but if you have files where the data contain commas, other
    delimiters might be preferable. Text can be put in quotes in CSV files, and
    this can allow use of commas within the data. This is difficult to
    deal with from the command line, but `read_table()` in Pandas handles this situation.

    -   One occasionally tricky difficulty is as follows. If you have a
        text file created in Windows, the line endings are coded
        differently than in UNIX. Windows uses a newline
        (the ASCII character `\n`)
        and a carriage return (the ASCII character `\r`) whereas
        UNIX uses onlyl a  newline in UNIX). There are
        UNIX utilities (`fromdos` in
        Ubuntu, including the SCF Linux machines and `dos2unix` in other
        Linux distributions) that can do the necessary conversion. If
        you see `\^M` at the end of the lines in a file, that's the tool
        you need. Alternatively, if you open a UNIX file in Windows, it
        may treat all the lines as a single line. You can fix this with
        `todos` or `unix2dos`.

2.  In some contexts, such as textual data and bioinformatics data, the
    data may be in a text file with one piece of information per row, but
    without meaningful columns/fields.

3.  Data may also be in text files in formats designed for data
    interchange between various languages, in particular XML or JSON.
    These formats are "self-describing"; namely the metadata is part of
    the file. The `lxml` and `json` packages are useful for
    reading and writing from these formats. More in Section 4.

4.  You may be scraping information on the web, so dealing with text
    files in various formats, including HTML. The `requests` and `BeautifulSoup`
    packages are useful for reading HTML.

5.  In scientific contexts, netCDF (`.nc`) (and the related HDF5) are
    popular format for gridded data that allows for highly-efficient
    storage and contains the metadata within the file. The basic
    structure of a netCDF file is that each variable is an array with
    multiple dimensions (e.g., latitude, longitude, and time), and one
    can also extract the values of and metadata about each dimension.
    The `netCDF4` package in Python nicely handles working with netCDF files.

6.  Data may already be in a database or in the data storage format of another
    statistical package (`Stata`, `SAS`, `SPSS`, etc.). The `Pandas`
    package in Python has  capabilities for importing Stata
    (`read_stata`), SPSS (`read_spss`), and SAS (`read_sas`) files, among others.

7.  For Excel, there are capabilities to read an Excel file (see the
    `read_excel` function in Pandas), but you can also
    just go into Excel and export as a CSV file or the like and then
    read that into Python. In general, it's best not to pass around data
    files as Excel or other spreadsheet format files because (1) Excel
    is proprietary, so someone may not have Excel and the format is
    subject to change, (2) Excel imposes limits on the number of
    rows, (3) one can easily manipulate text files such as CSV using
    UNIX tools, but this is not possible with an Excel file, (4) Excel
    files often have more than one sheet, graphs, macros, etc., so
    they're not a data storage format per se.

8.  Python can easily interact with databases (SQLite, PostgreSQL, MySQL,
    Oracle, etc.), querying the database using SQL and returning results
    to Python. More in the big data unit and in the large datasets tutorial
    mentioned above.

## CSV vs. specialized formats such as Parquet

CSV is a common format (particularly in some disciplines/contexts) and has the advantages of being simple to understand, human readable, and readily manipulable by line-based processing tools such as shell commands. However, it has various disadvantages:

  - storage is by row, which will often mix values of different types;
  - extra space is taken up by explicitly storing commas and newlines; and
  - one must search through the document to find a given row or value -- e.g., to find the 10th row, we must search for the 9th newline and then read until the 10th newline.

A popular file format that has some advantages over plain text formats such as CSV is [Parquet](https://parquet.apache.org/docs/overview/motivation/). The storage is by column (actually in chunks of columns). This works well with how datasets are often structured in that a given field/variable will generally have values of all the same type and there may be many repeated values, so there are opportunities for efficient storage including compression. Storage by column also allows retrieval only of the columns that a user needs. As a result data stored in the Parquet format often takes up much less space than stored as CSV and can be queried much faster. Also note that data stored in Parquet will often be stored as multiple files.

Here's a brief exploration using a data file not in the class repository.

```python
import time

## Read from CSV
t0 = time.time()
data_from_csv = pd.read_csv(os.path.join('..', 'data', 'airline.csv'))
print(time.time() - t0)
```

```python
## Write out Parquet-formatted data
data_from_csv.to_parquet(os.path.join('..', 'data', 'airline.parquet'))

## Read from Parquet
t0 = time.time()
data_from_parquet = pd.read_parquet(os.path.join(
                                    '..', 'data', 'airline.parquet'))
print(time.time() - t0)
```

The CSV file is 51 MB while the Parquet file is 8 MB.

```python
import subprocess
subprocess.run(["ls", "-l", os.path.join("..", "data", "airline.csv")])
subprocess.run(["ls", "-l", os.path.join("..", "data", "airline.parquet")])
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Reading data from text files into Python →](03-2-reading-data-from-text-files-into-python.md)
