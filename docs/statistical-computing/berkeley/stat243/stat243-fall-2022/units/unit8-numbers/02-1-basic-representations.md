---
title: 1. Basic representations
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit8-numbers.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Basic representations

**Source:** [`units/unit8-numbers.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Everything in computer memory or on disk is stored in terms of bits. A
*bit* is essentially a switch than can be either on or off. Thus
everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make
up a *byte*. For information stored as plain text (ASCII), each byte is
used to encode a single character (as previously discussed, actually only 7 of the 8 bits are
actually used, hence there are $2^{7}=128$ ASCII characters). One way to
represent a byte is to write it in hexadecimal, rather than as 8 0/1
bits. Since there are $2^{8}=256$ possible values in a byte, we can
represent it more compactly as 2 base-16 numbers, such as "3e" or "a0"
or "ba". A file format is nothing more than a way of interpreting the
bytes in a file.

Here we'll use the *bits* function from *pryr* to look
at the underlying binary representation. Note that 'b' is encoded as 1
more than 'a', and similarly for '0', '1', and '2'.


```r
library(pryr)
bits('a')
bits('b')

bits('0')
bits('1')
bits('2')

bits('@')
```


We can think about how we'd store an integer in terms of bytes. With two
bytes (16 bits), we could encode any value from $0,\ldots,2^{16}-1=65535$. This is
an *unsigned* integer representation. To store negative numbers as well,
we can use one bit for the sign, giving us the ability to encode
-32767 - 32767 ($\pm2^{15}-1$).

R actually uses 4 bytes per integer, so it can encode -2147483647 -
2147483647 ($\pm2^{31}-1$). Note that in general, rather than be stored
simply as the sign and then a number in base 2, integers (at least the
negative ones) are actually stored in different binary encoding to
facilitate arithmetic. Here we use the "L" to force R to store the
number as an integer. More on that later in the Unit.


```r
library(pryr)
bits(0L)
bytes(0L)

bits(1L)
bytes(1L)

bits(2L)
bytes(2L)

bits(-1L)
bytes(-1L)
```

What do I mean about facilitating arithmetic? As an example, consider adding
the binary representations of -1 and 1 above. Nice, right?


Finally note that the set of computer integers is not closed under
arithmetic, with R reporting an overflow (i.e., a result that is too
large to be stored as an integer using 4 bytes):


```r
a <- as.integer(3423333)  # 3423333L
a * a
```


Real numbers (or *floating points*) use a minimum of 4 bytes, for single
precision floating points. (GPU calculations often use single precision.)
In general (including in R) 8 bytes are used to represent real
numbers on a computer and these are called *double precision floating
points* or *doubles*. Let's see some examples in R of how much space
different types of variables take up.

Let's see how this plays out in terms of memory use in R.


```r
doubleVec <- rnorm(100000)
intVec <- 1:100000
object.size(doubleVec)
object.size(intVec) # so how many bytes per integer in R?
```


We can easily calculate the number of megabytes (MB) a vector of
floating points (in double precision) will use as the number of elements
times 8 (bytes/double) divided by $10^{6}$ to convert from bytes to
megabytes. (In some cases when considering computer memory, a megabyte
is $1,048,576=2^{20}=1024^{2}$ bytes (this is formally called a
*mebibyte*) so slightly different than $10^{6}$ -- see [here for more
details](https://en.wikipedia.org/wiki/Megabyte)). Finally, R has a
special object that tells us about the characteristics of computer
numbers on the machine that R is running on called *.Machine.* For
example, `.Machine\$integer.max` is $2147483647=2^{31}-1$, which
confirms how many bytes R is using for each integer (and that R is using
a bit for the sign of the integer). Since we have both negative and
positive numbers, we have $2\cdot2^{31}=2^{32}=(2^{8})^{4}$, i.e., 4
bytes, with each byte having 8 bits.


```r
bits(.Machine$integer.max)
bits(-.Machine$integer.max)
bits(-1L)
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Floating point basics →](03-2-floating-point-basics.md)
