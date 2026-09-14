---
title: Unit 07 — numbers Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — numbers Part 06 —

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So why is 0.5 stored exactly and 0.1 not stored exactly? By analogy, consider the difficulty with representing 1/3 in base 10.

### **2.2 Overflow and underflow**

The largest and smallest numbers we can represent are 2<sup>_e_max</sup> and 2<sup>_e_min</sup> where _e_ max and _e_ min are the smallest and largest possible values of the exponent. Let’s consider the exponent and what we can infer about the range of possible numbers. With 11 bits for _e_ , we can represent _±_ 2<sup>10</sup> = _±_ 1024 different exponent values (see _.Machine$double.max.exp_ ) (why is _.Machine$double.min.exp_ only -1022? ). So the largest number we could represent is 2<sup>1024</sup> . What is this in base 10?

**log10** (2^1024) _# whoops ... we've actually just barely overflowed_ ## [1] Inf **log10** (2^1023) ## [1] 307.9536855642527370946

We could have been smarter about that calculation: log10 2<sup>1024</sup> = log2 2<sup>1024</sup> _/_ log2 10 = 1024 _/_ 3 _._ 32 _≈_ 308. Analogously for the smallest number, so we have that floating points can range between 1 _×_ 10<sup>_−_308</sup> and 1 _×_ 10<sup>308</sup> . Take a look at _.Machine$double.xmax_ and _.Machine.double.xmin_ . Producing something larger or smaller in magnitude than these values is called overflow and underflow respectively. When we overflow, R gives back an Inf or -Inf (and in other cases we might get an error message). When we underflow, we get back 0, which in particular can be a problem if we try to divide by the value.

6

### **2.3 Integers or floats?**

Values stored as integers should overflow if they exceed _.Machine$integer.max_ . Should 2<sup>45</sup> overflow?

x <- 2^45 z <- 25 **class** (x) ## [1] "numeric" **class** (z) ## [1] "numeric" **as.integer** (x) ## Warning: NAs introduced by coercion ## [1] NA **as.integer** (z) ## [1] 25 1e308 ## [1] 1.000000000000000010979e+308 **as.integer** (1e308) ## Warning: NAs introduced by coercion ## [1] NA 1e309 ## [1] Inf

In R, numbers are generally stored as doubles. We’ve basically already seen why - consider the maximum integer when using 4 bytes and the maximum floating point value. Representing integers as floats isn’t generally a problem, in part because integers will be stored exactly in base

7

two provided the absolute value is less than 2<sup>53</sup> . Why 2<sup>53</sup> ?

However, you can force storage as integers in a few ways: values generated based on _seq()_ , based on the : operator, specified with an “L”, or explicitly coerced:

x <- 3 **typeof** (x) ## [1] "double" x <- **as.integer** (3) **typeof** (x) ## [1] "integer" x <- 3L **typeof** (x) ## [1] "integer"

### **2.4 Precision**

Consider our representation as ( _S, d, e_ ) where we have _p_ = 52 bits for _d_ . Since we have 2<sup>52</sup> _≈_ 0 _._ 5 _×_ 10<sup>16</sup> , we can represent about that many discrete values, which means we can accurately represent about 16 digits (in base 10). The result is that floats on a computer are actually discrete (we have a finite number of bits), and if we get a number that is in one of the gaps (there are uncountably many reals), it’s approximated by the nearest discrete value. The accuracy of our representation is to within 1/2 of the gap between the two discrete values bracketing the true number. Let’s consider the implications for accuracy in working with large and small numbers. By changing _e_ we can change the magnitude of a number. So regardless of whether we have a very large or small number, we have about 16 digits of accuracy, since the absolute spacing depends on what value is represented by the least significant digit (the _ulp_ , or _unit in the last place_ ) in _d_ , i.e., the _p_ = 52nd one, or in terms of base 10, the 16th digit. Let’s explore this:

**options** (digits = 22) .1234123412341234 ## [1] 0.1234123412341233960721

8

1234.1234123412341234 _# not accurate to 16 places_ ## [1] 1234.123412341234143241 123412341234.123412341234 _# only accurate to 4 places_ ## [1] 123412341234.1234130859 1234123412341234.123412341234 _# no places!_ ## [1] 1234123412341234 12341234123412341234 _# fewer than no places!_ ## [1] 12341234123412340736

We can see the implications of this in the context of calculations:

