---
title: Unit 07 — numbers Part 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — numbers Part 08 —

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

res2

### **3.2 Calculating with integers vs. floating points**

It’s important to note that operations with integers are fast and exact (but can easily overflow) while operations with floating points are slower and approximate. Because of this slowness, floating point operations ( _flops_ ) dominate calculation intensity and are used as the metric for the amount of work being done - a multiplication (or division) combined with an addition (or subtraction) is one flop. We’ll talk a lot about flops in the next unit on linear algebra.

### **3.3 Comparisons**

As we saw, we should never test a==b unless (1) _a_ and _b_ are represented as integers in R, (2) they are integers stored as doubles that are small enough that they can be stored exactly) or (3) they are decimal numbers that have been created in the same way (e.g., 0.1==0.1 vs. 0.1==0.4-0.3. Similarly we should be careful about testing a==0. And be careful of greater than/less than comparisons. For example, be careful of x[ x < 0 ] <- NA if what you are looking for is values that might be _mathematically_ less than zero, rather than whatever is _numerically_ less than zero.

4L - 3L == 1L ## [1] TRUE 4 - 3 == 1 ## [1] TRUE 4.1 - 3.1 == 1 ## [1] FALSE

One nice approach to checking for approximate equality is to make use of _machine epsilon_ . If the relative spacing of two numbers is less than _machine epsilon_ , then for our computer approximation, we say they are the same. Here’s an implementation that relies on the absolute spacing being _xϵ_ (see above):

13

if(abs(a - b) < .Machine$double.eps * abs(a + b)) print(“approximately equal”)

Actually, we probably want to use a number slightly larger than _.Machine$double.eps_ to be safe. You can also take a look at the R function _all.equal.numeric()_ .

Finally, in computing, we often encounter the use of an unusual integer as a symbol for missing values. E.g., a datafile might store missing values as -9999. Testing for this using == in R should generally be ok: x [ x == -9999 ] <- NA, but only because integers of this magnitude are stored exactly. To be really careful, you can read in as character type and do the assessment before converting to numeric.

### **3.4 Calculations**

Given the limited _precision_ of computer numbers, we need to be careful when:

- Subtracting large numbers that are nearly equal (or adding negative and positive numbers of the same magnitude). You won’t have the precision in the answer that you would like.

123456781234.56 - 123456781234.00

---

[← 3 Implications for calculations and comparisons](07-3-implications-for-calculations-and-comparisons.md) · [Up: contents](index.md) · [Unit 07 — numbers Part 09 — →](09-unit-07-numbers-part-09.md)
