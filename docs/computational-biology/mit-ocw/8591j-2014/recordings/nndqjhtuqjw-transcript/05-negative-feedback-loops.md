---
title: negative feedback loops.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/nndqjhtuqjw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# negative feedback loops.

**Source:** `recordings/nndqjhtuqjw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**There are many cases where you have, some x that actually is positively, it's kind of activating itself. And this is very much something that will not lead to oscillations on its own. It might be bistable, which is interesting, but not oscillations on its own. But then there's also maybe a negative feedback loop through another protein.**

**And the idea is that this one somehow operates-- this one's fast, and this one's slow. And the key feature of these relaxation oscillators is they are two time scales. And it's the slow time scale that specifies the period of the oscillation, and this fast one kind of locks the system into these alternative states. And this helps maintain the amplitude, because it has this nature being bistable, right, so it's on or off. So this helps you maintain amplitude, so this is kind of in charge of amplitude, and this one over here is in charge of the period.**

**So what you can imagine that by changing this time scale, you change the period of the oscillation, whereas this loop allows you to maintain the amplitude. And what Jim's group did computationally in this paper, is they analyzed many different circuit designs that can lead to oscillations, and they showed that for the loops that are made of purely negative interactions like this, if you change a parameter in order to change the period, you'll also in general make the amplitude of the oscillations drop dramatically.**

**So that's the sense in which they're not tunable. Whereas if you have this kind of design, you can actually tune over, in some cases a very wide range, but maintain the amplitude of the oscillation. And in addition to being tunable, these things also end up being robust in various ways. The oscillation is maintained subject to various kinds of-- If you twiddle with the parameters, you double this, you have that, you still get nice oscillations here, whereas in those designs you tend to lose the oscillations more easily.**

**So they claim that based on that, that these might be more evolvable. So even in cases where you don't need to tune the period, maybe you still end up evolving towards this design, just because it's robust to stochastic fluctuations in the**

5

**concentrations of things, but also it might be easier to evolve these sorts of oscillations.**

**Are there any questions about the kind of intuition behind this for now?**

**There's a nice kind of circuit analogy that people often talk about in the context of this. So if you imagine you have some battery, with some voltage, v, well, we'll say v battery, some capacitor over here, but over here you have something that will spark at some voltage, some v t, you get a spark. Now the question is, well, what happens over time if the threshold is less than v battery? We maybe should have a resistor in here.**

**So the threshold is less than v battery, then this can generate nice oscillations in the voltage say across the capacitor as a function of time, that are tunable. Because if you plot as a function of time. This is the voltage across the capacitor, where up here we might have the v, the battery, here we might have v threshold. Now in the absence of-- This thing's that's going to short periodically, we're just going to charge up the capacitor. So in principle, there's going to be this standard r, c time constant, coming up to here, but before we get there, we get the spark. So then we discharge across here and this drops. So you get something that looks like this.**

**Now you can imagine by changing, for example, the resistor, you can change the rate that this thing, the capacitor, will charge up. But the amplitude of the oscillations stay constant, because that's set by the voltage threshold across this-- where it shorts. This is capturing this dynamic of the separation of time scales. So there's a slow time scale, which is this r, c time constant, and then there's the rapid time scale is where this shorts out. So you can imagine that this is an example of an oscillatory signal that we can to tune the frequency without sacrificing the amplitude.**

**What we've said so far is that there are engineering analogs to these sorts of relaxation oscillators. We can model various synthetic circuits, or we can look at natural oscillatory networks, in order to get a sense of what's going on. But of course, a major goal of this kind of system synthetic approach to the field, is that if all this stuff is really true, we should be able to build it.**

6

**y ,**

**And there's a very nice demonstration of this, also in 2008, by Jeff Hasty's group. So Jeff Hasty was actually trained as a high energy theorist, and then I think it was during his postdoc, maybe he switched into experimental biology. Went and did his postdoc, I think, with Jim Collins. And then eventually now has his own group doing systems synthetic biology.**

**In this paper, it was a Nature paper in 2008, it's called A Fast Robust and Tunable Synthetic Gene Oscillator. It's a nice statement, tells you what he's about to do. The data here, this is again using this basic insight of having both interlinked positive negative feedback loops in E. coli. He demonstrated that he can get really beautiful oscillations, in essentially all the cells, and that they're tunable, enter n period, by a factor of three, or four, or so, by a fair amount. And indeed as fast as 13 minutes, the oscillatory period. Which is pretty nice, right? So I encourage you to check out this paper.**

**This paper was also an example of how it was in principle possible to get oscillations just by doing negative auto regulation. Right, so this was a case where they designed a gene network that they could tune and had this wonderful property. But then after they did that they noticed that in their model at least, they could get oscillations in some parameter regime, just by having the negative auto-regulatory loop. And as a result of all these intermediate processes, of protein maturation, and so forth, and then they went and they constructed that network, and they showed that that could also oscillate.**

**So again this is an example of the interplay between modeling, experiment theory, modeling, And Jeff Hasty has gone on to write another several, really beautiful papers looking at these sorts of oscillations, looking at how you can get synchronization of oscillators, and you get period doubling ideas. It's really a whole string of wonderful, wonderful papers. So I encourage you to, if you're interested in oscillations, to look at Jeff Hasty's work over the years.**

**If you want a quick introduction to these papers, I also wrote a news and views in**

7

**Nature on these two papers. So you can read that, it's only a page. Although I guess you won't hear anything that you haven't already heard probably.**

**Any other questions about this idea of how we can use both positive and negative feedback in order to get some nice oscillatory properties? OK, then let's move on. What did you guys think of this paper, the Barabasi paper? Good, bad, difficult, easy?**

**AUDIENCE: Why does it have so many citations?**

**PROFESSOR: Why does it have so many citations? All right that's an inter-- and you should look at how many-- according to Google Scholar, I haven't checked this year, but it's probably 20,000 citations. I mean it's--**

**AUDIENCE: Is it a cult thing?**

**PROFESSOR: It's a cult thing. Well, I don't know. That might be exaggerating.**

**AUDIENCE: I mean it's a nice paper.**

**PROFESSOR: Yeah, right. So this is interesting, and I think that the basic answer is that there are networks that are relevant in many, many, many fields, which they allude to. And there are many researchers that have been excited about studying those networks in many, many fields, and many, many, many of the networks that are observed in nature or social science, the web, everywhere, they have these power law structures. And this is the first clear simple mechanism to generate it. My understanding is that actually a mathematician decades before, actually did demonstrate that this kind of thing could be constructed, that would lead to this, but that paper doesn't have 20,000 citations.**

**I mean like it's a lot of these things, you have to be the right time, right place, and have the right idea. AUDIENCE: Yeah, I guess my main thought about the paper is exactly that, the interesting thing about it was, it came out at about the time that data on large networks was readily**

8

**available.**

**PROFESSOR: That's right. There's a reason that this paper was published at this time, and of course if Barabasi didn't do it here, someone else would have done it a year or two later. But it was really that the data were available everywhere, and we were seeing these power law distributions, and it's really crying out for an explanation. I think it's- You know sometimes people complain, that they say, oh yeah, you know I could have come up with this idea, it's not that deep. And maybe you could have, but you didn't.**

---

[← [INAUDIBLE].](04-inaudible.md) · [Up: contents](index.md) · [[LAUGHTER] →](06-laughter.md)
