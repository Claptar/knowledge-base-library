---
title: "46. Floating-Point Numbers and Precision"
course: "Berkeley Stat 243"
chapter: 46
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 46. Floating-Point Numbers and Precision

## What this covers

This chapter answers a practical question for anyone writing numerical code: what actually
happens when a real number is stored in computer memory, and why does that make some perfectly
ordinary calculations misbehave — `0.3 - 0.2 == 0.1` coming out `False`, a sum of squares that
goes negative, a covariance matrix whose "positive" eigenvalues come out negative? It assumes only
basic familiarity with binary and hexadecimal notation and some exposure to Python/numpy; no prior
exposure to IEEE-754 is assumed.

## Bits, bytes, and integers

Everything stored in computer memory or on disk is, at bottom, bits: switches that are either on
or off, so everything is encoded in base 2. Eight bits make a byte, and since a byte has
$2^{8}=256$ possible values, it is often written more compactly as two base-16 (hexadecimal)
digits, e.g. `3e`, `a0`, `ba`. A file format is nothing more than a convention for how to interpret
the bytes in a file.

Two bytes (16 bits) can encode any unsigned integer from $0$ to $2^{16}-1=65535$. To also represent
negative numbers, one bit is spent on the sign — e.g. a 16-bit signed integer covers
$\pm(2^{15}-1)$. In practice, negative integers are not stored simply as sign-and-magnitude; they
use a binary encoding chosen so that ordinary addition circuitry works correctly (adding the bit
patterns for $-1$ and $1$ gives the bit pattern for $0$, with no special case needed).

Because a fixed number of bits can only represent finitely many values, computer integers are not
closed under arithmetic: multiplying two representable integers can silently overflow.

```python
a = np.int32(3423333)
a * a       # overflows

a = np.int64(3423333)
a * a       # doesn't overflow — more bits available
```

numpy gives no warning when this happens; `np.int64(34233332342343) ** 2` and
`np.int64(10000000000) ** 2` both silently wrap around. Python's own `int` type is
arbitrary-precision and never overflows this way, but at the cost of extra memory
(`sys.getsizeof` shows the footprint growing with the value) and losing the fixed-width layout
that makes array-based numerical computation fast. `np.iinfo(np.int32)` confirms the range
directly: the maximum 32-bit signed integer is $2^{31}-1=2147483647$; with the sign bit, that
covers $2\cdot2^{31}=2^{32}=(2^{8})^{4}$ values across 4 bytes of 8 bits each.

## Floating point: single and double precision

Real numbers need a different scheme, because unlike integers we want to trade range for precision
depending on the size of the number in play. In C — and hence in most of what Python/numpy is
built on — the standard representation is 8 bytes (64 bits), called *double precision*, or a
*double*. An older 4-byte format is *single precision*; it is still used on GPUs today for speed
and to save memory. The choice matters for memory footprint: an array of $10^{5}$ normal draws
takes noticeably less memory stored as `float32` or `float16` than as the default `float64`.

## Scientific notation and the IEEE-754 layout

A floating-point number is stored essentially in scientific notation,
$$\pm d_{0}.d_{1}d_{2}\ldots d_{p}\times b^{e},$$
where $b$ is the base, $e$ the exponent, and $d=d_{1}d_{2}\ldots d_{p}$ the *mantissa*. The
advantage over a fixed decimal point is that the representable numbers can range over many orders
of magnitude while keeping the same number of significant digits everywhere — the point *floats*
to the size of the number. With only three decimal digits and a fixed decimal point,
$0.120\times0.120=0.014$ already loses a digit of accuracy (and cannot represent anything above
$0.99$); letting the point float, $(1.20\times10^{-1})\times(1.20\times10^{-1})=1.44\times10^{-2}$
keeps all three digits.

Designing this representation means choosing, for a fixed total number of bits, how many go to the
exponent $e$ (controlling range) and how many go to the mantissa $d$ (controlling precision) — a
genuine trade-off, since more of one means less of the other.

