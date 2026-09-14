---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/dp4nqipuh6w-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/dp4nqipuh6w-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**[INAUDIBLE].**

**PROFESSOR: Yeah, yeah. Right. So again, it's surprising. The thing is that even with just two, in principle, we can be very sensitive. Right? I mean, actually, sometimes people actually do just put it on like quadrant photo detector, where you really only get essentially binary information. But even with just two, if I say OK, well, it looks like this, or if it looks a little bit like that, if there's no error in our measurements there, then you can actually get that location very well. Yeah.**

**It's surprising. I'm not going to like. Yeah, but even with this quantization of some sort that's due to the CCD, city you can still get down to nanometer resolution. Your resolution is worse than it would be if you knew actually exactly where each photon was hitting, but it's not very sensitive, actually.**

**And indeed, in the presence of-- and this is a highly technical comment. But in the presence of read noise and other kinds of noise in the CCD, actually, in many cases, it's actually better to have somewhat larger pixels, again, than you would expect.**

**So these balancing many different things. People have thought carefully about this stuff. But in the end, 100 nanometer pixel is actually fine. And just to be clear, it's 100 nanometers at the sample plane. So it's typically of order 10 microns size on the camera itself. So the physical size of each of the pixels on the cameras, 10 microns within a factor of 2, between 5 and 20, but then you get 100x typically magnification at the sample point.**

**So to be clear, 10 microns divided by 100 is 100 nanometers. Is everybody following? OK I don't want to-- all right. The key thing-- three, you can ignore. But the key thing to notice here is this thing that's here, which is nanometer resolution. And it's been known for decades that this is, in principle, possible and so forth. But I think that within the realm of single molecule biophysics, it was really popularized in some very nice papers by Ahmet Yildiz, et al, where they attached single molecules**

11

**onto the heads of various motors as they were walking along tracks, and showing that these motors were walking kind of like this, by catching fluorophores here, and then you could really just see it, see them walking it.**

**Any questions about why it's in principle possible to get nanometer resolution in this process?**

**AUDIENCE: Doesn't this assume that the protein is 100% static?**

**PROFESSOR: Yes.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah. Yeah, indeed. Right now, I'm assuming that this thing is constant. And the question is like, how much movement is a problem? And so then you have to-- you know.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: That's right. So indeed, often, you're trading off spatial resolution for temporal resolution. And also, the intensity of your laser, and so forth. But in these sort of experiments, I think that what they did is they slowed down the motors quite a lot. So it was limiting ATP.**

**So indeed, the motors in those experiments, I think they were taking steps of order every second or 10 seconds. I mean, it was as slow as you can go, and still, yes. And then at each location, I think they were collecting 10 to the 4 or a few 10 to the 4 photons. And incidentally in this case, these are the photons that are being collected. And typically, you would only be collecting 10%, 15% of the photons. Because the photons are actually being emitted everywhere. But you only collect the ones that go back to your objective.**

**All right. I just want to make one comment about the super resolution techniques that have been spreading. So the question here is, well, let's say that you have two proteins next to each other. What can you do?**

12

**Now, the basic idea of all these super resolution techniques is that if we know that we have a signal for only one protein, then we can actually figure out where it is. So what you need to do is figure out a way so you just have one at a time emitting. So there are various schemes to make it so that these proteins can either turn on or off.**

**Now, what you can do is if just one turns on, you got some photons, you say OK, this protein goes over here. Then if later, this other protein becomes fluorescent, now you can figure out where that is. And so you do this basic super resolution localization multiple times, and then you can identify where things are.**

**Yeah. So all the microscopy guys really like to have fun acronyms. So these guys, when they did it, they called it FIONA. So this is-- is it DreamWorks? Or this is where the green ogre like that and then the red head?**

**AUDIENCE: Shrek.**

**PROFESSOR: Shrek? All right. So Shrek. And so Fiona was the redhead. And this stands for fluorescent imaging with 1 nanometer accuracy. And then indeed, a group at UCSF then developed SHREK, which is simultaneous high resolution imaging-- something. OK. I can't remember how it ended. But, yeah.**

**So the super resolution techniques, they call them-- so Xiaowei Zhuang at Harvard called hers STORM, stochastic reconstruction of something or another. So this is the Zhuang method. And then Eric Betzig called his PALM, which stood still for something else.**

