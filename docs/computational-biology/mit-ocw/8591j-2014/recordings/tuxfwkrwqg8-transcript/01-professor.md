---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/tuxfwkrwqg8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/tuxfwkrwqg8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So today, the general theme is going to be to try to understand how bacteria find food. And in particular, how do they know which direction to swim? How do they swim given that they're operating in this low Reynolds number regime that you read about maybe last night? What did you guys think of the life in low Reynolds number?**

**Yeah, it's kind of fun. You very much get the impression that you are kind of there in that lecture hall with him. They do say that some essential arm waving was not reproduced or so, right? But you kind of imagine his arms waving as he talks, even though you don't get to hear him talk.**

**So that's fun. And it's a surprising number of typos given that-- every time I read that, I'm like, somehow this is still the best version that I've been able find of that talk. But I think it's just a neat example of how clearly a talented physicist can kind of from a naive perspective say interesting things about the way that life has to work.**

**Now today, so we will be talking indeed about how bacteria are swimming. But we want to start by just making sure we understand something about how diffusion works, what life is like in this low Reynolds number regime. And for these sorts of problems, it's really very, very valuable if you can just apply some simple dimensional analysis ideas. And so we're going to practice that in a few different cases, that dimension analysis can often tell you a great deal.**

**In many cases, you can discover new physical laws. You can figure out how things have to scale. And in some cases, the scalings are rather surprising. And given some of the constraints that microscopic life is facing in this low Reynolds number regime where diffusion is very important, viscous forces are dominating over these**

1

**inertial forces, it really constrains what bacteria, for example, are able to do. And it really constrains how they have to go about solving the challenges of life.**

**So what I want to do is start by thinking about just a very kind of simple situation, which is we have in, we'll say water, a non-permeable membrane that is separating two compartments. Whereas over here, we have maybe salt or something on the right. So this is a salty solution. And this is pure water.**

**Now, this is a non-permeable membrane. So it doesn't allow the salt to cross. But the question is, what happens if I puncture, and I put a little hole in the membrane of some radius a, let's say? Now, the question is, what will be the flow rate, the net flow, of salt, in this case, from the right to the left?**

**All right, so first of all, can somebody kind of answer at least for a couple-- what are possible things that might be relevant if we're going to try to figure this out? What quantities will we need to know or measure?**

**AUDIENCE: Concentration.**

**PROFESSOR: Concentration seems relevant, yeah. And in this case, there's only one concentration. Because well, this conservation is 0 here, and some concentration c over here. What else might we need to know?**

**AUDIENCE: Pore size.**

**PROFESSOR: The pore size, perfect. We'll use a as the radius of the pore. And is that going to do it?**

**AUDIENCE: You need a time for something.**

**PROFESSOR: We need a time. Because what we want is some number of molecules per unit time that is going to be crossing from the right to the left. So we need something that has a time. Yes.**

**AUDIENCE: The diffusivity.**

2

**PROFESSOR: All right, the diffusivity. So D, so we'll say D, which is the diffusion coefficient. How many S's? All right, now other things that might be relevant?**

**AUDIENCE: Temperature PROFESSOR: Temperature, OK. AUDIENCE: I guess it's probably going to be incorporated into the [INAUDIBLE] PROFESSOR: Exactly, right, so indeed the flow rate will be dependent upon the temperature. But the way that that manifests is by doing what to D? In general, if we go up to higher temperature, how will D change? AUDIENCE: Should get bigger. PROFESSOR: Should get bigger, yeah, so indeed, D will be typically given by this Einstein relation of kT over gamma. We'll talk more about this in a little bit. But for now, let's just say that D is something that we've measured. Now, other things that may enter into the expression? All right, so this is pretty simple. We have three things. Now, the question is, if we double the size of the pore, i.e. if we double a, how does the flow rate change? So we'll go ahead and do a vote, since we like to do this. All right, so we double a. The flow goes up by what factor? All right, maybe not all. All right, and if you think it's something else, you can splay your cards out. Now, the idea here is that using dimensional analysis, we should be able to figure this out. Now, I'll give you just a minute to try to think through this. AUDIENCE: [INAUDIBLE]**

