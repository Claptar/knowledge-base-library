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

**PROFESSOR: Maybe. I don't want to get too much into this because, well, on Thursday we spent a long time talking about it. Once we get going, we'll spend another long time taling about it again. But you should review your notes from Thursday before the exam.**

**So this thing is gamma distributed. And if we looked at the mRNA number as a function of time and we did a histogram of that, the mRNA distribution would be what? It's poisson. So it's important to remember that just because I tell you that a protein number is gamma distributed, that doesn't immediately tell you exactly what you should be expecting for the distribution of, say, the number of protein as a function of time.**

**I mean, there are many different things I could plot over here that would all kind of come down to a gamma distribution over here. So it's important to kind of keep in mind the different representations that you might want to think about the data.**

**So what we want to do now is we want to think a little bit more about this master equation in the context of if we're going to divide it up into these states. Now I would**

6

**say that any time that you are asked to write down the master equation for something-- so now how many equations will the master equation-- I say master equation, but there is really more than one, maybe. So how many equations will be involved in the master equation kind of description of this model?**

**Infinitely many. But there were infinitely many already when we had just one, when we just had the mRNA distribution. Well, you know, infinite times infinite is still infinite. So long as it's a countably infinite number. But yeah, but it's still infinite, always. All right.**

**So what we want to do is divide up the states. So when somebody asks you for-- the equation's describing how those probabilities are going to vary, really what we're interested in is some derivative with respect to time of some probabilities described by m,n. We want to know the derivative with respect to time for all m,n's. So that's why there are infinite number, because m goes in one direction, n goes in another. Lots of them, OK?**

**Now it's always tempting to just write down this derivative and then just write down the equation. If you do that, that's fine, but I would recommend that in general what you do is you try to write a little chart out to keep track of what directions things can go. So for example, here we have the probability of being the m,n state. Now there's going to be ways of going here. And this is going to be going probability of being an m plus 1,n.**

**What I'm going to do is I'm going to give you just a couple minutes. And in two minutes, I want you to try to write down as many of the rates, the f's and n's that correspond to all these transitions. You may not be able to get through all of them, but if you don't try to figure out some of them, then you're going to have trouble doing it at a later date.**

**Do you understand what I'm asking you to do? So next to each one of these arrows, you should write something. So I'll give you two minutes to kind of do your best of writing these things down.**

7

**All right. Why don't we reconvene, and we'll see how we are? So this is very similar to what we did on Thursday. We have to remember that m's are the mRNAs, and this is what we solved before, where it's just a long row.**

**Now first of all, the mRNA distributions and the rates, do they depend on the protein numbers? No. So what that mean about, say, this arrow as compared to the arrow that would be down here? It's going to be the same, because n does not appear in that equation describing mRNA. If we had autoregulation of some sort, then it would. So let's go through.**

**All right. What we're going to do is we're going to do a verbal yelling out. OK, ready. This arrow.**

**AUDIENCE: Km.**

**PROFESSOR: This one here is, 3,2,1-AUDIENCE: Km. PROFESSOR: Km. All right. All right. Ready, 3, 2, 1. AUDIENCE: Gamma m times m. PROFESSOR: Gamma m times m. 3, 2, 1. AUDIENCE: Gamma n times m plus 1. PROFESSOR: Gamma m times m plus 1. Now remember that there are more mRNA over here then there are here, which means that the rate of degradation will increase. Now coming here, now this is talking about the creation and destruction of the proteins, changes in n. All right, this arrow here. Ready, 3, 2, 1.**

**AUDIENCE: Kp times m.**

**PROFESSOR: It's Kp times m. So this is the rate of creation, going from n minus 1 to n. That's fine. You know, I was looking at my notes from last year, and I got one of these things incorrect, so-- and then, OK, ready. This one here, 3, 2, 1. Kp times m. So here the**

8

**same rate, and should we be surprised by that?**

**So the number of proteins are changing, but here it's the number of mRNA that matters, because we're talking about the rate of translation, right? Now this one here, 3, 2, 1. Gamma p times n. And here, 3, 2, 1.**

**AUDIENCE: Gamma p times n plus 1.**

**PROFESSOR: Gamma p times n plus 1. All right. Perfect. Now this is, of course, as you can imagine, the simplest possible kind of set of equations that we could have written down. If you have other crazy things, you get different distributions, if you have autoregulation or if you have interactions of something with something else, or the same thing, so forth.**

**But I think it's really very useful to kind of write this thing down to clarify your thinking in these problems. And then you can fill out-- for change of probability, you have mn. You come here and you just go around and you count, take all the arrows coming in, and those are ways of increasing your probability. And ways going out are ways of decreasing your probability.**

**Now in all those cases you have to multiply these raw rates by the probabilities of being in all these other states.**

**So can you use the master equation to get these probabilities if you're out of equilibrium, out of steady state? So that's a question. So the master equation useful out of steady state? Yes. Ready. 3, 2, 1. All right. So we got a fair number of-- there is some disagreement, but yeah.**

**So it actually-- the answer is yes. And that's because you can start with any distribution of probabilities across all the states that you'd like. It could be that all of the probabilities at one state. It could be however you like. And the master equation tells you about how that probability distribution will change over time.**

**Now if you let that run forever, then you come to some equilibrium steady state. And that's a very interesting quantity, is the steady state distribution of these**

9

**probabilities. But you can actually calculate from any initial distribution of probabilities evolving to any later time t what the probability would be later.**

**This comes to another question here. All right. So let's imagine that at time t equal to 0, I tell you that there are m not mRNA and P not-- I always do this. I don't know, somehow my brain does not like this. Because the P's we want to be probabilities. We start with m not mRNA, n not protein.**

**And maybe it's a complicated situation. We can't calculate this analytically. So what we do is we go to our computer, and we have it solve how this probability distribution will evolve so that time T equal to some time-- if we'd like we can say this is T1. I'll tell you, oh, the probability of having m and n mRNA and protein is going to be equal to something P1.**

**Now the question is, let's say I then go and I do this simulation again. Now I calculate some other at time T1 again, the probability that you're in the m,n state. The question is, will you again get P1? So this is a question mark. And A is yes, B is no. All right. I'm going to give you 15 seconds. I think this is very important that you understand what the master equation is doing and what it is not doing.**

---

[← AUDIENCE: [INAUDIBLE]](03-audience-inaudible.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](05-audience-inaudible.md)
