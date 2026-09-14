---
title: 1. Basic representations
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit8-numbers.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Basic representations

**Source:** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit8-numbers.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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

def bits(x):
    obj = Bits(float = x, length = 64)
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
a = np.int32(3423333)
a * a       # overflows

a = np.int64(3423333)
a * a       # doesn't overflow if we use 64 bit int

a = np.int64(34233332342343)
a * a
```

That said, if we use Python's `int` rather than numpy's integers,
we don't get overflow. But we do use more than 8 bytes that would be used
by numpy.

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
megabytes. (In some cases when considering computer memory, a megabyte
is $1,048,576=2^{20}=1024^{2}$ bytes (this is formally called a
*mebibyte*) so slightly different than $10^{6}$ -- see [here for more
details](https://en.wikipedia.org/wiki/Megabyte)).

Finally, `numpy` has some helper functions that can tell us
about the characteristics of computer
numbers on the machine that Python is running.


```python
np.iinfo(np.int32)
np.iinfo(np.int64)

np.binary_repr(2147483647, width=32)
np.binary_repr(-2147483648, width=32)
np.binary_repr(2147483648, width=32)  # strange
np.binary_repr(1, width=32)
np.binary_repr(-1, width=32)
```

So the max for a 32-bit (4-byte) integer is $2147483647=2^{31}-1$, which
is consistent with 4 bytes.  Since we have both negative and
positive numbers, we have $2\cdot2^{31}=2^{32}=(2^{8})^{4}$, i.e., 4
bytes, with each byte having 8 bits.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Floating point basics →](03-2-floating-point-basics.md)
