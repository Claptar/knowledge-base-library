---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/cn5k8r8ceii-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/cn5k8r8ceii-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Everyone all dies.**

**PROFESSOR: Yeah. Everyone's going to die, right? And that's even true in the-- it's not even that the population's dying as a result of the infection. Because even in the absence of any infected individuals, you just have people dying. So you need to have some way of keeping the population going, so you can study it perhaps. What we're going to assume is that sensitive individuals, or uninfected individuals, will enter the population just at some rate, k.**

**Now, in terms of the philosophical question, in the beginning of the chapter, Martin talks a bit about this question of microparasites versus macroparasites. And I can somebody remind us, what's the distinction? and For what kind of parasite might this be intended to model? Yes?**

2

**AUDIENCE: Well, what I got from it is that microparasites are on the order of single-cellular organisms, generally things that have much shorter reproductive steps, I guess. They reproduce a lot more frequently.**

**PROFESSOR: That's right.**

**AUDIENCE: Whereas, macro-parasites are like the [INAUDIBLE] or the tapeworm or something, which would not necessarily reproduce a lot inside the host.**

**PROFESSOR: Mm-hm. Right. And I would say, that just given this distinction between the microparasites, that might be viruses and bacteria, as compared to the macroparasites, that are things like tapeworms and so forth, it's not obvious from that that you would have two different modeling frameworks.**

**But what is the argument that is made in Martin's book? Or can you think up an argument for why it is that it might be this kind of model you would want to use for microparasites? Yes.**

**AUDIENCE: Because we don't really care about-- he mentioned something that the microparasites reproduce in large numbers in infected individuals. So we don't have to keep track of the internal state of someone that's infected.**

**PROFESSOR: That's right. And some of it's, maybe, even a historical thing. There might be huge numbers of viruses-- a flu virus or so-- in an infected individual. And in some ways, maybe, the number of viruses that is in that host is not the most relevant thing. And it's certainly would be much more complicated to try to keep track of that.**

**And so, if you can get meaningful predictions-- rather than keeping track of the number of viruses, say, in each host, instead you just put the host into different classes-- sensitive and infected, for example. Later, we'll talk about what happens if you have a resistant type of class. But the idea there is that there's, maybe, even also some separation of time scales. Because you get infected. And kind of quickly, you're just sick and may be infective.**

3

**But at some rate, you get better. And it's not that you'll necessarily gain very much by keeping track of the precise number of viruses in the host. Of course, this is ultimately an experimental observational question of whether this sort of model provides you inside that you're going to need to make sense of these diseases, right?**

**AUDIENCE: And then it also seems like your method of transmission of macroparasites can be very different.**

**PROFESSOR: That's right. So the mechanism of transmission depends very much on the disease that you're studying. And the macroparasites, in many cases, they're transmitted not from direct interactions between the hosts, but through the environment or something else.**

**It's also, perhaps, just worth pointing out that parasites are just a ubiquitous aspect of life. So you can name an organism, and you can pretty much be guaranteed that there's going to be some notion of a parasite on that organism. And there can be multiple layers of this. So we certainly have many parasites. We're infected by many viruses and bacteria and other things.**

**But bacteria-- we think of them as being very small-- they're also preyed upon by these phage, which is a parasite that targets specifically bacteria. So it's not just that it's an incidental thing. But these are really viruses that have evolved specifically to divide in bacteria.**

**And we didn't really talk about this very much. But one of the classic models for cooperation and cheating is based on what you could think about as some sort of parasitic sub-population within phage. So this is a classic paper by Lin Chow where he showed that if you evolved phage and bacteria in a condition where many phage infect a given bacteria, then, you can evolve what you could think of as cheater strategies or cheater phage.**

**Because these are phage that maybe can't reproduce on their own, but have shorter genomes and can out-replicate the normal phage. So if both of these end**

4

