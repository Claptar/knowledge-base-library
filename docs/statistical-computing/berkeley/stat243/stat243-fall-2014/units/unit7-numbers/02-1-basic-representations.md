---
title: 1 Basic representations
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Basic representations

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Everything in computer memory or on disk is stored in terms of bits. A _bit_ is essentially a switch than can be either on or off. Thus everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make up a _byte_ . For information stored as plain text (ASCII), each byte is used to encode a single character (actually 7 bits are used, hence there are 2<sup>7</sup> = 128 ASCII characters). One way to represent a byte is to write it in hexadecimal, rather than as 8 0/1 bits. Since there are 2<sup>8</sup> = 256 possible values in a byte, we can represent it more compactly as 2 base-16 numbers, such as “3e” or “a0” or “ba”. A file format is nothing more than a way of interpreting the bytes in a file.

We can think about how we’d store an integer in terms of bytes. With two bytes, we could encode any value from 0 _, . . . ,_ 2<sup>16</sup> _−_ 1 = 65535. This is an unsigned integer representation. To store negative numbers as well, we can use one bit for the sign, giving us the ability to encode -32767 - 32767 ( _±_ 2<sup>15</sup> _−_ 1). Note that in general, rather than be stored simply as the sign and then a number in base 2, integers are actually stored in a different binary encoding to facilitate arithmetic. Finally note that the set of computer integers is not closed under arithmetic, with R reporting an overflow (i.e., a result that is too large to be stored as an integer):

1

a <- **as.integer** (3423333) _# 3423333L_ a * a ## Warning: NAs produced by integer overflow ## [1] NA

Real numbers (or _floating points_ ) use a minimum of 4 bytes, for single precision floating points. In general 8 bytes are used to represent real numbers on a computer and these are called _double precision floating points_ or _doubles_ . Let’s see some examples in R of how much space different types of variables take up.

Let’s see how this plays out in terms of memory use in R.

doubleVec <- **rnorm** (1e+05) intVec <- 1:1e+05 **set.seed** (0) charVec <- **sample** (letters, 1e+05, replace = TRUE) **object.size** (doubleVec) ## 800040 bytes **object.size** (intVec) _# so how many bytes per integer in R?_ ## 400040 bytes **object.size** (charVec) ## 801288 bytes **.Internal** ( **inspect** (charVec)) _# anything jump out at you?_ ## @3b17c10 16 STRSXP g0c7 [MARK,NAM(2)] (len=100000, tl=0) ## @e5f9a8 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "x" ## @13db578 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "g" ## @135b9f8 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "j" ## @1248948 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "o" ## @e5f9a8 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "x" ## ...

2

We can easily calculate the number of megabytes (Mb) a vector of floating points (in double precision) will use as the number of elements times 8 (bytes/double) divided by 10<sup>6</sup> to convert from bytes to megabytes. (In some cases when considering computer memory, a megabyte is 1 _,_ 048 _,_ 576 = 2<sup>20</sup> = 1024<sup>2</sup> bytes so slightly different than 10<sup>6</sup> ). Finally, R has a special object that tells us about the characteristics of computer numbers on the machine that R is running on called _.Machine._ For example, _.Machine$integer.max_ is 2147483647 = 2<sup>31</sup> _−_ 1, which confirms how many bytes R is using for each integer (and that R is using a bit for the sign of the integer). We have 2 _·_ 2<sup>31</sup> = 2<sup>32</sup> = (2<sup>8</sup> )<sup>4</sup> , i.e., 4 bytes, with each byte having 8 bits.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Floating point basics →](03-2-floating-point-basics.md)
