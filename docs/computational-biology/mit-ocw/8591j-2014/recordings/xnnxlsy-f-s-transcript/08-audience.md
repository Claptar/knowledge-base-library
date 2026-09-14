---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/xnnxlsy-f-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/xnnxlsy-f-s-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Big alpha?**

**PROFESSOR: Big alpha. Yes, perfect. And it turns out, big alpha is a little bit-- OK, and remember we have to remember what p0 was. p0 was this p0 times 1 plus p0. All right, so this is the requirement.**

**And actually, if you play with these equations just a little bit, what you'll find is that, if alpha is much larger than 1, then this requirement is that n is less than 2 or less than around 2. This is saying, on the flip side, the fixed point is stable if you don't have very strong cooperativity and repression. And the flip side is, if you have strong cooperativity of repression, then you can get oscillations because this interior fixed point becomes unstable.**

26

**So this is also saying that n greater than around 2 leads to oscillations. And this maybe makes sense because, when you have strong productivity in the repression there, what that's telling you is that it's a switch like response. And in that regime, it maybe becomes more like a simple Boolean kind of network where, if you just write down the ones and zeroes, you can convince yourself that this thing maybe, in principle, could oscillate.**

**Now if you look at the Elowitz repressilator paper, you'll see that he gives some expression for what this thing should be like. And it looks vaguely similar. Of course, there he's including the mRNAs, as well. But if you think that this was painful to do in class, then including the mRNAs is more painful. Are there any questions about this idea? Yeah.**

**AUDIENCE: So in the paper, did they also only do the stability analysis to determine the--**

**PROFESSOR: I think they did simulations, as well. So the nature of simulations is that you can convince yourself that their exist places that do oscillate or don't oscillate. Although, you'll notice that they have a very, kind of, enigmatic sentence in here, which is that it is possible that, in addition to simple oscillations, this and more realistic models may exhibit other complex types of dynamic behavior.**

**And this is just a way of saying, well, you know, I don't know. Maybe someday because once you talk about six dimensional system, you never know if you've explored all of the parameter space. I mean, even for fixed parameters, you don't know if you started at all the right locations.**

**You can kind develop some sense that, oh, this thing seems to oscillate or seems to not oscillate. And it does correspond to these conditions. But you don't know. I mean, it could be that, in some regions, you get chaos or other things. Right?**

**So it's funny because I've read this paper many times. But it was only last night when I was re-reading it that I kind of thought about that sense like, yeah, I'm not sure either what this model could possibly do. Yes?**

27

|**AUDIENCE:**|**In this linear analysis the three x's are the same.**|
|---|---|
|**PROFESSOR:**|**That's right.**|
|**AUDIENCE:**|**Because they're non-dimensional?**|
|**PROFESSOR:**|**All right. So the reason that the three X's are the same is because we've assumed**<br>**that this really is the symmetric version of the repressilator because we're assuming**<br>**that all of the alphas, all the ends, all the K's, everything's the same across all three**<br>**of them. So given that symmetry, then you're always going to end up with a**<br>**symmetric version of this.**|
||**So I think if it were asymmetric and then you made the non-dimensional versions of**<br>**things, I think you still won't end up getting the same X's just because, if it's**<br>**asymmetric, then and something has to be asymmetric. Yes?**|
|**AUDIENCE:**|**[INAUDIBLE] so large alpha leads to--**|
|**PROFESSOR:**|**Yes, OK. We can go ahead and do this. So for large alpha, this fixed point is going**<br>**to be-- p0 is going to be much larger than 1. So this is about p0 to the n plus 1. We**<br>**can neglect the 1 for large alpha.**<br>**And then and then what we can say is that, over here, for example, if we multiply**<br>**both sides by-- p0 squared, p0 squared, so multiply it by one. Then this down here**<br>**is definitely alpha squared. And then, up here, what we have is p0 to the n plus 1,**<br>**which we decided was around alpha for a strong alpha.**<br>**So that gives us alpha times alpha divided by alpha squared. So this actually all**<br>**goes away for large alpha. So then, you're just left with n less than 2. Did that--**|
|**AUDIENCE:**|**Sorry. Where did that top right equation come from?**|
|**PROFESSOR:**|**OK, so this equation here is this is the solution for where that fixed point is. So in**<br>**this space of the p0's, if you set the equations for p1, p2, p3, if you set that equal to**<br>**0, this is the expression always for a large alpha, small. So this is a need be location**<br>**of that fixed point.**|


28

**And it's just, as alpha is large, then we get that p0 to the n plus 1 is approximately equal to alpha. And this is for alpha much greater than 1. And in that case, all of these things just go away. And you're just left with n less than 2.**

