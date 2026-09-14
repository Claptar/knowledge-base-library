---
title: same. p tilde dot.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/xnnxlsy-f-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# same. p tilde dot.

**Source:** `recordings/xnnxlsy-f-s-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**We can linearize by taking derivatives around the fixed points. And in particular, what we want to do is we want to take the derivative of f with respect to m. Evaluate at the fixed point. That derivative is, indeed, just minus 1.**

**So in general, in these situations, what we have is we have derivatives m, m dot p dot, and we have partial of this first function f with respect to m. Partial of g. Oh, no. So this is still f. Respect to p. Down here is derivative g with respect to m. Derivative g with respect to p.**

**And this is all evaluated around the fixed point m 0 p 0. So we want to take these derivatives and evaluate at the fixed point. And if we do that, we get minus 1 here, derivative m with respect to m times m tilde.**

**This other guy, when you take the derivative, you get a minus sign with respect to p. So we get a minus sign because this is in the denominator. And then, we have to take derivative inside. So we get n alpha p 0 to the n minus 1. And down, we get a 1 plus p 0 squared. So we took the derivative of this term with respect to p. And we evaluated at the fixed point p 0. Did I do that right?**

**But we still have to add a p tilde because this is saying how sensitive is the function to changes in where you are times how far you've gone away from the fixed point. And then, again, over here, we take the derivatives down below. So derivative g with respect to m. That gives us a beta m tilde. And then, we have a minus beta p tilde.**

**All right, so this is just an example of linearizing those equations around that fixed point. So ultimately, what we care about is really this matrix that's specifying deviations around the equilibrium. Right? So it's useful to just write it in matrix format because we get rid of some of the M's and P's.**

**Indeed, so this matrix that we either call A or the Jacobean depending on-- so what we have is a minus 1. And we're going to call this thing x because it's going to pop up a lot is this minus n alpha p 0. So it's an x beta and minus beta.**

16

**And then, we have our simple rules for determining whether this thing is going to be stable or not. It depends on the trace. And it depends on the determinant. So the trace should be negative. And is this trace negative? Yes. Yes because beta-- does anybody remember what beta was again.**

**AUDIENCE: Ratio of lifetimes.**

**PROFESSOR: Ratio of lifetimes. Lifetimes are positive. So beta is positive. All right, so the trace is equal to minus 1 minus beta. This is, indeed, less than 0. So this is consistent for stability. Does prove that it's stable? No. But we also need to know about the determinant of a, which is going to be beta, this times this, minus this times this.**

**So that's minus. And this is a beta times what x was. So this gives us-- we can write this all down just so that it's clear that it has to be positive. So beta is positive. Positive, positive, positive, positive, positive. Everything's positive. So this thing has to be greater than 0.**

**So what does this mean about the stability of Ethics Point? Stable. Fixed point stable. And what does that mean about oscillations? It means there are no oscillations. Fixed point stable. Therefore, no oscillations.**

**So what this is saying is that the original, kind of simple, equation we wrote down for negative auto regulation, that thing was not allowed to oscillate mathematically. But that doesn't mean that, if you explicitly model the mRNA, it could go either way. But still, that's insufficient to generate oscillations. However, maybe if you included more steps, maybe it would oscillate. Question?**

**AUDIENCE: So just to double check-- when you said, no oscillations, you mean stable oscillations?**

**PROFESSOR: That's right, sorry. When I mean no oscillations, what I mean are indeed, no limit cycle oscillations. AUDIENCE: This is like a dampened--**

**PROFESSOR: Yeah. Yeah, so we, actually, have not solved exactly what it looks like. And I've**

17

**drawn this is a pretty oscillatory thing. But it might just look like this, depending on the parameters and so forth. And indeed, we haven't even proven that this thing has complex eigenvalues.**

**But certainly, there are no limit cycle oscillations. And I'd say it's really limit cycle oscillations that people find most exciting as because limit cycle oscillations have a characteristic amplitude. So it doesn't matter where you start. The oscillations go to some amplitude.**

**And they have a characteristic period, again, independent of your starting condition. So a limit cycle oscillation has a feeling similar to a stable fixed point in the since that it doesn't matter where you start. You always end up there. So they're the ones that are really what you would call mathematically nice oscillations.**

**And when I say this, I'm, in particular, comparing them to neutrally stable orbits. So there are cases in which, in two variables, you have a fixed point here. And at least in the case of linear stability, if you have purely imaginary eigenvalues, what that means is that you have orbits that go around your fixed point.**

**And we'll see some cases that look like this later on. And this is, indeed, the nature of the oscillations in the Lotka-Volterra model for predator prey oscillations. They're not actually limit cycle oscillations. They're of this kind that are considered less interesting because they're less robust.**

**Small changes in the model can cause these things to either go away, to turn into this kind of stable spiral, or to turn into limit cycle oscillations. So we'll talk about this more in a couple months. These are neutrally stable orbits.**

**OK, but what I wanted to highlight, though, is that just because the original, simple, protein only model didn't oscillate and this protein mRNA together doesn't oscillate does not mean that it's impossible to get oscillations using negative auto regulation, either experimentally or computationally. And the question is, what might you need to do to get oscillations?**

18

---

[← PROFESSOR](04-professor.md) · [Up: contents](index.md) · [AUDIENCE →](06-audience.md)
