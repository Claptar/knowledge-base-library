---
title: probabilities are 0 above some number?
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/exbo08-78iu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# probabilities are 0 above some number?

**Source:** `recordings/exbo08-78iu-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Oh no, that's not at all a silly question, because-AUDIENCE: [INAUDIBLE] PROFESSOR: Exactly. Right. And yes, it's a very good question. So I told you this is an infinite set of differential equations. But at the same time I told you this master equation's supposed to be useful for something, and kind of at the face of it, these are incompatible ideas. And the basic answer is that you have to include all the states where there is a sort of non-negligible probability. We could be concrete, though. So let's imagine that I tell you we want to look at the mRNA number here. And I tell you that OK, Km is equal to-- well, let me make sure. Gamma m. What are typical lifetimes of mRNAs in bacteria again? AUDIENCE: [INAUDIBLE] PROFESSOR: Right. Order a minute. So that means that-- let's say this is 0.5 minutes minus 1. To get a lifetime of around 2 minutes. And then let's imagine that this is then 50 per minute. So an mRNA is kind of made once a minute. There's 50 of them. That's a lot, but whatever. There are a few genes. Minute. I wanted the number to be something. So there's a fair rate of mRNA production. Now how many equations do you think you might need to simulate? So we'll think about this. First of all, does it depend upon the initial conditions or not? AUDIENCE: Maybe. PROFESSOR: Yeah. It does. So be careful. But let's say that I tell you that we start with 50 mRNA. The question is, how many equations do you think you might have to write down? And let's say we want to understand this once it gets to, say, the equilibrium. All right. Number of equations. Give me a moment to come up with some**

12

**reasonable options. Well, these are-- let's say that this could show up on your homework. So the question is, how many equations are you going to program into your intersimulation? And it may be-- doesn't have to be exactly any of these number, but order. Do you guys understand the question?**

**So we need a different equation for each of these probabilities. So in principle we have-- the master equation gives us an infinite number of equations. So we have d the probability of having 0 mRNA with respect to time. That's going to be-- any idea what this is going to be?**

---

[← AUDIENCE: [INAUDIBLE]](05-audience-inaudible.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](07-audience-inaudible.md)