The double-precision standard uses base 2 (arithmetic is faster in base 2 than base 10) and lays
out the 64 bits as
$$(-1)^{S}\times1.d\times2^{\,e-1023}=(-1)^{S}\times1.d_{1}d_{2}\ldots d_{52}\times2^{\,e-1023},$$
with 1 bit for the sign $S$, 11 bits for the exponent $e$ (so $e\in\{0,1,\ldots,2047\}$, and the
$-1023$ is a *bias* that plays the role a sign bit would otherwise play for the exponent), and the
remaining $52=64-1-11$ bits for the mantissa $d$.

<figure>
<svg viewBox="0 0 620 170" role="img" aria-label="Layout of the 64 bits of an IEEE-754 double precision number">
  <rect x="20" y="60" width="40" height="50" fill="currentColor" fill-opacity="0.25" stroke="currentColor" stroke-width="1.5"/>
  <rect x="60" y="60" width="160" height="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <rect x="220" y="60" width="380" height="50" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="90" text-anchor="middle" font-size="12" fill="currentColor">S</text>
  <text x="140" y="90" text-anchor="middle" font-size="12" fill="currentColor">e</text>
  <text x="410" y="90" text-anchor="middle" font-size="12" fill="currentColor">d1 d2 ... d52</text>
  <text x="40" y="45" text-anchor="middle" font-size="11" fill="currentColor">1 bit</text>
  <text x="140" y="45" text-anchor="middle" font-size="11" fill="currentColor">exponent, 11 bits</text>
  <text x="410" y="45" text-anchor="middle" font-size="11" fill="currentColor">mantissa, 52 bits</text>
  <text x="310" y="140" text-anchor="middle" font-size="12" fill="currentColor">value = (-1)^S x 1.d x 2^(e-1023)</text>
</svg>
<figcaption>The 64 bits of an IEEE-754 double: one sign bit, an 11-bit biased exponent, and a
52-bit mantissa interpreted as 1.d1d2...d52.</figcaption>
</figure>

The leading `1.` in $1.d$ is the *hidden bit*: it is always present for a nonzero number in this
normalized form and so need not be stored, and its presence guarantees that every representable
number has a unique encoding — without it, $1$ could equally be written $1.0\times2^{0}$,
$0.1\times2^{1}$, $0.01\times2^{2}$, and so on.

Worked example: $5.25$ in this scheme is $1.0101\times2^{2}$ — check it:
$1\times2^{2}+0\times2^{1}+1\times2^{0}+0\times2^{-1}+1\times2^{-2}=4+1+0.25=5.25$. The stored
exponent field encodes $2+1023=1025$, whose binary representation $10000000001$ occupies the
second through twelfth bits of the number.

## Why 0.1 is not exact but 0.5 is

Not every decimal fraction has a finite binary expansion — exactly the way $1/3$ has no finite
decimal expansion. $0.5=2^{-1}$ and $0.25=2^{-2}$ are exact in binary; $0.1$ and $0.26$ are not,
and are stored as the nearest representable double. This is why `0.3 - 0.2 == 0.1` is `False`
while `0.75 - 0.5 == 0.25` is `True`: the second calculation involves only numbers with exact
binary representations, the first does not.

## Range: overflow and underflow

With 11 exponent bits, doubles cover exponents up to about $2^{1024}$ in magnitude — using
$\log_{10}2^{1024}=1024/\log_{2}10\approx1024/3.32\approx308$, that is about $10^{308}$. Computing
a value like $10^{309}$ overflows (the reason $2^{1024}$ itself overflows is that the top of the
exponent range is reserved so that infinity can be represented). At the small end, magnitudes
below about $2^{-1023}\approx10^{-308}$ underflow to zero, with **no warning** in numpy.

Curiously, numbers as small as $10^{-309}$ through $10^{-323}$ can still be represented, even
though they are smaller than the smallest exponent seems to allow — left as an open exercise below.

