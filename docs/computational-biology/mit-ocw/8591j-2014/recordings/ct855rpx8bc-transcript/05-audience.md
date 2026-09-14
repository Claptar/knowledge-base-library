---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/ct855rpx8bc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/ct855rpx8bc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**JEFF GORE:**

**But I guess-- sorry, just one last thing. My question is not why it's 10 minutes. It's not an evolutionary question, like why is it useful, right? It's just somehow, [INAUDIBLE]**

**Yeah I think that there are different ways of looking at this and then depending on how you look at it, you either feel surprised or not. So it's a little-- now on the other hand, if you had added a repellent, then the tumbling frequency would actually go up and then come back down. But the key, key thing in this system that we want to focus our attention on is the fact that it comes back to where it started. So it's the fact that I can draw this dashed line that is this perfect adaptation.**

**And so what we want to do is understand where this phenomenon of perfect adaptation comes from and maybe why it is robust to changes in, for example, the concentrations of some of these proteins. Now, let's just make sure that we're all on the same page in terms of what was known about this chemotaxis network. And I think it's worth mentioning, perhaps, here that the whole series of studies of bacterial chemotaxis going back to Howard Berg and company and then later, the studies that in robustness that Uri Alon and Stan Leibler and Naama Barkai did. I think they represent really just a wonderfully beautiful exploration at the interface between physics and biology.**

**I think you could teach an entire course just on bacterial chemotaxis and you could hit pretty much all the major themes in biophysics over the last 40 years. It's really amazing to me. I myself have not done any work in the field, but from afar, I've really just admired the beauty of all these studies.**

**And because you go back to Howard Berg and Purcell and they're thinking about how simple physics can inform the challenges that bacteria are facing and how cells are actually able to do a biased random walk and get anywhere, limits on sensing**

15

**both concentrations and gradients-- and then later, the studies that they're this topic of robustness, it's really a wonderful example where Naama Barkai, when she was a postdoc at Stan Leibler, they had published a Nature paper in maybe '97 basically saying, this idea of robustness is really important in biology and in order to have a robust response of perfect adaptation, a model has to have these features.**

**So there's no experiments there, but their model was guided by previous observations that people had made. And then, two years later, Uri, when he was a postdoc in Stan's lab again, did kind of the experimental confirmation of the model, where he went in and he controlled the concentration of chi R and showed that thee key predictions of the model, i.e. the perfect adaptation, would be robust to the concentration but that the tumbling frequency and the adaptation time, they would not be robust to chi R concentrations. They would move in a way predicted by the model and all that.**

**It's really amazing that it all kind of holds together, because in many cases, we do the modeling kind of post facto, right? And then, it's kind of explaining our results. But the case where a model is really useful is when it makes new predictions that get you to go make new measurements. And this is a situation where there are an infinite number of experiments that you could do, but only some of them will actually provide you a deep insight into the mechanisms that are going on in the system. And I think this was a real case where the models made some really clear predictions and that allowed, in this case, Uri to go and make the strains that allowed him to test the predictions of the model. And I think it's really amazing that it all kind of works.**

**All right. Now, all of the letters that you see up there, they're not actually-- well, first of all, the letters are somehow real. This is the real names of the protein components in the chemotaxis network in E. coli and largely in other organisms. But in each case, there's a chi that comes in front, right? So R corresponds to chi R, for example. And then, there's chi B, chi W, chi A. And these were all identified by genetics, so then by researchers looking for mutants that were defective in chemotaxis. I don't know what happened to C, D, E, F, G, because it does seem like**

16

**we got the first part of the alphabet and the last part of the alphabet. I don't know.**

**All right. Now, the basic idea in the system is that you have chi W/A that we often here will refer to as X just for simplicity. Now, these are proteins in the membrane, so they have a binding kind of pocket outside that will allow binding of attractants or repellents. There might be say, five different kinds of these receptor complexes that can sense, that bind at different rates, different kinds of attractants, repellents, and then the signal is somehow integrated.**

