---
title: "47. Simulation and Monte Carlo"
course: "Berkeley Stat 243"
chapter: 47
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 47. Simulation and Monte Carlo

## What this covers

A simulation study asks a computer to answer a question that is too hard to answer by algebra: the
bias of an estimator under model misspecification, the true coverage of a confidence interval, how a
robust procedure compares with the MLE under heavy-tailed errors. These are expectations with no
closed form, so they are estimated by generating many pseudo-random datasets and averaging a
statistic across them. This chapter covers what such an estimate actually is and how precise it is
for a given amount of computing (Monte Carlo error); how to design and run a simulation study so the
answer is trustworthy and reproducible; how the pseudo-random numbers underneath it are generated,
and why the seed, the internal state, and parallel streams matter; and the standard devices — inverse
CDF, rejection sampling, importance sampling — for turning uniform draws into draws from an arbitrary
target distribution. It assumes basic probability (expectation, variance, the law of large numbers)
and enough linear algebra to recognize a Cholesky factorization.

## Monte Carlo estimation

### A motivating example: regression under the wrong model

Take ordinary linear regression, $Y=(y_1,\ldots,y_n)$, design matrix $X$, and
$\hat\beta=(X^\top X)^{-1}X^\top Y$. Under the standard assumptions $EY=X\beta$,
$\mathrm{Var}(Y)=\sigma^2I$, everything about $\hat\beta$ is closed-form:

$$E\hat\beta=\beta,\qquad \mathrm{Var}(\hat\beta)=\sigma^2(X^\top X)^{-1},\qquad
\mathrm{MSPE}(Y^*)=E\big((Y^*-\hat Y)^2\big)=\sigma^2\big(1+X^{*\top}(X^\top X)^{-1}X^*\big),$$

for a new observation $Y^*$ predicted from $X^*$. But if the mean is not linear in $X$, or the errors
are not independent and homoscedastic (they never quite are — the question is how far from the truth
the assumption is), or the estimator has been modified to be robust to outliers, none of this is
available anymore. The fix: generate $m$ datasets $Y_1,\ldots,Y_m$ from a distribution $f$ encoding
the departure of interest, compute $\hat\beta_i$ from each, and average:

$$\hat E(\hat\beta)=\bar{\hat\beta}=\frac{1}{m}\sum_{i=1}^m\hat\beta_i,\qquad
\widehat{\mathrm{Var}}(\hat\beta)=\frac{1}{m}\sum_{i=1}^m(\hat\beta_i-\bar{\hat\beta})^2.$$

The rest of this chapter is about what it takes to do this properly.

### Monte Carlo basics

The general object of interest is $\phi\equiv E_f(h(Y))$ for $Y\sim f$. Taking $h$ to be an indicator
recovers probabilities: for scalar $Y$, $p=P(Y\le y)=F(y)=\int I(t\le y)f(t)\,dt=E_f(I(Y\le y))$.
Variances and MSEs come from letting $h$ involve squared terms. Given an iid sample $Y_1,\ldots,Y_m$,

$$\hat\phi=\frac{1}{m}\sum_{i=1}^m h(Y_i),$$

justified by the law of large numbers, $\lim_{m\to\infty}\frac1m\sum h(Y_i)=E_fh(Y)$. In most
simulation studies $Y$ is an entire simulated dataset, not a scalar: $Y_i=(Y_{i1},\ldots,Y_{in})$ for
a dataset of size $n$, and the "iid sample" means $m$ independently generated datasets.

Back in the regression example: for bias, $\phi=E\hat\beta$, $h(Y)=\hat\beta(Y)$. For variance,
$\phi=\mathrm{Var}(\hat\beta)$, $h(Y)=(\hat\beta-E\hat\beta)^2$ — and the Monte Carlo estimate of
$E\hat\beta$ has to be plugged in to get $\widehat{\mathrm{Var}}(\hat\beta)$. For the coverage of a
confidence interval, $h(Y)=1_{\beta\in CI(Y)}$ and $\hat\phi=\frac1m\sum_i 1_{\beta\in CI(y_i)}$
should land near $1-\alpha$ for a nominal $100(1-\alpha)\%$ interval. Coverage that comes out too low
can mean either of two things: the estimated uncertainty is too small, or the point estimator is
biased.

