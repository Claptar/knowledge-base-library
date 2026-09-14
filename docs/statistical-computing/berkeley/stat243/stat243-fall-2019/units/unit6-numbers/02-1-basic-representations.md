---
title: 1 Basic representations
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Basic representations

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Everything in computer memory or on disk is stored in terms of bits. A _bit_ is essentially a switch than can be either on or off. Thus everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make up a _byte_ . For information stored as plain text (ASCII), each byte is used to encode a single character (actually only 7 of the 8 bits are actually used, hence there are 2<sup>7</sup> = 128 ASCII characters). One way to represent a byte is to write it in hexadecimal, rather than as 8 0/1 bits. Since there are 2<sup>8</sup> = 256 possible values in a byte, we can represent it more compactly as 2 base16 numbers, such as “3e” or “a0” or “ba”. A file format is nothing more than a way of interpreting the bytes in a file. Here we’ll use the _bits_ function from _pryr_ to look at the underlying binary representation. Note that ’b’ is encoded as 1 more than ’a’, and similarly for ’0’, ’1’, and ’2’.

1

**library** (pryr) **bits** ('a') ## [1] "01100001" **bits** ('b') ## [1] "01100010" **bits** ('0') ## [1] "00110000" **bits** ('1') ## [1] "00110001" **bits** ('2') ## [1] "00110010" **bits** ('@') ## [1] "01000000"

We can think about how we’d store an integer in terms of bytes. With two bytes, we could encode any value from 0 _, . . . ,_ 2<sup>16</sup> _−_ 1 = 65535. This is an unsigned integer representation. To store negative numbers as well, we can use one bit for the sign, giving us the ability to encode -32767 - 32767 ( _±_ 2<sup>15</sup> _−_ 1).

R actually uses 4 bytes per integer, so it can encode -2147483647 - 2147483647 ( _±_ 2<sup>31</sup> _−_ 1). Note that in general, rather than be stored simply as the sign and then a number in base 2, integers are actually stored in a different binary encoding to facilitate arithmetic.

**library** (pryr) **bits** (0)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[1] "00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000" bytes (0) →](03-1-00000000-00000000-00000000-00000000-00000000-00000000-0000.md)
