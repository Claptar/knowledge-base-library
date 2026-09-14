---
title: 4. Random number generation (RNG)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit9-sim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit9-sim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Random number generation (RNG)

**Source:** [`units/unit9-sim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit9-sim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

At the core of simulations is the ability to generate random numbers,
and based on that, random variables. On a computer, our goal is to
generate sequences of pseudo-random numbers that behave like random
numbers but are replicable. The reason that replicability is important
is so that we can reproduce the simulation.

## Generating random uniforms on a computer

Generating a sequence of random standard uniforms is the basis for all
generation of random variables, since random uniforms (either a single
one or more than one) can be used to generate values from other
distributions. Most random numbers on a computer are *pseudo-random*. The
numbers are chosen from a deterministic stream of numbers that behave
like random numbers but are actually a finite sequence (recall that both
integers and real numbers on a computer are actually discrete and there
are finitely many distinct values), so it's actually possible to get
repeats. The seed of a RNG is the place within that sequence where you
start to use the pseudo-random numbers.

### Sequential congruential generators

Many RNG methods are sequential congruential methods. The basic idea is
that the next value is $$u_{k}=f(u_{k-1},\ldots,u_{k-j})\mbox{mod}\,m$$
for some function, $f$, and some positive integer $m$ . Often $j=1$.
*mod* just means to take the remainder after dividing by $m$. One then
generates the random standard uniform value as $u_{k}/m$, which by
construction is in $[0,1]$. For our discussion below, it is important
to distinguish the *state* ($u$) from the output of the RNG.

Given the construction, such sequences are periodic if the subsequence
ever reappears, which is of course guaranteed because there is a finite
number of possible subsequence values given that all the $u_{k}$ values
are remainders of divisions by a fixed number . One key to a good random
number generator (RNG) is to have a very long period.

An example of a sequential congruential method is a basic linear
congruential generator: $$u_{k}=(au_{k-1}+c)\mbox{mod}\,m$$ with integer
$a$, $m$, $c$, and $u_{k}$ values. (Note that in some cases $c=0$, in which case the periodicity can't exceed $m-1$ as the method is then set up so that we never get $u_{k}=0$ as this causes the
algorithm to break.) The seed is
the initial state, $u_{0}$ - i.e., the point in the sequence at which we
start. By setting the seed you guarantee reproducibility since given a
starting value, the sequence is deterministic. In general $a$, $c$ and $m$
are chosen to be 'large'. The standard values of $m$
are Mersenne primes, which have the form $2^{p}-1$ (but these are not
prime for all $p$). Here's an example of a
linear congruential sampler (with $c=0$):

```python
n = 100
a = 171
m = 30269

u = np.empty(n)
u[0] = 7306

for i in range(1, n):
    u[i] = (a * u[i-1]) % m

u = u / m
uFromNP = np.random.uniform(size = n)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(range(1, n+1), u)
plt.title("manual")
plt.xlabel("Index"); plt.ylabel("Value")

plt.subplot(2, 2, 2)
plt.plot(range(1, n+1), uFromNP)
plt.title("numpy")
plt.xlabel("Index"); plt.ylabel("Value")

plt.subplot(2, 2, 3)
plt.hist(u, bins=25)
plt.xlabel("Value"); plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.hist(uFromNP, bins=25)
plt.xlabel("Value"); plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
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

### PCG generators

Somewhat recently [O'Neal (2014) proposed a new approach](https://www.pcg-random.org/pdf/hmc-cs-2014-0905.pdf) to using the linear congruential generator in a way that gives much better performance than the basic versions of such generators described above. This approach is now the default random number generator in numpy (see `numpy.random.default_rng()`), called the [PCG-64 generator](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64). 'PCG' stands for permutation congruential generator and encompasses a family of such generators.

The idea of the PCG approach goes like this:

  - Linear congruential generators (LCG) are simple and fast, but for small values of $m$ don't perform all that well statistically, in particular having values on a lattice as discussed above.
  - Using a large value of $m$ can actually give good statistical performance.
  - Applying a technique called  *permutation functions* to the state of the LCG in order to produce the output at each step (the random value returned to the user) can improve the statistical performance even further.

Instead of using relatively small values of $m$ seen above, in the PCG approach one uses $m=2^k$, for 'large enough' $k$, usually 64 or 128. It turns out that if $m=2^k$ then the period of the $b$th bit of the state is $2^b$ where $b=1$ is the right-most bit. Small periods are of course bad for RNG, so the bits with small period cause the LCG to not perform well. Thankfully, one simple fix is simply to discard some number of the right-most bits (this is one form of *bit shift*). Note that if one does this, the output of the RNG is based on a subset of the bits, which means that the number of unique values that can be generated is smaller than the period. This is not a problem given we start with a state with a large number of bits (64 or 128 as mentioned above).

O'Neal then goes further; instead of simply discarding bits, she proposes to either shift bits by a random amount or rotate bits by a random amount, where the random amount is determined by a small number of the initial bits. This improves the statistical performance of the generator. The choice of how to do this gives the various members of the PCG family of generators. The details are fairly complicated (the PCG paper is 50-odd pages) and not important for our purposes here.

### Mersenne Twister

A commonly used generator (including in both R and Python) is the Mersenne Twister.
It's the default in R and "sort of" the default in numpy (see next section for what I mean by "sort of").

The Mersenne Twister has some theoretical support,
has performed reasonably on standard tests of pseudorandom numbers and
has been used without evidence of serious failure. (But note that O'Neal criticizes it in
[her technical report](https://www.pcg-random.org/pdf/hmc-cs-2014-0905.pdf).) Plus it's fast
(because bitwise operations are fast).  The
particular Mersenne twister used has a periodicity of
$2^{19937}-1\approx10^{6000}$. Practically speaking this means that if
we generated one random uniform per nanosecond for 10 billion years,
then we would generate $10^{25}$ numbers, well short of the period. So
we don't need to worry about the periodicity! The state (sometimes also called the seed) for the Mersenne
twister is a set of 624 32-bit integers plus a position in the set,
where the position is `.Random.seed[2]` in R and (I think) `np.random.get_state()[2]` in Python.

The Mersenne twister is in the class of generalized feedback shift registers (GFSR). The basic idea of
a GFSR is to come up with a deterministic generator of bits (i.e., a way
to generate sequences of 0s and 1s), $B_{i}$, $i=1,2,3,\ldots$. The
pseudo-random numbers are then determined as sequential subsequences of
length $L$ from $\{B_{i}\}$, considered as a base-2 number and dividing
by $2^{L}$ to get a number in $(0,1)$. In general the sequence of bits
is generated by taking $B_{i}$ to be the *exclusive or* $$i.e., 0+0 = 0;
0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0$$ summation of two previous bits further
back in the sequence where the lengths of the lags are carefully chosen.

numpy provides access to the Mersenne Twister via the `MT19937` generator;
more on this below. It looks like PCG-64 only became available as of numpy version 1.17.

### The period versus the number of unique values generated

The output of the PCG-64 is 64 bits while for the Mersenne Twister the output is 32 bits.
The result is that the generators generate fewer unique values than their periods.
This means you could get duplicated values in long runs, but this does not violate the
comment about the periodicity of PCG-64 and Mersenne-Twister being longer than $2^{64}$ and $2^{32}$.
Why not? Because the two values after the two
duplicated numbers will not be duplicates of each other -- as noted previously, there is
a distinction between the output presented to the user and the state of
the RNG algorithm.

### The seed and the state

Setting the seed picks a position in the periodic sequence of the RNG,
i.e., in the state of the RNG. The state can be a single number or something
much more complicated. As mentioned above, the state for the Mersenne Twister
is a set of 624 32-bit integers plus a position in the set. For the PCG-64
in numpy, the state is two numbers -- the actual state and the increment (`c` above).
This means that when the user passes a single number as the seed, there
needs to be a procedure that deterministically sets the state based on
that single number seed. The details of this are not usually well-documented
or viewable by the user.

Ideally, nearby seeds generally should not correspond to getting sequences from
the RNG stream that are closer to each other than far away seeds.
According to Gentle (CS, p. 327) the input to `set.seed()` in R should be an integer,
$i\in\{0,\ldots,1023\}$ , and each of these 1024 values produces
positions in the RNG sequence that are "far away" from each other. I
don't see any mention of this in the R documentation for `set.seed()`
and furthermore, you can pass integers larger than 1023 to `set.seed()`,
so I'm not sure how much to trust Gentle's claim. More on generating
parallel streams of random numbers below.

When one invokes a RNG without a seed, RNG implementations generally have a method for
choosing a seed (often based on the system clock). The numpy documentation
says that it "mixes sources of entropy in a reproducible way" to do this.

Generators should give you the same sequence of random numbers, starting
at a given seed, whether you ask for a bunch of numbers at once, or
sequentially ask for individual numbers.

#### Additional notes

There have been some attempts to generate truly random numbers based on
physical randomness. One that is based on quantum physics is
<http://www.idquantique.com/true-random-number-generator/quantis-usb-pcie-pci.html>.
Another approach is based on lava lamps!

## RNG in Python

### Choosing a generator

In numpy, the *default_rng* RNG is PCG-64. It has a period of $2^{128}$ and supports
advancing an arbitrary number of steps, as well
as $2^{127}$ streams (both useful for generating random numbers when parallelizing). The state of the PCG-64 RNG is represented by two
128-bit unsigned integers, one the actual state and one the value of $c$ (the *increment*).

However, while the *default* is PCG-64, simply
using the functions available via `np.random` to generate random numbers
seems to actually use the Mersenne Twister, so the meaning of *default*
is tricky.

I think that this text from `help(np.random)` explains what is going on:

```
   Legacy
   ------

   For backwards compatibility with previous versions of numpy before 1.17, the
   various aliases to the global `RandomState` methods are left alone and do not
   use the new `Generator` API.
```

We can change to a specific RNG using syntax (the `Generator` API) like this:

```python
#| eval: false
rng = np.random.Generator(np.random.MT19937(seed = 1))  # Mersenne Twister
rng = np.random.Generator(np.random.PCG64(seed = 1))    # PCG-64
```
but below note that there is a simpler way to change to the PCG-64.

Then to use that generator when doing operations that generate random numbers, we need
to use methods accessed via the `Generator` object (`rng` here):

```python
#| eval: false
rng.random.normal(size = 3)     # Now generate based on chosen generator.
## np.random.normal(size = 3)   # This will NOT use the chosen generator.
```

In R, the default RNG is the Mersenne twister (`?RNGkind`).

### Using the Mersenne Twister


If we simply start using numpy or scipy to generate random numbers,
we'll be using the Mersenne Twister. I believe this is what the
documentation mentioned above means by "aliases to the global `RandomState` methods".

We get replicability by setting the seed to a specific value at the
beginning of our simulation. We can then set the seed to that same value
when we want to replicate the simulation.

```python
np.random.seed(1)
np.random.normal(size = 5)
np.random.seed(1)
np.random.normal(size = 5)
```

We can also save the state of the RNG and pick up where we left off. So
this code will pick where you had left off, ignoring what happened in
between saving to `saved_state` and resetting.

```python
np.random.seed(1)
np.random.normal(size = 5)
saved_state = np.random.get_state()
np.random.normal(size = 5)
```

Now we'll do some arbitrary work with random numbers, and see that if we use the saved state
we can pick up where we left off above.
```python
tmp = np.random.choice(np.arange(1, 51), size=2000, replace=True) # arbitrary work

## Restore the state.
np.random.set_state(saved_state)
np.random.normal(size = 5)
```

If we look at `saved_state`, we can confirm it actually corresponds to the Mersenne
Twister.

### Using PCG64

To use the PCG-64, we need to explicitly create and
make use of the `Generator` object (`rng` here), which is the new numpy
approach to handling RNG.

We set the seed  when setting up the generator via `np.random.default_rng(seed)`
(or `np.random.Generator(np.random.PCG64(seed = 1))`).

```python
rng = np.random.default_rng(seed = 1)
rng.normal(size = 5)
rng = np.random.default_rng(seed = 1)
rng.normal(size = 5)
saved_state = rng.bit_generator.state
rng.normal(size = 5)
tmp = rng.choice(np.arange(1, 51), size=2000, replace=True)
rng.bit_generator.state = saved_state
rng.normal(size = 5)

saved_state
saved_state['state']['state']   # actual state
saved_state['state']['inc']     # increment ('c')
```

`saved_state` contains the actual state and the value of `c`, the increment.

Question: how many bits does `saved_state['state']['state']` correspond to?

## RNG in parallel

We can generally rely on the RNG in Python and R to give reasonable set of
pseudo-random values. One time when we want to think harder is when doing work with
RNG in parallel on multiple processors. The worst thing that could
happen is that one sets things up in such a way that every process is
using the same sequence of random numbers. This could happen if you
mistakenly set the same seed in each process, e.g., using
`np.random.seed(1)` on every process. Numpy now provides some nice functionality
for parallel RNG, with more details given in the [SCF parallelization tutorial](https://berkeley-scf.github.io/tutorial-parallelization/parallel-python#5-random-number-generation-rng-in-parallel).

---

[← 3. Implementation of simulation studies](04-3-implementation-of-simulation-studies.md) · [Up: contents](index.md) · [5. Generating random variables →](06-5-generating-random-variables.md)
