---
title: 20 transcript no32 rec20 p2 convgprob1 part ef
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/20-transcript-no32-rec20-p2-convgprob1-part-ef.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 transcript no32 rec20 p2 convgprob1 part ef

**Source:** `recitations/20-transcript-no32-rec20-p2-convgprob1-part-ef.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **6.041SC Probabilistic Systems Analysis and Applied Probability, Fall 2013 Transcript – Recitation: Convergence in Probability and in the Mean Part 2**

For part E and F of the problem, we'll be introducing a new notion of convergence, so-called the convergence E mean squared sense. We say that xn converges to a number c in mean squared, if as we take and go to infinity, the expected value of xn minus c squared goes to 0. To get a sense of what this looks like, let's say we let c equal to the expected value of xn, and let's say the expected value of xn is always the same.

So the sequence of random variables has the same mean. Well, if that is true, then mean square convergence simply says the limit of the variance of xn is 0. So as you can imagine, somehow as xn becomes big, the variance of xn is very small, so xn is basically highly concentrated around c. And by this I mean, the density function for xn. So that's the notion of convergence we'll be working with.

Our first task here is to show that the mean square convergence is in some sense stronger than the convergence in probability that we have been working with from part A to part D. That is, if I know that xn converged to some number c in mean squared, then this must imply that xn converges to c in probability. And now, we'll go show that for part E.

Well, let's start with a definition of convergence in probability. We want to show that for a fixed constant epsilon the probability that xn minus c, greater than epsilon, essentially goes to 0 as n goes to infinity. To do so, we look at the value of this term.

Well, the probability of absolute value xn minus c greater than epsilon is equal to the case if we were to square both sides of the inequality. So that is equal to the probability that xn minus c squared greater than epsilon squared. We can do this because both sides are positive, hence this goes through.

Now, to bound this equality, we'll invoke the Markov's Inequality, which it says this probability of xn, some random variable greater than epsilon squared, is no more than is less equal to the expected value of the random variable. In this case, the expected value of x minus c squared divided by the threshold that we're trying to cross. So that is Markov's Inequality.

Now, since we know xn converges to c in mean squared, and by definition, mean square we know this precise expectation right here goes to 0. And therefore, the whole expression goes to 0 as n goes to infinity. Because the denominator here is a constant and the top, the numerator here, goes to 0. So now we have it. We know that the probability of xn minus c absolute value greater than epsilon goes to 0 as n goes to infinity, for all fixed value of epsilons and this is the definition of convergence in probability.

Now that we know if xn converges to c mean squared, it implies that xn converges to c in probability. One might wonder whether the reverse is true. Namely, if we know something converges in probability to a constant, does the same sequence of random variables converge to

1

the same constant in mean squared? It turns out that is not quite the case. The notion of probability converges in probability is not as strong as a notion of convergence in mean squared.

Again, to look for a counter example, we do not have to go further than the yn's we have been working with. So here we know that yn converges to 0 in probability. But it turns out it does not converge to 0 in the mean squared. And to see why this is the case, we can take the expected value of yn minus 0 squared, and see how that goes.

Well, the value of this can be computed easily, which is simply 0, if yn is equal to 0, with probability 1 minus n plus n squared when yn takes a value of n, and this happens with probability 1 over n. The whole expression evaluates to n, which blows up to infinity as n going to infinity. As a result, the limit n going to infinity of E of yn minus 0 squared is infinity and is not equal to 0. And there we have it, even though yn converges to 0 in probability, because the variance of yn, in some sense, is too big, it does not converge in a mean squared sense.

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
