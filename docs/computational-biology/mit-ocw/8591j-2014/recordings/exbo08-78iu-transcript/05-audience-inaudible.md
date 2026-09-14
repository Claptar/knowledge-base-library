---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/exbo08-78iu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/exbo08-78iu-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: I'm sorry, what's that? Right. OK. So I mean, this is just-- you know, you program in your computer to use the master equation to solve how the probabilities are going to evolve. I'm just telling you, start with some initial distribution. And if you do it once, it says, oh, the probability that you're going to have m-- this time you're going to have mRNA proteins is going to be P1, so it's 10%. Great.**

**Now I'm asking just, if you go back and do it again, will you again get 10%, or is this output stochastic? It's OK that if you're confused by this distinction. I think that it's easy to get confused by, which is why I'm doing this. But let's just see where we are. Ready? 3, 2, 1.**

**All right. So I'd say a majority again. We're kind of at the 80-20, 75-25. A majority**

10

**here are saying that, yes, you will get the same probability. And this is very important that we understand kind of where this where the stochasticity is somehow embedded in these different representations of these modelings.**

**The master equation is a set of differential equations telling you about how the probabilities change over time given some initial conditions. Now we're using these things to calculate the evolution of some random process, but the probabilities themselves evolve deterministically. So what that means is that although these things are probabilities, if you start somewhere and you use the master equation to solve, you get the same thing every time you do it.**

**Now this is not true for the Gillespie simulation, because that, you're looking at an individual trajectory. An individual trajectory, then the stochasticity is embedded in that trajectory itself, whereas in the master equation, the stochasticity arises because these are probabilities that are calculating, so any individual instantiation will be probabilistic because you are sampling from those different probability distributions.**

**Now this is, I think, a sufficiently important point that if there are questions about it, we should talk about it. Yeah.**

**AUDIENCE: How do you make the simulations? Would you essentially-- can you take a sum over different Gillespie?**

**PROFESSOR: So it's true that you can do a sum over different Gillespie. But we haven't yet told you about, what the Gillespie algorithm is, so I can't use that. But indeed, you can just use a standard solver of differential equations. So whatever program you use is going to have some way of doing this.**

**And once you've written down these equations, the fact that these are actually probabilities doesn't matter. So those could have been something else. So this could be the number of eggs, whatever, right? So once you've gotten the equations, then equations just tell you how the problems are going to change over time. Yeah.**

**AUDIENCE: Maybe this is a silly question, but in practice, do you have to assume all the**

11

---

[← AUDIENCE: [INAUDIBLE]](04-audience-inaudible.md) · [Up: contents](index.md) · [probabilities are 0 above some number? →](06-probabilities-are-0-above-some-number.md)