Integers behave differently: `np.int64(2) ** 64` overflows, because 64-bit integers cap out well
below $2^{64}$, while Python's arbitrary-precision `int` computes `2**64` and even `2**100`
without difficulty, and a `float64` does not overflow until far beyond either, reaching up to
about $10^{308}$.

But floats and integers disagree in the other direction too: an *integer-valued* number stored as
a double is only guaranteed exact when its absolute value is below $2^{53}$ — because the double
has only $53$ bits of precision (52 stored plus the hidden bit), so once an integer needs more
than 53 bits to write down exactly, the double can no longer distinguish it from its neighbours.
(Why $2^{53}$ exactly? Work out which integers can be written exactly in the
$(-1)^{S}\times1.d\times2^{e-1023}$ layout above — see the exercises.)

## Precision, machine epsilon, and the ulp

With $p=52$ mantissa bits, there are about $2^{52}\approx0.5\times10^{16}$ distinct values
available for $d$ — which is why doubles carry about 16 significant (decimal) digits, *regardless
of magnitude*: changing the exponent $e$ moves the whole window of representable values up or
down, but the number of digits inside the window stays the same. So `1234.1234123412341234` is
accurate to only 16 total digits, not 16 decimal places, and `123412341234.123412341234` has
already used up its 16 digits before the decimal point even ends — the value simply is not any
more accurate than that, no matter how many further digits get printed.

The spacing between one representable double and the next, near a number of magnitude 1, is called
*machine epsilon* ($\epsilon$). Equivalently, $\epsilon$ is the smallest $x$ such that
$1+x\ne1$ in floating-point arithmetic. The gap between $1=1.00\ldots0\times2^{0}$ and the next
representable number $1.00\ldots01\times2^{0}$ is
$$\epsilon=1\times2^{-52}\approx2.2\times10^{-16}\qquad\text{(double precision)}.$$
(In single precision it is much larger, about $2^{-23}$.)

Because the mantissa is always normalized the same way, $\epsilon$ is not just the absolute
spacing near 1 — it is the *relative* spacing everywhere: the next representable number above any
$x$ is $(1+\epsilon)x$, so the relative gap is always $\epsilon$, while the *absolute* gap scales
with $x$, equal to $x\epsilon$. So near $x=2^{52}$ the spacing between adjacent doubles is
$2^{52}\times2^{-52}=1$; near $x=2^{53}$ it is $2$; near $x=2^{54}$ it is $4$ — doubling every time
the exponent increases by one. This absolute spacing at $x$ is called the *ulp* (unit in the last
place). At $x=10^{6}$, the absolute error from this rounding is about $x\epsilon\approx2\times10^{-10}$
— consistent with "16 significant digits": 6 digits before the decimal point leaves 10 after it.

## Computer arithmetic is not real arithmetic

Two consequences of finite precision are worth separating from the range/overflow issue above:

- **It is not closed.** Multiplying two representable floats can overflow, exactly as for
  integers.
- **It is not associative or distributive.** $(a+b)+c$ need not equal $a+(b+c)$, and $a(b+c)$ need
  not equal $ab+ac$, because each intermediate result is rounded to the nearest representable
  value before the next operation happens. Multiplying `1/10 * 0.31 * 0.57` in one order and
  `0.57 * 0.31 * 1/10` in the other can give bit-for-bit different answers.

This is also why integer arithmetic is treated as fast and exact while floating-point arithmetic is
treated as slower and approximate — the reason *flops* (floating point operations: one
multiply-or-divide paired with one add-or-subtract) are the standard unit for how much numerical
work a calculation does.

## When you may, and may not, test equality

Because of everything above, `x == y` is safe only when:

1. `x` and `y` are integers;
2. they are integer-valued doubles, both small enough (below $2^{53}$) to be stored exactly; or
3. they are decimals computed in *exactly* the same way, so any rounding is identical on both sides
   (`0.4-0.3 == 0.4-0.3` is `True`; `0.1 == 0.4-0.3` is not).