**PROFESSOR: All right, so you don't even need to know this in principle. I'm going to give you something else that may help. AUDIENCE: Will it be by x? PROFESSOR: Yeah, so this is the mean squared distance that something will diffuse. So I wasn't**

3

**explaining, because I was sort of-- a hint in the sense that in case you might remember something like an equation like-- Yes. AUDIENCE: Are we doing this at the very beginning of-PROFESSOR: Yes, right, OK, so there's going to be some question of timescales here. OK, so it's really that after you puncture the hole, very rapidly it's going to assume some kind of steady state. And then the flow rate will be constant for some rather long time. But then eventually the concentration on this half will decrease. So we're thinking about the flow rate after you've reached that steady state, but before you've equilibrated across the two sides of the tube. All right, do you need more time? All right, let's go ahead and see where we are. Ready-- three, two, one. All right, so we have a pretty good agreement. It seems that it's D. But didn't I tell you how to do the problem already? OK, so it's not-AUDIENCE: So the naive thing, I guess, would be C. Because-- oh, sorry, never mind. Except for-- [INAUDIBLE] PROFESSOR: All right, so I'm going to give you another-- collaborate with a neighbor. And I'll tell you that it's not D to nudge you in the right direction. So spend a minute. [INTERPOSING VOICES]**

**PROFESSOR: All right, let's go ahead and reconvene. All right, I just want to see where we are now. So if you still believe it's D despite my telling you that I don't think it's D, you can still vote D, and then we can argue about it. And that's fine, too. All right, ready-- three, two, one. OK, so now there's maybe a disagreement between A and C now. All right, well, nobody liked my root 2? Maybe you saw me hesitate a little bit before I wrote it. I was like, oh, let me throw in a root. So indeed the flow rate does not scale as the area. It only scales with a linear dimension of this hole. This is weird, which is why everybody says D. And even after**

4

**you've done this problem, you still think it's D in your intuition. But you have to like pound that intuition away from you. We'll try to understand in multiple different ways why this might be. But what I want to do first is just make sure that we understand from dimensional analysis why this has to be the case.**

**Now, the first thing you need to know for dimensional analysis is the units of your answer. We're looking for something that is going to be units, some number of molecules over time. Number-- there's no units attached to that. So the answer is supposed to be just 1 over time.**

**Indeed, this is why we needed something that had some unit of time somewhere in order to get an answer that could possibly do this. And indeed, we know that the diffusion coefficient has units of, for example, microns squared per second. So it's a length squared over time.**

**Now, the one barrier that people have to use dimensional analysis is because we have trouble remembering what the units of things are. So if you don't remember something like the units of a diffusion coefficient, then what you have to do is try to find some equation in your brain where that symbol is used. And of course it should be the correct use of the symbol.**

**So here this is why I'm saying it. This is essentially the definition of this linear diffusion coefficient. And from that, you get the units. This is just very, very common. Something like viscosity, impossible to remember what the units of that thing are. But then you just have equations in your brain where the viscosity enters, and you can figure it out.**

**All right, so then if you want to use this dimensional analysis study, just be very clear. Write down what all the dimensions are. And then the answer just comes screaming out at you in general. Now, we see that we want something 1 over time. There's only one of these symbols that has a time in there. So we know exactly how the diffusion coefficient has to enter.**

**We know that the flow is going to have to be something where we know that D has**

5

**to enter in there linearly. Because if it was any other way, then the time would have some weird units. It would be time squared or square root of time or something.**

**Now, it's true that we could in principle dream up something crazy between concentration and the pore size in the sense that if we wanted to, we could do c times-- we could always add a c times a cubed or something like that. But of course this is diffusion.**

**What that means is that these are non-interacting diffusing molecules. That means that if we double the number of the molecules over on the right hand side, we have to double the flow rate in this diffusion equation. And for diffusion, these molecules are not interacting at all. They don't see each other. And that means if you just double the concentration on the right, you have to double the flow rate.**

**So that means we know that it has to show up as a single c. And all we're left with is going to be one unit of length that we have to get rid of. Now, this is not, of course, a rigorous definition. And does this have to be actually an equal sign? No, so what we can actually say is that it has to be proportional to this. But actually just from dimensional analysis and this idea of, say, superposition of the concentrations, you can get something that's really kind of a deep statement about how diffusion is going to operate. Yes.**