### Simulation uncertainty: what precision does $m$ buy

$\hat\phi$ is an average of $m$ iid values $h(Y_1),\ldots,h(Y_m)$, so $\mathrm{Var}(\hat\phi)=\sigma^2/m$
with $\sigma^2=\mathrm{Var}(h(Y))=E_f((h(Y)-\phi)^2)$, estimated by

$$\hat\sigma^2=\frac{1}{m-1}\sum_{i=1}^m(h(Y_i)-\hat\phi)^2,\qquad
\widehat{\mathrm{Var}}(\hat\phi)=\frac{\hat\sigma^2}{m}=\frac{1}{m(m-1)}\sum_{i=1}^m(h(Y_i)-\hat\phi)^2.$$

If $\hat\phi$ is itself $\widehat{\mathrm{Var}}(\hat\beta)$, this is
$\widehat{\mathrm{Var}}(\widehat{\mathrm{Var}}(\hat\beta))$ — a variance of a variance, which reads
oddly but is exactly what it says. The simulation variance is $O(1/m)$: $m^2$ in the denominator
against a sum of $m$ terms. What makes this setting unusual is that the randomness is entirely under
your control, generated on demand — so in principle the simulation error can be driven as low as
desired, just by raising $m$; the catch is the usual $\sqrt m$ rate, so quartering the error costs a
sixteen-fold increase in replicates.

> This is the uncertainty in a simulation-based *estimate* of some quantity, not the statistical
> uncertainty of the original problem. Reporting $\widehat{\mathrm{Var}}(\hat\beta)$ without its own
> simulation standard error conflates the two.

Concrete instances of this second-order uncertainty in the regression example: uncertainty in the
estimated bias, $\widehat{\mathrm{Var}}(\hat E(\hat\beta)-\beta)$; in the estimated variance,
$\widehat{\mathrm{Var}}(\widehat{\mathrm{Var}}(\hat\beta))$; in the estimated MSPE,
$\widehat{\mathrm{Var}}(\widehat{\mathrm{MSPE}}(Y^*))$ — every reported quantity needs its own
$\widehat{\mathrm{Var}}()$.

One caveat: if the $Y_i$ are generated *dependently* (sequential Monte Carlo, MCMC), this variance
estimator no longer holds, since the samples are not iid — but $\hat\phi$ remains a valid, unbiased
estimator of $\phi$ regardless.

### Variance reduction (optional)

Importance sampling (below) is one variance-reduction tool; control variates and antithetic sampling
are two more, not developed here. Where natural strata exist with known probabilities, estimating
within each stratum and combining removes the variability due to how many draws land in each one.

*Rao-Blackwellization* has a clean derivation. For $E(h(X))$ with $X=\{X_1,X_2\}$, iterated
expectation gives $E(h(X))=E(E(h(X)\mid X_2))$. If $E(h(X)\mid X_2)=\int h(x_1,x_2)f(x_1\mid x_2)\,dx_1$
is available analytically, there is no reason to simulate the $X_1$ draw at all — only $X_2$ needs
simulating, giving

$$\hat\mu_{RB}=\frac{1}{m}\sum_{i=1}^m E(h(X)\mid X_{2,i}),$$

averaged over simulated $X_2$ (drawn from its marginal, or by drawing $X$ jointly and discarding
$X_1$). This strictly reduces variance: each term contributes $\mathrm{Var}(E(h(X)\mid X_2))$ rather
than $\mathrm{Var}(h(X))$, and the iterated-variance identity
$V(X)=E(V(X\mid Y))+V(E(X\mid Y))\Rightarrow V(E(X\mid Y))<V(X)$ guarantees the inequality.

