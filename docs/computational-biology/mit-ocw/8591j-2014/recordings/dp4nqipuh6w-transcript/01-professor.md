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

**Today, as I mentioned to you in last lecture, we're going to really be focusing in quite some depth into this paper by Sunney Xie. So I would say that it is one of my all time favorite papers. And in particular from the standpoint of discussing a paper in class, I think it is absolutely wonderful.**

**It is, I think, clearly written. It explains why that did all these things. And they checked all sorts of possible sources of perhaps being lead astray. And I think it was a huge amount of work, and it was a technical tour de force when it came out.**

**So before this, I would say single molecule biophysics, by which I mean both single molecule fluorescence, i.e., detection, as well as single molecule manipulation, were almost exclusively in vitro techniques. So we took purified components, and then we studied the fluorescence, or the mechanical properties and so forth, of these molecules in the equivalent of a test tube.**

**But really, in glass slides, where we just had to purified components, so no know living cells. And I think we got a lot of insight into the dynamics of molecular motors, transcription, translation, and so forth. And I think that many of us in the field thought that this paper was essentially not possible.**

**I did my Ph.D in the single molecule area, from of 2002 to 2005, I graduated. And indeed, I did a little bit of work in this area of single molecule fluorescence, and I was basically unsuccessful. Even just doing this kind of an in vitro setting. My lab is [INAUDIBLE], we did primarily single molecule manipulation. We were playing with the single molecule fluorescence . And eventually, people in the lab got it to work. But I would say that my foray into it was maybe unsuccessful.**

**So I had a very healthy respect for the challenges that are involved in doing single**

1

**molecule fluorescence. And the thought of doing this in live cells was very scary. And I'd say that many of us thought it was not going to work. And indeed, this project was one-- and the general goal of studying a single molecule dynamics in living cells, is something that's Sunney's group had been working on, I think, for many years.**

**And it indeed was very hard. But then there were these two papers they came out, both from Sunnye's lab actually. And they came out both, i think, in January of 2006, one in science, one in Nature, demonstrating not one way of doing this, but rather two ways of getting single molecule dynamics inside living cells.**

**So today, obviously, we're going to be primarily talking about this paper by [INAUDIBLE]. But if you're interested in these things, I encourage you to check out [INAUDIBLE] paper, which also published, [INAUDIBLE], at the same time. And that was based on a microfluidic assay, where instead of doing the single molecule fluorescence within cells, instead by trapping the cells in small volumes, and then using more traditional enzymatic assays, such as this beta [INAUDIBLE] assay, enclosed in a small volume, it's almost possible to study, once again, these sort of busting dynamics in E. coli. And also they did it in yeast, and demonstrated that it's kind of a generally practical assay.**

**So if you're interested in those papers, I encourage you to check it out. But for me, this was really an eye-opening thing. So I graduated with my Ph.D. in December of 2005, and then I went to a conference in Cambridge, England, where where Sunney presented this work. And I think that it really blew many of our minds, this idea that you could start to get this sort of data within live cells.**

**And indeed, Sunney's group over the next five years did a whole series of what I'd consider to be beautiful studies, probing, for example, the dynamics of this [INAUDIBLE] repressor binding, unbindings onto this promoter, the search process. Yeah. A whole slew of, I think, really beautiful things. So we're not going to have the chance to go over all those papers in this class, but I encourage you to look at them.**

2

**Can somebody say what the primary challenge is with doing single molecule fluorescence in these live cells? So why is it that I did not think that this was going to work? And now, you're going to have to give an argument that ends up not being true. But why is it that this is such a hard thing to do. Yeah?**

**AUDIENCE: [INAUDIBLE] laser at the cell but you can't kill the cell?**

**PROFESSOR: Right. OK. So one is that there's laser, the cell, and then there's a big question mark. Is this going to be OK? And indeed, we certainly know that at one limit, it's not going to be OK.**

**If you take the lasers at Los Alamos National Lab, you can vaporize the cell. So it's certainly enough power, and the cell's going to be dead for sure. And so the question is maybe, oh, can you dial down the laser power enough to get-- and indeed, this is something that they talk about, their strategy in this paper.**

**Other challenges, problems?**

**AUDIENCE: Many molecules.**

**PROFESSOR: Right. so the principle of many molecules. So we have to figure out some way of separating them, either temporarily or spatially. Indeed in this paper, they actually do both. We say many molecules. And of course, we have to decide what we mean by this. Because ultimately, we're interested in doing single molecule measurements.**

**But then, of course, of the plural of single is many. How many is too many for us to study, and so forth? The question here is maybe like, how to separate, right? What are other challenges in this?**

**AUDIENCE: Diffusion.**

**PROFESSOR: Right. There's diffusion. So we're going to talk more about this, for sure. Well, actually, all of these things, we're going to talk about. Diffusion. And why is this a problem, though? Right. So it's diffusion is maybe fast. And so this is going to end**

3

**up being relevant for kind of signal to noise reasons. So what's the signal and what's the noise? AUDIENCE: Autofluorescence. PROFESSOR: Right. So there's autofluorescence. So in particular, this noise is autofluorescence from what? AUDIENCE: From the cell. PROFESSOR: From the cell. Right. And what's the signal, just to be clear here? AUDIENCE: Photons from [INAUDIBLE]. PROFESSOR: Right. So it's photons from, in this case, the GFP-like molecule. Yeah? So we want to do single molecule measurements. We want to be able to measure or detect the fluorescence coming from this single fluorescent protein. Now the question is, if it's a single molecule, does that mean that it's going to send out just a single photon? No. Maybe they come out as single photons. But we can detect them. Now the challenge in, in some ways surprising, is not that the number of photons is so small. Does anybody have any rough sense of maybe how many photons are we collecting from each of these? AUDIENCE: Many thousands. PROFESSOR: Yes. I'd say many thousands. In particular-- so we'll say many thousands. It could be even 10 to the 4 per second or so. It depends on the laser intensity. Many thousands of photons collected. Yes? AUDIENCE: That's before [INAUDIBLE]. PROFESSOR: Yes. That's right. And indeed, the stronger the intensity of the laser light that you illuminate with, the faster you're going to collect the photons, but in general, it won't increase the total number of photons that you collect. So in these sorts of situations, you might get, say-- we'll say 10 to the 4, plus or minus in order of magnitude,**

