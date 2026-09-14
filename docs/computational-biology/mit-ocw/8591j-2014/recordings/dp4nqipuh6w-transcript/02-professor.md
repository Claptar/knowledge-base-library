---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/dp4nqipuh6w-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/dp4nqipuh6w-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Greater than. So this thing is greater than 514. Now, if you just have scattering off something-- so let's say that we had a gold particle, and we shine-- what's going to be the relationship between lamba incident and lambda emission?**

**Is it possible to have the same wavelength come out as you put in of some object? Yes. If you just have something, a mirror, you can get back-- so it is possible. But in general, there's going to be some dissipation. It's a question of how much and so forth.**

**But certainly for something like fluorescence, you have a higher energy photon, and you have a photon that's emitted. And of course, energy goes as 1 over lambda.**

**Now, this is useful because you can actually spectrally separate things. I just want to highlight, though, that if this separation is of order 300 nanometers and our protein is-- that [INAUDIBLE] our GFP. Nicely drawn. Not even quite to scale. To scale, it's actually even smaller.**

**It's a factor of 100 in size. This thing is only 3 nanometers in size, 300 nanometers wide. Now, it's important to be clear about what this means, this diffraction limited spot. The first thing to note is that what it means is that if you have two proteins-- so for example, I add another one over here-- that it's going to be very hard to tell that we have those two proteins next to each other. Because the resulting fluorescence pattern will look essentially the same.**

**Will it be exactly the same? What's going to change? The intensity. The intensity, you expect to go up by a factor of two, absent some interaction between. You can, in principle, get interactions there. But let's for now assume that there's no interaction.**

**Right. Then the intensity wouldn't need to go up by a factor of two. But unless you're very careful about all of your optics and so forth, it's actually a challenge to use this intensity alone to distinguish these things. It's only-- so the statement with a diffraction-- you need these two proteins to be separated by something like lambda**

8

**over 2 in order for you to start to see the separation.**

**Right. Because then you have something that looks like this. Something that looks like this. And then the sum of those two, indeed-- so you say, all right, well, it looks like there are two molecules there.**

**Now, I just want to-- and the notion of a lot of these so-called super resolution techniques is figuring out a way to distinguish these things, and we'll maybe say something about that in a moment. But I just want to highlight that if we come back to the situation where we have a single protein there. Now the question is, how accurately can we tell where that protein is, if we know that there's just a single protein there?**

**Now in particular, this size of the spot is telling us something, but it might not be quite as strong of a limitation as it appears at first glance. And that's because in this case, well maybe I'll bring it back, what we see is a big spot. 300 nanometers, kind of wide.**

**But if we see this and we know it's just a single protein there, I mean, could the protein be over here? No. If the protein where over here, then the spot would be over there right. So actually, even though the size of the spot is 300 nanometers, in principle, if you want to know where that protein is, if you know there's just a single protein, well, in that case what you want to know is, where's the center of that distribution?**

**And that problem, well, the width of the distribution is relevant. But there's something else that's also very relevant. And quite generally, if you measure some quantity n times, and you want to know-- so you're measuring the height of min entering the army-- if you want to know the mean, what is it that determines your uncertainty around the mean?**

**Right. There's the sample size. Now, does the width of the distribution enter? Yeah. So in general, your uncertainty in the mean is going to go with the width of the distribution, sigma of whatever, divided by-- what do I put down here? Root of N,**

9

**where N is the number of samples that we take.**

**What this is saying is that as we sample this distribution more and more, does the standard deviation of the distribution, does it go to 0? No. These are all trivial statements, but I can't tell you how many times I see this getting confused.**

**OK. So if you measure many, many, many times, you get a very beautiful distribution. Right. The width of this region of the sigma, that you get very accurately. It's true also that your uncertainty in the width, that actually does go to 0. But the width of it, the width doesn't go to 0. The width of the distribution.**

**But your uncertainty in the mean, that goes down as 1 over root of N. And what is N in the case our detection business here? The number of photons. Right?**

**Now, of course, in the actual experiment, we don't get precisely this distribution. Instead, it's kind of sort of quantized somehow spatially, because we're actually detecting it on a CCD chip. All right. So you can go and do the math, figure out everything. But actually, that's not as much a limitation as you might have expected.**

**In many cases, the pixel size on the image plane is actually something like 100 nanometers. So this distribution that measure, although in principle it looks like this, what you actually measure is something that looks like-- well, maybe I should-something like that. Right. Because you have discrete pixels on the CCD.**

**And it feels that that should just kind of totally screw you. But if you go and do the math, you find it's not as bad as you might expect. So broadly, you do get essentially something that goes as 1 over the root of N, where N is the number of photons. And if you collect 10 to the 4 photons, that actually, it's a lot of photons.**

**So if we want to know the uncertainty in the center of our distribution, well, this thing, we might have something that's of order 300 nanometers here. We take the square root of 10 to the 4.**

**All right. So we get to divide by something like 100. And these are all very rough numbers. But the point is that we can get down to nanometer resolution in terms of**

10

**the uncertainty that which we know the mean of that distribution. Yes?**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
