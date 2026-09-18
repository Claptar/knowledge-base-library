---
title: 'Unit 6: Computer numbers'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Unit 6: Computer numbers

October 9, 2021

References:

- Gentle, Computational Statistics, Chapter 2.
- http://www.lahey.com/float.htm
- And for more gory detail, see Monahan, Chapter 2.

A quick note that, as we've already seen, R's version of scientific notation is XeY, which means $X \cdot 10^Y$.

A second note is that the concepts developed here apply outside of R, but we'll illustrate the principles of computer numbers using R. R makes use of the *double* and *int* types in C for the underlying representation of R's numbers in C variables, so what we'll really be seeing is how such types behave in C on most modern machines.

## 1 Basic representations

Everything in computer memory or on disk is stored in terms of bits. A *bit* is essentially a switch than can be either on or off. Thus everything is encoded as numbers in base 2, i.e., 0s and 1s. 8 bits make up a *byte*. For information stored as plain text (ASCII), each byte is used to encode a single character (actually only 7 of the 8 bits are actually used, hence there are $2^7 = 128$ ASCII characters). One way to represent a byte is to write it in hexadecimal, rather than as 8 0/1 bits. Since there are $2^8 = 256$ possible values in a byte, we can represent it more compactly as 2 base-16 numbers, such as "3e" or "a0" or "ba". A file format is nothing more than a way of interpreting the bytes in a file. Here we'll use the `bits` function from `pryr` to look at the underlying binary representation. Note that 'b' is encoded as 1 more than 'a', and similarly for '0', '1', and '2'.

```r
library(pryr)
bits('a')
## [1] "01100001"
bits('b')
## [1] "01100010"
bits('0')
## [1] "00110000"
bits('1')
## [1] "00110001"
bits('2')
## [1] "00110010"
bits('@')
## [1] "01000000"
```

We can think about how we'd store an integer in terms of bytes. With two bytes, we could encode any value from $0, \dots, 2^{16} - 1 = 65535$. This is an unsigned integer representation. To store negative numbers as well, we can use one bit for the sign, giving us the ability to encode -32767 - 32767 ($\pm 2^{15} - 1$).

R actually uses 4 bytes per integer, so it can encode -2147483647 - 2147483647 ($\pm 2^{31} - 1$). Note that in general, rather than be stored simply as the sign and then a number in base 2, integers (at least the negative ones) are actually stored in different binary encoding to facilitate arithmetic. Here we use the "L" to force R to store the number as an integer. More on that later in the Unit.

```r
library(pryr)
bits(0L)
## [1] "00000000 00000000 00000000 00000000"
bytes(0L)
## [1] "00 00 00 00"
bits(1L)
## [1] "00000000 00000000 00000000 00000001"
bytes(1L)
## [1] "00 00 00 01"
bits(2L)
## [1] "00000000 00000000 00000000 00000010"
bytes(2L)
## [1] "00 00 00 02"
bits(-1L)
## [1] "11111111 11111111 11111111 11111111"
bytes(-1L)
## [1] "FF FF FF FF"
```

Finally note that the set of computer integers is not closed under arithmetic, with R reporting an overflow (i.e., a result that is too large to be stored as an integer):

```r
a <- as.integer(3423333) # 3423333L
a * a
## Warning in a * a: NAs produced by integer overflow
## [1] NA
```

Real numbers (or *floating points*) use a minimum of 4 bytes, for single precision floating points. In general 8 bytes are used to represent real numbers on a computer and these are called *double precision floating points* or *doubles*. Let's see some examples in R of how much space different types of variables take up.

Let's see how this plays out in terms of memory use in R.

```r
doubleVec <- rnorm(100000)
intVec <- 1:100000
set.seed(1)
charVec <- sample(letters, 100000, replace = TRUE)
object.size(doubleVec)
## 800048 bytes
object.size(intVec) # so how many bytes per integer in R?
## 400048 bytes
object.size(charVec)
## 801504 bytes
charVec[1:5] <- c('a','a','b','b','c')
.Internal(inspect(charVec)) # anything jump out at you?
## @55be592eb670 16 STRSXP g0c7 [REF(1)] (len=100000, tl=0)
##   @55be52ee84a8 09 CHARSXP g1c1 [MARK,REF(3872),gp=0x61] [ASCII] [cached] "a"
##   @55be52ee84a8 09 CHARSXP g1c1 [MARK,REF(3872),gp=0x61] [ASCII] [cached] "a"
##   @55be531fe650 09 CHARSXP g1c1 [MARK,REF(3907),gp=0x61] [ASCII] [cached] "b"
##   @55be531fe650 09 CHARSXP g1c1 [MARK,REF(3907),gp=0x61] [ASCII] [cached] "b"
##   @55be52c06cc0 09 CHARSXP g1c1 [MARK,REF(4259),gp=0x61] [ASCII] [cached] "c"
## ...
```

We can easily calculate the number of megabytes (MB) a vector of floating points (in double precision) will use as the number of elements times 8 (bytes/double) divided by $10^6$ to convert from bytes to megabytes. (In some cases when considering computer memory, a megabyte is $1,048,576 = 2^{20} = 1024^2$ bytes (this is formally called a mebibyte) so slightly different than $10^6$ -- see here for more details). Finally, R has a special object that tells us about the characteristics of computer numbers on the machine that R is running on called `.Machine`. For example, `.Machine$integer.max` is $2147483647 = 2^{31} - 1$, which confirms how many bytes R is using for each integer (and that R is using a bit for the sign of the integer). Since we have both negative and positive numbers, we have $2 \cdot 2^{31} = 2^{32} = (2^8)^4$, i.e., 4 bytes, with each byte having 8 bits.

```r
bits(.Machine$integer.max)
## [1] "01111111 11111111 11111111 11111111"
bits(-.Machine$integer.max)
## [1] "10000000 00000000 00000000 00000001"
bits(-1L)
## [1] "11111111 11111111 11111111 11111111"
```

## 2 Floating point basics

### 2.1 Representing real numbers

Reals (also called floating points) are stored on the computer as an approximation, albeit a very precise approximation. As an example, if we represent the distance from the earth to the sun using a double, the error is around a millimeter. However, we need to be very careful if we're trying to do a calculation that produces a very small (or very large number) and particularly when we want to see if numbers are equal to each other.

```r
0.3 - 0.2 == 0.1
## [1] FALSE
0.3
## [1] 0.3
0.2
## [1] 0.2
0.1 # Hmmm...
## [1] 0.1
0.75 - 0.5 == 0.25
## [1] TRUE
0.6 - 0.4 == 0.2
## [1] FALSE
## any ideas what is different about those two comparisons?
a <- 0.3
b <- 0.2
formatC(b, 20, format = 'f')
## [1] "0.20000000000000001110"
formatC(a, 20, format = 'f')
## [1] "0.29999999999999998890"
formatC(a - b, 20, format = 'f')
## [1] "0.09999999999999997780"
formatC(0.1, 20, format = 'f')
## [1] "0.10000
```

---

[Up: contents](../index.md)
