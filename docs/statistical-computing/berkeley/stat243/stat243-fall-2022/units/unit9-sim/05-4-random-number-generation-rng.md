---
title: 4. Random number generation (RNG)
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit9-sim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Random number generation (RNG)

**Source:** [`units/unit9-sim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

At the core of simulations is the ability to generate random numbers,
and based on that, random variables. On a computer, our goal is to
generate sequences of pseudo-random numbers that behave like random
numbers but are replicable. The reason that replicability is important
is so that we can reproduce the simulation.

## Generating random uniforms on a computer

Generating a sequence of random standard uniforms is the basis for all
generation of random variables, since random uniforms (either a single
one or more than one) can be used to generate values from other
distributions. Most random numbers on a computer are pseudo-random. The
numbers are chosen from a deterministic stream of numbers that behave
like random numbers but are actually a finite sequence (recall that both
integers and real numbers on a computer are actually discrete and there
are finitely many distinct values), so it's actually possible to get
repeats. The seed of a RNG is the place within that sequence where you
start to use the pseudo-random numbers.

Many RNG methods are sequential congruential methods. The basic idea is
that the next value is $$u_{k}=f(u_{k-1},\ldots,u_{k-j})\mbox{mod}\,m$$
for some function, $f$, and some positive integer $m$ . Often $j=1$.
*mod* just means to take the remainder after dividing by $m$. One then
generates the random standard uniform value as $u_{k}/m$, which by
construction is in $[0,1]$.

Given the construction, such sequences are periodic if the subsequence
ever reappears, which is of course guaranteed because there is a finite
number of possible subsequence values given that all the $u_{k}$ values
are remainders of divisions by a fixed number . One key to a good random
number generator (RNG) is to have a very long period.

An example of a sequential congruential method is a basic linear
congruential generator: $$u_{k}=(au_{k-1})\mbox{mod}\,m$$ with integer
$a$, $m$, and $u_{i}$ values. Here the periodicity can't exceed $m-1$
(the method is set up so that we never get $u_{k}=0$ as this causes the
algorithm to break), so we only have $m-1$ possible values. The seed is
the initial state, $u_{0}$ - i.e., the point in the sequence at which we
start. By setting the seed you guarantee reproducibility since given a
starting value, the sequence is deterministic. In general $a$ and $m$
are chosen to be large, but of course they can't be too large if they
are to be represented as computer integers. The standard values of $m$
are Mersenne primes, which have the form $2^{p}-1$ (but these are not
prime for all $p$), with $m=2^{31}-1$ common. Here's an example of a
linear congruential sampler:

```r
n <- 100
a <- 171
m <- 30269
u <- rep(NA, n)
u[1] <- 7306
for(i in 2:n)
  u[i] <- (a * u[i-1]) %% m
u <- u/m
uFromR <- runif(n)
par(mfrow = c(2,2), mgp = c(1.8, 0.7, 0), mai = c(.5,.5,.3,.1))
plot(1:n, u, type = 'l')
plot(1:n, uFromR, type = 'l')
hist(u, nclass = 25)
hist(uFromR, nclass = 25)
```

A wide variety of different RNG have been proposed. Many have turned out
to have substantial defects based on tests designed to assess if the
behavior of the RNG mimics true randomness. Some of the behavior we want
to ensure is uniformity of each individual random deviate, independence
of sequences of deviates, and multivariate uniformity of subsequences.
One test of a RNG that many RNGs don't perform well on is to assess the
properties of $k$-tuples - subsequences of length $k$, which should be
independently distributed in the $k$-dimensional unit hypercube.
Unfortunately, linear congruential methods produce values that lie on a
simple lattice in $k$-space, i.e., the points are not selected from
$q^{k}$ uniformly spaced points, where $q$ is the the number of unique
values. Instead, points often lie on parallel lines in the hypercube.

Combining generators can yield better generators. The Wichmann-Hill is
an option in R and is a combination of three linear congruential
generators with $a=\{171,172,170\}$, $m=\{30269,30307,30323\}$, and
$u_{i}=(x_{i}/30269+y_{i}/30307+z_{i}/30323)\mbox{mod}\,1$ where $x$,
$y$, and $z$ are generated from the three individual generators. Let's
mimic the Wichmann-Hill manually:

```r
RNGkind("Wichmann-Hill")
set.seed(1)
saveSeed <- .Random.seed
uFromR <- runif(10)
a <- c(171, 172, 170)
m <- c(30269, 30307, 30323)
xyz <- matrix(NA, nr = 10, nc = 3)
xyz[1, ] <- (a * saveSeed[2:4]) %% m
for( i in 2:10)
	xyz[i, ] <- (a * xyz[i-1, ]) %% m
for(i in 1:10)
	print(c(uFromR[i],sum(xyz[i, ]/m)%%1))
## we should be able to recover the current value of the seed
xyz[10, ]
.Random.seed[2:4]
```

By default R uses something called the Mersenne twister, which is in the
class of generalized feedback shift registers (GFSR). The basic idea of
a GFSR is to come up with a deterministic generator of bits (i.e., a way
to generate sequences of 0s and 1s), $B_{i}$, $i=1,2,3,\ldots$. The
pseudo-random numbers are then determined as sequential subsequences of
length $L$ from $\{B_{i}\}$, considered as a base-2 number and dividing
by $2^{L}$ to get a number in $(0,1)$. In general the sequence of bits
is generated by taking $B_{i}$ to be the *exclusive or* $$i.e., 0+0 = 0;
0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0$$ summation of two previous bits further
back in the sequence where the lengths of the lags are carefully chosen.

#### Additional notes

Generators should give you the same sequence of random numbers, starting
at a given seed, whether you ask for a bunch of numbers at once, or
sequentially ask for individual numbers.

When one invokes a RNG without a seed, they generally have a method for
choosing a seed, often based on the system clock.

There have been some attempts to generate truly random numbers based on
physical randomness. One that is based on quantum physics is
<http://www.idquantique.com/true-random-number-generator/quantis-usb-pcie-pci.html>.
Another approach is based on lava lamps!

## RNG in R

We can change the RNG in R using *RNGkind()*. We can set the seed with
*set.seed()*. The seed is stored in *.Random.seed*. The first element
indicates the type of RNG (and the type of normal RV generator). The
remaining values are specific to the RNG. In the demo code, we've seen
that for Wichmann-Hill, the remaining three numbers are the current
values of $\{x,y,z\}$.

In R the default RNG is the Mersenne twister (`?RNGkind`), which is
considered to be state-of-the-art -- it has some theoretical support,
has performed reasonably on standard tests of pseudorandom numbers and
has been used without evidence of serious failure. Plus it's fast
(because bitwise operations are fast). In fact this points out one of
the nice features of R, which is that for something as important as
this, the default is generally carefully chosen by R's developers. The
particular Mersenne twister used has a periodicity of
$2^{19937}-1\approx10^{6000}$. Practically speaking this means that if
we generated one random uniform per nanosecond for 10 billion years,
then we would generate $10^{25}$ numbers, well short of the period. So
we don't need to worry about the periodicity! The seed for the Mersenne
twister is a set of 624 32-bit integers plus a position in the set,
where the position is `.Random.seed[2]`.

We can set the seed by passing an integer to *set.seed()*, which then
sets as many actual seeds as required for a given generator. Here I'll
refer to the integer passed to *set.seed()* as *the* seed. Ideally,
nearby seeds generally should not correspond to getting sequences from
the stream that are closer to each other than far away seeds. According
to Gentle (CS, p. 327) the input to *set.seed()* should be an integer,
$i\in\{0,\ldots,1023\}$ , and each of these 1024 values produces
positions in the RNG sequence that are "far away" from each other. I
don't see any mention of this in the R documentation for *set.seed()*
and furthermore, you can pass integers larger than 1023 to *set.seed()*,
so I'm not sure how much to trust Gentle's claim. More on generating
parallel streams of random numbers below.

So we get replicability by setting the seed to a specific value at the
beginning of our simulation. We can then set the seed to that same value
when we want to replicate the simulation.

```r
set.seed(1)
rnorm(10)
set.seed(1)
rnorm(10)
```


We can also save the state of the RNG and pick up where we left off. So
this code will pick where you had left off, ignoring what happened in
between saving to *savedSeed* and resetting.

```r
set.seed(1)
rnorm(5)
savedSeed <- .Random.seed
rnorm(5)
tmp <- sample(1:50, 2000, replace = TRUE)
.Random.seed <- savedSeed
rnorm(5)
```


In some cases you might want to reset the seed upon exit from a function
so that a user's random number stream is unaffected:

```r
f <- function(args) {
  oldseed <- .Random.seed
  ## other code
  .Random.seed <<- oldseed # note global assignment!
}
```


Note the need to reassign to the global variable *.Random.seed*.

*RNGversion()* allows you to revert to RNG from previous versions of R,
which is very helpful for reproducibility.

The RNGs in R generally return 32-bit (4-byte) integers converted to
doubles, so there are at most $2^{32}$ distinct values. This means you
could get duplicated values in long runs, but this does not violate the
comment about the periodicity because the two values after the two
duplicated numbers will not be duplicates of each other -- note there is
a distinction between the values as presented to the user and the values
as generated by the RNG algorithm.

One way to proceed if you're using both R and C is to have C use the R
RNG, calling the C functions that R uses under the hood, which are
located in the *Rmath* library. This way you have a consistent source of
random numbers and don't need to worry about issues with RNG in C. If
you call C from R, this should approach should also work (see details in
<http://statistics.berkeley.edu/computing/cpp>); you could also generate
all the random numbers you need in R and pass them to the C function.

Note that whenever a random number is generated, the software needs to
retain information about what has been generated, so this is an example
where a function must have a side effect not observed by the user. R
frowns upon this sort of thing, but it's necessary in this case.

## RNG in parallel

We can generally rely on the RNG in R to give a reasonable set of
values. One time when we want to think harder is when doing work with
RNG in parallel on multiple processors. The worst thing that could
happen is that one sets things up in such a way that every process is
using the same sequence of random numbers. This could happen if you
mistakenly set the same seed in each process, e.g., using
*set.seed(mySeed)* in R on every process. More details on parallel RNG
are given in Unit 6.

---

[← 3. Implementation of simulation studies](04-3-implementation-of-simulation-studies.md) · [Up: contents](index.md) · [5. Generating random variables →](06-5-generating-random-variables.md)
