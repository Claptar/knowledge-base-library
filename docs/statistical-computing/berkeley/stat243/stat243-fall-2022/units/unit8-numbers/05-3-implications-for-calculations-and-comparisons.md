---
title: 3. Implications for calculations and comparisons
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit8-numbers.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Implications for calculations and comparisons

**Source:** [`units/unit8-numbers.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Computer arithmetic is not mathematical arithmetic!

As mentioned for integers, computer number arithmetic is not closed,
unlike real arithmetic. For example, if we multiply two computer
floating points, we can overflow and not get back another computer
floating point. One term that is used, which might pop up in an error
message (though probably not in R) is that an "exception" is "thrown".

Another mathematical concept we should consider here is that computer
arithmetic does not obey the associative and distributive laws, i.e.,
$(a+b)+c$ may not equal $a+(b+c)$ on a computer and $a(b+c)$ may not be
the same as $ab+ac$. Here's an example with multiplication:


```r
val1 <- 1/10; val2 <- 0.31; val3 <- 0.57
res1 <- val1*val2*val3
res2 <- val3*val2*val1
identical(res1, res2)
dg(res1)
dg(res2)
```

## Calculating with integers vs. floating points

It's important to note that operations with integers are fast and exact
(but can easily overflow) while operations with floating points are
slower and approximate. Because of this slowness, floating point
operations (*flops*) dominate calculation intensity and are used as the
metric for the amount of work being done - a multiplication (or
division) combined with an addition (or subtraction) is one flop. We'll
talk a lot about flops in the unit on linear algebra.

## Comparisons

As we saw, we should never test `a==b` unless (1) *a* and *b* are
represented as integers in R, (2) they are integer-valued but stored as
doubles that are small enough that they can be stored exactly) or (3)
they are decimal numbers that have been created in the same way (e.g.,
`0.4-0.3==0.4-0.3` returns `TRUE` but `0.1==0.4-0.3` does not). Similarly we should be careful
about testing `a==0`. And be careful of greater than/less than
comparisons. For example, be careful of `x[ x < 0 ] <- NA` if what you
are looking for is values that might be *mathematically* less than zero,
rather than whatever is *numerically* less than zero.


```r
4L - 3L == 1L
4.0 - 3.0 == 1.0
4.1 - 3.1 == 1.0
```

One nice approach to checking for approximate equality is to make use of
*machine epsilon*. If the relative spacing of two numbers is less than
*machine epsilon*, then for our computer approximation, we say they are
the same. Here's an implementation that relies on the absolute spacing
being $x\epsilon$ (see above).


```r
a = 12345678123456781000
b = 12345678123456782000

approxEqual = function(a, b){
  if(abs(a - b) < .Machine$double.eps * abs(a + b))
    print("approximately equal") else print ("not equal")
}

approxEqual(a,b)

a = 1234567812345678
b = 1234567812345677

approxEqual(a,b)
```

Actually, we probably want to use a number slightly larger than
*.Machine\$double.eps* to be safe. You can also take a look at the R
function *all.equal.numeric()*.

Finally, in computing, we often encounter the use of an unusual integer
as a symbol for missing values. E.g., a datafile might store missing
values as -9999. Testing for this using == in R should generally be
ok:` x [ x == -9999 ] <- NA`, both because integers of this magnitude
are stored exactly and because the -9999 values would presumably have
been created in the same way. To be really careful, you can read in as
character type and do the assessment before converting to numeric.

## Calculations

Given the limited *precision* of computer numbers, we need to be careful
when in the following two situations.

1.  Subtracting large numbers that are nearly equal (or adding negative
    and positive numbers of the same magnitude). You won't have the
    precision in the answer that you would like. How many decimal places
    of accuracy do we have here?


    ```r
    # catastrophic cancellation w/ large numbers
    dg(123456781234.56 - 123456781234.00)
    ```

    The absolute error in the original numbers here is of the order
    $\epsilon x=2.2\times10^{-16}\cdot1\times10^{11}\approx1\times10^{-5}=.00001$.
    While we might think that the result is close to the value 1 and
    should have error of about machine epsilon, the relevant absolute
    error is in the original numbers, so we actually only have about
    five significant digits in our result because we cancel out the
    other digits.

    This is called *catastrophic cancellation*, because most of the
    digits that are left represent rounding error -- many of the significant
    digits have cancelled with each other.\
    Here's catastrophic cancellation with small numbers. The right
    answer here is exactly 0.000000000000000000001234.


    ```r
    # catastrophic cancellation w/ small numbers
    a = .000000000000123412341234
    b = .000000000000123412340000

    # so we know the right answer is .000000000000000000001234 EXACTLY

    dg(a-b, 35)
    ## [1] "0.00000000000000000000123399999315140"
    ```

    But the result is accurate only to 8 places + 20 = 28 decimal
    places, as expected from a machine precision-based calculation,
    since the "1" is in the 13th position, after 12 zeroes (12+16=28).
    Ideally, we would have accuracy to 36 places (16 digits + the 20
    zeroes), but we've lost 8 digits to catastrophic cancellation.

    It's best to do any subtraction on numbers that are not too large.
    For example, if we compute the sum of squares in a naive way, we can
    lose all of the information in the calculation because the
    information is in digits that are not computed or stored accurately:
    $$s^{2}=\sum x_{i}^{2}-n\bar{x}^{2}$$


    ```r
    ## No problem here:
    x <- c(-1, 0, 1)
    n <- length(x)
    sum(x^2)-n*mean(x)^2
    sum((x - mean(x))^2)

    ## Adding/subtracting a constant shouldn't change the result:
    x <- x + 1e8
    sum(x^2)-n*mean(x)^2  # the result of this is not good!
    sum((x - mean(x))^2)
    ```

    A good principle to take away is to subtract off a number similar in
    magnitude to the values (in this case $\bar{x}$ is obviously ideal)
    and adjust your calculation accordingly. In general, you can
    sometimes rearrange your calculation to avoid catastrophic
    cancellation. Another example involves the quadratic formula for
    finding a root (p. 101 of Gentle).

2.  Adding or subtracting numbers that are very different in magnitude.
    The precision will be that of the large magnitude number, since we
    can only represent that number to a certain absolute accuracy, which
    is much less than the absolute accuracy of the smaller number:


    ```r
    dg(123456781234.2)
    dg(123456781234.2 - 0.1)        # truth: 123456781234.1
    dg(123456781234.2 - 0.01)       # truth: 123456781234.19
    dg(123456781234.2 - 0.001)      # truth: 123456781234.199
    dg(123456781234.2 - 0.0001)     # truth: 123456781234.1999
    dg(123456781234.2 - 0.00001)    # truth: 123456781234.19999
    dg(123456781234.2 - 0.000001)   # truth: 123456781234.199999
    123456781234.2 - 0.000001 == 123456781234.2
    ```

    The larger number in the calculations above is of magnitude
    $10^{11}$, so the absolute error in representing the larger number
    is around $1\times10^{^{-5}}$. Thus in the calculations above we can
    only expect the answers to be accurate to about $1\times10^{-5}$. In
    the last calculation above, the smaller number is smaller than
    $1\times10^{-5}$ and so doing the subtraction has had no effect.
    This is analogous to trying to do $1+1\times10^{-16}$ and seeing
    that the result is still 1.\
    A work-around when we are adding numbers of very different
    magnitudes is to add a set of numbers in increasing order. However,
    if the numbers are all of similar magnitude, then by the time you
    add ones later in the summation, the partial sum will be much larger
    than the new term. A (second) work-around to that problem is to add
    the numbers in a tree-like fashion, so that each addition involves a
    summation of numbers of similar size.

Given the limited *range* of computer numbers, be careful when you are:

-   Multiplying or dividing many numbers, particularly large or small
    ones. Never take the product of many large or small numbers as this
    can cause over- or under-flow. Rather compute on the log scale and
    only at the end of your computations should you exponentiate. E.g.,
    $$\prod_{i}x_{i}/\prod_{j}y_{j}=\exp(\sum_{i}\log x_{i}-\sum_{j}\log y_{j})$$

Let's consider some challenges that illustrate that last concern.

-   Challenge: consider multiclass logistic regression, where you have
    quantities like this:
    $$p_{j}=\text{Prob}(y=j)=\frac{\exp(x\beta_{j})}{\sum_{k=1}^{K}\exp(x\beta_{k})}=\frac{\exp(z_{j})}{\sum_{k=1}^{K}\exp(z_{k})}$$
    for $z_{k}=x\beta_{k}$. What will happen if the $z$ values are very
    large in magnitude (either positive or negative)? How can we
    reexpress the equation so as to be able to do the calculation? Hint:
    think about multiplying by $\frac{c}{c}$ for a carefully chosen $c$.

-   Second challenge: The same issue arises in the following
    calculation. Suppose I want to calculate a predictive density (e.g.,
    in a model comparison in a Bayesian context): $$\begin{aligned}
    f(y^{*}|y,x) & = & \int f(y^{*}|y,x,\theta)\pi(\theta|y,x)d\theta\\
     & \approx & \frac{1}{m}\sum_{j=1}^{m}\prod_{i=1}^{n}f(y_{i}^{*}|x,\theta_{j})\\
     & = & \frac{1}{m}\sum_{j=1}^{m}\exp\sum_{i=1}^{n}\log f(y_{i}^{*}|x,\theta_{j})\\
     & \equiv & \frac{1}{m}\sum_{j=1}^{m}\exp(v_{j})\end{aligned}$$
    First, why do I use the log conditional predictive density? Second,
    let's work with an estimate of the unconditional predictive density
    on the log scale,
    $\log f(y^{*}|y,x)\approx\log\frac{1}{m}\sum_{j=1}^{m}\exp(v_{j})$.
    Now note that $e^{v_{j}}$ may be quite small as $v_{j}$ is the sum
    of log likelihoods. So what happens if we have terms something like
    $e^{-1000}$? So we can't exponentiate each individual $v_{j}$. This
    is what is known as the "log sum of exponentials" problem (and the
    solution as the "log-sum-exp trick"). Thoughts?

Numerical issues come up frequently in linear algebra. For example, they
come up in working with positive definite and semi-positive-definite
matrices, such as covariance matrices. You can easily get negative
numerical eigenvalues even if all the eigenvalues are positive or
non-negative. Here's an example where we use an squared exponential
correlation as a function of time (or distance in 1-d), which is
*mathematically* positive definite (i.e., all the eigenvalues are
positive) but not numerically positive definite:


```r
xs <- 1:100
dists <- fields::rdist(xs)
corMat <- exp(- (dists/10)^2) # this is a p.d. matrix (mathematically)
dg(eigen(corMat)$values[80:100])  # but not numerically
```

## Final note

How the computer actually does arithmetic with the floating point
representation in base 2 gets pretty complicated, and we won't go into
the details. These rules of thumb should be enough for our practical
purposes. Monahan and the URL reference have many of the gory details.

---

[← large vs. small numbers](04-large-vs-small-numbers.md) · [Up: contents](index.md)