**Now, this could be either an attractant or a repellant. The distinction between these two is that we get different levels of methylation onto chi W. Now in this lecture, we're only going to be talking about the methylated state versus the unmethylated. But in reality, depending on the receptor complex they have, they might have four or five different methylation sites. And this ability to switch between different methylation states is really at the heart of the phenomenon of robust perfect adaptation.**

**The base feature in it, though, is that chi A can phosphorylate chi Y and chi Y will then go and yield the output, which is in this case, increased tumbling frequency. But there are lots of other bells and whistles that you can see on here, right? So of course, it's not just that this phosphorylated chi Y just kind of comes off on its own, but rather it's actually done by chi Z. So there's a constant cycling here and again, there's a constant cycling here where the methyl groups are taken off and then put back on.**

**So if you look at this, you really do feel that it's rather wasteful, because there's a huge number of these futile cycles going on. Chi Y is always kind of being phosphorylated and then dephosphorylated and this is all going to be costly to the cell. So you can imagine then the only reason it's there is because it's doing something useful. Now, there was a comment in the chapter about what is the rate limiting step in all this. And can somebody remember what it was? Yeah?**

**AUDIENCE: Is it methylation?**

17

|**JEFF GORE:**|**So methylation, there is a sense that that is actually the longest time scale, but I**<br>**guess because the methylation is what results in this thing coming in the perfect**<br>**adaptation over this 10 minutes. I guess what I meant-- so yeah, that is the longest**<br>**time scale. But I guess what I was thinking about in rate limiting is the sense of**<br>**when the cell finds itself in a new environment, it changes its state over a much**<br>**shorter time scale.**<br>**So this thing I drew is almost vertical, right? So this question is, if the cell finds itself**<br>**in a new environment suddenly and then it just really wants to tumble-- so you find**<br>**yourself in a crappy bar, how long does it take for you to get out? Now, what's going**<br>**to be rate limiting there? Yeah?**|
|---|---|
|**AUDIENCE:**|**Phospho-- phosphorylation.**|
|**JEFF GORE:**|**Phosphorylation, yeah, although it turns out that's not the rate limiting step. And this**<br>**actually comes back a little bit to something that we talked about in the first part of**<br>**the class that in these transcription networks, the characteristic timescale is what?**|
|**AUDIENCE:**|**G.**|
|**JEFF GORE:**|**Right. So the characteristic timescale in the case of transcription networks is the**<br>**time it takes for you to change concentrations of proteins, which is kind of cell**<br>**generation time or if you have active degradation, you might be able to make it**<br>**faster, whereas all of this is happening rather quickly, say, maybe 1/10 tenth of a**<br>**second. And a lot of these kinds of processes, binding, unbinding, and actually even**<br>**the interactions between the proteins can take place even maybe faster than that.**<br>**So the actual rate limiting step for when the cell finds itself in a bad environment for**<br>**it to start tumbling is actually due to diffusion. And that's diffusion of what?**|
|**AUDIENCE:**|**Y protein.**|
|**JEFF GORE:**|**Yeah, diffusion of the phosphorylated Y, right? And that's because we have the cells**<br>**here. They find themselves in the bad environment. They rapidly bind the repellent**<br>**or they quickly phosphorylate chi Y. But then, Y is going to be formed at one of the**<br>**poles, because actually, there's actually clustering of these receptors at the poles of**|


18

**a cell and incidentally, we're not going to talk about that here, but I think there's strong experimental and theoretical evidence that this actually increases the sensitivity.**

**And indeed, people have used simple Ising type models to try to understand how the coupling between the binding of repellents on what's essentially almost like a crystalline array of receptors can allow the array to better than you build it to as an individual. We're not going to get into that here, but in any case, there's receptors at the poles-- I don't know if it's both poles or one pole, but one of the poles of the other-- and that's where chi Y is phosphorylated.**

**But then, you can see that these flagella are distributed all around the cell. So you have to diffuse from say, the pole to the site of the flagella motor in order to cause it to go clockwise and then cause a tumble. Yeah?**

**AUDIENCE: So do you need only one motor?**

