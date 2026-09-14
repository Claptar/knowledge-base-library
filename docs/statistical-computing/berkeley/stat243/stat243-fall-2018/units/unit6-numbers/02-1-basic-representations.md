---
title: 1 Basic representations
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Basic representations

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Everything in computer memory or on disk is stored in terms of bits. A _bit_ is essentially a switch than can be either on or off. Thus everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make up a _byte_ . For information stored as plain text (ASCII), each byte is used to encode a single character (actually 7 bits are used, hence there are 2<sup>7</sup> = 128 ASCII characters). One way to represent a byte is to write it in hexadecimal, rather than as 8 0/1 bits. Since there are 2<sup>8</sup> = 256 possible values in a byte, we can represent it more compactly as 2 base-16 numbers, such as “3e” or “a0” or “ba”. A file format is nothing more than a way of interpreting the bytes in a file. Here we’ll use the _bits_ function from _pryr_ to look at the underlying binary representation. From this it’s not clear if the character is being stored in 7 or 8 bits.

1

**library** (pryr) **bits** ('a') ## [1] "01100001" **bits** ('b') ## [1] "01100010" **bits** ('0') ## [1] "00110000" **bits** ('1') ## [1] "00110001" **bits** ('2') ## [1] "00110010" **bits** ('@') ## [1] "01000000"

We can think about how we’d store an integer in terms of bytes. With two bytes, we could encode any value from 0 _, . . . ,_ 2<sup>16</sup> _−_ 1 = 65535. This is an unsigned integer representation. To store negative numbers as well, we can use one bit for the sign, giving us the ability to encode -32767 - 32767 ( _±_ 2<sup>15</sup> _−_ 1). Note that in general, rather than be stored simply as the sign and then a number in base 2, integers are actually stored in a different binary encoding to facilitate arithmetic.

**library** (pryr) **bits** (0)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 03 — →](03-unit-06-numbers-part-03.md)
