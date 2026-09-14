---
title: large vs. small numbers
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit8-numbers.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# large vs. small numbers

**Source:** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

dg(.1234123412341234)
dg(1234.1234123412341234) # not accurate to 16 decimal places
dg(123412341234.123412341234) # only accurate to 4 places
dg(1234123412341234.123412341234) # no places!
dg(12341234123412341234) # fewer than no places!
```

We can see the implications of this in the context of calculations:


```python
#| tidy: false
dg(1234567812345678.0 - 1234567812345677.0)
dg(12345678123456788888.0 - 12345678123456788887.0)
dg(12345678123456780000.0 - 12345678123456770000.0)
```

The spacing of possible computer numbers that have a magnitude of about
1 leads us to another definition of *machine epsilon* (an alternative,
but essentially equivalent definition to that given [previously](03-2-floating-point-basics.md#machine-epsilon).
Machine epsilon tells us also about the relative spacing of
numbers.

First let's consider numbers of magnitude one. The next biggest number we can represent after  $1=1.00...00\times2^{0}$ is $1.000...01\times2^{0}$. The difference between those two numbers (i.e., the spacing) is
$$
\begin{aligned}
\epsilon & = &0.00...01 \times 2^{0} \\
 & =& 0 \times 2^{0} + 0 \times 2^{-1} + \cdots + 0\times 2^{-51} + 1\times2^{-52}\\
 & =& 1\times2^{-52}\\
 & \approx & 2.2\times10^{-16}.
 \end{aligned}
 $$


Machine epsilon gives
the *absolute spacing* for numbers near 1 and the *relative spacing* for
numbers with a different order of magnitude and therefore a different
absolute magnitude of the error in representing a real. The relative
spacing at $x$ is $$\frac{(1+\epsilon)x-x}{x}=\epsilon$$ since the next
largest number from $x$ is given by $(1+\epsilon)x$.

Suppose $x=1\times10^{6}$. Then the absolute error in representing a
number of this magnitude is $x\epsilon\approx2\times10^{-10}$. (Actually
the error would be one-half of the spacing, but that's a minor
distinction.) We can see by looking at the numbers in decimal form,
where we are accurate to the order $10^{-10}$ but not $10^{-11}$. This
is equivalent to our discussion that we have only 16 digits of accuracy.


```python
dg(1000000.1)
```

Let's see what arithmetic we can do exactly with integer-valued numbers stored as
doubles and how that relates to the absolute spacing of numbers we've
just seen:


```python
2.0**52
2.0**52+1
2.0**53
2.0**53+1
2.0**53+2
dg(2.0**54)
dg(2.0**54+2)
dg(2.0**54+4)

bits(2**53)
bits(2**53+1)
bits(2**53+2)
bits(2**54)
bits(2**54+2)
bits(2**54+4)
```

The absolute spacing is $x\epsilon$, so we have spacings of
$2^{52}\times2^{-52}=1$, $2^{53}\times2^{-52}=2$,
$2^{54}\times2^{-52}=4$ for numbers of magnitude $2^{52}$, $2^{53}$, and
$2^{54}$, respectively.

With a bit more work (e.g., using Mathematica), one can demonstrate that
doubles in Python in general are represented as the nearest number that can
stored with the 64-bit structure we have discussed and that the spacing
is as we have discussed. The results below show the spacing that
results, in base 10, for numbers around 0.1. The numbers Python reports are
spaced in increments of individual bits in the base 2 representation.


```python
#| tidy: false
dg(0.1234567812345678)
dg(0.12345678123456781)
dg(0.12345678123456782)
dg(0.12345678123456783)
dg(0.12345678123456784)

bits(0.1234567812345678)
bits(0.12345678123456781)
bits(0.12345678123456782)
bits(0.12345678123456783)
bits(0.12345678123456784)
```

## Working with higher precision numbers

As we've seen, Python will automatically work with integers in arbitrary precision.
(Note that R does not do this -- R uses 4-byte integers, and for many calculations
it's best to use R's `numeric` type because integers that aren't really large
can be expressed exactly.)

For higher precision floating point numbers you can make use of the `gmpy2`
package.

```python
#| eval: false
import gmpy2
gmpy2.get_context().precision=200
gmpy2.const_pi()

## not sure why this shows ...00004
gmpy2.mpfr(".1234567812345678")
```

---

[← Interesting](05-interesting.md) · [Up: contents](index.md) · [3. Implications for calculations and comparisons →](07-3-implications-for-calculations-and-comparisons.md)
