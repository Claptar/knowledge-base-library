---
title: Unit 06 — numbers Part 13 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 13 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In R, numbers are generally stored as doubles. We’ve basically already seen why - consider the maximum integer when using 4 bytes and the maximum floating point value. Representing integers as floats isn’t generally a problem, in part because integers will be stored exactly in base two provided the absolute value is less than 2<sup>53</sup> . Why 2<sup>53</sup> ?

However, you can force storage as integers in a few ways: values generated based on _seq()_ , based on the : operator, specified with an “L”, or explicitly coerced:

10

x <- 3; **typeof** (x) ## [1] "double" x <- **as.integer** (3); **typeof** (x) ## [1] "integer" x <- 3L; **typeof** (x) ## [1] "integer" x <- 3:5; **typeof** (x) ## [1] "integer"

### **2.4 Precision**

Consider our representation as ( _S, d, e_ ) where we have _p_ = 52 bits for _d_ . Since we have 2<sup>52</sup> _≈_ 0 _._ 5 _×_ 10<sup>16</sup> , we can represent about that many discrete values, which means we can accurately represent about 16 digits (in base 10). The result is that floats on a computer are actually discrete (we have a finite number of bits), and if we get a number that is in one of the gaps (there are uncountably many reals), it’s approximated by the nearest discrete value. The accuracy of our representation is to within 1/2 of the gap between the two discrete values bracketing the true number. Let’s consider the implications for accuracy in working with large and small numbers. By changing _e_ we can change the magnitude of a number. So regardless of whether we have a very large or small number, we have about 16 digits of accuracy, since the absolute spacing depends on what value is represented by the least significant digit (the _ulp_ , or _unit in the last place_ ) in _d_ , i.e., the _p_ = 52nd one, or in terms of base 10, the 16th digit. Let’s explore this:

**options** (digits = 22) _# large vs. small numbers_ .1234123412341234 ## [1] 0.1234123412341233960721 1234.1234123412341234 _# not accurate to 16 places_ ## [1] 1234.123412341234143241

11

123412341234.123412341234 _# only accurate to 4 places_ ## [1] 123412341234.1234130859 1234123412341234.123412341234 _# no places!_ ## [1] 1234123412341234 12341234123412341234 _# fewer than no places!_ ## [1] 12341234123412340736

We can see the implications of this in the context of calculations:

_# How precision affects calculations_ 1234567812345678 - 1234567812345677 ## [1] 1 12345678123456788888 - 12345678123456788887 ## [1] 0 12345678123456780000 - 12345678123456770000 ## [1] 10240 .1234567812345678 - .1234567812345677 ## [1] 9.714451465470119728707e-17 .12345678123456788888 - .12345678123456788887 ## [1] 0 .00001234567812345678 - .00001234567812345677 ## [1] 8.470329472543003390683e-21 _# not as close as we'd expect, should be 1e-20_ .000012345678123456788888 - .000012345678123456788887 ## [1] 0 123456781234 - .0000123456781234 _# the correct answer is 123456781233.99998765...._ ## [1] 123456781233.9999847412

12

Suppose we try this calculation: 123456781234 _− ._ 0000123456781234. How many decimal places do we expect to be accurate?

The spacing of possible computer numbers that have a magnitude of about 1 leads us to another definition of _machine epsilon_ (an alternative, but essentially equivalent definition to that given previously in this Unit). Machine epsilon tells us also about the relative spacing of numbers. First let’s consider numbers of magnitude one. The difference between 1 = 1 _._ 00 _..._ 00 _×_ 2<sup>0</sup> and 1 _._ 000 _..._ 01 _×_ 2<sup>0</sup> is 1 _×_ 2<sup>_−_52</sup> _≈_ 2 _._ 2 _×_ 10<sup>_−_16</sup> . Machine epsilon gives the _absolute spacing_ for numbers near 1 and the _relative spacing_ for numbers with a different order of magnitude and therefore a different absolute magnitude of the error in representing a real. The relative spacing at _x_ is


since the next largest number from _x_ is given by (1+ _ϵ_ ) _x_ . Suppose _x_ = 1 _×_ 10<sup>6</sup> . Then the absolute error in representing a number of this magnitude is _xϵ ≈_ 2 _×_ 10<sup>_−_10</sup> . (Actually the error would be one-half of the spacing, but that’s a minor distinction.) We can see by looking at the numbers in decimal form, where we are accurate to the order 10<sup>_−_10</sup> but not 10<sup>_−_11</sup> .

1000000.1

---

[← Unit 06 — numbers Part 12 —](12-unit-06-numbers-part-12.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 14 — →](14-unit-06-numbers-part-14.md)