**AUDIENCE: It seems to me that we can break that. There's this degeneracy. We can't quite sort out the powers of c and a, right?**

**PROFESSOR: Right, so that's what I was saying, that just from the units alone, we could always add a c times a cubed, or to some power. And that's why I'm saying that you have to be able to invoke this idea that if you double the concentration of the salt on the right, you'll double the flow rate. Because these are non-interacting molecules. Because they're just diffusing around in solution.**

**AUDIENCE: I was going to say that if we simply chose the measure of flow in 90 units of number of atoms, but in units of mass per unit time, and concentration in units of mass per unit time, then we would clearly see what power of c it would be. And it would have**

6

**to be 1.**

**PROFESSOR: It's an interesting-- I think I'm going to disagree with you. But I want to make sure that I-- so you want to say, OK, you're entering. Yeah, the diffusion coefficient is about what the molecule is doing. So I'm not sure how we're going to-- if we measure concentration in units of, you're saying, mgs per mil of some protein, or so, then you're really saying that there's some mass density. And I guess you can always define diffusion coefficient, even from the standpoint of- because we don't even need numbers. We can measure some fluorescence or something of how it diffuses across. So that doesn't require numbers. Yeah, I'm trying to think if this is going to end up being different from the argument. I'd have to-AUDIENCE: If we put in the number of molecules, then it's going to have to be number of molecules per time. And then c has to be linear. Because c is number of molecules per something, right? PROFESSOR: OK, yeah, you could, say, treat molecules as a unit. And then that also ends up requiring that it's-- yeah, no, I think that's fair. But I'd have to think about this, how it would play out if you try to measure things in terms of mass per unit volume. Of course, you should be able to calculate this explicitly, and then also to figure out what the proportionality constant is. But indeed, what you find is that it scales linearly with the radius instead of as the area, which is, I think, very surprising. Yes. AUDIENCE: We can also say D scales with a squared times flow.**

**PROFESSOR: Oh, you're saying that maybe the concentration is not relevant. AUDIENCE: If we look at it that way, then the answer is D. PROFESSOR: OK, what you're saying is that maybe somehow the flow is just equal to or proportional. It goes as D times a squared in the sense that you would say that--**

7

**AUDIENCE: Over. Over.**

**PROFESSOR: Right, I think that this non-interacting particle business really does tell you that the flow has to be proportional to the concentration. And yeah, I think that is sufficient already. I agree that just from units, you could do this. But I think, well, it's not true, and it's nonsensical. And it's not proportional to c.**

**Let's move on. But I think it's important that it's possible to say something that's a deep kind of physical principle just based on analysis of the units. And then, of course, can somebody offer the intuitive explanation for why this might be? Why is it that it goes as a instead of a squared?**

**And this is a little bit weird given the fact that we all check our intuition, we all say D. But the thing is, once you know an answer, you should still try to figure out what the intuition might have been that you missed when you originally said D. Yes.**

**AUDIENCE: OK, this might not make any sense. So say you would first think it goes like a squared, because the area goes like a squared. But then maybe the fact that the perimeter grows like a, and the perimeter adds drag, maybe that would subtract from or cancel out any-- not necessarily make sense?**

**PROFESSOR: Yeah, well, OK, so I don't think that's the intuition that I would use. But then we have to figure out, OK, what might be wrong? Well first, I don't think you can subtract an a. But also we haven't invoked any actual drag in the sense that there's no sense that the perimeter should be-- right?**

**All right, so this is so mysterious that we are-- that's fine. So the way that I like to think about this is that it's not that we're shooting bullets at this membrane. If we were shooting bullets, or if these were raindrops coming, then indeed it would scale as the area.**

**But because it's diffusion, diffusion operates on gradients of concentration. And what's happening here is that you get a local depletion of the concentration at the pore. So it's not the case that you have concentration c all the way until you get to**

8

**the pore, and then all of a sudden you have a linear gradient of c across that little pore, but rather that you have a depletion of the concentration as you approach the pore. And so as you grow the pore, you're somehow competing with yourself.**

