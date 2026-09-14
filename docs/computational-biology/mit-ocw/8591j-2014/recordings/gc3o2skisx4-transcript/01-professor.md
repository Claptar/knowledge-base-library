---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/gc3o2skisx4-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/gc3o2skisx4-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So, welcome to systems biology. There are many different numbers that you might have signed up for this class through. My name is Jeff Gore. I'm an assistant professor in the physics department. And I think that this is really-- it's a fun class to teach. I hope that those of you that stick around for the rest of the semester find that it's a fun class to take as well.**

**I just want to give a little bit of an introduction of the teaching staff, and then we'll go over some administrative details before-- most of today, what we'll do is we'll basically just spend an hour. I'll give you a flash summary of the course, and then you'll have a sense of the kinds of ideas we'll be exploring.**

**So, what is this thing, systems biology? So it's, I would say, ill-defined. But in general, we have this idea that, in many cases, the really exciting functions that we see in biology are arising from the interactions, at a lower level, of relatively simple components. So, the kinds of behavior that we'd like to understand are nicely encapsulated in this video of a neutrophil chasing a bacterium. And if I can-- if my computer is actually doing something, then-- there's something.**

**So, this is a classic video that many of you guys might have seen over the years. So, this was taken in the 1950s. It's, as I said, a neutrophil, which is part of your innate immune system. So, sort of the first line of defense. When you get a bacterial infection, for example, this white blood cell is going to chase the bacterium and eat it up before it can divide and harm you.**

**So, I'm going to play that over again, because it's pretty cool. So, the features that you want to try to pay attention to-- so, this is a single cell that somehow is able to track this bacterial invader. It's using chemical cues in order to figure out where it is**

1

**that bacterial cell is going. It's able to disregard these red blood cells that are in its way, push them aside, change direction, before it eventually captures this bacterial cell. So, all of these are striking, amazing information-processing capabilities, where that information has to be coupled not only to some sort of decision-making within that cell, but also, it has to be transduced into these mechanical forces and motions that allow that cell to capture the bacterial cell. So, let's try it again.**

**So, here it is. You can see the bacterial cell is here. So, it's ignoring this other cell, keeping focus on this one, pushing aside the red blood cells, so it can follow it along. Every now and then-- now the cell changed direction. But eventually, you can see it catches up to the bacterial cell and eats it. Now you're not going to get sick from that infection.**

**So, that's an example of the kinds of remarkable behavior that can be implemented even just by a single cell. So, we know that, as humans, we have brains with 10 to the 12 neurons or so. So, maybe you'd say, it's not surprising that we can do fancy things. What's remarkable is that even at the level of an individual cell, it's possible to implement rather sophisticated information processing capabilities. So, this is the kind of thing that we'd like to be able to say something about by the end of the class.**

**Many of you, I think, probably read the course description, and this gives you a sense of the kinds of topics that we're going to be covering over the course of the semester. I'm not going to read it to you. But one thing I want to stress is I brought up this general idea of systems biology. How is it that function arises from interactions of smaller, simpler parts?**

**I think it's very important, right at the beginning, to be clear that there are really, I'd say, two distinct communities that self-identify as studying systems biology. And they're-- to simplify it a bit, what I would say is that, basically, there's the physics, or physics-inspired community, where-- and I'm in the physics department, so that's where I fall, and where this class is going to be. So, it's really trying to use some simple models from nonlinear dynamics or stochastic processes combined with**

2

**quantitative experiments, often on single cells, in order to try to illuminate how this cellular decision-making process works. And on over the next hour, you'll see-- get a flavor of what I mean by this.**

**Now, there's another branch of systems biology that is also very exciting, and that many of you may want to learn more about in the future. And maybe some of even were thinking that this was what the class is going to be in. But let me explain what is.**

**This other branch, I'd say, is more influenced by computer scientists and engineers, where what they're really trying to do is use complex models, machine learning techniques, and so forth, in order to extract signal from large data sets. And this is also, again, systems biology because it is trying to understand how the global properties of the cell result from all these interactions, but it's a rather different aesthetic take on the subject. And, indeed, much of the activity, that one would be doing here is different from the more physics branch of systems biology.**

**So, if what you were looking for was more of this large data set, high throughput, branch of systems biology, then you may not be at the right place. And there's an interesting fact, which is that if you decide that you want this other branch of systems biology, then, very conveniently, you actually have space in your schedule, because Manolis Kellis is teaching a class in computational biology-- really, this other branch of systems biology-- at the same time. So, if you think you're at the wrong place, you're welcome to just sneak out now. Go to over 32-141, and I'm sure that he will welcome you, and no hard feelings.**

**Similarly, in the spring, there's another computational biology class that some of you may be thinking about. And this is taught by Chris Burge and company, and also, I'd say, maybe more of this other branch of systems biology. And, finally, once again, in the spring there's a class, quantitative biology for graduate students, that I'd say probably assumes somewhat less mathematical background. So, if after looking at the syllabus, or maybe even getting started looking at the first problem set, if you think that maybe this class is expecting too much, then you may want to consider**

3

**taking quantitative biology in the spring, and maybe taking systems biology-- this class-- next fall.**

**So, on that note, I want to say something about the prerequisites. The major challenge with this class-- certainly, teaching it, from my standpoint, and I think for many of you taking it-- is that there's a wide range of different backgrounds. So, we can maybe get a sense of that now. Just a show of hands, how many of you are undergraduates? So, we've got a solid third or so. How many are-- mixing together undergraduate and graduate-- but how many of you are in the physics department at one level or another? So, we have maybe, again, a third.**

**Biology department? So, we have a quarter, a fifth. Engineers? So, a substantial fraction of engineers. And chemists? We've got a few of them. Mathematicians? All right, we've got one.**

**So, if you did not raise your hand, where you based, physically, intellectually, something? Did we get everybody? OK.**

**So, you can see that there's a really broad range of different backgrounds. And what that means in a concrete way for us is that I will very much try to avoid using unnecessary jargon or unnecessary mathematics. I think that mathematics is a wonderful thing, but in some cases it, I think, obscures as much as it illuminates.**

**So, for me, I very much try to focus on conceptual understanding. And on top of that, I try to build-- you like math, too. But I think that it's very important to be able to, for example, plot your solution. So, after you derive some fancy equation describing something, you should know whether that thing goes up or down as a function of something or another. And I think it's very easy to lose sight of these basic aspects when we get too deep into the mathematical equations.**

**But, that being said, we do, I'd say, expect something-- not necessarily full-- you don't have to have taken the full class, 701 or 702, but at least a solid high school class of biology. If it's been more than 10 years since you took a biology class, you might want to take one before coming here. You could, in principle, catch up, like all**

4

---

[Up: contents](index.md) · [things. →](02-things.md)
