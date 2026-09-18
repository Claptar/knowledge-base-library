---
title: 2. Floating point basics
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit8-numbers.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2. Floating point basics

## Representing real numbers

### Initial exploration

Reals (also called floating points) are stored on the computer as an
approximation, albeit a very precise approximation. As an example, if we
represent the distance from the earth to the sun using a double, the
error is around a millimeter. However, we need to be very careful if
we're trying to do a calculation that produces a very small (or very
large number) and particularly when we want to see if numbers are equal
to each other.

If you run the code here, the results may surprise you.
```python
#| eval: false
0.3 - 0.2 == 0.1
0.3
0.2
0.1 # Hmmm...

np.float64(0.3) - np.float64(0.2) == np.float64(0.1)

0.75 - 0.5 == 0.25
0.6 - 0.4 == 0.2
## any ideas what is different about those two comparisons?
```

Next, let's consider the number of digits of accuracy
we have for a variety of numbers. We'll use `format` within
a handy wrapper function, `dg`, defined earlier, to view as many digits as we want:

```python
a = 0.3
b = 0.2
dg(a)
dg(b)

dg(a-b)
dg(0.1)
dg(1/3)

```

So empirically, it looks like we're accurate up to the 16th decimal place

But actually, the key is the number of digits, not decimal places.

```python
dg(1234.1234)
dg(1234.123412341234)
```

Notice that we can represent the result accurately only up to 16
significant digits. This suggests no need to show more than 16
significant digits and no need to print out any more when writing to a
file (except that if the number is bigger than $10^{16}$ then we need
extra digits to correctly show the magnitude of the number if not using
scientific notation). And of course, often we don't need anywhere near
that many.

Let's return to our comparison, `0.75-0.5 == 0.25`.

```python
dg(0.75)
dg(0.50)
```

What's different about the numbers 0.75 and 0.5 compared to 0.3, 0.2,
0.1?

### Machine epsilon

*Machine epsilon* is the term used for indicating the
(relative) accuracy of real numbers and it is defined as the smallest
float, $x$, such that $1+x\ne1$:

```python
1e-16 + 1.0
np.array(1e-16) + np.array(1.0)
1e-15 + 1.0
np.array(1e-15) + np.array(1.0)
2e-16 + 1.0

np.finfo(np.float64).eps
dg(2e-16 + 1.0)
```

What about in single precision, e.g. on a GPU?
```python
np.finfo(np.float32).eps
```

### Floating point representation

*Floating point* refers to the decimal point (or *radix* point since we'll
be working with base 2 and *decimal* relates to 10).

To proceed further we need to consider scientific notation, such as in writing Avogadro's
number as $+6.023\times10^{23}$. As a
baseline for what is about to follow note that we can express a decimal
number in the following expansion
$$6.037=6\times10^{0}+0\times10^{-1}+3\times10^{-2}+7\times10^{-3}$$ A real number on a
computer is stored in what is basically scientific notation:
$$\pm d_{0}.d_{1}d_{2}\ldots d_{p}\times b^{e}\label{eq:floatRep}$$
where $b$ is the base, $e$ is an integer and $d_{i}\in\{0,\ldots,b-1\}$.
$e$ is called the *exponent* and $d=d_{1}d_{2}\ldots d_{p}$ is called the *mantissa*.

The great thing about floating points
is that we can represent numbers that range from incredibly small to
very large while maintaining good precision. The floating point *floats*
to adjust to the size of the number. Suppose we had only three digits to
use and were in base 10. In floating point notation we can express
$0.12\times0.12=0.0144$ as
$(1.20\times10^{-1})\times(1.20\times10^{-1})=1.44\times10^{-2}$, but if
we had fixed the decimal point, we'd have $0.120\times0.120=0.014$ and
we'd have lost a digit of accuracy. (Furthermore, we wouldn't be able
to represent numbers bigger than $0.99$.)

Let's consider the choices that the computer pioneers needed to make
in using this system to represent numbers on a computer using base 2 ($b=2$).
First, we need to choose the number of bits to represent $e$ so that we
can represent sufficiently large and small numbers. Second we need to
choose the number of bits, $p$, to allocate to
$d=d_{1}d_{2}\ldots d_{p}$, which determines the accuracy of any
computer representation of a real.

More specifically, the actual storage of a number on a computer these
days is generally as a double in the form:
$$(-1)^{S}\times1.d\times2^{e-1023}=(-1)^{S}\times1.d_{1}d_{2}\ldots d_{52}\times2^{e-1023}$$
where the computer uses base 2, $b=2$, (so $d_{i}\in\{0,1\}$) because
base-2 arithmetic is faster than base-10 arithmetic. The leading 1
normalizes the number; i.e., ensures there is a unique representation
for a given computer number. This avoids representing any number in
multiple ways, e.g., either
$1=1.0\times2^{0}=0.1\times2^{1}=0.01\times2^{2}$. For a double, we have
8 bytes=64 bits. Consider our representation as ($S,d,e$) where $S$ is
the sign. The leading 1 is the *hidden bit* and doesn't need to be
stored because it is always present. In general $e$ is
represented using 11 bits ($2^{11}=2048$), and the subtraction takes the
place of having a sign bit for the exponent. (Note that in our
discussion we'll just think of $e$ in terms of its base 10
representation, although it is of course represented in base 2.) This
leaves $p=52 = 64-1-11$ bits for $d$.

