---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/exbo08-78iu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/exbo08-78iu-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today what we want to do is discuss various approaches that you might want to take towards trying to understand stochastic systems. In particular, how is it that we might model or simulate a stochastic system?**

**Now, we will kind of continue our discussion of the master equation from last time. Hopefully now you've kind of thought about it a bit more in the context of the reading. And we'll discuss kind of what it means to be using the master equation and how to formulate the master equation for more complicated situations, for example, when you have more than one chemical species.**

**And then we'll talk about the idea of this Gillespie method, which is an exact way to simulate stochastic systems, and it's both exact and computationally tractable as compared to what you might call various naive methods. And the Gillespie method is really sort of qualitatively different from the master equation because in the master equation, you're looking at the evolution of probability distributions across the system, whereas the Gillespie method is really a way to generate individual stochastic trajectories.**

**So if you start with somehow similar initial conditions, then you can actually get-you can get, for example, the probability distributions from the Gillespie method by running many individual trajectories. But it's kind of conceptually rather different because of this notion of whether you think about probabilities or you're thinking about individual instantiations of some stochastic trajectory. So we'll try to make sense of when you might want to use one or the other.**

**And then finally we'll talk about this Fokker-Planck approximation, which, as the reading indicated, for intermediate ends, it's useful to make this kind of continuous**

1

**approximation, and then you can get a lot of intuition from your knowledge about diffusion on effective [INAUDIBLE] landscapes.**

**Are there any questions about this or administrative things before we get going? I just want to remind you that the midterm is indeed next Thursday evening, 7-9 PM. If you have a problem with that time, then you should have emailed [? Sarab. ?] And if you haven't emailed him yet, you should do it right now. And-- yes.**

**All right. So let's think about the master equation a little bit more. Now before what we did is we thought about the simplest possible case of the master equation, which is, if you just have something being created at a constant rate and then being degraded at a rate that's proportional to the number of that chemical species. And I'm going to be using the nomenclature that's a little bit closer to what was in your reading, just for, hopefully, clarity. And I think that some of my choices from last lecture were maybe unfortunate.**

**So here, this is, for example, m would be the number of mRNA, for example, in the cell. This is the rate of creation of the mRNA, and then the rate of degradation of the mRNA. So m is the number of mRNA. And if we want understand gene expression, we might include an equation for the protein, so we might have some p dot, where some Kp.**

**Now-- oh, sorry. Again, I always do this. All right. So we're going to have this be an n dot. So now n is going to be the number of the protein.**

**Now this really is kind of the simplest possible model that you might write down for gene expression that includes the mRNA and the protein. So there's no autoregulation of any sort. It's just that the mRNA is involved in increasing the protein, but then we have degradation of the protein as well.**

**So what we want to do is kind of try to understand how to formulate the master equation here. But then also, we want to make sure that we understand what the master equation is actually telling us and how it might be used.**

**So first of all, in this model, I want to know is there, in principle, protein bursts? So**

2

**before we talked about the fact that in-- at least in [? Sunny's ?] paper that we read- they could observe protein bursts, at least in those experiments in e Coli. Question is, should this model somehow exhibit protein bursts, and why or why not? I just want to see where we are on this.**

**I think this is something that, depending on how you interpret the question, you might decide the answer is yes or no. But I'm curious-- I think it's worth discussing what the implications are here. And the relevant part of this is going to be the discussion afterwards, so I'd say don't worry too much about what you think right now. But I'm just curious. This model, does it include, somehow, protein bursts? Ready? Three, two, one.**

**OK. So we got-- I'd say at least a majority of people are saying no. But then some people are saying yes. So can somebody volunteer why or why not? Yes?**

**AUDIENCE: I think the difference is if we're-- are we using this in a continuous fashion or are we using this in a discrete fashion [INAUDIBLE].**

**PROFESSOR: Yeah. OK. All right. All right. So he's answered both possible sides of the argument. And the point here is that if you just simulate this from the standpoint-- certainly, for example, this continuous, this discrete-- so if you just simulate this as a deterministic pair of differential equations, then will there be bursts? No. Because everything is well-behaved here.**

**On the other hand, if we go and we do a full Gillespie simulation of this pair of equations, then in the proper parameter regime, we actually will get protein bursts, which is, in some ways, weird, that depending upon the framework that you're going to be analyzing this in, you can get qualitatively different behaviors for things.**

**But there's a sense here that the deterministic, continuous evolution of these quantities would be the average over many of these stochastic trajectories, and the stochastic ones do have bursts, but if you average over many, many of them, then you end up getting some well-behaved pair of equations.**

**So we'll kind of try to make sense of this more later on. But I think this just highlights**

3

**that you can get really qualitatively different behaviors for the same set of equations depending upon what you're looking at.**

**And these protein bursts can be dramatic events, right, where the protein number pops up by a lot. So this really, then, if you look at the individual trajectories here, they would look very different whether you were doing kind of a stochastic treatment or the deterministic one.**

**Can somebody remind us the situation in which we get protein bursts in the stochastic model? In particular, will we always get these discrete protein bursts? Or what determines the size of a protein burst? Yes.**

---

[Up: contents](index.md) · [Exbo08 78iu transcript Part 02 — →](02-exbo08-78iu-transcript-part-02.md)