1234567812345678 - 1234567812345677 ## [1] 1 12345678123456788888 - 12345678123456788887 ## [1] 0 12345678123456780000 - 12345678123456770000 ## [1] 10240 .1234567812345678 - .1234567812345677 ## [1] 9.714451465470119728707e-17 .12345678123456788888 - .12345678123456788887 ## [1] 0 .00001234567812345678 - .00001234567812345677 ## [1] 8.470329472543003390683e-21 _# the above is not as close as we'd expect, should be 1e-20_ .000012345678123456788888 - .000012345678123456788887 ## [1] 0

9

Suppose we try this calculation: 123456781234 _− ._ 0000123456781234. How many decimal places do we expect to be accurate?

The spacing of possible computer numbers that have a magnitude of about 1 leads us to another definition of _machine epsilon_ (an alternative, but essentially equivalent definition to that given previously in this Unit). Machine epsilon tells us also about the relative spacing of numbers. First let’s consider numbers of magnitude one. The difference between 1 = 1 _._ 00 _..._ 00 _×_ 2<sup>0</sup> and 1 _._ 000 _..._ 01 _×_ 2<sup>0</sup> is 1 _×_ 2<sup>_−_52</sup> _≈_ 2 _._ 2 _×_ 10<sup>_−_16</sup> . Machine epsilon gives the _absolute spacing_ for numbers near 1 and the _relative spacing_ for numbers with a different order of magnitude and therefore a different absolute magnitude of the error in representing a real. The relative spacing at _x_ is


since the next largest number from _x_ is given by (1+ _ϵ_ ) _x_ . Suppose _x_ = 1 _×_ 10<sup>6</sup> . Then the absolute error in representing a number of this magnitude is _xϵ ≈_ 2 _×_ 10<sup>_−_10</sup> . (Actually the error would be one-half of the spacing, but that’s a minor distinction.) We can see by looking at the numbers in decimal form, where we are accurate to the order 10<sup>_−_10</sup> but not 10<sup>_−_11</sup> .

1000000.1 ## [1] 1000000.099999999976717

Let’s see what arithmetic we can do exactly with integers stored as doubles and how that relates to the absolute spacing of numbers we’ve just seen:

2^52 ## [1] 4503599627370496 2^52 + 1 ## [1] 4503599627370497 2^53 ## [1] 9007199254740992 2^53 + 1 ## [1] 9007199254740992

10

2^53 + 2 ## [1] 9007199254740994 2^54 ## [1] 18014398509481984 2^54 + 2 ## [1] 18014398509481984 2^54 + 4 ## [1] 18014398509481988

The absolute spacing is _xϵ_ , so 2<sup>52</sup> _×_ 2<sup>_−_52</sup> = 1, 2<sup>53</sup> _×_ 2<sup>_−_52</sup> = 2, 2<sup>54</sup> _×_ 2<sup>_−_52</sup> = 4.

With a bit more work (e.g., using Mathematica), one can demonstrate that doubles in R in general are represented as the nearest number that can stored with the 64-bit structure we have discussed and that the spacing is as we have discussed. The results here show the spacing that results, in base 10, for numbers around 1. The numbers R reports are spaced in increments of individual bits in the base 2 representation.

**options** (digits = 22) 0.1234567812345678 ## [1] 0.1234567812345677972896 0.12345678123456781 ## [1] 0.1234567812345678111674 0.12345678123456782 ## [1] 0.1234567812345678250452 0.12345678123456783 ## [1] 0.1234567812345678250452 0.12345678123456784 ## [1] 0.123456781234567838923

11

### **2.5 Working with higher precision numbers**

The _Rmpfr_ package allows us to work with numbers in higher precision. (This code is not working with _knitr_ , so I’m just showing the code here, not the output.)

**require** (Rmpfr) piLong <- **Const** ("pi", prec = 260) _# pi 'computed' to correct 260-bit precision_ piLong _# nicely prints 80 digits_ **mpfr** (".1234567812345678", 40) **mpfr** (".1234567812345678", 80) **mpfr** (".1234567812345678", 600)

In contrast to R, Python has arbitrary precision integers. So, e.g., pow(3423333, 15) returns an integer. But floating points are handled in similar fashion to R.

---

[← Unit 07 — numbers Part 05 —](05-unit-07-numbers-part-05.md) · [Up: contents](index.md) · [3 Implications for calculations and comparisons →](07-3-implications-for-calculations-and-comparisons.md)