In this code I force storage as a double by tacking on a decimal place, `.0`.

```python
bits(2.0**(-1)) # 1/2
bits(2.0**0)  # 1
bits(2.0**1)  # 2
bits(2.0**1 + 2.0**0)  # 3
bits(2.0**2)  # 4

bits(-2)
```

Let's see that we can manually work out the bit-wise representation
of 5.25 and it matches what we came up with before in class:

```python
bits(5.25)
```

So that is $1.0101 \times 2^{1025-1023} = 1\times 2^{2} + 0\times 2^{1} + 1\times 2^{0} + 0\times 2^{-1} + 1\times 2^{-2}$, where the 2nd through 12th
bits are $10000000001$, which codes for $1\times 2^{10}+2^{0}=1025$.

!!! tip "Tip"
Given a fixed number of bits for a number, what is the
tradeoff between using bits for the $d$ part vs. bits for the $e$ part?
:::

Let's consider what can be represented exactly:

```python
dg(.1)
dg(.5)
dg(.25)
dg(.26)
dg(1/32)
dg(1/33)
```

So why is 0.5 stored exactly and 0.1 not stored exactly? By analogy,
consider the difficulty with representing 1/3 in base 10.

## Overflow and underflow

The magnitudes of the largest and smallest numbers we can represent are $2^{e_{\max}}$ and
$2^{e_{\min}}$ where $e_{\max}$ and $e_{\min}$ are the smallest and
largest possible values of the exponent. Let's consider the exponent and
what we can infer about the range of possible numbers. With 11 bits for
$e$, we can represent $2^{11}=2048$ different exponent values, $e \in \{0,1,2,\ldots,2047\}$.
So the largest number we could represent should have magnitude $2^{1024}$. What
is this in base 10?

```python
#| error: true
x = np.float64(10)
x**308
x**309

np.log10(2.0**1024)  # Just barely overflows.
np.log10(2.0**1023)

np.finfo(np.float64)
```

We could have been smarter about the calculation of $2^{1024}$ in base 10:
$\log_{10}2^{1024}=\log_{2}2^{1024}/\log_{2}10=1024/3.32\approx308$.

(Note that the reason that $2^{1024}$ overflows is that we need a way to represent infinity.)

The result is analogous for the smallest number, so we have that floating
points can range in magnitude between about $1\times10^{-308}$ and $1\times10^{308}$.
Producing
something larger or smaller in magnitude than these values is called
overflow and underflow respectively.

Let's see what happens when we underflow in numpy. Note that there is no warning.

```python
x**(-308)
x**(-330)
```

Something subtle happens for numbers like $10^{-309}$ through $10^{-323}$. They can actually be represented despite the fact that it doesn't seem like we should be able to represent numbers smaller than $2^{-1023} \approx 10^{-308}$. Investigating that may be an extra credit problem on a problem set.

## Integers or floats?

Values stored as integers should overflow if they exceed the maximum integer.

Should $2^{65}$ overflow?

```python
np.log2(np.iinfo(np.int64).max)
x = np.int64(2)
# Yikes!
x**64
```

Python's `int` type doesn't overflow.

```python
# Interesting:
print(2**64)
print(2**100)
```

Of course, doubles won't overflow until much larger values than 4- or 8-byte integers because we know they can be as big as $10^{308}$.

```python
x = np.float64(2)
dg(x**64, '.2f')
dg(x**100, '.2f')
```

However we need to think about
what integer-valued numbers can and can't be stored exactly in our base 2 representation of floating point numbers.
It turns out that integer-valued numbers can be stored exactly as doubles when their absolute
value is less than $2^{53}$.

!!! tip "Tip"
Why $2^{53}$? Write out what integers can be stored exactly in our base 2 representation of floating point numbers.
:::

You can force storage as integers or doubles in a few ways.

```python
x = 3; type(x)
x = np.float64(x); type(x)
x = 3.0; type(x)
x = np.float64(3); type(x)
```

## Precision

Consider our representation as (*S, d, e*) where we have $p=52$ bits for
$d$. Since we have $2^{52}\approx0.5\times10^{16}$, we can represent
about that many discrete values, which means we can accurately represent
about 16 digits (in base 10). The result is that floats on a computer
are actually discrete (we have a finite number of bits), and if we get a
number that is in one of the gaps (there are uncountably many reals),
it's approximated by the nearest discrete value. The accuracy of our
representation is to within 1/2 of the gap between the two discrete
values bracketing the true number. Let's consider the implications for
accuracy in working with large and small numbers. By changing $e$ we can
change the magnitude of a number. So regardless of whether we have a
very large or small number, we have about 16 digits of accuracy, since
the absolute spacing depends on what value is represented by the least
significant digit (the *ulp*, or *unit in the last place*) in $d$, i.e.,
the $p=52$nd one, or in terms of base 10, the 16th digit. Let's explore
this:

```python
#| tidy: false
# large vs. small numbers
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
but essentially equivalent definition to that given [previously](#machine-epsilon).
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

[← 1. Basic representations](01-1-basic-representations.md) · [Up: contents](index.md) · [3. Implications for calculations and comparisons →](03-3-implications-for-calculations-and-comparisons.md)
