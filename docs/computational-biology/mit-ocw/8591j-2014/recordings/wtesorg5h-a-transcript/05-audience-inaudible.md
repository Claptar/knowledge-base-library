---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/wtesorg5h-a-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/wtesorg5h-a-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: That's right. That's right. As far as the model goes, it could be that the prey are really-- one species was just a point mutation. Then you'd say, oh yeah. That's kind of evolution. Or it could be two different prey populations and so forth. Right?**

**And depending upon what information you have access to, you would either be aware of these things or not. In this case, they just look under the microscope and say, oh yeah, this looks like an algae, or whatnot. And maybe they know that it's the same species. But they could be different in lots of different ways.**

**And I think this discussion is highlighting that a lot of the same effects that you see**

28

**in ecology also you see in evolution and vice versa. And depending upon your focus, you might want to put it more in the bin of evolution or in terms of population dynamics. I think that's a matter of taste at some point, actually.**

**Yeah. Because they say rapid evolution. And I think--**

**AUDIENCE:**

**[INAUDIBLE].**

**PROFESSOR: Yeah, right. So I think that different people will have different takes on this. I think, once again, this is really very much from the standpoint of an ecologist, this is rapid evolution. Because every cycle, the allele frequency is changing. And that's what's maybe leading to this.**

**But the thing is, it's very easy for you to read certainly the title, and come away thinking it's something different from what it was. I agree.**

**But one of the things I like about this whole line of research that took place over the course of say, 15 years, was that they did these nice measurements. They're guided by models. They saw some things that they were expecting, some things they couldn't explain.**

**And then they went and did more modeling. And then they could explain it. And that guided this experiment. Because before what they did is they just took kind of the sludge, or whatever, from the lake. So there were many different types of algae and of the rotifer, for that matter. And then they looked at the predator/prey oscillations between those.**

**And then in this paper what they did is they took individual prey populations that came from a single prey. So they were kind of isogenic. Of course eventually they would evolve, and blah, blah, blah. But in this case they took individual isolates from the prey. And then what they saw is that these two features went away.**

**The oscillation period was more what they were expecting. And they got the 90 degree phase lag. So it's was really a case of these models led to the experiments where they took kind of clonal prey. And then they recovered their classical**

29

**predictions.**

**And indeed, they've recently done some other measurements that I think were quite nice. They had an ecology letters paper just a couple years ago where what they did is they took two different algae that had different types embodying these tradeoffs that we were talking about. In particular, one of the algae can divide rapidly. But it kind of exists as singles.**

**Another algae is kind of clumpy. So this algal type was able to divide more rapidly than this algal type. But this type was harder to eat just because it was clumpy. OK?**

**It's one of things that once you hear it, you say, oh yeah. Sure. But then in the abstract, when you read this 2003 paper, you think, oh, I can't imagine what kind of behavior could possibly help the algae avoid these rotifers.**

**But then in this ecology letters paper, what they did is they actually tracked population densities of this type, this type, and of the rotifer over time. So then they could see all three sub-populations oscillating. So then you can really kind of see how this evolution, if you want, or you could just say it's ecology. Because it could be different species for all we care.**

**But in any case, it's certainly prey heterogeneity anyway you look at it. Whether it's evolution or ecology. It's heterogeneity in the prey population that leads to these very qualitatively different population oscillations. Any other questions on that before we--**

**And so just for the last few minutes I'll say something about this question of noiseinduced oscillations. This is going to be something you're going to be playing with over the next week. So you'll be experts eventually.**

**And the discussion in the homework is really guided by this paper by McKane and Newman. All right. So McKane. Newman. McKane is a professor at Manchester.**

**And what they showed is that if you take this model here, did this model have limit cycle oscillations, sustained oscillations? No. So this model where we include the**

30

**carrying capacity of the prey, this does not have sustained oscillations. So you take a model like this that just has a stable spiral. Now this is a model in the context of-it's a differential equation model.**

**Now the question is, how do you incorporate noise? Just the fact that individuals give birth, they die at random times. The first order way that we often think to do this is we just add some noise on to the differential equations.**

**So what we do is, you might say, oh well, you could add some a to x, and some a to y. Maybe this noise should be proportional to x or something. So you could think about the strength of this might be some pre-factor. So you could just take kind of a [INAUDIBLE] approach where you add noise onto the differential equations. And then what you get is a noisy kind of path to that fixed point.**

**The perhaps surprising thing is that instead of adding noise to a differential equation, if instead you start with the individual based approach, and you take kind of a master equation approach where you say they're individuals and they're doing something. Individual predators are eating individual prey, et cetera.**

**So if instead you take a master equation, just like what we did for the chemical equations modeling the cells and so forth that we talked about at the beginning of the class, if you formulate this predator/prey system as an underlying set of kind of individual based interactions, then what you actually find is that you get surprisingly large sustained oscillations. So you really end up with a situation where this thing comes. And it's noisy, of course. But it kind of comes around here in some way that looks like this.**

**And you'll see this in your simulations next week where-- and I don't know if you can see this at all. But this is some plots of predator and prey at reasonably large numbers, where you can actually have 1,000 predator or prey. Somehow you can get some sort of resonant enhancement of these oscillations.**

**And kind of what's going on is that the demographic fluctuations of the demographic noise excites the system at all frequencies. But then there is a characteristic**

31

**frequency given basically by this frequency of the inherent oscillation there that is somehow amplified. So you end up with a situation where you get these oscillations. And they're noisy and whatnot. But it's really because it's this particular frequency that was amplified. And just because it takes a long time for those oscillations to go away.**

**So you can imagine that the amplitude of the oscillation falls off as kind of a root end scaling, because it's kind of a demographic type noise. So it is true that the relative amplitude of these oscillations, it gets larger as you to smaller population sizes. But it still ends up being a surprisingly large effect.**

**And you'll see how this plays out in this model that's basically guided by this paper. And this was a PRL in 2005. Incidentally, other people have since studied how these sorts of ideas can result in noise-induced pattern formation, as well. All right, with that, I will let you guys go. Have a good Thanksgiving. I'll see you guys on Tuesday.**

32

---

[← AUDIENCE: [INAUDIBLE]](04-audience-inaudible.md) · [Up: contents](index.md)