**up in a single bacterial cell, then these cheater phage can spread by taking advantage of, say, the replication machinery from the rest of the phage. So in some ways, you might call that some sort of DNA parasite or so. So there's really parasites in many, many different levels. AUDIENCE: [INAUDIBLE]. PROFESSOR: Yes? AUDIENCE: [INAUDIBLE] ultimately think about is, k, is this really the number-PROFESSOR: Yeah, you know, I would say that the k is, in some ways, not a very satisfying feature of this model. Because it makes it feel that the model is very special, right? AUDIENCE: But I mean, in a natural population and rate at which people are born, is that the same change? Or-PROFESSOR: Yes. That was the example I was going to give. It's not clear-- of course, it requires somebody to give birth to kids, right? So in that sense, modeling this as a constant number per unit of time-- which is what we're doing-- this rate k, is a little bit funny. Because then, what you'd really want to do is say, oh, maybe it's these guys that give birth at some rate or so, if you really wanted to be accurate. So I'd say that this is, in some ways, just a mathematical simplification so that we can get at the heart of the dynamics. And what we'll see is that, in these SIR models, you don't invoke anything like this. But rather, what you do is you assume that, at some rate, infected individuals don't just die. But they become resistant. And then, maybe later, they become sensitive again.**

**So you need some way of being sure that it's not the case that everybody just always dies. So in some ways, this is more mathematical convenience. And the basic conclusions end up being very robust to these sorts of things.**

**All right, so in these models, it's always good to be clear about how we go from this framework to something that is more of a differential equation. And what we can do is we can think about these uninfected individuals, i.e. the S-es as compared to the**

5

**infected. And we're going to have these guys be x. And this S and I.**

**So the way that the x will be changing is that we're assuming that there's always some influx of individuals, which could be birth or migration or something else, that are just always entering. But then, there's going to be two ways that x is going to decrease. One is that there's just a death rate that is resulting in the absence of infection.**

**But then, also, there's going to be some rate of infection, which is going to be proportional to beta. So this is the simplest way that you can imagine capturing this element that the infected individuals can transmit the infection to the sensitive individuals. So we're modeling them as a well-mixed population, just like in chemical reactions. And somehow, the rate of infection is proportional to the frequency that they hit each other. Certainly, the simplest kind of model you can imagine.**

**Whereas, the infected individuals-- well, we're going to have an increased rate of death. So this is a simplified way to write it. So this is really that there's a minus, u plus v times y. So this is just the death rate. But then, any individual that leaves the sensitive class-- this minus beta xy-- enters the infected class. This makes a lot of sense, I think.**

**Now, the question is, can we make sense of what's going on? Now, you saw in your reading what this R0 parameter was. And you should always remember that it's defined as this thing of, if you introduce one infected individual into a population of sensitive individuals, what is the mean number of new infections that you get?**

**And it makes sense that the key thing is whether that R0 is greater or less than 1. Because if it's greater than one, that leads to this exponential explosion of the infected individuals. It doesn't mean that everyone's going to die, necessarily. We'll get into that. But if R0 is less than 1, then you expect that infection to die out.**

**So why is it that if R0 is greater than 1, and you introduce one infected individual, it doesn't necessarily lead to a wipe-out of the entire population? Or maybe it does. This model is a little funny. Because you always have an individual entering. But--**

6

- **AUDIENCE: If the [INAUDIBLE] is really virulent, then only infected individuals die before-PROFESSOR: Right. So if it's very virulent, then the infected individuals may die quickly. And this gets into this question of there may be some trade-offs in terms of virulence. And we'll talk more about, then, the evolution of virulence. But there's a wide variety of classes of models, not just the ones where you have k entering. But the question somehow is-- just because R0 is greater than 1, that doesn't mean that the entire population will necessarily become infected. Because we have this idea of an exponential growth of the infected population if R0 is greater than 1. So why is it that it's not necessarily going to happen that the entire population is-- well, this question's a little bit ill-posed in this model.**

- **AUDIENCE: Is it because the number of sensitive individuals becomes very low at some point and--**

- **PROFESSOR: That's right. And I think this is the basic intuition. As more and more members of the population become infected, then that could, in principle, reduce to the possibilities for new individuals to be susceptible. And I'm using susceptible and sensitive interchangeably. And so eventually, this exponential growth of the population can be limited in some way. We'll maybe look at this a little bit more in this SIR model. Because it's more clear.**

- **AUDIENCE: So we basically collect a rate. R0 is a rate, right? [INAUDIBLE]. PROFESSOR: No. It's a number. It's the expected number of new infections that you get when you introduce one infected individual into the population. And we're--**

- **AUDIENCE: It's like, period. So there's not, like, per-unit time or-PROFESSOR: It's a number, period. AUDIENCE: OK, so if you have R equal to 1, you expect that when you introduce an infected individual into a population of sensitive individuals, you will get one other infected individual.**

7

