---
title: Unit 07 — numbers Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — numbers Part 04 —

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Notice that we can represent the result accurately only up to the 16th decimal place. This suggests no need to show more than 16 decimal places and no need to print out any more when writing to a file. And of course, often we don’t need anywhere near that many. _Machine epsilon_ is the term used for indicating the accuracy of real numbers and it is defined as the smallest float, _x_ , such that 1 + _x̸_ = 1:

1e-16 + 1 ## [1] 1 1e-15 + 1 ## [1] 1.000000000000001110223 2e-16 + 1 ## [1] 1.000000000000000222045 .Machine$double.eps ## [1] 2.220446049250313080847e-16

_Floating point_ refers to the decimal point (or radix point since we’ll be working with base 2 and

4

_decimal_ relates to 10). Consider Avogadro’s number in terms of scientific notation: +6 _._ 023 _×_ 10<sup>23</sup> . A real number on a computer is stored in what is basically scientific notation:


where _b_ is the base, _e_ is an integer and _di ∈{_ 0 _, . . . , b −_ 1 _}_ . First, we need to choose the number of bits to represent _e_ so that we can represent sufficiently large and small numbers. Second we need to choose the number of bits, _p_ , to allocate to _d_ = _d_ 1 _d_ 2 _. . . dp_ , which determines the accuracy of any computer representation of a real. The great thing about floating points is that we can represent numbers that range from incredibly small to very large while maintaining good precision. The floating point floats to adjust to the size of the number. Suppose we had only three digits to use and were in base 10. In floating point notation we can express 0 _._ 12 _×_ 0 _._ 12 = 0 _._ 0144 as (1 _._ 20 _×_ 10<sup>_−_1</sup> ) _×_ (1 _._ 20 _×_ 10<sup>_−_1</sup> ) = 1 _._ 44 _×_ 10<sup>_−_2</sup> , but if we had fixed the decimal point, we’d have 0 _._ 120 _×_ 0 _._ 120 = 0 _._ 014 and we’d have lost a digit of accuracy.

More specifically, the actual storage of a number on a computer these days is generally as a double in the form:


where the computer uses base 2, _b_ = 2, because base-2 arithmetic is faster than base-10 arithmetic. The leading 1 normalizes the number; i.e., ensures there is a unique representation for a given computer number. This avoids representing any number in multiple ways, e.g., either 1 = 1 _._ 0 _×_ 2<sup>0</sup> = 0 _._ 1 _×_ 2<sup>1</sup> = 0 _._ 01 _×_ 2<sup>2</sup> . For a double, we have 8 bytes=64 bits. Consider our representation as ( _S, d, e_ ) where _S_ is the sign. The leading 1 is the _hidden bit_ . In general _e_ is represented using 11 bits (2<sup>11</sup> = 2048), and the subtraction takes the place of having a sign bit for the exponent. This leaves _p_ = 52 bits for _d_ .

**Question** : Given a fixed number of bits for a number, what is the tradeoff between using bits for the _d_ part vs. bits for the _e_ part?

Let’s consider what can be represented exactly:

0.1

---

[← 2 Floating point basics](03-2-floating-point-basics.md) · [Up: contents](index.md) · [Unit 07 — numbers Part 05 — →](05-unit-07-numbers-part-05.md)