## Designing a simulation study

A simulation study is an experiment and deserves the same design discipline as any other.

### The basic steps

1. Specify exactly how one simulated dataset is generated, given fixed inputs (sample size,
   distribution(s), parameters, statistic of interest).
2. Decide which inputs to vary; each unique combination of values is a *scenario*.
3. Write code carrying out one experiment, returning the quantity of interest, with the varying
   inputs as arguments.
4. For each scenario, repeat $m$ times — an embarrassingly parallel computation in both the
   replicate and the scenario dimensions.
5. Summarize each scenario's results, quantifying simulation uncertainty.
6. Report the results, graphically or in tables.

Comparing several methods means repeating steps 3–6 for each.

### Practical considerations

Let the structure of a *real* dataset — distributional assumptions, parameter values, dependence,
outliers, random effects, sample size $n$ — guide which of these become input variables. A common
setup fixes the data-generating context and compares methods within it (e.g. MLE vs. robust
estimator), with the "treatment variable" being the method and the outputs indexed as $Y_{ijklq}$:
$q$ for treatment, $j,k,l$ for other inputs (say, $t$ vs. normal errors, a parameter value, sample
size), $i\in\{1,\ldots,m\}$ for the replicate.

Because simulation is cheap, $m$ can often be made large enough to drive the simulation error to
essentially zero. To check whether this has happened, compute the simulation standard error
(typically $s/\sqrt m$) and compare it against the effect sizes under discussion — this matters most
when reporting a bias, since a "significant" bias smaller than its own simulation error is not a
finding. Choosing $m$ can be framed as a power calculation, but since more replicates are always
available, it is often simpler to proceed sequentially and stop once precision is adequate.

**Common random numbers.** When comparing methods, reuse the *same* simulated datasets across every
treatment level and analyze in a way that controls for the dataset — a paired comparison, pairing on
the dataset, removes that variability from the error term. The trick generalizes further: the same
random numbers can be reused across different data-generating mechanisms entirely. To compare
sensitivity to $t$-distributed versus normal errors, generate the normal deviates as usual, then
produce the $t$ deviates by pushing the *same* uniform quantiles through the $t$ quantile function
rather than drawing an independent $t$ sample:

```r
devs <- rnorm(100)
tdevs <- qt(pnorm(devs), df = 1)
plot(devs, tdevs); abline(0, 1)
```

`pnorm(devs)` recovers the quantile level behind each normal draw; `qt(...)` re-expresses that same
level as a $t$ deviate. The two datasets differ only in distributional shape, not in which draw
produced each observation, so a paired comparison sees only the effect of the distributional change.

### Experimental design (optional)

Varying one input at a time is inefficient — ordinary experimental design applies here. The usual
strategy discretizes each input into a few levels and, if the grid is small enough, runs a full
factorial (three inputs at three levels each gives $3^3$ combinations). Once the factorial is too
large, a *fractional factorial* omits combinations in a structured way: high-order interactions
become aliased to (confounded with) lower-order effects, in exchange for a design small enough to run
while still recovering main effects and perhaps two-way interactions. Interpret results via the
decomposition of sums of squares rather than significance — in most simulation settings every input
has *some* effect, so "no effect" is a straw-man null; the useful question is magnitude.

For very many inputs, a *Latin hypercube* design samples efficiently: treat each input as
$\mathcal U(0,1)$, divide the unit interval into $m$ bins per input, and independently randomize the
bin order and within-bin position for each input; combining across inputs spreads $m$ points evenly
over every one-dimensional projection. Explicit experimental design for a simulation study is
uncommon even among statisticians, but worth considering.

## Implementing a simulation study

### Computational efficiency

