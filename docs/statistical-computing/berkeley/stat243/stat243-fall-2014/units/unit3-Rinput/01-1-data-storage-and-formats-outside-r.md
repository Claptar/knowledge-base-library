---
title: 1 Data storage and formats (outside R)
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Data storage and formats (outside R)

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

At this point, we’re going to turn to reading data into R and manipulating text, including regular expressions. We’ll focus on doing these manipulations in R, but the concepts involved in reading in data, database manipulations, and regular expressions are common to other languages, so familarity with these in R should allow you to pick up other tools more easily. The main downside to working with datasets in R is that the entire dataset resides in memory, so R is not so good for dealing with very large datasets. More on alternatives in a bit. Another common frustration is controlling how the variables are interpreted (numeric, character, factor) when reading data into a data frame.

R has the capability to read in a wide variety of file formats. Let’s get a feel for some of the common ones.

1. Flat text files (ASCII files): data are often provided as simple text files. Often one has one record or observation per row and each column or field is a different variable or type of information about the record. Such files can either have a fixed number of characters in each field (fixed width format) or a special character (a delimiter) that separates the fields in each

1

row. Common delimiters are tabs, commas, one or more spaces, and the pipe (|). Common file extensions are _.txt_ and _.csv_ . Metadata (information about the data) is often stored in a separate file. I like CSV files but if you have files where the data contain commas, other delimiters can be good. Text can be put in quotes in CSV files. This was difficult to deal with in the shell in PS1, but _read.table()_ in R handles this situation.

- (a) One occasionally tricky difficulty is as follows. If you have a text file created in Windows, the line endings are coded differently than in UNIX (a newline (the ASCII character _\n_ ) and a carriage return (the ASCII character _\r_ ) in Windows vs. only a newline in UNIX). There are UNIX utilities ( _fromdos_ in Ubuntu, including the SCF Linux machines and _dos2unix_ in other Linux distributions) that can do the necessary conversion. If you see _^M_ at the end of the lines in a file, that’s the tool you need. Alternatively, if you open a UNIX file in Windows, it may treat all the lines as a single line. You can fix this with _todos_ or _unix2dos_ .

As a side note, Macs have line endings as in UNIX, but before Mac OS X, lines ended only in a carriage return. There is a UNIX utility call _mac2unix_ that can convert such text files.

2. In some contexts, such as textual data and bioinformatics data, the data may in a text file with one piece of information per row, but without meaningful columns/fields.

3. In scientific contexts, netCDF ( _.nc_ ) (and the related HDF5) are popular format for gridded data that allows for highly-efficient storage and contains the metadata within the file. The basic structure of a netCDF file is that each variable is an array with multiple dimensions (e.g., latitude, longitude, and time), and one can also extract the values of and metadata about each dimension. The _ncdf4_ package in R nicely handles working with netCDF files. These are examples of a binary format, which is not (easily) human readable but can be more space-efficient and faster to work with (because they can allow random access into the data rather than requiring sequential reading).

4. Data may also be in the form of XML or HTML files. The XML package is useful for reading and writing from these formats.

5. Data may already be in a database or in the data storage of another statistical package ( _Stata_ , _SAS_ , _SPSS_ , etc.). The _foreign_ package in R has excellent capabilities for importing Stata ( _read.dta()_ ), SPSS ( _read.spss()_ ), SAS ( _read.ssd()_ and, for XPORT files, _read.xport()_ ), and dbf (a common database format) ( _read.dbf()_ ), among others.

2

6. For Excel, there are capabilities to read an Excel file (see the _XLConnect_ package among others), but you can also just go into Excel and export as a CSV file or the like and then read that into R. In general, it’s best not to pass around data files as Excel or other spreadsheet format files because (1) Excel is proprietary, so someone may not have Excel and the format is subject to change, (2) Excel imposes limits on the number of rows, (3) one can easily manipulate text files such as CSV using UNIX tools, but this is not possible with an Excel file, (4) Excel files often have more than one sheet, graphs, macros, etc., so they’re not a data storage format per se.

---

[Up: contents](index.md) · [2 Reading data from text files into R →](02-2-reading-data-from-text-files-into-r.md)
