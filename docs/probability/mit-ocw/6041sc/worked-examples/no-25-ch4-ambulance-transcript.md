---
title: No 25 ch4 ambulance transcript
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/worked-examples/no-25-ch4-ambulance-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# No 25 ch4 ambulance transcript

**Source:** `worked-examples/no-25-ch4-ambulance-transcript.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we'll be looking at an ambulance that is traveling back and forth in interval of size l. Say from 0 to l.

At some point in time, there's an accident occurring, let's say at location x. And we'll assume the accident occurs in a random location so that x is uniformly distributed between 0 and l. Now, at this point in time, let's say the ambulance turns out to be at location y. Again, we'll assume that y is a uniform random variable between 0 and l, and also that x and y are independently distributed.

The question we're interested in answering is how long it would take an ambulance to respond to travel from point y to point x. Let's call this time T. And in particular, we want to know everything about distribution of T. For example, what is the CDF of T given by the probability of big T, less than or equal to little t, or the PDF, which is done by differentiating the CDF once we have it.

Now, to start, we'll express T you as a function of X and Y. Since we know that the ambulance travels at a speed V-- V meters or V units of distance per second-- then we can write that big T is simply equal to Y minus X, absolute value the distance between X and Y, divided by the speed at which the ambulance is traveling at, V. So now if we look at the probability of T less than or equal to little t, this is then equal to the probability that Y minus X divided by V less than or equal to little t.

We now take off the absolute value by writing the expression as negative vt less equal to Y minus X less equal to positive vt. Here we multiply v on the other side of t, and then took out the absolute value sign. As a final step, we'll also move X to the other side of inequalities by writing this as X minus vt less equal to y less equal to x plus vt.

To compute this quantity, we'll define a set A as a set of all points that satisfies this condition right here. In particular, it's a pair of all X and Y such that X minus vt less equal to little y less equal to X plus vt, and also that X is within 0 and l, and so is Y.

So the set A will be the set of values we'll be integrating over. Now that we have A, we can express the above probability as the integral of all X and Y, this pair within the set A, integrating the PDF of f of X, Y, little x, little y.

Let's now evaluate this expression right here in a graphical way. On the right, we're plotting out what we just illustrated here, where the shaded region is precisely the set A. As we can see, this is a set of values of X and Y where Y is sandwiched between two lines, the upper one being X plus vt right here, and the lower line being X minus vt, right here. So these are the values that correspond to the set A.

1

Now that we have A, let's look f of x, y. We know that both x and y are uniform random variables between 0 and l, and therefore, since they're independent, the probability density of x and y being at any point between 0 and l is precisely 1 over l squared, where l squared is the size of this square box right here.

So given this picture, all we need to do is to multiply by 1 over l squared the area of the region A. And depending on the value of T, we'll get different answers as right here. If T is less than 0, obviously, the area of A diminishes to nothing, so we get 0. If T is greater than l over V, the area of A fills up the entire square, and we get 1. Now, if T is somewhere in between 0 and l over v, we will have 1 over l squared, multiply by the area looking like something like that right here-the shaded region.

Now, if you wonder how we arrive at exactly this expression right here, here is a simple way to calculate it. What we want is 1 over l squared times the area A. Now, area A can be viewed as the entire square, l squared, minus whatever's not in area A, which is these two triangles right here. Now, each triangle has area 1/2, l minus vt squared. This multiply 2, and this, after some algebra, will give the answer right here.

At this point, we have obtained the probability of big T less equal to little t. Namely, we have gotten the CDF for T. And as a final step, we can also compute the probability density function for T. We'll call it little f of t. And we do so by simply differentiating the CDF in different regions of T.

To begin, we'll look at t between 0 and l over v right here at differentiating the expression right here with respect to t. And doing so will give us 2v over l minus 2v squared t over L squared. And this applies to t greater or equal to 0, less than l/v. Now, any other region, either t less than 0 or t greater than l/v, we have a constant for the CDF, and hence its derivative will be 0. So this is for any other t. We call it otherwise.

Now, this completely characterized the PDF of big T, and hence, we've also finished a problem.

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
