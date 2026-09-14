---
title: action on chi B.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/ct855rpx8bc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# action on chi B.

**Source:** `recordings/ct855rpx8bc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**All right. So what happens is that the attractant causes less of the phosphorylated chi Y. But it's also going to cause less of the phosphorylated chi B. Now, that means that we're going to-- and remember, the phosphorylated chi B is what's removing the methyl groups. So if we have less flux going to the left, but we have the same-at that moment, we don't have any change in the flux going to the right. So chi R is still acting on the same unmethylated X's that it was operating on before. So it's the same flux to the right, less flux to the left.**

**So there's a net accumulation of the methylated receptor, which we are calling X. So the key thing here is that-- and it's this methylated receptor that has more activity. In this model, this unmethylated version actually doesn't have any activity. So then, if we get more of the methylated X, then over time, we get a buildup of the methylated X and that causes the activity to come back up.**

**Now, of course, there's a question of-- I just said that it comes back up, but I didn't say that it comes back up exactly to its original tumbling frequency. I didn't say that it necessarily displays perfect adaptation. And that's because in this model, the perfect adaptation arises as a result of what we call fine-tuning, because it only happens if all of the parameters are just so.**

**In Uri's book, he describes a typical condition where that would be the case. And the problem is that you can always fine-tune for some concentrations of everything, chi R or chi this, chi that. But then if the concentrations change, then you're no longer fine-tuned correctly. You were fine-tuned for a different world and now you're not-and that's the definition of being fine-tuned is that if things change, you're no longer fine-tuned. You're just finely off-tune, right?**

**So this is the problem with the fine-tuned model is that you can get it right for a given-- for given concentrations of everything, you can always find what numbers. This is VB and then there's going to be-- you can talk about the activities of XM given the previous attractant concentration and so on and so forth, but it's not going to be fine-tuned if you change anything else, like if you change concentration of R,**

22

**for example. And I'm happy to go through the math and so forth maybe after class if anybody's curious, but it's really precisely what Uri did, so maybe I won't get into it now.**

**But the question then is, well, how is it that you might change this model in order to make it robust? And the change is somehow surprisingly simple, which is that what you want is chi B, instead of just acting on any old methylated X, you want it to act only on the methylated X that is in sort of in what we would call this active state, where it's actually able to catalyze either of those reactions.**

**So the notion is that if you have this methylated X, then it's kind of over a very fast time scale. It's switching between what we call an "active" state and some inactive one. And it's really only in the active versions that chi B is able to act on and remove the methyl group. And this is on the one hand a clever thing that allows you to implement this integral feedback. On the other hand, it's a little bit of like pulling a bunny out of a hat, because you feel like, well, these things may be happening over microsecond time scales. It's hard to know exactly-- how would you actually experimentally confirm this is precisely what's going on?**

**And I think that here, it's a little bit subtle because you could maybe show that indeed the rate of this demethylation is proportional to the activity here, but you don't necessarily have access to all of the molecular dynamics that are taking place over microsecond time scales. So I think that you can do measurements that give you confidence that this is maybe what's going on, but you can't quite 100% nail it because of the nature of these molecular fluctuations.**

**So the idea there is that if we say that there's this rapid shuttling between the socalled "active" and "inactive" methylated guys-- so this is indicating that it's what we call "active," able to catalyze this and this-- then this ends up being equivalent to integral feedback, where you'll always get perfect adaptation. Yeah?**

**AUDIENCE: When you put [INAUDIBLE]**

**JEFF GORE: So the idea is that we imagine that we're this receptor X. It's chi W, chi A. Now**

23

**whether it's-- let's say it's bound to something. It still bound to an attractant, right? The way that the attractant influences its activity-- and it has to influence its activity if it's going to do anything-- what we assume is the way that it's doing it is that it's changing the sort of fraction of time that I'm in some active conformation where I can actually do work, versus the inactive conformation where I'm taking a break. So when you get the attractant and you spend more of your time in this active conformation where you're, in this case, phosphorylating proteins, and that's sort of the mechanism through which an attractant or a repellent or whatnot actually transmits its signal. And indeed, it has to do something.**

**Nothing that we're discussing would work at all if we don't allow the signal to be transmitted somehow through this receptor. So there is this sense that this activity has to be a function of the things out there. And the assumption that goes into the perfect adaptation is really that the rate of demethylation is proportional to that kind of active fraction. And then, you can argue about how discrete these entities have to be in order for the mechanism to work and so forth, but certainly, there has to be some way that binding to an attractant leads to what we decided was less activity. Yeah?**

**AUDIENCE: Just a quick question. So what's the relationship between activity and methylation? Was it [INAUDIBLE]**

**JEFF GORE: So the idea is that we're typically maybe assuming that the unmethylated guy has no activity, so it doesn't do any of this phosphorylation, whereas the methylated guy has some activity. And you can characterize it by some rate of activity or some fraction of the time that it is in this active state that is doing something. Now, the question-- and indeed this ends up-- well, you can see here that in this model, because you're directly acting on the active XM, then the steady-state activity you can get from just setting this equal to zero and it's some number. But then, the question is, how long does it take to come back to that steady state? And that's where we get differences as a function of concentration of chi R, because what's happening always is that we have some kind of cycle here where chi B is**

24

**removing the methyl groups, groups chi R is adding them back. So you can imagine that if you have more chi R than a steady state, you get more-- when you're moving right by a steady state, you have to have the same moving to the left, because at steady state, it's equal. So the more chi R you have, the faster this thing is going around. And that means that the more chi R that you have, the more rapidly that you'll get this perfect adaptation.**

**So the experiment that Uri did that I think is very nice is he directly modulated the amount of chi R and he looked at this adaptation time. And he found this kind of came down, whereas if you look at the steady-state tumbling frequency, this came up, whereas the degree of perfect adaptation, say the ratio or the error in this thing, perfect adaptation was always kind of correct, in the sense it always came back to its original value.**

**AUDIENCE: Sorry. You say the [INAUDIBLE] it only phosphorylates chi B when an attractant [INAUDIBLE] Y [INAUDIBLE] attractant.**

**JEFF GORE: No. So the attractant or repellent can be combined to either the methylated or the non-methylated, right?**

**AUDIENCE: But [INAUDIBLE] only [INAUDIBLE] phosphorylation of chi B when [INAUDIBLE]**

**JEFF GORE: No. So you're talking about-- oh, OK. So it's really that the methylated state can phosphorylate either chi B or chi Y, but this is regardless whether an attractant is bound or not. The attractant will influence the rate or the activity that this happens. And given this model, you can see that you have more chi R, then at steady state, you're going to have more activity. More activity corresponds to more phosphorylated chi y and more tumbling, so an increase in the tumbling frequency. Yes?**

**AUDIENCE: I guess it's not clear to me where the ligand concentration actually come in.**

**JEFF GORE: Where which concentration? AUDIENCE: The ligand concentration.**

25

|**JEFF GORE:**|**Oh, OK, yeah.**|
|---|---|
|**AUDIENCE:**|**Because that's what [INAUDIBLE]**|
|**JEFF GORE:**|**Yeah, right. Yeah, so the idea here is that if we start out without any attractant-- so**<br>**first of all, so let's imagine we're at steady state. There's no attractant or little**<br>**attractant now, where of course, the fluxes to the left and the right are the same. So**<br>**there's some methylated, some not.**|
|**AUDIENCE:**|**No, but I agree the mechanics of just in the actual to write an equation for the**<br>**ligands to come in like [INAUDIBLE].**|
|**JEFF GORE:**|**Right. So the idea is that when you bind an attractant, that's going to change the**<br>**activity of the methylated. So it's going to change, for example, the fraction that are**<br>**active.**|
|**AUDIENCE:**|**And decreases the activity.**|
|**JEFF GORE:**|**And it decreases the activity, right.**|
|**AUDIENCE:**|**And some sort of signal--**|
|**JEFF GORE:**|**Yeah, there's some-- right. And of course, we haven't specified what that function,**<br>**but the idea is that it leads to a rapid decrease in activity, which corresponds to a**<br>**rapid decrease in this fraction that are active XM star. Does that make sense?**<br>**So the last thing I wanted to do is say something about what this means for**<br>**individuality. In particular, let's imagine that we have a clonal population of bacteria.**<br>**And the question is, in what ways will they be similar or different? So now, we can**<br>**just imagine an experiment where I take a population of cells with exactly the same**<br>**genetic code and I go and I measure, for example, the tumbling frequency across**<br>**this population.**<br>**So we can talk about-- we measure f1, f2, f3, fn-- so these are the tumbling**<br>**frequencies across n cells. This is n we'll say genetically identical cells. The question**<br>**is, will we get the same tumbling frequency or should these things be the same?**|


26

**And if not, why not? So let's just do our little votes, all right? We have should they be the same or should they be different. All right. Do you understand the question? Let's vote. Ready? Three, two, one. All right. Well, OK, so at least the majority of people are saying they should be different. And why might that be, somebody?**

---

[← [INAUDIBLE]](07-inaudible.md) · [Up: contents](index.md) · [AUDIENCE →](09-audience.md)
