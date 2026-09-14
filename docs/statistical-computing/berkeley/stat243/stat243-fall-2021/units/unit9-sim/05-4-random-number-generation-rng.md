---
title: 4 Random number generation (RNG)
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit9-sim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Random number generation (RNG)

**Source:** [`units/unit9-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

At the core of simulations is the ability to generate random numbers, and based on that, random variables. On a computer, our goal is to generate sequences of pseudo-random numbers that behave like random numbers but are replicable. The reason that replicability is important is so that we can reproduce the simulation.

### **4.1 Generating random uniforms on a computer**

Generating a sequence of random standard uniforms is the basis for all generation of random variables, since random uniforms (either a single one or more than one) can be used to generate values from other distributions. Most random numbers on a computer are pseudo-random. The numbers are chosen from a deterministic stream of numbers that behave like random numbers but are actually a finite sequence (recall that both integers and real numbers on a computer are actually discrete and there are finitely many distinct values), so it’s actually possible to get repeats. The seed of a RNG is the place within that sequence where you start to use the pseudo-random numbers.

Many RNG methods are sequential congruential methods. The basic idea is that the next value

is

_uk_ = _f_ ( _uk−_ 1 _, . . . , uk−j_ )mod _m_

for some function, _f_ , and some positive integer _m_ . Often _j_ = 1. _mod_ just means to take the remainder after dividing by _m_ . One then generates the random standard uniform value as _uk/m_ , which by construction is in [0 _,_ 1].

Given the construction, such sequences are periodic if the subsequence ever reappears, which is of course guaranteed because there is a finite number of possible subsequence values given that

11

all the _uk_ values are remainders of divisions by a fixed number . One key to a good random number generator (RNG) is to have a very long period.

An example of a sequential congruential method is a basic linear congruential generator:


with integer _a_ , _m_ , and _ui_ values. Here the periodicity can’t exceed _m −_ 1 (the method is set up so that we never get _uk_ = 0 as this causes the algorithm to break), so we only have _m −_ 1 possible values. The seed is the initial state, _u_ 0 - i.e., the point in the sequence at which we start. By setting the seed you guarantee reproducibility since given a starting value, the sequence is deterministic. In general _a_ and _m_ are chosen to be large, but of course they can’t be too large if they are to be represented as computer integers. The standard values of _m_ are Mersenne primes, which have the form 2<sup>_p_</sup> _−_ 1 (but these are not prime for all _p_ ), with _m_ = 2<sup>31</sup> _−_ 1 common. Here’s an example of a linear congruential sampler:

n <- 100 a <- 171 m <- 30269 u <- **rep** (NA, n) u[1] <- 7306 **for** (i **in** 2:n) u[i] <- (a * u[i-1]) %% m u <- u/m uFromR <- **runif** (n) **par** (mfrow = **c** (2,2)) **plot** (1:n, u, type = 'l') **plot** (1:n, uFromR, type = 'l') **hist** (u, nclass = 25) **hist** (uFromR, nclass = 25)

12


<!-- Start of picture text -->
0 20 40 60 80 0 20 40 60 80<br>1:n 1:n<br>Histogram of u Histogram of uFromR<br>0.0 0.4 0.8 0.0 0.4 0.8<br>u uFromR<br>0.8 0.8<br>u 0.4 0.4<br>uFromR<br>0.0 0.0<br>12<br>8<br>8<br>4<br>4<br>Frequency Frequency<br>0 0<br><!-- End of picture text -->

#### **Histogram of uFromR**

A wide variety of different RNG have been proposed. Many have turned out to have substantial defects based on tests designed to assess if the behavior of the RNG mimics true randomness. Some of the behavior we want to ensure is uniformity of each individual random deviate, independence of sequences of deviates, and multivariate uniformity of subsequences. One test of a RNG that many RNGs don’t perform well on is to assess the properties of _k_ -tuples - subsequences of length _k_ , which should be independently distributed in the _k_ -dimensional unit hypercube. Unfortunately, linear congruential methods produce values that lie on a simple lattice in _k_ -space, i.e., the points are not selected from _q_<sup>_k_</sup> uniformly spaced points, where _q_ is the the number of unique values. Instead, points often lie on parallel lines in the hypercube.

Combining generators can yield better generators. The Wichmann-Hill is an option in R and is a combination of three linear congruential generators with _a_ = _{_ 171 _,_ 172 _,_ 170 _}_ , _m_ = _{_ 30269 _,_ 30307 _,_ 30323 _}_ , and _ui_ = ( _xi/_ 30269 + _yi/_ 30307 + _zi/_ 30323)mod 1 where _x_ , _y_ , and _z_ are generated from the three individual generators. Let’s mimic the Wichmann-Hill manually:

13

**RNGkind** ("Wichmann-Hill") **set.seed** (1) saveSeed <- .Random.seed uFromR <- **runif** (10) a <- **c** (171, 172, 170) m <- **c** (30269, 30307, 30323) xyz <- **matrix** (NA, nr = 10, nc = 3) xyz[1, ] <- (a * saveSeed[2:4]) %% m **for** ( i **in** 2:10) xyz[i, ] <- (a * xyz[i-1, ]) %% m **for** (i **in** 1:10) **print** ( **c** (uFromR[i], **sum** (xyz[i, ]/m)%%1)) ## [1] 0.1297134 0.1297134 ## [1] 0.9822407 0.9822407 ## [1] 0.8267184 0.8267184 ## [1] 0.242355 0.242355 ## [1] 0.8568853 0.8568853 ## [1] 0.8408788 0.8408788 ## [1] 0.3421633 0.3421633 ## [1] 0.7062672 0.7062672 ## [1] 0.6212432 0.6212432 ## [1] 0.6537663 0.6537663 _## we should be able to recover the current value of the seed_ xyz[10, ] ## [1] 24279 14851 10966 .Random.seed[2:4] ## [1] 24279 14851 10966

By default R uses something called the Mersenne twister, which is in the class of generalized feedback shift registers (GFSR). The basic idea of a GFSR is to come up with a deterministic generator of bits (i.e., a way to generate sequences of 0s and 1s), _Bi_ , _i_ = 1 _,_ 2 _,_ 3 _, . . ._ . The pseudo-random numbers are then determined as sequential subsequences of length _L_ from _{Bi}_ , considered as a base-2 number and dividing by 2<sup>_L_</sup> to get a number in (0 _,_ 1). In general the sequence of bits is gen-

14

erated by taking _Bi_ to be the _exclusive or_ [i.e., 0+0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0] summation of two previous bits further back in the sequence where the lengths of the lags are carefully chosen.

**Additional notes** Generators should give you the same sequence of random numbers, starting at a given seed, whether you ask for a bunch of numbers at once, or sequentially ask for individual numbers.

When one invokes a RNG without a seed, they generally have a method for choosing a seed, often based on the system clock.

There have been some attempts to generate truly random numbers based on physical randomness. One that is based on quantum physics is http://www.idquantique.com/true-random-numbergenerator/quantis-usb-pcie-pci.html. Another approach is based on lava lamps!

### **4.2 RNG in R**

We can change the RNG in R using _RNGkind()_ . We can set the seed with _set.seed()_ . The seed is stored in _.Random.seed_ . The first element indicates the type of RNG (and the type of normal RV generator). The remaining values are specific to the RNG. In the demo code, we’ve seen that for Wichmann-Hill, the remaining three numbers are the current values of _{x, y, z}_ .

In R the default RNG is the Mersenne twister (?RNGkind), which is considered to be stateof-the-art – it has some theoretical support, has performed reasonably on standard tests of pseudorandom numbers and has been used without evidence of serious failure. Plus it’s fast (because bitwise operations are fast). In fact this points out one of the nice features of R, which is that for something as important as this, the default is generally carefully chosen by R’s developers. The particular Mersenne twister used has a periodicity of 2<sup>19937</sup> _−_ 1 _≈_ 10<sup>6000</sup> . Practically speaking this means that if we generated one random uniform per nanosecond for 10 billion years, then we would generate 10<sup>25</sup> numbers, well short of the period. So we don’t need to worry about the periodicity! The seed for the Mersenne twister is a set of 624 32-bit integers plus a position in the set, where the position is .Random.seed[2].

We can set the seed by passing an integer to _set.seed()_ , which then sets as many actual seeds as required for a given generator. Here I’ll refer to the integer passed to _set.seed()_ as _the_ seed. Ideally, nearby seeds generally should not correspond to getting sequences from the stream that are closer to each other than far away seeds. According to Gentle (CS, p. 327) the input to _set.seed()_ should be an integer, _i ∈{_ 0 _, . . . ,_ 1023 _}_ , and each of these 1024 values produces positions in the RNG sequence that are “far away” from each other. I don’t see any mention of this in the R documentation for _set.seed()_ and furthermore, you can pass integers larger than 1023 to _set.seed()_ , so I’m not sure how much to trust Gentle’s claim. More on generating parallel streams of random

15

numbers below.

So we get replicability by setting the seed to a specific value at the beginning of our simulation. We can then set the seed to that same value when we want to replicate the simulation.

**set.seed** (1) **rnorm** (10) ## [1] -1.12774688 0.94127649 1.06642978 -0.40656626 0.30874760 1.42146069 ## [7] -1.68323660 0.43367702 -0.01607178 -1.72752716 **set.seed** (1) **rnorm** (10) ## [1] -1.12774688 0.94127649 1.06642978 -0.40656626 0.30874760 1.42146069 ## [7] -1.68323660 0.43367702 -0.01607178 -1.72752716

We can also save the state of the RNG and pick up where we left off. So this code will pick where you had left off, ignoring what happened in between saving to _savedSeed_ and resetting.

**set.seed** (1) **rnorm** (5) ## [1] -1.1277469 0.9412765 1.0664298 -0.4065663 0.3087476 savedSeed <- .Random.seed **rnorm** (5) ## [1] 1.42146069 -1.68323660 0.43367702 -0.01607178 -1.72752716 tmp <- **sample** (1:50, 2000, replace = TRUE) .Random.seed <- savedSeed **rnorm** (5) ## [1] 1.42146069 -1.68323660 0.43367702 -0.01607178 -1.72752716

In some cases you might want to reset the seed upon exit from a function so that a user’s random number stream is unaffected:

16

f <- **function** (args) { oldseed <- .Random.seed _## other code_ .Random.seed <<- oldseed _# note global assignment!_ }

Note the need to reassign to the global variable _.Random.seed_ .

_RNGversion()_ allows you to revert to RNG from previous versions of R, which is very helpful for reproducibility.

The RNGs in R generally return 32-bit (4-byte) integers converted to doubles, so there are at most 2<sup>32</sup> distinct values. This means you could get duplicated values in long runs, but this does not violate the comment about the periodicity because the two values after the two duplicated numbers will not be duplicates of each other – note there is a distinction between the values as presented to the user and the values as generated by the RNG algorithm.

One way to proceed if you’re using both R and C is to have C use the R RNG, calling the C functions that R uses under the hood, which are located in the _Rmath_ library. This way you have a consistent source of random numbers and don’t need to worry about issues with RNG in C. If you call C from R, this should approach should also work (see details in http://statistics.berkeley.edu/computing/cpp); you could also generate all the random numbers you need in R and pass them to the C function.

Note that whenever a random number is generated, the software needs to retain information about what has been generated, so this is an example where a function must have a side effect not observed by the user. R frowns upon this sort of thing, but it’s necessary in this case.

### **4.3 RNG in parallel**

We can generally rely on the RNG in R to give a reasonable set of values. One time when we want to think harder is when doing work with RNG in parallel on multiple processors. The worst thing that could happen is that one sets things up in such a way that every process is using the same sequence of random numbers. This could happen if you mistakenly set the same seed in each process, e.g., using _set.seed(mySeed)_ in R on every process. More details on parallel RNG are given in Unit 7.

---

[← 3 Implementation of simulation studies](04-3-implementation-of-simulation-studies.md) · [Up: contents](index.md) · [5 Generating random variables →](06-5-generating-random-variables.md)
