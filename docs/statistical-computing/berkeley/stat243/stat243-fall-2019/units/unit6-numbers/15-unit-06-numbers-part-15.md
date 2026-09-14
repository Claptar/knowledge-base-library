---
title: Unit 06 — numbers Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 15 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So why is 0.5 stored exactly and 0.1 not stored exactly? By analogy, consider the difficulty with representing 1/3 in base 10.

### **2.2 Overflow and underflow**

The largest and smallest numbers we can represent are 2<sup>_e_max</sup> and 2<sup>_e_min</sup> where _e_ max and _e_ min are the smallest and largest possible values of the exponent. Let’s consider the exponent and what we can infer about the range of possible numbers. With 11 bits for _e_ , we can represent _±_ 2<sup>10</sup> = _±_ 1024 different exponent values (see _.Machine$double.max.exp_ ) (why is _.Machine$double.min.exp_ only -1022? ). So the largest number we could represent is 2<sup>1024</sup> . What is this in base 10?

**log10** (2^1024) _# whoops ... we've actually just barely overflowed_ ## [1] Inf **log10** (2^1023) ## [1] 307.9537 .Machine$double.xmax ## [1] 1.797693e+308 .Machine$double.xmin ## [1] 2.225074e-308

9

We could have been smarter about that calculation: log10 2<sup>1024</sup> = log2 2<sup>1024</sup> _/_ log2 10 = 1024 _/_ 3 _._ 32 _≈_ 308. The result is analogous for the smallest number, so we have that floating points can range between 1 _×_ 10<sup>_−_308</sup> and 1 _×_ 10<sup>308</sup> . Take a look at _.Machine$double.xmax_ and _.Machine.double.xmin_ . Producing something larger or smaller in magnitude than these values is called overflow and underflow respectively. When we overflow, R gives back an Inf or -Inf (and in other cases we might get an error message). When we underflow, we get back 0, which in particular can be a problem if we try to divide by the value.

### **2.3 Integers or floats?**

Values stored as integers should overflow if they exceed _.Machine$integer.max_ .

Should 2<sup>45</sup> overflow?

x <- 2^45 z <- 25 **class** (x) ## [1] "numeric" **class** (z) ## [1] "numeric" **as.integer** (x) ## Warning: NAs introduced by coercion to integer range ## [1] NA **as.integer** (z) ## [1] 25 1e308 ## [1] 1e+308 1e309 ## [1] Inf

10

2^31 ## [1] 2147483648 x <- 2147483647L x ## [1] 2147483647 **class** (x) ## [1] "integer" x <- 2147483648L **class** (x) ## [1] "numeric"

In R, numbers are generally stored as doubles. We’ve basically already seen why - consider the maximum integer when using 4 bytes and the maximum floating point value. Representing integers as floats isn’t generally a problem, in part because integers will be stored exactly in base two provided the absolute value is less than 2<sup>53</sup> .

Challenge: Why 2<sup>53</sup> ? Write out what integers can be stored exactly in our base 2 representation of floating point numbers.

However, you can force storage as integers in a few ways: values generated based on _seq()_ , based on the : operator, specified with an “L”, or explicitly coerced:

x <- 3; **typeof** (x) ## [1] "double" x <- **as.integer** (3); **typeof** (x) ## [1] "integer" x <- 3L; **typeof** (x) ## [1] "integer" x <- 3:5; **typeof** (x) ## [1] "integer"

11

### **2.4 Precision**

Consider our representation as ( _S, d, e_ ) where we have _p_ = 52 bits for _d_ . Since we have 2<sup>52</sup> _≈_ 0 _._ 5 _×_ 10<sup>16</sup> , we can represent about that many discrete values, which means we can accurately represent about 16 digits (in base 10). The result is that floats on a computer are actually discrete (we have a finite number of bits), and if we get a number that is in one of the gaps (there are uncountably many reals), it’s approximated by the nearest discrete value. The accuracy of our representation is to within 1/2 of the gap between the two discrete values bracketing the true number. Let’s consider the implications for accuracy in working with large and small numbers. By changing _e_ we can change the magnitude of a number. So regardless of whether we have a very large or small number, we have about 16 digits of accuracy, since the absolute spacing depends on what value is represented by the least significant digit (the _ulp_ , or _unit in the last place_ ) in _d_ , i.e., the _p_ = 52nd one, or in terms of base 10, the 16th digit. Let’s explore this:

_# large vs. small numbers_ **dg** (.1234123412341234)

---

[← Unit 06 — numbers Part 14 —](14-unit-06-numbers-part-14.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 16 — →](16-unit-06-numbers-part-16.md)
