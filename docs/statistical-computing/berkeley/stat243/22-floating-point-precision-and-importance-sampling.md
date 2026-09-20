---
title: "22. Floating-Point Precision and Importance Sampling"
course: "Berkeley Stat 243 Fall 2024"
chapter: 22
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Floating-Point Precision and Importance Sampling

## What this covers

This chapter is a problem set, not a lecture: Berkeley Stat243's "Problem Set 6", assigned in two
offerings of the course (fall 2024, fall 2025) over the same pair of units, with different concrete
examples each year. Unit 8 is the double-precision floating-point format — the representable range,
the spacing between representable numbers, and what happens at the edges of that range. Unit 9 is
Monte Carlo computation — doing likelihood and probability calculations on the log scale to dodge
overflow and underflow, and importance sampling. The chapter assumes the reader already has the
double-precision layout $(-1)^{S}\times 1.d\times 2^{e-1023}$ (sign bit $S$, 11-bit exponent $e$,
52-bit mantissa $d$) and the basic importance-sampling identity from lecture, since both problem
sets repeatedly point back to "the class notes" and "what we said in class" rather than re-deriving
either.

## How the two offerings pair up

Both years open with a floating-point exercise and close with an importance-sampling one, with one
or two problems on computing safely with probabilities in between — but the specific numbers change
every year, so the two offerings are worth reading side by side rather than one instead of the
other.

The floating-point exercise in fall 2024 pokes at the *edges* of the representable range: the
largest magnitude before it overflows to `inf`, and the smallest normalized magnitude before the
exponent runs out of bits. Fall 2025 instead pokes at the *middle* of the range, at the magnitude
$2^{53}$ where double precision stops being able to represent every integer exactly, and asks for
the resulting relative error. Both years carry, as an extra-credit problem, essentially the same
follow-up question: find, by trial and error, the smallest positive number Python can actually
represent, which turns out to be far smaller than $1\times10^{-308}$ — the smallest *normalized*
double — and explain how. The answer both years is the same: *denormalized* (subnormal) numbers,
which give up the implicit leading 1 before the radix point in exchange for reaching lower
magnitudes at reduced precision.

The middle problems change topic entirely between years — a variance calculation and a Bayesian
predictive density in 2024, a numerical derivative and a softmax in 2025 — but they are all
instances of the same two lessons: subtracting two nearly equal large floating-point numbers throws
away precision (catastrophic cancellation), and a product of many probabilities, or an exponential of
a large number, should be handled on the log scale rather than computed directly.

The importance-sampling problems share a common shape rather than common content: both ask for a
Monte Carlo estimate of a moment of a target density $f$ using draws from a different, tractable
density $g$, and both ask for histograms of the importance weights $f(x)/g(x)$ (and of the reweighted
summand) to check whether a handful of extreme draws dominate the estimate — the visible symptom of a
sampling density with tails lighter than the target's. Fall 2024 illustrates this with a truncated
$t_3$ distribution, sampled from a truncated normal and then from a truncated $t_1$; fall 2025 uses a
shifted exponential and a Pareto distribution, each in turn playing the role of target and of
sampler, so the same pair of tail behaviours gets examined from both directions.

## Exercises

### 1. Overflow at the top of the range (fall 2024)

In the exponent field of the double-precision format, $e \in \{0,\dots,2047\}$ (11 bits give
$2^{11}=2048$ values), which — ignoring the mantissa — suggests that the largest and smallest
positive normalized magnitudes are $2^{1024}$ and $2^{-1023}$.

a. $2^{1024}$ in fact overflows. Construct a numpy `float64` number larger than $10^{308}$ that
   overflows and is represented as `inf`. Give its bit-wise representation, and explain why it now
   makes sense that $2^{1024}$ cannot be stored as an ordinary number.

   Extra credit: the bit pattern consisting of a single 0 followed by sixty-three 1s (or all
   sixty-four bits set to 1) is *not* the pattern actually used for `inf`/`-inf`, even though it
   looks like a natural candidate. Investigate why.

b. Give the bit-wise representation of $2^{-1022}$. From it, work out — conceptually, without
   evaluating $2^{-1023}$ in Python — what the bit-wise representation of $2^{-1023}$ would naively
   be, and what number that pattern actually represents.

### 2. Exact integer representation near $2^{53}$ (fall 2025)

Integers up to $2^{53}$ can be stored exactly in double precision. (You may work in base 10 for the
exponent here; there is no need to write $e$ out in base 2.)

a. Show how the integers $1, 2, 3, \dots, 2^{53}-2, 2^{53}-1$ are represented exactly in the format
   $(-1)^{S}\times1.d\times2^{e-1023}$, with $d$ a 52-bit mantissa. Working out the pattern on a
   handful of examples, informally, is enough.
