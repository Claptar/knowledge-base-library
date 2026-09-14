---
title: Unit 06 — numbers Part 13 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 13 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

10

In R, numbers are generally stored as doubles. We’ve basically already seen why - consider the maximum integer when using 4 bytes and the maximum floating point value. Representing integers as floats isn’t generally a problem, in part because integers will be stored exactly in base two provided the absolute value is less than 2<sup>53</sup> .

Challenge: Why 2<sup>53</sup> ? Write out what integers can be stored exactly in our base 2 representation of floating point numbers.

However, you can force storage as integers in a few ways: values generated based on _seq()_ , based on the : operator, specified with an “L”, or explicitly coerced:

x <- 3; **typeof** (x) ## [1] "double" x <- **as.integer** (3); **typeof** (x) ## [1] "integer" x <- 3L; **typeof** (x) ## [1] "integer" x <- 3:5; **typeof** (x) ## [1] "integer"

### **2.4 Precision**

Consider our representation as ( _S, d, e_ ) where we have _p_ = 52 bits for _d_ . Since we have 2<sup>52</sup> _≈_ 0 _._ 5 _×_ 10<sup>16</sup> , we can represent about that many discrete values, which means we can accurately represent about 16 digits (in base 10). The result is that floats on a computer are actually discrete (we have a finite number of bits), and if we get a number that is in one of the gaps (there are uncountably many reals), it’s approximated by the nearest discrete value. The accuracy of our representation is to within 1/2 of the gap between the two discrete values bracketing the true number. Let’s consider the implications for accuracy in working with large and small numbers. By changing _e_ we can change the magnitude of a number. So regardless of whether we have a very large or small number, we have about 16 digits of accuracy, since the absolute spacing depends on what value is represented by the least significant digit (the _ulp_ , or _unit in the last place_ ) in _d_ , i.e., the _p_ = 52nd one, or in terms of base 10, the 16th digit. Let’s explore this:

11

**options** (digits = 22) _# large vs. small numbers_ .1234123412341234 ## [1] 0.1234123412341233960721 1234.1234123412341234 _# not accurate to 16 places_ ## [1] 1234.123412341234143241 123412341234.123412341234 _# only accurate to 4 places_ ## [1] 123412341234.1234130859 1234123412341234.123412341234 _# no places!_ ## [1] 1234123412341234 12341234123412341234 _# fewer than no places!_ ## [1] 12341234123412340736 We can see the implications of this in the context of calculations:

_# How precision affects calculations_ 1234567812345678 - 1234567812345677 ## [1] 1 12345678123456788888 - 12345678123456788887 ## [1] 0 12345678123456780000 - 12345678123456770000 ## [1] 10240 .1234567812345678 - .1234567812345677 ## [1] 9.714451465470119728707e-17 .12345678123456788888 - .12345678123456788887

12

---

[← Unit 06 — numbers Part 12 —](12-unit-06-numbers-part-12.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 14 — →](14-unit-06-numbers-part-14.md)