Simulation studies are embarrassingly parallel — each replicate to a different processor, results
collected afterward, with speedup scaling roughly with the processor count. Where a loop is
unavoidable and slow, C/C++ linked in is another route, not covered here.

R's `expand.grid()` builds the scenario grid directly, and `replicate()` repeats an expression a fixed
number of times in place of an explicit loop:

```r
require(fields)
thetaLevels <- c("low", "med", "hi"); n <- c(10, 100, 1000); tVsNorm <- c("t", "norm")
levels <- expand.grid(thetaLevels, tVsNorm, n)

## replicate(): generate m datasets of correlated normals
set.seed(1)
genFun <- function(n, theta = 1) {
  u <- rnorm(n); x <- runif(n)
  Cov <- exp(-rdist(x) / theta); U <- chol(Cov)
  return(cbind(x, crossprod(U, u)))
}
simData <- replicate(20, genFun(100, 1))
dim(simData)   # 100 obs by {x,y} by 20 replicates -> [1] 100 2 20
```

(Python's `itertools.product` plays the role of `expand.grid()` for the scenario grid:
`list(itertools.product(thetaLevels, tVsNorm, n))`.)

### Analysis and reporting

A plot often communicates a multi-scenario comparison better than a table; trellis/facetted plots
(`facet_wrap` in ggplot2, or seaborn/plotly equivalents) are usually the right tool for showing how
results vary across two or more inputs at once.

Set the seed once, at the start, so the whole run can be reproduced, and save the RNG state whenever
interim results are saved — this lets a long run (especially MCMC) restart from exactly where it left
off, random stream included. For reproducibility more broadly, post the simulation code (and, where
feasible, the data) publicly, so someone else can reproduce the results exactly, seed and all. The
American Statistical Association's guidance is explicit about what this means:

> "Articles reporting results based on computation should provide enough information so that readers
> can evaluate the quality of the results. Such information includes estimated accuracy of results,
> as well as descriptions of pseudorandom-number generators, numerical algorithms, programming
> languages, and major software components used."

## Random number generation

### Pseudo-randomness, the seed, and the state

A sequence of random standard uniforms underlies every other generated random variable. Numbers
produced this way are *pseudo-random*: a deterministic, finite, repeating stream that behaves like
randomness (integers and floats on a computer take only finitely many distinct values). The *seed* is
the position in that deterministic sequence at which generation begins; the *state* is the full
internal information the generator carries forward, which can be far richer than a single number.
Distinguishing state from the output shown to the user matters for what follows.

### Linear congruential and combined generators

Many generators are *sequential congruential methods*: $x_k=f(x_{k-1},\ldots,x_{k-j})\bmod m$ for
some $f$ and integer $m$ (often $j=1$), with $u_k=x_k/m\in[0,1]$. Since only finitely many remainders
mod $m$ exist, the sequence must eventually repeat; a long period is one mark of a good generator.
The basic *linear congruential generator* (LCG) is

$$x_k=(a\,x_{k-1}+c)\bmod m,$$

(with $c=0$, the algorithm is set up to avoid $x_k=0$, capping the period at $m-1$). The seed is the
initial state $x_0$: fixing it fixes the whole future sequence, which is what reproducibility
requires. Standard choices take $a,c,m$ large, with $m$ often a Mersenne prime, $2^p-1$:

```python
n, a, m = 100, 171, 30269
x = np.empty(n); x[0] = 7306
for i in range(1, n):
    x[i] = (a * x[i-1]) % m
u = x / m                                     # manual LCG output
rng = np.random.default_rng(seed=1)
uFromNP = rng.uniform(size=n)                 # numpy's generator, for comparison
```

A good RNG needs more than a long period: individual deviates should be uniform, sequences of them
independent, and $k$-tuples uniformly distributed over the $k$-dimensional unit hypercube. Plain LCGs
typically fail this last test — the $k$-tuples fall on a small number of parallel lines (a lattice)
rather than filling the hypercube.