The same caution applies to `x == 0` and to `<`/`>` comparisons: `x[x < 0]` finds values that are
*numerically* negative, which is not always the same set as the values that are *mathematically*
negative.

A practical alternative is to test approximate equality using machine epsilon, scaled by the
magnitude of the numbers being compared (recall that the absolute spacing at $x$ is $x\epsilon$):

```python
def approx_equal(a, b):
    if abs(a - b) < np.finfo(np.float64).eps * abs(a + b):
        print("approximately equal")
    else:
        print("not equal")
```

In practice it is safer to use a threshold somewhat larger than machine epsilon itself. One case
where a plain `==` test on floats is fine is testing for a sentinel value used to code missing
data, e.g. `x[x == -9999] = np.nan` — an integer of that magnitude is well within the range that
doubles store exactly, though reading the column in as an integer or string and testing before
converting to a float is the more careful option.

## Catastrophic cancellation

Subtracting two nearly equal numbers destroys precision, because the error already present in
each operand (of size roughly $\epsilon x$, where $x$ is their magnitude) does not shrink when the
numbers are subtracted — it becomes a much larger fraction of the (small) answer. Concretely,
subtracting two numbers of magnitude $10^{11}$ carries an absolute error of about
$\epsilon\times10^{11}\approx10^{-5}$; a difference computed from such numbers is trustworthy to
only about 5 significant digits, however large the numbers were to begin with. The same thing
happens with small numbers: subtracting `0.000000000000123412340000` from
`0.000000000000123412341234` should give exactly `0.000000000000000000001234`, but because the
inputs are only accurate to 16 significant digits (counted from their leading nonzero digit), the
computed answer is correct only to about 8 of the digits that follow — the rest is rounding noise,
not signal. This is *catastrophic cancellation*: most of the digits remaining after the subtraction
are the leftovers of rounding error, not real information, because the significant digits that
mattered cancelled against each other.

A standard place this bites is a naive sum of squares,
$$s^{2}=\sum_i x_i^{2}-n\bar x^{2},$$
which is mathematically equal to $\sum_i(x_i-\bar x)^{2}$ but can behave very differently in
floating point. On $x=(-1,0,1)$ both formulas agree. But shift the data by adding a large constant,
say $10^{8}$, to every value — which changes neither the true sum of squared deviations nor
$\bar x$'s role in it — and the first formula falls apart, because $\sum x_i^{2}$ and $n\bar x^{2}$
are now two very large, very close numbers whose difference is buried in rounding error, while
$\sum(x_i-\bar x)^{2}$, which never forms those large intermediate quantities, is unaffected. The
general lesson: subtract off something of similar magnitude to the data before combining terms,
and rearrange a calculation to avoid ever forming — and then cancelling — two large near-equal
quantities. (The quadratic formula has the same disease when its two roots differ greatly in size;
see Gentle, p. 101.)

## Adding numbers of very different magnitudes

If two numbers differ enormously in size, the precision of their *sum* is limited by the precision
of the larger number, since the double can only place the smaller number's digits where the larger
number's ulp allows. Subtracting `0.000001` from `123456781234.2` — a number of magnitude
$10^{11}$, whose absolute error is already around $10^{-5}$ — has no detectable effect at all, for
the same reason that $1+10^{-16}$ still equals $1$ in double precision.

Two standard workarounds are useful when summing many terms of similar size, where later partial
sums grow to swamp new terms: add the numbers **in increasing order** (so no term is added into
something vastly bigger than itself until it has to be), or add them **in a tree-like (pairwise)
fashion**, so that every individual addition combines two numbers of comparable size.

## Products, and the log-sum-exp trick

