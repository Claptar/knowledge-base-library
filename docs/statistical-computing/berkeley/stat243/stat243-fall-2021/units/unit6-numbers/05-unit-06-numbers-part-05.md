---
title: Unit 06 — numbers Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 05 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6

**formatC** (0.50, 20, format = 'f') ## [1] "0.50000000000000000000" _## alternative to formatC:_ **sprintf** ("%0.20f", a) ## [1] "0.29999999999999998890" _## define a wrapper function for convenience:_ dg <- **function** (x, digits = 20) **formatC** (x, digits, format = 'f')

Notice that we can represent the result accurately only up to 16 significant digits. This suggests no need to show more than 16 significant digits and no need to print out any more when writing to a file (except that if the number is bigger than 10<sup>16</sup> then we need extra digits to correctly show the magnitude of the number if not using scientific notation). And of course, often we don’t need anywhere near that many. _Machine epsilon_ is the term used for indicating the (relative) accuracy of real numbers and it is defined as the smallest float, _x_ , such that 1 + _x̸_ = 1:

**dg** (1e-16 + 1) ## [1] "1.00000000000000000000" **dg** (1e-15 + 1) ## [1] "1.00000000000000111022" **dg** (2e-16 + 1) ## [1] "1.00000000000000022204" **dg** (.Machine$double.eps) ## [1] "0.00000000000000022204" **dg** (.Machine$double.eps + 1) ## [1] "1.00000000000000022204"

7

**Floating point representation** _Floating point_ refers to the decimal point (or radix point since we’ll be working with base 2 and _decimal_ relates to 10). Consider Avogadro’s number in terms of scientific notation: +6 _._ 023 _×_ 10<sup>23</sup> . As a baseline for what is about to follow note that we can express a decimal number in the following expansion


A real number on a computer is stored in what is basically scientific notation:


where _b_ is the base, _e_ is an integer and _di ∈{_ 0 _, . . . , b −_ 1 _}_ . First, we need to choose the number of bits to represent _e_ so that we can represent sufficiently large and small numbers. Second we need to choose the number of bits, _p_ , to allocate to _d_ = _d_ 1 _d_ 2 _. . . dp_ , which determines the accuracy of any computer representation of a real. The great thing about floating points is that we can represent numbers that range from incredibly small to very large while maintaining good precision. The floating point floats to adjust to the size of the number. Suppose we had only three digits to use and were in base 10. In floating point notation we can express 0 _._ 12 _×_ 0 _._ 12 = 0 _._ 0144 as (1 _._ 20 _×_ 10<sup>_−_1</sup> ) _×_ (1 _._ 20 _×_ 10<sup>_−_1</sup> ) = 1 _._ 44 _×_ 10<sup>_−_2</sup> , but if we had fixed the decimal point, we’d have 0 _._ 120 _×_ 0 _._ 120 = 0 _._ 014 and we’d have lost a digit of accuracy.

More specifically, the actual storage of a number on a computer these days is generally as a double in the form:


where the computer uses base 2, _b_ = 2, (so _di ∈{_ 0 _,_ 1 _}_ ) because base-2 arithmetic is faster than base-10 arithmetic. The leading 1 normalizes the number; i.e., ensures there is a unique representation for a given computer number. This avoids representing any number in multiple ways, e.g., either 1 = 1 _._ 0 _×_ 2<sup>0</sup> = 0 _._ 1 _×_ 2<sup>1</sup> = 0 _._ 01 _×_ 2<sup>2</sup> . For a double, we have 8 bytes=64 bits. Consider our representation as ( _S, d, e_ ) where _S_ is the sign. The leading 1 is the _hidden bit_ . In general _e_ is represented using 11 bits (2<sup>11</sup> = 2048), and the subtraction takes the place of having a sign bit for the exponent. (Note that in our discussion we’ll just think of _e_ in terms of its base 10 representation, although it is of course represented in base 2.) This leaves _p_ = 52 bits for _d_ .

**bits** (2^(-1)) _# 1/2_

---

[← 2 Floating point basics](04-2-floating-point-basics.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 06 — →](06-unit-06-numbers-part-06.md)