**PROFESSOR: That's right. So that's kind of the neutrally-stable situation. If R0 is 1, then you add one infected individual and you expect to get one other one, so you have a random walk and-- well, in general, it will randomly go extinct, eventually. Yes? AUDIENCE: What is the lifetime of the infected-PROFESSOR: So it depends. And so, that's what we're going to do right now is see if we can reconstruct what this R0 is equal to in this model. AUDIENCE: Another quick question-- what's the distribution of the-- so--**

**PROFESSOR: Yes.**

**AUDIENCE: --a deterministic role--**

**PROFESSOR: Yes, exactly. So this is very interesting. The question is, what is going to the distribution of the number of infected individuals? And in this model, we're assuming that every infected individuals is the same. So we should be able to-- I wish that we just, on the wall somewhere, had our five different standard probability distributions, so that we could always go back to them.**

**So the question is, in this model, if you introduce one infected individual in the population, how many new infected individuals do you get? R0 tells you about the mean. But will you always get the mean? No.**

**So let's all think about this for 10 seconds. And we will verbally yell out what we think the distribution will be of the number of new infections from a single infected individual. OK? Verbally, ready! Five, (WHISPERING) four--**

**AUDIENCE: Poisson. AUDIENCE: Piosson. AUDIENCE: Exponential PROFESSOR: All right, everybody thinks it's Poisson. Why would it be Poisson?**

8

**AUDIENCE: Because you have a rate-AUDIENCE: It's not a rate. AUDIENCE: It's not? AUDIENCE: The initial population is much larger-PROFESSOR: Right. OK, so the idea is that we imagine we're some infected individual. And there's some rate that we are infecting others. Now, if I ask you the question, how many individuals will I infect in the next 10 days? Or we could do 21 days if you guys like that. So all right, if I ask, how many do I infect in the next 10 days? Now, I'm assuming that I stay alive. But let's say, assuming I stay alive, how many do I infect over the next 10 days? That's going to be distributed as-- that is Poisson. But the question you're asking is a different one. You're asking, what is going to be the distribution of the total number of new infections that I cause? And this is precisely the same situation that we've analyzed lots and lots of times. What does it look like? AUDIENCE: Geometric distribution. PROFESSOR: Hmm? AUDIENCE: Geometric. PROFESSOR: OK, yes. It's going to be a geometric distribution. But why? AUDIENCE: Well, because you can have an infection and then another infection. And so then, it's, like, multiples of ten. PROFESSOR: That's right. So we have an infected individual. There's two things that can happen. He's going to die at some rate. And there's this other rate, which is going to go as beta times x or so, telling us about the rate of new infections. And we want to know, how many times do we go around this loop before we degrade, or die, or something, disappear from the population? Does this look at all familiar?**

9

|**AUDIENCE:**|**Mm-hmm.**|
|---|---|
|**PROFESSOR:**|**All right. Were you guys the same students that were here for the first half of the**<br>**class?**|
|**AUDIENCE:**|**Ha.**|
|**PROFESSOR:**|**Yeah? No.**|
|**AUDIENCE:**|**And so, R0 is like the [INAUDIBLE]? It's like the number of--**|
|**AUDIENCE:**|**It's the mean number for bursts.**|
|**AUDIENCE:**|**You haven't evaluated when the population--**|
|**PROFESSOR:**|**So R0 is the mean size of protein bursts, in the context of this other model, which**<br>**was-- what was the situation? And this one's a really good one for you guys to**<br>**know. It's going to be useful. So we saw this exact model in the context of gene**<br>**expression. And what was the situation that we--**|
|**AUDIENCE:**|**Production of [INAUDIBLE].**|
|**PROFESSOR:**|**Production of--**|
|**AUDIENCE:**|**--proteins from a single mRNA.**|
|**PROFESSOR:**|**Yeah, the production of proteins from a single mRNA. Right? Because remember,**<br>**we had this thing where we had the mRNA. And we said, oh, well the mRNA is going**<br>**to be degraded at some rate. But also, it's going to be translated at some rate. So**<br>**the distribution number of times that it's translated before it degrades is going to be**<br>**geometric. Because we go around this loop some number of times. All right, so this**<br>**is the same thing.**|
||**And the paper that I put as supplementary reading, by Jamie Lloyd-Smith? I always**<br>**get his name and Jamie Lloyd Wright-- right? Something-- mixed up. But yeah,**<br>**Jamie Lloyd-Smith. Smith. So he was studying the dynamics of infections when you**|


10

