---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/xnnxlsy-f-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/xnnxlsy-f-s-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**Circadian.**

**The circadian oscillator. That's right. So the idea there is that there's a G network within many organizations that actually keeps track of the daily cycle and, indeed, is entrained by the daily cycle. So of course, the day, night cycle. That's an oscillator. It's on its own. And it goes without us, as well.**

**But it's often useful for organisms to be able to keep track of where in the course the day it might be. And the amount of light that the organism is getting at this particular moment might not be a faithful indicator of how much light there will be available in an hour because it could just be that there's a cloud crossing in front of the sun.**

**And you don't want-- as an organism-- to think that it's night. And then, you shut down all that machinery because, after that cloud passes, you want to be able to get going again. So it's often useful for an organism to know where in the morning, night, evening cycle one is.**

**And we will not be talking too much about the circadian oscillators in this class. Although, I would say to the degree of your interest in oscillations, I strongly encourage you to look up that literature because it's really beautiful. In particular, in some of these oscillators, it's been demonstrating you can get the oscillations in vitro. I.e, outside of the cell.**

**Even in the absence of any gene expression, in some cases, you can still get oscillations of just those protein components in a test tube. This was quite a shocking discovery when it was first published. But we want to start out with some simpler ones.**

**In particular, I want to start by thinking about auto repression. So if you have an**

2

**y g p y**

**p ,**

**auto regulatory loop where some gene is repressing itself, the question is does this thing oscillate. And indeed, it's reasonable that it might because we can construct a verbal argument.**

**Starts out high. Then, it should repress itself so you get less new x being made. So the concentration falls. So maybe I'll give you a plot to add to it. Concentration of x is a function of time.**

**You can imagine just starting somewhere high. That means it's a repressing expression. So it's going to fall. But then, once it falls too much, then all of a sudden, OK, well we're not repressing ourselves anymore.**

**So maybe then we get more expression. More of this x is being made. So it should come back up. And then, now we're back where we started. So this is a totally reasonable statement. Yes?**

**AUDIENCE: [INAUDIBLE]?**

**PROFESSOR: Well I don't know. I mean, I didn't introduce any damping in here. The amplitude is the same everywhere.**

**AUDIENCE: So you're saying that you could actually have something--**

**PROFESSOR: Well I guess what I'm really trying to say is that just because you can construct a verbal argument that something happens does not mean that a particular equation is going to do that. Part of the value of equations is that they force you to be explicit about all the assumptions that you're making. And then what you're going to do is you're going to ask, well, a given equation is a mathematical manifestation of the assumptions you're making.**

**And then, you're going to ask does that oscillate. Yes/no? And then you're going to say, OK, well what would we need to change in order to introduce oscillations? And I'll just-- OK. So this is definitely an oscillation. The question is, should you find this argument I just gave you convincing? And what I'm, I guess, about to say is that you shouldn't.**

3

**But then, we need to be clear about what's going on and why. And just because you can make a verbal argument for something doesn't mean that it actually exist. I mean, that's a guide to how you might want to formalize your thinking.**

**And in particular, the simplest way to think about oscillations that might be induced in this situation would be to just say, all right, well the simplest model we have for an auto regulatory loop that's negative is we say, OK, well there's some alpha 1 plus protein and minus p. So this is, kind of, the simplest equation you can write that captures this idea that this protein p is negatively regulating itself in a cooperative fashion maybe.**

**Now it's already in a non-dimensionalize version. Right? And what you can see is that, within this realm, there are only two things that can possibly be changing. There's how cooperative that repression is-- n-- and then, the strength of the expression in the absence of repression.**

**And as we discussed on Tuesday, alpha is capturing all these dynamics of the actual strength of expression together with the lifetime of the protein together with the binding. You know, the binding affinity k. So all those things get wrapped up in this a or alpha rather.**

**All right, so this is, indeed, the simplest model you can write down to describe such a negative auto regulatory loop. Now the question is now that we've done this, we want to know does this thing oscillate. And even without analyzing this equation, there's something that's very strong, which you can say.**

**So in theory we're going to ask is it possible for this thing to oscillate. All right. Possible. Your oscillations, we'll say oscillations possible. And this time, referring to mathematically possible. So maybe this thing does oscillate. Maybe it doesn't. But in particular, without analyzing it, is there anything that you can say without analyzing it?**

**We're just going to say is it possible. Yes or no? If you say no, you have to be prepared to give an argument for why this thing is not allowed to oscillate. I'm**

4

**talking about this equation. Do you don't you understand the question that I'm trying to ask?**

**And we haven't analyzed this thing yet. But the question is, even before analyzing it, can we say anything about whether it's mathematically allowed to oscillate? I'll give you 10 seconds to think about it. And if you say no, you get to tell me why.**

**All right, ready? Three, two, one. All right, so we got a smattering of things. So I think this is not, obviously, a priori. But it turns out that it's not actually. It's just mathematically impossible for this hing to oscillate. And can somebody say why that might be?**

**AUDIENCE: Because it might be you could only have one value of p dot?**

**PROFESSOR: Perfect OK. So for a given value of p, there's only some value of p dot that you can have. And in a particular-- so p here is like a concentration of x. So I'm going to pick some value, randomly, here of p.**

**And what you're pointing out is this is a differential equation in which if you give me or I give you the p, you can give me p dot. And there's a single value p dot for each p. And in this oscillatory scheme, is that statement true?**

**No. What you can see is that, over here, this is x slash p concentration of x. We're using p here because we're about to start talking about mRNA So I want to keep the notation consistent.**

**What you see is that the derivative here is negative. The derivative here is positive. Negative, positive. So any oscillation that you're going to be able to imagine is going to have multiple values for the derivative as a function of that value just because you have to come back and forth. You have to cross that point multiple times.**

**So what this is saying is that since this is a differential equation-- and it's actually important that it's a differential equation rather than a difference equation where you have discrete values. But given that this is a differential equation where time is taking little, little, little steps and you have a single variable, it just can't oscillate.**

5

**So for example, if you're talking about the oscillations the harmonic oscillator the important thing there is a you have both the position in the velocity see these two dynamical variables that are interacting in some way because you have momentum, in that case, that allows for the oscillations in the case of a mass on a spring, for example. Question.**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