**JEFF GORE: Yeah, so you actually only need one motor to get the tumbling. And so then, you may not have to diffuse all the way to the other end, but-- and of course, diffusion is random. And we all know that 0.1 seconds is around the time that it takes for a protein-sized object to diffuse across the volume of a bacterial cell. We did that calculation a couple weeks ago. So 0.1 seconds is indeed-- so the rate limiting step is indeed this step right here, which is diffusion of chi Y, the phosphorylated version of it.**

**All right. Now, we may not get too much into the models here, because you did read about them. But I will just kind of sketch out sort of what you might call the finetuned model and then the key assumption that goes into this robust model. Now, what both models assume and indeed what was known from previous work was that chi R is present at small number. So chi R, there might be around 100 proteins in the cell. And what does this mean about the activity of chi R? What is the other word for it? It doesn't actually have to quite mean it, but what is it that-- how--**

**AUDIENCE: [INAUDIBLE]**

19

|**JEFF GORE:**|**What's that?**|
|---|---|
|**AUDIENCE:**|**[? High ?] saturation.**|
|**JEFF GORE:**|**So yeah, something is high. And what is typically assumed is that chi R acts at**<br>**saturation, chi R. But what do we mean by "saturation" in these models?**|
|**AUDIENCE:**|**Maximum.**|
|**JEFF GORE:**|**Right. Does it mean that if we add more chi R than the rate of methylation, it doesn't**<br>**increase? And I should have put a little methyl group here. There are multiple things**<br>**you might mean by "acts at saturation." And in the models that you read about last**<br>**night, is what it means that if we increase the number of chi R that it doesn't change**<br>**the rate of methylation? Yes or no? Ready? Three, two, one.**|
|**AUDIENCE:**|**No.**|
|**JEFF GORE:**|**No. And what they mean is something rather different, which is that if we plot or if**<br>**we calculate the change in the concentration of the methylated X-- now, we're**<br>**calling this whole thing Xm, methylated X, and this is just X. The assumption is that**<br>**we have X is being methylated at a rate that is-- there's no Michaelis-Menten term.**<br>**If we were to write this as it not being saturated, what is it acting on?**|
|**AUDIENCE:**|**[INAUDIBLE]**|
|**JEFF GORE:**|**Yeah, it's not the methylated x. So indeed, if we were to write this, we're assuming**<br>**that this is at saturation, as they say. But any time that you see something like this,**<br>**you have to ask, well, what would be the alternative, right? And the alternative**<br>**would be to include a term that looks kind of like just X over some K plus X, because**<br>**R is acting on the unmethylated X.**<br>**We're not including that. What that means is that we're assuming that this thing is**<br>**saturated, that the concentration of X to be acted on is significantly larger than the**<br>**Michaelis constant there. And of course, this is related to the amount of R, because**<br>**as we get more and more R, then eventually, we'll remove some of this X and then**|


20

**we'll get into the non-saturated regime. So these two statements are related, but not the same thing.**

**Now, there's also some rate that the phosphorylated version of B removes the methyl groups and that's indeed just going to be this Michaelis constant. And this is going to be for the fine-tuned model. The robust model looks very similar, but this is the simplest kind of manifestation of this model.**

**Now, once we're writing this down, it's useful to make sure that we can keep track of what's actually happening over the course of perfect adaptation. So now, let's imagine first that an attractant arrives. That's going to change the activity of X. And when we say "activity," what we mean is the rate that's it's going to phosphorylate both B and Y.**

**So let's just make sure that we know this direction. So we add an attractant. We'll say "add." What does this do? Does it make activity go up or down? I'll give you 15 seconds to make sure that you kind of understand the workings of this network. This is activity of X, this complex X. All right. Do you need more time? All right. Let's see where we are. Ready? Three, two, one.**

**All right. So we got a majority of the group is saying that it should go down. Well, let's just follow the logic. So we imagine an attractant binding. If the activity goes down, that means that we get less of the phosphorylated chi Y. That means we get less propensity to tumbling, which means that we keep on going further. All right, that sounds reasonable. Any questions about that logic? Yes?**

---

[← AUDIENCE: [INAUDIBLE]](04-audience-inaudible.md) · [Up: contents](index.md) · [AUDIENCE →](06-audience.md)
