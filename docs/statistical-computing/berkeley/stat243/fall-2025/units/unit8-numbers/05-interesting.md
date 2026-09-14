---
title: Interesting
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit8-numbers.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Interesting

**Source:** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit8-numbers.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

---

[← Yikes!](04-yikes.md) · [Up: contents](index.md) · [large vs. small numbers →](06-large-vs-small-numbers.md)
