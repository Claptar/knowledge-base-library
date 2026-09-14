---
title: fundamental.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lly1u2aghiq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# fundamental.

**Source:** `recordings/lly1u2aghiq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: You should have a rate from S to P without the enzyme. PROFESSOR: Right so maybe there should be a rate, S to P, without the enzyme. Although, I'm just trying to tell you about the rate of what the enzyme is doing, so you could write a difference equation. If I just let this model go to infinity, then what happens? AUDIENCE: You get P. PROFESSOR: You get P. And how much P is it? A lot of P? A little bit of P? AUDIENCE: As much as it can make. PROFESSOR: It's all pee. Right? And how much substrate? None, right? So if I just let this go, you have 0 substrate, all product. Is that OK? I mean is that, in general-- I like product. AUDIENCE: Time. PROFESSOR: Time? AUDIENCE: How much time it would make too. PROFESSOR: Well, we can calculate what the V is in this model, and then we could figure out what the time. But there's something wrong with that. And normally I wouldn't want to belabor the point, but it's worth belaboring maybe. AUDIENCE: Yeah. If we had a back reaction, then that wouldn't happen. PROFESSOR: Right, OK, so this gets back to your back reaction, right? And I like the back rate. It's just there was something a little more fundamental than the way you phrased it, was my concern. Because what you said is, there might be some back rate. Right? And I guess what I would say is that there's kind of always some back rate, or that the equilibrium-- this is fundamental-- the equilibrium ratio between S and P, how does the enzyme change it? AUDIENCE: Not at all.**

16

**PROFESSOR: It doesn't change it, right? So if you take the enzyme, invertase, and you put it in a test tube with sucrose, it's going to break down almost all that sucrose, really fast. It's going to speed things up by a factor of 10 to the 5, or I don't know, by a lot. But if you leave the test tube for a year, it comes to an equilibrium with the enzyme. If you left it in the test you without the enzyme for a million years, you would get to the same outcome. You come to some equilibrium between the substrate and the product. And that's a function of the kinetics. There's a delta G and so forth, but the important point is that the enzyme does not change that equilibrium. AUDIENCE: I just have a question. This molecule is effectively [INAUDIBLE]. If you leave it in a test tube for a million years, then the ATP will all be consumed. PROFESSOR: Yes. AUDIENCE: But if you keep providing ATP, then you should-PROFESSOR: Well, first of all, not all enzymes actually are coupled to ATP. So ATP is a way of putting out a big delta G, right? So that you can really push things far. And ATP could, in principle, be included as a co-factor, and then you take the overall delta G of that, and then calculate it. But if you want to keep on adding, then it complicates things. But I think, for many enzymes, it's more straightforward just to think about enzymes that don't require any extra input of energy. So they're just lowering the energy barrier and they're just speeding up the rate of reaction. But the important point there is that they're speeding up both rates. So the equilibrium between those two is not going to change. And that's why, this thing, it's a great model, but like all models you have to make sure you keep track of what the assumptions are going into it. Because this is going to violate the laws of physics if you take this model too seriously. AUDIENCE: I don't understand what the fundamental principle that's being violated is. Because why is it not that if you have it stable, everything is product. You never see as in**

17

**nature. I mean, how is that not a physical situation?**

- **AUDIENCE 2: So if you can get a really small test tube with one G and one S, isn't it just like-PROFESSOR: But the same statement that we talked about for single, then you would want-- if you had just a single substrate going to product-- then you want to look probably at the time average. Because, the thing is that the equilibrium is determined by the delta G of the reaction. And that's going to determine the equilibrium, whether you have the enzyme there or not. So if the delta G is such that it's at equilibrium-- sort of 90% product, 10% substrate- then what you can do is go, well if you start out with all substrate, this model may work wonderfully. But then as you're getting closer to that equilibrium, then this model's going to be breaking down because this model is not accounting for the back reaction, as you were saying. But I just want to stress that it's not just a detailed model, or it's not just a failure for some enzymes, this is the way that enzymes work. Are there other questions about this? Or different ways of thinking about it? So, it's not used up. It speeds up reaction in both directions.**

- **AUDIENCE: I mean, but that's not necessarily true. You can have an enzyme that is only really capable of going in one direction.**

- **PROFESSOR: Really? We should meet after class and you can give me your-AUDIENCE: It basically binds in a particular direction. PROFESSOR: It's just not allowed. So it's true that enzymes can be-- and this is getting to the other fundamental point of an enzyme, which is that they, especially enzymes in biology, can be exquisitely specific. What you're saying is that it's really only catalyzing this one, weird reaction, going from some funny substrate to some funny product, right? But that enzyme also speeds up that back reaction, going from the funny product to the funny substrate. And that's just like the nature of the beast. I'm try to think of what I can--**

18

- **AUDIENCE: That's where you have one enzyme going one way, and another going the other way in biology.**

- **PROFESSOR: So it does happen there, but then what they are often doing is they're coupling things to ATP hydrolysis or something, in order to actually make that reaction go in the single way. Just as kind of like a general statement-- because the way these things work is that there's some over here and it's over here somehow, and these enzymes, they just lower this energy barrier.**

- **AUDIENCE: So the thing that confused me at first is that I was just thinking of rates, and I think the thing that's important is to just realize again that the enzyme doesn't change the thermodynamics, it only changes that variable to change where they are. So the key thing is that it doesn't change the ratio of the product through the substrate, the rates are realatively--**

**PROFESSOR: Right, because from a thermodynamic standpoint, it's not used up, which means there's an enzyme here and an enzyme here. So these final states, you can think about only in terms of the substrate and the product, because the enzyme was there in both beginning and ending. So from a thermodynamic standpoint, it's just you're not allowed to change one rate without the other.**

**Now in the reading, you saw the Michaelis Menten kinetics, where you found that once you reach this equilibrium between the enzyme substrate complex, the velocity can be described by something that is rather simple. There's some Km plus S, and then there's some Vmax. And if the substrate concentration, the total concentration is very large, then you can just think about this is the S total. Now in this case, this, once again, can be thought of in this limit of if the enzyme concentration is really small, then this is really just the fraction of the enzyme that's bound.**

**So we've already spent a lot of time thinking about how to get at the fraction bound, and the question is, what should this Km be here? Now that I've told you that it's the fraction bound, is it just going to be the same thing that we had before? Is the Km the same thing is the Kd? So remember, before, we found that Kd was just Kr over**

19

**Kf. But you should, in principle, be able ti just look at that and say what fraction bound should be.**

**AUDIENCE: Is it Kr over Kf plus-- other way around, Kr plus Kcat over Kf PROFESSOR: Yes, because now, from the standpoint of the enzyme, there's some rate at which you form the complex. And now the lifetime of that complex has been reduced, because now there are two ways for the complex to fall apart, right? One, is could just go back where it came from, but the other is that you can catalyze the reaction. So, from the standpoint of the enzyme and the fraction bound, then we can just-the entire discussion that we had before-- we can just replace Kd with this new Michaelis constant, Km. Where now, we say now it's the Kr up in the numerator still, but now, instead of just being Kf at the bottom, we have to add Kcat, because there are just two ways that that enzyme substrate complex can fall apart. Oh I'm sorry, I've already messed up. Kf over-- So Kcat has to be with Kr. So it just kind of speeds up the effective rate of dissociation. And of course, depending whether Kcat is large or small as compared to Kr, this can be either a large or small effect. But these rates, they just add. And we'll spend a lot of time thinking about how rates add and so forth in a few weeks.**

**AUDIENCE: For this expression to be valid, don't you need Kcat to be much longer than the other rates? PROFESSOR: Right, yes. So you want Kcat to be-- So there's various kinds of limits in which you can talk about this thing. So in general, what you want is Kcat to be small, and you also want the initial transient to have gone away. Because when you first add the substrate, you don't yet have any enzyme substrate complex. So you have to wait until you've gotten to this so-called steady state, where the Michaelis Menten formula applies. And then you also can't have let it go too far, because then of course you're going to start running out of substrate.**

**In the homework, you're going to get a chance to play with Michaelis Menten kinetics a little bit, and think about the dynamics when you have different kinds of**

20

**inhibitors. So you can imagine having inhibitors that inhibit multiple different ways. You could have an inhibitor the binds the enzyme, and prevents the enzyme from providing the substrate. Now should this effect the Vmax?**

**We'll think about it for 10 seconds and we'll vote because it's so much fun. We have these cards. Vmax change-- and this is with an inhibitor that binds here-- and forming an EI complex, reversibly. The question is, does Vmax change? A is yes and B is no. I'll give you 10 seconds to think about this.**

**So Vmax is, again, defined as this rate of product formation at saturation, when you have a lot of the substrate. Do you need time? Or will time help? Well who wants more time? Just nod if you want more time. OK, well let's see how we feel. Let's go ahead and vote.**

**If I add this competitive inhibitor, the question is, will be Vmax change? Ready. Three, two, one. So we have a majority of Bs, but some As. Can somebody give the intuition for why the Vmax should not change? Yes.**

**AUDIENCE: Vmax is when substrate is far excess to the enzyme and, at that time, all of the enzymes bond to the substrate not to the inhibitor.**

**PROFESSOR: Right, right. So Vmax occurs when you have lots and lots of substrate. And, of course, the condition you have to be a little bit careful, because it's not just having more substrate than the enzyme, but it's when the substrate is saturating. So if you have lots and lots of substrate, then the important point there is that it's when you've pushed this reaction all the way over here, all the enzyme is bound, and that's when you get this maximal rate of product formation.**

**And that's true, you might need more substrate in order to get all that enzyme bound, because you have to pull the enzyme away from this side reaction. And, indeed, this kind of inhibitor alters the Km, the effect of Km of the reaction. But it does not affect this Vmax, whereas other inhibitors can bind this complex and prevent it from catalyzing the reaction. And that will instead affect Vmax, but won't affect Km.**

21

**So this was a powerful way that enzymologists have used to try to get at mechanism of inhibitors. So if you have some small molecule you know somehow inhibits some enzymatic reaction and you want to know, how is it doing that? One thing you can do is you can titrate in that inhibitor and then measure the Michaelis Menten curve to get out the Vmax and Km to try to get a sense mechanism.**

**And I always say we should be drawing these things. So V is a function of-- and this is in the [? lit ?] for a lot of substrate relative to the enzyme-- then we can indeed say it's going to plateau in Vmax at concentration Km. It's at 1/2. And then it plateaus. This is a very, very, very common curve. Lots of things in biology and life start at 0 and plateau, and there are almost only two ways you can do that. OK, there are more than two ways, but there are a very small number of ways you can do that. This is one of them.**

**Any questions on these Michaelis and Menten kinetics inhibitors? You're going to spend a couple hours over the next few days thinking about this.**

**So what I want to do for the last 20 minutes is switch gears a little bit and to think about the simple dynamics of gene expression. The ideas that we've just been talking about end up being just very relevant for the simple models here.**

**So what we want to think about is a situation where we have some transcription factor, X, that is activating expression of gene Y. So we have X activating Y. Now, the way we can think about this, for example, is that we may have X, which together with some signal S of X, turns into some X star It's X star that can bind to the promoter and lead to expression of Y.**

**Now in Uri's book, he talks about this idea of a separation of time scales that is often useful to invoke when thinking about gene expression. In this context, what was the fast event?**

**AUDIENCE: Activation of X?**

**PROFESSOR: Activation of X. So in many cases, if this is a sugar or a small molecule that is going**

22

**to be, in this case, activating X, that can occur really quite quickly. Often maybe less than a second. The rate-limiting step would then, in many cases, be getting the signal into the cell, so depending on how that works.**

**So this occurs very rapidly. What that means is if we look at a signal Sx, as a function of time, where it starts out being absent and then, all of a sudden, sugar appears in the environment, we can think about the concentration of X and X star So X starts out high and then quickly goes down, right? Whereas X star will do the reverse here, quickly comes up. And this should be flat.**

**Now, what is it that Y will do as a function of time? So if X is an activator that means that before X star became available, there was no expression of Y. So it should be low. So X is quickly activated, turns into X star. So we start expressing Y. So, roughly, what does this curve look like? Somebody please help me.**

**AUDIENCE: It's S-shaped.**

**PROFESSOR: OK, so it could be S-shaped. The thing that's very fast is activation of X, and then what's really still rather fast is equilibration of X star on this promoter. So that might still be very rapid because these things were nearly instantaneous, But. Coming to equilibrium here still might happen over time scales of seconds.**

**So that means that you actually, sort of quickly, start getting expression, at least on time scales are relevant in terms of hours kind of time scales. Of course, it still does take time to express. So it takes minutes for the RNA polymerase to transcribe, and then of course the ribosome's going to have to do something. What do I want to ask?**

**Let's write down the equation that Uri invokes because there's a very real sense in which it does, maybe, look a little bit more S-like. But at least in terms of Uri's kind of formalism, he often would say, the change in the concentration of this protein, it's going to be some function of, in this case X star. And then there's another term here, which was the minus alpha Y. What was the minus alpha Y due to?**

**AUDIENCE: Degradation.**

23

**PROFESSOR: Right, so there are two terms. So there's alpha, and it's going to be the sum of two things. There's alpha due to degradation. So if the protein is degraded actively in some way. If the protein is not degraded, then does that mean that alpha is equal to 0? No. So what is this other term? AUDIENCE: Cell growth. PROFESSOR: Right, so it's alpha due to some growth. And cell growth leads to some dilution effect. So if you have the same number of proteins in the cell that the cell is growing, that means the concentration is shrinking. Right? Now the reality of this process is that it's complicated, because cell growth is not uniform. But if you kind of average over things, then a reasonable description is just to say, just a first order effective dilution rate. If you want to, you can write down a more detailed formula, or a model where, you say if cell growth does this, then-- It's going to kind of wiggle a little bit over the course of the cell cycle, but this is a reasonable description. Now what this is saying is that even if there is no active degradation, then there still is an effective term due to this dilution. And this means that if we immediately activate, and if F of X star-- at time T equal to 0 here-- if it just goes to some beta, then what is the long time solution of this equation? AUDIENCE: Beta/alpha. PROFESSOR: Beta/alpha, right? So we know it should eventually come to beta/alpha. What's the characteristic time scale for it to get there? AUDIENCE: Cell alpha's rate, it's 1/alpha. PROFESSOR: Right. So characteristic time is 1/alpha. The solution to this differential equation is just an exponential where, if extend this line here, this is 1/alpha. So that's time. And then, of course, the T 1/2, the time it takes to get to 1/2, is indeed different by log 2, and that's the cell division time. This point here-- this is at T 1/2-- is cell division.**

24

**This is for a stable protein, assuming that alpha degradation is equal to 0.**

**So the thing to remember is that this basic differential equation of Y dot is equal to a minus alpha Y, is an exponential by going to 0. Whereas if you have a constant term here, then it's an exponential going to some nonzero value. So, indeed, if the signal here goes away, then we quickly come back here. So this comes here. This comes here, and then this-- does it go back down to 0? Is it more or less rapid returning to 0 than it took to come up?**

**All right. OK. So, how can I phrase this? OK, faster decay, question mark. A is yes, and B is no, and you can always do C or something if you don't know what I'm asking.**

**The question is, we've turned off the signal, is it going to go away faster, or slower, or the same? This is faster. B can even be slower maybe. C is same. Do you understand the options now? So we stopped expressing Y, so concentration of X is going to decrease, right? Question is, it is going to go away faster, slower, or the same as the rate that it came up?**

**Do you need more time? Ready. Three, two, one. OK so we have a fair agreement that, this thing, it's going to be the same. So there's a characteristic time for it to come and it's the same characteristic time for it to degrade away. So this, I would say, is not a priori obvious, but it's really just the nature of when you have these sorts of situations. This sets the time scale for if you want to change the concentration-- doesn't matter whether you're going to 0, a finite number, or if you go from high to low, but not 0. Again, it's going to be exponential in the same time scale.**

**So if you want that to be faster, if you want to be able to respond more rapidly, then one solution would be to actively degrade the protein. Right? Now it's obvious that degrading the protein actively will allow it to go way more rapidly. What's perhaps less obvious is that there's a real sense in which degrading the protein allows this response to be more rapid as well. But of course, did we keep everything constant? If I say, oh I want the curve to look like this, can I just increase the degradation rate?**

25

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE]. →](05-audience-inaudible.md)