Combining generators helps. R's *Wichmann–Hill* combines three LCGs, $a=\{171,172,170\}$,
$m=\{30269,30307,30323\}$, emitting $u_i=(x_i/30269+y_i/30307+z_i/30323)\bmod 1$ from the three
component states $x,y,z$:

```r
RNGkind("Wichmann-Hill"); set.seed(1)
saveSeed <- .Random.seed                # seed determines initial state
uFromR <- runif(10)
a <- c(171, 172, 170); m <- c(30269, 30307, 30323)
u <- rep(0, 10)
xyz <- matrix(NA, 10, 3)                # state of the RNG
xyz[1, ] <- (a * saveSeed[2:4]) %% m
u[1] <- sum(xyz[1, ] / m) %% 1
for (i in 2:10) {
  xyz[i, ] <- (a * xyz[i-1, ]) %% m     # update state
  u[i] <- sum(xyz[i, ] / m) %% 1        # emit pseudo-random value
}
## u agrees with uFromR; xyz[10,] recovers .Random.seed[2:4]
```

### PCG generators

O'Neal (2014) proposed PCG ("permutation congruential generator"), now numpy's default
(`np.random.default_rng()`). LCGs are simple and fast but, at the small $m$ used historically,
statistically weak (the lattice problem above); a much larger $m$ is statistically better on its own.
For $m=2^k$ ($k=64$ or $128$), the $b$-th bit of the state (from the right, $b=1$) has period exactly
$2^b$ — the low-order bits cycle fast and are the weak link. The simple fix discards some low-order
bits before output (a bit shift), which reduces the number of distinct outputs below the period but
is harmless once the underlying state is 64–128 bits wide. PCG goes further, shifting or rotating the
output bits by an amount itself determined by a few of the state's initial bits, improving statistical
performance further; the different ways of doing this shift/rotate give the various PCG family
members.

### The Mersenne Twister

R's long-standing default, and numpy's before PCG-64, is the Mersenne Twister: theoretically
supported, good on standard randomness tests, fast (bitwise operations), used without evidence of
serious failure (though O'Neal's paper is critical of it relative to PCG). It is a *generalized
feedback shift register* (GFSR): a deterministic bit sequence $B_1,B_2,\ldots$, each $B_i$ the
exclusive-or of two earlier bits at carefully chosen lags, with output uniforms formed from
length-$L$ subsequences read as base-2 integers divided by $2^L$. Its period is
$2^{19937}-1\approx10^{6000}$ — generating one uniform per nanosecond for ten billion years would
produce only $10^{25}$ numbers, nowhere near exhausting it. Its state is 624 32-bit integers plus a
position within that set.

### Period versus number of unique output values

PCG-64 emits 64-bit output, the Mersenne Twister 32-bit, so both generate *fewer distinct output
values* than their period — long runs can show duplicate outputs. This does not contradict the
periods above: the state carries more information than the output, so the values immediately *after*
a pair of duplicate outputs will not themselves be duplicates, since the underlying state differs
even when the emitted value coincides.

### The seed and the state, in practice

Setting the seed fixes a position in the state sequence, and that state can be a single number or
something far more elaborate — 624 32-bit integers plus a position for the Mersenne Twister; two
128-bit unsigned integers (state and increment $c$) for PCG-64. Passing a single integer as "the
seed" requires the generator to expand it internally, by an undocumented procedure, into the full
state. Ideally nearby seeds should not land near each other in the output stream; Gentle's
*Computational Statistics* claims R's `set.seed()` is designed so integers $i\in\{0,\ldots,1023\}$
land "far apart," though R's own documentation says nothing of this and larger integers are accepted
without complaint. A generator invoked with no explicit seed falls back on some entropy source
(numpy: "mixes sources of entropy in a reproducible way"). A well-behaved generator gives the same
sequence from a given seed whether numbers are requested all at once or one at a time.