b. Show that $2^{53}$ and $2^{53}+2$ are exact but $2^{53}+1$ is not — so the spacing between
   representable numbers at this magnitude is 2 — and that from $2^{54}$ onward the spacing between
   exactly representable integers is 4. Check this against what Python (base floats or numpy) gives
   for $2.0^{53}-1$, $2.0^{53}$, and $2.0^{53}+1$.
c. Calculate the relative error in representing numbers of magnitude $2^{53}$ in base 10. (This
   should look familiar — it is the same relative error you would find at magnitude $2^{54}$, or at
   any other magnitude.)

### 3. The smallest positive representable number (extra credit; both offerings)

By trial and error, find the base-10 representation of the smallest positive number Python can
represent — considerably smaller than $1\times10^{-308}$. Explain how a number smaller than
$1\times2^{-1022}$ (the smallest *normalized* positive double) can be stored at all: start from the
bit-wise representation of $1\times2^{-1022}$, work out what the "natural" bit pattern for
$1\times2^{-1023}$ would be by the same rule, and check that this pattern does not in fact represent
$2^{-1023}$ but some other, more familiar, number. Then, from the *actual* bit-wise representation of
$1\times2^{-1023}$, show the progression of representable numbers below it, down to the smallest
positive number Python can represent, written in both base 2 and base 10.

(Hint: these are denormalized — subnormal — numbers, which do not carry a fixed leading 1 before the
radix point the way the format above assumes.)

### 4. Catastrophic cancellation in a variance calculation (fall 2024)

For a vector $w$, take $\mathrm{var}(w) = \sum_{i=1}^{n}(w_i-\bar w)^2/(n-1)$, and consider

```python
import numpy as np
rng = np.random.default_rng(seed=1)
def dg(x, form='.20f'):
    print(format(x, form))

z = rng.normal(size=100)
x = z + 1e12
dg(np.var(z))
dg(np.var(x))
```

Mathematically $\mathrm{var}(x) = \mathrm{var}(z)$, since $x$ is just $z$ shifted by a constant, yet
the two computed values agree to only a small number of decimal places. Explain why, say which of
the two values is the more accurate one, and estimate how many digits of accuracy you would expect
in the less accurate of the two.

### 5. A log-scale predictive density (fall 2024)

A predictive density for new data, in a Bayesian model-comparison setting, is

$$f(y^{*}\mid y,x) = \int f(y^{*}\mid y,x,\theta)\,\pi(\theta\mid y,x)\,d\theta
 = E_{\theta\mid y,x}\,f(y^{*}\mid y,x,\theta),$$

where $\pi(\theta\mid y,x)$ is the posterior. Given posterior draws $\theta_j \sim \pi(\theta\mid
y,x)$, $j=1,\dots,m$, and a vector of conditionally IID observations $y_1^{*},\dots,y_n^{*}$, a Monte
Carlo estimate of this quantity is

$$f(y^{*}\mid y,x) \approx \frac{1}{m}\sum_{j=1}^{m}\prod_{i=1}^{n} f(y_i^{*}\mid y,x,\theta_j).$$

a. Explain why the product inside the sum should be computed on the log scale, and what is likely to
   go wrong if it is instead computed directly.
b. Re-expressed on the log scale, the estimate becomes $\frac{1}{m}\sum_{j=1}^{m}\exp(v_j)$, where
   $v_j = \sum_{i=1}^{n}\log f(y_i^{*}\mid y,x,\theta_j)$. What is likely to go wrong when you try to
   exponentiate $v_j$?
c. For the log predictive density,
   $$\log f(y^{*}\mid y,x) \approx \log\left(\frac{1}{m}\sum_{j=1}^{m}\exp(v_j)\right),$$
   work out how to calculate this without running into the problems from (a) and (b). (Hint: recall
   how a similarly problematic expression was rescaled in the logistic-regression example done in
   class; the trick here is analogous, applied to the $\exp(v_j)$ terms — and note that it will only
   get you the *log* of the predictive density, not the density itself.)

### 6. Numerical differentiation and the choice of step size (fall 2025)

A standard way to approximate a derivative that is hard to obtain analytically is

$$f'(x) \approx \frac{f(x+\epsilon)-f(x)}{\epsilon}$$

for small $\epsilon$. Since the right-hand side tends to $f'(x)$ exactly as $\epsilon \to 0$, it
seems that $\epsilon$ should be chosen as small as possible.

a. Focusing on the numerator alone (the denominator only rescales the result, and is itself accurate
   to roughly 16 digits): in what ways — there is more than one — do the limitations of computer
   arithmetic constrain how small $\epsilon$ can usefully be?
b. Write a Python function implementing the approximation, and for a nonlinear function of your own
   choosing whose derivative you can also get analytically, explore how the error in the estimated
   derivative behaves as a function of $\epsilon$.

### 7. Softmax overflow in multiclass logistic regression (fall 2025)

In multiclass logistic regression,