**Another way to think about this is to think about what happens if we have two pores. For example, let's imagine that we have this poor here of size a. But now I'm going to add a second pore over here far away, same size. What should this do to the total flow rate, A, B, C, D, E? I'll give you 10 seconds to come up with an opinion. So I'm adding a second pore far away. Ready? Three, two, one-- all right, so we're all agreeing. And this should be 2x, again.**

**This is for two pores now. We also get 2x. This is because if the two pores are far away from each other, as relative to the size of the pores, then these are really noninteracting in the sense that there's none of this depletion effect that I was telling you about.**

**Whereas as we bring these pores together, then they start interfering with each other. Because they each involve some local depletion of the concentration. And once that kind of depletion area starts to overlap, then the point is that there is some molecule that was diffusing. And if you have the pores right next to each other, you're not going to get twice the net flow. Because that molecule, it might have diffused through the other pore even if it-- if one pore were not there, then it might have diffused through the other pore.**

**AUDIENCE: Can you not think of it as having to do with the fact that under a random walk, the displacement goes like square root of the time? So if you increase the number of molecules going through by the square of the perimeter, then actually be like total molecule displacement through [INAUDIBLE] will only go linearly in that perimeter, which would account for the fact that molecule is coming back across.**

**PROFESSOR: Right, so it's true that the molecules coming back across you always have to worry about. But I don't see this argument actually necessarily in my work.**

**AUDIENCE: Maybe in the case of, like [INAUDIBLE] which doubled in size.**

9

**PROFESSOR: Oh, I see. Yeah, I think that it may be connected, although I'm not sure if I'm sold on the argument. Yeah, I think it's a little bit dangerous. Yeah. AUDIENCE: So you mentioned you appeal to some sort of depletion with that. But if you just punctured a hole in the-PROFESSOR: OK, and this is why there is this question of timescale. Immediately after you puncture the hole, then the flow rate will actually be higher than it will be at that steady state. AUDIENCE: So it's going to be a squared. PROFESSOR: Yeah, right, I think that the flow right after you puncture it indeed will scale as a squared. Because what you're doing is you're taking the number of molecules across this area. And half of them are going to come through. And there's just more molecules in that area when you first puncture it. But that's going to equilibrate in, whatever, a microsecond. That'll be really fast. Whereas in the steady state flow rate, that could go in principle forever if it's a large reservoir. OK, so I want to move on. But I want to make sure that we understand how this basic principle allows us to say some interesting things. For example, there's a related problem, which is, how much food could a cell possibly eat? And can somebody say why there might be an upper bound on this?**

**AUDIENCE: There's a point at which you get too many nutrients inside of the cell. PROFESSOR: I'm sorry? AUDIENCE: There's a point at which you get too many nutrients inside of the cell. PROFESSOR: Oh no, this is a super hungry cell. It can in principle be able to use every glucose molecule that came in. AUDIENCE: No, but I'm saying that the osmosis of the water coming in would pop the membrane.**

10

**PROFESSOR: Oh, OK, we're talking about osmotic effects. OK, yeah, but we can just say that it's got a super tough cell wall. So it can take, we'll say, infinite. I guess what I'm saying is there's something. Even if I invoke such a thing, there still is a limit. That's really what I'm trying to say.**

- **AUDIENCE: The concentration of the glucose inside the cell is a bit high. PROFESSOR: Well, the glucose is going to get imported. And then it's going to be immediately converted into useful things. But then still there's a limit. There's a maximum. This is the maximum kind of possible nutrient uptake. Yes.**

- **AUDIENCE: If the diffusion is somewhat slow, or maybe there's [INAUDIBLE] around the cell. PROFESSOR: OK, right, so maybe it could be somehow diffusion limited. And what's the best that a cell could possibly do in this regard? So here's a cell. And now maybe we will, again, have it be radius a. So this is the cell of radius a. The best they can be, how would you describe that relative to diffusion?**

- **AUDIENCE: Can you be more specific?**