### RNG in Python and R

`np.random.default_rng()` uses PCG-64: period $2^{128}$, jump-ahead by an arbitrary number of steps,
and $2^{127}$ separate streams (useful for parallel work, next). The legacy top-level functions
(`np.random.normal()` and similar, bypassing a `Generator` object) use the Mersenne Twister instead,
for backward compatibility with numpy before 1.17; R's default remains the Mersenne Twister
(`?RNGkind`). To use PCG-64 explicitly, create a `Generator` and call its methods — the top-level
`np.random` functions ignore it:

```python
rng = np.random.default_rng(seed=1)
rng.normal(size=5)
saved_state = rng.bit_generator.state
rng.normal(size=5)
tmp = rng.choice(np.arange(1, 51), size=2000, replace=True)   # arbitrary work
rng.bit_generator.state = saved_state
rng.normal(size=5)                       # picks up exactly where saved_state left off
```

`saved_state['state']['state']` and `['inc']` are the actual PCG-64 state and increment $c$. R's
analogue is the vector `.Random.seed` (first element: which generator; the rest, generator-specific —
three values for Wichmann–Hill, above). A function that uses random numbers internally can restore
the caller's stream on exit, keeping its randomness invisible to the caller:

```r
f <- function(args) {
  oldseed <- .Random.seed
  ## ... code that calls rnorm(), runif(), etc. ...
  .Random.seed <<- oldseed    # global assignment, restoring the caller's stream
}
```

### RNG in parallel