**have this thing where there's intrinsic variation in, say, the infectivity of an individual. Because here, you get this geometric distribution, even though all the individuals are, in principal, identical.**

**Now, the question is, if there's some distributions of, say, infectivities, then you'll get an even broader distribution of resulting number of new infections. So there's this classic thing of Typhoid Mary. She's was a nurse-- OK, now I don't remember the story. Yeah?**

**AUDIENCE: She was a cook.**

**PROFESSOR: A cook. Oh, a cook, nurse-AUDIENCE: [INAUDIBLE] so she cooked for a lot of people. PROFESSOR: OK, so she was somehow resistant to typhoid. But then, she was cooking for other people and, so then, caused a bunch of infections. Is that--? OK. Yeah, so this would be an example of a very infective individual that's beyond the assumptions in this model. And as you can imagine, if you have variations in this infectivity, then what it does, for a given R0-- so if you fix R0, then you have a broader distribution of infectivity. What it means is that a larger fraction of the infections will go extinct. But those that get going will be explosive. If you're curious about these sorts of ideas, you should look at this optional reading paper that I put out there. All right, so I just want to be clear. This is geometric number of new infections, distribution of new infections. Yes? AUDIENCE: So is this just one cycle? Like, one-PROFESSOR: So we're talking about the number of infections that result when you just add one infected individual to the population. AUDIENCE: OK, so then, you don't think about, afterwards, what happens to those infected individuals and if they infect--**

11

**PROFESSOR: Well, we are not yet thinking about them. Although, in this case, those are also geometrically distributed. But what you expect is that the mean of those things will change. Because the number of susceptible or whatnot individuals-- that's going to change. So the mean number is going to change. But the distributions will still be geometric.**

**AUDIENCE: But in total, that won't be geometric anymore. Because if we're looking at the total number of infected individuals after learning about the geometric-PROFESSOR: No. So just because each of these sub-steps is geometric does not mean that you end up with a geometric distribution. Indeed, let's say that i put in 20 infected individuals into the population. And I ask, what's going to be the distribution of the number of infections caused immediately from those 20? That's going to be what? [INTERPOSING VOICES]**

**Yeah, and for 20, it's going to be basically Gaussian. OK, well if I said 100, well definitely Gaussian. It's a gamma distribution that looks very much look a Gaussian, in that case. All right? All right. So we've been talking about the definition of this R0. But of course, we should figure out what it is.**

**We want R0 is equal to-- and what I'm going to tell you is that there's a 1 over u plus v. But then, there's some other terms. And I've unfortunately lost my notes. So you guys are going to have to help me figure this out. And what you're going to do is you're going to take advantage of your cards.**

**And again, put things in the numerators and the denominators, corresponding to how I'm supposed to fill out this equation. You can start thinking about it while I give you the options.**

**OK. So I guess you could recapitulate this by just putting B and C, although maybe you need it more than once. Do what you will. Do you understand the question? There's going to be something else I'm going to put right here. And I want to know-there are going to be somethings in the numerator, somethings in the denominator. I'm going to give you 30 seconds to think about it. Because it's important to be able**

12

**to reason your way through this.**

**All right, do need more time? Yep, OK. I'll give you another 15 seconds. All right, let's go ahead and vote. Ready? Three, two, one. All right. I like it! We're really looking quite nice. So there's a claim that it's going to be AD over B. We should be writing a beta k over u. All right.**

**Can somebody explain how they got there? Yes, please.**

**AUDIENCE: Well, it's going to be-- these two--**

**PROFESSOR: OK, yeah. This helped, right? OK, good, perfect. So this thing is what? What is this term here?**

**AUDIENCE: That's the death rate.**

**PROFESSOR: Right. Which means that the one over it is the expected lifetime of an infected individual. So the definition of R0 is, you put an infected individual into a population of susceptibles. Now, we want to know, OK, well there's a expected lifetime of this infected individual, which is given by this.**

**And then, we have to think about, well, what's the rate that we're going to be infecting individuals? And that's going to be beta times x. But what we want to know is, is x before we add any infection? And without any infection, then we just have a rate of entry and, then, a death rate. So it's just k over u. OK?**

**Now, the key thing in all of these epidemiological models is whether this R0 is greater or less than 1. And that's going to tell us whether the disease becomes endemic or not, whether, at steady state, we have a population of infected individuals. So R0, greater than one, means it's in an endemic population.**

**Now, in this model, we can then ask--**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[LAUGHTER] →](03-laughter.md)
