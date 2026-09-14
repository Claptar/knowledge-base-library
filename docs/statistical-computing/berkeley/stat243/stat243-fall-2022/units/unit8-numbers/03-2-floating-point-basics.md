---
title: 2. Floating point basics
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit8-numbers.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Floating point basics

**Source:** [`units/unit8-numbers.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Representing real numbers

Reals (also called floating points) are stored on the computer as an
approximation, albeit a very precise approximation. As an example, if we
represent the distance from the earth to the sun using a double, the
error is around a millimeter. However, we need to be very careful if
we're trying to do a calculation that produces a very small (or very
large number) and particularly when we want to see if numbers are equal
to each other.

If you run the code here, the results may surprise you.
```r
0.3 - 0.2 == 0.1
0.3
0.2
0.1 # Hmmm...

0.75 - 0.5 == 0.25
0.6 - 0.4 == 0.2
## any ideas what is different about those two comparisons?
```

Next, let's consider the number of digits of accuracy
we have for a variety of numbers.

```r
a <- 0.3
b <- 0.2
formatC(b, 20, format = 'f')
formatC(a, 20, format = 'f')
formatC(a - b, 20, format = 'f')
formatC(0.1, 20, format = 'f')
formatC(1/3, 20, format = 'f')
```

So empirically, it looks like we're accurate up to the 16th decimal place

But actually, the key is the number of digits, not decimal places.

```r
formatC(1234.1234, 20, format = 'f')
formatC(1234.123412341234, 20, format = 'f')
```

Let's return to our comparison, `0.75-0.5 == 0.25`.

```r
formatC(0.75, 20, format = 'f')
formatC(0.50, 20, format = 'f')
```

For our future explorations, let's define a wrapper function for convenience:

```r
dg <- function(x, digits = 20) formatC(x, digits, format = 'f')

## alternative to formatC:
sprintf("%0.20f", a)
```

Notice that we can represent the result accurately only up to 16
significant digits. This suggests no need to show more than 16
significant digits and no need to print out any more when writing to a
file (except that if the number is bigger than $10^{16}$ then we need
extra digits to correctly show the magnitude of the number if not using
scientific notation). And of course, often we don't need anywhere near
that many.

*Machine epsilon* is the term used for indicating the
(relative) accuracy of real numbers and it is defined as the smallest
float, $x$, such that $1+x\ne1$:


```r
dg(1e-16 + 1)
dg(1e-15 + 1)
dg(2e-16 + 1)
dg(.Machine$double.eps)
dg(.Machine$double.eps + 1)
```

#### Floating point representation

*Floating point* refers to the decimal point (or *radix* point since we'll
be working with base 2 and *decimal* relates to 10). Consider Avogadro's
number in terms of scientific notation: $+6.023\times10^{23}$. As a
baseline for what is about to follow note that we can express a decimal
number in the following expansion
$$6.03=6\times10^{0}+0\times10^{-1}+3\times10^{-2}$$ A real number on a
computer is stored in what is basically scientific notation:
$$\pm d_{0}.d_{1}d_{2}\ldots d_{p}\times b^{e}\label{eq:floatRep}$$
where $b$ is the base, $e$ is an integer and $d_{i}\in\{0,\ldots,b-1\}$.
$e$ is called the *exponent* and $d=d_{1}d_{2}\ldots d_{p}$ is called the *mantissa*.

Let's consider the choices that the computer pioneers needed to make
in using this system to represent numbers on a computer using base 2.
First, we need to choose the number of bits to represent $e$ so that we
can represent sufficiently large and small numbers. Second we need to
choose the number of bits, $p$, to allocate to
$d=d_{1}d_{2}\ldots d_{p}$, which determines the accuracy of any
computer representation of a real.

The great thing about floating points
is that we can represent numbers that range from incredibly small to
very large while maintaining good precision. The floating point *floats*
to adjust to the size of the number. Suppose we had only three digits to
use and were in base 10. In floating point notation we can express
$0.12\times0.12=0.0144$ as
$(1.20\times10^{-1})\times(1.20\times10^{-1})=1.44\times10^{-2}$, but if
we had fixed the decimal point, we'd have $0.120\times0.120=0.014$ and
we'd have lost a digit of accuracy. (Furthermore, we wouldn't be able
to represent numbers bigger than $0.99$.

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


```r
bits(2^(-1)) # 1/2
bits(2^0)  # 1
bits(2^1)  # 2
bits(2^1 + 2^0)  # 3
bits(2^2)  # 4

bits(-2)
```

**Question**: Given a fixed number of bits for a number, what is the
tradeoff between using bits for the $d$ part vs. bits for the $e$ part?

Let's consider what can be represented exactly:


```r
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

The largest and smallest numbers we can represent are $2^{e_{\max}}$ and
$2^{e_{\min}}$ where $e_{\max}$ and $e_{\min}$ are the smallest and
largest possible values of the exponent. Let's consider the exponent and
what we can infer about the range of possible numbers. With 11 bits for
$e$, we can represent $\pm2^{10}=\pm1024$ different exponent values (see
*.Machine\$double.max.exp*) (why is *.Machine\$double.min.exp* only
-1022? ). So the largest number we could represent is $2^{1024}$. What
is this in base 10?


```r
log10(2^1024) # whoops ... we've actually just barely overflowed
log10(2^1023)

.Machine$double.xmax
.Machine$double.xmin
```

We could have been smarter about that calculation:
$\log_{10}2^{1024}=\log_{2}2^{1024}/\log_{2}10=1024/3.32\approx308$. The
result is analogous for the smallest number, so we have that floating
points can range between $1\times10^{-308}$ and $1\times10^{308}$. Take
a look at *.Machine\$double.xmax* and *.Machine.double.xmin*. Producing
something larger or smaller in magnitude than these values is called
overflow and underflow respectively. When we overflow, R gives back an
Inf or -Inf (and in other cases we might get an error message). When we
underflow, we get back 0, which in particular can be a problem if we try
to divide by the value.

## Integers or floats?

Values stored as integers should overflow if they exceed
*.Machine\$integer.max*.

Should $2^{45}$ overflow?


```r
x <- 2^45
z <- 25
class(x)
class(z)
as.integer(x)
as.integer(z)

1e308
1e309

2^31
x <- 2147483647L
x
class(x)
x <- 2147483648L
class(x)
```

In R, numbers are generally stored as doubles. We've basically already
seen why - consider the maximum integer when using 4 bytes and the
maximum floating point value. Representing integers as floats isn't
generally a problem, in part because integers will be stored exactly in
base two provided the absolute value is less than $2^{53}$.

> *Challenge*: Why $2^{53}$? Write out what integers can be stored exactly in our base 2 representation of floating point numbers.

However, you can force storage as integers in a few ways: values
generated based on *seq()*, based on the : operator, specified with an
"L", or explicitly coerced:


```r
x <- 3; typeof(x)
x <- as.integer(3); typeof(x)
x <- 3L; typeof(x)
x <- 3:5; typeof(x)
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


```r

---

[← 1. Basic representations](02-1-basic-representations.md) · [Up: contents](index.md) · [large vs. small numbers →](04-large-vs-small-numbers.md)