A single process's generator can generally be trusted. Parallel execution across processes needs real
care: the worst outcome is every process silently sharing the *same* stream, which happens if the
same seed is naively set on every worker (`np.random.seed(1)` identically on each). The fix is a
distinct, well-separated stream per process rather than a copy of one — exactly what PCG-64's
$2^{127}$ independent streams (and numpy's parallel-RNG support generally) provide.

## Generating random variables

### Multivariate normals via the Cholesky factor

For $X\sim N(0,\Sigma)$, factor $\Sigma=LL^\top$ and set $X=Lz$ for $z$ a vector of independent
standard normals:

```python
L = np.linalg.cholesky(covMat)              # L is lower-triangular
x = L @ np.random.normal(size=covMat.shape[0])
```

For singular $\Sigma$, a pivoted Cholesky sets as many rows to zero as the rank deficiency; the
resulting normals then respect the implicit constraints, but the output vector needs reordering to
undo the pivoting.

### The inverse CDF method

To generate $X\sim F$ for invertible $F$: draw $Z\sim\mathcal U(0,1)$, set $x=F^{-1}(z)$. For a
discrete distribution, work with a discretized $F^{-1}$. For a multivariate target, factor the joint
density into a marginal times a chain of conditionals,
$f(x_1)f(x_2\mid x_1)\cdots f(x_k\mid x_{k-1},\ldots,x_1)$, and apply the idea coordinate by
coordinate, whenever that analytic decomposition exists.

### Rejection sampling

Rejection sampling introduces an auxiliary uniform $u$. For $X\sim f$, $f(x)=\int_0^{f(x)}du$, so $f$
is the marginal of $X$ under $(X,U)\sim\mathcal U\{(x,u):0<u<f(x)\}$ — sampling $X$ is equivalent to
sampling uniformly under the graph of $f$, using only evaluations of $f$, never a direct draw from it.

Pick $g$, easy to sample, that *majorizes* $f$: a constant $c$ with $cg(x)\ge f(x)$ for all $x$, so
$cg$ is an upper envelope. The algorithm: (1) draw $x\sim g$; (2) draw $u\sim\mathcal U(0,1)$;
(3) accept $x$ if $u\le f(x)/(cg(x))$, else return to (1).

<figure>
<svg viewBox="0 0 400 260" role="img" aria-label="Rejection sampling: sampling uniformly under an envelope cg(x) and keeping only points that also fall under f(x)">
  <defs>
    <marker id="arrow-rs" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="220" x2="370" y2="220" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-rs)"/>
  <text x="378" y="224" font-size="12" fill="currentColor">x</text>

  <path d="M40,220 C90,220 140,40 200,40 C260,40 310,220 360,220" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="205" y="34" font-size="12" fill="currentColor">c·g(x)</text>

  <path d="M120,220 C150,220 170,120 200,120 C230,120 250,220 280,220 L120,220 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.8"/>
  <text x="204" y="112" font-size="12" fill="currentColor">f(x)</text>

  <circle cx="200" cy="172" r="3.2" fill="currentColor"/>
  <text x="207" y="176" font-size="11" fill="currentColor">accept (u ≤ f(x))</text>

  <circle cx="160" cy="140" r="3.2" fill="currentColor"/>
  <text x="60" y="132" font-size="11" fill="currentColor">reject (f(x) &#60; u ≤ cg(x))</text>
</svg>
<figcaption>Rejection sampling: draw x under the majorizing envelope cg(x), draw u uniformly up to
that height, and keep the pair only if u also falls under f(x).</figcaption>
</figure>

The majorizing density needs fatter tails than $f$ for $c$ to exist at all — a $t$ can majorize a
normal, but not the reverse. Since $1/c=\int f(x)\,dx/\int cg(x)\,dx$ is the acceptance probability, a
small $c$ (a tight envelope) wastes fewer draws. The method extends to multivariate densities in
principle, but the acceptance rate degrades with dimension, since an increasing share of the volume
under $cg$ sits above $f$.

When $f$ is expensive to evaluate, *squeezing* helps: given a cheap lower bound $f_{\mathrm{low}}\le
f$, accept immediately when $u\le f_{\mathrm{low}}(x)/(cg(x))$, falling back to the true ratio only
when that easier test fails.

A standard worked example: sampling a truncated normal. Sampling the untruncated normal and
discarding out-of-range draws works but is wasteful far in the tail — exactly where inverse-CDF also
runs into numerical trouble. For a (standardized) truncation point above zero, a translated
exponential with lower endpoint at the truncation point makes a good majorizing density (Robert,
1995, *Statistics and Computing*); for truncation below zero, negate the values and use the same
construction.

### Adaptive rejection sampling (optional)

The hard part of rejection sampling is finding a good envelope. For a continuous, differentiable,
log-concave density, adaptive rejection sampling refines the envelope as draws accumulate: on the log
scale, tangents (or secants) through a growing set of points give a piecewise-linear upper bound on
$\log f$, secants between the same points give a lower bound, and exponentiating turns both into
piecewise-exponential bounds on $f$. Drawing from the upper envelope means sampling a discrete
distribution (which linear piece) then the corresponding exponential; the lower envelope is used for
squeezing. A point accepted only after evaluating $f$ directly (squeezing did not resolve it) is added
to the set defining the envelopes, tightening them for later draws.

### Importance sampling

Importance sampling estimates $E_f(h(Y))$ using draws from a different, more convenient $g$:

$$\phi=E_f(h(Y))=\int h(y)\,\frac{f(y)}{g(y)}\,g(y)\,dy,\qquad
\hat\phi=\frac{1}{m}\sum_i h(y_i)\,\frac{f(y_i)}{g(y_i)},\quad y_i\sim g,$$

with $w_i=f(y_i)/g(y_i)$ correcting for sampling from $g$ instead of $f$. When $f$ is known only up to
a normalizing constant (the usual Bayesian case), the weights are self-normalized instead,
$w_i^*=w_i/\sum_j w_j$.

No majorizing property is required, only common support — but the estimator can behave badly if $g$
has *lighter* tails than $f$, since a rare tail draw can then carry an enormous weight, so a
heavier-tailed $g$ is preferred. More precisely, since

$$\mathrm{Var}(\hat\phi)=\frac{1}{m}\,\mathrm{Var}\!\left(h(Y)\frac{f(Y)}{g(Y)}\right),$$

a low-variance estimator wants $f(y)/g(y)$ large only where $h(y)$ is small, so no single draw
dominates. Equivalently, oversampling $y$ where $h(y)$ is large and undersampling where it is small
reduces variance, with the weights correcting for the resulting sampling bias — the canonical case is
a rare event, where oversampling the rare set and reweighting is far more efficient than sampling from
$f$ directly. If the goal is a genuine sample from $f$ rather than an expectation, *sampling
importance resampling* (SIR) resamples from $\{y_i\}$ with probabilities proportional to $\{w_i\}$.

### Ratio of uniforms (optional)

If $(U,V)$ is uniform on $C=\{(u,v):0\le u\le\sqrt{f(v/u)}\}$, then $X=V/U$ has density proportional
to $f$. The algorithm encloses $C$ in a rectangle, samples uniformly until $u\le\sqrt{f(v/u)}$, and
returns $x=v/u$. When $f(x)$ and $x^2f(x)$ are bounded, a simple bounding rectangle is
$0\le u\le\sup_x\sqrt{f(x)}$, $\inf_x x\sqrt{f(x)}\le v\le\sup_x x\sqrt{f(x)}$, and can sometimes be
tightened further. Monahan's *Numerical Methods of Statistics* recommends this approach, including a
version for discrete distributions (2nd ed., p. 323).

## Sources

- Overview, Monte Carlo basics, simulation uncertainty, Rao-Blackwellization: `unit9-sim/01-overview.md`
  and `02-1-monte-carlo-considerations.md`, identical text across fall-2021, fall-2024 and fall-2025
  of berkeley-stat243 Unit 9 (fall-2021 reconstructed from a PDF with no text layer, so its equations
  are unverified but agree throughout with the later, lossless conversions).
- Design of a simulation study, common random numbers, experimental design: `03-2-design-of-simulation-
  studies.md`, all three years. The common-random-numbers code is the R version (fall-2021), chosen
  for brevity over the equivalent Python (fall-2024/2025); both produce the same plot. All years open
  this section by referring to a "Cao et al." paper used as that year's problem set 5 (PS5) example —
  neither the paper nor the problem set was supplied, so the worked context is omitted here.
- Implementation, reporting, reproducibility, the ASA quotation: `04-3-implementation-of-simulation-
  studies.md`, all three years. The `expand.grid()`/`replicate()` worked example (`genFun`, correlated
  normals via Cholesky) is R-only (fall-2021); fall-2024/2025 show only the shorter Python
  `itertools.product` scenario-grid equivalent, also kept. All years point to an external tutorial,
  *simulation_tutorial_miratrix.pdf* by Luke Miratrix with accompanying R code, not supplied here.
- Random number generation: `05-4-random-number-generation-rng.md`. PCG-64, the period-versus-unique-
  values discussion, and the `Generator`/`bit_generator.state` API postdate fall-2021 and are taken
  from fall-2024/2025; the seed-restoring R function idiom is fall-2021-only and taken from there. The
  RNG-in-parallel section points to an SCF parallelization tutorial not supplied here.
- Generating random variables — Cholesky, inverse CDF, rejection sampling, squeezing, the truncated-
  normal example, adaptive rejection sampling, importance sampling, SIR, ratio of uniforms:
  `06-5-generating-random-variables.md`, essentially verbatim across all three years; the Cholesky code
  shown is the Python version (fall-2024/2025). The Robert (1995) truncated-normal reference and
  Monahan's *Numerical Methods of Statistics* are cited by the lecture but not supplied as source
  material.

---

[← 46. Floating-Point Numbers and Precision](46-floating-point-numbers-and-precision.md) · [Contents](index.md) · [48. Displaying Data Badly →](48-displaying-data-badly.md)