**I don't know. But in particular, Betzig-- there's a long history of the hard core microscopists, somehow like, developing their techniques in their garages. I don't know what it is, but there have been a number of these cases. And Betzig I think was one of them.**

**Now he's at Janelia Farm, HHMI, and has been developing all sorts of advanced microscopy techniques. So I think that that [INAUDIBLE] did not develop hers in the garage. But um--**

13

**AUDIENCE: And they're all based on the same principle-PROFESSOR: Yeah. It's all about temporal. It's a question of how you're getting them to turn on and off. AUDIENCE: It sounds like [INAUDIBLE] acronyms. PROFESSOR: Oh do they also have? AUDIENCE: ROSY, COZY, NOSY. PROFESSOR: Yeah. Right, right. For the different sequences or something? Yeah, yeah. All of these acronyms, maybe I just never came up with a good one, so then I-AUDIENCE: [INAUDIBLE]. PROFESSOR: Yes. Indeed. I always like when somebody uses acronyms that I don't know, I always like to say, oh, all these TLAs are tricky, or whatever. And then I say, it's three letter acronym. AUDIENCE: [LAUGHING] PROFESSOR: I very much like self-referential humor. OK. So that's the idea of the super resolution techniques. Any questions about that before we kind of get back actually to the paper? OK. Now in this whole discussion, as was pointed out, we've been assuming that the protein is not moving around during our imaging time. So one of the major challenges of doing this whole business in live cells is not only is there a lot of autofluorescence, but in addition, you can't necessarily wait 10 seconds to localize where this thing is, because it will have moved somewhere else right. And in particular, diffusion is a problem.**

**Can somebody remind us what the authors did in order to get around the diffusion problems? I'm sorry what was it? AUDIENCE: [INAUDIBLE].**

14

**PROFESSOR: They attached it to the membrane. And why does that help?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah. That's perfect. Proteins diffuse slower. And I think depending on the organism, there's more or less diffusion and so forth right. But what they did is they anchored to the membrane to reduce diffusion. I'll just say it reduces diffusion.**

**And indeed, just from a back of the envelope calculation, you can convince yourself that you probably are going to need to do this. So in particular, let's ask-- in this paper, actually, they image the fluorophore for 0.1 seconds, right? Does that sound right? So the image collected, so delta t is equal to 0.1 sets.**

**So the question is, how far will a protein typically diffuse in 0.1 seconds? Well, this is why we have diffusion calculations. Right. First of all, the diffusion coefficient, we're going to talk more about diffusion in a few weeks. But you should also in principal be able to calculate how these things go.**

**So in general, this is going to be a kT over some gamma, which tells us how hard-so kT is thermal energy. OK. So, thermal. And at room temperature kT is around 4.1 piconewton nanometers in some unit. There are many different ways you can write that.**

**Whereas gamma tells us just how hard it is to push something. In particular, if you push them with some force, it will move with some velocity. Now is this consistent with freshman mechanics? No. It's not. OK. Is that a problem? So why is it that I'm writing this?**

**AUDIENCE: Solvents exerting a force [INAUDIBLE]?**

**PROFESSOR: Right. So solvents exerting a force. That's true. But in the case of freshman mechanics, when we're pushing blocks, it's also true that the other things are exerting forces. The tables. But we still write down F is equal to MA. So it's not just that other things are exerting forces. Yeah?**

15

**AUDIENCE: They're always in a continuum? PROFESSOR: Always in a continuum. AUDIENCE: They're always surrounded by [INAUDIBLE]. PROFESSOR: OK. Yeah. It's always surrounded-- but I'm actually surrounded by fluid now too. You know, you can wave your arms and feel it. AUDIENCE: [INAUDIBLE]. PROFESSOR: OK, right. So it comes down to the viscosity. Indeed, this whole thing about being a low Reynolds number, we're going to talk about this in much more detail in a few weeks, when we think about how bacteria swim, and so forth. But I just want to mention that this is because we're at this low Reynolds number, where the so-called inertial forces, like momentum are negligible.**

**Inertia forces are negligible. So then it's really, this is in some ways more like Aristotelian physics, but it ends up being true for small objects in viscous liquids. And indeed, this thing it scales as the radius. So in principle, we can actually calculate roughly how the diffusion coefficient is going to behave as a function of size. The object and so forth.**

