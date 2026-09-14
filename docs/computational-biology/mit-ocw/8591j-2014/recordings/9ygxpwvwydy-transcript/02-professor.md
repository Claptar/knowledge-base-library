---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/9ygxpwvwydy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/9ygxpwvwydy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Why don't we go ahead and reconvene, so we can kind of try to figure out what is going on here. I just want to see if anybody has changed their opinion as a result of discussing with their neighbor. All right, let's see it. 3, 2, 1.**

**Some people are not even willing to-- all right, OK, so it's interesting. So now, actually, it seems like there is some convergence to this. Should I feel like that you guys in general have more accurate votes than past years somehow. I don't know.**

**So let's try to figure out why it might be that and what this thing standard deviation is. Let's try to figure out what all these things are.**

**So the idea is that we're going to measure some quantity, but it's a measurement with error. And for now, we'll just assume that the measurement error is Gaussian distributed, because otherwise, we get confused and everything.**

**So let's say-- so what we're going to do is we're going to measure some quantity with error. OK, so it's-- Now, what we're interested in is not really the width of the resulting distribution, because that's a result of how accurate, how good we are as experimentalists.**

**What we're really interested in is this true quantity, so the mean of our distribution. We want to know mean. Now, if you read the supplemental section of this paper, what you'll see is that there's a significant standard deviation to their measurements, where the standard deviation, they don't actually quote exactly what it is.**

**But they have plots of the histograms, where like, for example, this is a histogram of the different growth rate measurements across those 48 samples, and actually, in this case, even more than that. But what you see is that the standard deviation might be 3%, 4%.**

**So the standard deviation is actually something that's big. Now the question is, what we really want to now is, how the mean of these distributions are shifting, because we want to know something about this true underlying growth rate deficit, because each individual measurement is a rather noisy measurement.**

10

**And indeed, in this case, the noise is larger than the signal. But if we believe that we don't have a shifting systematic error, then we can average that out just by making many measurements.**

**So the question is, so the standard error of the mean, what it's telling us about is that if you measure this quantity n times, you get some mean. So let's say that this is a-- ooh, it's a little bit of a broad somehow Gaussian.**

**So this is a histogram of our measurements of this thing. And what we want to know is the mean of this distribution. So this is similar to our discussion of super resolution microscopy.**

**And the question is, how will the mean be distributed if you have these n measurements? It's a Gaussian distribution. And it's certainly a Gaussian distribution, because of course, if we-- what we're doing is we're measuring a bunch of Gaussians.**

**And we're going to add them all together. And then we're going to calculate the mean. So we definitely get a Gaussian. And indeed, because of the central limit theorem, this is also saying that even if your errors were not distributed super Gaussian, even if they were a little bit funny shaped, the resulting distributions of the means will look more like a Gaussian.**

**Now, what we often plot is the standard error of the mean, which is kind of the plus or minus 1 sigma of the distribution of the mean. So if we go and we sample from this distribution n times, we'll get some value. If we sample from it again, we'll get some other value, so forth.**

**Now, the distribution of the means we're going to calculate is not going to be a representation of the full standard deviation. But rather, it's going to be suppressed by this root n, where n is the number that we're sampling.**

**So if you look at the histogram of the means, you're going to get a Gaussian in here-- OK, that's not a very nice Gaussian, but-- with a width that is the standard**

11

**deviation divided by root n.**

**Now, if we assume that we don't have any systematic error, then this distribution of means that you would have calculated-- it's Gaussian, it's centered on the right value, but about a third of the time, it'll be beyond the plus or minus 1 sigma.**

**And what that means is that about a third of time, if you plot this standard error of the mean, it should fall off of the kind of true curve. And this basically does not depend on n. And can somebody say why it doesn't? Yeah.**

**AUDIENCE: Yeah, I think I was sort of confusing myself, but this makes sense. So yeah, I mean, you know that these error bars will shrink, if you take more measurements. But on the other hand, the actual measurements will be closer--**

**PROFESSOR: That's right.**

**AUDIENCE: --to the true value.**

**PROFESSOR: That's right. So what happens is that as you sample from this distribution a larger number n times, then your error bars shrink, but your measurements get closer to the curve. And those two effects cancel. So you should end up roughly with 2/3 of the errors bars containing this curve, or 1/3 falling off.**

**And I think that this is a little bit surprising, because there's always a sense that we feel that there's something wrong with our measurements or something wrong with our model or whatnot, if any error bar does not contain the line.**

**I mean, I feel like I often see there's this effort that people have to try to make it so that these error bars always overlap with some underlying curve that is supposed to represent reality. But that's not, in principle, supposed to be true.**

**Are there any questions about where we are right now? OK. Now, what I want to do is something slightly different, which is ask-- let's say that this is a curve that is not the underlying reality but is instead a fit to the data. How does this change anything that we've said? Or does it?**

12

**All right, well, OK, let's-- OK, so we're going to say do fit. The question is does this change the thing here? Do you understand? Change, A is Yes, B is No. Yes.**

**AUDIENCE: Do you have the same modeling for the fit as we did for the original--**

- **PROFESSOR: Yeah, well, let's say that this was a curve predicted by some fancy theory but that you have to specify the mass of something and the-- so I don't know, there are two things that are specified. So what you do is you fit.**

   - **And the question is, does it change what fraction of the error bars you expect to contain the true curve? Ready? Is it not clear what I'm asking?**

**AUDIENCE: But the true curve is determined by the god.**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[LAUGHTER] →](03-laughter.md)
