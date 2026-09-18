---
title: 3. Output from Python
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3. Output from Python

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
This also feels like something an AI coding assistant could do well, though
I haven't specifically tried.

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
val1 = 1.5
val2 = 2.5
# This works as of Python 3.6.
print(f"Let's add {val1} and {val2}.")
num1 = 1/3
print("Let's add the %s numbers %.5f and %15.7f."
       %('floating point', num1 ,32+1/7))
```

Or to insert into a file:
```python
#| eval: false
file_path = os.path.join('/tmp', 'tmp.txt')
with open(file_path, 'a') as file:
     file.write("Let's add the %s numbers %.5f and %15.7f."
                %('floating point', num1 ,32+1/7))

```

`round` is another option, but it's often better to directly control the printing format.

---

[← 2. Reading data from text files into Python](03-2-reading-data-from-text-files-into-python.md) · [Up: contents](index.md) · [4. Working with information on the web →](05-4-working-with-information-on-the-web.md)