$$p_j = \mathrm{Prob}(y=j) = \frac{\exp(x\beta_j)}{\sum_{k=1}^{K}\exp(x\beta_k)}
 = \frac{\exp(z_j)}{\sum_{k=1}^{K}\exp(z_k)}, \qquad z_k = x\beta_k,$$

where $p_j$ is the probability that observation $y$ belongs to class $j$.

a. What happens if the $z_k$ are large in magnitude, whether positive or negative?
b. Re-express the equation so that $p_j$ can still be computed correctly when that happens.

### 8. Importance sampling for a truncated $t$ distribution (fall 2024)

a. Use importance sampling to estimate the mean $\phi = E_f X$ of a $t_3$ distribution truncated to
   $X < -4$. Take the sampling density $g$ to be a normal distribution centered at $-4$, truncated to
   values below $-4$ (a half-normal) — arranged so that no draws need to be discarded (explain how
   this is possible). Use $m=10{,}000$ samples. Plot histograms of the weights $f(x)/g(x)$ and of the
   summand $h(x)f(x)/g(x)$ to judge whether $\mathrm{Var}(\hat\phi)$ is large, noting any extreme
   weights that would dominate $\hat\phi$, and estimate $\mathrm{Var}(\hat\phi)$. (Remember that
   $f(x)$ must be properly normalized on the truncated region, or the weights adjusted accordingly,
   as in the class notes. For comparison, numerical integration — feasible here but increasingly
   infeasible in higher dimensions — gives a true mean of $-6.216$.)
b. Repeat, but now take $g$ to be a $t_1$ distribution centered at $-4$ and truncated to $X<-4$
   (again without discarding any draws). Answer the same questions as in (a), and in addition give a
   95% simulation uncertainty interval for your estimate, using
   $\sqrt{\widehat{\mathrm{Var}}(\hat\phi)}$.

### 9. Importance sampling and the weight of the tails (fall 2025)

The Pareto distribution has pdf $p(x) = \dfrac{\beta\alpha^{\beta}}{x^{\beta+1}}$ for $x > \alpha$,
with $\alpha,\beta>0$; its mean is $\dfrac{\beta\alpha}{\beta-1}$ for $\beta>1$ (nonexistent
otherwise), and its variance is $\dfrac{\beta\alpha^{2}}{(\beta-1)^{2}(\beta-2)}$ for $\beta>2$
(nonexistent otherwise). Recall that $\mathrm{Var}(\hat\phi) \propto \mathrm{Var}\big(h(X)f(X)/g(X)\big)$.

a. Does the Pareto distribution's tail decay more quickly or more slowly than an exponential's?
b. Let $f$ be an exponential density with rate 1, shifted two units to the right so that $f(x)=0$ for
   $x<2$. Pretending you cannot sample directly from $f$, use importance sampling with $g$ a Pareto
   distribution with $\alpha=2$, $\beta=3$, and $m=10{,}000$ draws, to estimate $EX$ and $E(X^2)$, and
   compare against the known values for the shifted exponential. Plot histograms of $h(x)f(x)/g(x)$
   and of the weights $f(x)/g(x)$ to judge whether $\mathrm{Var}(\hat\phi)$ is large, noting any
   extreme weights.
c. Now let $f$ be the Pareto distribution above, and, pretending you cannot sample directly from it,
   use the shifted exponential as $g$. Answer the same questions as in (b), comparing against the
   known values for the Pareto.

## Sources

- `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps6.md` — converted losslessly from
  `ps/ps6.qmd` in the berkeley-stat243 fall-2024 repository, CC BY 4.0. Problems 1–4: the
  overflow/underflow floating-point questions (with the denormalized-number extra credit), the
  variance catastrophic-cancellation example, the log-scale predictive-density derivation, and the
  truncated-$t_3$ importance-sampling exercise.
- `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps6.md` — converted losslessly from
  `ps/ps6.qmd` in the berkeley-stat243 fall-2025 repository, CC BY 4.0. Problems 1–5: the exact
  integer-representation exercise near $2^{53}$, the numerical-differentiation step-size problem,
  the softmax overflow problem, the Pareto/shifted-exponential importance-sampling exercise, and the
  extra-credit smallest-representable-number problem.
- Referred to but not contained in either file: the course's Unit 8 (floating-point arithmetic) and
  Unit 9 (Monte Carlo methods) lecture notes, which both problem sets assume already covered; the
  in-class logistic-regression example that the log-scale rescaling trick in Problem 5c is said to
  resemble; the class notes on normalizing importance-sampling weights referred to in Problem 8; and
  Problem Set 1, for the formatting and attribution requirements both offerings point back to.

---

[← 21. Parallel Jobs on Shared Clusters](21-parallel-jobs-on-shared-clusters.md) · [Contents](index.md) · [23. Problem Set 7 →](23-problem-set-7.md)