**AUDIENCE: Everything that [INAUDIBLE] membrane could be absorbed. PROFESSOR: That's right. So that's what I was-- so the best that it could possibly be is a perfect absorber. What we mean by that is something where the moment that a molecule touches it, it gets imported. Now of course, a cell is not a perfect absorber. But what's fascinating is that even if it were, then it does not mean that it's going to be consuming, say, glucose at an infinite rate.**

**And particularly, we can ask, well, if we have a situation like this where we have a cell, a sphere of size a, it's a perfect absorber, how will its uptake rate scale with its size? In particular, if we double a, what is it going to do for the flow? All right, we're going to have 10 seconds to think about this.**

**If we imagine a cell as a perfect absorber, the moment that this nutrient touches it, it gets imported and chewed up. The question is, how does that maximum uptake rate**

11

**change if I double the size of the cell, double the radius? Are we ready? OK, let's see where we are. Ready? Three, two, one.**

**OK, so now it's a bit more of a mixture of A's, C's, D's, although it is a majority. We're getting a majority C. And again, this is, cell doubles size.**

**And indeed, from the standpoint of dimensional analysis, this is the same problem as that pore that we just did. Because again, it's diffusion. We're interested in uptake. Now, it's not flow across a membrane. But this is uptake rate by the cell. It's going to be numbers of molecules per unit time.**

**Again, there's diffusion. The concentration is still relevant. And so all the same arguments apply. And indeed, this is, again, proportional to the radius a. And remember, we're following the convention of Purcell and calling this a. Because Reynolds numbers is an r, and then problems arise. Are there any questions about why the argument is the same here as it was there?**

**OK, now, there's something interesting about this though, which is that you can imagine the fact that this only scales as the radius of the cell tells you that there's some sense in which we're wasting an awful lot of that surface area. Because we have this large surface area.**

**But it's not as good as you would have thought it would have been. And what that means is in principle, you could have a smaller fraction of the area covered by a bunch of little pores or transporters that are kind of analogous to this situation that we had before with the salt crossing the membrane.**

**And indeed, if you just imagine that these are each little absorbing patches that are perhaps one nanometer in size, small, there's an amusing calculation you can do, which is you can ask, well, how is it that the-- this is now uptake rate. We want to know, how is it that that is going to change as a function of the fraction of the surface area that we have covered with these transporters, with these little perfectly absorbing patches?**

**So we imagine the cell is 1 to 10 microns in size. Now we have a bunch of these**

12

**little pores that we're going to go on. And of course, this is going to saturate somewhere. And it's going to saturate. And as it turns out, this goes as 4 pi D, I think. Yeah, so the uptake rate is actually equal to 4 pi cDa for a sphere.**

**So this is the part that we could not have figured out from dimensional analysis. So indeed, the uptake rate, once we get up to-- this is a fraction that's covered. Once that's 1, indeed it's going to be 4 pi cDa. Now, the question is, how does it behave over here?**

**Now, you might have thought that it would just be some line like that. It's just the more of these transporters that you have, you just get a linear increase in your total uptake rate. But it turns out that that's not true. Because even at just having, say, 1%, roughly, of the surface covered by this transporter, you can get something like 50% of the total maximal uptake rate. And that's because these guys are not competing with each other so much, because they're far away. So this curve really looks something like-- well, OK?**

**Now, this is, I think, especially interesting. Because a cell is not trying to import just one thing. In principle, it's trying to import many different things. So you need carbon sources. You need all sorts of trace metals. You need nitrogen.**

**So in principle, there are many, many, many things that a cell is trying to get from the environment. And by simply having different transporters specific to different things-- all right, so here are some squares that uptake something else, and little, I don't know, triangles, whatever. So you can have many, many, many of these different transporters on the cell surface. And they're each uptaking their own thing.**

**And kind of surprisingly, you can get near optimal uptake rates of many, many different things. I feel that I've lost you. Somebody ask a question. Yes.**

**AUDIENCE: So this [INAUDIBLE], is it really proportional to the actual surface area covered?**

**PROFESSOR: Right, so this initial thing, this increases linearly for small areas. Because just like what we said before, if you had these two little holes in the membrane that are far away from each other, then they don't compete. What that means is that you do get**

13

---

[Up: contents](index.md) · [an initial linear increase here. →](02-an-initial-linear-increase-here.md)