**But I'll just tell you that for a protein size object in the cell, you might get something like 10 micron squared per second. Now, already just from units, you can see how the kind of typical diffusion distance has to scale with time. And in particular, you're going to get that the typical kind of distance that you go in a typical distance-- we'll say square root, because it's the square root of 2 times D times time.**

**So you can see if you multiply the time by the D, then you end up with a micron squared, so you have to take a square root to get something that's a characteristic distance. And indeed, this is the kind of math that I can do. So this is an order one micron.**

**And how big is an E. coli cell?**

16

**AUDIENCE: One micron? PROFESSOR: One micron, roughly, right? So it might be a couple microns long. A bit less than a micron in width. And what this is saying is that 0.1 seconds, which is our exposure time on our camera, you would expect something like GFP to diffuse around roughly the cell volume. And maybe not the entire one, but a fair fraction of it. What this is saying is that the diffusion really would be a problem, even with this relatively short exposure time. Yeah?**

**AUDIENCE: [INAUDIBLE]? PROFESSOR: Yes. So this is assuming that the cytoplasm has a viscosity that's maybe an order of magnitude larger than water. And that's just because the inside is chock full of proteins and so forth. Now, there's a lot of discussion of what the mechanism is of diffusion and transport inside cells. It may depend on the size. It's a very complicated area. But for our purposes, this is a reasonable way to think about it. But indeed, the viscosity of the cytoplasm, you'd expect to be significantly more than the viscosity of water. Yeah?**

**AUDIENCE: [INAUDIBLE] lower the [INAUDIBLE] time? PROFESSOR: Lower the? AUDIENCE: Yeah. Like two orders of magnitude instead of one? PROFESSOR: Right. So in principle, we could. There are technical issues on various sides. So of course, you have to say, oh well, a typical camera, just the shutter of opening, shutting, that actually has some limit. But you can get around that using kind of strob-- you know, there are fancy things you can do. But there's just a more fundamental thing here, which is-- so this is already 100 milliseconds. If you go down to like say, 1 millisecond, then it's true that the protein won't be able to diffuse very far, but then you also just don't collect any photons. The number of photons you collect scales linearly with the time, right? So at some**

17

**point, it's just that you really don't get very many photons. And then again, you have this extra problem of distinguishing the fluorescence from the autofluorescence.**

**And I just want to maybe mention one more thing. In Figure 1, you can actually see how big the fluorescence intensity of this Venus protein is, as compared to the autofluorescence. And you see that if you decrease that exposure time by even one order of magnitude, you wouldn't be able to see them over the background. Right? And that's true, even though they won't have had a chance to diffuse. It's just that you don't have enough signal.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Oh. Right. So you can also increase the intensity. Yeah, that's right. And there is some limit to how much you can increase the intensity of the laser, just because there is some cycling time of the protein in terms of, you excite it, and then it takes some time before it's going to emit. So that actually sets a fundamental limit.**

**Yeah, I don't know enough about the details of this in the sense of whether maybe it would've been possible for them to try to adjust these various parameters to do it in some other way. But these are all the things you have to consider. Question?**

**OK. So what we have now is some sense-- OK, we need to maybe anchor into the membrane to reduce the diffusion. All right. So they did that. And we'll maybe say something more about this anchoring process in a moment. But first, I want to make sure that we're all on the same page in understanding their arguments for why this is a single molecule that they're looking at. Can somebody remind us their primary evidence that this is a single molecule?**

**So question is, a molecule , we'll say single fluorophore, just to-- question mark. How do we know?**

**AUDIENCE: The intensity drops off.**

**PROFESSOR: Right. The intensity drops off suddenly. So if you look at the intensity as a function of time, what you see is that it looks like, and then. So it's actually more noise, but**

18

**this is just to-- now this is what it looks like for a single molecule, but we should also be clear of what it would look like if it were many molecules.**

**So this is if it's a single molecule. And this is what we call a bleach event. And so the molecule dies for one reason or another. So it goes, some oxygen reaction, something. Now the question is, what happens if it said there are many molecules?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: OK. Now, what we want to do is imaginn-- let's say that we shined light on a bead containing fluorescence, containing fluorescent molecules. So I'm going to give us some options. It could be many molecules. OK. We could. All right. I'll give you a choice those three.**

**AUDIENCE: So we're talking about [INAUDIBLE]?**

