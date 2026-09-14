---
title: '[STUDENTS RESPOND]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/03bvgr-vyhq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [STUDENTS RESPOND]

**Source:** `recordings/03bvgr-vyhq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Right. So it's going to be 1 over delta m. So this tells us the characteristic timescale to come back. So if we're-- this is the equilibrium Sm over delta m. This is m as a function of time. If we're below, we come here. If we're above, we come here. And this time is 1 over delta m. Are the any questions about?**

**Now this-- so I want to highlight that this is like the world's simplest dynamical equation, almost the world's simplest. Yet what we're going to find is that once we go over and we try to understand the full probability distribution of the stochastic system then it's a little bit more complicated. In particular, we end up with an infinite set of differential equations.**

**So in general the Master Equation format, where we're going to write differential**

16

**equations for how these probabilities change over time. Now what we've done is we've traded a single differential equation for an infinite number of differential equations. So that's a bummer. But on the other hand, it will allow us to do the full stochastic treatment. And it's also a nice, to me, the master equation is useful in kind of two ways.**

**One is that it's going to be a tool for us to do analytic calculations. But it's also kind of a principled way of organizing your thoughts so that you can go and do stochastic simulations, if that's what you want to do. So it's also just kind of like a weigh station to kind of help you set up your simulation.**

**So what we're going to do is we're going to ask about the general way that this thing is going to move between different states. In particular, we are going to have some general state in here. Mn, which can go forward or back, Mn plus 1.**

**Now what we want to do is think about how those probabilities are going to change over time. So we typically have fn. So this is often written as an fn and fn minus 1. And then this is a g. I want to make sure I get the n's and n minus ones correct here.**

**Typically we write gm plus 1, gn. So these are telling us about the rates of being in this state, with say, n mRNAs, as compared to going here. We're going here. So then what we can do is we can write the change in the probability of mn with respect to time.**

**Well there are just a few different ways that the probability can change. So we can leave the state in two different ways. fn, gn. So the way that we lose the probability is that we have fn plus gn times the probability that we are in mn. That's an n there.**

**And then there are going to be two ways that we gain probability. We can gain probably from the mn minus 1. So this is fn minus 1, plus we can get probability from the upper state. That's a gn plus 1 mn plus 1. So this is just saying that the change in the probability of being in this state is going to be given by the probability that we leave the state. Sorry. The probability that we enter the state, minus the**

17

**probability that we're leaving the state, kind of the rates.**

**Now this is going to be true for all n, except for n equal to zero, we don't have the terms over on the left. So this is kind of for all n. So this is, in particular this is for n, basically 0 on up to infinity. So this is a differential equation for the probability for having an mRNA. But this is, we have to have a different equation for each n, 0, 1, 2, 3, 4, 5 on up.**

**So this is what I mean by converting single differential equation, which is actually an exceedingly simple one, for one that is for an infinite set. And each one is even a little bit more complicated. In general, these f's and n's can be pretty complicated. In this situation they're not so bad.**

**But let's make sure. Can somebody say what fn and gn are equal to? Any volunteers?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Right so fn, this is rate that we add a new mRNA. Well that's just synthesis rate for mRNA. And this guy is what?**

**AUDIENCE: Delta.**

**PROFESSOR: So this is degradation rate. And we actually do have to multiply still by the number n. And that's because as we go further out here to the right, then it is true. The rate at which we come back to the left is increasing. Because there's just more mRNA that can be degraded.**

**Now it's worth saying that you can, for example, use this to simulate the probability distribution if you start from any distribution you like. So for example, you could start M0 equal to 1. And then just simulate how the probability recalibrates and comes over here. Similarly, you could do it over here. You could start with any probability distribution you want. And you could use this as a framework to calculate what the probability distribution will be at any time later.**

**But you can also use this just as a way of figuring out what the equilibrium**

18

**distribution is going to be. Because at equilibrium, we can just ask, for each one of these arrows, the probability of moving to the right has to be equal to the probability of moving to the left, otherwise we wouldn't be at equilibrium. And that's true for every one of these kinds of pairs of arrows.**

**And in particular, what we can get, and I want to make sure that-- so but it's not that fn is equal to gn-- so it's really going to end up being that if you see what fn and gn, so that fn is going to have to be equal to g of n plus 1 for all n. Yes?**

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
