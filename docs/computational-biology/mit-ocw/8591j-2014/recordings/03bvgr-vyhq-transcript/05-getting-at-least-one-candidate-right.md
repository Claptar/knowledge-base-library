---
title: getting at least one candidate, right?
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/03bvgr-vyhq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# getting at least one candidate, right?

**Source:** `recordings/03bvgr-vyhq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: So I'd say lambda has to be much, much larger than 1. So once you're at lambda of 100, it looks like a Gaussian. And in Sunney's paper, he had a comment about this. Does anybody remember what it was? Was mRNA production really well described as-- they mention that actually there is some violation of this model in the data. AUDIENCE: Does it go into eukaryotes? PROFESSOR: Oh, as soon as you go into eukaryotes, this is why I stay away from them. But even in their data, in E. coli, they actually observed a deviation. So what they found is that there was a cell cycle dependence to this bursting rate, i.e. the mRNA production over the course of the cell cycle. And presumably their conclusion of this was that you have this guy. And then he turns into, gets longer. And then eventually he septates, and then you get two cells.**

**What he found is that these longer cells had actually a larger rate of mRNA synthesis than the smaller cells. And actually this makes sense. Because here you maybe have just one copy of the genome. Whereas here you might have-- you're making a second copy. So you might have two copies of that gene. So it may make sense that this bursting rate should grow.**

**But does that mean that you should not expect it to be a Poisson distribution for the number of bursts per cell cycle? No. It actually is still-- it still is described by a Poisson. Because you can just say, this is the cell cycle. And here this is Poisson of sum lambda 1. Here is a Poisson of sum lambda 2. So there could be a different rate over the course of the thing. But you still have just two Poissons. You still get another Poisson. So adding Poissons, gives you backup Poisson. They don't have to have the same mean lambda.**

**I just want to make one comment about what you have to do once you start thinking about eukaryotes. And the basic-- so you can see the gamma distribution can either**

27

**be peaked at 0, or it can be peaked at nonzero value. So most, for like highly expressed proteins, you'll see that it looks something like this.**

**Now for eukaryotes, you also have to consider there's some rate that you go between an active and inactive promoter. And this actually makes things much more complicated. So there's a rate going to inactive, a rate going to active. And so now if you look at, for example, the mRNA number per cell, you'll see that it is no longer a Poisson.**

**And I encourage you, if you're curious about such things, to come up and look at this. The solution for the steady state distribution has been solved analytically. For example, Arjun Raj, who is the author of the review that you guys just read, derived this equation here, which I don't know if you can see. But even from a distance, you can see that this is the solution. And this is just for the mRNA distribution. This is not even getting to the level of the protein.**

**And it involves many gamma functions, as well as a confluent hypergeometric function of the first kind, which is a disaster. But he went to Courant. He was an applied mathematician. So this is, I guess, this is what you can do after doing a PhD in applied mathematics.**

**The point though is that it ends up being very complicated. And you can get hugely varying distributions for the mRNA. And indeed this is seen in individual cells. If you look at mammalian cells, just at the mRNA level, you can have some cells that have hardly any mRNA, some that have a huge number. The protein distributions actually end up being more regular than the mRNA distributions. Because of this difference in lifetime.**

**So the mRNA numbers may fluctuate wildly. But the protein numbers will fluctuate less, because they last longer. So then you do some averaging over this crazy mRNA business.**

**Now in the last-- yeah, go ahead.**

**AUDIENCE: In terms of timescale, like all this is switching to the active and inactive promoter,**

28

---

[← AUDIENCE](04-audience.md) · [Up: contents](index.md) · [like to the other-- →](06-like-to-the-other.md)