**PROFESSOR: Yes. I'm asking if instead-- what happens in the microscope is you see a spot. And the spot is always huge. Right? 300 nanometers. So there could be one molecule there, or there could be 100. You could fit 1,000 in there. No problem. Right? 10 by 10 by 10 molecules? That still is only 30 nanometers. That's still much smaller than defraction limited spot.**

**So of course, if you see something, and the spot is 10 microns in width, you'd be pretty confident that either your optics suck, or you're looking at many molecules. But if you see diffraction limited spot, then it's not so obvious. And so the question is, if you plot the intensity of a diffraction limited spot as a function of time, how do you know that it's a single molecule?**

**They claim, oh well, it's because of this. But it's always good to be clear. What would it look like if it were not a single molecule, but instead it were a collection of molecules> Let's go ahead and vote. Ready? Three, two, one.**

**So we have a fair number of different responses. It seems to be a split across the room is the only problem. So I'm not going to have you discuss, because I think your neighbors typically agree with you. But in this case, it's going to be C. And this,**

19

**it was an attempt of mine of drawing-- what is it? Exponential distribution. So you'll see exponential decay.**

**So this is typical of processes where something is happening at a constant rate over time, and then you're seeing this thing go away. So this could be, for example, radioactivity is the classic thing we always talk. These are random events. We thought the radiation coming off of some source is a function of time that's going to decay exponentially.**

**Similarly here, now this is-- again, intensity is a function of time. In the case of many molecules, we get this thing that look like C. Now, there's going to be some time scale here which is telling us about the typical time for this bleach event, which we're told is what?**

**250 milliseconds. And indeed, this is telling us, actually, that they're already illuminating these guys at pretty high intensity. Because 250 milliseconds is not that long. Yes?**

**AUDIENCE: [INAUDIBLE]?**

**PROFESSOR: Yes. AUDIENCE: Is it really a function common photons [INAUDIBLE]? PROFESSOR: It's not really a function of the-- it ends up being a function of the number of photons that are emitted, but that's basically because you're in kind of some ground state. You excite up to this other state. And then, you get this relaxation to a lower state.**

**So this is the energy of the absorbed photon. This is the energy of the emitted photon. The idea is that each time you go around this cycle, that's one emission cycle, there's some probability that's small-- 1 in 10 to the 5, or something like that-that it reacts with oxygen, or something that causes it to go to the start. And it's in principle, irreversible state.**

**Of course, the dynamics of these things can be more complicated, but that's the [INAUDIBLE] way of thinking about it. What that means is that that's more or less a**

20

**constant number of photons that you're going to get out. There are many cases where this approximation fails.**

**This single step bleaching is kind of a classic signature of the fact that you're looking at a single fluorescent molecule. Now, there are secondary arguments for why this is a single [INAUDIBLE] Venus they're looking at was what?**

**What was their supporting evidence? Yes?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah. The intensity matched what?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: That's right. So what they said is, well, all right. This intensity matched what they measured on a slide. Just the molecule. But I'd say this really is, I would say, supporting evidence, because the intensity of the fluorescence can just be different in different environments.**

**I think that this is kind of thing that it's-- there are many ways that this can fail. Right, so I think that in general, we consider this to be the gold standard. All right. Now in their experimental setup, there's something that's, I think, very nice that they do, which is, if you look at the-- now this is the we'll say, laser illumination. Here, this is kind of on, and this is off.**

**What they do is every three minutes, they illuminate. And then, this is not to scale. This was 1.2 seconds. So we might want to even-- there's a separation in there. So they illuminate for 1.2 seconds, and they collect the light for the first 0.1 seconds. This is the period where they collect for 0.1.**

**Can somebody tell us why they might possibly want to do this? Shine more light on the sample than they need to? They're not going to analyze that data. So this is an intentional bleaching step. So this part here is to bleach. And we'll see that this is actually essential for the way that they're collecting their data.**

21

**Given everything that we've just said, you should be able to tell me what fraction of the molecules will not be bleached. That survive bleaching. Survive the so-called bleaching step. You can ignore my writing. You should be able to think about it on your own.**

**I'll go ahead, and I'll give you 30 seconds to think about this. And I think all of the information that you need is in principle written up on the board. Yes?**

---

[← PROFESSOR](02-professor.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