The range problem shows up with products too: multiplying many large or many small numbers
together can overflow or underflow well before the true answer would, even though the true answer
is perfectly representable. The fix is to move to the log scale and only exponentiate — if at all
— at the very end:
$$\prod_i x_i \Big/ \prod_j y_j = \exp\Big(\sum_i \log x_i - \sum_j \log y_j\Big).$$
Often the calculation (maximizing a log-likelihood, for instance) never needs to leave the log
scale at all. Two concrete places this comes up — multiclass logistic regression, and averaging
likelihoods across posterior draws to get a predictive density — are posed as exercises below.

## Numerical positive-definiteness

Even linear algebra that is exact in theory can misbehave: a covariance-style matrix that is
*mathematically* positive definite (every eigenvalue strictly positive) can come out with small
negative eigenvalues once computed numerically. The example used is a squared-exponential
correlation matrix built from `exp(-(dists/10)**2)` for time points $0,\ldots,99$ — mathematically
positive definite, but `scipy.linalg.eigvals` applied to it returns some values in the tail of the
spectrum that are numerically negative.

## Exercises

1. For a fixed total number of bits split between the exponent $e$ and the mantissa $d$, what is
   the trade-off between giving more bits to one versus the other?
2. Working from the layout $(-1)^{S}\times1.d_{1}d_{2}\ldots d_{52}\times2^{e-1023}$, explain why
   an integer-valued double is stored exactly precisely when its absolute value is less than
   $2^{53}$, and write out which integers near that boundary are, and are not, representable
   exactly.
3. Why is $0.5$ represented exactly as a double while $0.1$ is not? (Compare with why $1/3$ has no
   finite decimal expansion.)
4. In multiclass logistic regression, $p_{j}=\dfrac{\exp(z_{j})}{\sum_{k=1}^{K}\exp(z_{k})}$. What
   goes wrong numerically if the $z_{k}$ are very large in magnitude, positive or negative, and how
   can multiplying numerator and denominator by a well-chosen $c/c$ fix it?
5. Suppose $v_{j}=\sum_{i=1}^{n}\log f(y_{i}^{*}\mid x,\theta_{j})$ for $j=1,\ldots,m$ posterior
   draws, and you want $\log\left(\frac{1}{m}\sum_{j}\exp(v_{j})\right)$ without ever forming
   $\exp(v_{j})$ directly (some $v_{j}$ may be as extreme as $-1000$). First, why work with the
   *log* conditional predictive density at all, rather than the density itself? Then, how do you
   evaluate the expression above safely?
6. Floating point should underflow to zero below about $2^{-1023}\approx10^{-308}$ in magnitude,
   yet numbers as small as $10^{-309}$ through $10^{-323}$ are still representable. What is being
   represented there, and why doesn't it contradict the range argument given above?

## Sources

- Basic representations, floating point basics, and implications for calculations and comparisons:
  Berkeley STAT 243 (statistical computing), Unit 8 ("Numbers"), fall-2024 and fall-2025
  offerings — the two are essentially identical; this chapter follows the fall-2025 text
  throughout, cross-checked against fall-2024. Files: `unit8-numbers/01-1-basic-representations.md`,
  `02-2-floating-point-basics.md`, `03-3-implications-for-calculations-and-comparisons.md` (both
  years), licensed CC BY 4.0.
- The lecture points to, but this chapter does not reproduce: Gentle, *Computational Statistics*,
  Ch. 2 (including the quadratic-formula cancellation example on p. 101); Monahan, *Numerical
  Methods of Statistics*, Ch. 2; and http://www.lahey.com/float.htm.
- Also supplied for this task were three files from Berkeley STAT 243's stat243-fall-2021
  offering, `unit8-bigData/01`-`03` (a few preparatory notes on "big data," Hadoop/MapReduce/
  Spark/Dask, and databases/SQL). In that year's syllabus, "Unit 8" covered big-data tooling
  rather than numeric representation — a different subject entirely, from before the unit's topic
  was changed in later years — so that material is not part of this chapter and is not used above.

---

[← 45. Preparatory Notes on Big Data](45-preparatory-notes-on-big-data.md) · [Contents](index.md) · [47. Simulation and Monte Carlo →](47-simulation-and-monte-carlo.md)
