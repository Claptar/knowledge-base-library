---
title: Unit 06 — numbers Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 04 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

2

**bits** (1L) ## [1] "00000000 00000000 00000000 00000001" **bytes** (1L) ## [1] "00 00 00 01" **bits** (2L) ## [1] "00000000 00000000 00000000 00000010" **bytes** (2L) ## [1] "00 00 00 02" **bits** (-1L) ## [1] "11111111 11111111 11111111 11111111" **bytes** (-1L) ## [1] "FF FF FF FF"

Finally note that the set of computer integers is not closed under arithmetic, with R reporting an overflow (i.e., a result that is too large to be stored as an integer):

a <- **as.integer** (3423333) _# 3423333L_ a * a ## Warning in a * a: NAs produced by integer overflow ## [1] NA

Real numbers (or _floating points_ ) use a minimum of 4 bytes, for single precision floating points. In general 8 bytes are used to represent real numbers on a computer and these are called _double precision floating points_ or _doubles_ . Let’s see some examples in R of how much space different types of variables take up.

Let’s see how this plays out in terms of memory use in R.

3

doubleVec <- **rnorm** (100000) intVec <- 1:100000 **set.seed** (1) charVec <- **sample** (letters, 100000, replace = TRUE) **object.size** (doubleVec) ## 800048 bytes **object.size** (intVec) _# so how many bytes per integer in R?_ ## 400048 bytes **object.size** (charVec) ## 801504 bytes charVec[1:5] <- **c** ('a','a','b','b','c') **.Internal** ( **inspect** (charVec)) _# anything jump out at you?_ ## @55c49e52bdc0 16 STRSXP g0c7 [NAM(1)] (len=100000, tl=0) ## @55c498eeeef0 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "a" ## @55c498eeeef0 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "a" ## @55c49920fc20 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "b" ## @55c49920fc20 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "b" ## @55c498be0478 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "c" ## ...

We can easily calculate the number of megabytes (MB) a vector of floating points (in double precision) will use as the number of elements times 8 (bytes/double) divided by 10<sup>6</sup> to convert from bytes to megabytes. (In some cases when considering computer memory, a megabyte is 1 _,_ 048 _,_ 576 = 2<sup>20</sup> = 1024<sup>2</sup> bytes (this is formally called a _mebibyte_ ) so slightly different than 10<sup>6</sup> – see here for more details). Finally, R has a special object that tells us about the characteristics of computer numbers on the machine that R is running on called _.Machine._ For example, _.Machine$integer.max_ is 2147483647 = 2<sup>31</sup> _−_ 1, which confirms how many bytes R is using for each integer (and that R is using a bit for the sign of the integer). Since we have both negative and positive numbers, we have 2 _·_ 2<sup>31</sup> = 2<sup>32</sup> = (2<sup>8</sup> )<sup>4</sup> , i.e., 4 bytes, with each byte having 8 bits.

4

**bits** (.Machine$integer.max) ## [1] "01111111 11111111 11111111 11111111" **bits** (-.Machine$integer.max) ## [1] "10000000 00000000 00000000 00000001" **bits** (-1L) ## [1] "11111111 11111111 11111111 11111111"

---

[← [1] "00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000" bytes (0)](03-1-00000000-00000000-00000000-00000000-00000000-00000000-0000.md) · [Up: contents](index.md) · [2 Floating point basics →](05-2-floating-point-basics.md)
