---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/nndqjhtuqjw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/nndqjhtuqjw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today what we're going to do is finish off our discussion about oscillators. In particular, we're going to talk about alternative designs for oscillators. So rather than having these loops that are purely composed of negative interactions, negative feedback, instead we're going to talk about cases where you have both positive and negative interactions.**

**So in using this kind of combined network structure, you can generate what are known as relaxation oscillators, which have some really wonderful properties. In particular you can get more robust oscillations, relative to the parameters. But also the oscillations become tunable, i.e. you can change the frequency, without compromising, for example, the amplitude of the oscillations. So for both natural and synthetic oscillators these so-called synthetic oscillators are perhaps the way to go.**

**And then we're going to transition to more of the global structure of some these networks in the context of transcription networks within cells. And discuss this paper that you guys just read, the Barabasi paper, which is one of the world's most cited papers, I think. And then after thinking about this global structure, of how you might be able to generate these so-called power law structures, we're going to look a little bit more in detail to try to understand something about these network motifs. We've already talked about them a little bit in the context of auto regulatory loops, but now we'll talk about them in a little bit more generality, in particular in the context of feed forward loops. And then on Thursday we will get into some of the possible beneficial features of feed forward loops.**

**On Thursday we talked about the repressilator. So if you have x inhibiting y inhibiting z coming back and inhibiting x, that it's reasonable to expect that it might**

1

**generate oscillations. And indeed in the Elowitz paper that we read, such a synthetic circuit did indeed generate oscillations, but there were perhaps a few problems there, right? So one is that only about 40% of the cells actually oscillated, who knows why not. But also there were other problems that the oscillations seemed rather noisy, there was relatively rapid desyncronization.**

**Moreover, if you go and you ask, well is it possible, or how easy would be to change the period of the oscillations just by changing something like the degradation rate, what you'll find is that the oscillations are not very tunable. So I'll say the period, or the frequency, is not very tunable, and indeed this is a general feature of oscillatory networks that have purely negative interactions. We talked about a couple of these cases, for example, you can get oscillations just with negative auto regulation. And what is it that's necessary?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: What's that?**

**AUDIENCE: High coordination.**

**PROFESSOR: High coordination? You me-- oh you're--**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Cooperativity in the repression, that I think is necessary, but is it going to be sufficient? Even in this case where I just have, let's say that I say, x dot the rate of production, if this thing is just as a function of x, the sharpest it could be, this is infinite cooperatively, so it's maximal expression. And then when you get above some x critical all of a sudden you fully repress. If I just have this be the formula-did you guys understand what I'm referring to here? What would this generate? Would this generate oscillations? So it actually doesn't.**

**In the simple equation, where if we have x dot is equal to this function. So I guess this is a theta, I want to make sure I get this x, less than x critical, that's what this means. So with some [INAUDIBLE] rate beta, minus some alpha x. Does this thing**

2

**oscillate? No, and we had a simple argument for why did not oscillate, as well. Yes? Yell it out somebody, I'm sure somebody was here on Thursday.**

---

[Up: contents](index.md) · [[LAUGHTER] →](02-laughter.md)
