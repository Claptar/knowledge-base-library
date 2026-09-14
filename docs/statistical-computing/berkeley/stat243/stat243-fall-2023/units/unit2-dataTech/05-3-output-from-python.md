---
title: 3. Output from Python
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Output from Python

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

## Writing output to files

Functions for text output are generally analogous to those for input.

```python
#| eval: false
file_path = os.path.join('/tmp', 'tmp.txt')
with open(file_path, 'w') as file:
     file.writelines(lines)
```

We can also use `file.write()` to write individual strings.

In Pandas, we can use `DataFrame.to_csv` and `DataFrame.to_parquet`.

We can use the `json.dump` function to output appropriate data objects
(e.g., dictionaries or possibly lists) as JSON. One
use of JSON as output from Python would be to 'serialize' the information in
an Python object such that it could be read into another program.

And of course you can always save to a Pickle data file (a binary file format) using
`pickle.dump()` and `pickle.load()` from the `pickle` package.
Happily this is platform-independent so can be used to transfer
Python objects between different OS.


## Formatting output

We can use [string formatting](https://docs.python.org/3/library/string.html#formatstrings) to control how output is printed to the screen.

The mini-language involved in the format specification can get fairly involved,
but a few basic pieces of syntax can do most of what one generally needs to do.

We can format numbers to chosen number of digits and decimal places
and handle alignment, using the `format` method of the string class.

For example:

```python
'{:>10}'.format(3.5)    # right-aligned, using 10 characters
'{:.10f}'.format(1/3)   # force 10 decimal places
'{:15.10f}'.format(1/3) # force 15 characters, with 10 decimal places
format(1/3, '15.10f') # alternative using a function
```

We can also "interpolate" variables into strings.

```python
"The number pi is {}.".format(np.pi)
"The number pi is {:.5f}.".format(np.pi)
"The number pi is {:.12f}.".format(np.pi)
```

```python
val1 = 1.5
val2 = 2.5

---

[← output is a sequence of bytes.](04-output-is-a-sequence-of-bytes.md) · [Up: contents](index.md) · [As of Python 3.6, put the variable names in directly. →](06-as-of-python-3-6-put-the-variable-names-in-directly.md)
