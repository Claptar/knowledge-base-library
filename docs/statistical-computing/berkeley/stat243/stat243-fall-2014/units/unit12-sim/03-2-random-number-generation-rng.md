---
title: 2 Random number generation (RNG)
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit12-sim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Random number generation (RNG)

**Source:** [`units/unit12-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

At the core of simulations is the ability to generate random numbers, and based on that, random variables. On a computer, our goal is to generate sequences of pseudo-random numbers that behave like random numbers but are replicable. The reason that replicability is important is so that we can reproduce the simulation.

3

### **2.1 Generating random uniforms on a computer**

Generating a sequence of random standard uniforms is the basis for all generation of random variables, since random uniforms (either a single one or more than one) can be used to generate values from other distributions. Most random numbers on a computer are pseudo-random. The numbers are chosen from a deterministic stream of numbers that behave like random numbers but are actually a finite sequence (recall that both integers and real numbers on a computer are actually discrete and there are finitely many distinct values), so it’s actually possible to get repeats. The seed of a RNG is the place within that sequence where you start to use the pseudo-random numbers.

Many RNG methods are sequential congruential methods. The basic idea is that the next value

is


for some function, _f_ , and some positive integer _m_ . Often _j_ = 1. _mod_ just means to take the remainder after dividing by _m_ . One then generates the random standard uniform value as _uk/m_ , which by construction is in [0 _,_ 1].

Given the construction, such sequences are periodic if the subsequence ever reappears, which is of course guaranteed because there is a finite number of possible values given that all the values are remainders of divisions by a fixed number . One key to a good random number generator (RNG) is to have a very long period.

An example of a sequential congruential method is a basic linear congruential generator:


with integer _a_ , _m_ , and _ui_ values. Here the periodicity can’t exceed _m −_ 1 (the method is set up so that we never get _uk_ = 0 as this causes the algorithm to break), so we only have _m −_ 1 possible values. The seed is the initial state, _u_ 0 - i.e., the point in the sequence at which we start. By setting the seed you guarantee reproducibility since given a starting value, the sequence is deterministic. In general _a_ and _m_ are chosen to be large, but of course they can’t be too large if they are to be represented as computer integers. The standard values of _m_ are Mersenne primes, which have the form 2<sup>_p_</sup> _−_ 1 (but these are not prime for all _p_ ), with _m_ = 2<sup>31</sup> _−_ 1 common. Here’s an example of a linear congruential sampler:

n <- 100 a <- 171 m <- 30269 u <- **rep** (NA, n) u[1] <- 7306

4

**for** (i **in** 2:n) u[i] <- (a * u[i-1]) %% m u <- u/m uFromR <- **runif** (n) **par** (mfrow = **c** (2,2)) **plot** (1:n, u, type = 'l') **plot** (1:n, uFromR, type = 'l') **hist** (u, nclass = 25) **hist** (uFromR, nclass = 25)


<!-- Start of picture text -->
0 20 40 60 80 0 20 40 60 80<br>1:n 1:n<br>Histogram of u Histogram of uFromR<br>0.0 0.4 0.8 0.0 0.4 0.8<br>u uFromR<br>0.8 0.8<br>u 0.4 0.4<br>uFromR<br>0.0 0.0<br>8 8<br>4 4<br>Frequency Frequency<br>0 0<br><!-- End of picture text -->

#### **Histogram of uFromR**

A wide variety of different RNG have been proposed. Many have turned out to have substantial defects based on tests designed to assess if the behavior of the RNG mimics true randomness. Some of the behavior we want to ensure is uniformity of each individual random deviate, independence of sequences of deviates, and multivariate uniformity of subsequences. One test of a RNG that many RNGs don’t perform well on is to assess the properties of _k_ -tuples - subsequences of length _k_ , which should be independently distributed in the _k_ -dimensional unit hypercube. Unfortunately,

5

linear congruential methods produce values that lie on a simple lattice in _k_ -space, i.e., the points are not selected from _q_<sup>_k_</sup> uniformly spaced points, where _q_ is the the number of unique values. Instead, points often lie on parallel lines in the hypercube.

Combining generators can yield better generators. The Wichmann-Hill is an option in R and is a combination of three linear congruential generators with _a_ = _{_ 171 _,_ 172 _,_ 170 _}_ , _m_ = _{_ 30269 _,_ 30307 _,_ 30323 _}_ , and _ui_ = ( _xi/_ 30269 + _yi/_ 30307 + _zi/_ 30323)mod 1 where _x_ , _y_ , and _z_ are generated from the three individual generators. Let’s mimic the Wichmann-Hill manually:

**RNGkind** ("Wichmann-Hill") **set.seed** (0) saveSeed <- .Random.seed uFromR <- **runif** (10) a <- **c** (171, 172, 170) m <- **c** (30269, 30307, 30323) xyz <- **matrix** (NA, nr = 10, nc = 3) xyz[1, ] <- (a * saveSeed[2:4]) %% m **for** ( i **in** 2:10) xyz[i, ] <- (a * xyz[i-1, ]) %% m **for** (i **in** 1:10) **print** ( **c** (uFromR[i], **sum** (xyz[i, ]/m)%%1)) ## [1] 0.4625532 0.4625532 ## [1] 0.2658268 0.2658268 ## [1] 0.5772108 0.5772108 ## [1] 0.5107932 0.5107932 ## [1] 0.3375606 0.3375606 ## [1] 0.3575848 0.3575848 ## [1] 0.4130476 0.4130476 ## [1] 0.1329034 0.1329034 ## [1] 0.2549908 0.2549908 ## [1] 0.9202022 0.9202022 _# we should be able to recover the current value of the seed_ xyz[10, ] ## [1] 20696 2593 4576 .Random.seed[2:4] ## [1] 20696 2593 4576

6

By default R uses something called the Mersenne twister, which is in the class of generalized feedback shift registers (GFSR). The basic idea of a GFSR is to come up with a deterministic generator of bits (i.e., a way to generate sequences of 0s and 1s), _Bi_ , _i_ = 1 _,_ 2 _,_ 3 _, . . ._ . The pseudo-random numbers are then determined as sequential subsequences of length _L_ from _{Bi}_ , considered as a base-2 number and dividing by 2<sup>_L_</sup> to get a number in (0 _,_ 1). In general the sequence of bits is generated by taking _Bi_ to be the _exclusive or_ [i.e., 0+0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0] summation of two previous bits further back in the sequence where the lengths of the lags are carefully chosen.

**Additional notes** Generators should give you the same sequence of random numbers, starting at a given seed, whether you ask for a bunch of numbers at once, or sequentially ask for individual numbers.

When one invokes a RNG without a seed, they generally have a method for choosing a seed, often based on the system clock.

There have been some attempts to generate truly random numbers based on physical randomness. One that is based on quantum physics is http://www.idquantique.com/true-random-numbergenerator/quantis-usb-pcie-pci.html. Another approach is based on lava lamps!

### **2.2 RNG in R**

We can change the RNG in R using _RNGkind()_ . We can set the seed with _set.seed()_ . The seed is stored in _.Random.seed_ . The first element indicates the type of RNG (and the type of normal RV generator). The remaining values are specific to the RNG. In the demo code, we’ve seen that for Wichmann-Hill, the remaining three numbers are the current values of _{x, y, z}_ .

In R the default RNG is the Mersenne twister (?RNGkind), which is considered to be stateof-the-art – it has some theoretical support, has performed reasonably on standard tests of pseudorandom numbers and has been used without evidence of serious failure. Plus it’s fast (because bitwise operations are fast). In fact this points out one of the nice features of R, which is that for something as important as this, the default is generally carefully chosen by R’s developers. The particular Mersenne twister used has a periodicity of 2<sup>19937</sup> _−_ 1 _≈_ 10<sup>6000</sup> . Practically speaking this means that if we generated one random uniform per nanosecond for 10 billion years, then we would generate 10<sup>25</sup> numbers, well short of the period. So we don’t need to worry about the periodicity! The seed for the Mersenne twister is a set of 624 32-bit integers plus a position in the set, where the position is .Random.seed[2].

We can set the seed by passing an integer to _set.seed()_ , which then sets as many actual seeds as required for a given generator. Here I’ll refer to the integer passed to _set.seed()_ as _the_ seed. Ideally, nearby seeds generally should not correspond to getting sequences from the stream that are

7

closer to each other than far away seeds. According to Gentle (CS, p. 327) the input to _set.seed()_ should be an integer, _i ∈{_ 0 _, . . . ,_ 1023 _}_ , and each of these 1024 values produces positions in the RNG sequence that are “far away” from each other. I don’t see any mention of this in the R documentation for _set.seed()_ and furthermore, you can pass integers larger than 1023 to _set.seed()_ , so I’m not sure how much to trust Gentle’s claim. More on generating parallel streams of random numbers below.

So we get replicability by setting the seed to a specific value at the beginning of our simulation. We can then set the seed to that same value when we want to replicate the simulation.

**set.seed** (0) **rnorm** (10) ## [1] -0.09400361 0.19476306 -0.41913001 -0.21971226 -0.65886639 ## [6] -0.55565967 0.08172452 0.20598600 0.97703169 -0.07111146 **set.seed** (0) **rnorm** (10) ## [1] -0.09400361 0.19476306 -0.41913001 -0.21971226 -0.65886639 ## [6] -0.55565967 0.08172452 0.20598600 0.97703169 -0.07111146

We can also save the state of the RNG and pick up where we left off. So this code will pick where you had left off, ignoring what happened in between saving to _savedSeed_ and resetting.

**set.seed** (0) **rnorm** (5) ## [1] -0.09400361 0.19476306 -0.41913001 -0.21971226 -0.65886639 savedSeed <- .Random.seed tmp <- **sample** (1:50, 2000, replace = TRUE) .Random.seed <- savedSeed **rnorm** (5) ## [1] -0.55565967 0.08172452 0.20598600 0.97703169 -0.07111146

In some cases you might want to reset the seed upon exit from a function so that a user’s random number stream is unaffected:

8

f = **function** (args) { oldseed <- .Random.seed _# other code_ .Random.seed <<- oldseed }

Note the need to reassign to the global variable _.Random.seed_ .

_RNGversion()_ allows you to revert to RNG from previous versions of R, which is very helpful for reproducibility.

The RNGs in R generally return 32-bit (4-byte) integers converted to doubles, so there are at most 2<sup>32</sup> distinct values. This means you could get duplicated values in long runs, but this does not violate the comment about the periodicity because the two values after the two duplicated numbers will not be duplicates of each other – note there is a distinction between the values as presented to the user and the values as generated by the RNG algorithm.

One way to proceed if you’re using both R and C is to have C use the R RNG, calling the C functions that R uses under the hood, which are located in the _Rmath_ library. This way you have a consistent source of random numbers and don’t need to worry about issues with RNG in C. If you call C from R, this should approach should also work (see details in http://statistics.berkeley.edu/computing/cpp); you could also generate all the random numbers you need in R and pass them to the C function.

Note that whenever a random number is generated, the software needs to retain information about what has been generated, so this is an example where a function must have a side effect not observed by the user. R frowns upon this sort of thing, but it’s necessary in this case.

### **2.3 Random slippage**

If the exact floating point representations of a random number sequence differ, even in the 14th, 15th, 16th decimal places, if you run a simulation long enough, such a difference can be enough to change the result of some conditional calculation. Suppose your code involves:

> if(x>0) { do one thing } else{ do something different }

As soon as a small difference changes the result of testing _x>0_ , the remainder of the simulation can change entirely. This happened to me in my thesis as a result of the difference of an AMD and Intel processor, and took a while to figure out.

### **2.4 RNG in parallel**

We can generally rely on the RNG in R to give a reasonable set of values. One time when we want to think harder is when doing work with RNG in parallel on multiple processors. The worst

9

thing that could happen is that one sets things up in such a way that every process is using the same sequence of random numbers. This could happen if you mistakenly set the same seed in each process, e.g., using _set.seed(mySeed)_ in R on every process.

#### **2.4.1 The naive approach**

The naive approach is to use a different seed for each process. E.g., if your processes are numbered id=1,. . . ,p, with _id_ unique to a process, using set.seed(id) on each process. This is likely not to cause problems, but raises the danger that two (or more sequences) might overlap. For an algorithm with dependence on the full sequence, such as an MCMC, this probably won’t cause big problems (though you likely wouldn’t know if it did), but for something like simple simulation studies, some of your ’independent’ samples could be exact replicates of a sample on another process.

#### **2.4.2 The clunky but effective approach**

One approach to avoid the problem is to do all your RNG on one process and distribute the random deviates to the other processes, but this can be infeasible with many random numbers.

#### **2.4.3 The sophisticated approach**

More generally to avoid this problem, the key is to use an algorithm that ensures sequences that do not overlap. In R, there are two packages that deal with this, _rlecuyer_ and _rsprng_ . We’ll go over _rlecuyer_ , as I’ve heard that rsprng is deprecated (though there is no evidence of this on CRAN) and _rsprng_ is (at the moment) not available for the Mac.

The L’Ecuyer algorithm has a period of 2<sup>191</sup> , which it divides into subsequences of length 2<sup>127</sup> . Here’s how you initialize independent sequences on different processes when using the _parallel_ package’s parallel apply functionality (illustrated here with _parSapply()_ .

**require** (parallel) _## Loading required package: parallel_ **require** (rlecuyer) _## Loading required package: rlecuyer_ nSims <- 250 testFun <- **function** (i){ val <- **runif** (1)

10

**return** (val) } nCores <- 4 **RNGkind** () ## [1] "Wichmann-Hill" "Inversion" cl <- **makeCluster** (nCores) iseed <- 0 **clusterSetRNGStream** (cl = cl, iseed = iseed) **RNGkind** () _# clusterSetRNGStream sets RNGkind as L'Ecuyer-CMRG_ ## [1] "Wichmann-Hill" "Inversion" _# but it doesn't show up here on the master_ res <- **parSapply** (cl, 1:nSims, testFun) **clusterSetRNGStream** (cl = cl, iseed = iseed) res2 <- **parSapply** (cl, 1:nSims, testFun) **identical** (res,res2) ## [1] TRUE **stopCluster** (cl) If you want to explicitly move from stream to stream, you can use _nextRNGStream()_ example: **RNGkind** ("L'Ecuyer-CMRG") seed <- 0 **set.seed** (seed) _## now start M workers_ s <- .Random.seed **for** (i **in** 1:M) { s <- **nextRNGStream** (s) _# now send s to worker i as .Random.seed_ }

If you want to explicitly move from stream to stream, you can use _nextRNGStream()_ . For example:

When using _mclapply()_ , you can use the _mc.set.seed_ argument as follows (note that _mc.set.seed_ is TRUE by default, so you should get different seeds for the different processes by default), but one

11

needs to invoke RNGkind("L’Ecuyer-CMRG") to get independent streams via the L’Ecuyer algorithm.

**require** (parallel) **require** (rlecuyer) **RNGkind** ("L'Ecuyer-CMRG") res <- **mclapply** ( **seq_len** (nSims), testFun, mc.cores = nSlots, mc.set.seed = TRUE) _# this also seems to auotmatically reset the seed when it is run_ res2 <- **mclapply** ( **seq_len** (nSims), testFun, mc.cores = nSlots, mc.set.seed = TRUE) **identical** (res,res2)

The documentation for _mcparallel()_ gives more information about reproducibility based on _mc.set.seed_ .

#### **With foreach**

**Getting independent streams** One question is whether _foreach_ deals with RNG correctly. This is not documented, but the developers (Revolution Analytics) are well aware of RNG issues. Digging into the underlying code reveals that the _doMC_ and _doParallel_ backends both invoke _mclapply()_ and set _mc.set.seed_ to TRUE by default. This suggests that the discussion above r.e. _mclapply()_ holds for _foreach_ as well, so you should do RNGkind("L’Ecuyer-CMRG") before your foreach call. For _doMPI_ , as of version 0.2, you can do something like this, which uses L’Ecuyer behind the scenes:

cl <- makeCluster(nSlots) setRngDoMPI(cl, seed=0)

**Ensuring reproducibility** While using _foreach_ as just described should ensure that the streams on each worker are are distinct, it does not ensure reproducibility because task chunks may be assigned to workers differently in different runs and the substreams are specific to workers, not to tasks.

For _doMPI_ , you can specify a different RNG substream for each task chunk in a way that ensures reproducibility. Basically you provide a list called _.options.mpi_ as an argument to _foreach_ , with _seed_ as an element of the list:

12

nslaves <- 4 **library** (doMPI, quietly = TRUE) _## ## Attaching package: ’Rmpi’ ## ## The following object is masked from ’package:rlecuyer’: ## ## .onUnload_ cl <- **startMPIcluster** (nslaves) ## 4 slaves are spawned successfully. 0 failed. **registerDoMPI** (cl) result <- **foreach** (i = 1:20, .options.mpi = **list** (seed = 0)) %dopar% { out <- **mean** ( **rnorm** (1000)) } result2 <- **foreach** (i = 1:20, .options.mpi = **list** (seed = 0)) %dopar% { out <- **mean** ( **rnorm** (1000)) } **identical** (result, result2) ## [1] TRUE

That single seed then initializes the RNG for the first task, and subsequent tasks get separate substreams, using the L’Ecuyer algorithm, based on _nextRNGStream()_ . Note that the _doMPI_ developers also suggest using the _chunkSize_ option (also specified as an element of _.options.mpi_ ) when using _seed_ . See ?”doMPI-package” for more details.

For other backends, such as _doParallel_ , there is a package called _doRNG_ that ensures that _foreach_ loops are reproducible. Here’s how you do it:

**rm** (result, result2) nCores <- 4 **library** (doRNG, quietly = TRUE) _## Loading required package: methods ## Loading required package: pkgmaker ## Loading required package: registry_

13

**library** (doParallel) **registerDoParallel** (nCores) result <- **foreach** (i = 1:20, .options.RNG = 0) %dorng% { out <- **mean** ( **rnorm** (1000)) } result2 <- **foreach** (i = 1:20, .options.RNG = 0) %dorng% { out <- **mean** ( **rnorm** (1000)) } **identical** (result, result2) ## [1] TRUE Alternatively, you can do: **rm** (result, result2) **library** (doRNG, quietly = TRUE) **library** (doParallel) **registerDoParallel** (nCores) **registerDoRNG** (seed = 0) result <- **foreach** (i = 1:20) %dopar% { out <- **mean** ( **rnorm** (1000)) } **registerDoRNG** (seed = 0) result2 <- **foreach** (i = 1:20) %dopar% { out <- **mean** ( **rnorm** (1000)) } ## Warning in selectChildren(ac, 1): error ’Interrupted system call’ in select **identical** (result,result2) ## [1] TRUE

14

---

[← 1 Monte Carlo considerations](02-1-monte-carlo-considerations.md) · [Up: contents](index.md) · [3 Generating random variables →](04-3-generating-random-variables.md)
