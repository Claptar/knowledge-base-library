---
title: 5. File and string encodings
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. File and string encodings

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Text (either in the form of a file with regular language in it or a data
file with fields of character strings) will often contain characters
that are not part of the [limited ASCII set of
characters](http://en.wikipedia.org/wiki/ASCII), which has $2^{7}=128$
characters and control codes; basically what you see on a standard US
keyboard. Each character takes up one byte (8 bits) of space (there is
an unused bit that comes in handy in the UTF-8 context). We can actually
hand-generate an ASCII file using the binary representation of each
character in Python as an illustration.

The letter "M" is encoded based on the ASCII standard in bits as
"01001101" as seen in the link above. For convenience, this is often
written as two base-16 numbers (i.e., hexadecimal), where "0100"="4" and
"1101"="d", hence we have "4d" in hexadecimal.

```python
## 4d in hexadecimal is 'M'
## 0a is a newline (at least in Linux/Mac)
hexvals = b'\x4d\x6f\x6d\x0a'  # "Mom\n" in ASCII as hexadecimal

with open('tmp.txt', 'wb') as textfile:
     nbytes = textfile.write(hexvals)

nbytes

subprocess.run(["ls", "-l", "tmp.txt"], capture_output=True).stdout

with open('tmp.txt', 'r') as textfile:
     line = textfile.readlines()

line
```


When encountering non-ASCII files, in some cases you may need to deal
with the text encoding (the mapping of individual characters (including
tabs, returns, etc.) to a set of numeric codes). There are a variety of
different encodings for text files, with different ones common on
different operating systems.

We'll focus on the most common and universal approach, using [Unicode](https://en.wikipedia.org/wiki/UTF-8) as the
numeric codes for characters/symbols and [UTF-8](https://en.wikipedia.org/wiki/UTF-8) as the encoding to bytes.

Unicode includes includes more than 110,000 characters from 100
different alphabets/scripts. It's widely used on the web. One alternative that is sometimes seen is Latin-1,
which encodes a small subset of Unicode and contains the characters used in
many European languages (e.g., letters with accents).

Unicode characters have unique integer identifiers (the unicode *code
point*), which is given by `ord` in Python. UTF-8 is the encoding
that represents each Unicode character in actual bytes (in memory or on disk).

Here's an example of using non-ASCII Unicode characters.
We can verify [online the representation of ñ](https://www.ascii-code.com/character/%C3%B1).

```python
## Python `str` type stores Unicode characters.
x2_unicode = 'Pe\u00f1a 3\u00f72'
x2_unicode
type(x2_unicode)

## From Unicode code point to hexadecimal representation of the code point:
ord('ñ')
hex(ord('ñ'))

## And now to the actual UTF-8 encoding, again in hexadecimal:
bytes('\u00f1', 'utf-8')    # indeed - two bytes, not one
bytes('\u00f7', 'utf-8')    # indeed - two bytes, not one
## specified directly as hexadecimal in UTF-8 encoding
x2_utf8 = b'Pe\xc3\xb1a 3\xc3\xb72'
x2_utf8

with open('tmp2.txt', 'wb') as textfile:
     nbytes = textfile.write(x2_utf8)
```

Now in the shell, let's check it.

```bash
## Here n-tilde and division symbol take up two bytes
ls -l tmp2.txt
```
```bash
## The shell knows how to interpret the UTF-8 encoded file
## and represent the Unicode character on the screen:
cat tmp2.txt
```

UTF-8 is cleverly designed in terms of the bit-wise representation of
characters such that ASCII characters still take up one byte, and most
other characters take two bytes, but some take four bytes. In fact it is
even more clever than that - the representation is such that the bits of
a one-byte character never appear within the representation of a two-
or three- or four-byte character (and similarly for two-byte characters
in three- or four-byte characters, etc.). And from the initial bit or bits,
one can determine how many bytes are used for the character. For example if
the first bit is a zero, it's clear that the character is an ASCII character
using only one byte. If it starts with a one, then one needs to look at the
next bit(s) to determine if the character takes up 2, 3, or 4 bytes.

The UNIX utility `file`, e.g. `file tmp.txt` can help provide some
information.

Various Python functions such as `readlines` allow
 one to specify the encoding as one reads text in.
The UNIX utility `iconv` and the Python function `encode` can help with
conversions.

The default encoding in Python is UTF-8; note below that
various types of information are interpreted in US English with the
encoding UTF-8:

```python
import locale
locale.getlocale()
```

Note that in Python and various other languages (including R and Julia), you
can use Unicode characters as part of variable names:

```python
peña = 7
print(peña)
σ = 4   # \sigma = 4 (the sigma doesn't show up in the PDF version of this document)
σ * peña
```


With strings already in Python, you can convert between encodings with
the `encode` method for string objects:

```python
text = 'Pe\u00f1a 3\u00f72'
text
text.encode('utf-8')
```
```python
text.encode('latin1')
```
```python
try:
    text.encode('ascii')
except Exception as error:
    print(error)
```

The results above show that the two non-ASCII characters we had been
working with, which required two bytes in UTF-8, require only one
byte in the Latin1 (ISO 8859-1) encoding, which provides 191 characters that
include ASCII characters and various characters (mostly letters with
accents) used in European languages.


An error message about decoding/invalid bytes in the message often indicates
an encoding issue. In particular errors may arise when trying to do
read or manipulate strings in Python for which the encoding is
not properly set. Here's an example with some Internet logging data that
we used a few years ago in class in a problem set and which caused some
problems.

```python
#| error: true
with open('file_nonascii.txt', 'r') as textfile:
    lines = textfile.readlines()
```

If we specify the file is encoded with Latin1, it works.

```python
with open('file_nonascii.txt', 'r', encoding = 'latin1') as textfile:
    lines = textfile.readlines()

## Note the non-ASCII (Latin-1) character (the upside-down question mark)
lines[16925]
```

---

[← Check the results.](17-check-the-results.md) · [Up: contents](index.md) · [6. Data structures →](19-6-data-structures.md)