**So for example, as alpha goes down in magnitude, then you end up getting a requirement that oscillations require a larger n. We'll give you practice on this. All right, so I think I wrote another-- if I can find my-- you can ask for alpha equal to 2. What n required for oscillations.**

**I'll let you start playing with that. And I will make sure that I've given you the right alpha to use. So in this case, what we're asking is, instead of having really strong maximal expression, if instead expression is just not quite as strong, then what we'll find is that you actually need to have a more cooperative repression in order to get oscillations.**

**And that's just because, if alpha is equal to 2, then we can, kind of, figure out what p0 is equal to. 1. Right. Great. So the fixed point is at one. That's great because this we can then figure out. Right?**

**So this is 1 plus 1 square. That's a four. 1. 2. So this tells us that, in this case, we need to have very cooperative repression. We have to have an n greater than around 4 in order to get oscillations in this protein only model. Yes?**

**AUDIENCE: It is kind of strange that even for a really big alpha you still need n greater than sum.**

**PROFESSOR: Yeah, right, right. So this is an interesting question that you might think that for a very large expression that you wouldn't need to have cooperative repression at all. Right? And I can't say that I have any wonderful intuition about this because it, somehow, has to do with just the slopes of those curves around that fixed point. And it's in three dimensions.**

**But I think that this highlights that it's a priori if you go and say, oh, I want to construct this repressilator, it's maybe not even obvious that you want it to be more or less. I mean, you might not even think about this idea of cooperative repression.**

29

**You might be tempted to think that any chain of three proteins repressing each other just, kind of, has to oscillate.**

**I mean, there's a little bit of a sense. And that's the logic that you get at if you just do 0's and 1's. If you say, oh, here's x. Here's y. Here's z. And they're repressing each other. Right? And you say, oh, OK, well if I start out at, say, 0 1 0 and you say, OK, that's all fine. But OK, so this is repressing.**

**And it's OK, but this guy wasn't repressing this one. So now we get a 1, 1, 0, maybe. Then you say, oh, OK. Well now this guy starts repressing this one. So now it gives us a 1 0 0. And what you see is that, over these two steps, the on protein has shifted. And indeed, that's going to continue going all the way around.**

**So from this Boolean logic kind of perspective, you might think that any three proteins mutually repressing each other just has to oscillate. And it's only by looking at things a little bit more carefully that you say, oh, well, we have to actually worry about this that you really have to think about you want to choose some transcription factors that are multimerizing and cooperatively repressing the next protein just to have some reasonable shot at having this thing actually oscillate.**

**AUDIENCE: So in this, we might still be able-- I mean, oscillations like this might still [INAUDIBLE] but just not like, maybe, oscillations around some stable fix point or something. Like, they're just not limit cycle oscillations. Do you think that in a [INAUDIBLE] there would probably still be some kind of oscillations somewhere. Just not this beautiful limit cycle kind.**

**PROFESSOR: Yeah, my understanding is that in, for example, this protein only model of the repressilator that if you do not have cooperative repression, then it really just goes to that stable fixed point. Of course, you have to worry about maybe these noiseinduced oscillation ideas. But at least within the realm of the deterministic, differential equations, then the system just goes to that internal fixed point that's specified by this. Question?**

**AUDIENCE: Can we think like that the cooperation, sort of, introduced delay?**

30

**PROFESSOR:**

**That's an interesting question. Whether cooperativity, maybe, is introducing a delay. And that's because, after the proteins are made, maybe it takes some extra time to dimer and so forth.**

**So that statement may be true. But it's not relevant. OK? And I think this is very important. This model has certainly not taken that into account. So the mechanism that's here is not what you're saying.**

**But it may be true that, for any experimental system, such delay from dimerization is relevant and helps you get oscillations. Right? But at least within the realm of this model, we have very much not included any sort of delay associated with dimerization or anything. So that is very much not the explanation for why dimerization leads to oscillations here.**

**And I think this is a wider point that it's very important always to keep track of which effects you've included in any given analysis and which ones are not. And it's very, very common. There are many things that are true. But they may not actually be relevant for the discussion at hand.**

**And I think, in those situations, it's easy to get mixed up because it still is true, even if it's not what's driving the effect that is being, in this case, analyzed. We're out of time. So we should quit. On Tuesday, we'll start by wrapping up the oscillation discussion by talking about other oscillator designs that allow for robustness and tunability. OK?**

31

---

[← PROFESSOR](07-professor.md) · [Up: contents](index.md)