4

**photons per second.**

**And they might last for, depending on how-- for 30 seconds or so. And of course, we'll look at the actual numbers in this paper. But in many of these situations-- times 10 to 100 seconds.**

**In this case, it actually bleached faster. Right. But we'll see. Well, you might be able to get also-- if you use organic dyes and other-- right. But this gives you some sense of that there's a fair number of photons that you could, in principle, collect from a single molecule.**

**Now, of course, you might be worried, well, these are the photons that you shine on your camera. But then your camera won't pick up all of them. The way that we think about this is by what's known as the quantum efficiency. Quantum efficiency tells us basically this is the fraction of photons detected.**

**But with modern cameras, actually, this thing is approximately one. So it's 0.9 maybe with modern cameras, which is for our purposes, basically one. Which means that you can detect, actually, the majority of the photons that are hitting your camera.**

**From that standpoint, the number of photons is not actually the problem. You can collect many thousands of photons. So the problem is really detecting that signal over the background signal. Over the autofluorescence of the cell.**

**And indeed, if you look at the figure, figure one, you can very clearly see the autofluorescence of the cell. So the fluorescence where there's the cell is indeed much larger than where there's no cell. The autofluorescence is, I'd say, the primary challenge here.**

**Of course, there are many, many others. Right. So this is potentially a big problem. And in order to get around that, there are all these other strategies that the author's going to implement. Yes?**

**AUDIENCE: What is the [INAUDIBLE]?**

5

**PROFESSOR: Yeah. So many things are weakly fluorescent, I think is the short answer. And this also depends upon, for example, cells are more autofluorescent if you grow them in a rich media than in minimal media, for some mysterious reason. Yeah. But it's really just that there are many things that are weakly fluorescent. And it's just there are a lot of molecules in a cell.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah, right. In the case that you put in a fluorescent protein or a fluorescent dye, then it has rather well-defined absorption and emission spectra. And each individual absorber emitter indeed has a well-defined absorption emission profile. But then in the cell, there are just many, many, many of them, which means that there's rather what you want to call an absorption of broadband emission. So indeed, in some wavelengths, it's worse than in others. But it's not that you get well-defined peaks the way you do for a single kind of [INAUDIBLE].**

**AUDIENCE: I guess I was just wondering [INAUDIBLE].**

**PROFESSOR: Yes. And indeed, in this case, they're exciting with a laser. So at least on the excitation, it's as precise as you can hope for. And indeed, on the emission they will use a filter. So they're not going to be absorbed. It's probably a few tens of nanometers that they're looking at. So in that sense, they are filtering out, but still, there is autofluorescence.**

**All right. Now getting at this question of the single molecule fluorescence, the limitations, diffusion, and so forth, it's always valuable to have a sense of scale in anything that you're ever doing. So just let's wake up by reminding ourselves, how big is a protein? Right. So, typical protein. Typical protein. And for now, we'll say e.g. For example, GFP or whatever.**

**All right. We're not going to give you very much time to think about this. But I just want to make sure that we all keep track of senses of scale in the world. Ready. Three, two, one. All right. So we've got some B's, C's, D's. All right.**

6

**Wow. We got a lot of surprisingly wide wide range, actually. [LAUGHING] OK. Well, we also have the mirror image problem over here. OK, right. So, indeed, I'll say this is a typical protein size. So, it's a few nanometers. Depending on, there are some that get longer, especially if you're thinking about a long-- there are some structural- well, you know. Of course, if you're talking about filaments, they can be-- but if you're talking about a typical globular protein, it's a few nanometers in diameter.**

**The question is, let's say that this is a fluorescent protein, or GFP. And now what we do is we look at it. And we're going to get some fluorescent spot. So this is plotting the intensity as a function of position. Right?**

**So this is the intensity I is a function of position X. Now the question is, what is going to be the size of the spot? We conveniently have some size scales up on the board. I'll let us think about this for eight seconds. All right. Ready. Three, two, one.**

**OK. We have a majority of the group that is saying that indeed, it's going to be D. So this is what's known as a diffraction limited spot. And this is a fundamental physics limitation, that if you are imaging something with light that is of some wavelength, lambda, this is of order lambda over 2-- it depends on numerical aperture or projective and so forth. But you know.**

**So order of lambda. A little bit less maybe. And indeed, the wavelength of the light that's being used here is-- they're exciting with 500 something. And then let me just- 514. OK. So indeed, what happens is that we shine in light. So this is the lambda incident that is 514.**

**Now, there's going to be some GFP that looks like this. And then, we're going to get out lambda emission. All right. Question, is the emitted light going to be equal? Is the wavelength going to be 514 nanometers? Yes or no? Ready? Three, two, one.**

**AUDIENCE: No.**

**PROFESSOR: No. Lambda emission. Is it going to be greater than or less than lambda incident? Ready? Three, two, one.**

7

**AUDIENCE: Greater than.**

---

[Up: contents](index.md) · [PROFESSOR →](02-professor.md)
