---
title: 3 Implications for calculations and comparisons
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Implications for calculations and comparisons

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Computer arithmetic is not mathematical arithmetic!**

As mentioned for integers, computer number arithmetic is not closed, unlike real arithmetic. For example, if we multiply two computer floating points, we can overflow and not get back another computer floating point. One term that is used, which might pop up in an error message (though probably not in R) is that an “exception” is “thrown”. Another mathematical concept we should consider here is that computer arithmetic does not obey the associative and distribute laws, i.e., ( _a_ + _b_ ) + _c_ may not equal _a_ + ( _b_ + _c_ ) on a computer and _a_ ( _b_ + _c_ ) may not be the same as _ab_ + _ac_ . Here’s an example:

val1 <- 1/10; val2 <- 0.31; val3 <- 0.57 res1 <- val1*val2*val3 res2 <- val3*val2*val1 **identical** (res1, res2) ## [1] FALSE **dg** (res1) ## [1] "0.01766999999999999821" **dg** (res2) ## [1] "0.01767000000000000168"

### **3.2 Calculating with integers vs. floating points**

It’s important to note that operations with integers are fast and exact (but can easily overflow) while operations with floating points are slower and approximate. Because of this slowness, floating point

17

operations ( _flops_ ) dominate calculation intensity and are used as the metric for the amount of work being done - a multiplication (or division) combined with an addition (or subtraction) is one flop. We’ll talk a lot about flops in the unit on linear algebra.

### **3.3 Comparisons**

As we saw, we should never test a==b unless (1) _a_ and _b_ are represented as integers in R, (2) they are integer-valued but stored as doubles that are small enough that they can be stored exactly) or (3) they are decimal numbers that have been created in the same way (e.g., 0.4-0.3==0.4-0.3 vs. 0.1==0.4-0.3. Similarly we should be careful about testing a==0. And be careful of greater than/less than comparisons. For example, be careful of x[ x < 0 ] <- NA if what you are looking for is values that might be _mathematically_ less than zero, rather than whatever is _numerically_ less than zero.

4L - 3L == 1L ## [1] TRUE 4.0 - 3.0 == 1.0 ## [1] TRUE 4.1 - 3.1 == 1.0 ## [1] FALSE

One nice approach to checking for approximate equality is to make use of _machine epsilon_ . If the relative spacing of two numbers is less than _machine epsilon_ , then for our computer approximation, we say they are the same. Here’s an implementation that relies on the absolute spacing being _xϵ_ (see above).

a = 12345678123456781000 b = 12345678123456782000 approxEqual = **function** (a, b){ **if** ( **abs** (a - b) < .Machine$double.eps * **abs** (a + b)) **print** ("approximately equal") **else print** ("not equal") }

18

**approxEqual** (a,b)

---

[← Unit 06 — numbers Part 40 —](40-unit-06-numbers-part-40.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 42 — →](42-unit-06-numbers-part-42.md)
