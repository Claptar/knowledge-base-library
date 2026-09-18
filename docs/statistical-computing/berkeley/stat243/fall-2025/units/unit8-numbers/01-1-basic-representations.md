---
title: 1. Basic representations
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit8-numbers.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1. Basic representations

```r
#| echo: false
reticulate::use_python('/usr/local/linux/miniforge-3.13/bin/python')
```

```python
#| echo: false
import numpy as np
import scipy.linalg
import sys
```

## Overview

References:

-   Gentle, Computational Statistics, Chapter 2.
-   [http://www.lahey.com/float.htm](http://www.lahey.com/float.htm)
-   And for more gory detail, see Monahan, Chapter 2.

A quick note that, as we've already seen, Python's version of scientific
notation is `XeY`, which means $X\cdot10^{Y}$.

A second note is that the concepts developed here apply outside of Python,
but we'll illustrate the principles of computer numbers using Python.
Python usually makes use of the *double* type (8 bytes) in C for the underlying
representation of real-valued numbers in C variables, so what we'll really be
seeing is how such types behave in C on most modern machines.
It's actually a bit more complicated in that one can use real-valued numbers
that use something other than 8 bytes in numpy by specifying a `dtype`.

The handling of integers is even more complicated. In numpy, the default
is 8 byte integers, but other integer dtypes are available. And in Python
itself, integers can be arbitrarily large.

Everything in computer memory or on disk is stored in terms of bits. A
*bit* is essentially a switch than can be either on or off. Thus
everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make
up a *byte*. As discussed in Unit 2, for information stored as plain text (ASCII), each byte is
used to encode a single character (as previously discussed, actually only 7 of the 8 bits are
actually used, hence there are $2^{7}=128$ ASCII characters). One way to
represent a byte is to write it in hexadecimal, rather than as 8 0/1
bits. Since there are $2^{8}=256$ possible values in a byte, we can
represent it more compactly as 2 base-16 numbers, such as "3e" or "a0"
or "ba". A file format is nothing more than a way of interpreting the
bytes in a file.

We'll create some helper functions to all us to look
at the underlying binary representation.

```python
from bitstring import Bits

def bits(x, type='float', len=64):
    if type == 'float':
        obj = Bits(float = x, length = len)
    elif type == 'int':
        obj = Bits(int = x, length = len)
    else:
        return None
    return(obj.bin)

def dg(x, form = '.20f'):
    print(format(x, form))
```

Note that 'b' is encoded as one
more than 'a', and similarly for '0', '1', and '2'.
We could check these against, say, the Wikipedia
table that shows the [ASCII encoding](https://en.wikipedia.org/wiki/ASCII).

```python
Bits(bytes=b'a').bin
Bits(bytes=b'b').bin

Bits(bytes=b'0').bin
Bits(bytes=b'1').bin
Bits(bytes=b'2').bin

Bits(bytes=b'@').bin
```

We can think about how we'd store an integer in terms of bytes. With two
bytes (16 bits), we could encode any value from $0,\ldots,2^{16}-1=65535$. This is
an *unsigned* integer representation. To store negative numbers as well,
we can use one bit for the sign, giving us the ability to encode
-32767 - 32767 ($\pm2^{15}-1$).

Note that in general, rather than be stored
simply as the sign and then a number in base 2, integers (at least the
negative ones) are actually stored in different binary encoding to
facilitate arithmetic.

Here's what a 64-bit integer representation
the actual bits.

```python
np.binary_repr(0, width=64)
np.binary_repr(1, width=64)
np.binary_repr(2, width=64)

np.binary_repr(-1, width=64)
```

What do I mean about facilitating arithmetic? As an example, consider adding
the binary representations of -1 and 1. Nice, right?

Finally note that the set of computer integers is not closed under
arithmetic. We get an overflow (i.e., a result that is too
large to be stored as an integer of the particular length):

```python
#| error: true
a = np.int32(3423333)
a * a       # overflows
```

```python
a = np.int64(3423333)
a * a       # doesn't overflow if we use 64 bit int
```

This is disconcerting behavior with numpy...:

```python
a = np.int64(34233332342343)
a * a

a=np.int64(10000000000)
a *a

a = 34233332342343
a * a
```

That said, if we use Python's `int` rather than numpy's integers,
we don't get overflow. But we do use more than 8 bytes that would be used
by numpy. And if we use Python `int` or lists of such values, we're not
set up for efficient array-based computation.

```python
a = 34233332342343
a * a
sys.getsizeof(a)
sys.getsizeof(a*a)
```

In C, one generally works with 8 byte real-valued numbers (aka *floating point* numbers or *floats*).
However, many years ago, an initial standard representation used 4 bytes. Then
people started using 8 bytes, which became known as *double precision floating points*
or *doubles*, whereas the 4-byte version became known as *single precision*.
Now with GPUs, single precision is often used for speed and reduced memory use.

Let's see how this plays out in terms of memory use in Python.

```python
x = np.random.normal(size = 100000)
sys.getsizeof(x)
x = np.array(np.random.normal(size = 100000), dtype = "float32")
sys.getsizeof(x)
x = np.array(np.random.normal(size = 100000), dtype = "float16")
sys.getsizeof(x)
```

We can easily calculate the number of megabytes (MB) a vector of
floating points (in double precision) will use as the number of elements
times 8 (bytes/double) divided by $10^{6}$ to convert from bytes to
megabytes. (In some cases when considering computer memory, people use
mebibyte (MiB), which is $1,048,576=2^{20}=1024^{2}$ bytes (so slightly different than $10^{6}$), and call that a
megabyte  -- see [here for more
details](https://en.wikipedia.org/wiki/Megabyte)).

Finally, `numpy` has some helper functions that can tell us
about the characteristics of computer
numbers on the machine that Python is running.

```python
#| error: true
np.iinfo(np.int32)
np.iinfo(np.int64)

np.binary_repr(2147483647, width=32)
np.binary_repr(-2147483648, width=32)
np.binary_repr(2147483648, width=32)  # strange
np.int32(2147483648)
np.binary_repr(1, width=32)
np.binary_repr(-1, width=32)
```

So the max for a 32-bit (4-byte) integer is $2147483647=2^{31}-1$, which
is consistent with 4 bytes.  Since we have both negative and
positive numbers, we have $2\cdot2^{31}=2^{32}=(2^{8})^{4}$, i.e., 4
bytes, with each byte having 8 bits.

---

[Up: contents](index.md) · [2. Floating point basics →](02-2-floating-point-basics.md)
