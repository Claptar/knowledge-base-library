---
title: '[INAUDIBLE].'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/nndqjhtuqjw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [INAUDIBLE].

**Source:** `recordings/nndqjhtuqjw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**That's right. So this is just-- This is just an x dot, there's no x double dot, so that means the derivative of x, the single value is a function of x, that means that we can't get any oscillation here. And then remember we analyzed this model where we explicitly included the mRNA, so then we just had that x comes, and what it does, is it represses expression of this mRNA for x, and then this mRNA comes back and makes x. Right?**

**And in this model, was this sufficient? Did this give oscillations? No, so this also here, there was no oscillations. Again here, there were no oscillations. But I did tell you that you could do something more to get oscillations, just with a single protein repressing itself. So you need more delays. So if you add delays, then it's possible to get oscillations. So those delays could be in the form of having a model where you explicitly take into account that first mRNA is made, and then that goes, and then you translate that to make some monomer, and then the monomer has to maybe fold, and then the folded protein maybe has to dimerize in order to do a repression.**

**So if you have a more detailed mechanistic model, that includes all these steps, that kind of introduces some sort of delay, that in principle can lead to oscillations in such a circuit. Or if you wanted to, you could just explicitly put in a delay. So you could say that x dot, instead being a function of x, instead what you can do, is you could say, well its actually a function of x at some time, t minus tao. So instead of having the rate of production of x be a function of x, at that moment in time, instead it could be a function of x at some previous time. Doing that, that's a very explicit form of delay.**

**And that can also be used to generate oscillations in a simple negative auto**

3

**regulatory loop. These are all different kind of approaches for encoding delays into a model and in various approaches will give you oscillations. Yes? AUDIENCE: Question for the repressilator, when you say the period is not tunable, it's because the mRNA lifeline is very difficult to-PROFESSOR: All right, when we say-AUDIENCE: --in the model you can-PROFESSOR: Yes, that's right. In the model you can, in principle-- So what I mean when I say this is that in this class of model, so you could also have, instead of this repressilator with three, you have the so-called pentalator, where you have five proteins and each is repressing itself. So these all have similar features, so all have these odd numbers of proteins going around and repressing one another. And so you can write down the model with seven, if you want. But in all these cases, it's not tunable. What we mean by that is that, when you tune the frequency, you in general lose the amplitude of the oscillation. So the amplitude will go down.**

**There was a very nice paper that was written in 2008 on this topic, written by Jim Ferrell at Stanford. So I just want to mention this. So its Ferrell, at Stanford, this is a paper in Science 2008, and it's called Robust Tunable Biological Oscillations from Interlinked Positive and Negative Feedback Loops. So nice title, I like titles that say something. So it's sort of the ultimate short version of an abstract, right, if you can do it I recommend it.**

**Incidentally in graduate school, I once wrote a paper with four words, short words, DNA over-winds when stretched. Nice statement, you may or may not actually know what I mean by that, but it's a nice short, title, it's a statement. I encourage you to think about that when you're writing your papers.**

**So he wrote this paper where, he said, all right, well, oscillations are really important. Thinking about context of heart rhythms, or cell cycle, or this or that. Oscillations are important, but if you go and you look at the circuits that are generating oscillations in biology, they often have so-called interlinked positive and**

4

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [negative feedback loops. →](05-negative-feedback-loops.md)
